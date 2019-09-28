import unittest

from generators import simple
from generators import simple_with_probability
from generators import bipartite
from generators import bipartite_with_probability
from generators import eulerianCycle
from generators import regular


class TestSimpleGraphGeneratorsEC(unittest.TestCase):

    def setUp(self):
        self.simpleGraph = None
        self.simpleGraphWithProbility = None

    # Tests de la méthode simple_with_probility
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

    # V1 -> d1 = <{v=0, p=0.8}, {ERROR}>
    def test_simple_graph_with_probility_V_smaller_than_zero(self):
        exceptionWasRaised = False

        try:
            self.simpleGraphWithProbility = simple_with_probability(-1, 0.8)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised and self.simpleGraphWithProbility is None)

    # V3P5 -> d2 = <{v=4, p=0.8}, {graph}>
    def test_simple_graph_with_probility_V_greater_than_zero_p_between_one_and_zero(self):
        exceptionWasRaised = False

        try:
            self.simpleGraphWithProbility = simple_with_probability(4, 0.8)
        except:
            exceptionWasRaised = True

        self.assertFalse(exceptionWasRaised and self.simpleGraphWithProbility is not None)

    def test_simple_graph_with_probility_p_not_between_zero_and_one(self):
        exceptionWasRaised = False

        try:
            self.simpleGraphWithProbility = simple_with_probability(4, 1.5)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised and self.simpleGraphWithProbility is None)

    # Tests de la méthode simple
    # Nomenclature :

    # V1 = {V=0}                    [erreur]
    # V2 = {V<0}                    [erreur]
    # V3 = {V>0}                    [proprietes: validNbrVertices]

    # E1 = {V=0}                    [erreur]
    # E2 = {V<0}                    [erreur]
    # E3 = {V>0}                    [proprietes: validNbrEdges]

    # G1 = {0 > E > V*(V-1)/2}      [if validNbrVertices && validNbrEdges]
    # G2 = {E < V*(V-1) /2 }        [if validNbrVertices && validNbrEdges]

    # cas d'erreurs: V1, V2, E1, E2, G2

    # V2 -> d1 = <{v=-1.0, e=4}, {ERROR}>
    def test_simple_graph_V_smaller_than_zero(self):
        exceptionWasRaised = False

        try:
            self.simpleGraph = simple(-1.0, 4)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised and self.simpleGraphWithProbility is None)

    # E2 -> d1 = <{v=4, e=-1.0}, {ERROR}>
    def test_simple_graph_E_smaller_than_zero(self):
        exceptionWasRaised = False

        try:
            self.simpleGraph = simple(4, -1.0)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised and self.simpleGraphWithProbility is None)

    # G1 -> d1 = <{v=4, e=4}, {graph}>
    def test_simple_graph_E_greater_than_G1(self):
        exceptionWasRaised = False

        try:
            self.simpleGraph = simple(4, 4)
        except:
            exceptionWasRaised = True

        self.assertFalse(exceptionWasRaised and self.simpleGraphWithProbility is not None)

