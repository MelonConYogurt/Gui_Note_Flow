from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///BaseDeDatosTokens.db', echo=True)
Base = declarative_base()

class UserTokens(Base):
    __tablename__ = 'Tokens'
    
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Token = Column(String(500), nullable=False, unique=True)
    Token_Created_at = Column(DateTime(), default=datetime.now())

Session = sessionmaker(bind=engine)
session1 = Session()

if __name__ == '__main__':
    Base.metadata.create_all(engine)