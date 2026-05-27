Notes for Roadmap of AI Engineer
-------------------------------------

THE GOLDEN RULE

You will ALWAYS learn topics in THIS order:

1. Watch concept
2. Take notes
3. Code manually
4. Break code
5. Fix code
6. Solve logic problems
7. Build mini project
8. Push to GitHub
9. Explain concept yourself

------------------------------------------


Day 1 Homework 

print("*" * 10) -> this is an expression. An expression is a piece of code that adds value. Python interpreter while running this code will evaluate the code that we put between the parenthesis, so it will evaluate our expression. Our expression will produce 10 asterisks which will be printed. 

Variables - store data temporarily in a computer's memory. 
Eg- 
1. price = 10
print(price)
->price is an identifier, an equal sign which is an operator, the 10 is the value. When this 10 will be stored in the memory first it will be  converted to it's binary representation (0 & 1s)

2. price = 10
price = 20
print(price) 
-> Since python interpreter executes the code line by line the result for price will be 20 in the output

3. birth_year = input("What is your birth year?  ")
age = 2026 - birth_year
print(age)
-> this will throw an error because wherever the input () is used it carries the value as string so everytime we need to convert it. we are subtracting 'str' from 'int', i.e., in age variable 2026 is subtracting string value ''. So, we need to convert this string value to integer in order to get the correct result. 

Converting string to other data types
int()
float()
bool()

4. weight_lbs = input("Weight: in Pounds")
weight_kgs = float(weight_lbs) * 0.45
print(weight_kgs)

5. 
course = 'Python for Beginners'
print(course[0])
print(course[-1])
print(course[-2])
- we can also use negative indexing in Python

--------------------------------
Day -1 exercises
-----------------------------
print("Prapti Sinha")
print("0----")
print("  | | | | ")
print("*" * 10)
price = 10
price = 20
print(price)

patient_name = "John Smith"
age = 20
is_new = True

name = input("What is your name?  ")
print("Hi " + name)
fav_color = input("What is your favorite color?  ")
print(name + " likes " + fav_color)

birth_year = input("What is your birth year?  ")
print(type(birth_year))
print(type(age))
age = 2026 - int(birth_year)
print(age)

course = "Python's Course for Beginners"
course = 'Python for "Beginners"'

course = '''
Hi John, 

Here is our first email to you.

Thank you, 
The support team
'''
course = 'Python for Beginners'
print(course[0])
print(course[-1])
print(course[-2])


course = 'Python for Beginners'
print(course[0:3])
course = 'Python for Beginners'
print(course[0:]) - Python for Beginners
print(course[1:]) - ython for Beginners
print(course[:5]) - Pytho
print(course[:]) - Python for Beginners
another = course[:]
print(another) - Python for Beginners

name = 'Jennifer'
print(name[1:-1]) - ennife

first = 'John'

last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(message) - John [Smith] is a coder
print(msg) - John [Smith] is a coder
---------------------------------------------------
27-05-26

Interview round by Senior Project Engineer 
ROUND 1 — PYTHON FUNDAMENTALS
QUESTION 1

What is a variable in Python?

Explain:

technically
like you are explaining to a 10-year-old

-> a reference/name pointing to a value stored in memory
name = "Prapti"
stores "Prapti" in memory
creates label name
points label to that memory

Excellent beginner understanding.
QUESTION 2

What is the difference between:

age = 22

and

age = "22"

Why does this difference matter?

QUESTION 3

Predict the output:

a = "2"
b = "3"

print(a + b)
-> 23, because strings concatenate.

AND:

a = 2
b = 3

print(a + b)
-> 5

Explain WHY both outputs are different.

QUESTION 4

What does this mean?

name = input("Enter name: ")

What datatype does input() return?
> str
Why is this VERY important?
-> input() ALWAYS returns string

QUESTION 5

Difference between:

=

and

==

Give real examples.
-> one is used as assignment operator other as comparison

QUESTION 6 — DEBUGGING THINKING

What error will this code give?

print(age)

if variable age was never created?

Why does this happen?

QUESTION 7 — ENGINEERING THINKING

What is the difference between:

Commit

and

Push

in Git/GitHub?

Explain like a software engineer.
-> SAVE GAME

Commit creates LOCAL snapshot.

Only on your laptop.

Example:

git commit -m "Added calculator program"

Git remembers project state.

UPLOAD SAVE TO CLOUD

Push uploads commits to GitHub website.

Example:

git push

Commit saves changes locally in Git history, while push uploads committed changes to remote repository like GitHub.

QUESTION 8 — LOGIC QUESTION

Write logic (no need perfect syntax):

Take 2 numbers from user and print:

addition
subtraction
multiplication

How would you think about solving this?
-> a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

add = a + b
sub = a - b
mul = a * b

print(add)
print(sub)
print(mul)

QUESTION 9 — SENIOR ENGINEER QUESTION

Why do I keep telling you to:

type code manually
intentionally break code
commit often

What engineering skill does that build?
-> Because engineers are paid to:

understand failure

not just success.

Breaking code builds:

debugging skill
error recognition
reasoning ability
confidence during failures

Typing manually builds:

muscle memory
syntax familiarity
logical sequencing

Committing often builds:

version control discipline
rollback ability
engineering workflow

QUESTION 10 — MINDSET QUESTION

Suppose tomorrow:

VS Code crashes
Git fails
Python gives errors everywhere

What should your mindset be as an engineer?

This question matters more than syntax.
->Errors are information, not attacks.

When systems fail:

investigate calmly
isolate issue
read error carefully
test assumptions
solve step by step

Weak engineers panic.

Strong engineers debug systematically.
--------------------------------------------------------------



