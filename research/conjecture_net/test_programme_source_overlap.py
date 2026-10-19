import json
import unittest
from check_programme_source_overlap import HOME, validate


class OverlapAttachmentTests(unittest.TestCase):
    def setUp(self):
        self.hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v12.json').read_text())
        self.receipt = json.loads((HOME / 'results/source-overlap-screen-audit.json').read_text())

    def test_live_indexed_package_and_restricted_screen(self):
        result = validate(self.hierarchy, self.receipt)
        self.assertEqual(result['faithful_indexed_package_dimension'], 26)
        self.assertEqual(result['typed_closed_words_through_length_12'], 840)
        self.assertFalse(result['one_common_physical_witness'])

    def test_package_not_renamed_physical_unification(self):
        self.hierarchy['cross_source_overlap_screens'][0]['one_common_physical_witness'] = 'proved'
        with self.assertRaisesRegex(ValueError, 'physical unification'):
            validate(self.hierarchy, self.receipt)

    def test_finite_screen_not_promoted_to_all_word_no_go(self):
        self.receipt['word_or_endpoint_dependent_bindings_ruled_out'] = True
        with self.assertRaisesRegex(ValueError, 'verification upgrade'):
            validate(self.hierarchy, self.receipt)


if __name__ == '__main__':
    unittest.main()
