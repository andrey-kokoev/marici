"""Weighted matrix residues, exact assembly, scope guards and actual weights."""
import copy
from fractions import Fraction as Q
import json
import unittest
import check_named_preparation_weights as weights


class NamedPreparationTests(unittest.TestCase):
    def test_scalar_and_weighted_two_port_residues(self):
        F=weights.F
        D,adj=weights.determinant_and_adjugate([[[F(1),F(-4)]]])
        J,norm=weights.quadratic_numerator(adj,[[F(2)]],[[F(3)]])
        self.assertEqual(norm,F(18));self.assertEqual(J,[F(1)])
        self.assertEqual(weights.symmetric_weight_interval(J,D,Q(1,4),Q(1,4)),
                         (F(Q(15,16)),F(Q(15,16))))
        B=[[[F(1),F(-4)],[F(),F(-1)]],[[F(),F(-2)],[F(1),F(-5)]]]
        D,adj=weights.determinant_and_adjugate(B)
        self.assertEqual(D,[F(1),F(-9),F(18)])
        J,norm=weights.quadratic_numerator(adj,[[F(2),F()],[F(),F(1)]],[[F(1)],[F(1)]])
        self.assertEqual(norm,F(3));self.assertEqual(J,[F(1),F(Q(-10,3))])
        for s,w in ((Q(1,3),Q(8,81)),(Q(1,6),Q(70,81))):
            self.assertEqual(weights.symmetric_weight_interval(J,D,s,s),(F(w),F(w)))

    def test_assembly_and_energy_separation(self):
        common={'belt':(Q(1,10),Q(1,10)),'carrier_sum':(Q(1,5),Q(1,5))}
        anti={'native':(Q(1,10),Q(1,10)),'enriched':(Q(1,20),Q(1,20))}
        tables=weights.assemble_named(common,anti)
        self.assertEqual(tables['native']['carrier_1'],(Q(3,20),Q(3,20)))
        self.assertEqual(tables['enriched']['carrier_2'],(Q(1,8),Q(1,8)))
        self.assertEqual(weights.certify_energy_separation([{'energy_bracket':['5','6']},{'energy_bracket':['7','8']}]),
                         [['5','6'],['7','8']])
        with self.assertRaises(AssertionError):
            weights.certify_energy_separation([{'energy_bracket':['5','7']},{'energy_bracket':['6','8']}])

    def test_scope_guards(self):
        c=json.loads(weights.CONTRACT.read_text(encoding='utf-8'))
        for key in ('coherent_mixture_weights_from_diagonals_claimed','full_visible_retained_quadratic_form_certified',
                    'complement_declared_escaped','physical_capture_or_branching_ratio_claimed',
                    'C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
            bad=copy.deepcopy(c);bad[key]=True
            with self.assertRaises(AssertionError):weights.validate_contract(bad)

    def test_actual_absolute_weights(self):
        r=weights.build();self.assertEqual(r['symmetric_contact_rank'],2)
        self.assertEqual(len(r['symmetric_modes']),2)
        self.assertEqual(len(r['cross_sector_point_energy_intervals']['native']),5)
        self.assertEqual(len(r['cross_sector_point_energy_intervals']['enriched']),3)
        expected={'native':['0.128138834975','0.128138834976'],
                  'enriched':['0.125085778147','0.125085778148']}
        for label,interval in expected.items():
            self.assertEqual([Q(x) for x in r['absolute_named_weight_enclosures'][label]['carrier_1']],
                             [Q(x) for x in interval])
        self.assertTrue(r['all_named_point_contributions_accounted'])
        self.assertTrue(r['exact_equality_for_symmetric_preparations'])
        for key in ('full_visible_retained_quadratic_form_certified','complement_declared_escaped',
                    'physical_capture_or_branching_ratio_claimed','historical_ancestor_freshness_claimed',
                    'new_live_proposition_admitted','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
            self.assertFalse(r[key],key)


if __name__=='__main__':unittest.main()
