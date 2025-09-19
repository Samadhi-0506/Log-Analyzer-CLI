# 🛠️ Log Analyzer CLI Tool

A simple Python CLI tool to analyze Nginx logs, extract error messages, and export them to CSV reports. Designed for beginners.

------

## ✨ Features

- 🔍 Analyze Nginx logs and extract error messages
- 📄 Export errors to a clean CSV report
- ⏰ Schedule automatic analysis every N minutes
- 🧠 Beginner-friendly CLI with `click`
- 📁 Organized folders for logs and reports


---

## 📦 Installation
```bash
# Clone the repo
git clone https://github.com/Samadhi-0506/Log-Analyzer-CLI
cd log-analyzer-cli

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  

# Install dependencies
pip install -r requirements.txt

#Analyze logs manually
python3 log_analyzer.py analyze --logfile logs/access.log

#Schedule periodic analysis
python3 log_analyzer.py schedule-report --interval 2 --logfile logs/access.log


   📊 Output
   CSV report saved to reports/error_report.csv
