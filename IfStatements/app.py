is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cool day")
    print("Wear warm cloth")
else:
    print("It's a lovey day")

print("Enjoy your day")

is_good_credit = True
house_value = 1000000

if is_good_credit:
    down_payment = house_value * (10/100)
else:
    down_payment = house_value * (20 / 100)

print(f"Down Payment Required: ${down_payment}")