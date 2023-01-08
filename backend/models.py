from sqlalchemy import Column, ForeignKey, Integer, String

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True)
    password = Column(String)
    #ユーザーごとに表を参照したい
    #動的に表を参照できるようにする
    
class User(Base):
    __tablename__ = "images"
    #ユーザーごとにテーブルを作成したい
    #テーブル名を動的に設定できるようにする

    id = Column(Integer, primary_key=True, index=True)
    poster = Column(String)
    image_name = Column(String, unique=True)
    image_path = Column(String)
    title = Column(String)
    poster_comment = Column(String)
    good_num = Column(Integer)
    #reader_comment = relationship('reader_comment')
    