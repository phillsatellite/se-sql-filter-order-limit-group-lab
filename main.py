import pandas as pd
import sqlite3

##### Part I: Basic Filtering #####

# Create the connection
# Note the connect is 'conn1' since there will be multiple .db used
conn1 = sqlite3.connect('planets.db')

# Select all
select_planets = pd.read_sql("""
SELECT * 
FROM planets; 
""", conn1)

# STEP 1
# Return planets that have 0 moons
df_no_moons = pd.read_sql("""
SELECT *
FROM planets
WHERE num_of_moons = 0;
""", conn1)

#print(df_no_moons)

# STEP 2
# Retuns planets with exactly 7 letters in their name 
df_name_seven = pd.read_sql("""
SELECT name, mass
FROM planets
WHERE LENGTH(name) = 7;
""", conn1)

#print(df_name_seven)

##### Part 2: Advanced Filtering #####

# STEP 3
# Returns planets names that have a mass <= 1
df_mass = pd.read_sql("""
SELECT name, mass
FROM planets
WHERE mass <= 1.00
""", conn1)

#print(df_mass)

# STEP 4
# Returns all planets with >= 1 moons and a mass < 1
df_mass_moon = pd.read_sql("""
SELECT *
FROM planets
WHERE num_of_moons >= 1
    AND mass < 1.00;
""", conn1)

#print(df_mass_moon)

# STEP 5
# Returns name and color of planets that have color containing string blue
df_blue = pd.read_sql("""
SELECT name, color
FROM planets
WHERE color LIKE "%blue";
""", conn1)

#print(df_blue)

##### Part 3: Ordering and Limiting #####

# STEP 0

# Create a connection
# Note the connect is 'conn2' since they will be multiple .db used
conn2 = sqlite3.connect('dogs.db')

# Select all
select_all_dogs = pd.read_sql("""
SELECT * 
FROM dogs;
""", conn2)

#print(select_all_dogs)

# STEP 6
# Returns name age breed sorts youngest - oldest
df_hungry = pd.read_sql("""
SELECT name, age, breed
FROM dogs
WHERE hungry = 1
ORDER BY age ASC;
""", conn2)

df_hungry['name'] = df_hungry['name'].astype(object).where(df_hungry['name'].notna(), None)

#print(df_hungry)

# STEP 7
# Returns name age hungry if dog is between 2/7 and hungry = true order alphabetically
df_hungry_ages = pd.read_sql("""
SELECT name, age, hungry
FROM dogs
WHERE age BETWEEN 2 AND 7
AND hungry = 1
ORDER BY name ASC;
""", conn2)

#print(df_hungry_ages)

# STEP 8
# Return name age hungry for hugry dogs sort alphabetically based on breed
df_4_oldest = pd.read_sql("""
SELECT name, age, breed
FROM dogs
ORDER BY age DESC, breed ASC
LIMIT 4;
""", conn2)

#print(df_4_oldest)

##### Part 4: Aggregation #####

# STEP 0

# Create a connection
# Note the connect is 'conn3' since they will be multiple .db used
conn3 = sqlite3.connect('babe_ruth.db')

# Select all
select_all_stats = pd.read_sql("""
SELECT * 
FROM babe_ruth_stats; 
""", conn3)

#print(select_all_stats)

# STEP 9
# Total years played
df_ruth_years = pd.read_sql("""
SELECT COUNT(*) AS total_years
FROM babe_ruth_stats;
""", conn3)

#print(df_ruth_years)

# STEP 10
# Returns total home runs
df_hr_total = pd.read_sql("""
SELECT SUM(HR) AS total_hr
FROM babe_ruth_stats;
""", conn3)

#print(df_hr_total)

##### Part 5: Grouping and Aggregation #####

# STEP 11
# Replace None with your code
df_teams_years = pd.read_sql("""
SELECT team, count(*) AS number_years
FROM babe_ruth_stats
GROUP BY team
""", conn3)

#print(df_teams_years)

# STEP 12
# Replace None with your code
df_at_bats = pd.read_sql("""
SELECT team, AVG(at_bats) AS average_at_bats
FROM babe_ruth_stats
GROUP BY team
HAVING AVG(at_bats) > 200;
""", conn3)

print(df_at_bats)

conn1.close()
conn2.close()
conn3.close()