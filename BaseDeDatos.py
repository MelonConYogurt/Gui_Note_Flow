from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Cambia la URL de conexión al servidor MySQL en red
db_url = 'mysql+mysqlconnector://root:alecontra1313@localhost/usuarios'

engine = create_engine(db_url, echo=True)
Base = declarative_base()

class User_values(Base):
    __tablename__ = 'users'
    
    Id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(200), nullable=False, unique=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=True, unique=True)
    genero = Column(String(100), nullable=True, unique=False)
    ocupacion = Column(String(100), nullable=True, unique=False)
    created_at = Column(DateTime(), default=datetime.now())

Session = sessionmaker(bind=engine)
session_user_values = Session()

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    

"""from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Cambiar la cadena de conexión a PostgreSQL
DATABASE_URL = DATABASE_URL = 'postgresql://postgres:dU:!h9Azp.ZAq7Q@localhost:5432/usuarios'

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    Id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(200), nullable=False, unique=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=True, unique=True)
    genero = Column(String(100), nullable=True, unique=False)
    ocupacion = Column(String(100), nullable=True, unique=False)
    created_at = Column(DateTime(), default=datetime.now())

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    Base.metadata.create_all(engine)"""
    


"""from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///BaseDeDatosApp.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    Id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(200), nullable=False, unique=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=True, unique=True)  # Agregar nueva columna
    genero = Column(String(100), nullable=True, unique=False)
    ocupacion = Column(String(100), nullable=True, unique=False)
    created_at = Column(DateTime(), default=datetime.now())

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    Base.metadata.create_all(engine)"""