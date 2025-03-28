# PracticeAssessment-Friday-#######################################################################################################################################################
# 
# Name:Yunhan Jiang
# SID:740083712
# Exam Date:28/03/2025
# Module:BEMM458 Programming for business analycis
# Github link for this assignment: https://github.com/UniversityExeterBusinessSchool/practiceassessment-friday-Jiang-Yunhan
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Data Processing and Loops
# You are given a string representing customer reviews. Use a for loop to process the text and count occurrences of specific keywords.
# Your allocated keywords are determined by the first and last digit of your SID.
# Count and store occurrences of each keyword in a dictionary called keyword_counts.
 
customer_reviews = """The product is well-designed and user-friendly. However, I experienced some issues with durability. The customer service was helpful, 
but I expected a faster response. The quality of the materials used is excellent. Overall, the purchase was satisfactory."""

# Keywords dictionary
keywords = {
    0: 'user-friendly',
    1: 'helpful',
    2: 'durability',
    3: 'response',
    4: 'satisfactory',
    5: 'quality',
    6: 'service',
    7: 'issues',
    8: 'purchase',
    9: 'materials'
}

# Write your code to process the text and count keyword occurrences
SID = "740083712"
first_digit = int(SID[0])
last_digit = int(SID[-1])

# Get corresponding keywords
selected_keywords = [keywords[first_digit], keywords[last_digit]]

# Initializes the counting dictionary
keyword_counts = {keyword: 0 for keyword in selected_keywords}

# Iterate through the list of keywords
for keyword in selected_keywords:
    keyword_counts[keyword] = customer_reviews.lower().count(keyword.lower())

print(keyword_counts)

##########################################################################################################################################################

# Question 2 - Business Metrics
# Scenario - You work in an online retail company as a business analyst. Your manager wants weekly reports on financial performance, including:
# Gross Profit Margin, Inventory Turnover, Customer Retention Rate (CRR), and Break-even Analysis. Implement Python functions 
# that take relevant values as inputs and return the computed metric. Use the first two and last two digits of your ID number as input values.

# Insert first two digits of ID number here:
first_two = 74
# Insert last two digits of ID number here:
last_two = 12
# Write your function for Gross Profit Margin
def gross_profit_margin(gross_profit, revenue):
    return (gross_profit / revenue) * 100
# Write your function for Inventory Turnover
def inventory_turnover(cogs, avg_inventory):
    return cogs / avg_inventory
# Write your function for Customer Retention Rate (CRR)
def customer_retention_rate(customers_end, customers_start, new_customers):
    return ((customers_end - new_customers) / customers_start) * 100
# Write your function for Break-even Analysis
def break_even_analysis(fixed_cost, contribution_margin):
    return fixed_cost / contribution_margin
# Call your functions here
gpm = gross_profit_margin(first_two, last_two)
it = inventory_turnover(first_two, last_two)
crr = customer_retention_rate(first_two, last_two, 10)
bea = break_even_analysis(first_two, last_two)
##########################################################################################################################################################

# Question 3 - Forecasting and Regression
# A logistics company has gathered data on delivery costs and shipment volumes. The table below provides different costs and their corresponding shipment volumes.
# Develop a linear regression model and determine:
# 1. The optimal delivery cost that maximizes profit
# 2. The expected shipment volume when the cost is set at £68

"""
Delivery Cost (£)    Shipment Volume (Units)
-------------------------------------------
25                  500
30                  480
35                  450
40                  420
45                  400
50                  370
55                  340
60                  310
65                  290
70                  250
"""

# Write your regression model code here
import numpy as np

# Dataset
cost = np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70])
volume = np.array([500, 480, 450, 420, 400, 370, 340, 310, 290, 250])
# Linear regression calculations
n = len(cost)
sum_x = np.sum(cost)
sum_y = np.sum(volume)
sum_xy = np.sum(cost * volume)
sum_x2 = np.sum(cost ** 2)
# Slope (a) and intercept (b) calculation
numerator = n * sum_xy - sum_x * sum_y
denominator = n * sum_x2 - sum_x ** 2
a = numerator / denominator  # Slope
b = (sum_y - a * sum_x) / n  # Intercept

# 1. Find cost that maximizes revenue (X*Y)
optimal_cost = -b / (2 * a)

# 2. Predict volume at £68 using regression equation
predicted_volume = a * 68 + b

# Results formatted to 2 decimal places
print(f"1. Optimal Delivery Cost: £{optimal_cost:.2f}")
print(f"2. Predicted Volume at £68: {predicted_volume:.0f} units")
##########################################################################################################################################################

# Question 4 - Debugging and Data Visualization

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student ID number
your_ID = input("Enter your Student ID: 740083712")
max_value = int(your_ID)
random_numbers = [random.randint(1, max_value) for _ in range(100)]

# Plotting the numbers in a histogram
plt.hist(random_numbers, bins=10, edgecolor='blue', alpha=0.7, color='red')
plt.title("Histogram of 100 Random Numbers")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()