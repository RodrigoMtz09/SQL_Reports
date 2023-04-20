# Bikes_Sales_Analysis (SQL)
##### Author: Rodrigo Martinez Mina

## Introduction

As in any company, financial analysis helps internal stakeholders to undesrtand their situation as well as gives them the metrics and insights they need to make proper actions on time. 

In this project, we're going to work with data from a Bike's Store called "Ride my Bike". This database contain information about every transaction between 2015 and 2016. And other details as the customer's age, gender, location, and the products sold. 
Using SQL queries in Jupyter Notebook, we'll explore the data and uncover insights so, they can take better decesions and improve its operations. 


```python
# Regenate magic sql command. 
%reload_ext sql
```


```python
# To Jupyter notebook with database personal administrator 
%sql postgresql://postgres:1@localhost:5432/postgres
```

## Problem

According to the data provided, we're going to be able to answer questions related to profit and profit margin, sales trends and purchasing behavior across different demographic groups. 

For this project, we'll asnwer the following questions:
- What is the Ride my Bike's profit in 2015 and 2016?
- What is the total revenue of the store in each countries per year? Are there any significant differences in revenue between the countries?

- What is the total cost of the store in each country? Are there any significant differences in costs between the countries?

- What is the sales volume for each category ? Is there a significant difference in sales volume between the countries? 

- Which three states in the United States have the highest sales volume in "Ride my Bike"?

- Which gender has the highest sales volume for the products in "Ride my Bike"?

- What are the top 10 ages in terms of sales volume?
- Which 5 ages have the lowest sales volume?
- Is there a significant difference in sales volume between different age groups?

- Are there any cost-saving measures that the store could implement to     improve profitability?


## Analyzing the Data

In order to execute SQL commands we are gonna need to import 'sqlalchemy' library which provides a interface interact with SQL databases. While pandas offers integration with SQL databases using 'read_sql' function. 


```python
# Import the packages and libraries required
from sqlalchemy import create_engine
import pandas as pd
```


```python
# Import csv file into a pandas dataframe
df = pd.read_csv('Desktop/Data/bike_sales.csv')
```


```python
# Connect our PostgreSQL database by running a string command in Jupyter notebook
%sql postgresql://postgres:1@localhost:5432/postgres
```


```python
engine = create_engine("postgresql://postgres:1@localhost:5432/postgres")
df.to_sql('bike_sales', con=engine, if_exists='replace', index=False)
```




    866




```python
# Let's execute a basic SQL command to verify the connectivity of our database
%sql SELECT * 
FROM bike_sales 
LIMIT 5;
```

     * postgresql://postgres:***@localhost:5432/postgres
    5 rows affected.





<table>
    <thead>
        <tr>
            <th>index</th>
            <th>date</th>
            <th>year</th>
            <th>month</th>
            <th>customer_age</th>
            <th>customer_gender</th>
            <th>country</th>
            <th>state</th>
            <th>product_category</th>
            <th>sub_category</th>
            <th>quantity</th>
            <th>unit_cost</th>
            <th>unit_price</th>
            <th>cost</th>
            <th>revenue</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0</td>
            <td>2/19/2016</td>
            <td>2016</td>
            <td>February</td>
            <td>29</td>
            <td>F</td>
            <td>United States</td>
            <td>Washington</td>
            <td>Accessories</td>
            <td>Tires and Tubes</td>
            <td>1</td>
            <td>80.0</td>
            <td>109.0</td>
            <td>80</td>
            <td>109</td>
        </tr>
        <tr>
            <td>1</td>
            <td>2/20/2016</td>
            <td>2016</td>
            <td>February</td>
            <td>29</td>
            <td>F</td>
            <td>United States</td>
            <td>Washington</td>
            <td>Clothing</td>
            <td>Gloves</td>
            <td>2</td>
            <td>24.5</td>
            <td>28.5</td>
            <td>49</td>
            <td>57</td>
        </tr>
        <tr>
            <td>2</td>
            <td>2/27/2016</td>
            <td>2016</td>
            <td>February</td>
            <td>29</td>
            <td>F</td>
            <td>United States</td>
            <td>Washington</td>
            <td>Accessories</td>
            <td>Tires and Tubes</td>
            <td>3</td>
            <td>3.67</td>
            <td>5.0</td>
            <td>11</td>
            <td>15</td>
        </tr>
        <tr>
            <td>3</td>
            <td>3/12/2016</td>
            <td>2016</td>
            <td>March</td>
            <td>29</td>
            <td>F</td>
            <td>United States</td>
            <td>Washington</td>
            <td>Accessories</td>
            <td>Tires and Tubes</td>
            <td>2</td>
            <td>87.5</td>
            <td>116.5</td>
            <td>175</td>
            <td>233</td>
        </tr>
        <tr>
            <td>4</td>
            <td>3/12/2016</td>
            <td>2016</td>
            <td>March</td>
            <td>29</td>
            <td>F</td>
            <td>United States</td>
            <td>Washington</td>
            <td>Accessories</td>
            <td>Tires and Tubes</td>
            <td>3</td>
            <td>35.0</td>
            <td>41.666667</td>
            <td>105</td>
            <td>125</td>
        </tr>
    </tbody>
