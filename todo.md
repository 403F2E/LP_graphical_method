# Linear Programming : **Graphical Method** 

## models (Entities) :
 - point : ### DONE
 **attributes** :
  - float x
  - float y
 **methods** :
  - ?
 - line : ### DONE
 **attributes** :
  - point a
  - point b
 **methods** :
  - __add__ : overloading it to calc the intersection between two lines
 - System :
 **attributes** :
  - float/int x1
  - float/int x2
  - line lines = []
 **methods** :
  - comparePoints : comparing the points with all the constraints
  - conclude : having the optimal point
  - draw : representing the system using matplotlib

## features :
 - [ ] take variables from user
 - [ ] take constraints from user
 - [ ] the user choose to minimize/maximize
 - [ ] calculate the points at the intersections between lines #I don't know if it is necessary to have intersections
 - [ ] compare the points with the constraints
 - [ ] have the optimal point according to the constraints
 - [ ] represents that in the graph using matplotlib
