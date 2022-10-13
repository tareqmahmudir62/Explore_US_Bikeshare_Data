
import pandas as pd
import numpy as np
import time
import datetime



dfc= pd.read_csv('chicago.csv')
dfn= pd.read_csv ('new_york_city.csv')
dfw= pd.read_csv ('washington.csv')
months= ['january','february','march','april','may','june','all',]
days= ['sunday','monday','tuesday','wednesday','thursday','friday','all',]
    
dfc.head(5)
dfn.head(5)
dfw.head(5)

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
	
# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Hello! Let\'s explore some US bikeshare data!')
    cities= ['chicago','new york city','washington']
    city= input("insert the name of the city: ").lower()

    while city not in cities:
        city= input("oops!there was a typo! please select either chicago, new york city or washington: ").lower()


# get user input for month (all, january, february, ... , june)
    months= ['january','february','march','april','may','june']
    month= input("insert the name of the month : ").lower()

    while month not in months:
        month= input("oops!there was a typo! Please select any month from january to december: ").lower()


# get user input for day of week (all, monday, tuesday, ... sunday)
    days= ['sunday','monday','tuesday','wednesday','thursday','friday']
    day= input("insert the name of the day : ").lower()

    while day not in days:
        day= input("oops!there was a typo! please select any day from sunday to saturday: ").lower()

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
    df= pd.read_csv(CITY_DATA[city])
    
    #converting the data type of the 'Start Time' column into datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month # create a new column for 'month'
    df['day']= df['Start Time'].dt.dayofweek # create a new column for 'day' that consists the name of the week
    
    # use filter on the 'month' column to get the month and set Month's index starts from 1 to 6 
    if month != 'all':
        month= months.index(month)+1
        df= df[df['month']==month]
    # use filter on the 'day' column to get the day and set day's index starts from 1 to 7 
    if day != 'all':
        day= days.index(day)
        df= df[df['day']==day]
    return df

load_data('washington', 'january', 'monday').tail(5)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month= df['month'].mode()[0]
    print('the most common month is: '.format(common_month))

    # display the most common day of week
    common_day= df['day'].mode()[0]
    print('the most common day is: '.format(common_day))
    
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour # creating a column for Hour
    common_hour= df['hour'].mode()[0]
    print('the most common hour is: '.format(common_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # most commonly used start station
    common_start_station= df ['Start Station'].mode()[0]
    print('the most common start station is: '.format(common_start_station))
    
    # most commonly used end station
    common_station= df ['End Station'].mode()[0]
    print('the most common station is: '.format(common_station))
    
    # most frequent combination of start station and end station trip
    station_combination = df ['Start Station'] + ' ' + df ['End Station'].mode()[0]
    print('the most most frequent combination of start station and end station trip is: '.format(station_combination))
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel= df['Trip Duration'].sum()
    print('Total travel time calculated is: '. format(total_travel))
    # display mean travel time
    mean_travel_time= df['Trip Duration'].mean()
    print('Total average travel time calculated is: '. format(mean_travel_time))
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    
    gender= ['Male','Female']
    
    print('\nCalculating User Stats...\n')
    
    start_time = time.time()

    # Display counts of user types
    user_type_count= df['User Type'].value_counts()
    print('The count of the different users numbers: '. format(user_type_count))
    
    # Display counts of gender
    if city != 'washington':
        print('Gender count is: {}'.format(df['Gender'].value_counts()))
    else:
        print('Please select any city but washington. We dont have data for Washington.')
        
    # Display earliest, most recent, and most common year of birth
    birth_year_earliest= int(df['Birth Year'].min())
    birth_year_recent= int(df['Birth Year'].max())
    birth_year_common= int(df['Birth Year'].mode()[0])
    if city !='washington':
        print ("the earliest,,recent and commont birth year {},{},{}.". format(birth_year_earliest,birth_year_recent,birth_year_common))
    else:
        print('birth_year for this {} is not available. Please select another city.'.format(city))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
        
            
        

def display_data(df):
    index=0
    user_input=input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower()



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


