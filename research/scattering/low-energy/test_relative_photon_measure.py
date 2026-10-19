"""Relative quantum coordinate map, exact normalization and phase retention."""
import copy
from fractions import Fraction as Q
import json
import unittest
import check_relative_photon_measure as measure


class RelativePhotonMeasureTests(unittest.TestCase):
    def test_chart_inverse_and_permutation_half_density(self):
        for u,v in ((Q(1),Q(1)),(Q(2),Q(1,3)),(Q(3,7),Q(11,5))):
            y=measure.coordinates(u,v)
            self.assertEqual(sum(y),1)
            self.assertEqual((y[0]/y[1],y[0]/y[2]),(u,v))
            self.assertEqual(measure.rho(1/u,v/u)/u**3,measure.rho(u,v))
            self.assertEqual(measure.rho(v,u),measure.rho(u,v))
        with self.assertRaises(AssertionError):measure.coordinates(Q(0),Q(1))

    def test_simplex_moments_and_profile_orthogonality(self):
        F=measure.F;y=[measure.var(i) for i in range(3)]
        S2=measure.add(*(measure.power(z,2) for z in y))
        p0=measure.const(1)
        p1=measure.scale(2*measure.phase.root(6),measure.add(S2,measure.const(Q(-1,2))))
        self.assertEqual(measure.simplex_integral(S2),F(Q(1,2)))
        self.assertEqual(measure.simplex_integral(measure.power(S2,2)),F(Q(4,15)))
        self.assertEqual(measure.inner(p0,p1),F())
        self.assertEqual(measure.inner(p1,p1),F(1))
        self.assertEqual(measure.inner(p0,measure.mul(S2,p1)),F(1)/(2*measure.phase.root(6)))

    def test_source_receipt_coherence_and_counterexamples(self):
        r=measure.build()
        self.assertTrue(r['relative_coordinate_unitary_constructed'])
        self.assertTrue(r['normalizable_Bose_relative_profiles_constructed'])
        self.assertEqual(r['omitted_half_density_squared_norm'],'8/55')
        self.assertEqual(r['symmetric_density_examples']['1']['variance_energy_fraction'],'1/72')
        self.assertEqual(r['symmetric_density_examples']['3']['variance_energy_fraction'],'1/180')
        self.assertIn('erase_coherent_cross_term',r['hostile_controls_refused'])
        self.assertFalse(r['native_input_to_photon_isometry_constructed'])
        self.assertFalse(r['full_Fock_wavepacket_constructed'])

    def test_no_physical_or_inventory_promotion(self):
        c=json.loads(measure.CONTRACT.read_text(encoding='utf-8'));measure.validate_contract(c)
        for key in ('sharp_configuration_is_normalizable_profile','native_seed_measure_selected',
                    'native_input_to_photon_isometry_constructed','full_Fock_wavepacket_constructed',
                    'helicity_lorentz_intertwiner_constructed','profile_selected_by_native_dynamics',
                    'relative_two_three_sector_amplitude_selected','branching_ratio_derived',
                    'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed',
                    'physical_outcomes_admitted'):
            bad=copy.deepcopy(c);bad[key]=True
            with self.assertRaises(AssertionError):measure.validate_contract(bad)


if __name__=='__main__':unittest.main()
