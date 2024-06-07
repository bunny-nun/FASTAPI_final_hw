import databases
import sqlalchemy
from datetime import datetime

DATABASE_URL = "sqlite:///mydatabase.db"
db = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column(
        'user_id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        'user_name', sqlalchemy.String(30), nullable=False),
    sqlalchemy.Column(
        'user_last_name', sqlalchemy.String(30), nullable=False),
    sqlalchemy.Column(
        'user_email', sqlalchemy.String(128), nullable=False),
    sqlalchemy.Column(
        'password', sqlalchemy.String(128), nullable=False),
)

items = sqlalchemy.Table(
    'items',
    metadata,
    sqlalchemy.Column(
        'item_id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        'item_name', sqlalchemy.String(30), nullable=False),
    sqlalchemy.Column(
        'item_description', sqlalchemy.Text(500), nullable=True),
    sqlalchemy.Column(
        'item_price', sqlalchemy.Float(), nullable=False),
)

order_statuses = sqlalchemy.Table(
    'order_statuses',
    metadata,
    sqlalchemy.Column(
        'status_id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        'status_description', sqlalchemy.String(30), nullable=False),
)

orders = sqlalchemy.Table(
    'orders',
    metadata,
    sqlalchemy.Column(
        'order_id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        'user_id', sqlalchemy.Integer,
        sqlalchemy.ForeignKey('users.user_id',
                              onupdate='CASCADE', ondelete='CASCADE')),
    sqlalchemy.Column(
        'item_id', sqlalchemy.Integer,
        sqlalchemy.ForeignKey('items.item_id',
                              onupdate='CASCADE', ondelete='CASCADE')),
    sqlalchemy.Column(
        'order_date', sqlalchemy.DateTime, default=datetime.now),
    sqlalchemy.Column(
        'order_status_id', sqlalchemy.Integer,
        sqlalchemy.ForeignKey('order_statuses.status_id'), default=1),
)

if __name__ == '__main__':
    engine = sqlalchemy.create_engine(
        DATABASE_URL, connect_args={'check_same_thread': False})
    metadata.create_all(engine)
