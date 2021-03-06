from server import api
from server.models import SessionManager
from server.models.htb import HTBResult
from server.views.auth_view import token_authentication


@api.route('/api/htb/ranking')
class HTBRankingView:
    def on_get(self, req, resp):
        is_auth, message = token_authentication(req.headers)
        if not is_auth:
            resp.media = {'message': message}
            resp.status_code = api.status_codes.HTTP_403
            return

        with SessionManager() as session:
            scores = session.query(HTBResult).order_by(HTBResult.score).all()
            scores.reverse()

        N = min(10, len(scores))
        resp.media = {
            'message': message ,
            'scores': [s.serialize() for s in scores[:N]]
        }
        resp.status_code = api.status_codes.HTTP_200

    async def on_post(self, req, resp):
        is_auth, message = token_authentication(req.headers)
        if not is_auth:
            resp.media = {'message': message}
            resp.status_code = api.status_codes.HTTP_403
            return

        data = await req.media()

        if 'player_name' not in data.keys() or 'score' not in data.keys():
            resp.media = {
                'message': 'the paramator is not found:{}{} .'.format(
                    int('player_name' not in data.keys()) * ' `player_name`',
                    int('score' not in data.keys()) * ' `score`'
                )
            }
            resp.status_code = api.status_codes.HTTP_400
        else:
            try:
                score = int(data['score'])
            except ValueError:
                resp.media = {'message': 'Is the `score` numeric ?'}
                resp.status_code = api.status_codes.HTTP_400
                return

            result = HTBResult(
                player_name=data['player_name'],
                score=score
            )

            with SessionManager() as session:
                session.add(result)
                session.commit()

            resp.media = {'message': 'Good Request .'}
            resp.status_code = api.status_codes.HTTP_201
