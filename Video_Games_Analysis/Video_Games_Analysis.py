#!/usr/bin/env python
# coding: utf-8

# # Case Study: Video_Games_Analysis 
# Author: Rodrigo Martinez Mina

# ![videogame.jpeg](attachment:videogame.jpeg)

# ## Introduction

# Hi everyone! 
# 
# In this SQL analysis project, we're gonna explore into the dynamic world of gaming, where imagination meets technology. With the power of Structured Query Language (SQL), we embark on a quest to unlock insights, patterns, and trends that shape the gaming landscape.
# 
# Since the creation of the first video game, "Tennis for Two," in 1958, the video game industry has experienced remarkable growth and has become a significant economic force. With a global market worth billions of dollars, video games have evolved beyond traditional arcade styles, offering a vast variety of genres and experiences.
# 
# The purpose of this project is to navigate through interconnected tables, uncovering the secrets of success and discovering the hidden treasures within the gaming industry.
# 
# The data was collected from: https://www.databasestar.com/sample-database-video-games/
# 
# If you have any questions or need further assistance, feel free to ask!
# 
# Get Ready, go! 

# ## Importing Data

# To begin, we start by importing the necessary libraries, including the SQLAlchemy library for interacting with SQL databases and the pandas package for data manipulation and analysis. 
# 
# Once the libraries are imported, the next step is to import each table from the database into Jupyter notebook using pandas and the appropriate database engine. This allows you to load the tables as pandas DataFrames, which provide a tabular structure for easy data manipulation and analysis.

# In[113]:


from sqlalchemy import create_engine
import pandas as pd


# In[114]:


get_ipython().run_line_magic('reload_ext', 'sql')


# In[115]:


get_ipython().run_line_magic('sql', 'postgresql://postgres:1@localhost:5432/postgres')


# Importing and connecting the corresponding tables to our Jupyter Notebook.

# In[116]:


df = pd.read_csv('Desktop/videogames/game.csv')


# In[117]:


engine = create_engine("postgresql://postgres:1@localhost:5432/postgres")
df.to_sql('game', con=engine, if_exists='replace', index=False)


# In[118]:


df = pd.read_csv('Desktop/videogames/game_platform.csv')


# In[119]:


engine = create_engine("postgresql://postgres:1@localhost:5432/postgres")
df.to_sql('game_platform', con=engine, if_exists='replace', index=False)


# In[120]:


df = pd.read_csv('Desktop/videogames/game_publisher.csv')


# In[121]:


engine = create_engine("postgresql://postgres:1@localhost:5432/postgres")
df.to_sql('game_publisher', con=engine, if_exists='replace', index=False)


# In[122]:


df = pd.read_csv('Desktop/videogames/genre.csv')


# In[123]:


engine = create_engine("postgresql://postgres:1@localhost:5432/postgres")
df.to_sql('genre', con=engine, if_exists='replace', index=False)


# In[124]:


df = pd.read_csv('Desktop/videogames/platform.csv')


# In[125]:


engine = create_engine("postgresql://postgres:1@localhost:5432/postgres")
df.to_sql('platform', con=engine, if_exists='replace', index=False)


# In[126]:


df = pd.read_csv('Desktop/videogames/publisher.csv')


# In[127]:


engine = create_engine("postgresql://postgres:1@localhost:5432/postgres")
df.to_sql('publisher', con=engine, if_exists='replace', index=False)


# In[128]:


df = pd.read_csv('Desktop/videogames/region.csv')


# In[129]:


engine = create_engine("postgresql://postgres:1@localhost:5432/postgres")
df.to_sql('region', con=engine, if_exists='replace', index=False)


# In[130]:


df = pd.read_csv('Desktop/videogames/region_sales.csv')


# In[131]:


engine = create_engine("postgresql://postgres:1@localhost:5432/postgres")
df.to_sql('region_sales', con=engine, if_exists='replace', index=False)


# Once imported all our tables, let's just see with a simple query if we are able to see the information.

