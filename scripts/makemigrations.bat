@echo off
call %cd%/scripts/envs.bat
python3 manage.py makemigrations

