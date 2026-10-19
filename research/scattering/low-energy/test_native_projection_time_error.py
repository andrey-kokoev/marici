"""Finite-time formulas and scope guards; no numerical evolution asserted."""
import copy
import json
import unittest
from fractions import Fraction as Q
import check_native_projection_time_error as error


class ProjectionTimeErrorTests(unittest.TestCase):
    def test_bounds_and_negative_time(self):
        for t in (Q(1,30),Q(-1,30)):
            self.assertEqual(error.state_bound(t,Q(1)),Q(1,10))
            self.assertEqual(error.omitted_probability_bound(t,Q(1)),Q(1,100))
            self.assertEqual(error.effect_probability_bound(t,Q(1)),Q(1,5))
        self.assertEqual(error.state_bound(Q(100),Q(0)),0)
        self.assertEqual(error.state_bound(Q(100),Q(1,2)),1)
        self.assertEqual(error.omitted_probability_bound(Q(100),Q(1,2)),Q(1,2))

    def test_preparation_domains(self):
        for fn,value in ((error.state_bound,Q(-1)),(error.omitted_probability_bound,Q(2)),
                         (error.effect_probability_bound,Q(2))):
            with self.assertRaises(AssertionError):fn(Q(1),value)

    def test_contract_promotions(self):
        c=json.loads(error.CONTRACT.read_text(encoding='utf-8'))
        for key in ('asymptotic_scattering_bound_claimed','uniform_in_time_small_error_claimed',
                    'high_energy_protocol_executed','physical_outcomes_admitted'):
            bad=copy.deepcopy(c);bad[key]=True
            with self.assertRaises(AssertionError):error.validate_contract(bad)

    def test_actual_metric_norm_and_preparations(self):
        r=error.build();tau=error.F(*r['exact_residual_norm_squared'])
        self.assertTrue((tau-error.F(4)).positive())
        self.assertTrue((error.F(9)-tau).positive())
        self.assertEqual(r['residual_rank'],1)
        self.assertEqual(r['certified_residual_norm_upper_bound'],3)
        profiles=r['normalized_core_preparations']
        self.assertEqual(profiles['belt']['alpha_squared'],'0')
        self.assertEqual(profiles['carrier_difference']['alpha_squared'],'1')
        self.assertEqual(profiles['carrier_1']['alpha_squared'],'1/2')
        for key in ('asymptotic_scattering_bound_claimed','uniform_in_time_small_error_claimed',
                    'physical_clock_or_detector_binding_claimed','new_live_proposition_admitted',
                    'C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
            self.assertFalse(r[key],key)


if __name__=='__main__':unittest.main()
