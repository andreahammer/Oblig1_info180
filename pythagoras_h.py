from heuristic import Heuristic
from make_grid import SIZE
import math

class Pythagoras_h(Heuristic):

    @staticmethod
    def h(node):
        i = node.i
        j = node.j
        i_goal = SIZE
        j_goal = SIZE
        i_dist = i_goal - i
        j_dist = j_goal - j
        hypotenuse = math.sqrt(i_dist**2 + j_dist**2)
        return hypotenuse
