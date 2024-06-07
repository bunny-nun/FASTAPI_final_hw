from pydantic import BaseModel, Field
from datetime import datetime


class User(BaseModel):
    user_name: str = Field(min_length=1, max_length=30)
    user_last_name: str = Field(min_length=1, max_length=30)
    user_email: str = Field(max_length=128)
    password: str = Field(max_length=128)


class UserOut(BaseModel):
    user_id: int
    user_name: str = Field(min_length=1, max_length=30)
    user_last_name: str = Field(min_length=1, max_length=30)
    user_email: str = Field(max_length=128)
    password: str = Field(max_length=128)


class Item(BaseModel):
    item_name: str = Field(min_length=1, max_length=30)
    item_description: str = Field(min_length=1, max_length=500)
    item_price: float = Field()


class ItemOut(BaseModel):
    item_id: int
    item_name: str = Field(min_length=1, max_length=30)
    item_description: str = Field(min_length=1, max_length=500)
    item_price: float = Field()


class OrderStatus(BaseModel):
    status_id: int
    status_description: str = Field(max_length=30)


class Order(BaseModel):
    user_id: int
    item_id: int
    order_date: datetime = Field(default=datetime.now)
    order_status_id: int = Field(default=1)


class OrderOut(BaseModel):
    order_id: int
    user_id: int
    item_id: int
    order_date: datetime = Field()
    order_status_id: int = Field()

