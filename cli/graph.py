from rich.console import Console


class Graph:
    def __init__(self, data) -> None:
        self.__console = Console()
        self.__max_contributions = 0
        self.__range_set = [0, 25, 30, 40, 50, 100, 150, 200, 250]
        self.__color_offset = 5
        self.__data = self.__parse_data(data)

    def __parse_data(self, data) -> "dict[str,list]":
        all_day_data = {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": []}
        weeks = data["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
        for week in weeks:
            for day in range(len(week["contributionDays"])):
                count = week["contributionDays"][day]["contributionCount"]
                all_day_data[str(day)].append(count)

                if count > self.__max_contributions:
                    self.__max_contributions = count
        return all_day_data

    # https://stackoverflow.com/a/5732390
    # linear mapping
    # parabolic mapping would be better
    def __map_linear(self, input_min, input_max, output_min, output_max, input_value):
        return output_min + ((output_max - output_min) / (input_max - input_min)) * (
            input_value - input_min
        )

    # https://www.desmos.com/calculator/ewnq4hyrbz
    def __map_parabolic(
        self, input_min, input_max, output_min, output_max, input_value
    ):
        return (
            ((output_min - output_max) * ((input_value - input_max) ** 2))
            / ((input_max - input_min) ** 2)
        ) + output_max

    # https://stackoverflow.com/a/42485216
    # rounds value to closes boundary in the given list
    def __to_closest(self, input_value):
        return min(self.__range_set, key=lambda boundary: abs(boundary - input_value))

    def print_graph(self) -> None:
        # TODO refactor vars
        for key, all_day in self.__data.items():
            for per_day in all_day:
                mapped = self.__to_closest(
                    self.__map_parabolic(0, self.__max_contributions, 0, 250, per_day)
                )
                # TODO print a single string
                self.__console.print(
                    "■ ", style=f"rgb(0,{mapped+self.__color_offset},0)", end=""
                )
            self.__console.print("")

    def print_raw(self) -> None:
        self.__console.print(self.__data)
