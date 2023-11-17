# URL-shortener

## Manual

1. Clone `git clone https://github.com/MarcAlmirallBertran/URL-shortener.git & cd URL-shortener`
2. (Optional) Install virtualenv (optional but recommended)
    - `python -m venv venv`
    - `.\venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. `uvicorn app.main:app --reload` (It runs FastAPI servers using gunicorn)
5. Visit `127.0.0.1:8000` to use the app