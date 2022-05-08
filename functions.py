#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from mpl_toolkits.mplot3d import axes3d
import seaborn as sns


# In[10]:


GDP_data = pd.read_csv("GDP.csv")
fr2 = pd.read_csv("exports and imports of india(1997-2022) - exports and imports.csv")
fr3 =  pd.read_csv("india_population.csv") 
Export_data = pd.read_csv("2018-2010_export.csv")
Trade_data = pd.read_csv("Trade_data.csv")
file2= pd.read_csv("GDP.csv")


# In[11]:


def clean_data(file1,file3):
    """

    :param file1: GDP data containing the values of GDP for all countries
    :param file3: Import, export, trade balance of all countries in the world
    :return: cleaned and combined dataframe of the above two files
    """
    global final_stacked
    for i in range(1960, 2010):
        file1 = file1.drop(columns = str(i))
    file2 = file1.drop(columns = ['Indicator Name', 'Indicator Code', 'Country Code'])
    file2 = file2.set_index('Country Name')
    file2 = file2.stack()
    df = pd.DataFrame(file2)
    final_stacked = df.index.set_names('Year', level=len(df.index.names)-1, inplace=True)
    final_stacked= df.reset_index().rename(columns={0:'GDP'})
    final_stacked['Country Name'] = final_stacked['Country Name'].str.upper()
    final_stacked['Year'] =final_stacked['Year'].str.replace(',','')
    final_stacked= final_stacked.astype({"Year": "int"})
    file3 = file3.drop(columns = ['Year(end)'])
    file3['Country'] = file3['Country'].str.upper()
    combined = pd.merge(left=file3 , right=final_stacked, left_on=['Country', 'Year(start)'], right_on=['Country Name', 'Year'], how='inner')
    return combined


# In[12]:


cleaned_data = clean_data(GDP_data, fr2)
cleaned_data


# In[13]:


def refine_more(filename):
    """

    :param filename: Combined dataframe of GDPs, Import, Export and trade balance of all countries in the world
    :return: Cleaned file
    """
    filename['Total Trade'] = filename['Total Trade'].str.replace(',','')
    filename['Export'] = filename['Export'].str.replace(',','')
    filename['Import'] = filename['Import'].str.replace(',','')
    filename['Trade Balance'] = filename['Trade Balance'].str.replace(',','')
    filename['Total Trade'] = filename['Total Trade'].astype(float)
    filename['Export'] = filename['Export'].astype(float)
    filename['Import'] = filename['Import'].astype(float)
    filename['Trade Balance'] = filename['Trade Balance'].astype(float)
    return filename


# In[14]:


refined_data = refine_more(cleaned_data) 
refined_data


# In[15]:


def filtering_countries(filename, country):
    """

    :param filename: File containing Import, export, trade balance of all countries in the world
    :param country: Passing country name China
    :return: dataframe containing trade details of China
    """
    new = filename.loc[filename['Country'] == country]
    year = new.loc[:, ["Export", "Import", "Country", "Year"]]
    year = year.set_index(["Country", "Year"])
    year = year.groupby(["Country", "Year"]).apply(lambda x: x.sort_values (["Country", "Year"]))
    return year


# In[16]:


def plotting(filename, country):
    """

    :param filename: passing GraphAF function for the China file
    :param country: passing China because trade deficit with China is being calculated
    :return: A bar chart
    """
    Graph = filename.plot(kind = 'bar', figsize =(30,10), title = country)
    return Graph


# In[17]:


GraphAF = filtering_countries(refined_data, "CHINA P RP")
plotting(GraphAF, "CHINA P RP")



# In[21]:


def arrange_TradeData(file):
    """

    :param file: CSV file containing Trade data of all the counties in the world
    :return: cleaned dataframe
    """

    file = file.drop(columns = ['Country Code','Indicator Name','Indicator Code'])
    file = file.set_index('Country Name')
    file = file.stack()
    final_stacked_Trade = file.index.set_names('Year', level=len(file.index.names)-1, inplace=True)
    final_stacked_Trade = file.reset_index().rename(columns={0:'Net_Trade'})
    final_stacked_Trade = pd.DataFrame(final_stacked_Trade)
    final_stacked_Trade ['Country Name'] = final_stacked_Trade ['Country Name'].str.upper()
    final_stacked_Trade['Net_Trade'] = final_stacked_Trade['Net_Trade'].astype('float')
    final_stacked_Trade['Year'] = final_stacked_Trade['Year'].astype('int')
    return final_stacked_Trade


