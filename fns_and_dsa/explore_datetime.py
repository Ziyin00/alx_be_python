from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date


def calculate_future_date(current_date):
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date


def main():
    current_date = display_current_datetime()
    calculate_future_date(current_date)


if __name__ == "__main__":
    main()
