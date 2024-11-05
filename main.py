from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Waltez, Welcome to API development"}

@app.get("/posts")
def get_posts():
    return{"message": "This is your posts",
    "message_2": "The journey will be arduous but adventurous"
    }

