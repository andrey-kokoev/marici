"""Phase-volume retention and nonuniform late-time sensitivity to an opened tail."""
import copy
from fractions import Fraction as Q
import json
import unittest
import check_photon_energy_tail as tail


class PhotonEnergyTailTests(unittest.TestCase):
    def test_beta_moments_and_ultraviolet_guard(self):
        self.assertEqual(30*tail.beta_integral(2,6),Q(1))
        self.assertEqual(30*tail.beta_integral(1,6),Q(3,2))
        self.assertEqual(30*tail.beta_integral(4,6),Q(6))
        self.assertEqual(tail.tail_weight(Q(1)),Q(15,32))
        for power in (0,2):
            with self.assertRaises(AssertionError):tail.beta_integral(power,0)
        self.assertEqual(tail.positive_margin(Q(1,16)),Q(29,32))
        self.assertLess(tail.positive_margin(Q(1)),0)

    def test_added_triplet_really_is_orthogonal(self):
        h=tail.triplet_extra_profile();m=tail.measure
        self.assertEqual(m.inner(m.const(1),h),tail.F())
        self.assertEqual(m.inner(h,h),tail.F(1))
        self.assertNotEqual(h,m.const(1))

    def test_fresh_tail_receipt_and_limit_order(self):
        r=tail.build()
        self.assertEqual(r,json.loads(tail.RESULT.read_text(encoding='utf-8')))
        self.assertEqual(r['tail_density_boundary_identity_checks'],5)
        self.assertTrue(r['arbitrarily_small_positive_tail_removes_active_point_sector'])
        self.assertTrue(r['opposite_helicity_channel_orthogonality_checked'])
        self.assertFalse(r['small_tail_and_long_time_limits_commute'])
        self.assertEqual(r['asymptotic_survival_probability_difference_for_any_nonzero_tail'],'1/5')
        self.assertFalse(r['physical_spatial_photon_escape_proved'])
        self.assertFalse(r['branching_ratio_derived'])
        self.assertEqual(len(r['hostile_controls_refused']),6)

    def test_no_source_or_physical_promotion(self):
        c=json.loads(tail.CONTRACT.read_text(encoding='utf-8'));tail.validate_contract(c)
        for key,value in c.items():
            if value is False:
                bad=copy.deepcopy(c);bad[key]=True
                with self.assertRaises(AssertionError):tail.validate_contract(bad)
        for key in ('orthogonal_output_profiles_retained','identical_particle_constants_retained_symbolically',
                    'all_spectators_and_output_channels_retained'):
            bad=copy.deepcopy(c);bad[key]=False
            with self.assertRaises(AssertionError):tail.validate_contract(bad)


if __name__=='__main__':unittest.main()