</table>



Having established a connection with the data source, we may proceed to examine and analyze our data


```python
# This command counts the number of rows in our dataset
%sql SELECT COUNT(*) 
FROM bike_sales
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
            <td>34866</td>
        </tr>
    </tbody>
</table>




```python
# This command retrieves the columns name of our dataset and its datatype
%sql SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'bike_sales';
```

     * postgresql://postgres:***@localhost:5432/postgres
    15 rows affected.





<table>
    <thead>
        <tr>
            <th>column_name</th>
            <th>data_type</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>index</td>
            <td>bigint</td>
        </tr>
        <tr>
            <td>year</td>
            <td>bigint</td>
        </tr>
        <tr>
            <td>customer_age</td>
            <td>bigint</td>
        </tr>
        <tr>
            <td>quantity</td>
            <td>bigint</td>
        </tr>
        <tr>
            <td>unit_cost</td>
            <td>double precision</td>
        </tr>
        <tr>
            <td>unit_price</td>
            <td>double precision</td>
        </tr>
        <tr>
            <td>cost</td>
            <td>bigint</td>
        </tr>
        <tr>
            <td>revenue</td>
            <td>bigint</td>
        </tr>
        <tr>
            <td>date</td>
            <td>text</td>
        </tr>
        <tr>
            <td>product_category</td>
            <td>text</td>
        </tr>
        <tr>
            <td>month</td>
            <td>text</td>
        </tr>
        <tr>
            <td>sub_category</td>
            <td>text</td>
        </tr>
        <tr>
            <td>customer_gender</td>
            <td>text</td>
        </tr>
        <tr>
            <td>country</td>
            <td>text</td>
        </tr>
        <tr>
            <td>state</td>
            <td>text</td>
        </tr>
    </tbody>
</table>



This dataset is composed by 15 columns

A brief explanation of each column:

- Year: year in which the transaction occurred. 
- Month: month in which the transaction occurred. 
- Customer Age: age of the customer. 
- Customer Gender: This column represents the gender of the customer. 
- Country: where the transaction occurred. 
- State: state where the transaction occurred. 
- Product Category: broad category of the product sold. 
- Sub Category: This column represents the specific subcategory of the product sold. 
- Quantity: quantity of the product sold. 
- Unit Cost: cost of producing or acquiring one unit of the product. 
- Unit Price: the price at which one unit of the product was sold. 
- Cost: This column represents the total cost of the products sold, which is calculated as the product of the quantity and the unit cost.
- Revenue: This column represents the total revenue generated by the sales, which is calculated as the product of the quantity and the unit price. 


```python
# To change the data type of some columns to integer
%sql ALTER TABLE bikes_sales 
ALTER COLUMN revenue TYPE INTEGER,
ALTER COLUMN year TYPE INTEGER,
ALTER COLUMN customer_age TYPE INTEGER, 
ALTER COLUMN quantity TYPE INTEGER, 
ALTER COLUMN cost TYPE INTEGER,
ALTER COLUMN unit_price TYPE INTEGER,
ALTER COLUMN unit_cost TYPE INTEGER;
```

     * postgresql://postgres:***@localhost:5432/postgres
    Done.





    []



We change the data type of some columns in order to perform calculations easier. 


```python
# IS NULL with Count function, we're counting the total number of rows where there's a missing value.
%sql SELECT COUNT(*) 
FROM bike_sales 
WHERE revenue IS NULL OR date IS NULL
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



