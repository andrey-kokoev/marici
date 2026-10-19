"""Point-count support, decaying tails and projection-gap scope guards."""
import copy
from fractions import Fraction as Q
import json
import unittest
import check_enriched_bound_sector as bound


class EnrichedBoundSectorTests(unittest.TestCase):
    def test_tail_and_contact_convention(self):
        self.assertEqual(bound.energy(Q(1,2)),Q(9,2))
        self.assertEqual(bound.tail_factor(Q(1,2)),Q(1,3))
        self.assertEqual(bound.tail_factor(Q(1,3)),Q(1,8))
        F=bound.F
        self.assertEqual(bound.boundary_matrix([[F(1)]],[[F(1)]],Q(1)),[[F(1)]])
        for s in (Q(0),Q(1),Q(-1),Q(2)):
            with self.assertRaises(AssertionError):bound.tail_factor(s)

    def test_scalar_monotone_crossing_support(self):
        F=bound.F;K=[[F(5)]];P=[[F(1)]]
        self.assertTrue((-bound.boundary_matrix(K,P,Q(1))[0][0]).positive())
        self.assertTrue(bound.boundary_matrix(K,P,Q(1,10))[0][0].positive())
        # The exact scalar secular equation is 1/s-4=0.
        self.assertEqual(bound.boundary_matrix(K,P,Q(1,4)),[[F()]])

    def test_scope_guards(self):
        c=json.loads(bound.CONTRACT.read_text(encoding='utf-8'))
        for key in ('named_antisymmetric_retained_weights_evaluated','same_finite_time_state_error_lower_bound_claimed',
                    'native_bound_counts_inherited','C12_protocol_renewed','physical_outcomes_admitted'):
            bad=copy.deepcopy(c);bad[key]=True
            with self.assertRaises(AssertionError):bound.validate_contract(bad)
        bad=copy.deepcopy(c);bad['enriched_point_dimension']=5
        with self.assertRaises(AssertionError):bound.validate_contract(bad)

    def test_actual_point_sector_comparison(self):
        r=bound.build()
        self.assertEqual(r['native']['upper_edge_inertia'],[6,5,0])
        self.assertEqual(r['enriched']['upper_edge_inertia'],[6,3,0])
        self.assertEqual(r['native']['point_dimension'],5)
        self.assertEqual(r['enriched']['point_dimension'],3)
        self.assertEqual(r['ambient_lifted_bound_projection_norm_gap'],1)
        self.assertEqual(r['enriched']['symmetric']['point_dimension'],2)
        self.assertEqual(r['enriched']['antisymmetric']['point_dimension'],1)
        self.assertTrue(r['symmetric_preparation_bound_weights_exactly_preserved'])
        for key in ('named_antisymmetric_retained_weights_evaluated','same_finite_time_state_error_lower_bound_claimed',
                    'native_bound_counts_inherited','new_singular_continuous_or_full_central_release_completeness_claimed',
                    'physical_preparation_or_detector_binding_claimed','historical_ancestor_freshness_claimed',
                    'new_live_proposition_admitted','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
            self.assertFalse(r[key],key)


if __name__=='__main__':unittest.main()
