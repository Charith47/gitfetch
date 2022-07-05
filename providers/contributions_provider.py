from util.query import Query

class ContributionsProvider(Query):
    def __init__(self, query_path):
        super().__init__(query_path)

    def get_contrib_data(self):
        result = super()._execute({'userName': 'charith47'})
        print(result)