Fortunately, there are no missing values in our dataset, so cleaning or dropping data won't be necessary. 

## Analysis the Data

Now that we have verified the available information and its composition in our dataset, our next step is to analyze the data and to try to answer the questions previoulsly planted. 
By applying the correct SQL commands thourgh different functions and clauses we hope to extract meaningful information and draw valuable conclusions from the dataset. 

### What is the Ride my Bike's profit in 2015 and 2016?


```python
# In order to get the profit, we need first to get the revenue and cost of each year. 
%sql SELECT year, 
SUM(unit_price*quantity) AS total_revenue, 
SUM(unit_cost*quantity) AS total_cost, 
SUM(unit_price*quantity)- SUM(unit_cost*quantity)AS profit 
FROM bikes_sales 
WHERE year IS NOT NULL 
GROUP BY year; 
```

     * postgresql://postgres:***@localhost:5432/postgres
    2 rows affected.





<table>
    <thead>
        <tr>
            <th>year</th>
            <th>total_revenue</th>
            <th>total_cost</th>
            <th>profit</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2016</td>
            <td>12396787</td>
            <td>10423414</td>
            <td>1973373</td>
        </tr>
        <tr>
            <td>2015</td>
            <td>9947702</td>
            <td>9658933</td>
            <td>288769</td>
        </tr>
    </tbody>
</table>



This first command calculates the total revenue, total cost and the profit for each year in the dataset (2015 & 2016)

Just to remember:
- Revenue = (unit_price * quantity)
- Cost = (unit_cost * quantity)
- Profit = revenue - cost

As we can see, the year resulted in a profit of 288,624 dollars. 
While in 2016, the profit was 1,972986 dollars. This represents an increase of approximately 6.8 times over the previous year.

### What is the total revenue of the store in each countries per year?      
### Are there any significant differences in revenue between the countries?


```python
# To Calculate total revenue per country each year
%sql SELECT country, year, 
SUM(revenue)AS total_revenue 
FROM bikes_sales 
WHERE year IS NOT NULL 
GROUP BY country, year 
ORDER BY year, total_revenue DESC;
```

     * postgresql://postgres:***@localhost:5432/postgres
    8 rows affected.





<table>
    <thead>
        <tr>
            <th>country</th>
            <th>year</th>
            <th>total_revenue</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>United States</td>
            <td>2015</td>
            <td>4735408</td>
        </tr>
        <tr>
            <td>United Kingdom</td>
            <td>2015</td>
            <td>1894467</td>
        </tr>
        <tr>
            <td>Germany</td>
            <td>2015</td>
            <td>1773323</td>
        </tr>
        <tr>
            <td>France</td>
            <td>2015</td>
            <td>1544573</td>
        </tr>
        <tr>
            <td>United States</td>
            <td>2016</td>
            <td>5642334</td>
        </tr>
        <tr>
            <td>Germany</td>
            <td>2016</td>
            <td>2471187</td>
        </tr>
        <tr>
            <td>United Kingdom</td>
            <td>2016</td>
            <td>2381753</td>
        </tr>
        <tr>
            <td>France</td>
            <td>2016</td>
            <td>1901531</td>
        </tr>
    </tbody>
</table>



This table contains financial data on the total revenue generated by "Ride my Bike" in each country (United States, Kingdom, Germany and France) in 2015 and 2016.

In both years, the United States generated the highest income with 4,735,408 and 5,642,334 dollars respectively. The company generated 2,471,187 dollars in 2016. This is significant increase compared to the previuos year (2015) where the store generated a total revenue of 1,773,323 dollars. 

Finally, France is the country with the lowest total revenue generated in both years. It's important to develop strategies to address this issue. 

### What is the total cost of the store in each country? 
### Are there any significant differences in costs between the countries?


```python
# To Calculate the total cost of the company per country, each year
%sql SELECT country, year, 
SUM(cost) AS total_cost 
FROM bikes_sales 
WHERE year IS NOT NULL 
GROUP BY country,year 
ORDER BY year, total_cost DESC;
```

     * postgresql://postgres:***@localhost:5432/postgres
    8 rows affected.





