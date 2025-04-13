
from matplotlib import pyplot as plt
from system.system import System
from system.graphElement.elements import Point

def draw(x: float, y: float):
    plt.plot(x, y, label="test", color="blue", marker="o")
    plt.title("Simple test")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")

def mold() -> list:
    print("Welcome to your system solver 📖")
    print("*" * 20)
    print("\n")

    ''' Reading the objectif function '''
    print(" --- \\\\ What is the objectif function related to your system : ")
    x1: float = float(input("Enter the X1's factor : "))
    x2: float =  float(input("Enter the X2's factor : "))
    print("0/ addition (+)")
    print("1/ subtraction (-)")
    choice: int = int(input("Enter the operation between the 2 variables (0 or 1): "))
    op: str = "sub" if choice else "add"
    objectif_func: tuple[Point, str] = (Point(x1, x2), op)

    ''' Reading the constraints '''
    constraints: list[tuple[Point, str, float]] = []
    nbr_cst = int(input(" --- \\\\ How many constraint do you have : "))
    for _ in range(nbr_cst):
        print("0/ addition (+)")
        print("1/ subtraction (-)")
        choice: int = int(input("Enter the operation between the 2 variables (0 or 1): "))
        op: str = "sub" if choice else "add"
        limit: float = float(input("Enter the limit of this constraint : "))
        constraints.append((Point(x1, x2), op, limit))

    return [objectif_func, constraints]

if __name__=='__main__':
    system = System()
    system_content = mold()
    system.set_objectif_func = system_content[0]
    system.set_constraints = system_content[1]
    print("hello world!")
