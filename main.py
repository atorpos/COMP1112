# This is a sample Python script.
from math import log


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def testing(teststuff):
    print(f'Holy crow {teststuff}')

def secondstest(*whatisthat):
    print("the length is " + whatisthat[2])

def thirdtest(food):
    for x in food:
        print(x)

def forthtext(x):
    return log(x)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
thisdixt = {
    "brand": "ford",
    "model": "F150",
    "year" : "2020"
}
print(thisdixt["year"])

print(len(thisdixt))

testing('oh my oh my')
fruit = ['appple', 'orange', 'banana']
thirdtest(fruit)
lognumber = forthtext(10)
print(lognumber)

# print "Hello World"[::-1]
print(fruit.re)
# del fruit[1:2]
test_6= 'testing'
# thirdtest(fruit)
print(5 + 2 * 3)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
