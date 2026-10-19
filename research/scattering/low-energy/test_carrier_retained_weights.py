"""Exact intervals, a calibrated scalar residue, and actual named weights."""
import copy
from fractions import Fraction as Q
import json
import unittest
import check_carrier_retained_weights as weights


class CarrierWeightTests(unittest.TestCase):
    def test_signed_interval_arithmetic_and_rounding(self):
        F=weights.F
        self.assertEqual(weights.idiv((F(1),F(2)),(F(-3),F(-2))),(F(-1),F(Q(-1,3))))
        with self.assertRaises(AssertionError):weights.idiv((F(1),F(2)),(F(-1),F(1)))
        self.assertEqual(weights.ipoly([F(),F(),F(1)],(F(Q(1,3)),F(Q(1,2)))),
                         (F(Q(1,9)),F(Q(1,4))))
        self.assertEqual(weights.outward((F(Q(1,3)),F(Q(1,3))),100),(Q(33,100),Q(34,100)))

    def test_scalar_full_tail_residue(self):
        F=weights.F
        N,S=weights.secular_polynomials([F(-1)],[F(-5),F(1)])
        self.assertEqual(N,[F(-1)]);self.assertEqual(S,[F(1),F(-4)])
        self.assertEqual(weights.weight_interval(N,S,Q(1,4),Q(1,4)),(F(Q(15,16)),F(Q(15,16))))
        self.assertEqual(1/(1+weights.bound.tail_factor(Q(1,4))),Q(15,16))
        with self.assertRaises(AssertionError):weights.refine_root([F(1)],Q(1,8),Q(3,8),1)

    def test_scope_guards(self):
        c=json.loads(weights.CONTRACT.read_text(encoding='utf-8'))
        for key in ('absolute_single_carrier_weights_evaluated','arbitrary_preparation_error_bound_claimed',
                    'complement_declared_escaped','physical_capture_or_branching_ratio_claimed',
                    'C12_protocol_renewed','physical_outcomes_admitted'):
            bad=copy.deepcopy(c);bad[key]=True
            with self.assertRaises(AssertionError):weights.validate_contract(bad)

    def test_actual_full_tail_weights(self):
        r=weights.build()
        self.assertEqual(r['native']['mode_count'],3);self.assertEqual(r['enriched']['mode_count'],1)
        self.assertEqual([Q(x) for x in r['native']['total_rational_enclosure']],
                         [Q('0.120818958780'),Q('0.120818958781')])
        self.assertEqual([Q(x) for x in r['enriched']['total_rational_enclosure']],
                         [Q('0.114712845124'),Q('0.114712845125')])
        single=[Q(x) for x in r['single_carrier_native_minus_enriched_enclosure']]
        self.assertEqual(single,[Q('0.0030530568275'),Q('0.0030530568285')])
        self.assertTrue(r['all_antisymmetric_point_modes_accounted'])
        for key in ('absolute_single_carrier_weights_evaluated','arbitrary_preparation_error_bound_claimed',
                    'complement_declared_escaped','physical_capture_or_branching_ratio_claimed',
                    'historical_ancestor_freshness_claimed','new_live_proposition_admitted',
                    'C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
            self.assertFalse(r[key],key)


if __name__=='__main__':unittest.main()
