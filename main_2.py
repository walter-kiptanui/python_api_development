from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Waltez, Welcome to API development"}

@app.get("/posts")
def get_posts():
    return{"message": "This is your posts",
    "message_2": "The journey will be arduous but adventurous"
    }

@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f" title {payload['title']} content: {payload['content']}"}