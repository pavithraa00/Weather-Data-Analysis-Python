import pandas as pd
data=pd.read_csv('1. Weather Data.csv')

### BASIC FUNCTIONS USED

data
data.head()
data.shape
data.index
data.columns
data.dtypes
data['Weather'].unique()
data.nunique()
data.count()
data['Weather'].value_counts()

#### DATA ANALYSIS WITH PYTHON ON WEATHER DATASET

## 1.Find all unique 'Wind Speed' values in the data 
data['Wind Speed_km/h'].unique()

## 2.Find the no.of times when the 'Weather is exactly Clear'
  # using filtering
  data[data.Weather == 'Clear']
  # using groupby
  data.groupby('Weather').get_group('Clear')

## 3. Find the no.of times when wind speed was exactly 4km/h
data[data['Wind Speed_km/h'] == 4]

## 4.Find null values from the data
data.isnull().sum()

## 5.Rename the column name "Weather" to "Weather Condition"
data.rename(columns = {'Weather' : 'Weather Condition'}, inplace = True)
data.head(2)

## 6.What is the mean of 'Visibility' ?
data.Visibility_km.mean()

## 7.What is the standard deviation of 'pressure' ?
data.Press_kPa.std()

## 8.What is the variance of 'relative humidity' ?
data['Rel Hum_%'].var()

## 9.Find all instances when 'Snow' was recorded
  # using value_counts
  data['Weather Condition'].value_counts()
  # using filtering
  data[data['Weather Condition'] == 'Snow' ]  
  # using groupby
  data.groupby('Weather Condition').get_group('Snow')
  # using str.contains
  data[data['Weather Condition'].str.contains("Snow")]

## 10.Find all instances when 'Wind Speed is above 24' and 'Visbility is 25'
data[(data['Wind Speed_km/h']> 24) & (data['Visibility_km'] == 25)]

## 11.What is mean value of each column against each 'Weather Condition'?
data.groupby('Weather Condition').mean(numeric_only=True)

## 12.What is the minimum & maximum value of each column against 'Weather Condition'
  # MINIMUM
  data.groupby('Weather Condition').min(numeric_only=True)
  #MAXIMUM
  data.groupby('Weather Condition').max(numeric_only=True)

## 13.Show all records where 'Weather Condition' is Fog
data[data['Weather Condition'] == 'Fog' ]

## 14.Find all the instances when "Weather is Clear" or 'Visibility > 40 '
data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40) ]

#  15.Find all the instances when  'Weather is Clear' and 'Relative Humidity is greater than 50'  or 'Visibility is above 40'
data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50) | (data['Visibility_km'] > 40)]
