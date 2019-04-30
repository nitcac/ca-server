from server import api
from server.util import decrypt_payload
from server.models import SessionManager
from server.models.auth import Token

import json
import base64
import secrets

from sqlalchemy.orm.exc import NoResultFound


@api.route('/api/auth/token')
def get_unique_token(req, resp):
    unique_token = secrets.token_hex()
    token = Token(unique_token=unique_token)

    with SessionManager() as session:
        session.add(token)
        session.commit()

    resp.media = {
        'token': unique_token
    }


@api.route('/api/auth')
class Authorization:
    def on_request(self, req, resp):
        # get params
        headers = req.headers

        if 'encrypted' not in headers.keys() or 'iv' not in headers.keys():
            resp.media = {
                'message': 'Bad Request: Invalid Header'
            }
            resp.status_code = api.status_codes.HTTP_400

        else:
            # get enc and iv
            encrypted = headers['encrypted']
            iv = headers['iv']

            text = decrypt_payload(encrypted, iv)

            # search message in  table
            with SessionManager() as session:
                try:
                    token = session.query().filter(Token.unique_token==text).one_or_none()
                except NoResultFound:
                    resp.media = {
                        'message': 'Bad Request: tokens conflicted'
                    }
                    resp.status_code = api.status_codes.HTTP_400
                    return 

            if token:
                token.authorized = True

                with SessionManager() as session:
                    session.add(token)
                    session.commit()

                resp.media = {
                    'message': 'Good Request'
                }
                resp.status_code = api.status_codes.HTTP_200
            else:
                resp.media = {
                    'message': 'Bad Request: Not found the token'
                }
                resp.status_code = api.status_codes.HTTP_400


def token_authentication(headers):
    if 'encrypted' not in headers.keys() or 'iv' not in headers.keys():
        message = 'invalid headers'
        return (False, message)
    else:
        # get enc and iv
        encrypted = headers['encrypted']
        iv = headers['iv']

        text = decrypt_payload(encrypted, iv)

        # search message in  table
        try:
            with SessionManager() as session:
                token = session.query().filter(Token.unique_token==text).once()
        except NoResultFound:
            message = 'invalid token'
            return (False, message)

        return (
            token.authorized,
            f"the token is{'' if token.authorized else ' not'} authorized"
        )
