WEEK 1 TASK

1. Python Variables (Theory)
What is a Variable?

A variable is a named memory location used to store data.

Instead of remembering raw values like 25 or "Saurav", we store them in variables so the program can reuse and manipulate them.

Think of it like:

Variable = Label on a box
Value = Content inside the box

Key Characteristics of Python Variables

No need to declare data type explicitly (Python is dynamically typed)

Created when you assign a value

Case-sensitive (age ≠ Age)

Syntax
age = 25
name = "Saurav"
temperature = 36.5
Rules for Naming Variables

Must start with a letter or underscore

Cannot start with a number (1age)

No spaces (user name)

Use meaningful names (not x1, a2 unless necessary)

2. Data Types (Theory)

Data types define what kind of data a variable holds and what operations can be performed on it.

Main Python Data Types (Beginner Level)
Data Type	Description	Example
int	Integer numbers	10, -5
float	Decimal numbers	3.14
str	Text/String	"Hello"
bool	True/False values	True, False
Example Code
a = 10        # int
b = 3.14      # float
name = "John" # string
is_active = True  # boolean

print(type(a))
print(type(name))

Output:

<class 'int'>
<class 'str'>
3. Operators (Theory)

Operators are symbols used to perform operations on variables and values.

(A) Arithmetic Operators

Used for mathematical calculations.

Operator	Meaning
+	Addition
-	Subtraction
*	Multiplication
/	Division
%	Modulus (remainder)
//	Floor Division
**	Power
Example
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.33
print(a % b)   # 1 (remainder)
print(a ** 2)  # 100 (power)
(B) Comparison Operators

Used in decision-making (if-else).

x = 10
y = 20

print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
(C) Logical Operators

Used to combine conditions.

a = 10
print(a > 5 and a < 20)  # True
print(a > 15 or a < 20)  # True
print(not(a > 5))        # False
4. Input and Output (Theory)
Input

Used to take data from the user during runtime.

name = input("Enter your name: ")
print(name)

Important:
input() always returns a string by default.

So if you need numbers:

age = int(input("Enter age: "))
Output

Used to display results using print().

print("Hello World")
print("Age:", age)
5. Conditional Statements (if-else) – Theory

Conditional statements are used for decision making.

Real life analogy:

If it rains → take umbrella
Else → go normally

Syntax Structure
if condition:
    # code
elif condition:
    # code
else:
    # code
Example: Even or Odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
6. Loops (Theory)

Loops are used to repeat tasks automatically instead of writing the same code multiple times.

Two main types:

for loop (fixed iterations)

while loop (condition-based)

(A) For Loop

Used when you know how many times to repeat.

Syntax
for variable in range(start, stop, step):
    # code
Example
for i in range(1, 6):
    print(i)

Output:

1 2 3 4 5


(B) While Loop

Used when repetition depends on a condition.

Syntax
while condition:
    # code
Example
i = 1
while i <= 5:
    print(i)
    i += 1


7. Hands-On Programs 
(1) Temperature Converter (Celsius to Fahrenheit)
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)
(2) Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
8. Client Project: Basic Data Processing Script (Average Temperature)


Example: Average Temperature Calculator
total = 0
days = int(input("Enter number of days: "))

for i in range(days):
    temp = float(input(f"Enter temperature for day {i+1}: "))
    total += temp

average = total / days
print("Average Temperature:", average)

What concepts used here:

Variables

Data types (float, int)

Input/Output

Loop (for)

Operators

9. Summary (What You Actually Learned This Week)

How Python stores data (Variables)

Types of data (Data Types)

Mathematical & logical operations (Operators)

Taking user input & showing output

Decision making (if-else)

Repetition logic (for & while loops)

Writing real mini programs like a data analyst

WEEK 2 TASK

1. Python Lists (Theory)
What is a List?

A list is an ordered, mutable collection of elements.

Key properties:

Ordered (index-based)

Mutable (can be changed)

Allows duplicate values

Can store multiple data types

Real-life analogy:

List = Shopping cart (you can add, remove, reorder items anytime)

