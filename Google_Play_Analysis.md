![Google-Play-Logo.png](attachment:Google-Play-Logo.png)

# Google_Play_Analysis
##### Author: Rodrigo Martinez Mina

## Introduction

In today's digital age, mobile applications have become an integral part of our daily lives. With over 3.5 million android apps available on the Google Play Store, it can be difficult for developers to create a successful app that stands out in a crowded market. By analyzing trends and patterns within the app market, developers and marketers can gain valuable insights that can inform their decisions and improve the performance of their apps.

The goal of this data analysis project is to identify these insights and provide actionable recommendations for app developers and marketers. 

For this analysis, we will be using SQL to extract information from the Google Play apps database, which can be found on Kaggle.


```python
# Regenate magic sql command. 
%reload_ext sql
```


```python
# To Jupyter notebook with database personal administrator 
%sql postgresql://postgres:1@localhost:5432/postgres
```

## Data Exploration and Cleaning

In order to execute SQL commands we are gonna need to import 'sqlalchemy' library which provides a interface interact with SQL databases. While pandas offers integration with SQL databases using 'read_sql' function.


```python
# Import the packages and libraries required
from sqlalchemy import create_engine
import pandas as pd
```


```python
# Import csv file into a pandas dataframe
df = pd.read_csv('Desktop/Data/google_play_data_cleaned.csv')
```


```python
engine = create_engine("postgresql://postgres:1@localhost:5432/postgres")
df.to_sql('google_play_data', con=engine, if_exists='replace', index=False)
```




    196




```python
# Check the sql commands, extracting the 5 first rows of our dataset
%sql SELECT * FROM google_play_data LIMIT 5;
```

     * postgresql://postgres:***@localhost:5432/postgres
    5 rows affected.





<table>
    <thead>
        <tr>
            <th>index</th>
            <th>app</th>
            <th>category</th>
            <th>rating</th>
            <th>reviews</th>
            <th>installs</th>
            <th>type</th>
            <th>price</th>
            <th>content_rating</th>
            <th>genres</th>
            <th>update_month</th>
            <th>update_year</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>House party - live chat</td>
            <td>DATING</td>
            <td>1.0</td>
            <td>1</td>
            <td>10</td>
            <td>0</td>
            <td>0.0</td>
            <td>Mature 17+</td>
            <td>Dating</td>
            <td>7</td>
            <td>2018</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Speech Therapy: F</td>
            <td>FAMILY</td>
            <td>1.0</td>
            <td>1</td>
            <td>10</td>
            <td>1</td>
            <td>2.99</td>
            <td>Everyone</td>
            <td>Education</td>
            <td>10</td>
            <td>2016</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Clarksburg AH</td>
            <td>MEDICAL</td>
            <td>1.0</td>
            <td>1</td>
            <td>50</td>
            <td>0</td>
            <td>0.0</td>
            <td>Everyone</td>
            <td>Medical</td>
            <td>5</td>
            <td>2017</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Truck Driving Test Class 3 BC</td>
            <td>FAMILY</td>
            <td>1.0</td>
            <td>1</td>
            <td>50</td>
            <td>1</td>
            <td>1.49</td>
            <td>Everyone</td>
            <td>Education</td>
            <td>4</td>
            <td>2012</td>
        </tr>
        <tr>
            <td>5</td>
            <td>BJ Bridge Standard American 2018</td>
            <td>GAME</td>
            <td>1.0</td>
            <td>1</td>
            <td>1000</td>
            <td>0</td>
            <td>0.0</td>
            <td>Everyone</td>
            <td>Card</td>
            <td>5</td>
            <td>2018</td>
        </tr>
    </tbody>
</table>




```python
# Count the number of rows in our dataset
%sql SELECT COUNT(*) FROM google_play_data
```

     * postgresql://postgres:***@localhost:5432/postgres
    1 rows affected.





<table>
    <thead>
        <tr>
            <th>count</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>8196</td>
        </tr>
    </tbody>
</table>



For this project, we're gonna be evaluating 8,196 apps available in google play store. 


```python
# This command retrieves the columns name of our dataset and its datatype
%sql SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'google_play_data' 
ORDER BY column_name;
```

     * postgresql://postgres:***@localhost:5432/postgres
    12 rows affected.





<table>
    <thead>
        <tr>
            <th>column_name</th>
            <th>data_type</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>app</td>
            <td>text</td>
        </tr>
        <tr>
            <td>category</td>
            <td>text</td>
        </tr>
        <tr>
            <td>content_rating</td>
            <td>text</td>
        </tr>
        <tr>
            <td>genres</td>
            <td>text</td>
        </tr>
        <tr>
            <td>index</td>
            <td>bigint</td>
        </tr>
        <tr>
            <td>installs</td>
            <td>bigint</td>
        </tr>
        <tr>
            <td>price</td>
            <td>double precision</td>
        </tr>
        <tr>
            <td>rating</td>
            <td>double precision</td>
        </tr>
        <tr>
            <td>reviews</td>
            <td>bigint</td>
        </tr>
        <tr>
            <td>type</td>
            <td>bigint</td>
        </tr>
        <tr>
            <td>update_month</td>
            <td>bigint</td>
        </tr>
        <tr>
            <td>update_year</td>
            <td>bigint</td>
        </tr>
    </tbody>
</table>



This dataset is composed by 12 columns. Here a brief explanatio of each column:

