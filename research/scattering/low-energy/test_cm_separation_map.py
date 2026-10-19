"""Mass-shell completion, retained inverse, three-body shapes, scope limits."""
import copy
from fractions import Fraction as Q
import json
import unittest
import check_cm_separation_map as separation


class CMSeparationTests(unittest.TestCase):
    def test_already_balanced_pair_and_inverse(self):
        F=separation.F
        seeds=[[F(1),F(1),F(),F()],[F(1),F(-1),F(),F()]]
        out,record=separation.complete(seeds,F(2),F(2))
        self.assertEqual(out,seeds);self.assertEqual(record['boost'],separation.eye(4))
        self.assertEqual(record['scale'],F(1))
        with self.assertRaises(AssertionError):separation.complete(seeds,F(2),F(3))
        with self.assertRaises(AssertionError):separation.complete([seeds[0]],F(2),F(1))

    def test_interior_three_body_energy_shape_inverse(self):
        weights=(Q(1),Q(2),Q(1,3));energies=(Q(7,18),Q(4,9),Q(1,6))
        self.assertEqual(separation.energy_fractions(weights),energies)
        self.assertEqual(separation.inverse_shape(energies),weights)
        self.assertEqual(separation.energy_fractions((Q(1),)*3),(Q(1,3),)*3)
        with self.assertRaises(AssertionError):separation.inverse_shape((Q(1,2),Q(1,4),Q(1,4)))

    def test_actual_source_examples_and_covariance(self):
        r=separation.build()
        self.assertTrue(r['classical_CM_map_constructed'])
        self.assertEqual(r['two_ray_witness_first_direction'],['-1/3','-2/3','2/3'])
        self.assertEqual(r['three_weight_sensitivity_energy_fractions'],['7/18','4/9','1/6'])
        self.assertEqual(r['source_rotation_covariance_cases'],36)
        for example in r['examples'].values():self.assertTrue(example['exact_inverse_verified'])
        self.assertFalse(r['quantum_separation_isometry_constructed'])
        self.assertFalse(r['contact_amplitudes_derived'])

    def test_no_erasure_or_physical_promotion(self):
        c=json.loads(separation.CONTRACT.read_text(encoding='utf-8'))
        bad=copy.deepcopy(c);bad['boost_scale_record_retained']=False
        with self.assertRaises(AssertionError):separation.validate_contract(bad)
        for key in ('source_native_separation_derived','physical_motion_implemented','quantum_separation_isometry_constructed',
                    'normalizable_photon_output_constructed','unequal_seed_weights_source_selected',
                    'contact_amplitudes_derived','branching_ratio_derived','EF1_N_refutation_reversed',
                    'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
            bad=copy.deepcopy(c);bad[key]=True
            with self.assertRaises(AssertionError):separation.validate_contract(bad)


if __name__=='__main__':unittest.main()
