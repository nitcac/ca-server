from server import api
from server.models import SessionManager
from server.models.htb import HTBResult

import json


@api.route('/api/htb/ranking')
class HTBRankingView:
    def on_get(self, req, resp):
        with SessionManager() as session:
            scores = session.query(HTBResult).order_by(HTBResult.score).all()
            scores.reverse()

        N = min(10, len(scores))
            
        resp.media = {'scores': [s.serialize() for s in scores[:N]]}
        resp.status_code = api.status_codes.HTTP_200

    async def on_post(self, req, resp):
        try:
            data = await req.media()
        except json.decoder.JSONDecodeError:
            data = {}

        if 'player_name' in data.keys() and 'score' not in data.keys() and data['score'].isdecimal():
            score = int(data['score'])
            result = HTBResult(
                player_name=data['player_name'],
                score=score
            )

            with SessionManager() as session:
                session.add(result)
                session.commit()

                scores = session.query(HTBResult).order_by(HTBResult.score).all()
                scores.reverse()

            N = min(10, len(scores))
            
            resp.media = {'scores': [s.serialize() for s in scores[:N]]}
            resp.status_code = api.status_codes.HTTP_201

        else:
            resp.media = {'message': 'Invalid request body'}
            resp.status_code = api.status_codes.HTTP_400