class TestBipartiteGeneratorsEC(unittest.TestCase):

    def setUp(self):
        self.bipartiteGraph = None
        self.bipartiteGraphWithProbility = None

    # Tests de la méthode bipartite_with_probility
    # Nomenclature :

    # V1(1) = {V1=0}    [proprietes: validNbrOfVertices]
    # V1(2) = {V1>0}    [proprietes: validNbrofVertices]
    # V1(3) = {V1<0}    [erreur]

    # V2(1) = {V2=0}    [proprietes: validNbrOfEdges]
    # V2(2) = {V2>0}    [proprietes: validNbrOfEdges]
    # V2(3) = {V2<0}    [erreur]

    # P1 = {P<0}        [erreur]
    # P2 = {P>1}        [erreur]
    # P3 = {0<P<1}      [if validNbrOfEdges && validNbrOfVertices]

    # cas d'erreur: P2, P3, V1(3), V2(3)

    def test_bipartite_with_probility_V1_smaller_than_zero(self):
        exceptionWasRaised = False

        try:
            self.bipartiteGraphWithProbility = bipartite_with_probability(-1.0, 4, 0.8)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised and self.bipartiteGraphWithProbility is None)

    def test_bipartite_with_probility_V2_smaller_than_zero(self):
        exceptionWasRaised = False

        try:
            self.bipartiteGraphWithProbility = bipartite_with_probability(4, -1.0, 0.8)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised and self.bipartiteGraphWithProbility is None)

    def test_bipartite_with_probility_P_between_one_and_zero(self):
        exceptionWasRaised = False

        try:
            self.bipartiteGraphWithProbility = bipartite_with_probability(4, 4, 0.8)
        except:
            exceptionWasRaised = True

        self.assertFalse(exceptionWasRaised and self.bipartiteGraphWithProbility is not None)

    # Tests de la méthode bipartite
    # Nomenclature :

    # V1(1) = {V1=0}            [erreur]
    # V1(2) = {V1>0}            [proprietes: validNbrVertices1]
    # V1(3) = {V1<0}            [erreur]

    # V2(1) {V2=0}              [erreur]
    # V2(2) {V2>0}              [proprietes: validNbrVertices2]
    # V2(3) {V2<0}              [erreur]

    # E1 {E=0}                  [erreur]
    # E2 {E<0}                  [erreur]
    # E3 {E>0}                  [proprietes: validNbrEdges]

    # G1 {0 <= E <= E>V1*V2}    [if validNbrVertices1 && validNbrVertices2 validNbrEdges]
    # G2 {E <V1*V2}             [if validNbrVertices1 && validNbrVertices2 validNbrEdges]

    # Cas d'erreurs = V1(1), V1(3), V2(3), E1, E2, E5

    def test_bipartite_V1_smaller_than_zero(self):
        exceptionWasRaised = False

        try:
            self.bipartiteGraph = bipartite(-1.0, 2, 6)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised and self.bipartiteGraph is None)

    def test_bipartite_V2_smaller_than_zero(self):
        exceptionWasRaised = False

        try:
            self.bipartiteGraph = bipartite(4, -1.0, 6)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised and self.bipartiteGraph is None)

    def test_bipartite_E_smaller_than_zero(self):
        exceptionWasRaised = False

        try:
            self.bipartiteGraph = bipartite(4, 4, -1.0)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised and self.bipartiteGraph is None)

    def test_bipartite_E_between_G1(self):
        exceptionWasRaised = False

        try:
            self.bipartiteGraph = bipartite(2, 2, 6)
        except:
            exceptionWasRaised = True

        self.assertFalse(exceptionWasRaised and self.bipartiteGraph is not None)

class TestEulerianCycleEC(unittest.TestCase):

    def setUp(self):
        self.eulerianCycle = None

    # Tests de la méthode eulerianCycle
    # Nomenclature :

    # V1 = {V<0}    [erreur]
    # V2 = {V=0}    [erreur]
    # V3 = {V>0}    [proprietes: validNbrVertices]

    # E1 = {E<0}    [erreur]
    # E2 = {E=0}    [erreur]
    # E3 = {E>0}    [proprietes: validNbrEdges]

    # cas d'erreur: V1, V2, E1, E2

    # V1 -> d1 = <{v=-1.0, e=4}, {ERROR}>

    def test_eulerianCycle_V_smaller_than_zero(self):
        exceptionWasRaised = True

        try:
            self.eulerianCycle = eulerianCycle(-1.0, 4)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised and self.eulerianCycle is None)

    def test_eulerianCycle_E_smaller_than_zero(self):
        exceptionWasRaised = True

        try:
            self.eulerianCycle = eulerianCycle(4, -1.0)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised and self.eulerianCycle is None)


class TestRegularGeneratorsEC(unittest.TestCase):

    def setUp(self):
        self.regularGraph = None

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

    def test_eulerianCycle_V1_smaller_than_zero(self):
        exceptionWasRaised = False

        try:
            self.regularGraph = regular(-1.0, 4)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised and self.regularGraph is None)

    def test_eulerianCycle_K_smaller_than_zero(self):
        exceptionWasRaised = False

        try:
            self.regularGraph = regular(4, -1.0)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised and self.regularGraph is None)

    def test_eulerianCycle_multiplication_V_K_is_pair(self):
        exceptionWasRaised = False

        try:
            self.regularGraph = regular(2, 4)
        except:
            exceptionWasRaised = True

        self.assertFalse(exceptionWasRaised and self.regularGraph is not None)

if __name__ == '__main__':
    unittest.main()
