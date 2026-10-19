from fractions import Fraction as Q
import json
import unittest

import check_photon_joint_cut_fibres_v1 as t


class JointCutFibreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_exhaustive_stratum_controls(self):
        self.assertEqual(self.r['source_chart_checks'],{'ordinary':3000,'single-minus-cancellation':54,'zero-leading':125})
        self.assertEqual(self.r['calibrations_against_independent_cut_coefficients'],243)

    def test_generic_sign_pair_not_selected(self):
        x=(Q(1),Q(2),Q(3),Q(4),Q(5));c=t.chart(t.observe(x))
        self.assertEqual(c['free_indices'],())
        self.assertEqual(t.observe_scaled(*t.instantiate(c,sign=1)),t.observe_scaled(*t.instantiate(c,sign=-1)))
        self.assertFalse(self.r['physical_Born_sign_selected'])

    def test_nontrivial_h3_fibre(self):
        c=t.chart(t.observe((1,-6,2,3,7)))
        self.assertEqual(c['free_indices'],(4,))
        self.assertEqual(self.r['cancellation_witness']['single_minus_Born_difference'],'1008/625')

    def test_zero_g2_chart_is_not_zero_leading(self):
        c=t.chart(t.observe((0,2,3,4,5)))
        self.assertEqual(c['chart'],'f2-positive');self.assertEqual(c['stratum'],'ordinary')
        self.assertEqual(t.chart((0,0,0,0,0,0,0))['free_indices'],(2,3,4))

    def test_nonsquare_chart_is_exact(self):
        self.assertEqual(self.r['nonsquare_root_chart']['root_square'],'7')
        self.assertEqual(self.r['nonsquare_root_chart']['coefficients'],['1','2','3','5','7'])

    def test_singular_rank_and_conditioning(self):
        self.assertEqual(self.r['Jacobian_ranks']['origin'],0)
        self.assertEqual(self.r['fibre_dimensions_before_sign_quotient']['zero-leading'],3)
        self.assertEqual(self.r['near_cancellation_inverse_lower_bounds'],{'10':'10','100':'100','1000':'1000'})

    def test_invalid_data_and_scope_promotions(self):
        self.assertEqual(self.r['nonrealizable_data_refused'],6)
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('global_inverse_without_strata_derived','physical_Born_sign_selected','actual_couplings_or_matching_selected',
                    'degree_six_cut_inventory_constructed','native_or_UV_dynamics_derived','C12_budget_renewed'):
            with self.assertRaises(AssertionError,msg=key):t.validate({**c,key:True})


if __name__=='__main__':unittest.main()