Syntax
my_list = [10, 20, 30, 40]
Important Operations
numbers = [10, 20, 30, 40]

# Access
print(numbers[0])   # 10

# Modify
numbers[1] = 25

# Add element
numbers.append(50)

# Remove element
numbers.remove(30)

print(numbers)

Output:

[10, 25, 40, 50]
2. Tuples (Theory)
What is a Tuple?

A tuple is an ordered, immutable collection.

Key properties:

Ordered

Immutable (cannot be modified)

Faster than lists

Used for fixed data

Real-life analogy:

Tuple = Aadhaar number (fixed, not meant to change)

Syntax
my_tuple = (1, 2, 3, 4)
Example
coordinates = (10, 20)

print(coordinates[0])  # 10

# coordinates[0] = 50 (Error: immutable)

When data should not change (config, coordinates, constants)

3. Dictionaries (Theory)
What is a Dictionary?

A dictionary stores data in key-value pairs.

Structure:

{key: value}

Key properties:

Unordered (in logic)

Mutable

Fast lookup using keys

Keys must be unique

Real-life analogy:

Dictionary = Contact list (Name → Phone Number)

Syntax
student = {
    "name": "Saurav",
    "age": 25,
    "course": "MCA"
}
Example
student = {"name": "Rahul", "marks": 85}

# Access value
print(student["name"])

# Add new key
student["city"] = "Delhi"

# Update value
student["marks"] = 90

print(student)
4. Sets (Theory)
What is a Set?

A set is an unordered collection of unique elements.

Key properties:

No duplicates allowed

Unordered

Mutable

Very useful in data cleaning

Real-life analogy:

Set = Unique student ID list (no repetition allowed)

Syntax
my_set = {1, 2, 3, 3, 4}
print(my_set)

Output:

{1, 2, 3, 4}
Example Operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))        # {1,2,3,4,5}
print(a.intersection(b)) # {3}
5. Functions (Theory)
What is a Function?

A function is a reusable block of code designed to perform a specific task.

Why functions matter (seriously):

Avoid repetition

Improve readability

Modular coding (industry standard)

Essential for data pipelines & ML workflows

Syntax
def function_name(parameters):
    return result
Example
def greet(name):
    return "Hello " + name

print(greet("Saurav"))
6. Lambda Functions (Theory)
What is a Lambda Function?

A lambda function is a small anonymous function written in one line.

Used when:

Function is simple

Needed temporarily

Used in data processing (map, filter, etc.)

Syntax:

lambda arguments: expression
Example
square = lambda x: x * x
print(square(5))  # 25

With list:

numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)
7. Recursion (Theory)
What is Recursion?

Recursion is when a function calls itself to solve a problem.

Critical condition:

Must have a base case (stopping condition)
Otherwise → infinite recursion crash.

Real-life analogy:

Mirror facing mirror (repeats until stop condition)

Example: Factorial
def factorial(n):
    if n == 1:  # Base case
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # 120

Recursion is elegant but not always efficient. For large data, loops are often better.

8. List Comprehension (Theory)
What is List Comprehension?

A compact way to create lists using a single line of code.

Normal method:

squares = []
for i in range(5):
    squares.append(i*i)

List comprehension:

squares = [i*i for i in range(5)]
print(squares)

Advantages:

Shorter code

Faster execution

Cleaner logic (used heavily in data science)

With condition:

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)
9. Hands-On: Data Transformation Functions
(1) Sum of Squares
def sum_of_squares(numbers):
    return sum([x**2 for x in numbers])

data = [1, 2, 3, 4]
print(sum_of_squares(data))
(2) Filtering Data (Important for Data Science)
def filter_even(numbers):
    return [x for x in numbers if x % 2 == 0]

data = [1, 2, 3, 4, 5, 6]
print(filter_even(data))
10. Client Project: Data Cleaning Script (Realistic)

Objective:

Remove duplicates

Filter invalid data

Clean dataset

