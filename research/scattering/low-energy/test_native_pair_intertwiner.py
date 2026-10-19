"""Native pair source identities, Bose coefficient codes and finite-group limits."""
import copy
from fractions import Fraction as Q
import json
import unittest
import check_native_pair_intertwiner as pair


class NativePairIntertwinerTests(unittest.TestCase):
    def test_exact_sphere_moments(self):
        F=pair.F
        self.assertEqual(pair.sphere_integral({(0,0,0):F(1)}),F(1))
        self.assertEqual(pair.sphere_integral({(0,2,2):F(1)}),F(Q(1,15)))
        self.assertEqual(pair.sphere_integral({(4,0,0):F(1)}),F(Q(1,5)))
        self.assertEqual(pair.sphere_integral({(1,2,0):F(1)}),F())

    def test_vandermonde_normalization_and_exchange_sign(self):
        y=[pair.measure.var(i) for i in range(3)]
        A=pair.mul(pair.mul(pair.add(y[0],pair.scale(pair.F(-1),y[1])),
                            pair.add(y[1],pair.scale(pair.F(-1),y[2]))),
                   pair.add(y[2],pair.scale(pair.F(-1),y[0])))
        self.assertEqual(pair.measure.inner(A,A),pair.F(Q(1,840)))
        self.assertEqual(pair.measure.permute(A,(1,0,2)),pair.scale(pair.F(-1),A))

    def test_fresh_source_pair_codes_and_nonselection(self):
        r=pair.build()
        self.assertEqual(r['native_group_cases'],24)
        self.assertEqual(r['pair_invariant_rank'],1)
        self.assertEqual(r['scalar_profile_only_pair_intertwiner_max_rank'],1)
        self.assertEqual(r['lone_spinor_center_even_intertwiner_rank'],0)
        self.assertTrue(r['raw_pair_intertwining_verified'])
        self.assertTrue(r['native_pair_to_Bose_scalar_coefficient_isometries_constructed'])
        self.assertEqual(r['two_output_quadrupole_45_degree_leakage_squared_norm'],'1')
        self.assertEqual(r['counterexample_sector_probabilities'][1],['9/25','16/25'])
        self.assertEqual(r['counterexample_sector_probabilities'][2],['16/25','9/25'])
        self.assertTrue(r['owner_files_unchanged'])
        self.assertFalse(r['finite_symmetry_selects_multiplicity'])
        self.assertFalse(r['physical_photon_helicity_intertwiner_constructed'])

    def test_no_physical_or_budget_promotion(self):
        c=json.loads(pair.CONTRACT.read_text(encoding='utf-8'));pair.validate_contract(c)
        for key in ('physical_electron_positron_preparation_bound','physical_photon_helicity_intertwiner_constructed',
                    'native_input_to_photon_isometry_constructed','finite_symmetry_selects_multiplicity',
                    'two_ray_quadrupole_code_is_SO3_vector_intertwiner','contact_generator_constructed',
                    'branching_ratio_derived','full_Fock_wavepacket_constructed','live_proposition_inventory_changed',
                    'C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
            bad=copy.deepcopy(c);bad[key]=True
            with self.assertRaises(AssertionError):pair.validate_contract(bad)


if __name__=='__main__':unittest.main()
