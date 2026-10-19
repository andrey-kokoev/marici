import copy
import json
import unittest
from fractions import Fraction as Q
import check_bilinear_photon_ir_series as ir


class BilinearPhotonIRSeriesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=ir.build()

    def test_receipt(self):
        self.assertEqual(self.result,json.loads(ir.RESULT.read_text(encoding='utf-8')))
        for key,value in (('legacy_pair_controls',5),('pair_shape_checks',81),('pair_norm_bound_checks',81),
                          ('combinatorial_bound_witnesses',111),('spectral_coefficient_bound_checks',65),
                          ('finite_square_projection_checks',42),('local_scale_tensor_checks',128),
                          ('all_outgoing_permutation_checks',1536),('Ward_checks',32),('Lorentz_checks',8),
                          ('finite_scale_checks',384),('geometric_tail_identity_checks',24)):
            self.assertEqual(self.result[key],value)

    def test_ordered_pairs_and_legacy_mixing(self):
        p=ir.pair_polynomials(2,3);target=ir.six.mixed.cut_polynomials()
        self.assertEqual((ir.ct.scale(2,p[0]),2*p[1],ir.ct.scale(2,p[2]),2*p[3]),target)
        p6=ir.homogeneous_polynomials(6,{2:Q(2),3:Q(3),4:Q(5)})
        s33=ir.six.sector_polynomials('c1_squared');s24=ir.six.sector_polynomials('c0_r4')
        self.assertEqual(p6[1],9*s33[1]+10*s24[1])
        self.assertEqual(ir.scalar_logs(3,4),ir.scalar_logs(4,3))
        with self.assertRaises(AssertionError):ir.pair_polynomials(1,3)

    def test_tail_and_scope(self):
        self.assertEqual(ir.input_majorant(0,0),16)
        self.assertEqual(ir.kernel_tail(40,Q(1,2)),Q(576*39,2**40))
        self.assertEqual(ir.uniform_log_tail_half_window(48),Q(1344*47,2**48))
        self.assertLess(ir.uniform_log_tail_half_window(40),Q(1,10**7))
        self.assertLess(ir.uniform_log_tail_half_window(48),Q(1,10**9))
        for key in ('all_subthreshold_convergence_derived','coupling_series_convergence_derived',
                    'finite_counterterm_series_convergence_derived','spectral_control_source_licensed'):
            self.assertFalse(self.result[key])
        with self.assertRaises(AssertionError):ir.tail_count(40,1)
        with self.assertRaises(AssertionError):ir.tail_count(3,Q(1,2))
        self.assertEqual(len(self.result['hostile_controls_refused']),8)

    def test_contract_guards(self):
        c=json.loads(ir.CONTRACT.read_text(encoding='utf-8'))
        for key,value in c.items():
            if isinstance(value,bool):
                bad=copy.deepcopy(c);bad[key]=not value
                with self.subTest(key=key),self.assertRaises(AssertionError):ir.validate_contract(bad)
        bad=copy.deepcopy(c);bad['domain']='all_0<s<4_and_complex_physical_sheet'
        with self.assertRaises(AssertionError):ir.validate_contract(bad)


if __name__=='__main__':unittest.main()
