import socket

HEADERSIZE = 10
# IP = socket.gethostname()
IP = "0.0.0.0"  # Accept Request from anywhere
PORT = 1888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((IP, PORT))
s.listen(5)
# print('listening....')


def main():
    while True:
        clientsocket, address = s.accept()
        try:
            # print(f"Connection from {address} has been establish!")
            msg = "Welcom to our server"
            # Add Header
            # msg = f"{len(msg):<{HEADERSIZE}}" + msg
            clientsocket.send(bytes(msg, "utf-8"))
            while True:
                clientsocket.send(bytes('Enter Input:', "utf-8"))
                recived_msg = clientsocket.recv(256)
                output = startProgram(recived_msg.decode("utf-8"))
                if (output == 'Quit'):
                    clientsocket.close()
                    break
                clientsocket.send(bytes(output, "utf-8"))
        except:
            # print(f'closed Connection by force from {address}')
            pass

# letter => character , num => number


def converter(inp):
    user_input = inp.strip()
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


def startProgram(inp):
    # usr_inp = input("please enter your input:")
    usr_inp = inp
    usr_inp = usr_inp.strip()
    data = converter(usr_inp)
    # print(data[1])
    return data[1]


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


# def main(inp):
#     while (True):
#         # usr_inp = input("please enter your input:")
#         usr_inp = inp
#         usr_inp = usr_inp.strip()
#         data = converter(usr_inp)
#         if (data[1] == 'Quit'):
#             break
#         # print(data[1])
#         return data[1]
