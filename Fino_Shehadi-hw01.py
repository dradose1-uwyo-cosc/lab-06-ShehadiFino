# Shehadi Fino
# COSC 1010
# Submission Date: 10-14-24
# HW 01
# Lab Section:14
# Sources, people worked with, help given to: Ryan
# your
# comments
# here

# Homework Question:
#
# You are given a list of dictionaries where each dictionary represents a student
# and their scores
# in different subjects.
#
# Student Data:
students = [
 {"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
 {"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
 {"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
 {"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
 ]

# Write a Python program that:
# 1. Calculates the average score for each student.
# 2. Stores these averages in a new dictionary where the student’s name is the key
#and their average score is the value.
# 3. Prints the names of students whose average score is greater than 80.
# Your task is to calculate the average scores for each student and print the names of students
# whose average score is greater than 80.

#Solutionl6

average_scores = {}

for student in students:
    name = student["name"]
    scores = student["scores"]
    average = sum(scores.values()) / len(scores)
    average_scores[name] = average

print("Students with average scores greater than 80:")
for name, average in average_scores.items():
    if average > 80:
        print(f"{name}: {average:.2f}")