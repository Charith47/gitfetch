import sys
from cli.graph import Graph

from providers.contributions_provider import ContributionsProvider

if __name__ == "__main__":
    if len(sys.argv) == 2:
        username = sys.argv[1]

        contributions_provider = ContributionsProvider()
        data = contributions_provider.get_contrib_data(user_name=username)

        graph = Graph(data)
        graph.print_graph()
    else:
        print(f"Expected 1 arguement but got {len(sys.argv)-1}")
