import time
import pandas as pd

# Data file paths mapped to city names
CITY_FILES = {
    'chicago': 'data/chicago.csv',
    'new york city': 'data/new_york_city.csv',
    'washington': 'data/washington.csv',
}

def fetch_filters():
    """
    Prompts user input to specify a city, month, and day for data analysis.
    Returns:
        city (str): Selected city name
        month (str): Selected month or 'all'
        day (str): Selected day of the week or 'all'
    """
    print("Welcome! Let's analyze US bikeshare data.")
    
    # Request city input
    city = input_validated(
        prompt="\nChoose a city (Chicago, New York City, or Washington): ",
        options=CITY_FILES.keys(),
        case_insensitive=True
    )
    
    # Request month input
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input_validated(
        prompt="\nEnter a month (January - June) or 'all': ",
        options=months,
        case_insensitive=True
    )
    
    # Request day input
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = input_validated(
        prompt="\nEnter a day of the week or 'all': ",
        options=days,
        case_insensitive=True
    )
    
    print(f"\nFilters applied -> City: {city.title()}, Month: {month.title()}, Day: {day.title()}")
    return city, month, day

def input_validated(prompt, options, case_insensitive=False):
    """
    Validates user's input against a set of options.
    Args (arguments):
        prompt (str): Input prompt for the user
        options (iterable): Valid options for input
        case_insensitive (bool): Whether validation is case insensitive
    Returns:
        str (string): Validated user input
    """
    options = {option.lower() for option in options} if case_insensitive else set(options)
    while True:
        user_input = input(prompt).strip()
        normalized_input = user_input.lower() if case_insensitive else user_input
        if normalized_input in options:
            return user_input.lower() if case_insensitive else user_input
        print("Invalid input. Please try again.")

def load_city_data(city, month, day):
    """
    Loads and filters bikeshare data by city, month, and day.
    Args:
        city (str): City name
        month (str): Month name or 'all'
        day (str): Day name or 'all'
    Returns:
        pd.DataFrame: Filtered data
    """
    print("\nLoading data...")
    df = pd.read_csv(CITY_FILES[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    
    if month != 'all':
        df = df[df['month'] == month.lower()]
    if day != 'all':
        df = df[df['day_of_week'] == day.lower()]
    
    return df

def display_statistics(df, stat_name, stat_func):
    """
    Generic function to compute and display a statistic.
    Args:
        df (pd.DataFrame): Data frame to analyze
        stat_name (str): Name of the statistic
        stat_func (callable): Function to compute the statistic
    """
    print(f"\nCalculating {stat_name}...")
    start_time = time.time()
    result = stat_func(df)
    print(result)
    print(f"\nTime taken: {time.time() - start_time:.2f} seconds.")
    print("-" * 40)

# Other specific functions (e.g., time_stats, station_stats, trip_duration_stats, user_stats) follow similar logic
# They would call `display_statistics` with appropriate parameters

def main():
    while True:
        city, month, day = fetch_filters()
        df = load_city_data(city, month, day)
        
        # Call specific analysis functions here
        
        restart = input("\nWould you like to restart? Enter 'yes' or 'no': ").strip().lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()


    