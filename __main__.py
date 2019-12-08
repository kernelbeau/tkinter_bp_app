"""Main entry point for this app.

From command line: "$ python ." to start
"""
from src.app import AppCtrl


def main():
    app = AppCtrl()
    app.start()


if __name__ == '__main__':
    main()
