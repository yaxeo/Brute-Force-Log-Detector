## How It Works

The script scans authentication logs line by line and looks for failed SSH login attempts.
For each IP address found, it stores the timestamps of failed logins and checks whether the number of failures exceeds a defined threshold inside a configurable time window.

If an IP performs too many failed logins in a short period of time, the tool flags it as a possible brute-force attack.

### Features

Detects brute-force SSH attacks
Configurable time window
Configurable maximum failed attempts
Fast log parsing
Generates real-time alerts in terminal
Works with standard Linux auth.log

### Requirements

Python 3.x
Linux system with authentication logs (/var/log/auth.log)

### Installation

### Clone the repository:
git clone https://github.com/yourusername/bruteforce-detector.git
cd bruteforce-detector

### Configuration
Edit these values inside bruteforce_detector.py:

LOG_FILE = "auth.log"     # Path to the log file
MAX_ATTEMPTS = 5         # Number of failed logins to trigger an alert
WINDOW_MINUTES = 2       # Time window in minutes

### Usage

Run the script:
python3 bruteforce_detector.py

### Output Example

BRUTE FORCE ALERTS
[!] IP 185.143.22.91 performed 5+ failed logins between 00:12:01 and 00:13:10

If no attack is detected:
No brute force attacks detected.

### Detection Logic

Parse authentication logs
Extract IP addresses from failed SSH attempts
Store timestamps per IP
Compare the number of failures within the configured time window
Trigger alert if threshold is exceeded

### Use Cases

Detect SSH brute-force attacks
SOC alerting and monitoring
Incident response automation
Security research and training
SIEM enrichment

### Future Improvements
Automatic IP blocking (iptables)
JSON report generation
Email/Telegram alerting
Apache/Nginx log support
Dashboard integration

License
This project is licensed under the MIT License.
