################################################################################
"""
Recommended readings: 
  Chapter on dictionaries: https://automatetheboringstuff.com/3e/chapter7.html 
  Iterating through dictionaries: https://realpython.com/iterate-through-dictionary-python/
"""
################################################################################

"""
Exercise 4.1

Task:
------
Print the sum of the values in the dictionary.
"""

dct = {'a': 3, 'b': 7, 'c': -2, 'd': 10, 'e': 5}

print("Exercise 4.1")

print(sum(dct.values()))

print("---")

"""
Exercise 4.2

Task:
------
Print the key that has the largest value in dct.
"""

print("Exercise 4.2")

print(max(dct.keys()))

print("---")

"""
Exercise 4.3

Task:
------
Create a new dictionary with the squares of all the values in dct.
"""

print("Exercise 4.3")

print(dct)
dct_sqr = {}
for k, v in dct.items():
    dct_sqr[k] = v**2
    
print(dct_sqr)

print("---")

"""
Exercise 4.4

Task:
------
Print only the keys in dct whose values are even numbers.
"""

print("Exercise 4.4")

for k, v in dct.items():
    if v % 2 == 0:
        print(k)

print("---")

"""
Exercise 4.5

Task:
------
Create a new dictionary that swaps the keys and values in dct.
"""

print("Exercise 4.5")

dct_swap = {}
for k, v in dct.items():
    dct_swap[v] = k
print(dct_swap)

print("---")

"""
Exercise 4.6

Task:
------
Count the number of times each letter appears in the string 'ccctcctttttcc'
and print the resulting dictionary.
"""

s = 'ccctcctttttcc'

print("Exercise 4.6")

number_cs = 0
number_ts = 0

for letter in s:
    if letter == 'c':
        number_cs += 1
    else:
        number_ts += 1

print("the number of cs in the string is: " + str(number_cs))
print("the number of ts in the string is: " + str(number_ts))

print("---")

"""
Exercise 4.7

Task:
------
Given the dictionary of responses_mapping = {'j':'jazz', 'p':'pop'},
and the string responses = 'jjjpjjpppppjj',
print the list of corresponding words.
"""

responses_mapping = {'j':'jazz','p':'pop'}
responses = 'jjjpjjpppppjj'            

print("Exercise 4.7")

for letter in responses:
    for k, v in responses_mapping.items():
        if letter == k:
            print(v)

print("---")

"""
Exercise 4.8

Task:
------
Merge the following two dictionaries into one:
{'a': 1, 'b': 2} and {'c': 3, 'd': 4}
"""

print("Exercise 4.8")

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict3 = {**dict1, **dict2}
print(dict3)

print("---")

"""
Exercise 4.9

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose keys are sorted alphabetically.
"""

print("Exercise 4.9")

dict4 = {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9}

print(dict(sorted(dict4.items())))

print("---")

"""
Exercise 4.10

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose values appear in increasing order.
"""

print("Exercise 4.10")

print(dict(sorted(dict4.items(), key = lambda item: item[1])))

print("---")