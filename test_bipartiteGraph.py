import unittest

from generators import bipartite
from generators import bipartite_with_probability

class TestBipartiteGraph(unittest.TestCase):
    def setUp(self):
        self.bipartiteGraph = None
        self.bipartiteGraphWithProbility = None

    def test(self):
        self.bipartiteGraph = bipartite(4, 4, 4)

        vertices = self.bipartiteGraph.vertices()
        edges = self.bipartiteGraph.edges()

        visited = {}
        couples = self.get_graph_couples(self.bipartiteGraph)
        for i in couples:
            if isinstance(couples[i], list):
                visited.update({i: True})
                for j in couples[i]:
                    if visited.get(j) is True:
                        visited.update({j: False})
                    else:
                        visited.update({j: True})
            else:
                visited.update({i: True})
                if couples[i] is not None:
                    visited.update({couples[i]: True})

        count = 0
        for value in visited.values():
            self.assertTrue(value, 'Edge ' + str(count) + ' has been visited twice')
            count = count + 1



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

    def get_graph_couples(self, graph):
        edges = graph.edges()
        vertices = graph.vertices()

        couple = {}
        for edge in edges:
            values = []
            for vertice in edge:
                values.append(vertice)
            first = values[0]
            second = values[1]
            if couple.get(first) is not None:
                otherValue = couple[first]
                couple.update({first: [otherValue, second]})
            else:
                couple.update({first: second})

        for vertice in vertices:
            if vertice not in couple.keys() or not couple.values():
                couple.update({vertice: None})

        return couple

if __name__ == '__main__':
    unittest.main()
