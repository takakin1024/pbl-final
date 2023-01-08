#データベースモデル作成用ファイル

from sqlalchemy import Column, ForeignKey, Integer, String

from .database import Base

#ユーザーのデータベースモデル
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True)
    password = Column(String)
    
#画像のデータベースモデル   
class User(Base):
    __tablename__ = "images"
   

    id = Column(Integer, primary_key=True, index=True)
    poster = Column(String)
    image_name = Column(String, unique=True)
    image_path = Column(String)
    title = Column(String)
    poster_comment = Column(String)
    good_num = Column(Integer)
    
    