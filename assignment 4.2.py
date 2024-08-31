# task 1 sorting the givenm grades
# task 2 calculating given grades
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# Sort the grades in descending order
sorted_grades = sorted(grades, reverse=True)

# Print the sorted list
print("Sorted grades in descending order:", sorted_grades)


grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# Calculate the average grade
average_grade = sum(grades) / len(grades)

# Print the average grade
print("Average grade:", average_grade)

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# Task 1: Sort the grades in descending order
sorted_grades = sorted(grades, reverse=True)
print("Sorted grades in descending order:", sorted_grades)

# Task 2: Calculate the average grade
average_grade = sum(grades) / len(grades)
print("Average grade:", average_grade)



# 2) from the given list find out if alice submitted assignment and attended class 
# hint is given in a form of a keyword , 
# check if alice attended class and submitted assignment in one sattement
# using 'in' to check if 'Alice" attended class 
# using and for combined sentence to find out in one sentence


submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Check if Alice both submitted the assignment and attended the class
if "Alice" in submitted and "Alice" in attended:
    print("Alice has both submitted the assignment and attended the class.")
else:
    print("Alice has not both submitted the assignment and attended the class.")


# final assigment extract specific data from given numbers
# extract  temps the second week 'index 7 to index 14'
# extract all temperatures at the end from above
# if temps exceed 100 add to a new list or use slicing method

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Extract temperatures for the second week (index 7 to index 14)
second_week_temperatures = temperatures[7:14]

# Print the result
print("Temperatures for the second week:", second_week_temperatures)


#  task 2 above 100

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Extract temperatures above 100 using list comprehension
temperatures_above_100 = [temp for temp in temperatures if temp > 100]

# Print the result
print("Temperatures above 100:", temperatures_above_100)