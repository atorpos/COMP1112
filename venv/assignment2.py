def vowel_checker(word):
    v_count = 0
    c_count = 0
    vowels = {'a','e','i','o','u','A','E','I','O','U'}
    char_list = [char for char in word]
    # print(char_list)
    for _char in char_list:
        if _char in vowels:
            v_count +=1
        else:
            c_count +=1
    return v_count, c_count

def factorial_calculator(f_number):

    if type(f_number) is int:
        f_result = 1
        for i in range(1, f_number + 1):
            f_result *= i
        return f_result
    else:
        return 0


set_string = "pneumonoultramicroscopicsilicovolcanoconiosis"
n_of_v, n_of_c = vowel_checker(set_string)

print(f"String: {set_string}")
print(f"total vowel in text are {n_of_v}")
print(f"total consonant in text are {n_of_c}")

print(f"The factorial number is {factorial_calculator(25)}")