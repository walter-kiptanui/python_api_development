from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to my API! Imagination is everything"}

@app.get("/posts")
def get_posts():
    return {"data": "Your bible says, your gift will make room for you."}

@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload['title']} content :{payload['content']}"}
    

