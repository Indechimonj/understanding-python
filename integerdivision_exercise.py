# This script calculates the number of days since the epoch (January 1, 1970) in Kenya's timezone.
#Based on the question of using time dodule to compute the number of days since the epoch in Kenya's timezone,and the current time in Kenya in HH:MM:SS format.
#The logic used is simple:just convert the current time to seconds since the epoch, adjust for Kenya's timezone, and then calculate the number of days and the current time in HH:MM:SS format.
import time

current_time = time.time()# Get the current time in seconds since the epoch

kenya_offset = 3 * 3600 # Kenya is UTC+3, so we add 3 hours in seconds
kenya_time = current_time + kenya_offset # Calculate the current time in Kenya

seconds_per_day = 24 * 3600 # Number of seconds in a day

days_since_epoch = int(kenya_time // seconds_per_day) # Calculate the number of days since the epoch

seconds_today = int(kenya_time % seconds_per_day) # Calculate the number of seconds today

hours_today = seconds_today // 3600 # Calculate the number of hours today
minutes_today = (seconds_today % 3600) // 60 # Calculate the number of minutes today
seconds_today = seconds_today % 60  # Calculate the remaining seconds today

print(f"Days since epoch: {days_since_epoch}") # Print the number of days since the epoch
print(f"Current time in Kenya: {hours_today:02}:{minutes_today:02}:{seconds_today:02}") # Print the current time in Kenya in HH:MM:SS format

