from server import api
from server.models.htb import HTBResult


@api.route('/api')
class HTBRankingView:
    async def on_post(self, req, resp):
        data = await req.media()
        response = {}

        resp.media = response