Example Script
def clean_data(data):
    # Remove duplicates using set
    unique_data = list(set(data))
    
    # Filter only positive values
    filtered_data = [x for x in unique_data if x > 0]
    
    return filtered_data

# Sample raw data (messy dataset)
raw_data = [10, -5, 20, 20, 30, -2, 40, 10, 50]

cleaned = clean_data(raw_data)

print("Raw Data:", raw_data)
print("Cleaned Data:", cleaned)
11. Advanced Data Cleaning (More Realistic Version)
def clean_temperature_data(data):
    # Remove None values
    data = [x for x in data if x is not None]
    
    # Remove duplicates
    data = list(set(data))
    
    # Filter unrealistic temperatures
    data = [x for x in data if -50 <= x <= 60]
    
    return sorted(data)

temps = [30, 32, None, 45, 200, 32, -60, 28, 30]
print(clean_temperature_data(temps))
12. Summary (What You Actually Learned in Week 2)

Lists → Flexible data storage

Tuples → Fixed data

Dictionaries → Key-value structured data

Sets → Remove duplicates (critical for data cleaning)

Functions → Reusable logic blocks

Lambda → Short one-line functions

Recursion → Self-calling logic

List Comprehension → Efficient data processing

WEEK 3 TASK

1. NumPy Arrays (Theory)
What is NumPy?

NumPy (Numerical Python) is a library used for:

Fast numerical computations

Multi-dimensional arrays

Mathematical operations on large datasets

Why not just use Python lists?
Because:

Lists are slow

Lists use more memory

Lists don’t support vectorized operations

NumPy arrays are:

Faster

Memory efficient

Optimized for mathematical operations

NumPy Array vs Python List (Conceptual Difference)
Feature	Python List	NumPy Array
Speed	Slow	Very Fast
Memory	High usage	Efficient
Math Operations	Limited	Vectorized
Data Type	Mixed allowed	Mostly homogeneous
Creating NumPy Arrays
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

2D Array:

import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(matrix)
2. NumPy Operations (Theory)

NumPy allows vectorized operations, meaning operations on entire arrays at once instead of loops.

This is critical for performance.

Arithmetic Operations
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)  # Element-wise addition
print(a * b)  # Element-wise multiplication
print(a ** 2) # Square of each element
Statistical Operations (Very Important for Data Analysis)
import numpy as np

data = np.array([10, 20, 30, 40, 50])

print(np.mean(data))  # Average
print(np.sum(data))   # Sum
print(np.max(data))   # Maximum
print(np.min(data))   # Minimum
print(np.std(data))   # Standard deviation
3. Broadcasting (Theory)
What is Broadcasting?

Broadcasting is NumPy’s ability to perform operations on arrays of different shapes automatically.

Instead of manually looping, NumPy “stretches” smaller arrays to match larger ones.

Real-life analogy:

One teacher giving marks to an entire class at once instead of one by one.

Example
import numpy as np

arr = np.array([1, 2, 3])
result = arr + 10  # Broadcasting
print(result)

Output:

[11 12 13]

2D Broadcasting:

import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print(matrix + 5)

Key Rule:
Broadcasting works when shapes are compatible.

4. Pandas (Theory)
What is Pandas?

Pandas is a Python library used for:

Data manipulation

Data analysis

Data cleaning

Handling datasets (CSV, Excel, etc.)

Core Data Structures:

Series (1D)

DataFrame (2D table)

Think:

NumPy = Engine
Pandas = Smart Data Manager

5. Pandas Series (Theory)
What is a Series?

A Series is a one-dimensional labeled array.

Example:

import pandas as pd

data = pd.Series([10, 20, 30, 40])
print(data)

With index labels:

import pandas as pd

data = pd.Series([100, 200, 300], index=["A", "B", "C"])
print(data)

Accessing values:

print(data["A"])
6. Pandas DataFrame (Theory)
What is a DataFrame?

A DataFrame is a 2D table-like structure (rows and columns), similar to Excel sheet or database table.

Why it’s powerful:

Handles large datasets

Supports missing values

Easy filtering, grouping, aggregation

Creating a DataFrame
import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Raj"],
    "Age": [22, 25, 23],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)
print(df)
7. Indexing in Pandas (Theory)

Indexing means selecting specific data from dataset.

Column Selection
print(df["Name"])
Row Selection using loc (label-based)
print(df.loc[0])
Row Selection using iloc (position-based)
print(df.iloc[1])

Filtering data:

print(df[df["Marks"] > 85])
8. Data Grouping (Theory)
What is Grouping?

Grouping means splitting data into categories and applying operations like:

Sum

Mean

Count

Max/Min

Used heavily in:

Business analytics

Data science

Dashboards

Example
import pandas as pd

data = {
    "Department": ["IT", "HR", "IT", "HR", "Finance"],
    "Salary": [50000, 40000, 60000, 45000, 70000]
}

df = pd.DataFrame(data)

grouped = df.groupby("Department")["Salary"].mean()
print(grouped)
9. Hands-On: NumPy Operations (Practical)
import numpy as np

# Create array
arr = np.array([10, 20, 30, 40])

# Basic operations
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Squared:", arr ** 2)
print("Add 5 (Broadcasting):", arr + 5)
10. Hands-On: Dataset Manipulation with Pandas
import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Raj", "Aman"],
    "Age": [22, None, 23, 22],
    "Marks": [85, 90, None, 85]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nCleaned Dataset:")
print(df)
11. Client Project: Data Cleaning & Aggregation Script (Industry-Type)

Objective:

Remove missing values

Calculate averages

Aggregate dataset

import pandas as pd

# Sample dataset
data = {
    "City": ["Delhi", "Mumbai", "Delhi", "Chennai", "Mumbai", None],
    "Temperature": [35, 32, None, 30, 32, 28],
    "Humidity": [60, 70, 65, None, 70, 75]
}

df = pd.DataFrame(data)

print("Raw Data:")
print(df)

# Step 1: Remove rows with missing City
df = df.dropna(subset=["City"])

# Step 2: Fill missing numerical values with average
df["Temperature"] = df["Temperature"].fillna(df["Temperature"].mean())
df["Humidity"] = df["Humidity"].fillna(df["Humidity"].mean())

# Step 3: Group by City and calculate average
result = df.groupby("City").mean(numeric_only=True)

print("\nCleaned & Aggregated Data:")
print(result)
12. Summary (What You Actually Learned in Week 3)

NumPy arrays for fast numerical computation

Vectorized operations (no loops needed)

Broadcasting for efficient calculations

Pandas Series (1D data)

Pandas DataFrame (2D structured dataset)

Indexing and filtering datasets

Data cleaning (missing values, duplicates)

Data aggregation using groupby()

WEEK 4 TASK
1. Data Visualization (Core Theory)
What is Data Visualization?

Data visualization is the process of converting raw data into graphs, charts, and plots to:

Identify patterns

Detect trends

Find outliers

Communicate insights clearly

Real-world analogy:

Raw dataset = Excel sheet full of numbers
Visualization = Story that explains those numbers instantly

Example:
A table of 10,000 rows → confusing
A graph → instant understanding

2. Matplotlib (Theory)
What is Matplotlib?

Matplotlib is a Python library used for:

Basic plotting

Custom graphs

Full control over visualization

It is the foundation library.
Seaborn is built on top of Matplotlib.

Key Features:

Highly customizable

Works with NumPy & Pandas

Industry standard for basic plots

3. Basic Plots in Matplotlib (Theory + Code)

First import:

import matplotlib.pyplot as plt
(A) Line Plot (Trend Analysis)
Theory

Used to show trends over time or sequence data.

Example use cases:

Stock prices over time

Temperature trends

Sales growth

Code
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y)
plt.title("Line Plot Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
(B) Bar Plot (Category Comparison)
Theory

Used to compare values across categories.

Example:

Sales by product

Marks by students

Revenue by department

Code
import matplotlib.pyplot as plt

categories = ["A", "B", "C", "D"]
values = [50, 70, 40, 90]

plt.bar(categories, values)
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
(C) Histogram (Data Distribution)
Theory

Shows frequency distribution of numerical data.

Critical for:

Outlier detection

Understanding spread of data

Normal distribution analysis

Code
import matplotlib.pyplot as plt

data = [10, 12, 15, 20, 22, 22, 25, 30, 35]

plt.hist(data, bins=5)
plt.title("Histogram Example")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()
(D) Scatter Plot (Relationship Between Variables)
Theory

Used to identify correlation between two variables.

Example:

Study hours vs marks

Ad spend vs sales

Temperature vs humidity

Code
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 6]

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X Variable")
plt.ylabel("Y Variable")
plt.show()
4. Seaborn (Advanced Visualization) – Theory
What is Seaborn?

Seaborn is a high-level visualization library built on Matplotlib.

Why Seaborn is preferred in Data Science:

Better aesthetics (professional plots)

Built-in statistical graphs

Works directly with Pandas DataFrames

Faster analysis of relationships

Blunt truth:
Matplotlib = Control
Seaborn = Speed + Beauty + Statistical insights

5. Seaborn Advanced Plots (Theory + Code)

First import:

import seaborn as sns
import matplotlib.pyplot as plt
(A) Heatmap (Correlation Analysis)
Theory

A heatmap shows correlation between multiple variables using color intensity.

Used in:

Feature selection (ML)

Data analysis dashboards

Pattern detection

Code
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Math": [90, 85, 78, 92, 88],
    "Science": [85, 80, 75, 95, 90],
    "English": [88, 82, 70, 90, 85]
}

df = pd.DataFrame(data)

correlation = df.corr()

sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
(B) Pairplot (Feature Relationships)
Theory

Pairplot shows relationships between multiple numerical variables simultaneously.

Very useful for:

Exploratory Data Analysis (EDA)

Detecting trends & clusters

Understanding dataset structure

Code
import seaborn as sns
import pandas as pd

data = {
    "Age": [22, 25, 30, 35, 28],
    "Salary": [30000, 40000, 50000, 60000, 45000],
    "Experience": [1, 3, 5, 7, 4]
}

df = pd.DataFrame(data)

sns.pairplot(df)
plt.show()
(C) Box Plot (Outlier Detection)
Theory

Shows:

Median

Quartiles

Outliers

Used heavily in real data cleaning.

Code
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Scores": [50, 55, 60, 62, 65, 70, 200]  # 200 is outlier
}

df = pd.DataFrame(data)

sns.boxplot(x=df["Scores"])
plt.title("Box Plot for Outlier Detection")
plt.show()
6. Hands-On: Visualization for Dataset Analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7],
    "Marks": [40, 50, 55, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

# Scatter plot
plt.scatter(df["Hours_Studied"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.show()
7. Client Project: Mini Visualization Dashboard (Industry-Style)

Objective:

Histogram (distribution)

Scatter plot (relationship)

Heatmap (correlation)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
data = {
    "Age": [22, 25, 30, 35, 40, 28, 32],
    "Salary": [30000, 40000, 50000, 60000, 65000, 45000, 52000],
    "Experience": [1, 3, 5, 8, 10, 4, 6]
}

df = pd.DataFrame(data)

# Histogram
plt.figure(figsize=(12,4))
plt.subplot(1,3,1)
plt.hist(df["Salary"], bins=5)
plt.title("Salary Distribution")

# Scatter Plot
plt.subplot(1,3,2)
plt.scatter(df["Experience"], df["Salary"])
plt.title("Experience vs Salary")

# Heatmap
plt.subplot(1,3,3)
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()
8. What You Must Submit (Google Classroom)

Your submission should include:

Python script (.py or .ipynb)

At least 3 plots:

Histogram

Scatter plot

Heatmap or Pairplot

Short summary of concepts learned

9. Summary (What You Actually Learned in Week 4)

Matplotlib for basic plots (line, bar, histogram, scatter)

Seaborn for advanced statistical visualization

Heatmaps for correlation analysis

Pairplots for multi-feature relationship analysis
