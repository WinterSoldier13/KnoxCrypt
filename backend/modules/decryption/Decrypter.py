import os
import time
from cryptography.fernet import Fernet
from tqdm import tqdm
import pyAesCrypt as hash

class Decrypter:
    def __init__(self, files, password) -> None:
        self.files = files
        self.hash_password = password
        self.fernet = Fernet(b'zta1UUofnowc3cur17oddzYerqMb2XDJEsKVE6wnjSI=')

    def get_file_name(self, file_name):
        output = self.fernet.decrypt(file_name[2:-1].encode()).decode()
        return output
    
    def decrypt(self):
        now = time.time()
        for i in tqdm(range(len(self.files))):
            file = os.path.join(self.files[i][0], self.files[i][1])
            file_name = self.files[i][1]
            root_path = self.files[i][0]

            original_filename = self.get_file_name(file_name[:-5])
            print("Decryprting {0} to {0}".format(file, original_filename))
            hash.decryptFile(file, '{}'.format(os.path.join(root_path, str(original_filename))), self.hash_password)
            os.unlink(file)
        return {
            "time_taken" : "{}".format(time.time() - now),
            "total_files" : "{}".format(len(self.files))
        }
