#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')
    
    # ----------------------------------------------------
    # Custom Host and Port Configuration
    # ----------------------------------------------------
    DEFAULT_HOST = '0.0.0.0'  # Change to '0.0.0.0' to allow network access
    DEFAULT_PORT = '80'       # Change to your desired port
    
    # If the user is running the development server
    if len(sys.argv) > 1 and sys.argv[1] == 'runserver':
        # Check if the user already provided an explicit host/port in the terminal
        # (This prevents your default from overriding a manual override)
        has_custom_address = any(':' in arg or arg.isdigit() for arg in sys.argv[2:])
        
        if not has_custom_address:
            sys.argv.append(f"{DEFAULT_HOST}:{DEFAULT_PORT}")
    # ----------------------------------------------------
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

