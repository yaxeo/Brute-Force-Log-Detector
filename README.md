### How It Works

The tool analyzes Linux authentication logs to detect possible SSH brute-force attacks.
It scans log files line by line, identifies failed SSH login attempts, and groups them by IP address.

For each IP, the tool tracks the timestamps of failed login attempts and checks whether the number of failures exceeds a configurable threshold within a defined time window.

If an IP performs too many failed authentication attempts in a short period of time, the tool flags it as a potential brute-force attack.

## Features

Detects SSH brute-force attacks
Configurable time window
Configurable maximum failed login attempts
Fast and efficient log parsing
Terminal-based alerts
Compatible with standard Linux authentication logs

## Requirements

Python 3.x
Linux system with authentication logs (/var/log/auth.log)

Installation
Clone the repository
git clone https://github.com/yourusername/bruteforce-detector.git
cd bruteforce-detector

## Configuration

Edit the following variables inside bruteforce_detector.py:

LOG_FILE = "auth.log"      # Path to the authentication log file
MAX_ATTEMPTS = 5          # Failed login attempts threshold
WINDOW_MINUTES = 2        # Time window in minutes

## Usage

Run the script:

python3 bruteforce_detector.py

Output Example

If a brute-force attack is detected:

## BRUTE FORCE ALERTS

[!] IP 185.143.22.91 performed 5+ failed logins between 00:12:01 and 00:13:10


If no attack is detected:

No brute force attacks detected.

## Detection Logic

Parse authentication logs
Extract IP addresses from failed SSH login attempts
Store timestamps per IP address
Compare failed attempts within the configured time window
Trigger an alert when the threshold is exceeded

## Use Cases

Detection of SSH brute-force attacks
SOC monitoring and alerting
Incident response support
Security research and training
SIEM enrichment

## Future Improvements

Automatic IP blocking (iptables)
JSON report generation
Email or Telegram alerting
Apache and Nginx log support
Dashboard and SIEM integration

## License

This project is licensed under the MIT License.
