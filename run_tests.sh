
#!/usr/bin/env bash
python -m pytest -m "success or failed or extract" --html=reports/report.html --self-contained-html -q
mkdir -p reports/archive
cp reports/report.html reports/archive/report_$(date +%s).html
echo "Report generated: reports/report.html"
