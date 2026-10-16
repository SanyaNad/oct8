from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "genre": "Science Fiction"
    },
    {
        "title": "The Martian",
        "author": "Andy Weir",
        "genre": "Science Fiction"
    },
    {
        "title": "Expanse",
        "author": "James Corey",
        "genre": "Science Fiction"
    }
]

@app.get("/")
def get_info():
    return {
        "message": "API books",
        "endpoint": "/books"
    }

@app.get("/books")
def get_books():
    return books