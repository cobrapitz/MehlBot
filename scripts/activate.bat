@echo off

@REM On windows the poetry shell command doesn't have
@REM a history function (arrow up/down) and it seems there isn't
@REM a method to activate the env in any (simple) other way.

for /f %%a in ('poetry env info -p') do (
    %%a\Scripts\activate.bat
)
