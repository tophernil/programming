# 1: The brief
name = input("Enter your name? ").strip().title()
hourly_wage = input("Enter your hourly wage: ")
hours_worked = input("Enter hours worked this week: ")

earnings = float(hourly_wage) * float(hours_worked)

print(f"{name} earned ${earnings} this week.")

# 2: Bonus material
# Remove $ from user input (Use strip or replace)
# Specify number of figures (2) after the decimal point for earnings
name = input("Enter your name? ").strip().title()
hourly_wage = input("Enter your hourly wage: ").replace("$", "").strip()
hours_worked = input("Enter hours worked this week: ").replace('hours', '').strip()

earnings = float(hourly_wage) * float(hours_worked)
print(f"{name} earned ${earnings:.2f} this week.")
