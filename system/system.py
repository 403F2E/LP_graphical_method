from graphElement.elements import Line

class System:
    def __init__(self) -> None:
        self.__lines: list[Line] = []
        self.__constraints: list[tuple[int]] = []
        self.__minOrmax: bool = True

    @property
    def get_lines(self) -> list[Line]:
        return self.__lines

    @property
    def get_constraints(self) -> list[tuple[int]]:
        return self.__constraints

    @property
    def get_minOrmax(self) -> bool:
        return self.__minOrmax

    @get_lines.setter
    def set_line(self, line: Line) -> None:
        self.__lines.append(line);

    @get_constraints.setter
    def set_constraints(self, constraint: tuple[int]) -> None:
        self.__constraints.append(constraint)

    @get_minOrmax.setter
    def set_minOrmax(self, choice: bool) -> None:
        self.__minOrmax = choice

    @get_lines.deleter
    def del_lines(self) -> None:
        del self.__lines

    @get_lines.deleter
    def del_constraints(self) -> None:
        del self.__constraints

    @get_minOrmax.deleter
    def del_minOrmax(self) -> None:
        del self.__minOrmax
