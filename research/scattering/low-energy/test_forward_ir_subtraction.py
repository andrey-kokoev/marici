import copy
import json
import unittest
from fractions import Fraction as Q
import check_forward_ir_subtraction as sub


class ForwardIRSubtractionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=sub.build()

    def test_receipt(self):
        self.assertEqual(self.result,json.loads(sub.RESULT.read_text(encoding='utf-8')))
        for key,value in (('forward_and_crossed_coefficient_norm_checks',49),('paired_Cauchy_division_checks',18),
                          ('analytic_remainder_coefficient_checks',33),('window_cocycle_checks',33),
                          ('reference_window_compatibility_checks',33),('endpoint_window_flow_checks',66),
                          ('rim_residue_checks',12),('missing_improved_contour_controls_refused',8)):
            self.assertEqual(self.result[key],value)

    def test_logarithmic_degree_and_transport(self):
        coeff=sub.coefficients({2:Q(1)});a,b,d=Q(1,4),Q(1,2),Q(3,4)
        self.assertEqual(sub.shell(coeff,4,a,b),sub.log_form(sub.cross.crossed_sum(coeff[4],4),b,a))
        self.assertEqual(sub.shell(coeff,8,a,d),sub.add_form(sub.shell(coeff,8,a,b),sub.shell(coeff,8,b,d)))
        self.assertEqual(sub.analytic_coefficient(coeff,4,b,b),{})
        self.assertEqual(self.result['c0_only_unnormalized_n2_shell'],{'Bell_plus':'-37/5120','product_plus':'63/5120'})
        self.assertLess(sub.remainder_tail(48,b,a),Q(1,10**10))
        with self.assertRaises(AssertionError):sub.remainder_tail(48,b,Q(1,3))

    def test_positive_shell_not_matrix_order_and_conditional_gate(self):
        c=self.result['spectral_comparison']
        self.assertTrue(all(Q(box[0])>0 for box in c['positive_right_shell_eigenvalue_boxes'].values()))
        self.assertLess(Q(c['paired_Bell_plus_box'][1]),0)
        self.assertGreater(Q(c['paired_product_plus_box'][0]),0)
        assumptions={key:True for key in ('entire_retained_IR_cut_subtracted','regular_matching_and_exhaustive_IR_inventory',
            'poles_and_forward_limit_accounted','large_arc_zero_at_n','global_cut_positive_at_same_scope',
            'jet_and_cut_same_scope','forward_crossing_and_Hermitian_analyticity')}
        self.assertTrue(sub.improved_dispersion_gate(8,2,assumptions))
        with self.assertRaises(AssertionError):sub.improved_dispersion_gate(8,2,{})
        with self.assertRaises(AssertionError):sub.improved_dispersion_gate(2,4,assumptions)
        self.assertFalse(self.result['physical_IR_improved_amplitude_constructed'])
        self.assertFalse(self.result['finite_matching_fixed_or_bounded'])
        self.assertEqual(len(self.result['hostile_controls_refused']),8)

    def test_contract_guards(self):
        c=json.loads(sub.CONTRACT.read_text(encoding='utf-8'))
        for key,value in c.items():
            if isinstance(value,bool):
                bad=copy.deepcopy(c);bad[key]=not value
                with self.subTest(key=key),self.assertRaises(AssertionError):sub.validate_contract(bad)
        bad=copy.deepcopy(c);bad['kernel']='subtract_only_the_leading_cut_density'
        with self.assertRaises(AssertionError):sub.validate_contract(bad)


if __name__=='__main__':unittest.main()
