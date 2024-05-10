

def converter(string):
    # user_input = "B"
    user_input = string.strip()
    user_input_lst = user_input.split(" ")
    checker_returned = check_inputs(user_input)
    if (not checker_returned[0]):
        return checker_returned

    # print('(' + character + '-' + num+')')
    # print('200', num)
    return [True, '200 '+str(555)]


def main():
    while (True):
        usr_inp = input("please enter your input:")
        usr_inp = usr_inp.strip()
        data = converter(usr_inp)
        if (data[1] == 'Quit'):
            break
        print(data[1])


def check_inputs(user_input):
    user_input_lst = user_input.split(" ")
    if (len(user_input) == 0):
        return [False, '500 Request is empty']
    if (len(user_input_lst) > 2 or len(user_input_lst) < 1):
        return [False, '300 Bad request']
    iterator = iter(user_input_lst)
    character = next(iterator, '*')
    num = next(iterator, '*')
    if (character == "Q"):
        return [False, 'Quit']
    if (character not in ["B", "H"]):
        return [False, '300 Bad request']
    if (num == "*"):
        return [False, '400 The number is missing']
    return [True, '']


main()

# converter(" ")
# converter("B")
# converter("B 22")  # True input
# converter("G 22")
# converter("B 22 55")
