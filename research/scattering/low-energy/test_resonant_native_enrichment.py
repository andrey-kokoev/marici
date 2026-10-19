"""Enriched projection, polynomial algebra and exact interval certificates."""
import copy
from fractions import Fraction as Q
import json
import unittest
import check_resonant_native_enrichment as enriched


class ResonantEnrichmentTests(unittest.TestCase):
    def test_compliance_polynomial_recurrence(self):
        F=enriched.F
        model={'A':[[F(1),F()],[F(),F(3)]],'G':enriched.eye(2),
               'u':[[F(1)],[F(1)]],'norm':F(2)}
        num,den=enriched.compliance_polynomials(model)
        self.assertEqual(num,[F(2),F(-1)]);self.assertEqual(den,[F(3),F(-4),F(1)])
        self.assertTrue(enriched.certify_coprime(num,den))
        with self.assertRaises(AssertionError):enriched.certify_coprime(enriched.pm(num,den),den)

    def test_bernstein_subdivision(self):
        F=enriched.F
        cells=enriched.certify_nonnegative([F(4),F(-4),F(1)])
        self.assertEqual([c['interval'] for c in cells],[['0','2'],['2','4']])
        with self.assertRaises(AssertionError):enriched.certify_nonnegative([F(-1)],max_depth=0)

    def test_scope_guards(self):
        c=json.loads(enriched.CONTRACT.read_text(encoding='utf-8'))
        for key in ('global_minimum_among_arbitrary_fitted_models_claimed','native_bound_counts_inherited',
                    'physical_outcomes_admitted','C12_protocol_renewed'):
            bad=copy.deepcopy(c);bad[key]=True
            with self.assertRaises(AssertionError):enriched.validate_contract(bad)

    def test_actual_full_band_certificate(self):
        r=enriched.build()
        self.assertEqual(r['full_core_dimension'],9);self.assertEqual(r['hidden_dimension'],6)
        self.assertEqual(r['weighted_core_inertia'],[8,0,1])
        self.assertEqual(r['full_band_scattering_norm_error_upper_bound'],'1/4')
        self.assertEqual(len(r['bernstein_cells']),5)
        self.assertEqual(r['minimum_core_dimension_in_native_endpoint_projection_class_for_error_below_2'],9)
        self.assertEqual(r['cross_polynomial_zero_multiplicities'],{'-1':2,'-2':2,'2/5':2})
        witness=enriched.F(*r['lower_witness']['norm_error_squared'])
        self.assertTrue((witness-enriched.F(Q(9,50)**2)).positive())
        for key in ('global_minimum_among_arbitrary_fitted_models_claimed','all_energy_identity_claimed',
                    'native_bound_counts_inherited','physical_energy_or_detector_binding_claimed',
                    'historical_ancestor_freshness_claimed','new_live_proposition_admitted',
                    'C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
            self.assertFalse(r[key],key)


if __name__=='__main__':unittest.main()
