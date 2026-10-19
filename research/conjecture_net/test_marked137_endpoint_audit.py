from dataclasses import replace
import json
import unittest
from marked137_endpoint_audit import source_table, MarkedEndpointObserver
from check_marked137_endpoint_audit import audit, validate_contract, CONTRACT


class MarkedEndpointTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = source_table()
        cls.observer = MarkedEndpointObserver(cls.source['source'])
        cls.controls = audit()

    def test_endpoint_roles_change_grouping_without_changing_J4(self):
        self.assertEqual(self.controls['first_families_using_carrier_target'], 32)
        self.assertEqual(self.controls['first_families_using_assembly_target'], 1)
        self.assertTrue(self.controls['same_fixed_J4_under_role_view'])
        self.assertEqual(self.controls['original_rows_recovered'], 137)

    def test_153_rule_only_partially_overlaps_137_domain(self):
        self.assertEqual(self.controls['parent153_marked137_overlap'], 130)
        self.assertEqual(len(self.controls['marked_states_outside_parent_domain']), 7)
        self.assertEqual(self.controls['partial_endpoint_readouts'], 145)
        self.assertEqual(self.controls['reachable_state_keys'], 9)

    def test_reference_index_exclusion_not_removed(self):
        parent = self.source['source'][0]
        with self.assertRaisesRegex(ValueError, 'reference-index0 exclusion'):
            self.observer.observe(parent, 0)
        self.assertEqual(self.observer.observe(parent, 1).observed_state_key, ('s', 2, 2))

    def test_parent_restore_does_not_make_coarse_readout_invertible(self):
        parent = self.source['source'][0]
        packet = self.observer.observe(parent, 1)
        self.assertIs(self.observer.restore_parent(packet), parent)
        with self.assertRaisesRegex(ValueError, 'not an invertible connector'):
            self.observer.inverse(packet)

    def test_full_response_collision_not_erased(self):
        hostile = self.controls['response_descent_hostile']
        self.assertNotEqual(hostile['parent_values'][0], hostile['parent_values'][1])
        self.assertEqual(hostile['state_key'], ['s', 2, 2])
        packet = self.observer.observe(self.source['source'][0], 1)
        with self.assertRaisesRegex(ValueError, 'no response-level'):
            self.observer.state_response(packet)

    def test_corrupted_packet_rejected(self):
        packet = self.observer.observe(self.source['source'][0], 1)
        with self.assertRaisesRegex(ValueError, 'corrupted endpoint packet'):
            self.observer.restore_parent(replace(packet, observed_state_key=('s', 1, 1)))

    def test_foreign_parent_response_rejected(self):
        parent = self.source['source'][0]
        with self.assertRaisesRegex(ValueError, 'foreign or changed'):
            self.observer.observe(replace(parent, mass=2), 1)

    def test_no_intended_T9_promotion(self):
        contract = json.loads(CONTRACT.read_text())
        contract['boundary']['intended_T9_selected'] = True
        with self.assertRaisesRegex(ValueError, 'boundary promotion'):
            validate_contract(contract)


if __name__ == '__main__':
    unittest.main()
