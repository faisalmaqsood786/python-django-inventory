@echo off
call %cd%/scripts/envs.bat
python3 manage.py runserver 0.0.0.0:8000
