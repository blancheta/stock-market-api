import os
import pytest

from app import create_app
from app.order.models import User, db
from config import TestingConfig


def app_mock():
    return create_app(TestingConfig)


@pytest.fixture(scope="class")
def drop_db():
    yield

    with app_mock().app_context():
        os.remove("app-test.db")


@pytest.fixture(autouse=True)
def drop_data():
    # execute the test
    yield

    # clean up / reset resources here
    with app_mock().app_context():
        db.session.remove()
        db.drop_all()


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

        return db.session.query(User).filter_by(name="111").first()
