# Plotting data from csv files
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

countiesPath = "us-counties.csv"
statesPath = "us-states.csv"
countryPath = "us.csv"

# County data
countyData = pd.read_csv(countiesPath)
cookMask = countyData["fips"] == 17031
countyDates = countyData[cookMask]["date"]
countyCases = countyData[cookMask]["cases"].diff().fillna(0)
county7DayAvg = countyCases.rolling(7).mean().fillna(0)

countyDates = pd.to_datetime(countyDates)
countyDates = countyDates.dt.strftime("%m/%d/%y")

# State data
stateData = pd.read_csv(statesPath)
ILMask = stateData["state"] == "Illinois"
stateDates = stateData[ILMask]["date"]
stateCases = stateData[ILMask]["cases"].diff().fillna(0)
state7DayAvg = stateCases.rolling(7).mean().fillna(0)

stateDates = pd.to_datetime(stateDates)
stateDates = stateDates.dt.strftime("%m/%d/%y")

# Country data
countryData = pd.read_csv(countryPath)
countryDates = countryData["date"]
countryCases = countryData["cases"].diff().fillna(0)
country7DayAvg = countryCases.rolling(7).mean().fillna(0)

countryDates = pd.to_datetime(countryDates)
countryDates = countryDates.dt.strftime("%m/%d/%y")

# plot county data
plt.bar(countyDates, countyCases, alpha = .3)
plt.plot(countyDates, county7DayAvg)
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.ylabel("Daily New Cases")
plt.title("Total Cases in Cook County")
fig = plt.gcf()
fig.canvas.set_window_title("Cook County")


plt.figure("Illinois") # create a new figure

# plot state data
plt.bar(stateDates, stateCases, alpha = .3)
plt.plot(stateDates, state7DayAvg)
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.ylabel("Daily New Cases")
plt.title("Total Cases in Illinois")

plt.figure("United States") # another plot

# plot for country data
plt.bar(countryDates, countryCases, alpha = .3)
plt.plot(countryDates, country7DayAvg)
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.ylabel("Daily New Cases")
plt.title("Total Cases in the US")

# plot
plt.show()