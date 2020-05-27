import sys
from FlaskService import flask_server


def main():
    flask_server.start()


if __name__ == '__main__':
    sys.exit(main())
