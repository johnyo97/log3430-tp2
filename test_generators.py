import unittest
import re

from generators import simple
from generators import simple_with_probability


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.simpleGraph = simple(4, 4)

    def test_simple_graph_with_probility(self):
        exceptionWasRaised = False
        simpleGraphWithProbility = None

        try:
            # Try to create a simple graph with probility '0.8'
            simpleGraphWithProbility = simple_with_probability(4, 0.8)
        except Exception:
            exceptionWasRaised = True

        self.assertTrue(simpleGraphWithProbility is not None and exceptionWasRaised is False)

    def test_simple_graph_with_probility_less_than_zero(self):
        exceptionWasRaised = False
        falseProbility = -1.0

        try:
            # Try to create a simple graph with probility '-1'
            simpleGraphWithProbility = simple_with_probability(4, falseProbility)
        except Exception:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised, 'Exception was not raised, method has passed with p=' + str(falseProbility))

    def test_simple_graph_with_probability_greater_than_one(self):
        exceptionWasRaised = False
        falseProbility = 1.5

        try:
            # Try to create a simple graph with probility '1.5'
            simpleGraphWithProbility = simple_with_probability(4, falseProbility)
        except Exception:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised, 'Exception was not raised, method has passed with p=' + str(falseProbility))

    def test_simple_graph_has_no_multiple_edges(self):
        edges = self.simpleGraph.edges()

        values = []
        # Counter for number of duplicates, if present
        duplicatesCount = 0
        for edge in edges:
            # Check if two edges are the same
            if edge not in values:
                values.append(edge)
            # If they are the same, increment 'count'
            else:
                duplicatesCount = duplicatesCount + 1
        # Check if number of duplicates is equal to 0
        self.assertTrue(duplicatesCount == 0)

    def test_simple_graph_has_no_loopsM(self):
        edges = self.simpleGraph.edges()

        # Counter for the number of loops, if present
        nbrOfLoops = 0
        for edge in edges:
            values = []
            for vertice in edge:
                # Check if edge has the same vertice
                if vertice not in values:
                    values.append(vertice)
                else:
                    # If edge has the same vertice, increment 'nbrOfLoops'
                    nbrOfLoops = nbrOfLoops + 1

        self.assertTrue(nbrOfLoops == 0)


if __name__ == '__main__':
    unittest.main()
