import copy
import json
import unittest
from fractions import Fraction as Q
import check_forward_crossing_positivity as cross


class ForwardCrossingPositivityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=cross.build()

    def test_receipt(self):
        self.assertEqual(self.result,json.loads(cross.RESULT.read_text(encoding='utf-8')))
        for key,value in (('Gamma_matrix_unit_checks',16),('Gamma_self_adjoint_checks',256),
                          ('field_crossing_matrix_checks',18),('physical_helicity_section_checks',288),
                          ('local_cut_free_counterterm_section_checks',64),('complex_product_preparation_checks',75),
                          ('restricted_cone_controls',12),('missing_contour_or_scope_controls_refused',8)):
            self.assertEqual(self.result[key],value)

    def test_crossing_is_not_positive_and_entanglement_is_not_blanket_excluded(self):
        bell=cross.scale(Q(1,2),cross.outer([Q(1),Q(1),Q(),Q()]))
        self.assertTrue(cross.is_psd(bell))
        self.assertFalse(cross.is_psd(cross.gamma(bell)))
        identity=[[Q(int(i==j)) for j in range(4)] for i in range(4)]
        rho=cross.add(cross.scale(Q(3,20),identity),cross.scale(Q(2,5),bell))
        self.assertFalse(cross.is_psd(cross.gamma(rho)))
        self.assertTrue(cross.is_psd(cross.crossed_sum(rho,2)))
        self.assertFalse(cross.restricted_even_safe(bell))
        self.assertEqual(self.result['c0_only_tau_half_even_n2_Bell_plus'],'-37/3840')
        self.assertLess(Q(self.result['spectral_zero_subtraction_pi_squared_even_n2_Bell_plus_box'][1]),0)

    def test_conditional_not_admitted(self):
        assumptions={key:True for key in ('poles_and_forward_limit_accounted','regular_IR_matching_jet_and_cut_inventory',
            'large_arc_zero_at_n','global_cut_positive_at_same_scope','jet_and_cut_same_scope','forward_crossing_and_Hermitian_analyticity')}
        self.assertTrue(cross.conditional_dispersion_gate(2,2,2,assumptions))
        with self.assertRaises(AssertionError):cross.conditional_dispersion_gate(2,4,2,assumptions)
        with self.assertRaises(AssertionError):cross.conditional_dispersion_gate(4,2,2,assumptions)
        with self.assertRaises(AssertionError):cross.conditional_dispersion_gate(2,2,2,{})
        self.assertFalse(self.result['finite_matching_fixed_or_bounded'])
        self.assertFalse(self.result['UV_fixed_order_spectral_positivity_derived'])
        self.assertEqual(len(self.result['hostile_controls_refused']),8)

    def test_contract_guards(self):
        c=json.loads(cross.CONTRACT.read_text(encoding='utf-8'))
        for key,value in c.items():
            if isinstance(value,bool):
                bad=copy.deepcopy(c);bad[key]=not value
                with self.subTest(key=key),self.assertRaises(AssertionError):cross.validate_contract(bad)
        bad=copy.deepcopy(c);bad['gamma']='ordinary_pair_exchange'
        with self.assertRaises(AssertionError):cross.validate_contract(bad)


if __name__=='__main__':unittest.main()
