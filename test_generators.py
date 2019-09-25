import unittest
import re

from generators import simple
from models import Graph


class MyTestCase(unittest.TestCase):


    def setUp(self):
        self.simpleGraph = simple(4, 4)

    def test_simple_graph_has_no_multiple_edges(self):
        edges = self.simpleGraph.edges()

        values = []
        count = 0
        for edge in edges:
            if edge not in values:
                values.append(edge)
            else:
                count = count + 1

        self.assertTrue(count == 0)

    def test_simple_graph_has_no_loops(self):
        edges = self.simpleGraph.edges()

        count = 0;
        for edge in edges:
            values = []
            for vertice in edge:
                if vertice not in values:
                    values.append(vertice)
                else:
                   count = count + 1

        self.assertTrue(count == 0)



if __name__ == '__main__':
    unittest.main()
