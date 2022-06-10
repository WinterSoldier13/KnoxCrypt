from pydantic import BaseModel

class FilePathRequest(BaseModel):
    file_path: str
    call_for_decryption: bool

