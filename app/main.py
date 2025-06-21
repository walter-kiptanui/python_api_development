from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host = 'localhost', database = 'fastapi',
                                user = 'postgres', password = 'Vassiriki@22',
                                cursor_factory = RealDictCursor)
    
        cursor = conn.cursor()
        print("Database connection was successfull!")
        break
    
    except Exception as error:
        print("Connection to database failed!")
        print("The error is: ", error)
        time.sleep(2)
    

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1 }, 
            {"title": "This ain't your life", "content": "Your real life is in your imagination", "id": 2}]

def find_post(id: int):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index(id: int):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
        
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/posts")
def root():
    return {"data": my_posts}

@app.get("/posts")
def get_posts():
    return {"data": "Your bible says, your gift will make room for you."}

@app.post("/posts", status_code = status.HTTP_201_CREATED)
def create_posts(post : Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(1, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}



@app.get("/posts/{id}")
def get_post(id: int, response: Response):

    post = find_post(id)
    print(post)
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"post with id {id} not found"}
    return {"post detail": post}

@app.get("posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}

@app.delete("/posts/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index(id)

    if index == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"post with id {id} not found")
    my_posts.pop(index)        
    return Response(status_code = status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):

    """
    
    my_posts.append(post_dict)"""
    print(post)
    index = find_index(id)

    if index == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"post with id {id} not found")
    
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict

    return {"data": "post_dict"}