import unittest
import re

from generators import simple
from generators import simple_with_probability
from generators import bipartite
from generators import bipartite_with_probability
from generators import eulerianCycle
from generators import regular

class TestSimpleGraphGenerators(unittest.TestCase):

    def setUp(self):
        self.simpleGraph = None
        self.simpleGraphWithProbility = None

    # Tests de la méthode bipartite
    # Nomenclature :

    # V1 = {V=0}
    # V2 = {V<0}
    # V3 = {V>0}

    # P1 = {P=0}
    # P2 = {P=1}
    # P3 = {P>1}
    # P4 = {P<0}
    # P5 = {0 <= P <= 1}

    # cas d'erreurs: V1, V2, P2, P3

    # V3P5 -> d1 = <{v=4, p=0.8}, {graph}>
    def test_simple_graph_probility_greater_than_zero_smaller_than_one(self):
        exceptionWasRaised = False

        try:
            self.simpleGraphWithProbility = simple_with_probability(4, 0.8)
        except Exception:
            exceptionWasRaised = True

        self.assertTrue(self.simpleGraphWithProbility is not None and exceptionWasRaised is False)

    # V3P3 -> d2 = <{v=4, p=-1.0}, {ERROR}>
    def test_simple_graph_with_probility_less_than_zero(self):
        exceptionWasRaised = False

        try:
            self.simpleGraphWithProbility = simple_with_probability(4, -1.0)
        except Exception:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised, 'Exception was not raised, method has passed with p=' + str(-1.0))

    # V3P2 -> d3 = <{v=4, p=1.5}, {ERROR}>
    def test_simple_graph_with_probability_greater_than_one(self):
        exceptionWasRaised = False

        try:
            self.simpleGraphWithProbility = simple_with_probability(4, 1.5)
        except Exception:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised, 'Exception was not raised, method has passed with p=' + str(1.5))

    # Tests de la méthode bipartite
    # Nomenclature :

    # V1 = {V=0}
    # V2 = {V<0}
    # V3 = {V>0}

    # E1 = {V=0}
    # E2 = {V<0}
    # E3 = {V>0}

    # G1 = {V>E}
    # G2 = {V<E}

    # cas d'erreurs: V1, V2, E1, E2, G2

    # V2E2G1 -> d1 = <{v=4, E=2}, {graph}>
    def test_simple_graph_v_greater_than_e(self):
        exceptionWasRaised = False

        try:
            # <{v = 4}, {e = 2}>
            self.simpleGraph = simple(4, 2)
        except Exception:
            exceptionWasRaised = True

        self.assertTrue(self.simpleGraph is not None and exceptionWasRaised is False)

    # E2 -> d2 = <{v=4, E=-1}, {ERROR}>
    def test_simple_graph_number_of_edges_is_less_than_zero(self):
        exceptionWasRaised = False

        try:
            self.simpleGraph = simple(4, -1)
        except Exception:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised)

    # V2 -> d3 = <{v=-1, E=4}, {ERROR}>
    def test_simple_graph_number_of_vertices_is_less_than_zero(self):
        exceptionWasRaised = False

        try:
            self.simpleGraph = simple(-1, 4)
        except Exception:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised)

    # V1E3 -> d4 = <{v=0, E=4}, {graph}>
    def test_simple_graph_number_of_vertices_equals_zero(self):
        exceptionWasRaised = False

        try:
            self.simpleGraph = simple(0, 4)
        except Exception as ex:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised)

    # V3E1 -> d5 = <{v=4, E=0}, {graph}>
    def test_simple_graph_number_of_edges_equals_zero(self):
        exceptionWasRaised = False

        try:
            self.simpleGraph = simple(4, 0)
        except:
            exceptionWasRaised = True

        self.assertFalse(exceptionWasRaised)

    # V3E3G1 -> d6 = <{v=4, e=2}, {graph}>
    def test_simple_graph_vertices_greater_than_edges(self):
        exceptionWasRaised = False

        try:
            self.simpleGraph = simple(4, 2)
        except:
            exceptionWasRaised = True

        self.assertFalse(exceptionWasRaised and self.simpleGraph is not None)

    # V3E3G2 -> d7 = <{v=2, e=4}, {ERROR}>
    def test_simple_graph_vertices_smaller_than_edges(self):
        exceptionWasRaised = False

        try:
            self.simpleGraph = simple(2, 4)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised)

    # V3E3G3 -> d8 = <{v=2, e=2}, {ERROR}>
    def test_simple_graph_vertices_equals_edges(self):
        exceptionWasRaised = False

        try:
            self.simpleGraph = simple(2, 2)
        except:
            exceptionWasRaised = True

        self.assertFalse(exceptionWasRaised and self.simpleGraph is not None)

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
    # E4 {E>V1+V2}
    # E5 {E<V1+V2}

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

    # Tests de la méthode regular
    # Nomenclature :

    # V1 = {V=-1}
    # V2 = {V<K+1}
    # V3 = {V>=K+1}
    # K1 = {K=-1}
    # K2 = {K>=0}
    # VK1 = {V*K pair}
    # VK2 = {V*K impair}

    # Combinaisons retenues :
    # Cas d'erreurs = V1, V2, K1, VK2
    # Cas ok : V3K2VK1

    def test_regular_V1(self):

        exceptionWasRaised = False
        try:
            # Try to create a regular graph with negative number of vertices
            self.regularGraph = regular(-1, 2)
        except Exception:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised, 'Exception was not raised, method has passed with V=-1')

    def test_regular_V2(self):
        exceptionWasRaised = False
        try:
            # Try to create a regular graph with invalid numbers of vertices and degree
            self.regularGraph = regular(3, 3)
        except Exception:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised, 'Exception was not raised, method has passed with V=3 and K=3')

    def test_regular_K1(self):
        exceptionWasRaised = False
        try:
            # Try to create a regular graph with negative degree
            self.regularGraph = regular(3, -1)
        except Exception:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised, 'Exception was not raised, method has passed with K=-1')

    def test_regular_VK2(self):
        exceptionWasRaised = False
        try:
            # Try to create a regular graph with V*K not even
            self.regularGraph = regular(3, 3)
        except Exception:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised, 'Exception was not raised, method has passed with VK=9')

    def test_regular_V3K2VK1(self):
        # TODO
        pass


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