* **app:** The name of the application
* **category:** The category the application belongs to
* **content_rating:** The content rating assigned to the application (Everyone, Teen, Mature=17, Adults only 18+)
* **genres:** The genre the application belongs to
* **index:** Index number of the application in the dataset
* **installs:** Number of installs of the application
* **price:** Price of the application 
* **rating:** Average rating of the application 
* **reviews:** Number of reviews of the application 
* **type:** Type of the application (free or paid)
* **update_month:** The month when the application was last updated 
* **update_year:** The yar when the application was last updated 

Additionally, it is important to note that the command mentioned above also displays the data type of each column. For the numeric columns, we plan to convert them to integer or decimal data type instead of bigint or double precision for ease of analysis.  


```python
# To change the data type of some columns to integer
%%sql ALTER TABLE google_play_data 
ALTER COLUMN index TYPE INTEGER, 
ALTER COLUMN installs TYPE INTEGER, 
ALTER COLUMN price TYPE INTEGER,
ALTER COLUMN rating TYPE DECIMAL, 
ALTER COLUMN reviews TYPE DECIMAL,
ALTER COLUMN type TYPE INTEGER,
ALTER COLUMN update_month TYPE INTEGER, 
ALTER COLUMN update_year TYPE INTEGER;
```

     * postgresql://postgres:***@localhost:5432/postgres
    Done.





    []




```python
# We will use this command to verify that the changes have been made correctly
%%sql SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'google_play_data' 
ORDER BY column_name;
```

     * postgresql://postgres:***@localhost:5432/postgres
    12 rows affected.





<table>
    <thead>
        <tr>
            <th>column_name</th>
            <th>data_type</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>app</td>
            <td>text</td>
        </tr>
        <tr>
            <td>category</td>
            <td>text</td>
        </tr>
        <tr>
            <td>content_rating</td>
            <td>text</td>
        </tr>
        <tr>
            <td>genres</td>
            <td>text</td>
        </tr>
        <tr>
            <td>index</td>
            <td>integer</td>
        </tr>
        <tr>
            <td>installs</td>
            <td>integer</td>
        </tr>
        <tr>
            <td>price</td>
            <td>integer</td>
        </tr>
        <tr>
            <td>rating</td>
            <td>numeric</td>
        </tr>
        <tr>
            <td>reviews</td>
            <td>numeric</td>
        </tr>
        <tr>
            <td>type</td>
            <td>integer</td>
        </tr>
        <tr>
            <td>update_month</td>
            <td>integer</td>
        </tr>
        <tr>
            <td>update_year</td>
            <td>integer</td>
        </tr>
    </tbody>
</table>



The numeric columns have been converted to the desired data type for efficient analysis


```python
# Counting the total number of rows where there's a missing value.
%sql SELECT COUNT(*) 
FROM google_play_data 
WHERE price IS NULL OR reviews IS NULL
```

     * postgresql://postgres:***@localhost:5432/postgres
    1 rows affected.





<table>
    <thead>
        <tr>
            <th>count</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0</td>
        </tr>
    </tbody>
</table>



In this case, our dataset doesn't contain any missing values, ensuring that all rows and columns have complete data. 

## Problems

After verifying and cleaning our dataset, we can now proceed with addressing any issues and analyzing the data. The goal of this project is to answer the following questions:"

- What are the top 10 most popular apps based on the number of installs, and what is the average rating of this apps?
- Which category has the most number of apps in the database?
- How many apps in the database are free and how many are paid?
- How many apps are in the database for each content-rating category? 
- What are the top 10 most expensive apps across all categories?
- Which app category has the highest average rating, and which has the lowest?
- How do the number of reviews vary by app category, and is there a relationship between the number of reviews and the rating of the app?
- What is the most common app type (free or paid) according to the number of installs?
- What is the average price of paid apps by category?
- Which app genres are most commonly associated with high-rated apps, and which genres are most commonly associated with low-rated apps?
- How many apps in the database have a rating above 4.5, and what is the distribution of these apps across different categories?

## Data Analysis

### What are the top 10 most popular apps based on the number of installs, and what is the average rating of this apps?


```python
# Top 10 most popular apps according to the number of installs 
%%sql SELECT app, installs, rating 
FROM google_play_data 
ORDER BY installs DESC 
LIMIT 10;
```

     * postgresql://postgres:***@localhost:5432/postgres
    10 rows affected.





<table>
    <thead>
        <tr>
            <th>app</th>
            <th>installs</th>
            <th>rating</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Google+</td>
            <td>1000000000</td>
            <td>4.2</td>
        </tr>
        <tr>
            <td>Google Street View</td>
            <td>1000000000</td>
            <td>4.2</td>
        </tr>
        <tr>
            <td>Messenger – Text and Video Chat for Free</td>
            <td>1000000000</td>
            <td>4</td>
        </tr>
        <tr>
            <td>Skype - free IM &amp; video calls</td>
            <td>1000000000</td>
            <td>4.1</td>
        </tr>
        <tr>
            <td>Google Play Movies &amp; TV</td>
            <td>1000000000</td>
            <td>3.7</td>
        </tr>
        <tr>
            <td>Facebook</td>
            <td>1000000000</td>
            <td>4.1</td>
        </tr>
        <tr>
            <td>Google Play Books</td>
            <td>1000000000</td>
            <td>3.9</td>
        </tr>
        <tr>
            <td>Google News</td>
            <td>1000000000</td>
            <td>3.9</td>
        </tr>
        <tr>
            <td>Hangouts</td>
            <td>1000000000</td>
            <td>4</td>
        </tr>
        <tr>
            <td>Google Chrome: Fast &amp; Secure</td>
            <td>1000000000</td>
            <td>4.3</td>
        </tr>
    </tbody>
