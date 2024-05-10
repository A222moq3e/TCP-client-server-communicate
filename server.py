

def converter(string):
    # user_input = "B"
    user_input = string.strip()
    checker_returned = check_inputs(user_input)
    if (not checker_returned[0]):
        return checker_returned
    character, num = user_input.split(" ")
    num = int(num)
    num_after_converted = 0
    # To Binary
    if (character == 'B'):
        num_after_converted = str(bin(num))[2:]
    # To Binary
    if (character == 'H'):
        num_after_converted = hex(num)
    return [True, '200 ' + str(num_after_converted)]


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
