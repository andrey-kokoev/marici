import copy
import json
import unittest
from fractions import Fraction as Q
import check_hodge_cycle_equivariance_audit as s


class EquivarianceAuditTests(unittest.TestCase):
    def setUp(self):self.c=json.loads(s.CONTRACT.read_text(encoding='utf-8'))

    def test_Hodge_module_average_is_divisor_projection(self):
        r=s.contraction(s.diag([1,-1,-1]))
        self.assertEqual(r['averaging'],s.serial(s.diag([1,0,0])))

    def test_Weil_sign_module_has_zero_invariants(self):
        r=s.contraction(s.diag([-1,-1]));self.assertEqual(r['averaging'],s.serial(s.zero(2)))
        self.assertEqual(r['h_odd'],s.serial(s.diag([Q(-1,2),Q(-1,2)])))

    def test_faithful_rotation_not_just_involutions(self):
        t=((Q(0),Q(-1)),(Q(1),Q(0)));r=s.contraction(t)
        self.assertEqual(r['N'],s.serial(s.zero(2)))

    def test_trivial_module_keeps_degree_zero(self):
        r=s.contraction(s.diag([1]));self.assertEqual(r['averaging'],s.serial(s.eye(1)))
        self.assertEqual(r['positive_group_cohomological_degree_over_Q'],'zero')

    def test_forgetting_division_by4_breaks_contraction(self):
        with self.assertRaisesRegex(ValueError,'periodic contraction'):s.contraction(s.diag([1,-1,-1]),1)

    def test_infinite_order_action_not_admitted(self):
        with self.assertRaisesRegex(ValueError,'fourth power identity'):s.contraction(s.diag([2]))

    def test_arbitrary_conjugate_representation(self):
        # An integral change of basis of diag(1,-1,-1), not a diagonal-only check.
        t=((Q(1),Q(-2),Q(0)),(Q(0),Q(-1),Q(0)),(Q(0),Q(0),Q(-1)))
        self.assertEqual(s.contraction(t)['positive_group_cohomological_degree_over_Q'],'zero')

    def test_fixed_source_point_has_four_distinct_translates(self):
        r=s.point_control();self.assertEqual(r['orbit_length'],4)
        self.assertTrue(r['p_distinct_from_tau_p'])

    def test_origin_cannot_supply_noninvariant_support_control(self):
        with self.assertRaisesRegex(ValueError,'four distinct'):s.point_control(1)

    def test_object_counterexample_does_not_refute_class_invariance(self):
        r=s.point_control();self.assertFalse(r['cycle_object_tau_equivariance'])
        self.assertTrue(r['cycle_class_and_rational_Chow_class_tau_invariance'])
        self.assertIn('not computed projective equations',r['geometry'])

    def test_averaging_is_not_the_identity_on_alpha(self):
        alpha=(Q(0),Q(1),Q(0));a=s.diag([1,0,0])
        self.assertEqual(s.vec(a,alpha),(0,0,0));self.assertNotEqual(alpha,(0,0,0))

    def test_stability_does_not_decide_projected_image(self):
        r=s.linear_models();self.assertTrue(r['P_A0_zero']);self.assertFalse(r['P_A1_zero'])
        self.assertFalse(r['geometric_realizability_of_either_model_is_claimed'])

    def test_total_equivariant_degree_is_not_group_degree(self):
        r=s.shifted_complex_control();self.assertEqual(r['total_equivariant_degree2_dimension'],1)
        self.assertFalse(r['positive_total_degree_vanishes'])
        self.c['vanishing_degree_scope']='all_positive_total_degrees'
        with self.assertRaisesRegex(ValueError,'group degree confused'):s.check_contract(self.c)

    def test_integral_torsion_controls_do_not_survive_Q(self):
        r=s.torsion_controls();self.assertEqual(r['after_tensor_Q'],'zero')
        self.assertFalse(r['identification_with_actual_integral_Hodge_lattice_claimed'])

    def test_integral_coefficients_cannot_replace_Q(self):
        self.c['source']['coefficients']='Z'
        with self.assertRaisesRegex(ValueError,'source changed'):s.check_contract(self.c)

    def test_wrong_cycle_codimension_cannot_be_substituted(self):
        self.c['source']['codimension']=6
        with self.assertRaisesRegex(ValueError,'source changed'):s.check_contract(self.c)

    def test_scope_guards_cannot_be_deleted_or_renamed(self):
        self.c['forbidden_promotions'][0]='arbitrary_replacement'
        with self.assertRaisesRegex(ValueError,'scope inventory'):s.check_contract(self.c)

    def test_fixed_X_all_cycle_gate_remains_open(self):
        net=json.loads((s.ROOT/s.USED_SOURCES[0]).read_text(encoding='utf-8'))
        n=next(n for n in net['conjectures'] if n['id']=='all-algebraic-cycles-annihilation')
        self.assertEqual((n['status'],n['verdict'],n['evidence']),('open','open',[]))

    def test_report_does_not_promote_audit_to_Hodge_result(self):
        r=s.report();self.assertFalse(r['Hodge_proved']);self.assertFalse(r['Hodge_refuted'])
        self.assertFalse(r['main_net_modified'])
        for name in s.FORBIDDEN:self.assertIs(r[name],False)
        self.assertIn('Bertini',r['verification_level'])


if __name__=='__main__':unittest.main()
