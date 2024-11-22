from fastapi import FastAPI , HTTPException , Depends, status
from fastapi import Body
from pydantic import BaseModel
from typing import Optional
from typing import Dict
from sqlalchemy.orm import Session

from .database import engine , get_db

from . import models

app = FastAPI()

class resource_post (BaseModel):
    post_id : Optional[int] = None
    title : str
    description : Optional[str] = None
    http_link : str
    # tags : dict = {} not_working


@app.get("/")
def root():
    return { "message" : "working" }


@app.get("/posts")
def get_all_post(db : Session = Depends(get_db)):
    all_posts = db.query(models.resource).all()
    return all_posts

@app.get("/try")
def tryIt(db: Session = Depends(get_db)):
    new_post = models.resource(title = "this is a title" , http_link = "this is a link" , author_id = 222)

    db.add(new_post)
    db.commit()

@app.get("/posts/{id}")
def get_post_with_id(id : int , db : Session = Depends(get_db)):
    post = db.query(models.resource).filter(models.resource.post_id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , 
        detail=f" ID {id} NOt Found.")
    return post


@app.post("/posts" , status_code=status.HTTP_201_CREATED)    
def create_posts( post_body :resource_post , db : Session = Depends(get_db)):
    new_post = models.resource(author_id=0,**post_body.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
    


@app.delete("/posts/{id}" , status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int , db : Session = Depends(get_db)):
    post_query = db.query(models.resource).filter(models.resource.post_id == id)
    post = post_query.first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"No post with id {id} found")
    post_query.delete(synchronize_session=False)
    db.commit()

    return None
    

@app.put("/posts/{id}")
def update_post(id : int, new_post_body : resource_post ,  db : Session = Depends(get_db)):
    post_query = db.query(models.resource).filter(models.resource.post_id == id)
    post = post_query.first()
    to_add = new_post_body.model_dump()
    to_add["author_id"] = "0"
    to_add["post_id"] = post.post_id
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"No post with id {id} found")
    post_query.update(to_add,synchronize_session=False)
    db.commit()
    db.refresh(post)

    return post

