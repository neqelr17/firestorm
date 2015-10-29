# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import sys
import site
site.addsitedir(b'.')


def _get_env():
    '''Extracts the environment PYTHONPATH and appends the current sys.path to
    those.'''
    env = dict(os.environ)
    env[b'PYTHONPATH'] = os.pathsep.join(sys.path)
    return env


def set_environment():
    if 'site:dev' in sys.argv:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                              "web__django.settings.settings_dev")
        sys.argv.remove('site:dev')
    elif 'site:test' in sys.argv:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                              "web__django.settings.settings_test")
        sys.argv.remove('site:test')
    elif 'site:prod' in sys.argv:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                              "web__django.settings.settings_prod")
        sys.argv.remove('site:prod')
    elif 'pylint' in sys.argv:
        sys.argv.remove('pylint')
        os.environ.setdefault(b"DJANGO_SETTINGS_MODULE",
                              b"web__django.settings.settings_dev")
        # Start pylint
        # pip install pylint
        # pip install pylint-django
        # Ensure we use the python and pylint associated with the running epylint
        from pylint import lint as lint_mod
        from subprocess import Popen, PIPE
        parent_path = os.path.dirname(os.getcwd())
        child_path = os.path.basename(os.getcwd())
        lint_path = lint_mod.__file__
        cmd = [r'C:\Python27\python.exe', lint_path] + [
            '--msg-template', '{path}:{line}: {category} ({msg_id}, {symbol}, {obj}) {msg}',
            '--max-line-length=79', #'--disable=R,C,W',
            '--generated-members=objects,get,DoesNotExist', child_path]
        process = Popen(cmd, stdout=PIPE, cwd=parent_path, env=_get_env(),
                        universal_newlines=True)

        currently_saving = False
        rpt_data = []
        for line in process.stdout:
            line = line.strip()
            if line == 'Raw metrics':
                currently_saving = True
            if currently_saving:
                rpt_data.append(line)
            # remove pylintrc warning
            if line.startswith("No config file found"):
                continue

            print line

        process.wait()
        with open('bleh.txt', 'w') as ofstream:
            for line in rpt_data:
                ofstream.write(line + '\n')
        sys.exit()
    else:
        print sys.argv
        print 'exiting'
        sys.exit()


if __name__ == "__main__":
    if os.environ.get('DJANGO_SETTINGS_MODULE', None) == None:
        set_environment()
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
