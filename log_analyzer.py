import click
import pandas as pd
import re
import os
import schedule
import time

# Path settings
LOG_DIR = "logs"
REPORT_DIR = "reports"

# Ensure directories exist
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

# Function to parse nginx logs and extract errors
def parse_nginx_logs(log_file):
    error_lines = []
    with open(log_file, "r") as f:
        for line in f:
            if "error" in line.lower():
                error_lines.append(line.strip())
    return error_lines

# Save errors to CSV
def save_to_csv(errors, output_file):
    df = pd.DataFrame(errors, columns=["Error Logs"])
    df.to_csv(output_file, index=False)
    click.echo(f"✅ Report saved at {output_file}")

@click.group()
def cli():
    """Log Analyzer CLI Tool"""
    pass

# Command: analyze logs
@cli.command()
@click.option("--logfile", default=f"{LOG_DIR}/access.log", help="Path to Nginx log file")
def analyze(logfile):
    """Analyze nginx logs and export errors to CSV"""
    if not os.path.exists(logfile):
        click.echo("❌ Log file not found!")
        return
    errors = parse_nginx_logs(logfile)
    if errors:
        output_file = os.path.join(REPORT_DIR, "error_report.csv")
        save_to_csv(errors, output_file)
    else:
        click.echo("✅ No errors found in logs.")

# Command: schedule reports
@cli.command()
@click.option("--interval", default=1, help="Run every N minutes")
@click.option("--logfile", default=f"{LOG_DIR}/access.log", help="Path to Nginx log file")
def schedule_report(interval, logfile):
    """Schedule log analysis periodically"""

    def job():
        click.echo("🔄 Running scheduled log analysis...")
        errors = parse_nginx_logs(logfile)
        if errors:
            output_file = os.path.join(REPORT_DIR, "error_report.csv")
            save_to_csv(errors, output_file)

    schedule.every(interval).minutes.do(job)
    click.echo(f"⏳ Scheduled log analysis every {interval} minutes... (Ctrl+C to stop)")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    cli()
