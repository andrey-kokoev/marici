"""Infinite escape versus retained point spectrum, without deleting bound clouds."""
import copy
from fractions import Fraction as Q
import json
import unittest
import check_contact_escape_continuum as escape


class ContactEscapeContinuumTests(unittest.TestCase):
    def test_threshold_and_decoupling_are_distinct(self):
        self.assertTrue(escape.spectral_classification(Q(3),Q(1,4))['pure_ac'])
        self.assertFalse(escape.spectral_classification(Q(3),Q())['pure_ac'])
        threshold=escape.spectral_classification(Q(3),Q(1))
        self.assertTrue(threshold['upper_threshold_resonance'])
        self.assertEqual(threshold['above_band'],0)
        self.assertEqual(escape.spectral_classification(Q(3),Q(4))['below_band'],1)
        with self.assertRaises(AssertionError):escape.bound_certificate(escape.F(3),escape.F(1),escape.F(-1))

    def test_bound_weight_is_not_local_survival(self):
        F=escape.F;sqrt5=escape.phase.root(4)
        E,Z=escape.bound_certificate(F(3),escape.phase.SQ2,(F(1)-sqrt5)/2)
        self.assertEqual(E,F(2)+sqrt5)
        self.assertEqual(Z,F(1)/sqrt5)
        self.assertEqual(Z*Z,F(Q(1,5)))
        self.assertNotEqual(F(1)-Z,F(1)-Z*Z)
        self.assertEqual(escape.density_denominator(Q(3),Q(2)),[Q(1),Q(4),Q(-1)])

    def test_fresh_escape_receipt(self):
        r=escape.build()
        self.assertEqual(r,json.loads(escape.RESULT.read_text(encoding='utf-8')))
        self.assertTrue(r['self_adjoint_infinite_escape_completion_constructed'])
        self.assertTrue(r['weak_model_initial_encoded_pair_complete_local_release_proved'])
        self.assertEqual(r['native_irrep_boundary_rotation_cases'],24)
        self.assertEqual(r['source_density_boundary_checks'],15)
        self.assertEqual(r['positive_bound_example']['local_pair_probability_formula'],'1/5')
        self.assertFalse(r['initial_contact_source_is_sharp_total_energy'])
        self.assertFalse(r['lead_dispersion_identified_with_physical_photon_dispersion'])
        self.assertFalse(r['branching_ratio_derived'])
        self.assertEqual(len(r['hostile_controls_refused']),6)

    def test_no_physical_promotion(self):
        c=json.loads(escape.CONTRACT.read_text(encoding='utf-8'));escape.validate_contract(c)
        for key,value in c.items():
            if value is False:
                bad=copy.deepcopy(c);bad[key]=True
                with self.assertRaises(AssertionError):escape.validate_contract(bad)
        bad=copy.deepcopy(c);bad['all_spectator_and_bound_components_retained']=False
        with self.assertRaises(AssertionError):escape.validate_contract(bad)


if __name__=='__main__':unittest.main()
