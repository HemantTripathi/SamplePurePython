# Exponential Backoff
# Problem : Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retires

import time

wait_time = 1
max_reties = 5
attempts = 0

while attempts < max_reties:
    print("Attempt",attempts + 1, "-wait time", wait_time)
    time.sleep(wait_time)
    wait_time *=2
    attempts += 1

