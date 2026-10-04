"""Hostile tests for generation, independent replay, and nonpromotion gates."""
import ast
import copy
import io
import json
from contextlib import redirect_stdout
from itertools import product
from pathlib import Path
import unittest

import algebra_formula_search as search
from check_algebra_synthesis import (BASE, TARGET, audit_lower, audit_supplement,
    catalan, completions, check_model, direct_holds, freeze, select_cached_adequacy, unrank)


class SynthesisTests(unittest.TestCase):
    def test_independent_unranking_and_coverage(self):
        for cost in range(5):
            seen = set()
            for ordinal, candidate in enumerate(search.candidates(cost)):
                self.assertEqual(candidate, unrank(cost, ordinal))
                self.assertNotIn(candidate, seen)
                seen.add(candidate)
            self.assertEqual(len(seen), catalan(cost + 1) * completions(cost + 1, 1))

    def test_bitplanes_against_scalar_all_two_element_operations(self):
        for left, right, variables in search.candidates(2):
            for table in product(range(2), repeat=4):
                self.assertEqual(search.satisfies(left, right, variables, 2, table),
                                 direct_holds(left, right, variables, 2, table))

    def test_specialized_boolean_filter_against_scalar(self):
        for left, right, variables in search.candidates(3):
            for term in (left, right):
                bits = search.nand_value(term, variables)
                from check_algebra_synthesis import scalar
                for i, assignment in enumerate(product(range(2), repeat=variables)):
                    self.assertEqual((bits >> i) & 1, scalar(term, assignment, 2, (1, 1, 1, 0)))

    def test_scalar_against_ternary_bitplanes(self):
        tables = [(0,) * 9, tuple(range(3)) * 3, (2, 2, 2, 2, 1, 1, 2, 1, 0)]
        for left, right, variables in search.candidates(2):
            for table in tables:
                self.assertEqual(search.satisfies(left, right, variables, 3, table),
                                 direct_holds(left, right, variables, 3, table))

    def test_obstructions_are_witnesses_not_model_labels(self):
        for table in product(range(2), repeat=4):
            failure = search.obstruction(2, table)
            self.assertEqual(failure is None, table in ((1, 1, 1, 0), (1, 0, 0, 0)))
            if failure:
                check_model({'size': 2, 'table': table, 'obstruction': failure})
        # Three-valued De Morgan NAND satisfies the first three necessary laws,
        # but not Boolean complement/top independence.
        self.assertEqual(search.obstruction(3, (2, 2, 2, 2, 1, 1, 2, 1, 0))['law'], 'top-independence')

    def test_fake_countermodel_rejected(self):
        with self.assertRaises(AssertionError):
            check_model({'size': 2, 'table': (1, 1, 1, 0),
                         'obstruction': {'law': 'commutativity', 'assignment': [0, 1]}})

    def test_malformed_countermodels_rejected(self):
        for size, table in [(0, []), (True, [0]), (2, [0]), (2, [0, 0, True, 1]), (2, [0, 0, 0, 2])]:
            with self.assertRaises(AssertionError):
                check_model({'size': size, 'table': table,
                             'obstruction': {'law': 'commutativity', 'assignment': [0, 1]}})

    def test_no_quotient_by_boolean_truth_or_commutativity(self):
        self.assertEqual(search.nand_value((0, 1), 2), search.nand_value((1, 0), 2))
        self.assertNotEqual((0, 1), (1, 0))
        self.assertIn(((0, 1), (1, 0), 2), set(search.candidates(2)))
        # Neither equal Boolean values nor universal validity makes an identity adequate.
        with redirect_stdout(io.StringIO()):
            packet = search.search(2, 2)
        self.assertEqual(packet['survivors'], [])

    def test_bounds(self):
        for cost, size, discovery in [(-1, 2, 5), (7, 2, 5), (True, 2, 5), (2, 4, 5), (2, 2, 6)]:
            with self.assertRaises(ValueError):
                search.search(cost, size, discovery)

    def test_generator_has_no_adequacy_backend_dependency(self):
        tree = ast.parse(Path(search.__file__).read_text(encoding='utf-8'))
        imports = {n.module for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)}
        imports |= {a.name for n in ast.walk(tree) if isinstance(n, ast.Import) for a in n.names}
        self.assertLessEqual(imports, {'functools', 'itertools', 'argparse', 'hashlib', 'json', 'pathlib'})
        self.assertNotIn('TARGET', {n.id for n in ast.walk(tree) if isinstance(n, ast.Name)})

    def test_missing_and_forged_held_out_target(self):
        with self.assertRaises(AssertionError):
            select_cached_adequacy({'survivors': []})
        wrong = {'left': TARGET[0], 'right': TARGET[1], 'cost': 6, 'ordinal': 0, 'variables': 3}
        with self.assertRaises(AssertionError):
            select_cached_adequacy({'survivors': [wrong]})

    def test_missing_rejection_is_not_coverage(self):
        with redirect_stdout(io.StringIO()):
            packet = search.search(2, 2)
        audit_lower(packet, 3)
        forged = copy.deepcopy(packet)
        forged['rejections'].pop()
        with self.assertRaises(AssertionError):
            audit_lower(forged, 3)

    def test_duplicate_rejection_rejected(self):
        with redirect_stdout(io.StringIO()):
            packet = search.search(0, 2)
        packet['rejections'] *= 2
        with self.assertRaises(AssertionError):
            audit_lower(packet, 1)

    def test_budget_exhaustion_does_not_discharge_obligation(self):
        minimum = {'unresolved': [(4, 1072)], 'kernel_checked_minimality': False}
        report = {'cost': 4, 'ordinal': 1072, 'status': 'budget-exhausted-not-a-refutation'}
        result = audit_supplement(minimum, {'reports': [report]})
        self.assertEqual(result['unresolved'], [(4, 1072)])
        self.assertFalse(result['runtime_certificate_package_constructed'])

    def test_supplement_replayed_and_tampering_rejected(self):
        data = json.loads((BASE / 'results/algebra-finite-sat.json').read_text(encoding='utf-8'))
        minimum = {'unresolved': [(r['cost'], r['ordinal']) for r in data['reports']],
                   'kernel_checked_minimality': False, 'agda_sigma_package_constructed': False}
        result = audit_supplement(minimum, data)
        self.assertEqual(result['unresolved'], [])
        self.assertFalse(result['kernel_checked_minimality'])
        self.assertFalse(result['agda_sigma_package_constructed'])
        bad = copy.deepcopy(data)
        bad['reports'][0]['model']['table'] = [0] * 16
        with self.assertRaises(AssertionError):
            audit_supplement(minimum, bad)

    def test_omitted_supplement_stays_open(self):
        data = json.loads((BASE / 'results/algebra-finite-sat.json').read_text(encoding='utf-8'))
        minimum = {'unresolved': [(r['cost'], r['ordinal']) for r in data['reports']]}
        data['reports'].pop()
        result = audit_supplement(minimum, data)
        self.assertEqual(len(result['unresolved']), 1)
        self.assertFalse(result['runtime_certificate_package_constructed'])

    def test_discovered_model_has_no_two_element_nand_quotient(self):
        data = json.loads((BASE / 'results/algebra-finite-sat.json').read_text(encoding='utf-8'))
        table = data['reports'][0]['model']['table']
        quotients = [f for f in product(range(2), repeat=4)
                     if all(f[table[4*x+y]] == 1 - (f[x] & f[y]) for x, y in product(range(4), repeat=2))]
        self.assertEqual(quotients, [])

    def test_term_decoder(self):
        for malformed in [True, -1, 9, None, [0], [0, 1, 2], 'x']:
            with self.assertRaises(ValueError):
                freeze(malformed)


if __name__ == '__main__':
    unittest.main()
