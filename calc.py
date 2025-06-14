from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
def root():
    return {"message": "Welcome to my API! Imagination is everything"}

@app.get("/posts")
def get_posts():
    return {"data": "Your bible says, your gift will make room for you."}

@app.post("/createposts")
def create_posts(new_post : Post):
    print(new_post.rating)
    print(new_post.dict())
    return {"data": "new post"}
    

