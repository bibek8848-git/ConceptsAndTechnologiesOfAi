# -*- coding: utf-8 -*-
"""Worksheet0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vb438hD-66b0h2qmnnqtmg61CdQlb-52
"""

#given temperatures
temperatures = [8.2, 17.4, 14.1, 7.9, 18.0, 13.5, 9.0, 17.8, 13.0, 8.5,
16.5, 12.9, 7.7, 17.2, 13.3, 8.4, 16.7, 14.0, 9.5, 18.3, 13.4, 8.1,
17.9, 14.2, 7.6, 17.0, 12.8, 8.0, 16.8, 13.7, 7.8, 17.5, 13.6, 8.7,
17.1, 13.8, 9.2, 18.1, 13.9, 8.3, 16.4, 12.7, 8.9, 18.2, 13.1, 7.8,
16.6, 12.5]

#create empty list for each category
cold = []
mild = []
comfortable = []

#classify each temperature
for temp in temperatures:
    if temp < 10:
        cold.append(temp)
    elif 10 <= temp < 15:
        mild.append(temp)
    elif 15 <= temp < 20:
        comfortable.append(temp)

#print the outcomes
print("Cold : ", cold)
print("Mild : ", mild)
print("Comfortable : ", comfortable)

#TASK2

#count the number of items in each list
cold_count = len(cold)
mid_count = len(mild)
comfortable_count = len(comfortable)

#print the outcomes
print("cold count : ", cold_count)
print("mild count : ", mid_count)
print("comfortable count : ", comfortable_count)

#TASK3

#create new list for temp in fahrenheit
temperatures_fahrenheit = []

for temp in temperatures:
    fahrenheit = (temp * 9/5)+32
    temperatures_fahrenheit.append(fahrenheit)

print("temperautures in fahrenheit : ", temperatures_fahrenheit)

#TASK4

#create empty lists for each time of the day
night_temps = []
evening_temps = []
day_temps = []

#group the temperatures
for temp in range(0, len(temperatures), 3):
    night_temps.append(temperatures[temp])
    evening_temps.append(temperatures[temp+1])
    day_temps.append(temperatures[temp+2])

#calculate the average day time temperature
average_day_temp = sum(day_temps)/len(day_temps)

#print the required outputs
print("Night temperatures : ", night_temps)
print("Evening temperatures : ", evening_temps)
print("Day temperatures : ", day_temps)
print("Average day-time temperature : ",average_day_temp)

