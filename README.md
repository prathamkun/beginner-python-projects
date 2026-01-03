# 1. 📧 Python Email Sender

A beginner-friendly Python project that sends emails using **Gmail SMTP**.
---

## 🔹 Features
* Send emails using Python
* Uses Gmail SMTP with SSL
* Tested using a temporary email

---

## 🔐 Setup (Important)

1. Enable **2-Step Verification** on your Gmail account
2. Go to **App Passwords**
3. Create an app password

   * App name: **Python**
4. Copy the generated password
5. Paste it in the code where it says:

```python
# WRITE YOUR PASS HERE
```

⚠️ Do **not** use your normal Gmail password.

---

## ▶️ Run

```bash
python 1emailsender.py
```

---

## 📸 Screenshot

**Email successfully received:**
<img width="1525" height="985" alt="image" src="https://github.com/user-attachments/assets/5d25e05b-0979-43bc-bf39-2d13c90822f9" />




---
# 2. 🔁 Word Replacement using Python

A simple beginner Python project that replaces a word in a sentence using user input.


## ✨ Features

Takes user input

Replaces a word in a sentence

Uses Python string replacement

Beginner-friendly logic

## ▶️ How to Run
```bash
python 2wordreplacement.py
```


## 🧠 Example
Original sentence:
Hello friends, i am pratham, hi hi hi

Enter the word to replace: hi
Enter the word replacement: hello

Output:
Hello friends, i am pratham, hello hello hello
---
# 3.🧮 Calculator using Python

A simple menu-driven calculator built using Python that performs basic arithmetic operations.

## ✨ Features

Addition

Subtraction

Multiplication

Division

Menu-driven program

Runs continuously until user exits

## ▶️ How to Run
```
python 3calculator.py
```

## 🧠 How It Works

User selects an operation from the menu

Enters two numbers

Result is displayed

Program repeats until Exit is chosen

## 📌 Example
A. Addition
B. Subtraction
C. Multiplication
---
# 4. 📧 Email Slicer (Python)

A simple Python program that splits an email address into username, domain, and extension.

## 🚀 How it works

Takes an email as input

Splits it using @ and .

Displays username, domain, and extension

## ▶ Example
Input: example@gmail.com
Username: example
Domain: gmail
Extension: com

## 🛠 Tech

Python 3

String operations

## 📌 Note

Enter a valid email format

Stop the program with Ctrl + C
D. Division
E. Exit
---
# 5.🔍 Binary Search Algorithm (Python)

A Python implementation of the Binary Search algorithm to efficiently find an element in a sorted list.

## 🚀 How it works

Repeatedly divides the list into halves

Compares the middle element with the target

Narrows the search range until the element is found or not present

## ▶ Example
List: [1,2,3,4,5,6,7,8,9,10,11,12,13]
Target: 12
Output: Index of target element

## 🛠 Tech

Python 3

Loops and conditional statements

## 📌 Notes

The list must be sorted

Returns the index of the element if found

Returns -1 if the element is not present

Prints each step to show how binary search works
---
# 6.🧠 Quiz Program (Python)

A simple Python quiz game that asks multiple-choice questions and calculates the final score and percentage.

## 🚀 How it works

Stores questions and answers in a dictionary

Takes user input for each question

Compares answers (case-insensitive)

Updates and displays the score after every question

## ▶ Example
What is the capital of France?
Answer? Paris
Correct
Your score is: 1

## 🛠 Tech Used

Python 3

Dictionaries

Loops and conditionals

## 📌 Features

Instant feedback (Correct / Wrong)

Final score and percentage display

Beginner-friendly logic
---
# 7.💰 Loan Interest Calculator (Python)

A simple Python program that calculates the monthly loan payment based on loan amount, annual interest rate, and loan duration.

## 🚀 How it works

Takes loan amount (principal)

Takes annual interest rate (APR)

Takes loan duration in years

Calculates and displays the monthly payment

## ▶ Example
Input the loan amount: 500000
Input the annual interest rates: 7.5
Input amount of years: 20
The monthly payment for this loan is: 4027.97

## 🛠 Tech Used

Python 3

Basic math operations

## 📌 Notes

Interest rate should be entered as a percentage

Output is rounded to 2 decimal places

Assumes fixed-rate loan
---
# 8.🔐 Random Password Generator (Python)

A simple Python program that generates a strong random password using letters, numbers, and special characters.

## 🚀 How it works

Asks the user whether to generate a password

Takes desired password length as input

Randomly selects characters and shuffles them

Displays the generated password

## ▶ Example
Do you want to generate a password? (Yes/No): Yes
How long would you like your password to be? 12
A9$kP2@Qm#8Z

## 🛠 Tech Used

Python 3

random module

string module

## 📌 Notes

Uses uppercase, lowercase, digits, and symbols

Password is randomized for better security

Type Yes or No when prompted
---
# 9.🎲 Dice Rolling Simulator (Python)

A simple Python program that simulates rolling two dice and displays their values using ASCII art.

## 🚀 How it works

Prompts the user to roll the dice

Generates two random numbers between 1 and 6

Displays the dice values and their visual representation

Continues rolling until the user chooses No

## ▶ Example
Roll the dice? (Yes/No): Yes
dice rolled: 4 and 6

