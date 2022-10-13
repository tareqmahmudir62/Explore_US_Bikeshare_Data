# Explore_US_Bikeshare_Data
US bike share data was used to answer interesting questions about it by computing descriptive statistics


## <b> Overview </b> ##

In this project, I have used Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. I wrote code to import the data and answer interesting questions about it by computing descriptive statistics. I have also written a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

## <b> Project Details </b> ## 

Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

## <b> The Datasets </b> ## 

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

              Start Time (e.g., 2017-01-01 00:07:57)
              End Time (e.g., 2017-01-01 00:20:53)
              Trip Duration (in seconds - e.g., 776)
              Start Station (e.g., Broadway & Barry Ave)
              End Station (e.g., Sedgwick St & North Ave)
              User Type (Subscriber or Customer)
              
The Chicago and New York City files also have the following two columns:

Gender
             Birth Year

![nyc-data](https://user-images.githubusercontent.com/97672246/195616615-2d0ee042-27d2-4bea-8162-9ac170c02b25.png)
              Data for the first 10 rides in the new_york_city.csv file

The original files are much larger and messier, and you don't need to download them, but they can be accessed here if you'd like to see them (Chicago, New York City, Washington). These files had more columns and they differed in format in many cases. Some data wrangling has been performed to condense these files to the above core six columns to make your analysis and the evaluation of your Python skills more straightforward.


## <b> Statistics Computed </b> ## 

You will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, you'll write code to provide the following information:

#1 Popular times of travel (i.e., occurs most often in the start time)

    1. most common month
    2. most common day of week
    3. most common hour of day

#2 Popular stations and trip

    1. most common start station
    2. most common end station
    3. most common trip from start to end (i.e., most frequent combination of start station and end station)

#3 Trip duration

    1. total travel time
    2. average travel time

#4 User info

    1. counts of each user type
    2. counts of each gender (only available for NYC and Chicago)
    3. earliest, most recent, most common year of birth (only available for NYC and Chicago)

## <b> Software Needed </b> ## 

To complete this project, the following softwars/tools were used:

1. I have used Python 3, NumPy, and pandas installed using Anaconda
2. Text editor like Sublime or Atom.
3. A terminal application (Terminal on Mac and Linux or Cygwin on Windows).


## <b> Information about the Datasets </b> ## 
To answer these questions using Python, I wrote a Python script. To help guide my work in this project, a template with helper code and comments is provided in a bikeshare.py file. The following three city dataset files were used for this project too:

  chicago.csv
  new_york_city.csv
  washington.csv
  
  ## <b> Tools used/Built with </b> ## 
  
  1. Python
  2. numpy
  3. pandas
  4. jupyter notebook
