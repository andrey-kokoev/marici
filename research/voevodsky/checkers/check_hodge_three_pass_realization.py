"""Exact regression controls; no computed Chow group or Hodge verdict."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[3]


def mul(a, b):
    return tuple(tuple(sum(x*y for x, y in zip(row, col))
                       for col in zip(*b)) for row in a)


def compose(f, g):
    return tuple(f[x] for x in g)


class ThreePassTests(unittest.TestCase):
    def test_all_two_point_maps(self):
        maps = list(product(range(2), repeat=2))
        count = 0
        for c, r in product(maps, repeat=2):
            if compose(r, c) == (0, 1) or compose(c, r) == (0, 1):
                self.assertEqual(compose(c, compose(r, c)), c)
                count += 1
        self.assertEqual(count, 2)

    def test_section_recovers_class_not_representative(self):
        c = ((Q(1), Q(0)),)
        r = ((Q(1),), (Q(0),))
        d = ((Q(0),), (Q(1),))
        self.assertEqual(mul(c, r), ((Q(1),),))
        self.assertEqual(mul(mul(c, r), c), c)
        self.assertEqual(mul(mul(r, c), r), r)
        self.assertNotEqual(mul(mul(r, c), d), d)
        self.assertEqual(mul(c, d), ((Q(0),),))
        self.assertEqual(mul(mul(mul(r, c), r), c), mul(r, c))

    def test_bad_return_is_not_a_section(self):
        c = ((Q(1), Q(0)),)
        bad = ((Q(2),), (Q(0),))
        self.assertNotEqual(mul(mul(c, bad), c), c)
        self.assertNotEqual(mul(c, bad), ((Q(1),),))

    def test_partial_capability_third_step_fails(self):
        ready, spent = ('same value', True), ('same value', False)
        c, r = {ready: 'packet'}, {'packet': spent}
        returned = r[c[ready]]
        self.assertEqual(returned[0], ready[0])
        self.assertNotEqual(returned, ready)
        with self.assertRaises(KeyError):
            c[returned]

    def test_retaining_capability_repairs_this_fixture(self):
        ready = ('same value', True)
        c, r = {ready: 'packet'}, {'packet': ready}
        self.assertEqual(c[r[c[ready]]], c[ready])

    def test_class_erasure_hides_nonzero_reader(self):
        c = ((Q(1), Q(0)),)
        reader = ((Q(0), Q(1)),)
        kernel = ((Q(0),), (Q(1),))
        self.assertEqual(mul(c, kernel), ((Q(0),),))
        self.assertEqual(mul(reader, kernel), ((Q(1),),))


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ThreePassTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    receipt = {
        'passed': result.wasSuccessful(), 'tests': result.testsRun,
        'classification': 'standard_class_maps_repeat_enriched_operation_missing',
        'residuals': ['no_source_derived_partial_Hodge_realization_operation',
                      'no_all_algebraic_cycle_necessity_for_enriched_repetition'],
        'next_falsifier': 'Source-derived third-pass failure that survives cohomology comparison and excludes every algebraic representative.',
        'Hodge_proved': False, 'Hodge_refuted': False,
        'geometric_facts': 'Imported Poincare duality and elliptic Picard facts; not computed or formalized here.',
    }
    out = ROOT / 'research/voevodsky/results/hodge-three-pass-realization-v1.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(receipt))
    raise SystemExit(0 if result.wasSuccessful() else 1)
