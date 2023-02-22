def say_hello(user_name="anonymous", user_age=0):  # user_name 은 parameter 이라고 부른다
    print("hello", user_name, "you are", user_age, "old")


def sey_bye():
    print("bye")


def plus(a=0, b=0):
    print(a+b)


def tax_calc(money):
    return money*0.3


def pay_tax(tax):
    print("thx you for paying", tax)


def make_juice(fruit):
    return f"{fruit} + 1"


def add_ice(juice):
    return f"{juice} + 2"


def add_sugar(iced_juice):
    return f"{iced_juice} + 3"


say_hello("nico", 12)  # nico, lynn 은 argument 라고 부른다
say_hello()

plus(3, 5)

pay_tax(tax_calc(1500))

my_name = "nico"
my_age = 12
print(f"Hello I'm {my_name}, {my_age} year's old ")

juice = make_juice("apple")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)
print(perfect_juice)
