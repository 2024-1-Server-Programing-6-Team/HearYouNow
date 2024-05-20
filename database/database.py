import sys
import pymysql

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine, text


engine = create_engine('mysql+pymysql://root:root@localhost') # mysql 접속
with engine.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS HearYouNow")) # database가 없으면 생성
    
engine = create_engine('mysql+pymysql://root:root@localhost/HearYouNow') # database를 연결


HearYouNow_DB = declarative_base() # database 선언

class USER(HearYouNow_DB):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    password = Column(String(32), nullable=False) # password text to hash (with hashtable : SHA-256)
    email = Column(String(32), nullable=False)
    age = Column(Integer, default=-1)

class BOARD(HearYouNow_DB):
    __tablename__ = 'board'
    
    board_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class POST(HearYouNow_DB):
    __tablename__ = 'post'

    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user = relationship(USER)
    board_id = Column(Integer, ForeignKey('board.board_id'))
    board = relationship(BOARD)
    title = Column(String(250), nullable=False)
    content = Column(String(250), nullable=True)
    created_at = Column(String(250), nullable=False)
    
class POSTLIKE(HearYouNow_DB):
    __tablename__ = 'post_like'
    
    post_like_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user = relationship(USER)
    post_id = Column(Integer, ForeignKey('post.post_id'))
    post = relationship(POST)
    created_at = Column(String(250), nullable=False)
    
class COMMENT(HearYouNow_DB):
    __tablename__ = 'comment'
    
    comment_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user = relationship(USER)
    post_id = Column(Integer, ForeignKey('post.post_id'))
    post = relationship(POST)
    content = Column(String(250), nullable=False)
    created_at = Column(String(250), nullable=False)
    
class COMMENTLIKE(HearYouNow_DB):
    __tablename__ = 'comment_like'
    
    comment_like_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user = relationship(USER)
    comment_id = Column(Integer, ForeignKey('comment.comment_id'))
    comment = relationship(POST)
    created_at = Column(String(250), nullable=False)
    
class ANXIETYMARK(HearYouNow_DB):
    __tablename__ = 'anxiety_mark'
    
    anxiety_mark_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user = relationship(USER)
    post_id = Column(Integer, ForeignKey('post.post_id'))
    post = relationship(POST)
    created_at = Column(String(250), nullable=False)

class EXPERTAGENCY(HearYouNow_DB):
    __tablename__ = 'expert_agency'
    
    agency_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    phone_number = Column(Integer, primary_key=False)
    target_audience = Column(String(250), nullable=False)

##### insert at end of file #####

HearYouNow_DB.metadata.create_all(engine)
