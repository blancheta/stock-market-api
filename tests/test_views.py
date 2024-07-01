import pytest

from app import db

@pytest.mark.usefixtures("drop_db")
class TestViews:

    def test_request_example(self, client, new_user):
        print("run test ...")
        response = client.get("/health")
        assert {"status": "ok"} == response.get_json()
