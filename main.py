from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging
from typing import List
from models import *
from db import db, users, items, orders


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    logger.info('Starting up')

    yield

    await db.disconnect()
    logger.info('Shutting down')


app = FastAPI(lifespan=lifespan)


# Users
@app.get('/users/', response_model=List[UserOut])
async def read_users():
    logger.info('Отработал GET запрос для всех пользователей')
    query = users.select()
    return await db.fetch_all(query)


@app.get('/users/{user_id}', response_model=UserOut)
async def read_user_by_id(user_id: int):
    logger.info(f'Отработал GET запрос для пользователя с id {user_id}')
    query = users.select().where(users.c.user_id == user_id)
    return await db.fetch_one(query)


@app.post('/users/', response_model=UserOut)
async def create_user(new_user: User):
    logger.info('Отработал POST запрос для создания нового пользователя')
    query = users.insert().values(**new_user.dict())
    last_record_id = await db.execute(query)
    return {**new_user.dict(), 'user_id': last_record_id}


@app.put('/users/{user_id}', response_model=UserOut)
async def update_user_by_id(user_id: int, updated_user: User):
    logger.info(f'Отработал PUT запрос для пользователя с id {user_id}')
    query = (users.update().where(users.c.user_id == user_id).
             values(**updated_user.dict()))
    await db.execute(query)
    return {**updated_user.dict(), 'user_id': user_id}


@app.delete('/users/{user_id}')
async def delete_user_by_id(user_id: int):
    logger.info(f'Отработал DELETE запрос для пользователя с id {user_id}')
    query = users.delete().where(users.c.user_id == user_id)
    await db.execute(query)
    return {'message': 'User has been deleted'}


# Items
@app.get('/items/', response_model=List[ItemOut])
async def read_items():
    logger.info('Отработал GET запрос для всех товаров')
    query = items.select()
    return await db.fetch_all(query)


@app.get('/items/{item_id}', response_model=ItemOut)
async def read_item_by_id(item_id: int):
    logger.info(f'Отработал GET запрос для товара с id {item_id}')
    query = items.select().where(items.c.item_id == item_id)
    return await db.fetch_one(query)


@app.post('/items/', response_model=ItemOut)
async def create_item(new_item: Item):
    logger.info('Отработал POST запрос для создания нового товара')
    query = items.insert().values(**new_item.dict())
    last_record_id = await db.execute(query)
    return {**new_item.dict(), 'item_id': last_record_id}


@app.put('/items/{item_id}', response_model=ItemOut)
async def update_item_by_id(item_id: int, updated_item: Item):
    logger.info(f'Отработал PUT запрос для товара с id {item_id}')
    query = (items.update().where(items.c.item_id == item_id).
             values(**updated_item.dict()))
    await db.execute(query)
    return {**updated_item.dict(), 'item_id': item_id}


@app.delete('/items/{item_id}')
async def delete_item_by_id(item_id: int):
    logger.info(f'Отработал DELETE запрос для товара с id {item_id}')
    query = items.delete().where(items.c.item_id == item_id)
    await db.execute(query)
    return {'message': 'Item has been deleted'}


@app.get('/orders/', response_model=List[OrderOut])
async def read_orders():
    logger.info('Отработал GET запрос для всех заказов')
    query = orders.select()
    return await db.fetch_all(query)


@app.get('/orders/{order_id}', response_model=OrderOut)
async def read_order_by_id(order_id: int):
    logger.info(f'Отработал GET запрос для заказа с id {order_id}')
    query = orders.select().where(orders.c.order_id == order_id)
    return await db.fetch_one(query)


@app.get('/orders/user/{user_id}', response_model=List[OrderOut])
async def read_orders_by_user_id(user_id: int):
    logger.info(f'Отработал GET запрос для заказов пользователя с id {user_id}')
    query = orders.select().where(orders.c.user_id == user_id)
    return await db.fetch_all(query)


@app.post('/orders/', response_model=OrderOut)
async def create_order(new_order: Order):
    logger.info('Отработал POST запрос для создания нового заказа')
    query = orders.insert().values(**new_order.dict())
    last_record_id = await db.execute(query)
    return {**new_order.dict(), 'order_id': last_record_id}


@app.put('/orders/{order_id}', response_model=OrderOut)
async def update_order_by_id(order_id: int, updated_order: Order):
    logger.info(f'Отработал PUT запрос для заказа с id {order_id}')
    query = (orders.update().where(orders.c.order_id == order_id).
             values(**updated_order.dict()))
    await db.execute(query)
    return {**updated_order.dict(), 'order_id': order_id}


@app.delete('/orders/{order_id}')
async def delete_order_by_id(order_id: int):
    logger.info(f'Отработал DELETE запрос для заказа с id {order_id}')
    query = orders.delete().where(orders.c.order_id == order_id)
    await db.execute(query)
    return {'message': 'Order has been deleted'}
