# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 11:01:24 2022

@author: Terrance
"""
"""
This is my "Life Expectancy and GDP" portfolio project for Codecademy
I know it says to use Jupyter Notebook but I prefer Spyder so here we are.
I'm also really bad at using comments, so if you're reading this, forgive me
in advance. It's going to be messy and things will be missing.
I'll start by loading in the data and taking a look to formulate my questions.
"""

import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
%matplotlib inline

sns.set_palette("bright")


#importing the data as leag_data (Life Expectancy and GDP)
leag_data = pd.read_csv("all_data.csv")
#cleaning column names
leag_data.columns = ["country", "year", "life_expectancy", "GDP"]
#changing "United States of America" to "USA"
leag_data.country.replace("United States of America", "USA", inplace=True)
#print(leag_data.head())
#print(leag_data.info())
#print(leag_data.country.unique())

#explore mean GDP by country
print(leag_data.groupby("country").GDP.mean())

"""
I think the main things I would like to look at are:
1) The relationship of GDP to Life Expectancy, for the set and by country
2) The change in GDP and Life Expectancy over time, for the set and by country
3) Any notable difference in these two between "Developed" and "Developing"
    countries.
    *note: Since there is no universally accepted definition of developed or
    developing, for my purpose I will use "Greater than 1.0e+12 mean GDP" as
    the signifier for "Developed". This means Chile, Mexico, and Zimbabwe are
    "Developing", and China, Germany, and the US are "Developed"
