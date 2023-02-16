from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, select
from sqlalchemy.orm import Mapped, Session, declarative_base, relationship

from starlite.plugins.sql_alchemy import SQLAlchemyConfig, SQLAlchemyPlugin

engine = create_engine("sqlite+pysqlite:///test.sqlite")
sqlalchemy_config = SQLAlchemyConfig(engine_instance=engine, use_async_engine=False)
sqlalchemy_plugin = SQLAlchemyPlugin(config=sqlalchemy_config)

Base = declarative_base()