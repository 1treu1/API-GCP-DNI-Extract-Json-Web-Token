from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
import requests
from middlewares.verify_token_route import VerifyTokenRoute
from requests import post
from typing import List
users_ocr = APIRouter(route_class=VerifyTokenRoute)


@users_ocr.post("/users/ocr")
def ocr_users(files: List[UploadFile] = File(...)):
    url = "https://ocr-gcp-wubzfxhjna-uc.a.run.app/docs"
    out = {}
    for file in files:
        file_dict = {"files": (file.filename, file.file, file.content_type)}  
        try:
            response = requests.post(url, files=file_dict)
            response.raise_for_status()
            out[file.filename] = response.json()
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail=str(e))
    return out