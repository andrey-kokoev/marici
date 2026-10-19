"""Finite rational cochain controls; geometric statements are imported in the note."""
from fractions import Fraction as Q
from pathlib import Path
import json
import unittest


def scale(a, s):
    return tuple(tuple(s*x for x in row) for row in a)


def transpose(a):
    return tuple(zip(*a))


def mul(a, b):
    return tuple(tuple(sum(x*y for x, y in zip(row, col)) for col in zip(*b)) for row in a)


def eye(n):
    return tuple(tuple(Q(i == j) for j in range(n)) for i in range(n))


def sign(n):
    return Q(1 if n % 2 == 0 else -1)


def dual(v):
    dims, ds = v
    return ({-n: size for n, size in dims.items()},
            {-n-1: scale(transpose(d), sign(-n)) for n, d in ds.items()})


class DualityTests(unittest.TestCase):
    def setUp(self):
        self.v = ({0: 1, 1: 2, 2: 1},
                  {0: ((Q(1),), (Q(0),)), 1: ((Q(0), Q(1)),)})

    def test_d_squared_zero_in_both_complexes(self):
        for dims, ds in (self.v, dual(self.v)):
            for n in ds:
                if n+1 in ds:
                    self.assertTrue(all(x == 0 for row in mul(ds[n+1], ds[n]) for x in row))

    def test_double_dual_differential_and_signed_evaluation(self):
        dims, ds = self.v
        ddims, dds = dual(dual(self.v))
        self.assertEqual(ddims, dims)
        for n, d in ds.items():
            self.assertEqual(dds[n], scale(d, -1))
            self.assertEqual(mul(dds[n], scale(eye(dims[n]), sign(n))),
                             mul(scale(eye(dims[n+1]), sign(n+1)), d))

    def test_unsigned_evaluation_fails(self):
        d = self.v[1][0]
        dd = dual(dual(self.v))[1][0]
        self.assertNotEqual(dd, d)

    def test_triangle_on_every_dual_degree(self):
        for n, size in dual(self.v)[0].items():
            eta_dual = scale(eye(size), sign(n))
            dual_eta = transpose(scale(eye(size), sign(-n)))
            self.assertEqual(mul(dual_eta, eta_dual), eye(size))

    def test_nonexact_complex_not_erased(self):
        v = ({-1: 1, 0: 1}, {-1: ((Q(0),),)})
        self.assertEqual(dual(dual(v)), v)
        self.assertEqual(dual(dual(dual(v))), dual(v))
        self.assertEqual(sum(v[0].values()), 2)

    def test_odd_chern_component_not_self_dual_but_third_repeats(self):
        for p in range(7):
            alpha = Q(3, 7)
            first = sign(p)*alpha
            third = sign(p)**3*alpha
            self.assertEqual(third, first)
            if p % 2:
                self.assertNotEqual(first, alpha)


if __name__ == '__main__':
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(DualityTests))
    receipt = {
        'passed': result.wasSuccessful(), 'tests': result.testsRun,
        'classification': 'derived_duality_repeats_not_an_algebraicity_detector',
        'residuals': ['algebraic_specific_operation_beyond_duality_not_supplied'],
        'next_falsifier': 'A source-derived operation with all-cycle necessity and a rational class-level failure.',
        'Hodge_proved': False, 'Hodge_refuted': False,
        'verification_scope': 'Finite rational cochain signs and triangle only; geometry and topological K comparison use written imported theorems.'
    }
    root = Path(__file__).resolve().parents[3]
    out = root/'research/voevodsky/results/hodge-derived-duality-realization-v1.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(receipt))
    raise SystemExit(0 if result.wasSuccessful() else 1)
