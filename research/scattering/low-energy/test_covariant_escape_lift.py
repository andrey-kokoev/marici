"""Poincare lift and invariant-mass retention, without native/local promotions."""
import copy
from fractions import Fraction as Q
import json
import unittest
import check_covariant_escape_lift as lift


class CovariantEscapeLiftTests(unittest.TestCase):
    def test_lab_and_trajectory_clocks_differ(self):
        F=lift.F;u=lift.packet.velocity([F(Q(1,8)),F(),F()])
        lab,trajectory=lift.clock_coefficients(u)
        self.assertEqual(lab,F(Q(65,63)))
        self.assertEqual(trajectory,F(Q(63,65)))
        self.assertEqual(lab*trajectory,F(1))
        self.assertNotEqual(lab,trajectory)

    def test_mass_bound_weight_is_not_energy_point_weight(self):
        cutoff=lift.retained_mass_weights(Q())
        self.assertEqual(cutoff['mass_bound'],lift.F(1)/lift.phase.root(4))
        self.assertEqual(cutoff['local_pair'],lift.F(Q(1,5)))
        self.assertNotEqual(cutoff['local_pair'],cutoff['mass_bound'])
        self.assertEqual(cutoff['mass_bound']+cutoff['outgoing'],lift.F(1))
        opened=lift.retained_mass_weights(Q(1,4))
        self.assertEqual(opened['mass_bound'],lift.F())
        self.assertEqual(opened['outgoing'],lift.F(1))
        with self.assertRaises(AssertionError):lift.retained_mass_weights(Q(1))

    def test_fresh_covariant_lift_receipt(self):
        r=lift.build()
        self.assertEqual(r,json.loads(lift.RESULT.read_text(encoding='utf-8')))
        self.assertTrue(r['active_velocity_Poincare_completion_constructed'])
        self.assertTrue(r['lab_escape_wave_operator_constructed'])
        self.assertTrue(r['completed_outgoing_bound_spectator_readout_isometric'])
        self.assertTrue(r['cutoff_bound_mass_retention_survives_boost_dephasing'])
        self.assertEqual(r['spectral_momentum_covariance_cases'],9)
        self.assertEqual(r['free_lead_Chebyshev_Gram_dimension'],6)
        self.assertEqual(r['cutoff_packet_lab_energy_point_weight'],'0')
        self.assertFalse(r['native_source_Poincare_representation_derived'])
        self.assertFalse(r['microcausality_proved'])
        self.assertFalse(r['branching_ratio_derived'])

    def test_scope_and_record_guards(self):
        c=json.loads(lift.CONTRACT.read_text(encoding='utf-8'));lift.validate_contract(c)
        for key,value in c.items():
            if isinstance(value,bool):
                bad=copy.deepcopy(c);bad[key]=not value
                with self.assertRaises(AssertionError):lift.validate_contract(bad)


if __name__=='__main__':unittest.main()
