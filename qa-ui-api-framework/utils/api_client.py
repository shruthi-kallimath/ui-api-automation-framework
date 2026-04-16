import requests


class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, endpoint: str, params=None, headers=None):
        return requests.get(f"{self.base_url}{endpoint}", params=params, headers=headers)

    def post(self, endpoint: str, json=None, headers=None):
        return requests.post(f"{self.base_url}{endpoint}", json=json, headers=headers)

    def put(self, endpoint: str, json=None, headers=None):
        return requests.put(f"{self.base_url}{endpoint}", json=json, headers=headers)

    def delete(self, endpoint: str, headers=None):
        return requests.delete(f"{self.base_url}{endpoint}", headers=headers)
    
    