# In[132]:


# Extracting the first 10 rows of genre table
get_ipython().run_line_magic('sql', 'SELECT * FROM game LIMIT 10;')


# ## Data Exploration

# In our dataset, we have multiple tables that contain valuable information. We will explore each table individually and provide a brief explanation of their contents.

# In[133]:


# Counting the number of rows in our dataset
get_ipython().run_line_magic('sql', 'SELECT COUNT(*) FROM game')


# In[134]:


# This command retrieves the columns name of our dataset and its datatype
get_ipython().run_line_magic('sql', "SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'game' ORDER BY column_name;")


# In[135]:


# Extracting the first 10 rows of game table
get_ipython().run_line_magic('sql', 'SELECT * FROM game LIMIT 5;')


# #### Game Table
# * id: Unique identifier for each videogame
# * genre_id: The genre of each videogame, referring to a genre table
# * game_name: The name of the videogame
# 
# Our dataset comprises information on a substantial number of video games, specifically over 11,000 different titles. 

# In[136]:


# Counting the number of rows in our dataset
get_ipython().run_line_magic('sql', 'SELECT COUNT(*) FROM genre')


# In[137]:


# This command retrieves the columns name of our dataset and its datatype
get_ipython().run_line_magic('sql', "SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'genre' ORDER BY column_name;")


# #### Genre Table 
# * genre_id: Unique identifier for each genre
# * genre_name: Name of the genres
# 
# The genre table contains 12 rows, representing different genres in the context of videogames. And it provides a reference for understanding the genre classification used in the game table.

# In[138]:


# Counting the number of rows in our dataset
get_ipython().run_line_magic('sql', 'SELECT COUNT(*) FROM game_publisher')


# In[139]:


# This command retrieves the columns name of our dataset and its datatype
get_ipython().run_line_magic('sql', "SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'game_publisher' ORDER BY column_name;")


# #### Game Publisher Table 
# * game_id: Unique identifier for each game.
# * id: Another unique identifier.
# * publisher_id: The identifier of the publisher associated with each game
# 
# The publisher_id column is used to establish a relationship between the games and their respective publishers, which are in a separate table containing publisher information.

# In[140]:


# Counting the number of rows in our dataset
get_ipython().run_line_magic('sql', 'SELECT COUNT(*) FROM game_platform')


# In[141]:


# This command retrieves the columns name of our dataset and its datatype
get_ipython().run_line_magic('sql', "SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'game_platform' ORDER BY column_name;")


# #### Game Platform Table 
# 
# * game_publisher: Unique identifier for a game-publisher relationship
# * id: It Represents row unique identifier
# * platform_id: It provides an identifier of a specific gaming platform
# * release_year: The year in which a game was released
# 
# In general, this table, can be used to establish a relationship between a game and its corresponding publisher and between a game and the platform on which it is available, linking to a separate tables. 

# In[142]:


# Counting the number of rows in our dataset
get_ipython().run_line_magic('sql', 'SELECT COUNT(*) FROM publisher')


# In[143]:


# This command retrieves the columns name of our dataset and its datatype
get_ipython().run_line_magic('sql', "SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'publisher' ORDER BY column_name;")


# #### Publisher Table 
# * id: Unique identifier for each entry in the table
# * publisher_name: Name of publishers
# 
# According to the table, there're 577 different publishers in this dataset. 

# In[144]:


# Counting the number of rows of platform table 
get_ipython().run_line_magic('sql', 'SELECT COUNT(*) FROM platform')


# In[145]:


# This command retrieves the columns name of our dataset and its datatype
get_ipython().run_line_magic('sql', "SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'platform' ORDER BY column_name;")


# #### Platform Table 
# * id: Unique Identifier for each entry in this table
# * platform_name: Name of the platform

# In[146]:


# Counting the number of region sales table 
get_ipython().run_line_magic('sql', 'SELECT COUNT(*) FROM region_sales')


# In[147]:


# This command retrieves the columns name of our dataset and its datatype
get_ipython().run_line_magic('sql', "SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'region_sales' ORDER BY column_name;")


# In[148]:


# Change the num_sales columnn to only 2 decimal 
get_ipython().run_line_magic('sql', 'ALTER TABLE region_sales ALTER COLUMN num_sales TYPE DECIMAL(5,2);')


# To simplify the results, we just updated the "num_sales" column from a double_precision data type to DECIMAL. This change ensures that the sales figures are presented in a more straightforward manner, making it easier to work with and interpret the results.

# #### Region Sales Table
# * game_platform_id: it storages an unique identifier for the game-platform relationship
# * num_sales: Number of sales or units sold for a particular game-platform combination
# * region_id: The identifier for a specific region or geographic area
# 
# To avoid any ambiguity, it is crucial to clarify that the values in the "num_sales" column are expressed in millions. 

# In[149]:


# Counting the number of rows of region table 
get_ipython().run_line_magic('sql', 'SELECT COUNT(*) FROM region')


# In[150]:


# This command retrieves the columns name of our dataset and its datatype
get_ipython().run_line_magic('sql', "SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'region' ORDER BY column_name;")


# In[151]:


# First rows of region table
get_ipython().run_line_magic('sql', 'SELECT * FROM region')


# #### Region Table 
# * id: Unique identifier for each region
# * region_name: Name of the region
# 
# The four regions of this dataset are NorthAmerica, Europe, Japan and Other. 
# Japan is cosidered as a region by itself because this country has a rich history and a significant impact on the global gaming market. Besides, it's home to renowned video game companies like Nintendo, Sony, and Capcom.  

# ## Data Modeling

# #### Entity Relationship Diagram 
# Once the tables are imported into your Jupyter notebook, it's indeed a good idea to develop an Entity Relationship Diagram (ERD). An ERD is a visual representation of the database's structure, including the tables and their relationships.
# 
# The ERD will provide a clear overview of the database structure, making it easier to understand how the tables are related and how the data flows between them.
# 
# This ERD was developed in MySQL management system.

# ![Screen%20Shot%202023-05-17%20at%204.04.37%20PM.png](attachment:Screen%20Shot%202023-05-17%20at%204.04.37%20PM.png)

# ### Explanation of each table: 
# 
# #### Game Table
# * id: Unique identifier for each videogame
# * genre_id: The genre of each videogame, referring to a genre table
# * game_name: The name of the videogame
# 
# #### Genre Table
# * genre_id: Unique identifier for each genre
# * genre_name: Name of the genres
# 
# #### Game Publisher Table
# * game_id: Unique identifier for each game.
# * id: Another unique identifier.
# * publisher_id: The identifier of the publisher associated with each game
# 
# #### Game Platform Table
# * game_publisher: Unique identifier for a game-publisher relationship
# * id: It Represents row unique identifier
# * platform_id: It provides an identifier of a specific gaming platform
# * release_year: The year in which a game was released
# 
# #### Publisher Table
# * id: Unique identifier for each entry in the table
# * publisher_name: Name of the publisher
# 
# #### Platform Table
# * id: Unique Identifier for each entry in this table
# * platform_name: Name of the platform
# 
# #### Region Sales Table
# * game_platform_id: it storages an unique identifier for the game-platform relationship
# * num_sales: Number of sales or units sold for a particular game-platform combination
# * region_id: The identifier for a specific region or geographic area
# 
# #### Region Table
# * id: Unique identifier for each region
# * region_name: Name of the region

# ## Limitations

# Please consider the following limitations in the source data that resulted in this database design:
# 
# * The release year applies to a combination of game, platform, and publisher, not just for a game as I assumed
# * The sales are captured overall as at a point in time and are not broken down by years
# * A game can have different publishers for different platforms
# * The data includes games released in 2016 and a couple of games released in 2017

# ## Problems to Solve