<table>
    <thead>
        <tr>
            <th>country</th>
            <th>year</th>
            <th>total_cost</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>United States</td>
            <td>2015</td>
            <td>4757956</td>
        </tr>
        <tr>
            <td>United Kingdom</td>
            <td>2015</td>
            <td>1886032</td>
        </tr>
        <tr>
            <td>France</td>
            <td>2015</td>
            <td>1526868</td>
        </tr>
        <tr>
            <td>Germany</td>
            <td>2015</td>
            <td>1488295</td>
        </tr>
        <tr>
            <td>United States</td>
            <td>2016</td>
            <td>4918621</td>
        </tr>
        <tr>
            <td>United Kingdom</td>
            <td>2016</td>
            <td>2061233</td>
        </tr>
        <tr>
            <td>Germany</td>
            <td>2016</td>
            <td>1797390</td>
        </tr>
        <tr>
            <td>France</td>
            <td>2016</td>
            <td>1646579</td>
        </tr>
    </tbody>
</table>



Now, this table shows the total cost for each country in the years 2015 and 2016. In 2015 as in 2016, the United States generated the highest cost of sales. Meanwhile, Germany and France were the countries that generated the lowest cost. 

### What is the sales volume for each category ? 
### Is there a significant difference in sales volume between the countries?


```python
# Calculating the sales volume for each category
%sql SELECT product_category,
SUM(quantity)AS total_units_sold 
FROM bikes_sales 
WHERE year IS NOT NULL 
GROUP BY product_category 
ORDER BY total_units_sold DESC;
```

     * postgresql://postgres:***@localhost:5432/postgres
    3 rows affected.





<table>
    <thead>
        <tr>
            <th>product_category</th>
            <th>total_units_sold</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Accessories</td>
            <td>45048</td>
        </tr>
        <tr>
            <td>Bikes</td>
            <td>14291</td>
        </tr>
        <tr>
            <td>Clothing</td>
            <td>10481</td>
        </tr>
    </tbody>
</table>



According to the data, the category "Accesories" was the most popular product with a total of 45,048 units sold. Meanwhile, "clothing" was the least popular product category, with only 10,048 units sold. It's important for the company to understand this part because it helps to determine future decisions in inventory and marketing. 


```python
# Calculating the volume of sales for each category between countries 
%sql SELECT country,
product_category,
SUM(quantity)AS total_units_sold 
FROM bikes_sales 
WHERE year IS NOT NULL 
GROUP BY country, product_category 
ORDER BY country, total_units_sold DESC;
```

     * postgresql://postgres:***@localhost:5432/postgres
    12 rows affected.





<table>
    <thead>
        <tr>
            <th>country</th>
            <th>product_category</th>
            <th>total_units_sold</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>France</td>
            <td>Accessories</td>
            <td>6626</td>
        </tr>
        <tr>
            <td>France</td>
            <td>Bikes</td>
            <td>2296</td>
        </tr>
        <tr>
            <td>France</td>
            <td>Clothing</td>
            <td>1451</td>
        </tr>
        <tr>
            <td>Germany</td>
            <td>Accessories</td>
            <td>6405</td>
        </tr>
        <tr>
            <td>Germany</td>
            <td>Bikes</td>
            <td>2588</td>
        </tr>
        <tr>
            <td>Germany</td>
            <td>Clothing</td>
            <td>1393</td>
        </tr>
        <tr>
            <td>United Kingdom</td>
            <td>Accessories</td>
            <td>7910</td>
        </tr>
        <tr>
            <td>United Kingdom</td>
            <td>Bikes</td>
            <td>3022</td>
        </tr>
        <tr>
            <td>United Kingdom</td>
            <td>Clothing</td>
            <td>1890</td>
        </tr>
        <tr>
            <td>United States</td>
            <td>Accessories</td>
            <td>24107</td>
        </tr>
        <tr>
            <td>United States</td>
            <td>Bikes</td>
            <td>6385</td>
        </tr>
        <tr>
            <td>United States</td>
            <td>Clothing</td>
            <td>5747</td>
        </tr>
    </tbody>
</table>



