from graphElement.elements import Line, Point

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
    def get_constraints(self) -> list[tuple[Point, str, float]]:
        return self.__constraints

    @property
    def get_minOrmax(self) -> bool:
        return self.__isMax

    @property
    def get_objectif_func(self) -> tuple[Point, str]:
        return self.__objectif_func

    @property
    def get_lines(self) -> list[Line]:
        return self.__lines

    @property
    def get_intersections(self) -> list[Point]:
        return self.__intersections

    ''' setters of the private attributes '''
    @get_constraints.setter
    def set_constraints(self, constraint: tuple[Point, str, float]) -> None:
        self.__constraints.append(constraint)

    @get_minOrmax.setter
    def set_minOrmax(self, choice: bool) -> None:
        self.__isMax = choice

    @get_objectif_func.setter
    def set_objectif_func(self, objectif_func: tuple[Point, str]) -> None:
        self.__objectif_func = objectif_func

    @get_lines.setter
    def set_line(self) -> None:
        point1: Point = Point(123473411413, 0)
        point2: Point = Point(-123473411413, 0)
        point3: Point = Point(0, 123473411413)
        point4: Point = Point(0, -123473411413)
        self.__lines.append(Line(point1, point2))
        self.__lines.append(Line(point3, point4))
        for constraint in self.__constraints:
            point1 = Point(constraint[0].getx + constraint[2], constraint[0].gety)
            point2 = Point(constraint[0].getx, constraint[0].gety + constraint[2])
            self.__lines.append(Line(point1, point2))

    @get_intersections.setter
    def set_intersections(self) -> None:
        n_lines = len(self.__lines)
        for i in range(n_lines):
            for j in range(i+1, n_lines):
                doesIntersect = self.__lines[i] + self.__lines[j]
                if not doesIntersect:
                    continue
                self.__intersections.append(Point(doesIntersect[0], doesIntersect[1]))

    ''' the deconstructures of the private attributes '''
    @get_lines.deleter
    def del_constraints(self) -> None:
        del self.__constraints

    @get_minOrmax.deleter
    def del_minOrmax(self) -> None:
        del self.__isMax

    @get_objectif_func.deleter
    def del_objectif_func(self) -> None:
        del self.__objectif_func

    @get_lines.deleter
    def del_lines(self) -> None:
        del self.__lines

    @get_intersections.deleter
    def del_intersections(self) -> None:
        del self.__intersections

    def comparePoints(self) -> list[Point]:
        optimal_points: list[Point] = []
        for intersection in self.__intersections:
            for constraint in self.__constraints:
                if constraint[1] == "add" and (intersection + constraint[0]) == constraint[2]:
                    optimal_points.append(intersection) 
                elif constraint[1] == "sub" and (intersection - constraint[0]) == constraint[2]:
                    optimal_points.append(intersection)
        return optimal_points 

    def haveAnswer(self) -> Point:
        optimal_points: list[Point] = self.comparePoints()
        optimal_point: Point = optimal_points[1]
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
