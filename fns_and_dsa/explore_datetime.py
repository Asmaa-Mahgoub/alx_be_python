from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_current = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_current}")

    number_of_days = int(input("Enter the number of days to add to the current date: "))

    def calculate_future_date():
        td = timedelta(days=number_of_days)
        future_date = current_date + td
        formatted_future = future_date.strftime("%Y-%m-%d")
        print(f"The future date is: {formatted_future}")

    calculate_future_date()

display_current_datetime()