Related to the previous table, this updated table provides a more detailed analysis of sales performance, showing how each category is performing in each country. Accesories is the most popular category in all four countries. It's followed by Bikes in second place and Clothing in third place. As we can see, there's no significant difference in preference between countries. 

By examining the sales volume for each category and country, the company  can gain valuable insights into consumer preferences and adjust their strategies accordingly.

### Which three states in the United States have the highest sales volume in "Ride my Bike"?


```python
# Calculating the gross profit margin by country
%sql SELECT country, state, 
SUM(quantity) AS total_sales 
FROM bikes_sales 
WHERE year IS NOT NULL AND country='United States' 
GROUP BY country, state 
ORDER BY total_sales DESC 
LIMIT 3;
```

     * postgresql://postgres:***@localhost:5432/postgres
    3 rows affected.





<table>
    <thead>
        <tr>
            <th>country</th>
            <th>state</th>
            <th>total_sales</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>United States</td>
            <td>California</td>
            <td>20722</td>
        </tr>
        <tr>
            <td>United States</td>
            <td>Washington</td>
            <td>10431</td>
        </tr>
        <tr>
            <td>United States</td>
            <td>Oregon</td>
            <td>4908</td>
        </tr>
    </tbody>
</table>



The table displays the sales performance of the top three locations in the United States that sold the highest volume of "Ride my Bike." The data reveals that California had the highest sales figures, with a total of 20,722 units sold between 2015 and 2016. This suggests that California is a crucial market for "Ride my Bike". In other hand, Oregon still important, lagged behind with only 4,908 units sold, indicating a clear difference between the states. 

This can help the company to provide valuable insights in order to choose proper strategies to optimize sales in one of the most important target market. 

### Which gender has the highest sales volume for the products in "Ride my Bike"? 
### Is there any difference between countries?


```python
# To calculate total sales per gender
%sql SELECT customer_gender, 
SUM(quantity) AS total_sales 
FROM bikes_sales 
WHERE customer_gender IS NOT NULL 
GROUP BY customer_gender 
ORDER BY total_sales DESC;
```

     * postgresql://postgres:***@localhost:5432/postgres
    2 rows affected.





<table>
    <thead>
        <tr>
            <th>customer_gender</th>
            <th>total_sales</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>M</td>
            <td>35484</td>
        </tr>
        <tr>
            <td>F</td>
            <td>34336</td>
        </tr>
    </tbody>
</table>



The table above shows no great difference in total sales between genders. According to the data, men purchased 35,484 units between 2015 and 2016,  while women generated 34,336 units sold. 


```python
# Total sales per gender in the four countries  
%sql SELECT country, customer_gender, 
SUM(quantity) AS total_sales 
FROM bikes_sales 
WHERE customer_gender IS NOT NULL AND country IS NOT NULL 
GROUP BY country, customer_gender 
ORDER BY total_sales DESC, country;
```

     * postgresql://postgres:***@localhost:5432/postgres
    8 rows affected.





<table>
    <thead>
        <tr>
            <th>country</th>
            <th>customer_gender</th>
            <th>total_sales</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>United States</td>
            <td>M</td>
            <td>18762</td>
        </tr>
        <tr>
            <td>United States</td>
            <td>F</td>
            <td>17477</td>
        </tr>
        <tr>
            <td>United Kingdom</td>
            <td>F</td>
            <td>6452</td>
        </tr>
        <tr>
            <td>United Kingdom</td>
            <td>M</td>
            <td>6370</td>
        </tr>
        <tr>
            <td>Germany</td>
            <td>F</td>
            <td>5242</td>
        </tr>
        <tr>
            <td>France</td>
            <td>M</td>
            <td>5208</td>
        </tr>
        <tr>
            <td>France</td>
            <td>F</td>
            <td>5165</td>
        </tr>
        <tr>
            <td>Germany</td>
            <td>M</td>
            <td>5144</td>
        </tr>
    </tbody>
</table>



Although there is no significant difference in total sales between genders in each country, the data suggests that in Europe, women were responsible for generating more units sold than men. In contrast, in the United States, men purchased the highest number of products, with a total of 18,762 units sold. 

