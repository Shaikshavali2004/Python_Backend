# 6. Writeaprogramtotakeasingledigitnumberfromthekeyboardandprint in english?

digit = input("Enter a single digit number (0-9): ")

digits_in_english = [
    "zero", "one", "two", "three", "four",
    "five", "six", "seven", "eight", "nine"
]

if digit.isdigit() and 0 <= int(digit) <= 9:
    print("The digits in English:", digits_in_english[int(digit)])
else:
    print("Please enter a valid single digit number (0-9).")