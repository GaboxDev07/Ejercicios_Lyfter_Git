print ("--- Welcome to the Seconds calculator ---")


time_in_seconds = int (input("Enter the time in seconds: "))

if time_in_seconds == 600:
    print("It is exactly on time!")
elif time_in_seconds > 600:
    print ("It is greater than 10 minutes.")
elif time_in_seconds < 600:
    seconds_missing = 600 - time_in_seconds
    print (seconds_missing, "are missing to reach 10 minutes")







