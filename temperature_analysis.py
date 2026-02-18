# Name: Parameswari Manthiramoorthi
# Roll Number: IITP_AIMLTN_2602771
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

ht = temperatures[0]   # Assume first number is highest
for i in temperatures:
    if ht < i:   # Compare  each elements 
        ht = i  # store highest elements
print(f"Highest Temperature: {ht}°C")   # Print highest number
lt = temperatures[0] # Assume first number is highest
for i in temperatures:
    if lt > i:          # Compare  each elements 
        lt = i           # store highest elements
print(f"Lowest Temperature: {lt}°C")  # Print highest number


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

count = 0
for i in temperatures:
  if i <= 30:
    continue
  count +=1

print(f"Hot Days (>30°C): {count}")


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]
day = 0
count = 0
for i in temperatures:
  day +=1 
  if i <= 30:
    continue   # skip non-hot days
  
  elif i >=40:
    break # stop immediately when alert occurs
  count +=1  # count hot days (>30°C) before alert
 
print(f"Hot Days Before Alert: {count}")
print(f"Alert! Extreme temperature 40°C detected on Day { day }")