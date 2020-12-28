from .. import DeclarativeBase, engine
from ...settings import envs


class Bootloader:

    def __init__(self, *tables: str):
        self.setup(*tables)

    @classmethod
    def setup(cls, *tables: str):
        if envs.DATABASE_RESET:
            DeclarativeBase.metadata.drop_all(engine)

        if tables:
            table_objects = [DeclarativeBase.metadata.tables[table_name] for table_name in tables]
        else:
            table_objects = None

        DeclarativeBase.metadata.create_all(engine, tables=table_objects)
