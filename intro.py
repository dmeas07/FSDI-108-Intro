# variables

name = "Daravy"
last_name = "Meas"
age = 33
price = 12.31
found = False

print(name)
print(last_name)

print(name + last_name)  # str concateneation
print(12 + 21)  # sum

# print(21 + name)

# math operands
print(21 * 21)

# if statements
if age < 100:
    print("Dont worry you are still young")
    print("Inside the if")
    print("Inside the if")
elif age == 100:
    print("congrats on the century")
else:
    print(" Sorry bud, you are getting old!")

print("outside the if")


def test():
    print("I'm a function")


def say_hello(name):
    print("Hello there, " + name)


def sum(num1, num2):
    return num1 + num2


test()  # call/execute function
test()
test()

say_hello("Bart")


result = sum(21, 22)
print("The result of the sum is:", + str(result))
