from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(String, primary_key=True)
    customer_id = Column(String, ForeignKey("customers.id"), nullable=False)
    total = Column(Float, nullable=False)

    customer = relationship("CustomerModel", back_populates="orders")

    items = relationship("OrderItemModel", back_populates="order", cascade="all, delete-orphan")

