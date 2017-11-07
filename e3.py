#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

# Read in each csv and append them into a list.
df_election = []
for i in range(1924,2020,4):
    header = pd.read_csv("president_general_{}.csv".format(i), nrows=5).dropna(axis=1)
    d = header.iloc[0].to_dict()
    df = pd.read_csv("president_general_{}.csv".format(i), index_col = 0, thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d)
    df.dropna(inplace = True, axis = 1)
    df["Year"] = i
    df_election.append(df.loc[:, ["Democratic", "Republican", "Total Votes Cast", "Year"]])

# Concat the list to a dataframe and adding the Republican Share column.
df_elections = pd.concat(df_election)
df_elections["Republican Share"] = df_elections["Republican"]/df_elections["Total Votes Cast"]

# Slicing out the county/city of interest, as well as the columns for plotting.
df_accomack = df_elections.loc["Accomack County", ["Year", "Republican Share"]]
df_albemarle = df_elections.loc["Albemarle County", ["Year", "Republican Share"]]
df_alexandria = df_elections.loc["Alexandria City", ["Year", "Republican Share"]]
df_alleghany = df_elections.loc["Alleghany County", ["Year", "Republican Share"]]

# Plot and save the figures as PDF.
df_accomack.plot(x = "Year", y = "Republican Share")
plt.ylabel("Accomack County")
plt.xticks(range(1924,2020,4),rotation = 90)
plt.title("Republican Share of Accomack county")
plt.savefig("accomack_county.pdf")

df_albemarle.plot(x = "Year", y = "Republican Share")
plt.ylabel("Albemarle County")
plt.xticks(range(1924,2020,4),rotation = 90)
plt.title("Republican Share of Albemarle County")
plt.savefig("albemarle_county.pdf")

df_alexandria.plot(x = "Year", y = "Republican Share")
plt.ylabel("Alexandria City")
plt.xticks(range(1924,2020,4),rotation = 90)
plt.title("Republican Share of Alexandria City")
plt.savefig("alexandria_city.pdf")

df_alleghany.plot(x = "Year", y = "Republican Share")
plt.ylabel("Alleghany County")
plt.xticks(range(1924,2020,4),rotation = 90)
plt.title("Republican Share of Alleghany County")
plt.savefig("alleghany_county.pdf")
