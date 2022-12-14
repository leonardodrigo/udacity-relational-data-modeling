# Relational Database Modeling

## Objectives
In this project, the main objective is to create a simple relational data model using Python and PostgreSQL to simulate a real project at Sparkify, some music streaming startup. Sparkify team wants to analyze the data they've been collecting on songs and user activity on their new music streaming application, but they don't have a database and all data are available only in JSON files generated by the app.

## How to run the scripts
First of all, you must have [Python](https://www.python.org/downloads/) and a [PostgreSQL](https://www.postgresql.org/download/) database instance configured in your machine. The others Python packages can be installed running the command below:

``` pip install -r requirements.txt ```

Now, we can start building our model. Running ```create_tables.py``` we are going to create a locally new database called *sparkifydb* and all the tables described in the next sessions using ```sql_queries.py```. With them, the next step is to run ```etl.py``` to read json files (song_data and log_data), process data and write into the tables. If you prefer, you can run ```etl.ipynb```, which has the same code as .py one, to see step by step what is going on with the ETL task.

* After running the ETL, you can do sanity checks in the database with ```test.ipynb```

## JSON files

*data/song_data.json* contains all songs metadata generated by the streaming app. They are being used to insert data into artists and songs tables.

*data/log_data.json* simulate the application logs, registering events sent by users regarding the listened musics and other information about themselves. This data are being used for songplays (fact table) and users tables.

## Modeling

A query in ```elt.py``` collects song and artist id from the songs and artists tables and combines this with log JSON file derived data to insert into songplays table. Below we can check the diagram that represents tables relashionship.
![Entity Relationship Diagram (3)](https://user-images.githubusercontent.com/49285727/198907964-f840ff40-079e-4e3f-ae3b-a07d64f70dd8.jpg)