</table>



The table includes the name of each application along with its corresponding number of installs and average rating. The number of installs for each application is the same at 1,000,000,000 (or 1 billion) installs, indicating that these are all extremely popular applications. The ratings for each application range from 3.7 to 4.3. 

It's interesting to note that many of the top 10 most popular applications in this dataset are developed by Google. That strong presence in the mobile app market may by a reflection of both the popularity of Google's brand and the quality of its applications (based on rating). 

### Which category has the most number of apps in the database?


```python
# Total number of applications in the dataset distributed by category
%%sql SELECT category, COUNT(app) AS number_of_apps 
FROM google_play_data 
GROUP BY category 
ORDER BY number_of_apps DESC 
LIMIT 15;
```

     * postgresql://postgres:***@localhost:5432/postgres
    15 rows affected.





<table>
    <thead>
        <tr>
            <th>category</th>
            <th>number_of_apps</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>FAMILY</td>
            <td>1608</td>
        </tr>
        <tr>
            <td>GAME</td>
            <td>912</td>
        </tr>
        <tr>
            <td>TOOLS</td>
            <td>718</td>
        </tr>
        <tr>
            <td>FINANCE</td>
            <td>302</td>
        </tr>
        <tr>
            <td>LIFESTYLE</td>
            <td>301</td>
        </tr>
        <tr>
            <td>PRODUCTIVITY</td>
            <td>301</td>
        </tr>
        <tr>
            <td>PERSONALIZATION</td>
            <td>298</td>
        </tr>
        <tr>
            <td>MEDICAL</td>
            <td>290</td>
        </tr>
        <tr>
            <td>PHOTOGRAPHY</td>
            <td>263</td>
        </tr>
        <tr>
            <td>BUSINESS</td>
            <td>263</td>
        </tr>
        <tr>
            <td>SPORTS</td>
            <td>260</td>
        </tr>
        <tr>
            <td>COMMUNICATION</td>
            <td>256</td>
        </tr>
        <tr>
            <td>HEALTH_AND_FITNESS</td>
            <td>244</td>
        </tr>
        <tr>
            <td>NEWS_AND_MAGAZINES</td>
            <td>204</td>
        </tr>
        <tr>
            <td>SOCIAL</td>
            <td>203</td>
        </tr>
    </tbody>
</table>



According to the dataset, the most common category is **Family** with 1608 applications. This category includes applications that are suitable for all members of a family, such as games, educational apps, and entertainment apps. 

Other popular categories include Game, Tools, Finance and Lifestyle.

### How many apps in the database are free and how many are paid?


```python
# Total number of applicatios by type (free or paid)
%%sql SELECT CASE WHEN type = 0 THEN 'Free' ELSE 'Paid' END AS type_app, 
            COUNT(app) AS number_of_apps 
FROM google_play_data 
GROUP BY type
```

     * postgresql://postgres:***@localhost:5432/postgres
    2 rows affected.





<table>
    <thead>
        <tr>
            <th>type_app</th>
            <th>number_of_apps</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Free</td>
            <td>7592</td>
        </tr>
        <tr>
            <td>Paid</td>
            <td>604</td>
        </tr>
    </tbody>
</table>



**The great majority of applications in this dataset are free, with 7592 applications.** This is not surprising, as the most of applications on app stores are free to download and use. These applications may generate revenue through advertising or in-app purchases. In this case, only 604 apps charge users upfront for the app.

### How many apps are in the database for each content-rating category?


```python
# The number of applications in the dataset based on their content rating
%%sql SELECT content_rating, COUNT(app) AS number_of_apps 
FROM google_play_data 
GROUP BY content_rating 
ORDER BY number_of_apps DESC; 
```

     * postgresql://postgres:***@localhost:5432/postgres
    5 rows affected.





<table>
    <thead>
        <tr>
            <th>content_rating</th>
            <th>number_of_apps</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Everyone</td>
            <td>6923</td>
        </tr>
        <tr>
            <td>Teen</td>
            <td>912</td>
        </tr>
        <tr>
            <td>Mature 17+</td>
            <td>357</td>
        </tr>
        <tr>
            <td>Adults only 18+</td>
            <td>3</td>
        </tr>
        <tr>
            <td>Unrated</td>
            <td>1</td>
        </tr>
    </tbody>
</table>



**The greater part of applications in the dataset have a content rating of Everyone with 6923 applications.** This rating indicates that the application is suitable for all ages and does not contain any objectionable content. The second most popular content rating is Teen with 912 applications. And finally, **there's around 360 applications that may contain more mature or explicit contain.**

Note: there's one application which its content rating was not specified. 

### What are the top 10 most expensive apps across all categories?


```python
# Top 10 most expensive paid applications and their respective category
%%sql SELECT app, category, price 
FROM google_play_data 
ORDER BY price DESC 
LIMIT 10;
```

     * postgresql://postgres:***@localhost:5432/postgres
    10 rows affected.





