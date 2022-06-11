# KnoxCrypt
KnoxCrypt [MacOS/Linux] - A secure cryptographic tool to encrypt-decrypt your files with SHA-256 hashing.

## How to Encrypt?
1. Select the folder that you want to encrypt using the UI (currently under development). 
2. Supply a password.
3. The backend will recursively encrypt all previously "non-encrypted" files inside the directory(including sub-dirs).

## How to Decrypt?
1. Select the folder that you want to decrypt using the UI. 
2. Supply the password with which the files were earlier encrypted.
3. The backend will recursively decrypt all previously "encrypted" files inside the directory(including sub-dirs).

## Features under development
1. The frontend.
2. Multi-Threading support for encryption/decryption for performance improvement
3. Assertion support for Windows Operating System.

## Before Encryption

![Alt text](./resources/before_encryption_folder.png?raw=true "Folder View before encryption")
![Alt text](./resources/before_encryption_term.png?raw=true "Terminal View before encryption")

## After Encryption

![Alt text](./resources/after_encryption_folder.png?raw=true "Folder View before encryption")
![Alt text](./resources/after_encryption_term.png?raw=true "Terminal View before encryption")

