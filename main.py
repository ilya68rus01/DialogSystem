import sys
from FlaskService.flask_server import Server


def main():
    server = Server()
    server.start()


if __name__ == '__main__':
    sys.exit(main())
