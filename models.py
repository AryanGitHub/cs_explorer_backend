from .database import Base , engine
from sqlalchemy.sql.expression import text
from sqlalchemy import Column, Integer, String, TIMESTAMP

class resource(Base):
    __tablename__ = "resources_post"
    post_id = Column(Integer ,primary_key=True)
    title = Column(String , nullable=False)
    description = Column(String , nullable=True)
    http_link = Column(String , nullable=False)
    votes = Column(Integer , nullable=False , default=0)
    created_at = Column(TIMESTAMP , nullable=False ,server_default=text('now()'))
    # modified_at : int ## fix this too
    author_id = Column(Integer , nullable=False)
    # tags : dict = {} not_working



Base.metadata.create_all(engine)
