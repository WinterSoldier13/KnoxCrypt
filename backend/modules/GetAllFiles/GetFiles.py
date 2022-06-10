import os
class GetFiles:
    def __init__(self, current_path, call_for_decryption = False) -> None:
        self.current_path = current_path
        self.call_for_decryption = call_for_decryption

    def get_all_files(self) -> list:
        files_ = []
        for root, dirs, files in os.walk(os.path.abspath(self.current_path)):
            for file in files:
                if file!='encrypter_decrypter.py' and file != 'encrypt_decrypt.sh' and file[0]!='.':
                    # for decryption only find the encrypted files
                    if self.call_for_decryption:
                        if '.gogl' in file:
                            file_path = os.path.join(root, file)
                            print(file_path)

                            files_.append([root, file])

                    # for encryption only get the files that are not pre-encrypted
                    else:
                        if '.gogl' not in file:
                            file_path = os.path.join(root, file)
                            print(file_path)
                            files_.append([root, file])

        return files_