### What are the top 10 ages in terms of sales volume?
### Which 5 ages have the lowest sales volume?
### Is there a significant difference in sales volume between different age groups?


```python
# Calculate the TOP 10 volume sales based on age 
%sql SELECT customer_age, 
SUM(quantity) AS total_sales 
FROM bikes_sales 
WHERE customer_age IS NOT NULL 
GROUP BY customer_age 
ORDER BY total_sales DESC 
LIMIT 10;
```

     * postgresql://postgres:***@localhost:5432/postgres
    10 rows affected.





<table>
    <thead>
        <tr>
            <th>customer_age</th>
            <th>total_sales</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>31</td>
            <td>2630</td>
        </tr>
        <tr>
            <td>28</td>
            <td>2545</td>
        </tr>
        <tr>
            <td>34</td>
            <td>2539</td>
        </tr>
        <tr>
            <td>29</td>
            <td>2509</td>
        </tr>
        <tr>
            <td>30</td>
            <td>2396</td>
        </tr>
        <tr>
            <td>32</td>
            <td>2380</td>
        </tr>
        <tr>
            <td>33</td>
            <td>2271</td>
        </tr>
        <tr>
            <td>35</td>
            <td>2236</td>
        </tr>
        <tr>
            <td>40</td>
            <td>2189</td>
        </tr>
        <tr>
            <td>37</td>
            <td>2155</td>
        </tr>
    </tbody>
</table>



According to the table above, individuals aged between 28 and 40 years old have the highest sales volume. Among these age groups, customers who are 31 years old generated the highest sales with 2,630 units sold, while customers who are 37 years old complete the top 10 with 2,155 units sold. It is worth noting that the difference in sales volume between these age groups is relatively small. 

However, this valuable insight can still be utilized to inform future marketing decisions.


```python
# 5 lowest sales volume based on age 
%sql SELECT customer_age, 
SUM(quantity) AS total_sales 
FROM bikes_sales 
WHERE customer_age IS NOT NULL 
GROUP BY customer_age 
ORDER BY total_sales 
LIMIT 5;
```

     * postgresql://postgres:***@localhost:5432/postgres
    5 rows affected.





<table>
    <thead>
        <tr>
            <th>customer_age</th>
            <th>total_sales</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>80</td>
            <td>4</td>
        </tr>
        <tr>
            <td>76</td>
            <td>4</td>
        </tr>
        <tr>
            <td>74</td>
            <td>4</td>
        </tr>
        <tr>
            <td>82</td>
            <td>5</td>
        </tr>
        <tr>
            <td>81</td>
            <td>8</td>
        </tr>
    </tbody>
</table>



In constrast, people aged between 74 to 82 years old generated the lowest units sold, with all of them with generating just single-digit sales. 


```python
# Calculating sales volume based on age groups 
%sql SELECT CASE WHEN 
customer_age BETWEEN 12 AND 17 THEN '12-17' 
WHEN customer_age BETWEEN 18 AND 24 THEN '18-24' 
WHEN customer_age BETWEEN 25 AND 34 THEN '25-34' 
WHEN customer_age BETWEEN 35 AND 44 THEN '35-44' 
WHEN customer_age BETWEEN 45 AND 54 THEN '45-54' 
WHEN customer_age BETWEEN 55 AND 64 THEN '55-64' 
WHEN customer_age BETWEEN 65 AND 74 THEN '65-74' 
WHEN customer_age BETWEEN 75 AND 84 THEN '75-84' 
ELSE '85+' END AS age_group, 
SUM(quantity) AS total_sales 
FROM bikes_sales 
GROUP BY age_group 
ORDER BY age_group; 
```

     * postgresql://postgres:***@localhost:5432/postgres
    9 rows affected.





<table>
    <thead>
        <tr>
            <th>age_group</th>
            <th>total_sales</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12-17</td>
            <td>731</td>
        </tr>
        <tr>
            <td>18-24</td>
            <td>9524</td>
        </tr>
        <tr>
            <td>25-34</td>
            <td>23247</td>
        </tr>
        <tr>
            <td>35-44</td>
            <td>20180</td>
        </tr>
        <tr>
            <td>45-54</td>
            <td>11528</td>
        </tr>
        <tr>
            <td>55-64</td>
            <td>4084</td>
        </tr>
        <tr>
            <td>65-74</td>
            <td>394</td>
        </tr>
        <tr>
            <td>75-84</td>
            <td>105</td>
        </tr>
        <tr>
            <td>85+</td>
            <td>27</td>
        </tr>
    </tbody>
