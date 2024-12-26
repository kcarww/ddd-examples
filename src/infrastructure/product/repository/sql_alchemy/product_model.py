from sqlalchemy import Column, String, Float
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Product(id='{self.id}', name='{self.name}', price={self.price})>"