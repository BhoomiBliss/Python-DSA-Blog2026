# --- SECTION 1: HELLO WORLD & SYNTAX ---
#Basic print statement
print("Hello, World!")

#Multi-line statements using separation (though rarely used)
print("Python"); print("is"); print("fun!")

# --- SECTION 2: COMMENTS ---
#This is a single-line comment
"""
4. This is a multiline string
used as a comment.
"""

# --- SECTION 3: VARIABLES ---
#Assigning a string
a = "Hello, World!"

#Assigning an integer
x = 5

#Re-assigning a variable to a different type (Dynamic Typing)
y = 4       # y is an int
y = "Sally" # y is now a str

#Case Sensitivity test
b = 4
B = "Sally" # B does not overwrite b

# --- SECTION 4: DATA TYPES & INSPECTION ---
#Checking types using type()
print(type(5))
print(type("John"))
print(type(3.14))

# --- SECTION 5: STRING OPERATIONS (As requested) ---
#Getting string length
print(len(a))

#Accessing string character by index
print(a[1])

#For loop through a string literal
for x in "Hello, World!":
    print(x)

#For loop through a variable using range and length
for x in range(len(a)):
    print(a[x], end=" ")
print() # For newline

# --- SECTION 6: NUMBERS ---
#Integer
num1 = 10
#Float
num2 = 20.5
#Math inside print
print(3 + 3)
#Mixing text and numbers with a comma
print("Result is:", 35)

# --- SECTION 7: CASTING (Detailed Examples) ---
#Casting to Integer (truncates floats)
val1 = int(3.8) # Results in 3
print(val1)

#Casting String to Integer
val2 = int("10")
print(val2)

#Casting to Float
val3 = float(3) # Results in 3.0
print(val3)

#Casting to String
val4 = str(3) # Results in '3'
print(val4)

# --- SECTION 8: INDENTATION EXAMPLE ---
# Correct indentation block
if 5 > 2:
    print("Five is greater than two!")