<table>
    <thead>
        <tr>
            <th>app</th>
            <th>category</th>
            <th>price</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>I&#x27;m Rich - Trump Edition</td>
            <td>LIFESTYLE</td>
            <td>400</td>
        </tr>
        <tr>
            <td>I am rich (Most expensive app)</td>
            <td>FINANCE</td>
            <td>399.99</td>
        </tr>
        <tr>
            <td>I am Rich!</td>
            <td>FINANCE</td>
            <td>399.99</td>
        </tr>
        <tr>
            <td>I am rich(premium)</td>
            <td>FINANCE</td>
            <td>399.99</td>
        </tr>
        <tr>
            <td>I am rich</td>
            <td>LIFESTYLE</td>
            <td>399.99</td>
        </tr>
        <tr>
            <td>I Am Rich Premium</td>
            <td>FINANCE</td>
            <td>399.99</td>
        </tr>
        <tr>
            <td>I am Rich Plus</td>
            <td>FAMILY</td>
            <td>399.99</td>
        </tr>
        <tr>
            <td>💎 I&#x27;m rich</td>
            <td>LIFESTYLE</td>
            <td>399.99</td>
        </tr>
        <tr>
            <td>I AM RICH PRO PLUS</td>
            <td>FINANCE</td>
            <td>399.99</td>
        </tr>
        <tr>
            <td>most expensive app (H)</td>
            <td>FAMILY</td>
            <td>399.99</td>
        </tr>
    </tbody>
</table>



This SQL command show the top 10 most expensive apps with their respective category and price. Curiously, all the apps in this list have similar names, which potentially may be offering similar functionality or features, but some of them belong to different categories. **The app I'm Rich - Trump Edition is the most expensive app of the dataset with a price of 400 dollars.** 

