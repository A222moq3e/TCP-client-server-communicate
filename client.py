import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# IP = socket.gethostname()
IP = "69.48.163.203"  # server ip
PORT = 1888
try:
    s.connect((IP, PORT))
except:
    print('Server is down, please try later.')
    exit()
# recive first message (welcom message)
print(s.recv(128).decode("utf-8"))

while True:
    # recive Enter Input Message
    print(s.recv(128).decode("utf-8"))
    
    s.send((input() + " ").encode("utf-8"))
    # s.send("hi".encode("utf-8"))
    msg = s.recv(128)
    if (len(msg) <= 0):
        break
    print(msg.decode("utf-8"))

s.close()
