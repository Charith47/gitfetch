from providers.contributions_provider import ContributionsProvider

if __name__ == "__main__":
    cp = ContributionsProvider('queries/contributions.gql')
    cp.get_contrib_data()