from sys import argv
from flask_script import Server, Manager

from homebank.app import make_app


def manage():
    if len(argv) == 1:
        argv.extend(["runserver", "-r", "-d"])

    manager = Manager(make_app(
        debug='-D' not in argv and '--no-debug' not in argv))
    manager.add_command("runserver", Server(host="0.0.0.0", port=8080))

    return manager.run()


if __name__ == "__main__":
    manage()
