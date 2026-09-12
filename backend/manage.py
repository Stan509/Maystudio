import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maystudio_api.settings')

    try:
        from fix_db import prepare_database
        prepare_database()
    except Exception as e:
        print("Notice (manage.py prep):", e)

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)



if __name__ == '__main__':
    main()
