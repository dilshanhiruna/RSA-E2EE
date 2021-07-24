# End-to-end encryption using RSA algorithm

## How to Run

1- Create server public key and private key<br/>
run python script in server directory<br/>
>import index\
>index.generate_keyPair_1()

2- Run api.py to pass server public key as json to client

3- Run Client\
run "npm start" in client directory
>npm start

(now the client public key is encrypted by the server public key and has been pass to the server)

4- decrypt the client public key using server private key\
run python script
>import index\
>index.decryptClientPublicKey()

5- generate 2nd key pair (public/private)
>index.generate_keyPair_2()

All the generated keys are saved in MySQL Database\
Project is completed and working upto generating server key pair 2

# About the Project

The client generates a public key and private key. It has servers public key (Key 1)

It then sends it's public key encrypted by servers public key (Key 1).

Then at server side the server decrypts the message by its private key and get the clients public Key

Then the server generates another public key and private key pair (Key 2)

it then sends its public key (Key 2) encrypted by the client's public key to the client.

client receives the message and decrypt it by using its private key
while this is happening the server should maintain a record of its two public and private key pairs and clients public key received in the database
