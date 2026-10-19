import json
import unittest
from source_overlap_screen import fixed_port_bindings, validate_indexed_word, tag_record, restore_record
from check_source_overlap_screen import HOME, audit, validate_contract


class SourceOverlapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.controls = audit()

    def test_all_distinct_port_bindings_erase_three_characters(self):
        rows = [row for row in self.controls['fixed_port_assignments'] if row['ports'][0] != row['ports'][1]]
        self.assertEqual(len(rows), 30)
        self.assertTrue(all(row['maximum_map_rank'] == 1 and row['mismatch_intertwiner_space_dimension'] == 4
                            and row['full_anchor_plus_mismatch_intertwiner_space_dimension'] == 20 for row in rows))

    def test_same_port_binding_is_only_a_rank_two_quotient(self):
        rows = [row for row in self.controls['fixed_port_assignments'] if row['ports'][0] == row['ports'][1]]
        self.assertEqual(len(rows), 6)
        self.assertTrue(all(row['maximum_map_rank'] == 2 and row['mismatch_intertwiner_space_dimension'] == 6 for row in rows))
        self.assertFalse(self.controls['faithful_fixed_port_overlap_found'])

    def test_all_typed_closed_words_within_declared_horizon(self):
        loops = self.controls['bounded_typed_loop_screen']
        self.assertEqual(loops['closed_nonempty_word_count'], 840)
        self.assertEqual(loops['base_vertices'], ['A', 'B', 'C', 'D'])
        self.assertEqual(loops['maximum_word_length'], 12)
        self.assertEqual(loops['negative_eigenspace_dimension_counts'], {'0': 520, '1': 320})
        self.assertEqual(loops['faithful_fixed_fibre_native_flip_candidates'], 0)

    def test_indexed_package_preserves_both_sources(self):
        self.assertEqual(self.controls['package_dimension'], 26)
        self.assertEqual(self.controls['isometric_source_inclusion_count'], 2)
        self.assertEqual(self.controls['packaged_metric_involution_count'], 8)
        self.assertEqual(self.controls['coordinate_quadratic_pullbacks'], 26)
        self.assertTrue(self.controls['source_records_retained'])

    def test_mixed_source_execution_rejected(self):
        with self.assertRaisesRegex(ValueError, 'cross-source arrow not supplied'):
            validate_indexed_word((('bool', 'left'), ('exchange', 'AB')))

    def test_exchange_seams_still_required_inside_package(self):
        with self.assertRaisesRegex(ValueError, 'unmatched source port seam'):
            validate_indexed_word((('exchange', 'AB'), ('exchange', 'AD')))

    def test_record_namespace_not_silently_changed(self):
        source_record = object()
        tagged = tag_record('bool', source_record)
        self.assertIs(restore_record(tagged, 'bool'), source_record)
        with self.assertRaisesRegex(ValueError, 'component mismatch'):
            restore_record(tagged, 'exchange')

    def test_restricted_obstruction_not_universalized(self):
        contract = json.loads((HOME / 'contracts/source-overlap-screen.v1.json').read_text())
        contract['boundary']['word_or_endpoint_dependent_bindings_ruled_out'] = True
        with self.assertRaisesRegex(ValueError, 'boundary promotion'):
            validate_contract(contract)

    def test_package_not_promoted_to_common_physical_witness(self):
        contract = json.loads((HOME / 'contracts/source-overlap-screen.v1.json').read_text())
        contract['boundary']['one_common_physical_witness_proved'] = True
        with self.assertRaisesRegex(ValueError, 'boundary promotion'):
            validate_contract(contract)


if __name__ == '__main__':
    unittest.main()