#plot "day vs temperature" using matplotib
"""
import matplotlib.pyplot as plt

#plot day-time temperatures
days = list(range(1, len(day_temps)+1))
plt.plot(days, day_temps, marker='o', color="red", label="Day Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature(°C)")
plt.title("Day vs Temperature")
plt.legend()
plt.show()

#TASK1
def sum_nested_list(nested_list):
    """Calculate the sum of all numbers in a nested list.
    This function takes a list that may contain integers and other nested lists.
    It recursively traverses the list and sums all the integers, no matter how deeply nested they are.
    Args:
    nested_list (list) : A list that may contain integers or other lists of integers.
    Returns:
    int: The total sum of all integers in the nested list, including those in sublists.

    Example:
    >>> sum_nested_list([1, [2, [3, 4], 5], 6, [7, 8]])
    36
    >>> sum_nested_list([1, [2, 3], [4, [5]]])
    15
    """
    total = 0
    for element in nested_list:
        if isinstance(element, list): #check if the element is a list
            total += sum_nested_list(element) #recursively sum the nested list
        else:
            total += element #add the number to the total
    return total

#run the fuction
nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
result = sum_nested_list(nested_list)
print("the total sum is : ", result)

#TASK2

def generate_permutations(s):
    """
    Generate all unique permutations of a given string.
    This function uses the concept of recursion to generate the permutations by fixing a character and permutatin the remaining characters. The characters are the listed in a set in oredr to ensure their uniqueness.

    Args:
    s (str) : The input string for which permutations are to be generated.

    Returns:
    list: A list of unique permutations of the input string.

    Examples:
    >>> generate_permutations("abc")
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    >>> generate_permutations("aab")
    ['aab', 'aba', 'baa']

    """
    #if the string has one character or is empty, return it as a single element list
    if len(s) <= 1:
        return[s]

    permutations = []

    for i, char in enumerate(s):
        #exclude the current character and permutate the remaining strings
        remaining = s[:i]+s[i+1:]
        for perm in generate_permutations(remaining):
            permutations.append(remaining)

    return list(set(permutations)) #remove the dupicates by converting to a set and back to a list

#test the function
print(generate_permutations("abc"))
print(generate_permutations("aab"))

def calculate_directory_size(directory):
    """
    Recursively calcualtes the total size of a drectory.

    Args:
    directory(dict) : A directry reperesenting a dircetory structure.

    Returns:
    int : The total size of the directory in KB.
    """

    total_size = 0
    for key, value in directory.items():
        if isinstance(value, dict):
            total_size += calculate_directory_size(value)
        else:
            total_size += value
    return total_size

#Sample directory structure
directory_structure = {
    "file1.txt": 200,
    "file2.txt": 300,
    "subdir1": {
        "file3.txt": 400,
        "file4.txt": 100
    },
    "subdir2": {
        "subsubdir1": {
            "file5.txt": 250
        },
        "file6.txt": 150
    }
}

#testing the function
total_size = calculate_directory_size(directory_structure)
print(f"Total size of the directory : {total_size} KB")

#TASK1

def min_coins(coins, amount):
    """
    Finds the minimum number of coins needed to make up a given amount using dynamic pragramming

    Parameters:
    coins(list of int) : A list of coin denominations available for making change.
    amount(int) : The target amount for which we need to find minimum number of coins.

    Returns:
    int : the minimum number of coins required to make the given amount.
            if it is not possible, returns -1.
    """
    #initialize the dp array with a large value representing infinity
    dp = [float('inf')] * (amount+1)
    dp[0] = 0 #no coins is needed to make amount 0

    #build the dynamic programmming array
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i-coin]+1)

    return dp[amount] if dp[amount] != float('inf') else -1

#testing the function
coins = [1,2,5]
amount = 11
result = min_coins(coins, amount)
print(f"Minimun number of coins to make {amount}: {result}")

#TASK2

def longest_common_sequences(s1, s2):
    """
    Finds the length of the longest common subsequence (LCS) of two strings using dynamic programming.

    Parameters:
    s1 (str): The first string.
    s2 (str): The second string.

    Returns:
    int: The length of the LCS of s1 and s2.
    """
    # Lengths of the input strings
    x, y = len(s1), len(s2)

    # Create two rows for dynamic programming
    prev = [0] * (y + 1)  # Previous row
    curr = [0] * (y + 1)  # Current row

    # Build the table using rolling rows
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if s1[i - 1] == s2[j - 1]:  # If the characters match
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])

        # Move to the next row and make the current row the previous row
        prev, curr = curr, prev

    # The length of the LCS is in the last row
    return prev[y]


# Testing the function
s1 = "abcde"
s2 = "ace"
result = longest_common_sequences(s1, s2)
print("The length of the LCS:", result)

#TASK3

def knapsack(weights, values, capacity):
    """\
        Solves the 0/1 knapsack problem using dynamic programming

        Parameters:
        weights(list of int) : the weights of the items
        values(list of int) : the values of the items
        capacity(int) : the maximum weight capacity of the knapsack

        Returns:
        int : the maximum value that can be achieved within the given capacity.
    """
    n = len(weights) #number of items

    #create a dp table with dimensions
    dp = [[0]*(capacity+1) for _ in range(n+1)]

    #build the dp table
    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if weights[i-1] <= w: #if item can fit in the knapsack
                dp[i][w] = max(dp[i-1][w], values[i-1]+dp[i-1][w-weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    #the maximun value is in dp[n][capacity]
    return dp[n][capacity]

#testing the function
weights = [1,3,4,5]
values = [1,4,5,7]
capacity = 7
result = knapsack(weights, values, capacity)
print(f"the maximum value that can be achieved is : {result}")