"""

countries = leag_data.country.unique().tolist()
developing = ["Chile", "Mexico", "Zimbabwe"]
developed = ["China", "Germany", "USA"]

#add "status" for developing countries
leag_data["status"] = leag_data.apply(lambda x: "Developing" if x.country in developing else "Developed", axis=1)
print(leag_data.info())
print(leag_data.groupby("country").status.unique())
# =============================================================================
print(countries)
# print(deving_data.head())
# print(devd_data.head())
# =============================================================================

#96 total entries shouldn't be too messy, so let's first look at gdp vs
#life expectancy for the whole set

countryplot = sns.scatterplot(
    x=leag_data.GDP,
    y=leag_data.life_expectancy,
    hue=leag_data.country,
    alpha=0.5)
countryplot.set(xscale="log")
plt.title("Life Expectancy vs GDP by country")
plt.xlabel("\u200A".join("GDP"))
#I spent forever figuring out how to edit the default font so "GDP" and "Year" didn't
#look so squished in axis labels. Couldn't do it so this is my filthy workaround.
#If you have a better solution I'm 110% ears.
plt.ylabel("Life Expectancy at Birth (years)")
plt.legend(title="Country", loc="lower right")
plt.show()
plt.clf()

"""This would appear to show a strong linear relationship between GDP and Life
Expectancy, although Zimbabwe has some irregularities. Let's look at a separate
plot for each country."""

fig, axs = plt.subplots(2, 3, figsize=(15,10), tight_layout=True)
countryct=0
for ax in axs.flat:
    data = leag_data[leag_data.country == countries[countryct]]
    ax.scatter(data.GDP,data.life_expectancy)
    model = sm.OLS.from_formula("life_expectancy ~ GDP", data=data)
    results = model.fit()
    ax.plot(data.GDP,
             results.params[0] + results.params[1]*data.GDP,
             color="r",
             label="OLS Regression Model")
    ax.set_title(countries[countryct], fontsize="x-large")
    ax.set_xlabel("\u200A".join("GDP"))
    ax.set_ylabel("Life Expectancy at Birth (years)")
    ax.legend(loc="lower right")
    countryct += 1
fig.suptitle("Life Expectancy vs GDP by Country", fontsize="xx-large")
plt.show()
plt.clf()

#Now let's create similar figures for both GDP and Life Expectancy over time
#by country

fig, axs = plt.subplots(2, 3, figsize=(15,10), tight_layout=True)
countryct=0
for ax in axs.flat:
    data = leag_data[leag_data.country == countries[countryct]]
    years = [int(x) for x in data.year.tolist() if (x+1)%3 == 0]
    years.sort()
    ax.plot(data.year, data.GDP)
    ax.set_title(countries[countryct], fontsize="x-large")
    ax.set_xlabel("\u200A".join("Year"))
    ax.set_ylabel("\u200A".join("GDP"))
    ax.set_xticks(years)
    ax.grid(visible=True, axis="x", linestyle="--")
    countryct += 1
fig.suptitle("GDP Over Time by Country", fontsize="xx-large")
plt.show()
plt.clf()

fig, axs = plt.subplots(2, 3, figsize=(15,10), tight_layout=True)
countryct=0
for ax in axs.flat:
    years = [int(x) for x in data.year.tolist() if (x+1)%3 == 0]
    years.sort()
    data = leag_data[leag_data.country == countries[countryct]]
    ax.plot(data.year, data.life_expectancy)
    ax.set_title(countries[countryct], fontsize="x-large")
    ax.set_xlabel("\u200A".join("Year"))
    ax.set_ylabel("Life Expectancy at Birth (years)")
    ax.set_xticks(years)
    ax.grid(visible=True, axis="x", linestyle="--")
    countryct += 1
fig.suptitle("Life Expectancy Over Time by Country", fontsize="xx-large")
plt.show()
plt.clf()

#I think it makes sense to do these as a single figure instead of one for each
#country, let's try that as well
years = [int(x) for x in leag_data.year.unique().tolist()]
years.sort()

fig, ax = plt.subplots(figsize=(10,8), tight_layout=True)
for country in countries:
    data = leag_data[leag_data.country == country]
    ax.plot(data.year, data.GDP, label=country)
ax.set_title("GDP Over Time by Country", fontsize="xx-large")
ax.set_xlabel("\u200A".join("Year"))
ax.set_ylabel("\u200A".join("GDP"))
ax.set_xticks(years)
ax.grid(visible=True, axis="x", linestyle="--")
ax.legend()
plt.show()
plt.clf()

fig, ax = plt.subplots(figsize=(10,8), tight_layout=True)
for country in countries:
    data = leag_data[leag_data.country == country]
    ax.plot(data.year, data.life_expectancy, label=country)
ax.set_title("Life Expectancy Over Time by Country", fontsize="xx-large")
ax.set_xlabel("\u200A".join("Year"))
ax.set_ylabel("Life Expectancy at Birth (years)")
ax.set_xticks(years)
ax.grid(visible=True, axis="x", linestyle="--")
ax.legend()
plt.show()
plt.clf()

#Last but not least let's try out a bubble plot to see if we can do time, GDP,
#and Life Expectancy, and colorize for developed/developing. Or if that is
#completely impossible to parse.

fig, ax = plt.subplots(figsize=(10,8), constrained_layout=True,)
sns.scatterplot(data=leag_data,
                x="year",
                y="life_expectancy",
                size="GDP",
                hue="country",
                #I originally had status here, but swapped it out for country.
                sizes=(100,5000),
                alpha=0.3)
ax.set_xlabel("\u200A".join("Year"))
ax.set_ylabel("Life Expectancy at Birth (years)")
ax.set_xticks(years)
ax.grid(visible=True, axis="x", linestyle="--")
plt.legend(loc="lower left", bbox_to_anchor=(1,0), ncol=2)
plt.show()
plt.clf()
#Seems kind of useless, but there we go. I think it's because the order of
#magnitude between Zimbabwe and the USA's GDP is so great that the sizing
#doesn't provide any real meaningful info. Also that legend is awful but wygd.

"""
Findings:
After reviewing my plots as well as comparing with the sample solution, here
is what I've found.

There appears to be a strong linear relationship between GDP and life expectancy.
All 6 countries showed growth in both GDP and Life Expectancy over the sample
time period.
Zimbabwe had a dip in Life Expectancy around 2004, but had the strongest growth
in that category overall.
The USA dominates the field in GDP, but China showed the strongest increase.

On a more personal note, I need to learn more about using Seaborn. It's taught
in tandem with Pyplot, and while Seaborn seems both more robust and user-
friendly, I simply don't know it well enough to use it on it's own; and using
it alongside Pyplot is frustrating and messy. Could do with learning more about
legend formatting as well, and different plots to use.
Also, my choice to investigate "Developed" and "Developing" countries proved fruitless; in a dataset with only 6 countries, it never showed any meaningful info. This is mainly due to the fact that I could only infer those statuses from GDP, which was already being shown anywhere I wanted to use it.
"""
