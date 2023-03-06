# first of all import the socket library
import socket            
from aes_1705037 import *
from rsa_1705037 import RSA
import os
import pickle
import filecmp

def save_file_at_dir(dir_path, filename, file_content, mode='w'):
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, filename), mode) as f:
        f.write(file_content)
        f.close()



key = input("Key :")
filename = "nan"

#bonus 2
aes_key_length = 256

#rsa key length
key_length = 32

rsa = RSA()
rsa.setPlainTextKeyLength(key,key_length)
rsa.generateKeys()
rsa.createCipherText()

save_file_at_dir('Don’t Open this', 'private_key.txt', str(rsa.keys['private'][0])+','+str(rsa.keys['private'][1]))


choice = int(input("1. Plain Text 2. Media File\n"))

ciphertexts = []
blocks = []
if choice==1 :
  plaintext = input("Plain Text :")
  plaintexthex = plaintext.encode("utf-8").hex()
  blocks = getBlocks(plaintexthex)
else:
  filename = input("file path :")
  # filename = "/media/sadia/SSD 1/Study/L4T1/406/Offline 1/Offline/sent_media/test2.jpg"
  blocks = processMedia(filename)

stage=0
for block in blocks :
    aes = AES()
    aes.setInitialTextinHex(block)
    aes.setKeyLength(aes_key_length)
    aes.setKey(key)
    # print("stage",stage,": encryption beginning..")
    aes.createCipherText()
    ciphertexts.append(aes.ciphertexthex)
    # print("stage",stage,": encryption completed.")
    print("stage",stage,": completed.")
    stage += 1



# next create a socket object
s = socket.socket()        
print ("Socket successfully created")
 
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345               
 
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(5)    
print ("socket is listening")           
 
# a forever loop until we interrupt it or
# an error occurs
while True:
 
# Establish connection with client.
  c, addr = s.accept()    
  print ('Got connection from', addr )
 
  stages = str(len(ciphertexts))
  c.send(stages.encode())
  ack = c.recv(1024).decode()

  # send file name
  c.send(filename.encode())
  ack = c.recv(1024).decode()

  b=0
  for ciphertexthex in ciphertexts:
    data1=pickle.dumps(ciphertexthex)
    data2=pickle.dumps(rsa.ciphertext)
    data3=pickle.dumps(rsa.keys['public'])
    size = str(len(data1)) + "," + str(len(data2)) + "," + str(len(data3))
    c.send(size.encode())
    ack = c.recv(1024).decode()
    
    c.send(data1)
    # print("sent 1",len(data1))
    data=pickle.dumps(rsa.ciphertext)
    c.send(data2)
    # print("sent 2",len(data2))
    data=pickle.dumps(rsa.keys['public'])
    c.send(data3)
    # print("sent 3",len(data3))
    print("sent block",b)
    b+=1

  ack = c.recv(1024).decode()
  # Close the connection with the client
  c.close()
   
  # Breaking once connection closed
  break

if choice==1:
  try :
    f = open("Don’t Open this/dpt.txt", "r")
    dpt = f.read()
    print("plaintext :",plaintext)
    print("decrypted text on file :",dpt)
    
    if dpt==plaintext :
      print("strings match")
    else :
      print("strings do not match")
  except :
    print("file does not exist")

else :
  # Path of first file
  file1 = filename
    
  # Path of second file
  file2 = "recvd_media/"+filename.split('/')[-1]
    
  # Compare the os.stat()
  # signature i.e the metadata
  # of both files 
  comp = filecmp.cmp(file1, file2)
    
  # Print the result of comparison
  print(comp)
    
  # Compare the
  # contents of both files
  comp = filecmp.cmp(file1, file2, shallow = False)
    
  # Print the result of comparison
  print(comp)

