"""Helper objects to improve modularity of tests."""
from flask import Flask
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, mapped_column

from fuisce.database import SQLAlchemy


def create_test_app(test_config):
    # Create and configure the test app
    app = Flask("test")
    app.config.from_object(test_config)
    init_app(app)
    return app


@SQLAlchemy.interface_selector
def init_app(app):
    # Initialize the app
    # * The decorator performs all necessary actions in this minimal test example
    pass


class Base(DeclarativeBase):
    metadata = SQLAlchemy.metadata


class Entry(Base):
    __tablename__ = "entries"
    # Columns
    x = mapped_column(Integer, primary_key=True)
    y = mapped_column(String, nullable=False)
    user_id = mapped_column(Integer, nullable=False)
