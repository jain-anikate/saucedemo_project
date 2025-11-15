@echo off
echo ===============================================
echo   SauceDemo Pytest Automation - Robust Runner
echo ===============================================

REM Ensure script runs from its own folder
cd /d %~dp0

REM Create venv if missing
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
    if ERRORLEVEL 1 (
        echo Failed to create virtual environment. Ensure Python 3.8+ is installed and on PATH.
        pause
        exit /b 1
    )
)

REM Activate venv
echo Activating virtual environment...
call venv\Scripts\activate.bat
if ERRORLEVEL 1 (
    echo Failed to activate virtual environment.
    pause
    exit /b 1
)

REM Upgrade pip and tools
echo Upgrading pip, setuptools, wheel...
python -m pip install --upgrade pip setuptools wheel
if ERRORLEVEL 1 (
    echo pip upgrade failed. Check network/proxy and try again.
    pause
    exit /b 1
)

REM Install dependencies
echo Installing dependencies from requirements.txt...
python -m pip install -r requirements.txt
if ERRORLEVEL 1 (
    echo pip install failed. Check the output for details (network/proxy or permissions).
    pause
    exit /b 1
)

echo.
echo -------------------------------
echo Running tests now...
echo -------------------------------

REM Use python -m pytest to avoid PATH issues
python -m pytest -m "success or failed or extract" --html=reports\report.html --self-contained-html -q
set EXITCODE=%ERRORLEVEL%

REM Archive report if created
if exist reports\report.html (
    if not exist reports\archive (
        mkdir reports\archive
    )
    powershell -Command "Copy-Item -Path 'reports\\report.html' -Destination 'reports\\archive\\report_$(Get-Date -Format yyyyMMdd_HHmmss).html'"
    echo Report generated at reports\report.html
) else (
    echo No report generated (pytest likely failed). Check test output above.
)

if %EXITCODE% NEQ 0 (
    echo Some tests failed. Exit code: %EXITCODE%
) else (
    echo All tests completed successfully.
)

pause
exit /b %EXITCODE%
