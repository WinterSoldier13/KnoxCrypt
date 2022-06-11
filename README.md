# KnoxCrypt
KnoxCrypt [MacOS/Linux] - A secure cryptographic tool to encrypt-decrypt your files with SHA-256 hashing.

## Requirements
1. `pip install -r requirements.txt` in backend folder
2. `npm install` in frontend folder
3. start the backend by `uvicorn main:app`
4. start the frontend by `npm start`

## How to Encrypt?
1. Select the folder that you want to encrypt using the UI. 
2. Supply a password.
3. The backend will recursively encrypt all previously "non-encrypted" files inside the directory(including sub-dirs).

## How to Decrypt?
1. Select the folder that you want to decrypt using the UI. 
2. Supply the password with which the files were earlier encrypted.
3. The backend will recursively decrypt all previously "encrypted" files inside the directory(including sub-dirs).

## Features under development
1. Multi-Threading support for encryption/decryption for performance improvement
2. Assertion support for Windows Operating System.

## DEMO VIDEO

![DEMO](./resources/demo.gif "demo video")

## Before Encryption

![Alt text](./resources/before_encryption_folder.png?raw=true "Folder View before encryption")
![Alt text](./resources/before_encryption_term.png?raw=true "Terminal View before encryption")

## After Encryption

![Alt text](./resources/after_encryption_folder.png?raw=true "Folder View before encryption")
![Alt text](./resources/after_encryption_term.png?raw=true "Terminal View before encryption")

