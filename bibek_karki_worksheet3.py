# -*- coding: utf-8 -*-
"""Bibek_Karki_Worksheet3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/174xy4g1hDCnpqOR_a7pTVMja_kYUZHsN
"""

#3.1
#question 1
import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/week 2 AI/Titanic-Dataset.csv')
print(df.head())

#problem 1
#question 1
fare = df[['Fare']]
print(fare.head())

#question 2
class_age = df[['Pclass', 'Age']]

print(class_age.head())

#question 3
survived_gender = df[['Survived', 'Sex']]

print(survived_gender.head())

#problem 2
#question 1
fare_gt_100 = df[df['Fare'] > 100]

print(fare_gt_100)

#question 2
first_class = df[df['Pclass'] == 1]
print(first_class)

#question 3
female_under_18 = df[(df['Age'] < 18) & (df['Sex'] == 'female')]
print(female_under_18)

#Subsetting Rows by Categorical variables:
#question 1
embarked_c_or_s = df[df['Embarked'].isin(['C', 'S'])]
print(embarked_c_or_s)

#question 2
first_second_class = df[df['Pclass'].isin([1, 2])]
print(first_second_class)

#3.3
#question 1
import pandas as pd
df = pd.read_csv("/content/drive/MyDrive/week 2 AI/Titanic-Dataset.csv")
df['Age'].fillna(df['Age'].median(), inplace=True)

df['fare_per_year'] = df['Fare'] / df['Age']

#question 2
high_fare_age = df[df['fare_per_year'] > 5]
print(high_fare_age)

#question 3
high_fare_age_srt = high_fare_age.sort_values(by='fare_per_year', ascending=False)
print(high_fare_age_srt)

# question 4
result = high_fare_age_srt[['Name', 'fare_per_year']]
print(result)

#question 5
# Display the result
print(result.head())

#question 1
import pandas as pd

df = pd.read_csv("/content/drive/MyDrive/week 2 AI/Titanic-Dataset.csv")
def categorize_age(age):
    if age < 18:
        return 'child'
    elif 18 <= age <= 64:
        return 'adult'
    else:
        return 'senior'

df['age group'] = df['Age'].apply(categorize_age)

print(df[['Age', 'age group']].head())

#question 2
total_passengers = df['Age'].notna().sum()

print(f"Total number of passengers: {total_passengers}")

#question 3
age_group_counts = df['age group'].value_counts()

print(age_group_counts)

#question 4
age_group_proportions = age_group_counts / total_passengers

print(age_group_proportions)

#question 5
age_group_percentage = age_group_proportions * 100

print(age_group_percentage)