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

    def test_simple_graph_with_probility_V_smaller_than_zero(self):
        exceptionWasRaised = False

        try:
            self.simpleGraphWithProbility = simple_with_probability(-1, 0.8)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised and self.simpleGraphWithProbility is None)

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

    # G1 = {0 > E > V*(V-1)/2}      [if validNbrVertices && validNbrEdges]

    def test_simple_graph_V_smaller_than_zero(self):
        exceptionWasRaised = False

        try:
            self.simpleGraph = simple(-1.0, 4)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised and self.simpleGraphWithProbility is None)

    def test_simple_graph_E_smaller_than_zero(self):
        exceptionWasRaised = False

        try:
            self.simpleGraph = simple(4, -1.0)
        except:
            exceptionWasRaised = True

        self.assertTrue(exceptionWasRaised and self.simpleGraphWithProbility is None)

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
    # G1 {0 <= E <= E>V1*V2}    [if validNbrVertices1 && validNbrVertices2 validNbrEdges]
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
