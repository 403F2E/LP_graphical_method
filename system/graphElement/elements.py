
class Point:
    '''
    This the class representing the point unit in the graphical method

    Identifys with 2 values:
     - x : axis value of the point
     - y : axis value of the point
    '''
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.__x: float = x
        self.__y: float = y

    ''' getters of the private coords of the point '''
    @property
    def dox(self) -> float:
        return self.__x

    @property
    def doy(self) -> float:
        return self.__y

    ''' setters of the coords of the point '''
    @dox.setter
    def dox(self, pos: float) -> None:
        self.__x = pos

    @doy.setter
    def doy(self, pos: float) -> None:
        self.__y = pos

    ''' deconstructures of the coords of the point '''
    @dox.deleter
    def dox(self) -> None:
        del self.__x

    @doy.deleter
    def doy(self) -> None:
        del self.__y

    def __add__(self, other: "Point") -> float:
        return self.__x * other.dox + self.__y * other.doy

    def __sub__(self, other: "Point") -> float:
        return self.__x * other.dox - self.__y * other.doy

    def __repr__(self) -> str:
        return f'({self.dox}, {self.doy})'

class Line:
    '''
    This the class representing the line unit in the graphical method

    Identifys with 2 points:
     - point1 : low point at the graph
     - point2 : high point at the graph
    '''
    def __init__(self, point1: Point = Point(0, 0), point2: Point = Point(0, 0)) -> None:
        self.__point1: Point = point1
        self.__point2: Point = point2

    ''' getters of the points of the line '''
    @property
    def first_point(self) -> tuple[float, float]:
        return (self.__point1.dox, self.__point1.doy)

    @property
    def second_point(self) -> tuple[float, float]:
        return (self.__point2.dox, self.__point2.doy)

    '''setters of the points of the line '''
    @first_point.setter
    def first_point(self, point: Point) -> None:
        self.__point1.dox = point.dox
        self.__point1.doy = point.doy

    @second_point.setter
    def second_point(self, point: Point) -> None:
        self.__point2.dox = point.dox
        self.__point2.doy = point.doy

    ''' deconstructures of the points '''
    @first_point.deleter
    def first_point(self):
        del self.__point1
        del self.__point2

    def __add__(self, other: "Line") -> Point | None:
        '''

        Calculating the intersection between 2 lines according to their points of reference

        we need 2 lines with 2 points of reference to calculate the intersection

        Args : 

        self : the first line 
        other : the second line

        Return : 

        either a tuple with 2 floats representing the point of intersection
        either the None if there is none
        '''
        # get the coords of the first line
        p1: tuple[float, float] = self.first_point
        p2: tuple[float, float] = self.second_point

        # get the coords of the second line
        p3: tuple[float, float] = other.first_point
        p4: tuple[float, float] = other.second_point

        # Line 1 vector
        A1: float = p2[1] - p1[1]
        B1: float = p1[0] - p2[0]
        C1: float = A1 * p1[0] + B1 * p1[1]

        # Line 2 vector
        A2: float = p4[1] - p3[1]
        B2: float = p3[0] - p4[0]
        C2: float = A2 * p3[0] + B2 * p3[1]

        # Determinant
        det: float = A1 * B2 - A2 * B1

        if det == 0:
            return None  # Lines are parallel or coincident

        x: float = (C1 * B2 - C2 * B1) / det
        y: float = (A1 * C2 - A2 * C1) / det

        return Point(x, y)

    def __repr__(self) -> str:
        return f"({self.first_point}), ({self.second_point})"
