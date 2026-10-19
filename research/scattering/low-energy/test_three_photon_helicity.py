"""Joint helicity rotation/exchange gauge and conditional three-photon isometry."""
import copy
from fractions import Fraction as Q
import json
import unittest
import check_three_photon_helicity as helicity


class ThreePhotonHelicityTests(unittest.TestCase):
    def reference(self):
        F=helicity.F;s=helicity.phase.SQ3/2
        return [[F(1),F(1),F(),F()],
                [F(1),F(Q(-1,2)),s,F()],
                [F(1),F(Q(-1,2)),-s,F()]], [F(),F(),F(1)]

    def test_odd_exchange_phase_is_not_optional(self):
        p,N=self.reference();order=(1,0,2)
        for h in (-1,1):
            eps=helicity.helicity_frame(p,N,h)
            exchanged=helicity.helicity_frame([p[i] for i in order],helicity.times(helicity.F(-1),N),h)
            permuted=helicity.tensor3([eps[i] for i in order])
            self.assertEqual(helicity.tensor3(exchanged),helicity.times(helicity.F(-1),permuted))
            self.assertNotEqual(helicity.tensor3(exchanged),permuted)

    def test_frame_domain_and_unitary_gauge(self):
        p,N=self.reference()
        with self.assertRaises(AssertionError):helicity.helicity_frame(p,N,0)
        with self.assertRaises(AssertionError):helicity.helicity_frame(p+[p[0]],N,1)
        with self.assertRaises(AssertionError):helicity.helicity_frame(p,helicity.times(helicity.F(-1),N),1)
        for k in p:
            g=helicity.gauge(helicity.direction(k))
            self.assertEqual(g*g.conjugate(),helicity.F(1))

    def test_source_cases_and_corrected_profiles(self):
        r=helicity.build()
        self.assertEqual(r['permutation_cases'],24)
        self.assertEqual(r['rotation_cases'],100)
        self.assertEqual(r['gauge_transition_cases'],24)
        self.assertEqual(r['unchanged_even_scalar_code_reuse_failures'],12)
        self.assertEqual(r['singlet_normalization_squared'],'840')
        self.assertEqual(r['triplet_normalization_squared'],'3')
        self.assertEqual(r['triplet_coherent_NxNy_expectation_gap'],'2/5')
        self.assertTrue(r['conditional_native_pair_to_relative_three_photon_isometry_constructed'])
        self.assertFalse(r['full_Lorentz_intertwiner_constructed'])
        self.assertFalse(r['native_joint_emission_operation_licensed'])
        self.assertFalse(r['branching_ratio_derived'])

    def test_no_emission_or_protocol_promotion(self):
        c=json.loads(helicity.CONTRACT.read_text(encoding='utf-8'));helicity.validate_contract(c)
        for key in ('physical_electron_positron_preparation_bound','native_continuous_rotation_licensed',
                    'native_joint_emission_operation_licensed','charge_conjugation_rule_bound',
                    'full_Lorentz_intertwiner_constructed','full_Fock_wavepacket_constructed',
                    'two_photon_helicity_audit_performed_by_this_checker','contact_generator_constructed',
                    'spectrum_selected_by_native_dynamics','branching_ratio_derived',
                    'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed',
                    'physical_outcomes_admitted'):
            bad=copy.deepcopy(c);bad[key]=True
            with self.assertRaises(AssertionError):helicity.validate_contract(bad)


if __name__=='__main__':unittest.main()
