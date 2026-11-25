units = float(input("Enter electricity units: "))
if units <= 100:
    bill = units * 1.5
else:
    if units <= 200:
        bill = 100 * 1.5 + (units - 100) * 2.5
    else:
        if units <= 300:
            bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
        else:
            bill = 100 * 1.5 + 100 * 2.5 + 100 * 4 + (units - 300) * 5
print("Electricity bill:", bill)
