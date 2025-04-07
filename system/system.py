from graphElement.elements import Line, Point

class System:
    """
    The system class representing the system in question

    represted with:
     - constraints : the values of the constraints
     - lines : the values of the lines of the constraints
     - minOrmax : the chosen objectif function
     - optimal_points: list of all the intersections to calculates the optimal point
    """
    def __init__(self) -> None:
        '''
        Initializing the system

        Args: 
            None
        '''
        self.__constraints: list[tuple[Point, float]] = []
        self.__minOrmax: bool = True
        self.__lines: list[Line] = []
        self.__optimal_points: list[Point] = []

    ''' the getters of the private attributes '''
    @property
    def get_constraints(self) -> list[tuple[Point, float]]:
        return self.__constraints

    @property
    def get_minOrmax(self) -> bool:
        return self.__minOrmax

    @property
    def get_lines(self) -> list[Line]:
        return self.__lines

    @property
    def get_optimal_points(self) -> list[Point]:
        return self.__optimal_points


    ''' setters of the private attributes '''
    @get_constraints.setter
    def set_constraints(self, constraint: tuple[Point, float]) -> None:
        self.__constraints.append(constraint)

    @get_minOrmax.setter
    def set_minOrmax(self, choice: bool) -> None:
        self.__minOrmax = choice

    @get_lines.setter
    def set_line(self) -> None:
        for constraint in self.__constraints:
            pass


    @get_optimal_points.setter
    def set_optimal_points(self) -> None:
        n_lines = len(self.__lines)
        for i in range(n_lines):
            for j in range(i+1, n_lines):
                doesIntersect = self.__lines[i] + self.__lines[j]
                if not doesIntersect:
                    continue
                self.__optimal_points.append(Point(doesIntersect[0], doesIntersect[1]))

    ''' the deconstructures of the private attributes '''
    @get_lines.deleter
    def del_constraints(self) -> None:
        del self.__constraints

    @get_minOrmax.deleter
    def del_minOrmax(self) -> None:
        del self.__minOrmax

    @get_lines.deleter
    def del_lines(self) -> None:
        del self.__lines

    @get_optimal_points.deleter
    def del_optimal_points(self) -> None:
        del self.__optimal_points
