from abc import ABC

from os.path import join, dirname
from dotenv import dotenv_values

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.exceptions import TransportQueryError


class Query(ABC):
    def __init__(self, query_path):
        path = join(dirname(dirname(__file__)), '.env')
        env = dotenv_values(path)
        headers = {"Authorization": f"Bearer {env['GH_PAT']}"}
        transport = AIOHTTPTransport(url=env['GH_ENDPOINT'], headers=headers)
        self._client = Client(transport=transport)
        self._query = self.__load_query(query_path=query_path)

    def __load_query(self, query_path):
        with open(join(dirname(dirname(__file__)), query_path)) as file:
           return gql(file.read())

    def _execute(self, variable_values):
        try:
            return self._client.execute(self._query, variable_values=variable_values)
        except Exception as e:
            print(e)
