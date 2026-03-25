from abc import ABC, abstractmethod
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# ІНТЕРФЕЙС
class IRepository(ABC):
    @abstractmethod
    def save_products(self, products): pass
    
    @abstractmethod
    def get_data_from_csv(self, path): pass

# РЕАЛІЗАЦІЯ (ORM)
class SqlAlchemyRepository(IRepository):
    def __init__(self, db_url="sqlite:///database.db"):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def save_products(self, products):
        session = self.Session()
        session.add_all(products)
        session.commit()
        session.close()

    def get_data_from_csv(self, path):
        return pd.read_csv(path).to_dict(orient='records')