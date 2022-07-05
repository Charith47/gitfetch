import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests

def run_gql_query(uri, query, variables, headers):
    try:
        request = requests.post(
            uri, json={'query': query, 'variables': variables}, headers=headers)
        if request.status_code == 200:
            return [request.json(), None]
        else:
            raise Exception(
                f"request failed with status code {request.status_code}")
    except Exception as e:
        print(f"Error: {e}")
        return [None, e]


if __name__ == "__main__":
    pass
