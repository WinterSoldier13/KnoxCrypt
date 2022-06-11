import imp
from subprocess import call
from typing import Union
from fastapi import FastAPI, Request
from modules.decryption.Decrypter import Decrypter
from modules.GetAllFiles.GetFiles import GetFiles
from modules.encryption.Encrypter import Encrypter
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get("/")
def get_status():
    return {"version": "1.0.0",
            "application_name": "KnoxCrypt",
            "backend_status": "active"}

@app.post("/all_files/")
async def get_files(file_path_request : Request):
    request_file = await file_path_request.form()
    request_file = jsonable_encoder(request_file)
    current_path = request_file['current_path']
    call_for_decryption = False if request_file['call_for_decryption'].lower() == 'false' else True
    print(current_path, call_for_decryption)

    ob = GetFiles(current_path=current_path, call_for_decryption=call_for_decryption)
    files = ob.get_all_files()

    return {"files" : files}

@app.post("/encrypt/")
async def encrypt_files(file_path_request : Request):
    request_file = await file_path_request.json()
    request_file = jsonable_encoder(request_file)
    current_path = request_file['current_path']

    assert len(current_path) != 0, "folder to encode was not specified"
    assert current_path!='/', "wow dealing with root dir is dangerous. Will not proceed."
    assert '/Users/' in current_path, "will deal only with User directories here buddy"

    call_for_decryption = False
    hash_password = request_file['password']

    ob = GetFiles(current_path=current_path, call_for_decryption=call_for_decryption)
    files = ob.get_all_files()

    encrypter_obj = Encrypter(files=files, password=hash_password)
    return encrypter_obj.encrypt()

@app.post("/decrypt/")
async def decrypt_files(file_path_request : Request):
    request_file = await file_path_request.json()
    request_file = jsonable_encoder(request_file)
    current_path = request_file['current_path']
    
    assert current_path!='/', "wow dealing with root dir is dangerous. Will not proceed."
    assert '/Users/' in current_path, "will deal only with User directories here buddy"

    call_for_decryption = True
    hash_password = request_file['password']

    ob = GetFiles(current_path=current_path, call_for_decryption=call_for_decryption)
    files = ob.get_all_files()
    print(files)

    decrypter_obj = Decrypter(files=files, password=hash_password)
    
    return decrypter_obj.decrypt()


    
