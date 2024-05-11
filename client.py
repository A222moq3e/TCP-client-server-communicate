import socket

HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethostname()
PORT = 1888

s.connect((IP, 1888))

print(s.recv(128))

while True:
    print(s.recv(128))
    s.send(input().encode("utf-8"))
    # s.send("hi".encode("utf-8"))
    msg = s.recv(128)
    if (len(msg) <= 0):
        break
    print(msg.decode("utf-8"))


# while True:
#     full_msg = ''
#     new_msg = True
#     while True:
#         msg = s.recv(16)
#         if new_msg:
#             print(f"new message len: {msg[:HEADERSIZE]}")
#             msglen = int(msg[:HEADERSIZE])
# new_msg = False
#         full_msg += msg.decode("utf-8")
#         print(msg.decode("utf-8"))
