import seaborn as sb
from cProfile import label
from lib2to3.pytree import HUGE
import numpy as np
import random
from numpy import row_stack
import pandas as pd
import matplotlib.pyplot as plt
import re
print("\033c")
dataSet = pd.read_csv(
    r'/Users/muhammadali/Documents/University/Introduction to Data Science/Lab/the-hello-dataset-fa22.csv')


# 1. Print the list of all students whose  first name starts with letter the 'H'.
# print(dataSet[dataSet['Name'].str.startswith('H')])

# 2. Print the total number of students who have a three words name (first-middle-surname).
# name = dataSet['Name']
# print("Total Number of Students= ", name.str.contains('\w+\s\w+\s\w').sum())

# 3. Print the percentage of students who have a CGPA of 3.0 or above.
# cgpa = dataSet[dataSet['CGPA'] >= 3.0].count() / dataSet.count() * 100
# print("Percentage of Students CGPA > 3 = ", cgpa['CGPA'].round(2), "%")

# 4. Plot a pie chart to show the ratio of male and female students.
# male = dataSet['Gender'].str.startswith('M').sum()
# female = dataSet['Gender'].str.startswith('F').sum()
# gender = ["Male", "Female"]
# data = [male, female]
# plt.pie(data, labels=gender, autopct='%1.1f%%')
# plt.title("Ratio of Male and Female Students")
# plt.show()

# 5. Plot the CGPA of all male students on a histogram with intervals 2.0-2.5, 2.6-3.0, 3.1-3.5, 3.6-4.0.
# list = dataSet[dataSet['Gender'].str.startswith('M')]
# maleList = list['CGPA'].tolist()
# intervals = [2.0, 2.5, 3.0, 3.5, 4.0]
# plt.hist(maleList, bins=intervals, ec='black')
# plt.title("CGPA of all Male Students")
# plt.xlabel("CGPA")
# plt.ylabel("Number of Students")
# plt.xticks(intervals)
# plt.show()


# 6. Plot the HSSC-1 marks of all male vs female students on a scatter plot.
# randomlist = random.sample(range(0, 500), 21)
# maleGrades = dataSet[dataSet['Gender'].str.startswith(
#     'M')]["HSSC-1"].tolist()
# femaleGrades = dataSet[dataSet['Gender'].str.startswith(
#     'F')]["HSSC-1"].tolist()
# maleGrades = maleGrades[:len(femaleGrades)]
# plt.scatter(maleGrades, randomlist, marker='o', label="Male")
# plt.scatter(femaleGrades, randomlist, marker='x', label="Female")
# plt.xlabel('Marks Scored', fontsize=12)
# plt.ylabel('Total Marks', fontsize=12)
# plt.title("Marks of all Male vs Female Students")
# plt.legend()
# plt.show()

# 7. Plot the favorite colors of male vs female students on a bar chart.
# maleFavColor = dataSet[dataSet['Gender'].str.startswith(
#     'M')]["FavoriteColor"].count()
# femaleFavColor = dataSet[dataSet['Gender'].str.startswith(
#     'F')]["FavoriteColor"].count()
# favColor = dataSet.groupby(["FavoriteColor", "Gender"]
#                            ).size().unstack(level=1).plot(kind='bar')
# plt.xlabel("Male")
# plt.ylabel("Female")
# plt.show()


# 8. Plot line chart of students and their birth months.
# birthMonth = dataSet["BirthMonth"].tolist()
# plt.plot(birthMonth, '-', label='birthMonth')
# plt.xlabel("Students")
# plt.ylabel("Birth Month")
# plt.show()
