import uvicorn
import hashlib

import validators
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from .db.database import get_db_session
from .models.url import URL
from .schemas.url import URLBase, URLInfo


app = FastAPI()

def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)

def raise_not_found(request):
    message = f"URL '{request.url}' doesn't exist"
    raise HTTPException(status_code=404, detail=message)

@app.get("/")
def read_root():
    return "Welcome to the URL shortener API :)"

@app.get("/{url_key}")
def forward_to_target_url(
        url_key: str,
        request: Request,
        db: Session = Depends(get_db_session)
    ):
    db_url = (
        db.query(URL)
        .filter(URL.key == url_key, URL.is_active)
        .first()
    )
    if db_url:
        return RedirectResponse(db_url.target_url)
    else:
        raise_not_found(request)

@app.post("/url", response_model=URLInfo)
def create_url(url: URLBase, db: Session = Depends(get_db_session)):
    if not validators.url(url.target_url):
        raise_bad_request(message="Your provided URL is not valid")

    hash_object = hashlib.sha256(url.target_url.encode())
    hash_hex = hash_object.hexdigest()
    key = hash_hex[:8]
    secret_key = hash_hex[:10]

    db_url = URL(
        target_url=url.target_url, key=key, secret_key=secret_key
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    db_url.url = key
    db_url.admin_url = secret_key

    return db_url

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