# Thu purpose of this analysis is to solve the following questions:
# 
# * Which game has the highest sales globally?
# * How many games are there in each genre?
# * How many games were released on each platform?
# * Top 10 games with the highest overall sales across all regions?
# * What are the total sales (in millions) for each genre?
# * Which game has the highest number of sales in Japan?
# * What is the total sales (in millions) for each platform?
# * Which games have global figures below 1 million dollars??
# * Which publisher has the highest number of sales?
# * How many games were released each year?
# * Most popular games that were published by "Electronic Arts
# * Compare  which genres are popular between Europe and Japan based on sales and average  (in millions) per game
# * Which games has the highest total sales (in millions) in the "North America" region
# 
# 

# #### Which game has the highest sales globally?

# In[152]:


# Sum the sales for the 4 regions grouped by game 
get_ipython().run_line_magic('sql', 'SELECT game.game_name, ROUND(SUM(region_sales.num_sales),2) AS global_sales FROM region_sales JOIN region ON region_sales.region_id = region.id JOIN game_platform ON game_platform.id = region_sales.game_platform_id JOIN game_publisher ON game_publisher.id = game_platform.game_publisher_id JOIN game ON game_publisher.game_id = game.id GROUP BY game.game_name ORDER BY global_sales DESC LIMIT 1;')


# According to the result, **"Call of Duty: Modern Warfare 3"** emerged as the top-selling video game worldwide between 2016 and 2017, encompassing all four regions.

# #### How many games are there in each genre?

# In[153]:


# Counting video games titles, grouped by genre 
get_ipython().run_line_magic('sql', 'SELECT genre.genre_name, COUNT(DISTINCT game.id) AS number_of_video_games FROM genre JOIN game ON genre.id = game.genre_id GROUP BY genre.genre_name ORDER BY number_of_video_games DESC;')


# This table provides a concise overview of the distribution of video games across different genres. AS we can see, **the most popular genre is 'Action' with 1900 distinct video games.** It's followed by 'Sports' and 'Misc' with 1,366 and 1,314 games respectively. At the end of the table you can find 'Platform', 'Strategy' and 'Puzzle'. 

# #### How many games were released on each platform?

# In[154]:


# Counting video games title, grouped by platform id. Several Joins are required
get_ipython().run_line_magic('sql', 'SELECT platform.platform_name, COUNT(game.id) AS total_number_of_video_games FROM game JOIN game_publisher ON game.id = game_publisher.game_id JOIN game_platform ON game_platform.game_publisher_id = game_publisher.id JOIN platform ON platform.id = game_platform.platform_id GROUP BY platform.platform_name ORDER BY total_number_of_video_games DESC;')


# The table displays the total number of video games available for each platform. The **PlayStation 2 (PS2) is indicated as having the highest number of video games with 439 titles.** The Xbox 360 and PlayStation 3 also show a significant number of games. On the other hand, platforms like DC (Dreamcast), GEN (Sega Genesis), and GameBoy Advance are mentioned as having a relatively lower presence in the market.
# 
# it's important to interpret the information with caution, as gaming trends and platform popularity changed since the dataset's last update was in 2016/2017.

# #### Top 10 games with the highest overall sales across all regions?

# In[155]:


# Sum the sales for the 4 regions grouped by game 
get_ipython().run_line_magic('sql', 'SELECT game.game_name, ROUND(SUM(region_sales.num_sales),2) AS global_sales FROM region_sales JOIN region ON region_sales.region_id = region.id JOIN game_platform ON game_platform.id = region_sales.game_platform_id JOIN game_publisher ON game_publisher.id = game_platform.game_publisher_id JOIN game ON game_publisher.game_id = game.id GROUP BY game.game_name ORDER BY global_sales DESC LIMIT 10;')


