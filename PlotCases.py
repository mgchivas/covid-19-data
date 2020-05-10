# Plotting data from csv files
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = "us-counties.csv"

# read csv using pandas
df = pd.read_csv(path)
ILMask = df["state"] == "Illinois"
cookMask = df["fips"] == 17031

datesIL = df[ILMask]["date"]
casesInIL = df[ILMask]["cases"]
datesCook = df[cookMask]["date"]
casesInCook = df[cookMask]["cases"]
# print(df[mask])

# plot
plt.bar(datesCook, casesInCook)
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.title("Total Cases in Cook")
plt.show()