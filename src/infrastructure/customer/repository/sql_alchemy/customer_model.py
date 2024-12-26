from sqlalchemy import Column, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class CustomerModel(Base):
    __tablename__ = 'customers'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    active = Column(Boolean, default=True)
    rewards_points = Column(Float, default=0)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
    country = Column(String, nullable=False)

    def __repr__(self):
        return f"<Product(id='{self.id}', name='{self.name}', price={self.price})>"