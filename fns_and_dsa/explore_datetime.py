from datetime import datetime, timedelta

def display_current_datetime():
    # Save the current date and time
    current_date = datetime.now()
    # Format and print in "YYYY-MM-DD HH:MM:SS"
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    # Current date and time
    current_date = datetime.now()
    # Calculate future date by adding days
    future_date = current_date + timedelta(days=days)
    # Print future date in "YYYY-MM-DD"
    print("Date after", days, "day(s):", future_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    display_current_datetime()
    
    # Prompt user for days input
    while True:
        try:
            user_input = int(input("Enter the number of days to add: "))
            break
        except ValueError:
            print("Please enter a valid integer.")
    
    calculate_future_date(user_input)
