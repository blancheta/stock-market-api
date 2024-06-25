import json


class TestViews:

    def test_request_example(self, client):
        response = client.get("/health")
        print(response.data)
        assert {"status": "ok"} == response.get_json()
