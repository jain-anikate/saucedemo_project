
@echo off
if exist venv\Scripts\activate.bat (
  call venv\Scripts\activate.bat
)

pytest -m "success or failed or extract" --html=reports\report.html --self-contained-html -q

if %ERRORLEVEL% neq 0 (
  echo Some tests failed.
) else (
  echo All tests finished.
)

powershell -Command "if(-not(Test-Path -Path 'reports\\archive')){ New-Item -ItemType Directory -Path 'reports\\archive' | Out-Null }; Copy-Item -Path 'reports\\report.html' -Destination 'reports\\archive\\report_%((Get-Date).ToString(\"yyyyMMdd_HHmmss\")).html'"
echo Report generated at reports\report.html
pause
