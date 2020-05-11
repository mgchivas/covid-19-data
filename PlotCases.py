# Plotting data from csv files
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

countiesPath = "us-counties.csv"
statesPath = "us-states.csv"

# County data
countyData = pd.read_csv(countiesPath)
cookMask = countyData["fips"] == 17031
print(cookMask)
countyDates = countyData[cookMask]["date"]
countyCases = countyData[cookMask]["cases"].diff().fillna(0)

# State data
stateData = pd.read_csv(statesPath)
ILMask = stateData["state"] == "Illinois"
stateDates = stateData[ILMask]["date"]
stateCases = stateData[ILMask]["cases"].diff().fillna(0)

# plot county data
plt.bar(countyDates, countyCases)
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.ylabel("Daily New Cases")
plt.title("Total Cases in Cook County")

plt.figure() # create a new figure

# plot state data
plt.bar(stateDates, stateCases)
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.ylabel("Daily New Cases")
plt.title("Total Cases in Illinois")

# plot
plt.show()