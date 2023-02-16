from sqlalchemy import  create_engine
from sqlalchemy.orm import  declarative_base

from starlite.plugins.sql_alchemy import SQLAlchemyConfig, SQLAlchemyPlugin

engine = create_engine("sqlite+pysqlite:///test.sqlite")
sqlalchemy_config = SQLAlchemyConfig(engine_instance=engine, use_async_engine=False)
sqlalchemy_plugin = SQLAlchemyPlugin(config=sqlalchemy_config)

Base = declarative_base()