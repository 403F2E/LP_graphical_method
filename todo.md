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
 - System : ### DONE
 **attributes** :
  - float/int x1
  - float/int x2
  - line lines = []
 **methods** :
  - get_lines : calculating the lines of the constraints ### DONE
  - get_intersections : calculating the intersections of all lines ### DONE
  - comparePoints : comparing the points with all the constraints ### DONE
  - conclude : having the optimal point ### DONE

## features :
 - [ ] take variables from user
 - [ ] take constraints from user
 - [ ] the user choose to minimize/maximize
 - [x] calculate the points at the intersections between lines
 - [x] compare the points with the constraints
 - [x] have the optimal point according to the constraints
 - [ ] represents that in the graph using matplotlib
