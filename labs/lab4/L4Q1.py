#1. Email to Dictionary Function
#This Python function reads a file where each line is an email address.  
# #It processes each email to separate the username from the domain 
# #name and stores them in a dictionary as key-value pairs. 

def emailDomain(fileName):
  """
  Reads a file containing email addresses and returns a dictionary with
  usernames as keys and domains as values.

  Args:
    fileName: The name of the file to read.

  Returns:
    A dictionary mapping usernames to email domains.
  """
  email_dict = {}
  try:
    with open(fileName, 'r') as file:
      for line in file:
        # Remove any leading/trailing whitespace (like \n)
        clean_line = line.strip()
        if '@' in clean_line:
          # Split the email into username and domain 
          username, domain = clean_line.split('@')
          email_dict[username] = domain
  except FileNotFoundError:
    print(f"Error: The file '{fileName}' was not found.")
  
  return email_dict

# Example Usage:
# Assume a file 'emails.txt' with the content from the question.
# To create the file for testing:
# with open('emails.txt', 'w') as f:
#     f.write('ramin.soltanzr@gmail.com\n')
#     f.write('reza.gholi@hotmail.com\n')
#     f.write('abol.fazl@yahoo.com\n')
#     f.write('ahmad.teacher@icm.com\n')

# result = emailDomain('emails.txt')
# print(result)

# Output:
#{'ramin.soltanzr': 'gmail.com', 'reza.gholi': 'hotmail.com', 'abol.fazl': 'yahoo.com', 'ahmad.teacher': 'icm.com'}

#2. Find Maximum Power in Equation
#This program asks a user to input a mathematical equation as a string and finds
# the highest power a variable is raised to.  It works by searching for 
# the ** operator and then checks the following character to find the power.  
# The program assumes powers are single digits from 1 to 9. 
def find_max_power():
  """
  Finds the maximum power of a variable in a mathematical equation string.
  """
  # Get input string from the user
  equation = input("Enter a mathematical equation: ")
  
  max_power = 0
  
  # Iterate through the string to find the '**' operator
  for i in range(len(equation) - 2):
    if equation[i:i+2] == '**':
      power_char = equation[i+2]
      # Check if the character is a digit and update max_power
      if power_char.isdigit():
        power = int(power_char)
        if power > max_power:
          max_power = power
          
  print(f"The maximum power found in the equation is: {max_power}")

# Example Usage:
# find_max_power()
# Example Interaction 1:

# Enter a mathematical equation: 3*x**8+6+4*(x**9)-y**3
# The maximum power found in the equation is: 9
# Example Interaction 2:

# Enter a mathematical equation: x*2+y**8-12*2**7-3*x**6
# The maximum power found in the equation is: 8

# 3. Plotting Mathematical Functions 📈
# This program uses the matplotlib and numpy libraries to 
# reproduce a figure containing three subplots.  
# The plots for y=sin(10πt), y=e^−t and their product 
# are graphed over a time period of 0 to 10 seconds. 
import matplotlib.pyplot as plt
import numpy as np

def plot_functions():
  """
  Generates and displays a figure with three subplots of mathematical functions.
  """
  # Create 10000 points from 0 to 10 seconds 
  t = np.linspace(0, 10, 10000)
  
  # Calculate the y-values for each function
  y1 = np.sin(10 * np.pi * t)
  y2 = np.exp(-t)
  y3 = y1 * y2
  
  # Create a figure and a set of subplots
  plt.figure(figsize=(8, 6))
  
  # --- First Subplot ---
  plt.subplot(3, 1, 1)
  plt.plot(t, y1)
  plt.ylabel("Amplitude") # 
  plt.text(10.1, 0, r'Sin(10$\pi$*t)', va='center', fontsize=12) # Add text annotation
  
  # --- Second Subplot ---
  plt.subplot(3, 1, 2)
  plt.plot(t, y2)
  plt.ylabel("Amplitude") # 
  plt.text(10.1, 0.1, r'e$^{-x}$', va='center', fontsize=12) # Add text annotation
  
  # --- Third Subplot ---
  plt.subplot(3, 1, 3)
  plt.plot(t, y3)
  plt.xlabel("Time") # 
  plt.ylabel("Amplitude") # 
  plt.text(10.1, 0, r'Sin(10$\pi$*t)*e$^{-x}$', va='center', fontsize=12) # Add text annotation
  
  # Adjust layout and display the plot
  plt.tight_layout(rect=[0, 0, 0.9, 1]) # Adjust for text
  plt.show()

# To run the code:
# plot_functions()



# 4. Count Passing Students
# This code snippet reads a file named grades.txt. Each line in the file 
# is expected to contain a student's username followed by three test scores.  
# The program counts and prints the number of students who passed all three 
# tests, with a passing score defined as 70 or higher. 

def count_passing_students(fileName='grades.txt'):
  """
  Scans a file with student grades and counts how many passed all tests.

  Args:
    fileName: The name of the file containing student grades.
  """
  passed_count = 0
  passing_score = 70 # 

  try:
    with open(fileName, 'r') as file:
      for line in file:
        parts = line.split()
        # Ensure the line has a name and at least three scores
        if len(parts) >= 4:
          try:
            # Get the three scores 
            score1 = int(parts[1])
            score2 = int(parts[2])
            score3 = int(parts[3])
            
            # Check if the student passed all three tests 
            if score1 >= passing_score and score2 >= passing_score and score3 >= passing_score:
              passed_count += 1
          except ValueError:
            # This line doesn't contain valid scores, so we skip it.
            print(f"Warning: Skipping malformed line: {line.strip()}")

    print(f"Number of students who passed all three tests: {passed_count}")

  except FileNotFoundError:
    print(f"Error: The file '{fileName}' was not found.")

# Example Usage:
# To create a sample 'grades.txt' file for testing:
# with open('grades.txt', 'w') as f:
#     f.write('GWashington 83 77 54\n')
#     f.write('JAdams 86 69 90\n')
#     f.write('TJefferson 92 88 95\n')
#     f.write('JMadison 75 71 80\n')

# count_passing_students()

Example Output (with sample file):
# Number of students who passed all three tests: 2