# As we can observe in the table, the Call of Duty franchise showcased its dominance in global video game sales during the specified period. "Call of Duty: Modern Warfare 3" secured the top spot as the best-selling game worldwide. Interestingly, the remaining versions of Call of Duty also claimed positions within the top 10 list, illustrating the franchise's widespread popularity and continued success.
# 
# Among the Call of Duty titles, "The Elder Scrolls V: Skyrim" managed to break into the top 10 with an impressive 18.64 million units sold.

# #### What are the total sales (in millions) for each genre?

# In[156]:


# Sum the sales by for th4 regions grouped by genres
get_ipython().run_line_magic('sql', 'SELECT genre_name, ROUND(SUM(region_sales.num_sales),2) AS global_sales FROM region_sales JOIN region ON region_sales.region_id = region.id JOIN game_platform ON game_platform.id = region_sales.game_platform_id JOIN game_publisher ON game_publisher.id = game_platform.game_publisher_id JOIN game ON game_publisher.game_id = game.id JOIN genre ON genre.id = game.genre_id GROUP BY genre.genre_name ORDER BY global_sales DESC;')


# As we can see in this table the **top three genres in terms of global sales re Sports, Action and Shooter**. This suggests a high demand for games that involve physical activity and intense action. Also, Racing and Role-Playing games demostrate a strong in sales. At the end of the table, we can find Puzzles, Strategy and Adventure genres. 

# #### Which game has the highest number of sales in Japan?

# In[157]:


# Get the game name and total sales, conditioned only by Japan
get_ipython().run_line_magic('sql', 'SELECT game.game_name, genre_name, region_sales.num_sales AS sales_in_japan FROM region_sales JOIN region ON region_sales.region_id = region.id  JOIN game_platform ON game_platform.id = region_sales.game_platform_id JOIN game_publisher ON game_publisher.id = game_platform.game_publisher_id JOIN game ON game.id = game_publisher.game_id JOIN genre ON genre.id = game.genre_id WHERE region.id = 3 ORDER BY sales_in_japan DESC LIMIT 5;')


# According to the table, **the most popular game in Japan**, in terms of total sales, is **"Monster Hunter Freedom 3"** which belongs to the Role-Playing genre, and it generated 4.87 million dollars in sales. 
# Other popular games are "Monster Hunter Freedom Unite", "Monster Hunter 4", "Street Fighter II: The World Warrior" and "Monster Hunter X"

# #### What is the total sales (in millions) for each platform?

# In[158]:


# Group platform and get their total amount 
get_ipython().run_line_magic('sql', 'SELECT platform.platform_name AS platform, SUM(region_sales.num_sales) AS global_sales FROM region_sales JOIN region ON region_sales.region_id = region.id JOIN game_platform ON game_platform.id = region_sales.game_platform_id JOIN platform ON platform.id = game_platform.platform_id JOIN game_publisher ON game_publisher.id = game_platform.game_publisher_id JOIN game ON game.id = game_publisher.game_id GROUP BY platform.platform_name ORDER BY global_sales DESC LIMIT 10;')


# The table show that the platform (or console) with their respective global sales. **The platform PS2 has the highest sales with 456.75 millions dollas**. In second and third place we find Xbox360 and PS3 with 432.53 and 389.46 million dollars respectively. Other popular consoles are PS, Wii and PS4. 
# 
# * It's important to mention that this dataset dates back to 2017, that helps explain the popularity of PlaysStation 2 compared to the PS3 which had just recently entered the market at that time. 

# #### Which games have global figures below 1 million dollars?

# In[159]:


# Sum the 4 regions grouped by game name where the global sales don't reach 1 million 
get_ipython().run_line_magic('sql', 'SELECT game.game_name AS game, genre.genre_name AS genre FROM region_sales JOIN region ON region_sales.region_id = region.id JOIN game_platform ON game_platform.id = region_sales.game_platform_id JOIN game_publisher ON game_publisher.id = game_platform.game_publisher_id JOIN game ON game.id = game_publisher.game_id JOIN genre ON genre.id = game.genre_id GROUP BY game.game_name, genre.genre_name HAVING ROUND(SUM(region_sales.num_sales),2)< 1;')


