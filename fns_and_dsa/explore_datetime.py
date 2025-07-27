from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date is {current_date}")
    number_of_days = int(input("Please enter a number of days (as an integer)"))

    def calculate_future_date():
        td = timedelta(days=number_of_days)  # Use 'days' keyword argument
        future_date = current_date + td      # Add timedelta to datetime
        print(f"The future date is {future_date}")

    calculate_future_date()

display_current_datetime()
