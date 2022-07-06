import sys
from cli.graph import print_contrib_graph

from providers.contributions_provider import ContributionsProvider

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        username = sys.argv[1]
        contributions_provider = ContributionsProvider()
        result = contributions_provider.get_contrib_data(user_name=username)
        print_contrib_graph(result)
    else:
        print(f"Expected 1 arguement but got {len(sys.argv)-1}")
