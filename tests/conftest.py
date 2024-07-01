import os
from contextlib import contextmanager

import pytest
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from app.order.models import User, db
from config import TestingConfig


def app_mock():
    return create_app(TestingConfig)


@pytest.fixture(autouse=True)
def db_drop():
    # execute the test
    yield

    # clean up / reset resources here
    with app_mock().app_context():
        db.session.remove()
        db.drop_all()
        os.remove("app-test.db")


@pytest.fixture()
def client():
    return app_mock().test_client()


@pytest.fixture()
def runner():
    return app_mock().test_cli_runner()


@pytest.fixture()
def new_user():
    with app_mock().app_context():
        db.session.add(User(name="111"))
        db.session.commit()

        return db.session.query(User).first()