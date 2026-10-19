import copy
from fractions import Fraction as Q
import json
import unittest

import check_photon_local_ward_basis_v1 as w


class LocalWardBasisTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result=w.build()

    def test_fresh_receipt(self):
        self.assertEqual(json.loads(w.RESULT.read_text(encoding='utf-8')),self.result)

    def test_full_tensor_components_and_Ward_constraints(self):
        self.assertEqual(self.result['one_point_tensor_components'],2048)
        self.assertEqual(self.result['one_point_component_Ward_constraints'],2048)

    def test_forward_jet_not_single_energy_rank(self):
        self.assertEqual(w.forward_map(),tuple(tuple(map(Q,r)) for r in (
            (1,0,0,0,0,0,0,0),(0,0,1,0,0,0,0,0),(0,0,0,0,0,1,0,0),
            (0,2,0,0,0,0,0,0),(0,0,0,0,0,0,0,4))))
        self.assertEqual(self.result['forward_rank'],5)

    def test_exact_coordinate_kernel(self):
        expected=tuple(tuple(Q(int(j==i)) for j in range(8)) for i in (3,4,6))
        self.assertEqual(w.nullspace(w.forward_map()),expected)

    def test_full_local_coefficient_independence(self):
        rows=[[Q(x) for x in r] for r in self.result['full_independence_witness_rows']]
        self.assertEqual(len(w.reduced_rows(rows)[1]),8)

    def test_off_forward_invisible_minor_is_invertible(self):
        expected=tuple(tuple(Q(144,625) if i==j else Q() for j in range(3)) for i in range(3))
        self.assertEqual(tuple(tuple(map(Q,r)) for r in self.result['nonforward_invisible_minor']),expected)

    def test_dropping_single_minus_is_not_a_forward_diagnostic(self):
        self.assertEqual(self.result['drop_h3_full_rank'],7)
        self.assertTrue(all(row[4]==0 for row in w.forward_map()))
        self.assertEqual(w.amplitude_rows(Q(3,5),Q(4,5))[4][4],Q(144,625))

    def test_Ward_alone_does_not_imply_Bose(self):
        self.assertEqual(Q(self.result['single_pair_f2_Bose_defect']),Q(369,625))

    def test_field_strength_Ward_without_null_assumption(self):
        q=((Q(2),Q(3)),(Q(5),Q(7)))
        self.assertNotEqual(w.determinant(q),0)
        self.assertEqual(w.fields(q,q),(w.Z,w.Z))

    def test_all_helicity_controls_include_backward_and_forward_patches(self):
        self.assertEqual(self.result['counts']['helicity'],64)
        self.assertEqual(self.result['counts']['reference'],64)
        self.assertEqual(self.result['counts']['Bose'],72)

    def test_local_result_cannot_promote_to_loop_or_native_result(self):
        c=json.loads(w.CONTRACT.read_text(encoding='utf-8'))
        for key in ('loop_tensor_lift_constructed','window_shift_lift_constructed',
                    'joint_analyticity_of_full_amplitude_derived','off_shell_operator_basis_exhausted',
                    'finite_matching_coefficients_selected','native_preparation_or_physical_rates_derived'):
            bad=copy.deepcopy(c);bad[key]=True
            with self.assertRaises(AssertionError,msg=key):w.validate_contract(bad)

    def test_no_parameter_erasure(self):
        c=json.loads(w.CONTRACT.read_text(encoding='utf-8'));c['coefficient_order'].remove('h3')
        with self.assertRaises(AssertionError):w.validate_contract(c)


if __name__=='__main__':unittest.main()
