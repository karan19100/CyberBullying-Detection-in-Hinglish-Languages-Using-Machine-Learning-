import socket
import select
import sys
import time
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer

model = pickle.load(open("/Users/karan/Desktop/final project demo/Safe_Chat/LinearSVC.pkl", 'rb'))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = "127.0.0.1"
port = 12345

server.connect((IP_address, port))
print("Connected To server")

user_id = input("Type user id: ")
room_id = input("Type room id: ")

server.send(str.encode(user_id))
time.sleep(0.1)
server.send(str.encode(room_id))

def prettyPrinter(self,data_1):
         # List of stopwords 
    my_file = open("/Users/karan/Desktop/final project demo/Safe_Chat/stopwords.txt", "r")
    content = my_file.read()
    content_list = content.split("\n")
    my_file.close()
    tfidf_vector =  TfidfVectorizer(stop_words = content_list, lowercase = True,vocabulary=pickle.load(open("/Users/karan/Desktop/final project demo/Safe_Chat/tfidf_vector_vocabulary.pkl", "rb")))
    data_2=tfidf_vector.fit_transform([data_1])
    print(data_2)
    pred = model.predict(data_2)
    print(pred)
    if pred==0:
        print('Non bullying')
        return pred
    else: 
        # print("Stop bullying people and behave decently. If you do this again we will block you.")
        print("Bullying message detected it has been hidden")
        return pred

while True:
    socket_list = [sys.stdin, server]

    read_socket, write_socket, error_socket = select.select(socket_list, [], [])

    for socks in read_socket:
        if socks == server:
            message = socks.recv(1024)
            
            print(str(message.decode()))

            if str(message.decode()) == "FILE":
                file_name = socks.recv(1024).decode()
                lenOfFile = socks.recv(1024).decode()
                send_user = socks.recv(1024).decode()

                if os.path.exists(file_name):
                    os.remove(file_name)

                print(file_name, lenOfFile, send_user)

                total = 0
                with open(file_name, 'wb') as file:
                    while str(total) != lenOfFile:
                        data = socks.recv(1024)
                        total = total + len(data)     
                        file.write(data)
                print("<" + str(send_user) + "> " + file_name + " sent")
                       
            else:
                print(message.decode())

        else:
            message = sys.stdin.readline()

            if str(message) == "FILE\n":
                file_name = input("Enter the file name : ")
                server.send("FILE".encode())
                time.sleep(0.1)
                server.send(str("client_" + file_name).encode())
                time.sleep(0.1)
                server.send(str(os.path.getsize(file_name)).encode())
                time.sleep(0.1)

                file = open(file_name, "rb")
                data = file.read(1024)
                while data:
                    server.send(data)
                    data = file.read(1024)
                sys.stdout.write("<You>")
                sys.stdout.write("File sent successfully\n")
                sys.stdout.flush()

            else:
                server.send(message.encode())
                sys.stdout.write("<You>")
                sys.stdout.write(message)
                sys.stdout.flush()
server.close()

