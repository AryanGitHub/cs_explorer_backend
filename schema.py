from datetime import datetime
from pydantic import BaseModel
from typing import Optional 

class resource_post_base (BaseModel):
    post_id : Optional[int] = None
    title : str
    description : Optional[str] = None
    http_link : str
    # tags : dict = {} not_working


class resource_post_create (resource_post_base):
    pass

class resource_post_response (resource_post_base):
    created_at : datetime
    author_id : int


