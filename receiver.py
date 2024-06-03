import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  

ip_address = "127.0.0.1"      # Enter the which is sending the message.

port_no = 2525

my_address = (ip_address, port_no)
s.bind(my_address)

while True:
    data = s.recvfrom(100)
    message = data[0]
    sender_address = data[1]
    sender_ip = sender_address[0]
    message = message.decode('ascii')

    if '.txt' in message:
        # Assuming the format is "file_name.txt: message"
        try:
            file_name, message = message.split(":", 1)  
            file_name = file_name.strip()  
            message = message.strip()  
            
            if file_name.endswith('.txt'):
                with open(file_name, 'a+', encoding='utf-8') as file:
                    file.write(message + "\n")
                    file.close()
                print(f"Message written to {file_name}: {message}")
            else:
                print(f"Error: The file name {file_name} does not have a .txt extension.")
        except ValueError:
            print("Error: Message format is incorrect. Expected format 'file_name.txt: message'")
    else:
        print("Received message:", message)
