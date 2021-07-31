from Cryptodome.PublicKey import RSA
import base64
import mysql.connector
from mysql.connector import Error
import Cryptodome
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES, PKCS1_OAEP
import dbconnection


def generate_keyPair_1():
    key = RSA.generate(2048)
    private_key = key.export_key()
    # sql = "INSERT INTO server (privateKey_1) VALUES ('%s')"
    sql = "UPDATE server SET privateKey_1 = '"+private_key.decode('utf-8')+"'"
    val = ("private_key")
    dbconnection.cursor.execute(sql,val)
    dbconnection.connection.commit() #save private key 1 in database
    file_out = open("keys/private_1.pem", "wb") 
    file_out.write(private_key) #save private key 1 in file
    file_out.close()

    public_key = key.publickey().export_key()
    sql = "UPDATE server SET publicKey_1 = '"+public_key.decode('utf-8')+"'"
    val = ("private_key")
    dbconnection.cursor.execute(sql,val)
    dbconnection.connection.commit() #save public key 1 in database
    file_out = open("keys/public_1.pem", "wb")
    file_out.write(public_key) #save public key 1 in file
    file_out.close()


def generate_keyPair_2():
    key = RSA.generate(4096)
    private_key = key.export_key()
    sql = "UPDATE server SET privateKey_2 = '"+private_key.decode('utf-8')+"'"
    val = ("private_key")
    dbconnection.cursor.execute(sql,val)
    dbconnection.connection.commit() #save private key 2 in database
    file_out = open("keys/private_2.pem", "wb")
    file_out.write(private_key) #save private key 2 in file
    file_out.close()

    public_key = key.publickey().export_key()
    sql = "UPDATE server SET publicKey_2 = '"+public_key.decode('utf-8')+"'"
    val = ("private_key")
    dbconnection.cursor.execute(sql,val)
    dbconnection.connection.commit() #save public key 2 in database
    file_out = open("keys/public_2.pem", "wb")
    file_out.write(public_key) #save public key 2 in file
    file_out.close()


# generate_keyPair_1() 
# generate_keyPair_2()

def encryption(arg_publickey, arg_cleartext): 
    encryptor = PKCS1_OAEP.new(arg_publickey)
    ciphertext = encryptor.encrypt(arg_cleartext)
    return base64.b64encode(ciphertext)




def decryption(arg_privatekey, arg_b64text):
    decoded_data = base64.b64decode(arg_b64text)
    decryptor = PKCS1_OAEP.new(arg_privatekey)
    decrypted = decryptor.decrypt(decoded_data)
    return decrypted


def decryptClientPublicKey():  #decrypts the client public key and prints it
    server_privateKey_1 = RSA.importKey(open('keys/private_1.pem').read())
    client_public_key = open('keys/clientPublicKey.pem').read()
    encrypted_client_key = str.encode(client_public_key)
    print(decryption(server_privateKey_1, encrypted_client_key))
   

def encryptServerPublicKey2(): # the function for encrypting server public key 2 by client public key
    client_public_key = open('keys/clientPublicKey.pem').read() #get client public key
    encrypted_client_key = str.encode(client_public_key)
    server_privateKey_1 = RSA.importKey(open('keys/private_1.pem').read()) #get server private key 1
    
    server_publicKey_2 = RSA.importKey(open('keys/public_2.pem').read())
    public_client_key = decryption(server_privateKey_1, encrypted_client_key) #decrypts the client public key 
    encrypted_server_publicKey_2 =encryption(public_client_key,server_publicKey_2) # encrypt server public key 2 by client public key (error occurs here)
    file_out = open("keys/encrypted_server_publicKey_2.pem", "wb")
    file_out.write(encrypted_server_publicKey_2)
    file_out.close()

# encryptServerPublicKey2()