</table>



This table shows the total sales for different age groups. The data has been aggregated by grouping the sales data by age group. According at the information provided, we can see that the age agroup with the highest volume is the "25-34" age group with a total of 20,180 units sold. It's followed by the "35-44" age group with 20,180 and the "18-24" age group with 9,524 units sold. 

As mentioned previously, the age group with the lowest sales volmes is the "85+" age group which only generated 27 units sold. 

### Are there any cost-saving measures that the store could implement to improve profitability?


```python
# Calculate the profit of the company in each country (As support)
%sql SELECT country,year, 
SUM(revenue)-SUM(cost) AS profit 
FROM bikes_sales 
WHERE year IS NOT NULL 
GROUP BY country, year 
ORDER BY year, country;
```

     * postgresql://postgres:***@localhost:5432/postgres
    8 rows affected.





<table>
    <thead>
        <tr>
            <th>country</th>
            <th>year</th>
            <th>profit</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>France</td>
            <td>2015</td>
            <td>17705</td>
        </tr>
        <tr>
            <td>Germany</td>
            <td>2015</td>
            <td>285028</td>
        </tr>
        <tr>
            <td>United Kingdom</td>
            <td>2015</td>
            <td>8435</td>
        </tr>
        <tr>
            <td>United States</td>
            <td>2015</td>
            <td>-22548</td>
        </tr>
        <tr>
            <td>France</td>
            <td>2016</td>
            <td>254952</td>
        </tr>
        <tr>
            <td>Germany</td>
            <td>2016</td>
            <td>673797</td>
        </tr>
        <tr>
            <td>United Kingdom</td>
            <td>2016</td>
            <td>320520</td>
        </tr>
        <tr>
            <td>United States</td>
            <td>2016</td>
            <td>723713</td>
        </tr>
    </tbody>
</table>




```python
# Number of products sold where their cost is higher than revenue
%sql SELECT product_category, 
COUNT(*) AS unprofitable_products_sold 
FROM bikes_sales 
WHERE cost > revenue 
GROUP BY product_category 
ORDER BY unprofitable_products_sold; 
```

     * postgresql://postgres:***@localhost:5432/postgres
    3 rows affected.





<table>
    <thead>
        <tr>
            <th>product_category</th>
            <th>unprofitable_products_sold</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Clothing</td>
            <td>530</td>
        </tr>
        <tr>
            <td>Accessories</td>
            <td>1038</td>
        </tr>
        <tr>
            <td>Bikes</td>
            <td>3286</td>
        </tr>
    </tbody>
</table>



The table contains the the total number od unprofitable products sold for each product category. An unprofitable product is a prduct that has a cost higher than its revenue, which means is selling producs at a loss. 

The product category "Bikes" has the highest number of times than an unprofitable product was sold with 3,286. This is followed by "Accesories and "Clothing" with 1,038 and 530 units respectively. 

This is related with table aboove that shows the profit by country each year where we can see that in 2015, the United States incurred a loss rather than generating a profit.

# Conclusions

To conclude, "Ride my Bike" has made significant progress in improving its sales and profits across all four countries from 2015 to 2016. 

Despite facing some challenges, such as unprofitable products "Ride my Bike" has been able to over come these obstacles and achieve impressive results. However, there may be further opportunities for the company to continue expanding its business and increasing its market share in the future. 

# Next Steps

Based on the analysis provided, here are some potential next steps for "Ride my Bike"

- Identify and optimize product prices: In other words, the company has to manage its costs and pricing strategies. The fact that there're unprofitabe products being sold indicates there's no profit at all and it may even be losing money. 

- Expand new markets: "Ride my Bike" has already succeded in four countries, there might be opportunities to expand into other markets. 

- Invest in marketing: This analysis also provided valuable insights about its market based on age groups and category products which could be used as guidelines. 

- Product innovation: In order to keep competitive, "Ride my Bike" shoud be involved explorin opportinities in product innovation and developing new features. 


```python

```
