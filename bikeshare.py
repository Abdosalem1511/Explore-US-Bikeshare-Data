import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities= ['chicago','new york city','washington']

months= ['january','february','march','april','may','june','all']

days= ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please enter name of the city: chicago, new york city, washington \n').lower()
        if city in cities :
            break
        else:
            print('Please enter name of the city correctly\n')
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please enter name of the month: january, february, march, april, may, june, all \n').lower()
        if month in months :
            break
        else:
            print('Please enter name of the month correctly\n')
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input('Please enter the day: sunday, monday, tuesday, wednesday, thursday, friday, saturday, all \n').lower()
        if day in days :
            break
        else: 
            print("Please enter name of the day correctly\n") 
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # get data from file into a dataframe
    df= pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time']= pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['Month']= df['Start Time'].dt.month_name()
    df['Day']= df['Start Time'].dt.day_name()
    df['Hour']= df['Start Time'].dt.hour

    # filter by month and by day of week if applicable
    if month != 'all':
        df = df[ df['Month'] == month.title() ]

    if day != 'all':
        df = df[ df['Day'] == day.title()]   

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month= df['Month'].mode()[0]
    print('Most common month:',most_common_month)
    
    # display the most common day of week
    most_common_day= df['Day'].mode()[0]
    print('Most common day:',most_common_day)

    # display the most common start hour
    most_common_hour= df['Hour'].mode()[0]
    print('Most common hour:',most_common_hour,': --')

    print("\nThis took %s seconds." % (time.time() - start_time))



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station:", most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station:", most_common_end_station)

    # display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station: {}, {}".format(most_common_start_end_station[0], most_common_start_end_station[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = round(df['Trip Duration'].sum()/60)
    print("Total travel time in minutes:", total_travel_time)


    # display mean travel time
    mean_travel_time = round(df['Trip Duration'].mean()/60)
    print("Mean travel time in minutes:", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_counts = df['User Type'].value_counts()
    print("Counts of user types:",user_counts)

    # Display counts of gender
    if city =='washington' :
        print('Count of gender: No information found')
    else:
        gender_counts = df['Gender'].value_counts()
        print('Counts of gender:',gender_counts)
        
    # Display earliest, most recent, and most common year of birth
    if city =='washington' :
        print('Birth year statistics: No information found')
    else:
        most_common_year= df['Birth Year'].mode()[0]
        most_recent = df['Birth Year'].max()
        earliest_year = df['Birth Year'].min()
        print('earliest, most recent, and most common year of birth: {},{},{}'.format(earliest_year,most_recent,most_common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    i=0
    j=5
    x=['yes','no']
    while True:
        print('Do you want five raw data?')
        user_answer = input('Please enter yes or no: ').lower()
        while user_answer not in x:
            print('Please enter yes or no: ')
            user_answer = input().lower()
        if user_answer == "yes":
            print(df.iloc[i:j])
            i+=5
            j+=5
        else: 
            print('Thanks for using bikeshare.')
            break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
