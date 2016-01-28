#!/usr/bin/env python3

"""
This is an application management application that allows to run the server.
"""

from flask_script import Manager

from server.app import app

manager = Manager(app)


if __name__ == '__main__':
    manager.run()