# In[160]:


# Counting how many video games are below 1 million dollas in global sales
get_ipython().run_line_magic('sql', 'SELECT COUNT(*) AS total_games_below_1M FROM (SELECT game.game_name AS game, genre.genre_name AS genre FROM region_sales JOIN region ON region_sales.region_id = region.id JOIN game_platform ON game_platform.id = region_sales.game_platform_id JOIN game_publisher ON game_publisher.id = game_platform.game_publisher_id JOIN game ON game.id = game_publisher.game_id JOIN genre ON genre.id = game.genre_id GROUP BY game.game_name, genre.genre_name HAVING ROUND(SUM(region_sales.num_sales),2)< 1) AS subquery;')


# There are 786 videogames that couldn't reach 1 million dollars in global sales. 

# In[165]:


get_ipython().run_line_magic('sql', 'SELECT genre.genre_name AS genre, COUNT(game.game_name) AS total_games_below_1M FROM (SELECT genre.genre_name, game.game_name FROM region_sales JOIN region ON region_sales.region_id = region.id JOIN game_platform ON game_platform.id = region_sales.game_platform_id JOIN game_publisher ON game_publisher.id = game_platform.game_publisher_id JOIN game ON game.id = game_publisher.game_id JOIN genre ON genre.id = game.genre_id GROUP BY genre.genre_name, game.game_name HAVING ROUND(SUM(region_sales.num_sales),2)< 1) AS subquery GROUP BY genre_name ORDER BY total_games_below_1M DESC;')


# #### Which publisher has the highest number of sales?

# In[171]:


# Sum num_sales grouped by publisher 
get_ipython().run_line_magic('sql', 'SELECT publisher.publisher_name, COUNT(*) AS number_of_videogames, ROUND(SUM(num_sales),2) AS global_sales, ROUND(AVG(num_sales),2) as average FROM region_sales JOIN region ON region_sales.region_id = region.id JOIN game_platform ON game_platform.id = region_sales.game_platform_id JOIN game_publisher ON game_publisher.id = game_platform.game_publisher_id JOIN publisher ON publisher.id = game_publisher.publisher_id GROUP BY publisher.publisher_name ORDER BY global_sales DESC LIMIT 15;')


# AS we can see, **the publisher with the most number of videogames and global sales is Electronic Arts with 853.35 million dollars**. Activision follows closely behind with 2,810 videogames in their repository and 691.1 milliosn dollars generated. Capcom ranks third 185 millions dollars genereted by 846 videogames. . 
# 
# Something interesting is that the publisher "Bethesda Softworks" stands out with an average of .38 million dollas in sales per videogame, which is the highest average among the listed publishers. They only have 210 videogames and a total of 78.87 million dollas in gobal sales.
# Also 989 Studios stands out with an average sales per videogame of 0.25 million dollars, which is one of the highest average sales in this data. 

# #### Most popular games that were published by "Electronic Arts

# In[176]:


# Sort videogames by global sales where publisher is Electronic Arts
get_ipython().run_line_magic('sql', "SELECT game.game_name, ROUND(SUM(region_sales.num_sales),2) AS global_sales FROM region_sales JOIN region ON region_sales.region_id = region.id JOIN game_platform ON game_platform.id = region_sales.game_platform_id JOIN game_publisher ON game_publisher.id = game_platform.game_publisher_id JOIN publisher ON publisher.id = game_publisher.publisher_id JOIN game ON game.id = game_publisher.game_id WHERE publisher.publisher_name = 'Electronic Arts' GROUP BY game.game_name ORDER BY global_sales DESC LIMIT 10;")


# The table above shows us that the most popular Electronic Art'svideogame s FIFA 15 generating 15.73 million dollars. It is followed by FIFA 14 and Battlefield 3. 
# Other versions of FIFA also appear on the list. Notably, Need for Speed: Most Wanted and Battlefield 4 managed to secure a position i nthe top 10 as well. 

