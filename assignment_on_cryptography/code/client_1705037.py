import socket
import os        
import pickle
from aes_1705037 import *
from rsa_1705037 import RSA

def save_file_at_dir(dir_path, filename, file_content, mode='w'):
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, filename), mode) as f:
        f.write(file_content)
        f.close()


#bonus 2
aes_key_length = 256

# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
port = 12345               

# connect to the server on local computer
s.connect(('127.0.0.1', port))

f = open("Don’t Open this/private_key.txt", "r")
private_key = f.read().split(',')
d = private_key[0]
n = private_key[1]
decipheredTexthex = ""
decipheredPlainText = ""
    
# receive data from the server and decoding to get the string.
stages = int(s.recv(1024).decode())
print("number of stages",stages)
s.send("ack".encode())

filename = s.recv(1024).decode()
s.send("ack".encode())

for stage in range(stages):
    buffer_sizes = s.recv(1024).decode().split(',')
    # print(buffer_sizes)
    s.send("ack".encode())

    recvd_data = s.recv(int(buffer_sizes[0]))
    aes_ciphertext = pickle.loads(recvd_data)
    # print("@@@",aes_ciphertext)
    
    recvd_data2 = s.recv(int(buffer_sizes[1]))
    rsa_ciphertext = pickle.loads(recvd_data2)
    # print("@@@",rsa_ciphertext)

    recvd_data3 = s.recv(int(buffer_sizes[2]))
    public_key = pickle.loads(recvd_data3)
    # print("@@@",public_key)


    rsa = RSA()
    rsa.ciphertext = rsa_ciphertext
    rsa.d = int(d)
    rsa.n = int(n)
    rsa.createDecryptedText()
    # print("@@@rsa.decryptedtext",rsa.decryptedtext)

    aes = AES()
    aes.setKeyLength(aes_key_length)
    aes.setKey(key=rsa.decryptedtext)
    aes.ciphertexthex = aes_ciphertext
    aes.createDecipheredText()
    decipheredTexthex += aes.decipheredtexthex
    decipheredPlainText += aes.decipheredtext.lstrip('\0')
    # print("aes_ciphertext",aes_ciphertext)
    # print("aes_deciphertext",aes.decipheredtext)
    print("stage",stage,": completed")


if filename!="nan":
    save_file_at_dir('Don’t Open this', 'dpt.txt', decipheredTexthex)
    createFileFromDeciphered(decipheredTexthex,filename)
else : #plaintext
    save_file_at_dir('Don’t Open this', 'dpt.txt', decipheredPlainText)

s.send("finished".encode())
# close the connection
s.close()    