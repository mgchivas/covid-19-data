# Plotting data from csv files
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

countiesPath = "us-counties.csv"
statesPath = "us-states.csv"

# County data
countyData = pd.read_csv(countiesPath)
cookMask = countyData["county"] == "Cook"
countyDates = countyData[cookMask]["date"]
countyCases = countyData[cookMask]["cases"]

# State data
stateData = pd.read_csv(statesPath)
ILMask = stateData["state"] == "Illinois"
stateDates = stateData[ILMask]["date"]
stateCases = stateData[ILMask]["cases"]

# plot county data
plt.bar(countyDates, countyCases)
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.ylabel("Total Cases")
plt.title("Total Cases in Cook County")

plt.figure() # create a new figure

# plot state data
plt.bar(stateDates, stateCases)
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.ylabel("Total Cases")
plt.title("Total Cases in Illinois")

# plot
plt.show()