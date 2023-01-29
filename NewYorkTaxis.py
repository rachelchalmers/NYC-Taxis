#### Your Uber Has Arrived ####

# Import Libraries
import matplotlib.pyplot as plt
import pandas as pd

# Set font for data visualisations
hfont = {'fontname':'Lao Sangam MN'}

# Read in data (available at https://data.world/data-society/uber-pickups-in-nyc)
taxi_data = pd.read_csv("/Users/Rachel/Downloads/nyc_taxi_data.csv",encoding='latin-1')
print(taxi_data.head(5))
print(taxi_data.info())

# Convert Date and Time columns to datetime
taxi_data['Date'] = pd.to_datetime(taxi_data['Date'])
taxi_data['Time'] = pd.to_datetime(taxi_data['Time'])

# Add columns for Day, Hour and Weekday
taxi_data["Day"] = taxi_data["Date"].apply(lambda x: x.day)
taxi_data["Hour"] = taxi_data["Time"].apply(lambda x: x.hour)
taxi_data["Weekday"] = taxi_data["Date"].apply(lambda x: x.weekday())

## Define functions for data visualisations ##

# Show ride frequency per day of the month
def daily_trips(data_frame):
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.hist(data_frame.Day, width=0.6, bins=31, color="lightskyblue")
    plt.title("Density of trips",**hfont, fontsize=16)
    plt.xlabel("Day",**hfont, fontsize=14)
    plt.ylabel("Number of trips",**hfont, fontsize=14)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.labelpad = 10
    ax.yaxis.labelpad = 10
    plt.show()

#Visualise the Density of rides per Weekday
def weekday_trips(data_frame):
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.hist(data_frame.Weekday, width=0.6, range=(0, 6.5), bins=7, color="darkseagreen")
    plt.title("Density of trips per Weekday",**hfont, fontsize=16)
    plt.xlabel("Weekday",**hfont, fontsize=14)
    plt.ylabel("Number of trips",**hfont, fontsize=14)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.labelpad = 10
    ax.yaxis.labelpad = 10
    plt.show()

#Visualise the Density of rides per hour
def hourly_trips(data_frame):
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.hist(data_frame.Hour, width=0.6, bins=24, color="plum")
    plt.title("Density of trips per Hour",**hfont, fontsize=16)
    plt.xlabel("Hour",**hfont, fontsize=14)
    plt.ylabel("Number of rides",**hfont, fontsize=14)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.labelpad = 10
    ax.yaxis.labelpad = 10
    plt.show()

## Call data vis functions

daily_trips(taxi_data)
weekday_trips(taxi_data)
hourly_trips(taxi_data)




