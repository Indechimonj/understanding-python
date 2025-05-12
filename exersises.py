num=input("Enter time in minutes and seconds: ")#prompts the user to enter time in minutes and seconds.
minutes,seconds= map(int,num.split())##splits the input into minutes and seconds and converts them to integers.
total_sec= (minutes*60)+seconds#calculates the total time in seconds by multiplying the minutes by 60 and adding the seconds.

print("Total seconds", total_sec)#prints the value of total_sec to the console.
