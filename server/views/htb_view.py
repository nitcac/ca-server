from server import api
from server.models.htb import HTBResult
from server.models import SessionManager


@api.route('/api/htb/ranking')
class HTBRankingView:
    async def on_post(self, req, resp):
        data = await req.media()

        if 'player_name' in data.keys() and 'score' in data.keys():
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

        else:
            resp.media = {
                'message': 'the paramator is not found:{}{} .'.format(
                    int('player_name' not in data.keys()) * ' `player_name`',
                    int('score' not in data.keys()) * ' `score`'
                )
            }
            resp.status_code = api.status_codes.HTTP_400
