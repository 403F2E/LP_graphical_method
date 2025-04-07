
class Point:
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
