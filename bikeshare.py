import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
             'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    cn_city = input('Please, Enter one City from the following :(chicago, new york, washington)').lower() #Selected City
    while cn_city not in (CITY_DATA.keys()): #Handel invalid input for City
      print('invalid input! please Enter a valid city from the following : (washington, new york city or chicago)') 
      cn_city = input().lower()
    strainer = input('please, Enter How do you like to filter the data! by month, day, both or not at all, Type "none" for no time filter').lower() #Method to filter using it.
    while strainer not in (['month' , 'day' , 'none' , 'both']): #Handel invalid input for Filtering
      print('invalid input, please Enter a valid method to filter the data using it:(filter by :month, day, both or not at all, Type "none" for no time filter')
      strainer = input().lower()
    
    month = ['january' , 'february' , 'march' , 'april' , 'may' , 'june']
    if strainer == 'month' or strainer =='both': #if user chose to filter by only Months or Months and days
      mnth = input('Which month from the following :january, february, march, april ,may, june ? ').lower() #input month
      while mnth not in month: #Handel invalid input for Months
        print('Invalid input! please try again using a valid input from the following: january, february, march, april ,may, june')
        mnth =input().lower()
    else:
      mnth = 'all'      #Set month = all to use it in filtering by month
    
    day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    if strainer == 'day' or strainer =='both': #if user chose to filter by only days or Months and days
      dy = input('Which day from the following : Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').lower()
      while dy not in day: #Handel invalid input for days
         print('invalid input! Please try again')
         dy = input('Which day from the following : Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').lower()
    else:
      dy = 'all' #Set day = all to use it in filtering by day

    print('-'*40)
    return cn_city, mnth, dy


def load_data(city, month, day):
   
    df = pd.read_csv(CITY_DATA[city]) #Load data
    df['Start Time'] = pd.to_datetime(df['Start Time']) #To convert data from string to date time
    df['month'] = df['Start Time'].dt.month #Extracted Month
    df['day'] = df['Start Time'].dt.day_name() #Extracted day
    df['hour'] = df['Start Time'].dt.hour #Extracted hour

    if month != 'all': 
      months=['january', 'february', 'march','april' , 'may', 'june'] 
      month = months.index(month) + 1 #Indexing Months 
       
      df = df[df['month'] == month] #filter by month
     
    if day != 'all':  
        df = df[df['day'] == day.title()]   #filter by day    
      
    return df

def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # most common month
    print('Most common month is :  ', df['month'].mode()[0])
     # most common day
    print('Most common day is :  ', df['day'].mode()[0])
     # most common hour
    print('Most common hour is :  ', df['hour'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    pop_stsation = df['Start Station'].mode()[0] # most commonly used start station
    print('The most commonly used start station', pop_stsation) 
     
    pop_endsation = df['End Station'].mode()[0] #most commonly used end station  
    print('The most commonly used end station', pop_endsation) 
      
    df['pop_trip'] = df['Start Station'] + ' to ' + df['End Station'] #most popular trip
    print('The most frequent trip is :' , df['pop_trip'] .mode()[0]) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    total_travel = df['Trip Duration'].sum().round() #total travel time
    print('Total travel time is :', total_travel)
     
    mean_travel = df['Trip Duration'].mean() #mean travel time
    print('Mean travel time is :', mean_travel)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
     
    count_user = df['User Type'].value_counts().to_frame() #counts of user types after converting series to data frame
    print('Count of user type = ' , count_user)
    
    if 'Gender' in(df.columns): #As washington has not Gender column
      count_gender = df['Gender'].value_counts().to_frame() #counts of gender after converting series to data frame
      print('Count of gender = ', count_gender)
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in(df.columns):
      earliest = int(df['Birth Year'].min())
      print('The earliest year of birth is :' ,earliest)
      most_recent = int(df['Birth Year'].max()) 
      print('The most recent year of birth is :' ,most_recent)
      most_common = int(df['Birth Year'].mode()[0])
      print('The most common year of birth is :' , most_common)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_(df):
  user = input('\nWould you like to diplay raw data?\n').lower()
  if user not in (['yes' , 'no']):
    print('Ok Thank you')
  elif user == 'no':
    print('Ok Thank you')  
  else:
    j = 0
    while j+5 < df.shape[0]:
      print(df.iloc[j : j+5])
      j += 5
      user = input('Next 5 raws?')
      if user.lower() != 'yes':
        print('Ok Thank you')
        break   
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
          print('OK Thank you')
          break
if __name__ == "__main__":
   main()