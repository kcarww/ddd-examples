from sqlalchemy import Column, String, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class OrderItemModel(Base):
    __tablename__ = "order_items"

    id = Column(String, primary_key=True)

    product_id = Column(String, ForeignKey("products.id"), nullable=False)
    product = relationship("ProductModel", back_populates="order_items")

    order_id = Column(String, ForeignKey("orders.id"), nullable=False)
    order = relationship("OrderModel", back_populates="items")

    quantity = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)