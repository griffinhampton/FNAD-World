@echo off
REM FNAD World Game Launcher for Windows
REM This script sets up the environment and launches the game

echo Starting FNAD World...
echo Setting up Python path...

set PYTHONPATH=%CD%
call .venv\Scripts\python.exe main.py

echo Game exited.
pause