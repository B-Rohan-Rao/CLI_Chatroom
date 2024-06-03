import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

TARGET_IP = "127.0.0.1"      # Enter Your own Ip address to which you want to send message

port_no = 2525

target_address = (TARGET_IP, port_no)

def send_file():
    file_path = input("Please enter the full path of the txt file: ")
    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError
        
        file_name = os.path.basename(file_path)
        with open(file_path, 'r', encoding='utf-8') as f:
            message = f.read()
        message_encrypted = f"{file_name}:{message}".encode('ascii')
        s.sendto(message_encrypted, target_address)
        print("Your file has been sent!")
    except FileNotFoundError:
        print("File not found!")

while True:
    message = input("Enter your message (or 'send_file' to send a file, 'exit' to quit): ")
    if message.lower() == "exit":
        print("Exiting")
        break
    elif message.lower() == "send_file":
        send_file()
    else:
        message_encrypted = message.encode('ascii')
        s.sendto(message_encrypted, target_address)
