#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    # os.environ : 환경변수목록, 기본적으로 django사용 없으면 내 프로젝트(savanna)의 setting
    # django 기본 setting : https://github.com/django/django/blob/master/django/conf/global_settings.py
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'savanna.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
