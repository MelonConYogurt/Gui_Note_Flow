from sqlalchemy import Column, Integer, String, create_engine, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///BaseDeDatosApp.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'Valores'
    
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Titulo_frame = Column(String(200), nullable=False, unique=False)
    Tarea1_frame = Column(String(200), nullable=False, unique=False)
    Tarea2_frame = Column(String(200), nullable=False, unique=False)
    Tarea3_frame = Column(String(200), nullable=False, unique=False)
    Tarea4_frame = Column(String(200), nullable=False, unique=False)
    Tarea5_frame = Column(String(200), nullable=False, unique=False)
    Tarea1_estado = Column(String(200), nullable=False, unique=False)
    Tarea2_estado = Column(String(200), nullable=False, unique=False)
    Tarea3_estado = Column(String(200), nullable=False, unique=False)
    Tarea4_estado = Column(String(200), nullable=False, unique=False)
    Tarea5_estado = Column(String(200), nullable=False, unique=False)
    Fila_frame = Column(Integer, nullable=False)
    Columna_frame = Column(Integer, nullable=True, unique=False)  # Agregar nueva columna
    created_at = Column(DateTime(), default=datetime.now())

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    Base.metadata.create_all(engine)