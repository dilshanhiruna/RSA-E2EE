import React, { useState, useEffect } from "react";
import axios from "axios";

const RSA = () => {
  const NodeRSA = require("node-rsa");

  const key = new NodeRSA({ b: 256 });

  let public_key = new NodeRSA(key.exportKey("public")); //client public key for encryption
  let private_key = new NodeRSA(key.exportKey("private")); //client public key for encryption

  const client_public_key = key.exportKey("public"); //client public key
  const client_private_key = key.exportKey("private"); //client private key

  const [server_public_key, setServerPubKey] = useState("");
  const [encrypted_client_public_key, setencrypted_client_public_key] =
    useState("");

  useEffect(() => {
    //get server public key (key 1)
    axios
      .get("http://127.0.0.1:5000/serverkey")
      .then((res) => {
        setServerPubKey(res.data.Key); //store key 1
        console.log(server_public_key); //print key 1
      })
      .catch((e) => {
        console.log(e);
      });
  }, []);

  useEffect(() => {
    if (server_public_key !== "") {
      const server_key = new NodeRSA(server_public_key); //key 1 for encryption
      const encrypted = server_key.encrypt(client_public_key, "base64"); //encrypt client public key by server public key (key 1)
      setencrypted_client_public_key(encrypted); //store encrypted key 1

      document.getElementById("key").innerHTML = client_public_key; //display client public key
    } else {
      console.log("error fetching server public key");
    }
  }, [server_public_key]);

  useEffect(() => {
    //send encryped client public key to the server
    axios
      .post(
        `http://127.0.0.1:5000/clientkey`,
        {
          client_public_key: encrypted_client_public_key,
        },
        {
          headers: {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/x-www-form-urlencoded",
          },
        }
      )
      .then(() => {
        console.log(encrypted_client_public_key); //print encryped client public key
      })
      .catch((e) => {
        console.log(e);
      });
  }, [encrypted_client_public_key, server_public_key]);

  return (
    <div style={{ padding: "30px" }}>
      <h1>Hello World</h1>
      <br />
      <h2>Client Public Key</h2>
      <p id="key"></p>
      <br />
      <h2>Client Private Key</h2>
      {client_private_key}
    </div>
  );
};

export default RSA;
