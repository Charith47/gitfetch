from rich.console import Console
console = Console()

#TODO: create a class
def print_raw_data(data):
    raw_data = parse_data(data)
    console.print(raw_data)


def print_contrib_graph(data):
    raw_data = parse_data(data)
    for key, value in raw_data.items():
        for day in value:
            # TODO: categorize range -> colors
            console.print("■ ", style=f"rgb(0,{day*15},0)", end="")
        console.print('\n')


def parse_data(data):
    cum_day_data = {
        "0": [],
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": [],
        "6": [],
    }

    weeks = data['user']['contributionsCollection']['contributionCalendar']['weeks']
    for days in weeks:
        for day in range(len(days['contributionDays'])):
            cum_day_data[str(day)].append(
                days['contributionDays'][day]['contributionCount'])
    return cum_day_data
