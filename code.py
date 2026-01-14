import re
from datetime import datetime, timedelta
from collections import defaultdict

LOG_FILE = "auth.log"      # Can also be apache.log
MAX_ATTEMPTS = 5          # Failed attempts threshold
WINDOW_MINUTES = 2        # Time window in minutes

# SSH failed login regex (Linux auth.log)
SSH_FAIL_REGEX = re.compile(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)")

attempts = defaultdict(list)

def parse_timestamp(line):
    try:
        return datetime.strptime(line[:15], "%b %d %H:%M:%S")
    except:
        return None

print("\nStarting brute force detection...\n")

with open(LOG_FILE, "r", errors="ignore") as log:
    for line in log:
        match = SSH_FAIL_REGEX.search(line)
        if match:
            ip = match.group(1)
            timestamp = parse_timestamp(line)
            if not timestamp:
                continue
            attempts[ip].append(timestamp)

alerts = []

for ip, times in attempts.items():
    times.sort()
    for i in range(len(times)):
        window = times[i:i + MAX_ATTEMPTS]
        if len(window) >= MAX_ATTEMPTS:
            if window[-1] - window[0] <= timedelta(minutes=WINDOW_MINUTES):
                alerts.append((ip, window[0], window[-1]))
                break

print("BRUTE FORCE ALERTS\n")

if alerts:
    for ip, start, end in alerts:
        print(f"[!] IP {ip} performed {MAX_ATTEMPTS}+ failed logins between {start} and {end}")
else:
    print("No brute force attacks detected.")
