
class Point:
    '''
    This the class representing the point unit in the graphical method

    Identifys with 2 values:
     - x : axis value of the point
     - y : axis value of the point
    '''
    def __init__(self) -> None:
        self.__x: float = 0
        self.__y: float = 0

    @property
    def getx(self) -> float:
        return self.__x

    @property
    def gety(self) -> float:
        return self.__y

    @getx.setter
    def setX(self, pos: float) -> None:
        self.__x = pos

    @gety.setter
    def setY(self, pos: float) -> None:
        self.__y = pos

    @getx.deleter
    def delX(self) -> None:
        del self.__x

    @gety.deleter
    def delY(self) -> None:
        del self.__y

class Line:
    '''
    This the class representing the line unit in the graphical method

    Identifys with 2 points:
     - point1 : low point at the graph
     - point2 : high point at the graph
    '''
    def __init__(self) -> None:
        self.__point1: Point = Point()
        self.__point2: Point = Point()

    @property
    def get_first_point(self) -> tuple[float, float]:
        return (self.__point1.getx, self.__point1.gety)

    @property
    def get_second_point(self) -> tuple[float, float]:
        return (self.__point2.getx, self.__point2.gety)

    @get_first_point.setter
    def set_first_point(self, point: Point) -> None:
        self.__point1.setX = point.getx
        self.__point1.setY = point.gety

    @get_second_point.setter
    def set_second_point(self, point: Point) -> None:
        self.__point2.setX = point.getx
        self.__point2.setY = point.gety

    @get_first_point.deleter
    def del_first_point(self):
        del self.__point1
        del self.__point2

    def __add__(self, other: "Line") -> tuple[float, float] | None:
        # get the coords of the first line
        p1: tuple[float, float] = self.get_first_point
        p2: tuple[float, float] = self.get_second_point

        # get the coords of the second line
        p3: tuple[float, float] = other.get_first_point
        p4: tuple[float, float] = other.get_second_point

        # Line 1 vector
        A1 = p2[1] - p1[1]
        B1 = p1[0] - p2[0]
        C1 = A1 * p1[0] + B1 * p1[1]

        # Line 2 vector
        A2 = p4[1] - p3[1]
        B2 = p3[0] - p4[0]
        C2 = A2 * p3[0] + B2 * p3[1]

        # Determinant
        det = A1 * B2 - A2 * B1

        if det == 0:
            return None  # Lines are parallel or coincident

        x = (B2 * C1 - B1 * C2) / det
        y = (A1 * C2 - A2 * C1) / det

        return (x, y)
