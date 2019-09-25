import unittest
import re

from generators import simple
from generators import simple_with_probability
from generators import bipartite


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.simpleGraph = None
        self.bipartiteGraph = None

    # WORK IN PROGRESS FOR BIPARTITE
    #def test_each_vertice_visited_once_in_bipartite_graph(self):
        #self.bipartiteGraph = bipartite(4, 4, 4)
        #couples = self.get_graph_couples(self.bipartiteGraph)

        #neighbors = []
        #visited = [False] * len(couples)

        #count = 0
        #for couple in couples:
            #print(str(couple))
            #if couple[1] in neighbors:
                #if visited[count] is True:
                    #visited[count] = False
                #else:
                    #visited[count] = True
            #else:
                #neighbors.append(couple[1])
            #count = count + 1

        #for i in range(len(visited)):
            #self.assertTrue(visited[i], str(couples[i][1]) + ' was visited twice')


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
        self.simpleGraph = simple(4,4)
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

    def test_simple_graph_has_no_loops(self):
        self.simpleGraph = simple(4,4)
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


    def get_graph_couples(self, graph):
        edges = graph.edges()

        couple = []
        for edge in edges:
            values = []
            for vertice in edge:
                # Check if edge has the same vertice
                if vertice not in values:
                    values.append(vertice)
                else:
                    # If edge has the same vertice, increment 'nbrOfLoops'
                    nbrOfLoops = nbrOfLoops + 1
            couple.append(values)
        return couple

if __name__ == '__main__':
    unittest.main()
