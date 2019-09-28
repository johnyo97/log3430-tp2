import unittest

from generators import bipartite
from generators import simple
from generators import bipartite_with_probability

class TestBipartiteGraph(unittest.TestCase):
    def setUp(self):
        self.bipartiteGraph = None
        self.bipartiteGraphWithProbility = None

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


    # Tests de la méthode bipartite
    # Nomenclature :

    # V1(1) = {V1=0}
    # V1(2) = {V1>0}
    # V1(3) = {V1<0}
    # V1(4) = {V1>V2}
    # V1(5) = {V1<V2}

    # V2(1) {V2=0}
    # V2(2) {V2>0}
    # V2(3) {V2<0}

    # E1 {E=0}
    # E2 {E<0}
    # E3 {E>0}
    # E4 {E>V1*V2}
    # E5 {E<V1*V2}

    # Cas d'erreurs = V1(1), V1(3), V2(3), E1, E2, E5

    # V1(1) -> d1 = <{V1=0, V2=4, E=8}, {ERROR}>
    def test_V1_equals_zero(self):
        exceptionWasRaised = False
        bipartiteGraph = None

        try:
            bipartiteGraph = bipartite(0, 4, 8)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised and bipartiteGraph is None)

    # V2(1) -> d2 = <{V1=4, V2=0, E=8}, {ERROR}>
    def test_V2_equals_zero(self):
        exceptionWasRaised = False
        bipartiteGraph = None

        try:
            bipartiteGraph = bipartite(4, 0, 8)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised and bipartiteGraph is None)

    # E1 -> d3 = <{V1=4, V2=4, E=0}, {ERROR}>
    def test_E_equals_zero(self):
        exceptionWasRaised = False
        bipartiteGraph = None

        try:
            bipartiteGraph = bipartite(2, 4, 0)
        except:
            exceptionWasRaised = True

        self.assertFalse(exceptionWasRaised and bipartiteGraph is not None)

    # V1(1) -> d1 = <{V1=0, V2=4, E=8}, {ERROR}>
    def test_V1_V2_and_E_greater_than_zero(self):
        exceptionWasRaised = False
        bipartiteGraph = None

        try:
            bipartiteGraph = bipartite(2, 2, 6)
        except:
            exceptionWasRaised = True

        self.assertFalse(exceptionWasRaised and bipartiteGraph is not None)

    # V1(1) -> d1 = <{V1=0, V2=4, E=8}, {ERROR}>
    def test_V1_greater_than_V2_E_greater_than_zero(self):
        exceptionWasRaised = False
        bipartiteGraph = None

        try:
            bipartiteGraph = bipartite(2, 1, 6)
        except:
            exceptionWasRaised = True

        self.assertFalse(exceptionWasRaised and bipartiteGraph is not None)

    # V1(2)V2(2)E3 -> d4 = <{V1=2, V2=2, E=6}, {graph}>
    def test_V2_greater_than_V1_E_greater_than_zero(self):
        exceptionWasRaised = False
        bipartiteGraph = None

        try:
            bipartiteGraph = bipartite(1, 2, 6)
        except:
            exceptionWasRaised = True

        self.assertFalse(exceptionWasRaised and bipartiteGraph is not None)

    # V1(2)V2(2)E5 -> d5 = <{V1=4, V2=4, E=6}, {graph}>
    def test_E_smaller_than_the_sum_of_V1_V2(self):
        exceptionWasRaised = False
        bipartiteGraph = None

        try:
            bipartiteGraph = bipartite(4, 4, 6)
        except Exception as ex:
            exceptionWasRaised = True

        self.assertFalse(exceptionWasRaised and bipartiteGraph is not None)

    # V1(2)V2(2)E4 -> d6 = <{V1=4, V2=4, E=6}, {graph}>
    def test_E_greater_than_the_sum_of_V1_V2(self):
        exceptionWasRaised = False
        bipartiteGraph = None

        try:
            bipartiteGraph = bipartite(2, 2, 6)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised and bipartiteGraph is None)

    # V1(3) -> d7 = <{V1=-1, V2=4, E=6}, {ERROR}>
    def test_V1_smaller_than_0(self):
        exceptionWasRaised = False
        bipartiteGraph = None

        try:
            bipartiteGraph = bipartite(-1, 4, 6)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised and bipartiteGraph is None)

    # V2(3) -> d8 = <{V1=4, V2=-1, E=6}, {ERROR}>
    def test_V2_smaller_than_0(self):
        exceptionWasRaised = False
        bipartiteGraph = None

        try:
            bipartiteGraph = bipartite(4, -1, 6)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised and bipartiteGraph is None)

    # E2 -> d9 = <{V1=4, V2=4, E=-1}, {ERROR}>
    def test_E_smaller_than_0(self):
        exceptionWasRaised = False
        bipartiteGraph = None

        try:
            bipartiteGraph = bipartite(4, 4, -1)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised and bipartiteGraph is None)

    def test_simple_graph_has_no_multiple_edges(self):
        # <{v = 6, e = 3}, {generatedGraph}>
        self.simpleGraph = simple(6, 3)
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
        # <{v = 4}, {e = 4}>
        self.simpleGraph = simple(4, 4)
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

    #def test(self):
     #   self.bipartiteGraph = bipartite(4, 4, 4)

      #  vertices = self.bipartiteGraph.vertices()
           # edges = self.bipartiteGraph.edges

        #visited = {}
        #couples = self.get_graph_couples(self.bipartiteGraph)
        #for i in couples:
         #   if isinstance(couples[i], list):
          #      visited.update({i: True})
           #     for j in couples[i]:
            #        if visited.get(j) is True:
             #           visited.update({j: False})
              #      else:
               #         visited.update({j: True})
            #else:
            #    visited.update({i: True})
             #   if couples[i] is not None:
              #      visited.update({couples[i]: True})

        #count = 0
        #for value in visited.values():
          #  self.assertTrue(value, 'Edge ' + str(count) + ' has been visited twice')
           # count = count + 1



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

    #def get_graph_couples(self, graph):
     #   edges = graph.edges()
      #  vertices = graph.vertices()

       # couple = {}
        #for edge in edges:
         #   values = []
          #  for vertice in edge:
         #       values.append(vertice)
           ##second = values[1]
            ##   otherValue = couple[first]
              #  couple.update({first: [otherValue, second]})
            #else:
             #   couple.update({first: second})

       # for vertice in vertices:
        #    if vertice not in couple.keys() or not couple.values():
         #       couple.update({vertice: None})

        #return couple

if __name__ == '__main__':
    unittest.main()