# #### Compare  which genres are popular between Europe and Japan based on sales and average  (in millions) per game

# In[183]:


# Sum sales and average sales per video game by genre only in Japan
get_ipython().run_line_magic('sql', "SELECT genre_name, ROUND(SUM(region_sales.num_sales),2) AS sales_in_Japan, ROUND(AVG(region_sales.num_sales),2) AS average FROM region_sales JOIN region ON region_sales.region_id = region.id JOIN game_platform ON game_platform.id = region_sales.game_platform_id JOIN game_publisher ON game_publisher.id = game_platform.game_publisher_id JOIN game ON game_publisher.game_id = game.id JOIN genre ON genre.id = game.genre_id WHERE region.region_name = 'Japan' GROUP BY genre.genre_name ORDER BY sales_in_Japan DESC;")


# In[182]:


# Sum sales and average sales per video game by genre in Europe
get_ipython().run_line_magic('sql', "SELECT genre_name, ROUND(SUM(region_sales.num_sales),2) AS sales_in_Europe, ROUND(AVG(region_sales.num_sales),2) AS average FROM region_sales JOIN region ON region_sales.region_id = region.id JOIN game_platform ON game_platform.id = region_sales.game_platform_id JOIN game_publisher ON game_publisher.id = game_platform.game_publisher_id JOIN game ON game_publisher.game_id = game.id JOIN genre ON genre.id = game.genre_id WHERE region.region_name = 'Europe' GROUP BY genre.genre_name ORDER BY sales_in_Europe DESC;")


# In Japan, the top-selling genre is Role-Playing with total sales of 38.83 million and an average of 0.25 million per game. It is followed by Action, Fithing, Sports and Shooter. 
# 
# On the othe rhand, in Europe, the top selling ggenre is Sports which generated 159.5 million dollas. Genres like Shooter, Action and Racing have significant figures. 
# 
# From this comparison, we can observe that the popular genre differ betwwn Europe ans Japan. While Sports and Shotter have siginificant presence in Europe, Role-Playing and Action dominate the Japanese market. Pereferences and cultural factors influence the popularity of different genres in these two regions. 

# #### Which games has the highest total sales (in millions) in the "North America" region

# In[186]:


# Most popular games in the North America based on sales 
get_ipython().run_line_magic('sql', "SELECT game.game_name, ROUND(SUM(region_sales.num_sales),2) AS sales FROM region_sales JOIN region ON region_sales.region_id = region.id JOIN game_platform ON game_platform.id = region_sales.game_platform_id JOIN game_publisher ON game_publisher.id = game_platform.game_publisher_id JOIN game ON game_publisher.game_id = game.id WHERE region.region_name = 'North America' GROUP BY game.game_name ORDER BY sales DESC LIMIT 15;")


# The table shows the games that have achieved significant sales in the North America market with the Call of Duty franchise dominating the top positions. Other popular titles like Guitar Hero III, the Elder Scrils V: Skyrim, Battlefield 3, Pac-Man and Madden 07 also made it to the list. 
# 
# North America, particularly United States represent a robust market with a a great amount of gamers and gaming enthusiasts. Bedisdes, combined with their disposable income, technological presence and industry presence make it a vital and potential lucrative market for the gaming industry. 

# ### Conclusions

# So, based on the analusis conducted on the videogame dataset revealed that preferences and market trends differ between regions. In Europe leans towards Sports and Shooting genres, while in Japan, has a strong affinity for Role-Playing games. Understand the different cultural factors in each region is important at the moment of game development and publishing. 
# 
# Electronic Arts and Activision stand out as publisher with great number of games developed and high global sales. But, it's important to highlight succeful titles of Capcom, Bethesda Softworks and Ubisoft.
# 
# Specific franchise like FIFA and Call of Duty have consistently performed well in terms of sales, indicating their popularity among gamers. 
# 
# Japan and North America are the most important market for this industry due their population, technological advancements and strong presence in the gaming industry. 
