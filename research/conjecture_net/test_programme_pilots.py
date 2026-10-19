import copy
import unittest
from check_programme_pilots import documents, validate


class PilotTests(unittest.TestCase):
    def setUp(self):
        self.hierarchy, self.terms, self.interface, self.targets, self.review = copy.deepcopy(documents())

    def check(self):
        return validate(self.hierarchy, self.terms, self.interface, self.targets, self.review)

    def test_candidate_specification(self):
        result = self.check()
        self.assertEqual(result['source_primitives'], 8)
        self.assertEqual(result['proposed_targets'], 3)
        self.assertEqual(result['empirical_datasets'], 0)
        self.assertEqual(result['unresolved_terms'], ['shared_regimes'])

    def test_premature_root_promotion(self):
        self.hierarchy['root']['outcome'] = '++'
        with self.assertRaisesRegex(ValueError, 'root promotion'):
            self.check()

    def test_inherited_proof_does_not_prove_pilot(self):
        self.targets['targets'][0]['outcome'] = '++'
        with self.assertRaisesRegex(ValueError, 'pilot outcome'):
            self.check()

    def test_empirical_success_without_data(self):
        self.targets['targets'][2]['physical_confirmation'] = True
        with self.assertRaisesRegex(ValueError, 'empirical confirmation'):
            self.check()

    def test_inserting_common_carrier_map(self):
        self.interface['first_source_instance']['common_carrier_embedding'] = 'identity'
        with self.assertRaisesRegex(ValueError, 'unproved carrier embedding'):
            self.check()

    def test_imported_law_cannot_be_promoted_to_derivation(self):
        self.targets['empirical_policy']['imported_law_is_derived_law'] = True
        with self.assertRaisesRegex(ValueError, 'circularity'):
            self.check()

    def test_source_review_drift(self):
        self.review['sources'][0]['source_sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'stale pilot source'):
            self.check()

    def test_pilot_same_source_mismatch(self):
        self.targets['targets'][1]['source_instance'] = 'unrelated'
        with self.assertRaisesRegex(ValueError, 'same-source pilot mismatch'):
            self.check()


if __name__ == '__main__':
    unittest.main()
