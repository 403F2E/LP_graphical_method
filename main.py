
from matplotlib import pyplot as plt
from random import choice
from system.system import System
from system.graphElement.elements import Line, Point
from numpy import array

def draw(lines: list[Line], intersections: list[Point]):
    """
    lines: list of Line objects with first_point and second_point as (x, y) tuples
    intersections: list of Point objects with .dox and .doy attributes
    """
    colors = [
        'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black',
        'purple', 'pink', 'brown', 'orange', 'teal', 'coral', 'lightblue',
        'lime', 'lavender', 'turquoise', 'darkgreen', 'tan', 'salmon',
        'gold', 'darkred', 'darkblue'
    ]

    plt.figure(figsize=(8, 8))

    # For scaling and axis
    all_x = []
    all_y = []

    for line in lines:
        x1, y1 = line.first_point
        x2, y2 = line.second_point

        all_x += [x1, x2]
        all_y += [y1, y2]

    for point in intersections:
        all_x.append(point.dox)
        all_y.append(point.doy)

    # Determine bounds and padding
    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)
    padding = 1
    x_range = (min_x - padding, max_x + padding)
    y_range = (min_y - padding, max_y + padding)

    # Draw extended lines
    for line in lines:
        x1, y1 = line.first_point
        x2, y2 = line.second_point

        color = choice(colors)

        if x1 == x2:  # vertical line
            plt.plot([x1, x1], y_range, color=color, linewidth=2)
        else:
            # Find slope and intercept
            m = (y2 - y1) / (x2 - x1)
            b = y1 - m * x1

            # Calculate y for full x range
            x_vals = array(x_range)
            y_vals = m * x_vals + b
            plt.plot(x_vals, y_vals, color=color, linewidth=2)

    # Draw intersection points
    for point in intersections:
        plt.plot(point.dox, point.doy, 'ko')  # black dot

    # Draw x and y axes in black
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    plt.xlim(x_range)
    plt.ylim(y_range)

    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Welcome to the solver!")
    plt.axis("equal")
    plt.show()


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
    print("\n")
    nbr_cst = int(input(" --- \\\\ How many constraint do you have : "))
    for i in range(nbr_cst):
        print(f" --- \\\\ Enter the constraint {i+1} : ")
        x1: float = float(input("Enter the X1's factor : "))
        x2: float =  float(input("Enter the X2's factor : "))
        print("0/ addition (+)")
        print("1/ subtraction (-)")
        choice: int = int(input("Enter the operation between the 2 variables (0 or 1): "))
        op: str = "sub" if choice else "add"
        limit: float = float(input("Enter the limit of this constraint : "))
        constraints.append((Point(x1, x2), op, limit))

    return [objectif_func, constraints]

def solve(system: System) -> Point:
    system.lines = system.constraints
    system.intersections = system.lines
    answer: Point = system.haveAnswer()
    draw(system.lines, system.intersections)
    return answer

if __name__=='__main__':
    system = System()
    # system_content = mold()
    system.objectif_func = (Point(1, 1), "add") # system_content[0]
    system.constraints = (Point(1, 0), "add", 20)
    system.constraints = (Point(0, 1), "add", 30)
    system.constraints = (Point(2, 0), "add", 80)
    system.constraints = (Point(0, 1.5), "add", 120)
    system.constraints = (Point(1, 0), "add", 0)
    system.constraints = (Point(0, 1), "add", 0)
    system.minOrmax = True
    answer: Point = solve(system)
    print(f"The point is ({answer.dox}, {answer.doy})")
