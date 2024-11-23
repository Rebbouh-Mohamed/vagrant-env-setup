from prj import db
from sqlalchemy import String,Column,Integer

class User(db.Model):
    id=Column(Integer,primary_key=True,nullable=False)
    user_name=Column(String(20),unique=True,nullable=False)
    email=Column(String(60),unique=True,nullable=False)
    pass_word=Column(String(60),nullable=False)
    def __repr__(self) -> str:
        return f"User('{self.user_name}','{self.email}'"
    
