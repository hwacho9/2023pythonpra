a = 10
b = 15

if a == 10 and b == a:
    print("True")
else:
    print("False")

winner = 10

if winner > 10:
    print("Winner is greater than 10")
elif winner < 10:
    print("Winner is less than 10")
else:
    print("winner is 10")

age = int(input("How old are you?"))
print("user answer", age)

print(type(age))
if age < 18:
    print("NO DRINK")
elif age >= 18 and age <= 35:
    print("drink beer!")
elif age == 60 or age == 70:
    print("take care!")
else:
    print("DRINK SOJU!")

user_choice = int(input("Choose number."))
pc_choice = 50

if user_choice == pc_choice:
    print("You won!")
elif user_choice > pc_choice:
    print("Lower!")
elif user_choice < pc_choice:
    print("Higer!")

test
