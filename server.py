import socket


# IP = socket.gethostname()
IP = "0.0.0.0"  # Accept Request from anywhere
PORT = 1888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((IP, PORT))
s.listen(5)
# print('listening....')

#  here program will start working


def main():
    while True:
        clientsocket, address = s.accept()
        try:
            # print(f"Connection from {address} has been establish!")
            msg = "Welcom To Our Server :)"
            clientsocket.send(bytes(msg, "utf-8"))
            while True:
                # Send question to request from client
                clientsocket.send(bytes('Enter Input:', "utf-8"))
                # Wait to recive message from client
                recived_msg = clientsocket.recv(256)
                output = converter(recived_msg.decode("utf-8"))
                if (output == 'Quit'):
                    clientsocket.close()
                    break
                # send value for converted valeus (if 200) with status code and message
                clientsocket.send(bytes(output, "utf-8"))
        except:
            # print(f'closed Connection by force from {address}')
            pass

# letter => character , num => number

# Converter to Binary or Hex


def converter(inp):
    user_input = inp.strip()
    checker_returned = check_inputs(user_input)
    # When checker is False
    if (not checker_returned[0]):
        # return when 300, 400, 500 status codesW
        return checker_returned
    character, num = user_input.split(" ")
    num = int(num)
    num_after_converted = 0
    # To Binary
    if (character == 'B'):
        num_after_converted = str(bin(num))[2:]
    # To Hexadicmal
    if (character == 'H'):
        num_after_converted = str(hex(num))[2:]
    return '200 ' + num_after_converted


# Check if its is a correct Inputs
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
