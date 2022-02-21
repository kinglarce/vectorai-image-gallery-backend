import databases
import sqlalchemy
from starlette.config import Config

config = Config("../.env")
DATABASE_URL = config('DATABASE_URL')
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Table definitions
Bank = sqlalchemy.Table(
    "bank",
    metadata,
    sqlalchemy.Column("_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("bank_type", sqlalchemy.String),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("position", sqlalchemy.Integer),
    sqlalchemy.Column("image", sqlalchemy.String),
)
