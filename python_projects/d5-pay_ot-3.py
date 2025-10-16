# User inputs
hours = float(input("Enter hours worked this week: "))
wage = float(input("Enter hourly wage: "))

# Pay calculations
reg_pay = min(hours, 40) * wage
ot_hours = max(0, hours - 40)
ot_factor = 10 / 100 + 1  # Calculate overtime factor when 10% extra is owed
ot_pay = wage * ot_hours * ot_factor
adjusted_pay = reg_pay + ot_pay



# Conditional statement and print
if hours > 40:
    print(
        f"Your regular pay for this week is ${reg_pay:.2f}; however, you are also entitled to ${ot_pay:.2f} OT pay, which brings your total pay for this week to ${adjusted_pay:.2f}."
    )
else:
    print(
        f"Your total pay for this week is ${adjusted_pay:.2f}. You have ${ot_pay:.2f} OT pay this week."
    )