In a deeper investigation, all this apps (I'm Rich) were designed to displayed a glowing red diamond on a black background, accompanied by the words "I Am Rich" at the center of the screen. No app seems to claim to offer any additional features or functionality beyond that. 

### Which app category has the highest average rating, and which has the lowest?


```python
# App categories ordered by their average rating
%%sql SELECT category, ROUND(AVG(rating),2) as average_rating 
FROM google_play_data 
GROUP BY category 
ORDER BY average_rating DESC;
```

     * postgresql://postgres:***@localhost:5432/postgres
    33 rows affected.





<table>
    <thead>
        <tr>
            <th>category</th>
            <th>average_rating</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>EVENTS</td>
            <td>4.40</td>
        </tr>
        <tr>
            <td>ART_AND_DESIGN</td>
            <td>4.33</td>
        </tr>
        <tr>
            <td>PARENTING</td>
            <td>4.32</td>
        </tr>
        <tr>
            <td>BOOKS_AND_REFERENCE</td>
            <td>4.31</td>
        </tr>
        <tr>
            <td>EDUCATION</td>
            <td>4.28</td>
        </tr>
        <tr>
            <td>BEAUTY</td>
            <td>4.24</td>
        </tr>
        <tr>
            <td>PERSONALIZATION</td>
            <td>4.23</td>
        </tr>
        <tr>
            <td>HEALTH_AND_FITNESS</td>
            <td>4.20</td>
        </tr>
        <tr>
            <td>AUTO_AND_VEHICLES</td>
            <td>4.19</td>
        </tr>
        <tr>
            <td>SOCIAL</td>
            <td>4.16</td>
        </tr>
        <tr>
            <td>SPORTS</td>
            <td>4.14</td>
        </tr>
        <tr>
            <td>FOOD_AND_DRINK</td>
            <td>4.13</td>
        </tr>
        <tr>
            <td>GAME</td>
            <td>4.13</td>
        </tr>
        <tr>
            <td>FAMILY</td>
            <td>4.12</td>
        </tr>
        <tr>
            <td>SHOPPING</td>
            <td>4.11</td>
        </tr>
        <tr>
            <td>MEDICAL</td>
            <td>4.11</td>
        </tr>
        <tr>
            <td>WEATHER</td>
            <td>4.11</td>
        </tr>
        <tr>
            <td>COMICS</td>
            <td>4.11</td>
        </tr>
        <tr>
            <td>PRODUCTIVITY</td>
            <td>4.11</td>
        </tr>
        <tr>
            <td>LIBRARIES_AND_DEMO</td>
            <td>4.11</td>
        </tr>
        <tr>
            <td>LIFESTYLE</td>
            <td>4.09</td>
        </tr>
        <tr>
            <td>FINANCE</td>
            <td>4.07</td>
        </tr>
        <tr>
            <td>NEWS_AND_MAGAZINES</td>
            <td>4.05</td>
        </tr>
        <tr>
            <td>HOUSE_AND_HOME</td>
            <td>4.05</td>
        </tr>
        <tr>
            <td>ENTERTAINMENT</td>
            <td>4.04</td>
        </tr>
        <tr>
            <td>BUSINESS</td>
            <td>4.04</td>
        </tr>
        <tr>
            <td>PHOTOGRAPHY</td>
            <td>4.03</td>
        </tr>
        <tr>
            <td>COMMUNICATION</td>
            <td>4.00</td>
        </tr>
        <tr>
            <td>VIDEO_PLAYERS</td>
            <td>3.98</td>
        </tr>
        <tr>
            <td>TOOLS</td>
            <td>3.97</td>
        </tr>
        <tr>
            <td>TRAVEL_AND_LOCAL</td>
            <td>3.96</td>
        </tr>
        <tr>
            <td>MAPS_AND_NAVIGATION</td>
            <td>3.95</td>
        </tr>
        <tr>
            <td>DATING</td>
            <td>3.95</td>
        </tr>
    </tbody>
</table>



The table above show the 33 different categories that contains the dataset. **The category with the higher average rating in their apps is Event with 4.40 over 5.** Other categories with similar average are Art & Design, Parenting and Books & Reference. 
In other hand, **the categories with the lowest average rating is Dating and Maps & Navigation with 3.95 over 5.** 

### How do the number of reviews vary by app category, and is there a relationship between the number of reviews and the rating of the app?


```python
# Total reviews and average rating of the application in every category 
%%sql SELECT category, sum(reviews) as total_reviews, ROUND(avg(rating),2) as total_rating 
FROM google_play_data 
GROUP BY category 
ORDER BY total_rating DESC, total_reviews DESC;
```

     * postgresql://postgres:***@localhost:5432/postgres
    33 rows affected.





<table>
    <thead>
        <tr>
            <th>category</th>
            <th>total_reviews</th>
            <th>total_rating</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>EVENTS</td>
            <td>160590</td>
            <td>4.40</td>
        </tr>
        <tr>
            <td>ART_AND_DESIGN</td>
            <td>1419135</td>
            <td>4.33</td>
        </tr>
        <tr>
            <td>PARENTING</td>
            <td>953609</td>
            <td>4.32</td>
        </tr>
        <tr>
            <td>BOOKS_AND_REFERENCE</td>
            <td>16720905</td>
            <td>4.31</td>
        </tr>
        <tr>
            <td>EDUCATION</td>
            <td>13363372</td>
            <td>4.28</td>
        </tr>
        <tr>
            <td>BEAUTY</td>
            <td>395133</td>
            <td>4.24</td>
        </tr>
        <tr>
            <td>PERSONALIZATION</td>
            <td>53542755</td>
            <td>4.23</td>
        </tr>
        <tr>
            <td>HEALTH_AND_FITNESS</td>
            <td>21361234</td>
            <td>4.20</td>
        </tr>
        <tr>
            <td>AUTO_AND_VEHICLES</td>
            <td>1163630</td>
            <td>4.19</td>
        </tr>
        <tr>
            <td>SOCIAL</td>
            <td>227927470</td>
            <td>4.16</td>
        </tr>
        <tr>
            <td>SPORTS</td>
            <td>35348212</td>
            <td>4.14</td>
        </tr>
        <tr>
            <td>GAME</td>
            <td>622295937</td>
            <td>4.13</td>
        </tr>
        <tr>
            <td>FOOD_AND_DRINK</td>
            <td>6324707</td>
            <td>4.13</td>
        </tr>
        <tr>
            <td>FAMILY</td>
            <td>143822304</td>
            <td>4.12</td>
        </tr>
        <tr>
            <td>PRODUCTIVITY</td>
            <td>55590391</td>
            <td>4.11</td>
        </tr>
        <tr>
            <td>SHOPPING</td>
            <td>44551541</td>
            <td>4.11</td>
        </tr>
        <tr>
            <td>WEATHER</td>
            <td>12295124</td>
            <td>4.11</td>
        </tr>
        <tr>
            <td>COMICS</td>
            <td>2340740</td>
            <td>4.11</td>
        </tr>
        <tr>
            <td>MEDICAL</td>
            <td>1182651</td>
            <td>4.11</td>
        </tr>
        <tr>
            <td>LIBRARIES_AND_DEMO</td>
            <td>903248</td>
            <td>4.11</td>
        </tr>
        <tr>
            <td>LIFESTYLE</td>
            <td>11831656</td>
            <td>4.09</td>
        </tr>
        <tr>
            <td>FINANCE</td>
            <td>12661784</td>
            <td>4.07</td>
        </tr>
        <tr>
            <td>NEWS_AND_MAGAZINES</td>
            <td>23129264</td>
            <td>4.05</td>
        </tr>
        <tr>
            <td>HOUSE_AND_HOME</td>
            <td>1929466</td>
            <td>4.05</td>
        </tr>
        <tr>
            <td>ENTERTAINMENT</td>
            <td>34762650</td>
            <td>4.04</td>
        </tr>
        <tr>
            <td>BUSINESS</td>
            <td>9889779</td>
            <td>4.04</td>
        </tr>
        <tr>
            <td>PHOTOGRAPHY</td>
            <td>105351227</td>
            <td>4.03</td>
        </tr>
        <tr>
            <td>COMMUNICATION</td>
            <td>285810907</td>
            <td>4.00</td>
        </tr>
        <tr>
            <td>VIDEO_PLAYERS</td>
            <td>67484072</td>
            <td>3.98</td>
        </tr>
        <tr>
            <td>TOOLS</td>
            <td>229355702</td>
            <td>3.97</td>
        </tr>
        <tr>
            <td>TRAVEL_AND_LOCAL</td>
            <td>26819594</td>
            <td>3.96</td>
        </tr>
        <tr>
            <td>MAPS_AND_NAVIGATION</td>
            <td>17728954</td>
            <td>3.95</td>
        </tr>
        <tr>
            <td>DATING</td>
            <td>3623311</td>
            <td>3.95</td>
        </tr>
    </tbody>
</table>



**Based on a basic examination, there appears to be relationship between number of reviews and and the average rating by category.**

The categories with the highest average ratings, such as Events, Art & Design, and Parenting tend to have a lower number of total reviews compared to other categories. On the other hand, categories with lower average ratings, such as Tools, Travel & Local and Maps & Navigation tend to have a bigger number of total reviews.

However, it's important to understand that this is a preliminary analysis and further investigation would be needed to confirm any correlations between number of reviews and average rating by category.

### What is the most common app (free & paid) according to the number of installs?


```python
# Extracting the paid apps with the most number of downloads
%%sql 
SELECT app, type, MAX(installs) AS max_installs 
FROM google_play_data 
WHERE type = 1 AND installs = (SELECT max(installs) FROM google_play_data WHERE type = 1)
GROUP BY app, type 
ORDER BY max_installs DESC;
```

     * postgresql://postgres:***@localhost:5432/postgres
    2 rows affected.





<table>
    <thead>
        <tr>
            <th>app</th>
            <th>type</th>
            <th>max_installs</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Hitman Sniper</td>
            <td>1</td>
            <td>10000000</td>
        </tr>
        <tr>
            <td>Minecraft</td>
            <td>1</td>
            <td>10000000</td>
        </tr>
    </tbody>
</table>



Hitman Sniper and Minecraft are the most popular paid apps in the data set, with over 1 billion downloads


```python
# Extracting the free apps with the most number of downloads
%%sql 
SELECT app, type, MAX(installs) AS max_installs 
FROM google_play_data 
WHERE type = 0 AND installs = (SELECT MAX(installs) FROM google_play_data WHERE type = 0)
GROUP BY app, type 
ORDER BY max_installs DESC;
```

     * postgresql://postgres:***@localhost:5432/postgres
    20 rows affected.





<table>
    <thead>
        <tr>
            <th>app</th>
            <th>type</th>
            <th>max_installs</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Facebook</td>
            <td>0</td>
            <td>1000000000</td>
        </tr>
        <tr>
            <td>Gmail</td>
            <td>0</td>
            <td>1000000000</td>
        </tr>
        <tr>
            <td>Google</td>
            <td>0</td>
            <td>1000000000</td>
        </tr>
        <tr>
            <td>Google Chrome: Fast &amp; Secure</td>
            <td>0</td>
            <td>1000000000</td>
        </tr>
        <tr>
            <td>Google Drive</td>
            <td>0</td>
            <td>1000000000</td>
        </tr>
        <tr>
            <td>Google News</td>
            <td>0</td>
            <td>1000000000</td>
        </tr>
        <tr>
            <td>Google Photos</td>
            <td>0</td>
            <td>1000000000</td>
        </tr>
        <tr>
            <td>Google Play Books</td>
            <td>0</td>
            <td>1000000000</td>
        </tr>
        <tr>
            <td>Google Play Games</td>
            <td>0</td>
            <td>1000000000</td>
        </tr>
        <tr>
            <td>Google Play Movies &amp; TV</td>
            <td>0</td>
            <td>1000000000</td>
        </tr>
        <tr>
            <td>Google Street View</td>
            <td>0</td>
            <td>1000000000</td>
        </tr>
        <tr>
            <td>Google+</td>
            <td>0</td>
            <td>1000000000</td>
        </tr>
        <tr>
            <td>Hangouts</td>
            <td>0</td>
            <td>1000000000</td>
        </tr>
        <tr>
            <td>Instagram</td>
            <td>0</td>
            <td>1000000000</td>
        </tr>
        <tr>
            <td>Maps - Navigate &amp; Explore</td>
            <td>0</td>
            <td>1000000000</td>
        </tr>
        <tr>
            <td>Messenger – Text and Video Chat for Free</td>
            <td>0</td>
            <td>1000000000</td>
        </tr>
        <tr>
            <td>Skype - free IM &amp; video calls</td>
            <td>0</td>
            <td>1000000000</td>
        </tr>
        <tr>
            <td>Subway Surfers</td>
            <td>0</td>
            <td>1000000000</td>
        </tr>
        <tr>
            <td>WhatsApp Messenger</td>
            <td>0</td>
            <td>1000000000</td>
        </tr>
        <tr>
            <td>YouTube</td>
            <td>0</td>
            <td>1000000000</td>
        </tr>
    </tbody>
</table>



The dataset reveals 20 free apps have reached 1 billion downloads. Notably, among the top performers are Facebook, Gmail, YouTube, Google Chrome, and Instagra 

### What is the average price of paid apps by category?


```python
# Average price for paid application by category
%%sql 
SELECT category, ROUND(AVG(price),2) as average_price_category
FROM google_play_data
WHERE type = 1
GROUP BY category
ORDER BY average_price_category DESC
```

     * postgresql://postgres:***@localhost:5432/postgres
    28 rows affected.





<table>
    <thead>
        <tr>
            <th>category</th>
            <th>average_price_category</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>FINANCE</td>
            <td>187.69</td>
        </tr>
        <tr>
            <td>LIFESTYLE</td>
            <td>108.89</td>
        </tr>
        <tr>
            <td>FAMILY</td>
            <td>14.66</td>
        </tr>
        <tr>
            <td>MEDICAL</td>
            <td>9.87</td>
        </tr>
        <tr>
            <td>BUSINESS</td>
            <td>7.11</td>
        </tr>
        <tr>
            <td>DATING</td>
            <td>6.33</td>
        </tr>
        <tr>
            <td>MAPS_AND_NAVIGATION</td>
            <td>5.40</td>
        </tr>
        <tr>
            <td>PARENTING</td>
            <td>5.00</td>
        </tr>
        <tr>
            <td>PHOTOGRAPHY</td>
            <td>4.73</td>
        </tr>
        <tr>
            <td>TRAVEL_AND_LOCAL</td>
            <td>4.63</td>
        </tr>
        <tr>
            <td>EDUCATION</td>
            <td>4.50</td>
        </tr>
        <tr>
            <td>SPORTS</td>
            <td>4.18</td>
        </tr>
        <tr>
            <td>WEATHER</td>
            <td>4.14</td>
        </tr>
        <tr>
            <td>ENTERTAINMENT</td>
            <td>4.00</td>
        </tr>
        <tr>
            <td>FOOD_AND_DRINK</td>
            <td>4.00</td>
        </tr>
        <tr>
            <td>PRODUCTIVITY</td>
            <td>3.83</td>
        </tr>
        <tr>
            <td>HEALTH_AND_FITNESS</td>
            <td>3.82</td>
        </tr>
        <tr>
            <td>GAME</td>
            <td>3.63</td>
        </tr>
        <tr>
            <td>TOOLS</td>
            <td>3.25</td>
        </tr>
        <tr>
            <td>BOOKS_AND_REFERENCE</td>
            <td>3.00</td>
        </tr>
        <tr>
            <td>VIDEO_PLAYERS</td>
            <td>2.50</td>
        </tr>
        <tr>
            <td>SHOPPING</td>
            <td>2.50</td>
        </tr>
        <tr>
            <td>COMMUNICATION</td>
            <td>2.45</td>
        </tr>
        <tr>
            <td>NEWS_AND_MAGAZINES</td>
            <td>2.00</td>
        </tr>
        <tr>
            <td>AUTO_AND_VEHICLES</td>
            <td>2.00</td>
        </tr>
        <tr>
            <td>ART_AND_DESIGN</td>
            <td>2.00</td>
        </tr>
        <tr>
            <td>PERSONALIZATION</td>
            <td>1.80</td>
        </tr>
        <tr>
            <td>SOCIAL</td>
            <td>1.00</td>
        </tr>
    </tbody>
</table>



This table display the average price of paid apps in each category on the Google Play Store dataset. The category Finance has the highest average with 187.69 dollars. While the average price of apps in the Social category is just 1 dollar. This table can help to make informed decisions and strategies comparing pricing across categories. 

It's important to remember to take in consideration the outliers, the apps I'm Rich", when interpreting the data. 

### Which app genres are most commonly associated with high-rated apps, and which genres are most commonly associated with low-rated apps?

In this case, we have set a minimum standard number to identify the genres that are most commonly associated with high ratings or low ratings. 


```python
# Calculate the total number of high-rated applications by genre 
%%sql 
SELECT CASE WHEN rating >= 4.0 THEN 'high-rated app' ELSE 'low-rated app' END AS rating_app, 
genres, COUNT(app) AS number_of_apps 
FROM google_play_data 
GROUP BY rating, genres 
HAVING rating >= 4.0 AND COUNT(app) >= 250
ORDER BY rating_app, number_of_apps DESC;
```

     * postgresql://postgres:***@localhost:5432/postgres
    4 rows affected.





<table>
    <thead>
        <tr>
            <th>rating_app</th>
            <th>genres</th>
            <th>number_of_apps</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>high-rated app</td>
            <td>Tools</td>
            <td>503</td>
        </tr>
        <tr>
            <td>high-rated app</td>
            <td>Entertainment</td>
            <td>356</td>
        </tr>
        <tr>
            <td>high-rated app</td>
            <td>Education</td>
            <td>298</td>
        </tr>
        <tr>
            <td>high-rated app</td>
            <td>Action</td>
            <td>259</td>
        </tr>
    </tbody>
</table>



According to the dataset, **the genres that have more than 250 applications with high ratings are Tools, Entertainment, Education, and Action.** Specifically, these applications have a rating of more than 4.0 out of 5.0 points. 


```python
# Calculate the total number of low-rated applications by genre 
%%sql 
SELECT CASE WHEN rating >= 4.0 THEN 'high-rated app' ELSE 'low-rated app' END AS rating_app, 
genres, COUNT(app) AS number_of_apps 
FROM google_play_data 
GROUP BY rating, genres 
HAVING rating <= 3.9 AND COUNT(app) >= 20
ORDER BY rating_app, number_of_apps DESC;
```

     * postgresql://postgres:***@localhost:5432/postgres
    11 rows affected.





<table>
    <thead>
        <tr>
            <th>rating_app</th>
            <th>genres</th>
            <th>number_of_apps</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>low-rated app</td>
            <td>Tools</td>
            <td>79</td>
        </tr>
        <tr>
            <td>low-rated app</td>
            <td>Entertainment</td>
            <td>46</td>
        </tr>
        <tr>
            <td>low-rated app</td>
            <td>Business</td>
            <td>34</td>
        </tr>
        <tr>
            <td>low-rated app</td>
            <td>Lifestyle</td>
            <td>33</td>
        </tr>
        <tr>
            <td>low-rated app</td>
            <td>Medical</td>
            <td>23</td>
        </tr>
        <tr>
            <td>low-rated app</td>
            <td>Photography</td>
            <td>22</td>
        </tr>
        <tr>
            <td>low-rated app</td>
            <td>Finance</td>
            <td>21</td>
        </tr>
        <tr>
            <td>low-rated app</td>
            <td>Tools</td>
            <td>21</td>
        </tr>
        <tr>
            <td>low-rated app</td>
            <td>Education</td>
            <td>20</td>
        </tr>
        <tr>
            <td>low-rated app</td>
            <td>Travel &amp; Local</td>
            <td>20</td>
        </tr>
        <tr>
            <td>low-rated app</td>
            <td>Productivity</td>
            <td>20</td>
        </tr>
    </tbody>
</table>



Meanwhile, **the genres of tools, entertainment, business, and lifestyle also contain a significant number of poorly rated applications within their repositories.**

### How many apps in the database have a rating above 4.5, and what is the distribution of these apps across different categories?


```python
# Number of apps by each category rated above 4.5 
%%sql 
SELECT category, COUNT(app) AS total_apps
FROM google_play_data
WHERE rating >4.5 
GROUP BY category
ORDER BY total_apps DESC;
```

     * postgresql://postgres:***@localhost:5432/postgres
    33 rows affected.





<table>
    <thead>
        <tr>
            <th>category</th>
            <th>total_apps</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>FAMILY</td>
            <td>342</td>
        </tr>
        <tr>
            <td>GAME</td>
            <td>159</td>
        </tr>
        <tr>
            <td>TOOLS</td>
            <td>111</td>
        </tr>
        <tr>
            <td>HEALTH_AND_FITNESS</td>
            <td>89</td>
        </tr>
        <tr>
            <td>MEDICAL</td>
            <td>81</td>
        </tr>
        <tr>
            <td>LIFESTYLE</td>
            <td>81</td>
        </tr>
        <tr>
            <td>PERSONALIZATION</td>
            <td>78</td>
        </tr>
        <tr>
            <td>FINANCE</td>
            <td>70</td>
        </tr>
        <tr>
            <td>BOOKS_AND_REFERENCE</td>
            <td>64</td>
        </tr>
        <tr>
            <td>PRODUCTIVITY</td>
            <td>63</td>
        </tr>
        <tr>
            <td>BUSINESS</td>
            <td>61</td>
        </tr>
        <tr>
            <td>SPORTS</td>
            <td>55</td>
        </tr>
        <tr>
            <td>SOCIAL</td>
            <td>47</td>
        </tr>
        <tr>
            <td>NEWS_AND_MAGAZINES</td>
            <td>38</td>
        </tr>
        <tr>
            <td>PHOTOGRAPHY</td>
            <td>37</td>
        </tr>
        <tr>
            <td>EDUCATION</td>
            <td>33</td>
        </tr>
        <tr>
            <td>SHOPPING</td>
            <td>32</td>
        </tr>
        <tr>
            <td>COMMUNICATION</td>
            <td>24</td>
        </tr>
        <tr>
            <td>FOOD_AND_DRINK</td>
            <td>23</td>
        </tr>
        <tr>
            <td>TRAVEL_AND_LOCAL</td>
            <td>22</td>
        </tr>
        <tr>
            <td>ART_AND_DESIGN</td>
            <td>22</td>
        </tr>
        <tr>
            <td>AUTO_AND_VEHICLES</td>
            <td>21</td>
        </tr>
        <tr>
            <td>VIDEO_PLAYERS</td>
            <td>21</td>
        </tr>
        <tr>
            <td>DATING</td>
            <td>20</td>
        </tr>
        <tr>
            <td>PARENTING</td>
            <td>19</td>
        </tr>
        <tr>
            <td>EVENTS</td>
            <td>19</td>
        </tr>
        <tr>
            <td>COMICS</td>
            <td>13</td>
        </tr>
        <tr>
            <td>MAPS_AND_NAVIGATION</td>
            <td>12</td>
        </tr>
        <tr>
            <td>BEAUTY</td>
            <td>11</td>
        </tr>
        <tr>
            <td>LIBRARIES_AND_DEMO</td>
            <td>10</td>
        </tr>
        <tr>
            <td>WEATHER</td>
            <td>9</td>
        </tr>
        <tr>
            <td>ENTERTAINMENT</td>
            <td>8</td>
        </tr>
        <tr>
            <td>HOUSE_AND_HOME</td>
            <td>7</td>
        </tr>
    </tbody>
</table>



Lastly, in terms of the number of applications rated above 4.5, **the Family category stands out with the highest number of such apps.** Following closely are the Game and Tools categories with 159 and 111 highly-rated apps respectively.

In contrast, the categories weather, entertainment and house & home seem to have the lowest number of applications with an rating above 4.5 points out of 5. 

## Conclusions

Based on the analysis of the Google Play Store dataset, we noticed that the most of the applications availabe on the dataset are free. Moreover, we found that ther no relation between the number of reviews and rating, indicating that not neccesarily reflect the quality of the application. In addition, we could see that the most of the applications have a content rating of Everyone while only a small number of applications are rated as Mature+17 or Adults only. 

Analyzng this dataset, we could be able to provide insights for app developers, marketers ans even users. Understanding the distribution of the app categories, price range and ratings can provide a wider context in order to identify which category to target, current trends and opportunities in the app market. 

Note: This anaysis didn't take the columns update_month and update_year into consideration. However, these columns could provide useful insights into trends of app updates over time.

## Next Steps

Based on the analysis, here are some of the possible next steps to follow:
* It may be useful to identify and investigate these outliers (I'm Rich) further to determine if they are valid data points or if they should be removed from the dataset. 
* To perform more in-depth statistical analysis to gain a better understanding of the relationships between different variables in the dataset.
* Conduct more research on user preferences and interests within specific categories to develop apps that better meet their needs.
* Explore ways to improve ratings for apps in categories with low average ratings, such as weather and house & home.
* Consider the impact of content ratings on app popularity and explore ways to optimize content ratings to reach a wider audience.
