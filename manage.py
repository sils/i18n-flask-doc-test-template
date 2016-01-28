#!/usr/bin/env python3

"""
This is an application management application that allows to run the server.
"""

from subprocess import call

from flask_script import Manager

from server.app import app

manager = Manager(app)


@manager.command
def coala(noninteractive=False):
    """
    Runs code analysis on the application.

    :param noninteractive: True if no interactions are to be done. (JSON
    output will be generated in this case.)
    :return: 0 if all is well.
    """
    if noninteractive:
        return call(['coala-format', '-S', 'format_str={origin}, {file}, from '
                                           '{line} to {end_line}. {message}'])
    else:
        return call('coala')


if __name__ == '__main__':
    manager.run()
