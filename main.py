from fastapi import FastAPI , HTTPException , status
from fastapi import Body
from pydantic import BaseModel
from typing import Optional
from typing import Dict

app = FastAPI()

postNum = 0
database = []


class resource_post (BaseModel):
    post_id : Optional[int] = None
    title : str
    description : Optional[str] = None
    http_link : str
    # votes : int
    # created_at : int ## fix this
    # modified_at : int ## fix this too
    # author_id : int ## maybe
    # tags : dict = {} not_working



def find_post_by_id(id):
    for x in database:
        if x["post_id"] == id:
            return x
    return None

def find_post_index_by_id(id):
    for i , x in enumerate(database):
        print (i , x)
        if x["post_id"] == id:
            return i
    return None

@app.get("/")
def root():
    return { "message" : "working" }


@app.get("/posts")
def get_all_post():
    return database

@app.get("/posts/{id}")
def get_post_with_id(id : int):
    print(id)
    post = find_post_by_id(id)
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , 
        detail=f" ID {id} NOt Found.")
    return post


@app.post("/posts" , status_code=status.HTTP_201_CREATED)    
def create_posts(post_body :resource_post):
    global postNum
    post_body  = post_body.dict()
    post_body["post_id"] = postNum
    postNum+=1
    database.append(post_body)
    return post_body
    


@app.delete("/posts/{id}" , status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int):
    post_index = find_post_index_by_id(id)
    if post_index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"No post with id {id} found")
    post = database.pop(post_index)
    return None
    

@app.put("/posts/{id}")
def update_post(id : int, new_post_body : resource_post):
    post_index = find_post_index_by_id (id)
    if post_index == None:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND , detail=f"Post id : {id} Not found." )
    new_post_body = new_post_body.dict()
    new_post_body["post_id"] = id
    database[post_index] = new_post_body
    return new_post_body