# In[22]:


Trade_data1 = arrange_TradeData(Trade_data)


# In[23]:


def filter_def(filename):
    """

    :param filename: Passing the function calling Trade_data1 containing clean dataframe
    :return: names of the countries with a trade deficit of more than 9 years in the last 10 years
    """
    df = filename[(filename['Year'] > 2009 ) & (filename['Year'] < 2021) & (filename['Net_Trade'] < 0)]
    df2 = df.groupby('Year').apply(lambda x: x.sort_values(by = 'Net_Trade', ascending = True).head(5))
    df3 = df2.groupby('Country Name').count() > 9 
    df4 = df3.loc[df3['Year'] == True]
    print(df4)


# In[24]:


filter_def(Trade_data1)


# In[25]:


def plot_country(filename, country1, country2):
    """

    :param filename: Passing the function calling Trade_data1 containing clean dataframe
    :param country1: India
    :param country2: United states
    :return: A bar chart representing trade deficit pattern for India and United states for the last 10 years
    """
    df = filename[(filename['Year'] > 2009 ) & (filename['Year'] < 2021) & (filename['Net_Trade'] < 0)]
    df2 = df.loc[df['Country Name'].isin([country1, country2])]
    sns.set()
    sns.catplot(x='Year', hue='Country Name', col='Country Name', y='Net_Trade', data=df2, kind='bar', col_wrap=3)


# In[26]:


plot_country(Trade_data1, 'INDIA', 'UNITED STATES')


# In[27]:


def arrange_GDP_data(file):
    """

    :param file: file containing GDP values for all the countries in the world for more than past 30 years
    :return: Dataframe containing GDP values of India and United States for last 10 years
    """
    for i in range(1960, 2010):
        file = file.drop(columns = str(i))
    file = file.drop(columns = ['Indicator Name', 'Indicator Code', 'Country Code'])
    file = file.set_index('Country Name')
    file = file.stack()
    df_GDP = pd.DataFrame(file)
    final_stacked_GDP = df_GDP.index.set_names('Year', level=len(df_GDP.index.names)-1, inplace=True)
    final_stacked_GDP = df_GDP.reset_index().rename(columns={0:'GDP'})
    final_stacked_GDP['GDP'] = round(final_stacked_GDP['GDP']/1000000,2)
    India = final_stacked_GDP.loc[final_stacked_GDP['Country Name'] == 'India']
    United_States = final_stacked_GDP.loc[final_stacked_GDP['Country Name'] == 'United States']
    combined_GDP = pd.merge(India, United_States, on='Year', how='outer')
    return combined_GDP


# In[28]:


Final_GDP = arrange_GDP_data(file2)
Final_GDP


# In[31]:


def mineral_sorting(file):
    """

    :param file: file containing the commodity value of various commodities for the more than past 20 years
    :return: Dataframe containing commodity value of Mineral fuels and Natural gems for past 10 years
    """
    file = file.drop(columns = ['country', 'HSCode'])
    file = file.set_index(['year','Commodity'])
    df = file.groupby(["year","Commodity"])['value'].sum()
    df = df.reset_index(name='value')
    df = df.groupby('year').apply(lambda x: x.sort_values(by = 'value', ascending = False).head(2))
    df.index = df.index.droplevel()
    df2 = df['year'].tolist()
    df3 = df['Commodity'].tolist()
    df4 = df['value'].tolist()
    arrays = [df2,df3]
    tuples = list(zip(*arrays))
    index = pd.MultiIndex.from_tuples(tuples, names=['year', 'Commodity']) 
    final_df = pd.DataFrame({'value': df4}, index=index)
    final_df = final_df.unstack(level = 1)
    final_df = final_df.value.rename_axis([None], axis=1).reset_index()
    final_df.rename(columns = {'MINERAL FUELS, MINERAL OILS AND PRODUCTS OF THEIR DISTILLATION; BITUMINOUS SUBSTANCES; MINERAL WAXES.':'Mineral_Fuels', 'NATURAL OR CULTURED PEARLS,PRECIOUS OR SEMIPRECIOUS STONES,PRE.METALS,CLAD WITH PRE.METAL AND ARTCLS THEREOF;IMIT.JEWLRY;COIN.':'Natural_Gems'}, inplace = True)
    return final_df
    


# In[32]:


final_export = mineral_sorting(Export_data)
final_export


# In[ ]:




