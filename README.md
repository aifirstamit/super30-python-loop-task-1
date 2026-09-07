# Super30 Python Loop Task 1

## 📌 Overview

This repository contains my solutions for **Python Loop Task 1** from the Super30 learning journey.

The main objective of this task is to build strong fundamentals in **iteration and loops** using Python.

---

## 🎯 Learning Objectives

In this task, I practiced:

* `for` loops
* `range()`
* Conditional statements with loops
* Iterating through strings
* Iterating through lists
* Iterating through dictionaries
* Solving problems without built-in functions

---

## 📝 Tasks Covered

### 1. Print Numbers from 1 to 100

Print all numbers from `1` to `100` using a `for` loop.

**Sample Input:**

No input required.

**Sample Output:**

```text
1
2
3
...
100
```

---

### 2. Print Even Numbers

Print all even numbers between `1` and `100`.

**Sample Input:**

No input required.

**Sample Output:**

```text
2
4
6
8
10
...
100
```

---

### 3. Print Odd Numbers

Print all odd numbers between `1` and `100`.

**Sample Input:**

No input required.

**Sample Output:**

```text
1
3
5
7
9
...
99
```

---

### 4. Multiplication Table

Take an integer `n` as input and print its multiplication table from `1` to `20`.

**Sample Input:**

```text
5
```

**Sample Output:**

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
...
5 x 20 = 100
```

---

### 5. Sum of Numbers

Take an integer `n` as input and calculate the sum of numbers from `1` to `n` using a loop.

**Sample Input:**

```text
5
```

**Sample Output:**

```text
Sum: 15
```

**Explanation:**

```text
1 + 2 + 3 + 4 + 5 = 15
```

---

### 6. Factorial

Take an integer `n` as input and calculate its factorial without using a built-in factorial function.

**Sample Input:**

```text
5
```

**Sample Output:**

```text
Factorial: 120
```

**Explanation:**

```text
5 × 4 × 3 × 2 × 1 = 120
```

---

### 7. Numbers Divisible by 3

Given a list of numbers, print only the numbers that are divisible by `3`.

**Sample Input:**

```python
numbers = [10, 12, 15, 20, 21, 25, 30]
```

**Sample Output:**

```text
12
15
21
30
```

---

### 8. Language Name and Length

Given a list of programming languages, print each language along with its length.

**Sample Input:**

```python
languages = ["Python", "Java", "C++", "JavaScript"]
```

**Sample Output:**

```text
Python 6
Java 4
C++ 3
JavaScript 10
```

---

### 9. Iterate Through Dictionary

Given a student dictionary, iterate through it and print every key and value.

**Sample Input:**

```python
student = {
    "name": "Amit",
    "age": 22,
    "course": "Data Science"
}
```

**Sample Output:**

```text
name : Amit
age : 22
course : Data Science
```

---

### 10. Count Vowels

Take a string from the user and count the number of vowels using a `for` loop.

**Sample Input:**

```text
Python Programming
```

**Sample Output:**

```text
Number of vowels: 4
```

---

### 11. Reverse a String

Reverse a string using a `for` loop without using:

* `[::-1]`
* `reversed()`

**Sample Input:**

```text
Python
```

**Sample Output:**

```text
Reverse: nohtyP
```

---

### 12. Find Largest Number

Find the largest number from a list without using the built-in `max()` function.

**Sample Input:**

```python
numbers = [10, 25, 8, 40, 15]
```

**Sample Output:**

```text
Largest Number: 40
```

---

## 💡 Program Explanation

For each program, the Python file contains comments explaining the solution.

Each program is also supported with:

1. **Logic** → What are we trying to solve?
2. **Execution Flow** → What happens step-by-step?
3. **Input** → What data does the program receive?
4. **Output** → What does the program produce?
5. **Sample Input** → Example data used to run the program.
6. **Sample Output** → Expected result from the sample input.
7. **Test Case** → Example to verify the result.

---

## 📂 Project Structure

```text
super30-python-loop-task-1/

│
├── README.md
├── 01_print_1_to_100.py
├── 02_even_numbers.py
├── 03_odd_numbers.py
├── 04_multiplication_table.py
├── 05_sum_1_to_n.py
├── 06_factorial.py
├── 07_divisible_by_3.py
├── 08_language_lengths.py
├── 09_dictionary_iteration.py
├── 10_count_vowels.py
├── 11_reverse_string.py
└── 12_largest_number.py
```

---

## 💡 Key Concepts Learned

### `for` Loop

A `for` loop allows us to repeat an operation for each item in a sequence.

Example:

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

### `range()`

`range()` is commonly used with loops to generate a sequence of numbers.

```python
range(1, 101)
```

This generates numbers from `1` to `100`.

> The ending value is excluded.

---

## 📚 What I Learned

Through this task, I learned how to:

* Use `for` loops effectively
* Generate sequences using `range()`
* Combine loops with `if` conditions
* Iterate over different Python data structures
* Build counters and accumulators
* Track the largest value manually
* Process individual characters in a string
* Solve problems without relying on built-in functions
* Test programs using sample input and output

---

## 👨‍💻 Learning Journey

Part of my **AI** learning journey.

**YouTube Channel:** AI First

---

⭐ **Keep learning, keep building, and stay AI First! 🤖**