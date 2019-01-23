#Import Pandas
import pandas as pd

#Load Videogames Dataset
videogames = pd.read_csv('Videogames2016.csv', low_memory=False)

#Print the first five rows
videogames.head(5)

#Replace empty values with 0

videogames.fillna(0, inplace=True)

#Replace 'tbd' string with 0
videogames.replace('tbd',0)

#Check data type for all columns
videogames.dtypes

#change User_Score data type from Object to numeric

videogames['User_Score'] = pd.to_numeric(videogames['User_Score'])

#Show the first 10 videogames

videogames.head(10)

# Calculate C
C = videogames['User_Score'].mean()
print(C)

# Calculate the minimum number of User's votes required to be in the chart, m
m = videogames['User_Count'].quantile(0.90)
print(m)

# Filter out all qualified Video Games into a new DataFrame
q_videogames = videogames.copy().loc[videogames['User_Count'] >= m]
q_videogames.shape

# Function that computes the weighted rating of each Videogame
def weighted_rating(x, m=m, C=C):
    v = x['User_Count']
    R = x['User_Score']
    # Calculation
    return (v/(v+m) * R) + (m/(m+v) * C)

# Define a new feature 'score' and calculate its value with 'weighted_rating()'
q_videogames['score'] = q_videogames.apply(weighted_rating, axis=1)

#Sort videogames based on score calculated above
q_videogames = q_videogames.sort_values('score', ascending=False)

#Print the top 30 videogames
q_videogames[['Name', 'User_Count', 'User_Score', 'score']].head(30)
