# 2022Spring_Finals
Final project for the course IS 597


**_The Influence of Imports and Exports of a Country on the GDP_**

**Created By:** Aayusha Sheregar and Nuka Rishitha

**Goal:** The goal of this project is to understand whether the exporting and importing activities of a country affects its GDP with the help of data analysis.


**HYPOTHESIS 1:**

**Article used:**  https://www.jagranjosh.com/general-knowledge/list-of-top-10-export-and-import-source-of-india-1584105230-1
  
"As per the article, India is in a trade deficit with China since the past 10 years hence, this could affect its GDP.”

Trade deficit is the amount by which the cost of a country's imports exceeds the value of its exports. GDP is the total value of goods produced and services provided in a country during one year. This hypothesis explores if the 10 year long trade deficit with China impacts India's GDP. 

<img src="https://thumbs.dreamstime.com/z/china-yuan-renminbi-indian-rupee-currency-banknotes-asia-money-india-179218360.jpg" height = "400" width="600"/> 

Conclusion: Below are 2 images, a bar chart representing India's Imports and Exports and a line graph illustrating India's GDP over a certain period. As seen in the bar chart created, we have proven with data analysis the statement that India is in a trade deficit with China since a long period of time. But the line graph is proof that this trade deficit hasn't affected the Indian GDP. There could be many factors that could affect its GDP. Therefore, we reject this hypothesis.

<div class="container"> 
<img src= "https://github.com/Nuka-Rishitha/2022Spring_Finals/blob/main/Screenshots/hyp1.1.PNG" height = "500" width="700"/>
<img src= "https://github.com/Nuka-Rishitha/2022Spring_Finals/blob/main/Screenshots/hyp1.2.PNG" height = "500" width="700"/>
</div>

We were curious to know what factors could have an effect on the GDP. While researching we came across many factors such as mortality, rate of inflation, poverty etc. One factor that we found worth discussing was the "Population Density", hence, we went a step further to prove whether Population Density infact, does affect the GDP. 

Conclusion: As shown in the graph below it is clear that as there was an increase in the population, there was an increase in the GDP as well. Hence, we have proven that Population Density could also be a factor that could influence GDP.

<img src= "https://github.com/Nuka-Rishitha/2022Spring_Finals/blob/main/Screenshots/hyp1.2.PNG" height = "500" width="700"/>
<img src= "https://github.com/Nuka-Rishitha/2022Spring_Finals/blob/main/Screenshots/hyp1.3.PNG" height = "400" width="900"/>


**HYPOTHESIS 2:**

"ALL countries with a trade deficit for past 10 years in a row have a direct effect on their GDP."

As proven with the help of multiple bar charts and line charts in hypothesis 1, we can say that even though India is in a trade deficit with China over several years, it’s GDP seems to not be affected by this factor and there could be other factors involved. This example was of a granular level specific to only one country, China. What we wanted to find further is if a long-term trade deficit affects most, if not all countries’ GDP negatively. 

<img src= "https://securecdn.pymnts.com/wp-content/uploads/2020/04/gdp-decline-q1.jpg" height = "400" width="550"/>

This hypothesis is an expansion of hypothesis 1 and dives further into proving whether trade deficit in ALL countries impacts it's GDP. 

Conclusion: We performed EDA on the dataset to clean it and found out that 2 countries, India and the United States have been in trade deficit for almost all the years. As shown below, in India’s case we can see that there was an increase in the net trade from 2019-2020 whereas for the United states, there were many fluctuations. 

<img src= "https://github.com/Nuka-Rishitha/2022Spring_Finals/blob/main/Screenshots/hyp2.1.PNG" height = "500" width="800"/>

It is clear by looking at the line graphs below,that even though there was an increase in India’s net trade from 2019-2020, there was a significant dip in it’s GDP. The United States also had fluctuations in the net trade but we see a steady increase in its GDP. Hence, we can say that there is no direct relation with a countries’ net trade and GDP. Hence, we reject the hypothesis.


<div class="container"> 
<img src= "https://github.com/Nuka-Rishitha/2022Spring_Finals/blob/main/Screenshots/hyp2.2.PNG" height = "300" width="400"/>
<img src= "https://github.com/Nuka-Rishitha/2022Spring_Finals/blob/main/Screenshots/hyp2.3.PNG" height = "300" width="400"/>
</div>



**HYPOTHESIS 3:**

"The global demand slow down and fall in crude oil prices during the period 2014-16 affected India’s exports of mineral fuel."

<img src= "https://i.pinimg.com/originals/d7/c6/38/d7c638bec03ac2fea730f145aaad8bc8.jpg" height = "400" width="500"/>

The world saw a global demand slowdown and reduction in crude oil prices in the year 2014. Since India's highest exported product is Mineral Fuels, with the help of this hypothesis we wanted to dig deeper and understand how both these situations have had an effect on the exporting trends of India from the year 2014-2016.

<img src= "https://github.com/Nuka-Rishitha/2022Spring_Finals/blob/main/Screenshots/hyp3.1.PNG" height = "400" width="800"/>

Conclusion: After thorough data analysis, we found that the top 2 commodities of Indian exports were Mineral Fuels and Natural Gems. After thorough Data Analysis we could prove that the export of Mineral Fuels decreased since the year 2014, stabilized and finally picked up in the year 2018. Hence, we have proven with the help of visualizations that the global demand slowdown did have a negative effect on the exports. Therefore, we accept the hypothesis.


<img src= "https://github.com/Nuka-Rishitha/2022Spring_Finals/blob/main/Screenshots/hyp%203.2.PNG" height = "400" width="800"/>

Some additional statistical considerations such as correlation with the help of heatmaps...

<img src= "https://github.com/Nuka-Rishitha/2022Spring_Finals/blob/main/Screenshots/heat1.PNG" height = "400" width="800"/>

The above heatmap shows a correlation between components like Export, Import, Total Trade, Trade Balance and GDP. It shows the extent to which each component is affected by the other. You can see that Import and Trade Balance are highly negatively correlated which means they are inversely proportional. Higher the Imports, lower is the Trade Balance.


<img src= "https://github.com/Nuka-Rishitha/2022Spring_Finals/blob/main/Screenshots/heat2.PNG" height = "400" width="800"/>

The above visual is a heatmap that demonstrates the progress of the net trade of the top 5 countries over the years 2015-2020. As shown above, it is clear that Euro area has had a high net trade over the overs whereas, China has seen significant fluctuations throughout. Other countries have seen a constant net trade.


Some of the sources used:
https://stackoverflow.com/questions/32998893/set-column-names-when-stacking-pandas-dataframe#:~:text=To%20avoid%20a%20phantom%20column%20name%20when%20calling,A%202%20B%202%20C%202%20dtype%3A%20int64

https://plotly.com/python/px-arguments/

https://pythonguides.com/matplotlib-plot-bar-chart/#:~:text=You%20can%20use%20the%20function%20bar%20%28%29%20of,matplotlib.pyplot.bar%20%28categories%2C%20heights%20%20%20width%2C%20bottom%2C%20align%2C...%5D%29%26%5D

Contributions:
Both of us worked together in formulating and testing the Hypothesis-1 and also played an equal part in preparing the Presentation. 
Rishitha worked on the idea and code for Hypothesis -2. Aayusha worked on the idea and code for Hypothesis-3.  


