import copy
import json
import unittest
from fractions import Fraction as Q
import check_windowed_photon_dispersion as win


class WindowedPhotonDispersionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=win.build()

    def test_receipt(self):
        self.assertEqual(self.result,json.loads(win.RESULT.read_text(encoding='utf-8')))
        for key,value in (('flow_coefficient_norm_checks',144),('exact_Cauchy_polynomial_division_checks',144),
                          ('rim_branch_checks',4),('retained_log_coefficient_checks',96),
                          ('all_outgoing_permutation_checks',1152),('Ward_checks',24),
                          ('Lorentz_checks',6),('reference_scale_cancellation_checks',288)):
            self.assertEqual(self.result[key],value)

    def test_Cauchy_polynomial_and_branch(self):
        p=win.flow_polynomial(2,2,0,None)
        self.assertEqual(p,{(2,0):Q(5,12)})
        self.assertEqual(win.divided_integral(p,Q(),Q(),Q(1,2)),Q(5,96))
        self.assertEqual(win.rim_window_log(Q(1,4),Q(1,2)),(Q(),Q(),1))
        self.assertEqual(win.rim_window_log(Q(3,4),Q(1,2))[2],0)
        self.assertEqual(win.rim_window_log(Q(-1,4),Q(1,2))[2],0)
        with self.assertRaises(AssertionError):win.rim_window_log(Q(1,2),Q(1,2))

    def test_remainder_bound_and_scope(self):
        self.assertLess(win.analytic_tail(40,Q(1,2),Q(1,4)),Q(1,10**8))
        self.assertLess(win.analytic_tail(48,Q(1,2),Q(1,4)),Q(1,10**10))
        with self.assertRaises(AssertionError):win.analytic_tail(40,Q(1,2),Q(1,3))
        for key in ('unknown_UV_matching_remainder_bounded','finite_matching_source_selected',
                    'window_endpoint_is_physical_threshold','prescribed_flow_is_QFT_derived_fixed_t_dispersion'):
            self.assertFalse(self.result[key])
        self.assertEqual(len(self.result['hostile_controls_refused']),8)

    def test_contract_guards(self):
        c=json.loads(win.CONTRACT.read_text(encoding='utf-8'))
        for key,value in c.items():
            if isinstance(value,bool):
                bad=copy.deepcopy(c);bad[key]=not value
                with self.subTest(key=key),self.assertRaises(AssertionError):win.validate_contract(bad)
        bad=copy.deepcopy(c);bad['domain']='all_subthreshold_physical_sheet'
        with self.assertRaises(AssertionError):win.validate_contract(bad)


if __name__=='__main__':unittest.main()
