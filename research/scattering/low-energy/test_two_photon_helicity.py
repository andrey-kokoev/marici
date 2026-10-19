"""Two-photon helicity characters, Bose exchange and finite/continuous distinction."""
import copy
from fractions import Fraction as Q
import json
import unittest
import check_two_photon_helicity as two


class TwoPhotonHelicityTests(unittest.TestCase):
    def test_all_stabilizer_characters_and_exchange(self):
        F=two.F;n=[F(),F(),F(1)];t=[F(1),F(),F()]
        R=[[F(),F(-1),F()],[F(1),F(),F()],[F(),F(),F(1)]]
        for h1 in (-1,1):
            for h2 in (-1,1):
                B=two.helicity_pair(n,t,h1,h2)
                character=F(1 if h1==h2 else -1)
                self.assertEqual(two.act_tensor(R,B),two.phase.scale(character,B))
                self.assertEqual(two.helicity_pair(two.three.times(F(-1),n),t,h2,h1),two.transpose(B))
        with self.assertRaises(AssertionError):two.helicity_pair(n,n,1,1)

    def test_global_equal_helicity_tensor(self):
        F=two.F;n=[F(Q(-1,3)),F(Q(-2,3)),F(Q(2,3))]
        for h in (-1,1):
            B=two.equal_helicity_section(n,h)
            self.assertEqual(two.frobenius(B),F(1))
            self.assertEqual(two.mm(B,B),B)
            self.assertEqual(two.equal_helicity_section(two.three.times(F(-1),n),h),two.transpose(B))
            self.assertEqual(two.cm.act(B,n),[F()]*3)
        with self.assertRaises(AssertionError):two.equal_helicity_section([F(1)]*3,1)

    def test_source_codes_and_conditional_continuous_exclusion(self):
        r=two.build()
        self.assertEqual(r['rotation_cases'],104)
        self.assertEqual(r['frame_independent_section_rotation_cases'],364)
        self.assertEqual(r['spin1_reference_constraint_Gram_determinants'],{'1,1':'48','1,-1':'16','-1,1':'16','-1,-1':'48'})
        self.assertEqual(r['conditional_continuous_total_J1_two_photon_intertwiner_rank'],0)
        self.assertTrue(r['conditional_native_pair_two_photon_finite_rotation_isometry_constructed'])
        self.assertFalse(r['source_triplet_identified_with_physical_total_J1'])
        self.assertFalse(r['finite_native_symmetry_alone_excludes_triplet_two_photons'])
        self.assertEqual(r['continuous_spin0_plus_spin1_sector_weight_examples'][1]['singlet_two_probability'],'9/25')

    def test_no_native_spin_or_physical_promotion(self):
        c=json.loads(two.CONTRACT.read_text(encoding='utf-8'));two.validate_contract(c)
        for key in ('source_triplet_identified_with_physical_total_J1','full_continuous_source_rotation_licensed',
                    'physical_electron_positron_preparation_bound','charge_conjugation_rule_bound',
                    'native_joint_emission_operation_licensed','full_Lorentz_intertwiner_constructed',
                    'full_Fock_wavepacket_constructed','contact_generator_constructed',
                    'finite_native_symmetry_alone_excludes_triplet_two_photons','branching_ratio_derived',
                    'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed',
                    'physical_outcomes_admitted'):
            bad=copy.deepcopy(c);bad[key]=True
            with self.assertRaises(AssertionError):two.validate_contract(bad)


if __name__=='__main__':unittest.main()
