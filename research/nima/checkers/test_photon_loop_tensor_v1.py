import copy
from fractions import Fraction as Q
import json
import unittest

import check_photon_loop_tensor_v1 as t


class LoopTensorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):
        self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_all_channel_and_coupling_coordinates(self):
        self.assertEqual(self.r['formal_log_channel_count'],3)
        self.assertEqual(self.r['quadratic_coupling_count'],3)
        self.assertEqual(self.r['counts']['helicity'],64)

    def test_component_Ward(self):self.assertEqual(self.r['component_Ward_scalar_constraints'],2304)

    def test_labelled_Bose_channels(self):self.assertEqual(self.r['counts']['Bose'],72)

    def test_full_tensor_scale_transport(self):
        self.assertEqual(self.r['counts']['flow'],256)
        self.assertEqual(self.r['pi_squared_scale_flow'],{
            'g4':['-7/160','0','-7/80'],'g4prime':['1/40','0','1/240'],'f4':['0','-5/96','0']})

    def test_forward_invisible_angular_error(self):
        self.assertEqual(Q(self.r['doubled_beta12_off_forward_f_squared_residual']),Q(3,3125))

    def test_exact_complex_divisor(self):
        c=self.r['complex_S2_zero_control']
        self.assertEqual(c['S2'],'0')
        self.assertTrue(c['regular_F2_only_scalar_lift_refuted'])
        self.assertEqual(c['s_log_gf_coefficient'],'-5*omega/48')

    def test_Bose_normalization_and_rim(self):
        self.assertEqual(self.r['pi_times_forward_absorptive_D_O_M_at_common_Born'],['19/2560','-5/768','1/1280'])

    def test_zero_loop_single_minus_does_not_remove_local_h3(self):
        self.assertEqual(t.rows()[4],(t.ZERO,)*3)
        self.assertEqual(t.w.amplitude_rows(Q(3,5),Q(4,5))[4][4],Q(144,625))
        self.assertTrue(self.r['all_eight_local_matching_coefficients_retained'])

    def test_scope_promotions_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('window_shift_lift_constructed','full_amplitude_analytic_at_massless_origin',
                    'finite_matching_coefficients_selected','native_preparation_or_physical_rates_derived','UV_completion_constructed'):
            bad=copy.deepcopy(c);bad[key]=True
            with self.assertRaises(AssertionError,msg=key):t.validate(bad)


if __name__=='__main__':unittest.main()
