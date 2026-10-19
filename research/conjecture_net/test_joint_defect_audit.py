import json
import unittest
from joint_defect_audit import source_interfaces, nullspace, act
from check_joint_defect_audit import audit, validate_contract, CONTRACT


class JointDefectTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.controls = audit()

    def test_actual_label_bound_ranks(self):
        self.assertEqual(self.controls['bound_original_slot_labels'], 137)
        self.assertEqual(self.controls['assembly_boundary_rank'], 28)
        self.assertEqual(self.controls['family_incidence_rank'], 47)
        self.assertEqual(self.controls['joint_rank'], 55)
        self.assertEqual(self.controls['joint_kernel_dimension'], 82)

    def test_kernels_not_identified_or_nested(self):
        self.assertEqual(self.controls['assembly_kernel_visible_to_family_dimension'], 27)
        self.assertEqual(self.controls['family_kernel_visible_to_assembly_dimension'], 8)
        self.assertTrue(all(self.controls['kernel_inclusion_hostiles'].values()))

    def test_unchanged_source_falsifies_sewing(self):
        hostile = self.controls['fixed_source_sewing_hostile']
        self.assertEqual(hostile['coefficients'], {'0': '1', '3': '-1', '11': '-1', '14': '1'})
        self.assertEqual(hostile['response'], [['0', '0'], ['0', '1/5']])
        self.assertEqual(self.controls['governing_conjecture'], 'falsified_on_the_unchanged_actual_shared_leg_assignment')

    def test_fixed_response_completion_not_uniform(self):
        self.assertEqual(self.controls['joint_plus_fixed_response_rank'], 56)
        self.assertEqual(self.controls['fixed_completed_kernel_dimension'], 81)
        self.assertEqual(self.controls['fixed_completion_nonuniform_hostile']['mixed_response'], [['0', '0'], ['0', '-1']])
        self.assertEqual(self.controls['uniform_source_probe_count'], 137)
        self.assertEqual(self.controls['uniform_source_response_minimum_linear_rank'], 137)

    def test_complete_joint_kernel_certificate_retained(self):
        self.assertEqual(len(self.controls['joint_kernel_basis']), 82)
        self.assertTrue(all(vector for vector in self.controls['joint_kernel_basis']))

    def test_different_grades_preserved(self):
        self.assertEqual(self.controls['assembly_cell_degree'], 2)
        self.assertEqual(self.controls['family_incidence_edge_degree'], 1)
        self.assertFalse(self.controls['chain_map_constructed'])

    def test_physical_preparation_not_inferred_from_probes(self):
        contract = json.loads(CONTRACT.read_text())
        contract['boundary']['physical_preparations_authorized'] = True
        with self.assertRaisesRegex(ValueError, 'boundary promotion'):
            validate_contract(contract)

    def test_frozen_completion_not_renamed_uniform(self):
        contract = json.loads(CONTRACT.read_text())
        contract['boundary']['fixed_source_rank56_completion_is_uniform'] = True
        with self.assertRaisesRegex(ValueError, 'boundary promotion'):
            validate_contract(contract)


if __name__ == '__main__':
    unittest.main()
