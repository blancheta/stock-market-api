import pytest

from app import db


class TestViews:

    def test_request_example(self, client, new_user):
        print("test_request_example")
        print(new_user)
        response = client.get("/health")
        print(response.data)
        assert {"status": "ok"} == response.get_json()
