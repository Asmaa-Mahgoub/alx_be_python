task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority :
    case "high" :
            message = f"'{task}' is a {priority} priority task"
    case "medium" :
            message = f"'{task}' is a {priority} priority task "
    case "low" :
            message = f"'{task}' is a {priority} priority task "

if time_bound == "yes":
       print("Reminder: " + message + "that requires immediate attention today!")
else :
       print("Note: " + message + "Consider completing it when you have free time.") 
 
