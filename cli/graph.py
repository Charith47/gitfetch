from rich.console import Console


class Graph:
    def __init__(self, data) -> None:
        self.__data = self.__parse_data(data)
        self.__console = Console()

    def __parse_data(self, data) -> "dict[str,list]":
        all_day_data = {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": []}
        weeks = data["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
        for days in weeks:
            for day in range(len(days["contributionDays"])):
                all_day_data[str(day)].append(
                    days["contributionDays"][day]["contributionCount"]
                )

        return all_day_data

    def print_graph(self) -> None:
        for key, value in self.__data.items():
            for day in value:
                # TODO: categorize range -> colors
                self.__console.print("■ ", style=f"rgb(0,{day*15},0)", end="")
            self.__console.print("\n")

    def print_raw(self) -> None:
        self.__console.print(self.__data)
