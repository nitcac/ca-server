from server import api
from server.models import Base, engine


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    api.run(address='0.0.0.0', port=80)
