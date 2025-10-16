# User inputs
hours = float(input("Enter hours worked this week: "))
wage = float(input("Enter hourly wage: "))

# Regular pay calc
reg_pay = hours * wage

# Adjusted pay calc
max_reg_pay = 40 * wage
ot_hours = hours - 40
ot_factor = 10 / 100 + 1  # 1.10
ot_pay = wage * ot_hours * ot_factor
adjusted_pay = max_reg_pay + ot_pay

if hours > 40:
    print(
        f"Your regular pay for this week is ${max_reg_pay:.2f}. You are also entitled to OT pay of ${ot_pay:.2f} for a total pay of ${adjusted_pay:.2f}."
    )
else:
    print(
        f"Your regular pay for this week is ${reg_pay:.2f}. You do not have any OT pay this week."
    )
