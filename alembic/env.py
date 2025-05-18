from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from database import Base  # import the Base from your database file
from models import User, Product  # import your models

# this is the Alembic Config object, which provides
# access to the .ini file configuration
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# Add your models' MetaData object here
# for 'autogenerate' support
target_metadata = Base.metadata

def run_migrations_online():
    # Configure the database connection
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()
