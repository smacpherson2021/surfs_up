# Surfs Up Analysis

## Overview of the statistical analysis:

A company would like to open a surf shop in Oahu. More information about temperature trends is needed before opening the surf shop. Specifically, temperature data for the months of June and December in Oahu are needed, in order to determine if the surf and ice cream shop business is sustainable year-round.

## Results:

- The average tempature is similar between June and Dec being aproximately 75 and 71 degrees respectively. This suggests that tempatures on average are good to support both a surf and an ice cream shop year round.

- The min tempature in Dec, at 56 degrees, is cooler then the min June temperature of 64. This suggests that there might be less sales for ice cream in the month of December

- December has a higher standard deviation then June. This indicates that the temperature spread between days in December is larger then in the month of June. Sales could be less consistant during this month. 

![June_Temps.png](https://github.com/smacpherson2021/surfs_up/blob/main/Resources/June_Temps.png)

![Dec_Temps.png](https://github.com/smacpherson2021/surfs_up/blob/main/Resources/Dec_Temps.png)

## Summary:

There is a high-level summary of the results and there are two additional queries to perform to gather more weather data for June and December.

- While average tempatures in June and December are similar an additional quere should be run to make sure these results are not cause by any outliers in the data. The standard deviation suggests there is a greater tempature spread in December so we would want to see how many days were close to the average vs not. This query would give us a better sense of how many days would be good for sales in each month using a catigorization like:
    * "Close to average" being +-5 degrees from average
    * "Below average" being more then 5 degrees less then the average
    * "Above average" being 5 degrees or more then then average

- 