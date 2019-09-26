import unittest


class TestBipartiteGraph(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


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


if __name__ == '__main__':
    unittest.main()
