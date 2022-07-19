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

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#importing the data as leag_data (Life Expectancy and GDP)
leag_data = pd.read_csv("all_data.csv")
#cleaning column names
leag_data.columns = ["country", "year", "life_expectancy", "GDP"]
#print(leag_data.head())
print(leag_data.info())
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
developed = ["China", "Germany", "United States of America"]

deving_data = leag_data[leag_data.country.isin(developing)]
devd_data = leag_data[leag_data.country.isin(developed)]

# =============================================================================
print(countries)
# print(deving_data.head())
# print(devd_data.head())
# =============================================================================

#96 total entries shouldn't be too messy, so let's first look at gdp vs
#life expectancy for the whole set

sns.scatterplot(
    x=leag_data.GDP,
    y=leag_data.life_expectancy,
    hue=leag_data.country,
    palette="colorblind"
    )
plt.title("Life Expectancy vs GDP by country")
plt.xlabel()
