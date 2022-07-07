from util.query import Query

class ContributionsProvider(Query):
    def __init__(self):
        query_path = 'graphql/contributions.gql'
        super().__init__(query_path)

    def get_contrib_data(self, user_name):
        result = super()._execute({'userName': user_name})
        return result