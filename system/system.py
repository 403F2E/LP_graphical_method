from system.graphElement.elements import Line, Point

class System:
    """
    The system class representing the system in question

    represted with:
     - constraints : the values of the constraints
     - lines : the values of the lines of the constraints
     - minOrmax : the chosen objectif function
     - intersections: list of all the intersections to calculates the optimal point
    """
    def __init__(self) -> None:
        '''
        Initializing the system

        Args: 
            None
        '''
        self.__constraints: list[tuple[Point, str, float]] = []
        self.__isMax: bool = True
        self.__objectif_func: tuple[Point, str] = tuple()
        self.__lines: list[Line] = []
        self.__intersections: list[Point] = []

    ''' the getters of the private attributes '''
    @property
    def constraints(self) -> list[tuple[Point, str, float]]:
        return self.__constraints

    @property
    def minOrmax(self) -> bool:
        return self.__isMax

    @property
    def objectif_func(self) -> tuple[Point, str]:
        return self.__objectif_func

    @property
    def lines(self) -> list[Line]:
        return self.__lines

    @property
    def intersections(self) -> list[Point]:
        return self.__intersections

    ''' setters of the private attributes '''
    @constraints.setter
    def constraints(self, constraint: tuple[Point, str, float]) -> None:
        self.__constraints.append(constraint)

    @minOrmax.setter
    def minOrmax(self, choice: bool) -> None:
        self.__isMax = choice

    @objectif_func.setter
    def objectif_func(self, objectif_func: tuple[Point, str]) -> None:
        self.__objectif_func = objectif_func

    @lines.setter
    def lines(self, constraints: list[tuple[Point, str, float]]) -> None:
        point1: Point = Point(1, 0)
        point2: Point = Point(-1, 0)
        point3: Point = Point(0, 1)
        point4: Point = Point(0, -1)
        self.__lines.append(Line(point1, point2))
        self.__lines.append(Line(point3, point4))
        for constraint in constraints:
            x1, x2, y1, y2 = constraint[0].dox, constraint[0].dox, constraint[0].doy, constraint[0].doy
            if constraint[0].dox == 0:
                y1 = 1
                y2 = -1
            elif constraint[0].doy == 0:
                x1 = 1
                x2 = -1
            else:
                x1 = 0
                y1 = constraint[2] / constraint[0].doy
                x2 = constraint[2] / constraint[0].dox
                y2 = 0
            point1 = Point(x1, y1)
            point2 = Point(x2, y2)
            self.__lines.append(Line(point1, point2))

    @intersections.setter
    def intersections(self, lines: list[Line]) -> None:
        n_lines = len(lines)
        for i in range(n_lines):
            for j in range(i+1, n_lines):
                doesIntersect = lines[i] + lines[j]
                if not doesIntersect:
                    continue
                self.__intersections.append(doesIntersect)

    ''' the deconstructures of the private attributes '''
    @constraints.deleter
    def constraints(self) -> None:
        del self.__constraints

    @minOrmax.deleter
    def minOrmax(self) -> None:
        del self.__isMax

    @objectif_func.deleter
    def objectif_func(self) -> None:
        del self.__objectif_func

    @lines.deleter
    def lines(self) -> None:
        del self.__lines

    @intersections.deleter
    def intersections(self) -> None:
        del self.__intersections

    def comparePoints(self) -> list[Point]:
        optimal_points: list[Point] = []
        for intersection in self.__intersections:
            for constraint in self.__constraints:
                if self.__isMax:
                    if constraint[1] == "add" and (intersection + constraint[0]) <= constraint[2]:
                        optimal_points.append(intersection) 
                    elif constraint[1] == "sub" and (intersection - constraint[0]) <= constraint[2]:
                        optimal_points.append(intersection)
                else:
                    if constraint[1] == "add" and (intersection + constraint[0]) >= constraint[2]:
                        optimal_points.append(intersection) 
                    elif constraint[1] == "sub" and (intersection - constraint[0]) >= constraint[2]:
                        optimal_points.append(intersection)
        return optimal_points 

    def haveAnswer(self) -> Point:
        optimal_points: list[Point] = self.comparePoints()
        print(optimal_points)
        optimal_point: Point = optimal_points[0]
        possibility: float = optimal_point + self.__objectif_func[0]
        if self.__isMax:
            for point in optimal_points:
                if self.__objectif_func[1] == "add":
                    possible_point: float = point + self.__objectif_func[0]
                    if possible_point > possibility:
                        optimal_point = point
                elif self.__objectif_func[1] == "sub":
                    possible_point: float = point - self.__objectif_func[0]
                    if possible_point > possibility:
                        optimal_point = point
        else:
            for point in optimal_points:
                if self.__objectif_func[1] == "add":
                    possible_point: float = point + self.__objectif_func[0]
                    if possible_point < possibility:
                        optimal_point = point
                elif self.__objectif_func[1] == "sub":
                    possible_point: float = point - self.__objectif_func[0]
                    if possible_point < possibility:
                        optimal_point = point

        return optimal_point
