import importlib.util
from itertools import combinations
from pathlib import Path
import sys
import unittest

DIRECTORY=Path(__file__).resolve().parents[1]/'research/chatgpt/ramsey'
sys.path.insert(0,str(DIRECTORY))
import heptagon_near_extremal_counterexample as example
from pauli_realization_audit import decode_graph6
from pauli_low_cost_structure import parity_closed_heptagons

class HeptagonForcingTests(unittest.TestCase):
    def test_counterexample_certificate(self):
        result=example.verify()
        self.assertEqual(result['minimum_qubits'],9)
        self.assertEqual(result['nullity'],3)
        rows=decode_graph6(result['graph6'])
        for candidate in result['vertex_extension']['witnesses']:
            neighborhood=candidate['neighbor_mask'];six=candidate['disjoint_independent_six_mask']
            self.assertEqual(neighborhood&six,0);self.assertEqual(six.bit_count(),6)
            for mask in (neighborhood,six):
                vertices=[i for i in range(21)if mask>>i&1]
                self.assertTrue(all(not(rows[i]>>j&1)for i,j in combinations(vertices,2)))

    def test_gap_proof(self):
        count=0
        for gaps in example.compositions(21,7):
            self.assertEqual(sum(gaps),21);self.assertTrue(all(g>=2 for g in gaps))
            self.assertTrue(example.gap_violates(gaps));count+=1
        self.assertEqual(count,1716)

    def test_polynomial_gcd(self):
        p=sum(1<<j for j in example.JUMPS);f=(1<<21)|1;d=example.polynomial_gcd(p,f)
        self.assertEqual(d,9)
        self.assertEqual(example.polynomial_remainder(p,d),0)
        self.assertEqual(example.polynomial_remainder(f,d),0)

    @unittest.skipUnless(importlib.util.find_spec('pysat'),'optional python-sat dependency')
    def test_sat_encoding_known_model(self):
        from heptagon_forcing_probe import build_formula
        from pysat.solvers import Solver
        lines=(DIRECTORY/'pauli-realization-catalogues/r37_22.g6').read_text().splitlines()
        rows=decode_graph6(lines[186]);cycles,_=parity_closed_heptagons(rows)
        cycle=next(iter(cycles.values()))
        for mode,expected in [('baseline',True),('two-zero',False),('sparse',False)]:
            clauses,_,edges,types=build_formula(mode)
            outside=[i for i in range(22)if i not in cycle]
            order=cycle+sorted(outside,key=lambda v:types.index(tuple(i for i,old in enumerate(cycle)if rows[v]>>old&1)))
            assumptions=[variable if rows[order[i]]>>order[j]&1 else -variable for(i,j),variable in edges.items()]
            with Solver(name='glucose4',bootstrap_with=clauses)as solver:
                self.assertEqual(solver.solve(assumptions=assumptions),expected)

if __name__=='__main__':unittest.main()
