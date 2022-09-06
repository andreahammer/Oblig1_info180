from heuristic import Heuristic
from make_grid import SIZE

class ZeroH3(Heuristic):

    @staticmethod
    def h(node):
        a = abs(node.i - SIZE)
        b = abs(node.j - SIZE)
        return (max(a, b))*3

