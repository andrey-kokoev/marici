import json
import unittest
from fractions import Fraction as Q

import check_photon_joint_transport_stability_v1 as t


class JointTransportStabilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_actual_degenerating_source(self):
        self.assertEqual(self.r['certificate']['degree6_rescaling_product_identities'],12)
        self.assertTrue(self.r['limit_data_realizable'])
        self.assertEqual(self.r['constant_cut_gap'],'7/10952')

    def test_growth_not_hidden(self):
        rows=self.r['exact_degenerating_controls'];self.assertEqual(len(rows),4)
        self.assertLess(Q(rows[-1]['joint_data_gap']),Q(rows[0]['joint_data_gap']))
        self.assertGreater(Q(rows[-1]['quartic_max_norm']),Q(rows[0]['quartic_max_norm']))
        self.assertTrue(self.r['all_source_maps_remain_polynomial_continuous'])

    def test_norms_and_bias(self):
        c=self.r['certificate']
        self.assertEqual((c['response_operator_norm'],c['cut_polynomial_operator_norm']),('61/18','13/3'))
        self.assertEqual((c['response_line_norm'],c['cut_polynomial_line_norm']),('5','18'))

    def test_conditional_controls(self):
        self.assertEqual((self.r['bounded_identity_controls'],self.r['unbounded_f4_controls']),(576,2))
        self.assertTrue(self.r['conditional_zero_leading_boundary_bound_derived'])

    def test_bound_requires_source_cap(self):
        with self.assertRaises(AssertionError):t.bias_bound(t.degenerating_source(Q(1,1000)),Q(1),Q(1))

    def test_no_physical_or_global_stability_promotion(self):
        self.assertFalse(self.r['physical_quartic_bound_derived'])
        self.assertFalse(self.r['global_compact_source_noise_modulus_derived'])

    def test_unearned_promotions_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('physical_quartic_bound_derived','bounded_source_continuity_refuted',
                    'uniform_EFT_window_for_diverging_sources_derived','global_compact_source_noise_modulus_derived',
                    'physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
            with self.assertRaises(AssertionError,msg=key):t.validate({**c,key:True})


if __name__=='__main__':unittest.main()
