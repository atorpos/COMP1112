#Student Name: Sun Fai Oskar Wong
#Student Number: 200561852
#Course Number: COMP1112-23F-13374
#assignment 1


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def print_the_star(row):
    for i in range(1, row+1):
        for j in range(row, i, -1):
            print(" ", end="")
        for k in range(1, i + 1):
            print("*", end=" ")
        print()
    print()

def question_ans(input_number):
    formula_text = ""
    sum_total = 0
    for i in range(1, input_number+1):
        sum_total = sum_total + i
        if formula_text == "":
            formula_text = str(i)
        else:
            formula_text = formula_text + " + " + str(i)
    print(formula_text + " = " +str(sum_total))
    print()

def question_3(input_char):
    letter_count = len(input_char)
    char_list = []
    for char in input_char:
        char_list.append(char)
    for i in range(0, letter_count):
        if i %2 != 1:
            print(f"The char {i+1} is {char_list[i]}")

if __name__ == '__main__':
    print_hi('this is Oskar')
n = 5
print('Question 1')
print_the_star(n)
print('Question 2')

number_input = input("Please input your number:")
question_ans(int(number_input))

print('Question 3')
question_3_input = input("Please input word: ")
question_3(question_3_input)

