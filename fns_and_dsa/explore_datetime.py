from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print("Date after", days, "day(s):", future_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    display_current_datetime()

    while True:
        try:
            user_input = int(input("Enter the number of days to add to the current date: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    calculate_future_date(user_input)
