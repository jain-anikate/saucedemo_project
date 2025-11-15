@echo off
echo ===============================================
echo   SauceDemo Pytest Automation - Auto Setup Run
echo ===============================================

cd /d %~dp0

REM Create venv if it does not exist
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate venv
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip and tools
echo Upgrading pip, setuptools, wheel...
python -m pip install --upgrade pip setuptools wheel

REM Install project dependencies
echo Installing dependencies from requirements.txt...
python -m pip install -r requirements.txt

echo Running tests...
python -m pytest -m "success or failed or extract" --html=reports\report.html --self-contained-html -q
set EXITCODE=%ERRORLEVEL%

if exist reports\report.html (
    if not exist reports\archive mkdir reports\archive
    powershell -Command "Copy-Item 'reports\\report.html' 'reports\\archive\\report_$(Get-Date -Format yyyyMMdd_HHmmss).html'"
    echo Report generated at reports\report.html
) else (
    echo No report generated. pytest failed.
)

pause
exit /b %EXITCODE%