## 🛠 Tech Used

Python 3

random module

Dictionaries and loops

## 📌 Notes

Input is case-insensitive (Yes, yes, YES)

Press Ctrl + C to exit anytime
---
# 10.🌐 Site Connectivity Checker (Python)

A simple Python program that checks whether a website is reachable by attempting a connection and displaying the HTTP response code.

## 🚀 How it works

Takes a website URL as input

Tries to connect using urllib.request

Displays a success message if the site is reachable

Shows the HTTP response status code

## ▶ Example
Input the url of the site you want to check: https://www.google.com
Checking connectivity
Connected to https://www.google.com successfully
The response code was: 200

## 🛠 Tech Used

Python 3

urllib.request

## 📌 Notes

Internet connection is required

HTTPS sites may raise SSL certificate errors if certificates are not installed

Press Ctrl + C to stop the program
---
# 11.💱 Currency Converter (USD to GBP) – Python

A simple Python program that converts US Dollars (USD) into British Pounds Sterling (GBP) using a fixed exchange rate.

## 🚀 How it works

Takes an amount in US dollars as input

Converts it to pounds using a predefined rate

Displays the converted amount

## ▶ Example
Enter amount in dollars: 100
That is 74.0 pounds.

## 🛠 Tech Used

Python 3

Functions and lambda expressions

## 📌 Notes

Uses a fixed exchange rate (1 USD = 0.74 GBP)

Exchange rate is based on 1st January and may change

Intended for learning purposes
---
# 12.📅 Leap Year Checker (Python)

A simple Python program that checks whether a given year is a leap year or not using standard leap year rules.

## 🚀 How it works

Takes a year as input

Applies leap year conditions:

Divisible by 4

Not divisible by 100 unless divisible by 400

Prints whether the year is a leap year

## ▶ Example
Input: 2028
Output: Leap Year

## 🛠 Tech Used

Python 3

Conditional statements

## 📌 Notes

Correctly follows the Gregorian calendar rules

Useful for beginner practice with if-else logic
---
# 13.📘 Word Dictionary (Python)

A simple Python program that works like a mini dictionary, displaying meanings of predefined words entered by the user.

## 🚀 How it works

Stores words and their meanings in a dictionary

Takes a word as user input

Displays the meaning if the word exists

Ends the program when the user presses Enter without typing a word

## ▶ Example
Enter a word: hi
hi : a way of greeting

## 🛠 Tech Used

Python 3

Dictionaries

Loops and conditionals

## 📌 Notes

Case-sensitive input

Only predefined words are supported

Designed for beginner practice
---
# 14.✊📄✂️ Rock Paper Scissors (Python)

A simple command-line Rock, Paper, Scissors game where the user plays against the computer and scores are tracked.

## 🚀 How it works

User chooses rock, paper, scissors, or exit

Computer randomly selects an option

Winner is decided based on game rules

Scores are updated and displayed

Game ends when the user types exit

## ▶ Example
Choose rock, paper, scissors or exit: rock
Your input is rock
Computer input is scissors
You Win!

## 🛠 Tech Used

Python 3

random module

Loops and conditional statements

## 📌 Features

Continuous gameplay

Score tracking for user and computer

Simple text-based interface

## ⚠️ Note

Input must be typed correctly (rock, paper, scissors, exit)

Designed for beginner practice
---
# 15.⏰📩 Automated SMS Sender (Python)

A Python program that automatically sends an SMS message at scheduled intervals using the Textbelt API.

## 🚀 How it works

Uses schedule to run tasks at fixed times or intervals

Sends an SMS using an HTTP POST request

Repeats automatically while the program is running

## ▶ Example
Message sent successfully
{'success': True, 'quotaRemaining': 0}

## 🛠 Tech Used

Python 3

requests module

schedule module

time module

Textbelt API

## 📌 Notes

Replace #yourphonenumberhere with a valid phone number

Free Textbelt API has limited quota

Program must keep running to send messages

Current setup sends a message every 10 seconds

## ⚠️ Important

Do not spam phone numbers

Use responsibly and for learning purposes
---
# 16.🖼️ Image Resizer (Python)

A simple Python program that resizes an image to user-defined dimensions using the Pillow (PIL) library.

## 🚀 How it works

Loads an image using PIL

Displays the original image size

Takes new width and height as input

Resizes the image

Saves the resized image with a new name

## ▶ Example
Enter Width: 400
Enter Length: 300
Current size: (1920, 1080)

## 🛠 Tech Used

Python 3

Pillow (PIL)

## 📌 Notes

Replace #yourimagenamehere with the actual image file name

Output image is saved as a .jpeg file

## Ensure Pillow is installed:
```

pip install pillow
```
---
# 17.📊 Graph Plotter (Python)

A simple Python program that plots two line graphs on the same chart using Matplotlib.

## 🚀 How it works

Defines X and Y values for two lines

Plots both lines on the same graph

Adds labels, title, and legend

Displays the graph window

## ▶ Example
Line 1: (2,4), (4,3), (5,6), (6,7)
Line 2: (1,1), (2,2), (3,3), (4,4)

## 🛠 Tech Used

Python 3

Matplotlib

## 📌 Notes

Requires matplotlib library:
```

pip install matplotlib
```


Useful for learning basic data visualization




