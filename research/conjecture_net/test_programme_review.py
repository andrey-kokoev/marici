import copy
import unittest
from check_programme_review import documents, validate


class ProgrammeReviewTests(unittest.TestCase):
    def setUp(self):
        self.hierarchy, self.terms, self.review = copy.deepcopy(documents())

    def check(self):
        return validate(self.hierarchy, self.terms, self.review)

    def test_review_checkpoint(self):
        result = self.check()
        self.assertEqual(result['candidate_terms'], 4)
        self.assertEqual(result['candidate_links'], 5)
        self.assertEqual(result['admitted_links'], 0)
        self.assertIsNone(result['root_outcome'])

    def test_source_drift_rejected(self):
        self.review['sources'][0]['source_sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'stale reviewed source'):
            self.check()

    def test_premature_root_closure_rejected(self):
        self.hierarchy['root']['outcome'] = '++'
        with self.assertRaisesRegex(ValueError, 'premature programme'):
            self.check()

    def test_candidate_link_promotion_rejected(self):
        self.hierarchy['existing_net_links'][0]['status'] = 'admitted'
        with self.assertRaisesRegex(ValueError, 'cannot admit proof'):
            self.check()

    def test_unknown_source_claim_rejected(self):
        self.hierarchy['existing_net_links'][0]['source_claim'] = 'all-physics-proved'
        with self.assertRaisesRegex(ValueError, 'unknown source claim'):
            self.check()

    def test_unreviewed_term_selection_rejected(self):
        term = next(t for t in self.terms['terms'] if t['id'] == 'physical_targets')
        term['definition'] = 'all physics'
        with self.assertRaisesRegex(ValueError, 'unreviewed term promoted'):
            self.check()

    def test_definition_evidence_upgrade_rejected(self):
        self.terms['terms'][0]['evidence'][0]['role'] = 'kernel_proof_of_common_carrier'
        with self.assertRaisesRegex(ValueError, 'evidence upgrade'):
            self.check()

    def test_same_witness_requirement_cannot_be_removed(self):
        self.hierarchy['promotion_policy']['common_witness_transport_required'] = False
        with self.assertRaisesRegex(ValueError, 'unsafe promotion'):
            self.check()


if __name__ == '__main__':
    unittest.main()
