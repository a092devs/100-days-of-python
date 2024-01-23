# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
combined_name = name1 + name2
to_lower_case = combined_name.lower()
t = to_lower_case.count("t")
r = to_lower_case.count("r")
u = to_lower_case.count("u")
e = to_lower_case.count("e")
first_digit = t + r + u + e

l = to_lower_case.count("l")
o = to_lower_case.count("o")
v = to_lower_case.count("v")
e = to_lower_case.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
