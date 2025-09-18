# 🛠️ Log Analyzer CLI Tool

A simple Python CLI tool to analyze Nginx logs, extract error messages, and export them to CSV reports. Designed for beginners.

------

## 📁 Project Structure

log-analyzer-cli/
│
├── logs/
│   └── access.log               # Sample Nginx log file
│
├── reports/
│   └── error_report.csv         # Output CSV with extracted errors
│
├── requirements.txt             # Python dependencies
├── log_analyzer.py              # Main CLI tool
└── venv/                        # Virtual environment

------

✨ Features

. Scans Nginx log files and extracts error messages for quick debugging.
. Saves extracted errors into a clean, structured CSV file for easy viewing and sharing.
. Automatically runs log analysis every N minutes using the schedule module.
. Simple command-line interface built with click, perfect for learners and campus projects.
. Keeps logs and reports in separate folders (logs/, reports/) for better project hygiene.

------


 📦 Installation
  
   sudo apt update
   sudo apt install python3
   cd log-analyzer-cli

   Create virtual environment:
   python3 -m venv venv
   source venv/bin/activate

   Install dependencies:
   pip install -r requirements.txt

   Analyze logs manually
   python3 log_analyzer.py analyze --logfile logs/access.log

   Schedule periodic analysis
   python3 log_analyzer.py schedule-report --interval 5 --logfile logs/access.log
   

   📊 Output
   CSV report saved to reports/error_report.csv
