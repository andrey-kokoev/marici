"""Regression tests for route compilation and the shared planner's cost tie-break."""
import copy
import math
import unittest
from check_closure_planning import load, compile_model, solve
from interpretation_planner import Action, Branch, Decoder, Effect, Planner, State, OUTCOMES
from objective_projection import ActionAssessment, Objective, ObjectiveKind, recommend

class ClosurePlanningTests(unittest.TestCase):
    def setUp(self):
        self.contract,self.ranges=load()
        self.observations=self.contract.pop('observed_attempts',[])
        self.params={k:v[1] for k,v in self.ranges.items()}

    def test_observed_inconclusive_audit_stops_without_unlock(self):
        self.contract['observed_attempts']=[{'action':'source-contract-audit/prove','outcome':'+-'}]
        actions,_,state=compile_model(self.contract,self.params)
        self.assertNotIn('source-contract-typed',state.interfaces)
        self.assertFalse(any(a.available(state) for a in actions))
        result=solve(self.contract,self.params)
        self.assertIsNone(result['first_action'])
        self.assertEqual(result['success_probability'],0)

    def test_downstream_cost_not_local_information_selects_audit(self):
        result=solve(self.contract,self.params,frontier=True)
        self.assertEqual(result['first_action'],'source-contract-audit/prove')
        # Success chain: audit, source, norm, remaining analytics, integration.
        expected=1+.7*4+.7*.09*6+.7*.09*.475*8+.7*.09*.475*.38*4
        self.assertAlmostEqual(result['expected_total_effort'],expected)
        self.assertAlmostEqual(result['success_probability'],.7*.09*.475*.38*.42)
        self.assertEqual(result['objective_projection']['action'],result['first_action'])

    def test_decoder_needs_all_interfaces_not_just_raw_success(self):
        actions,decoders,initial=compile_model(self.contract,self.params)
        d=decoders[0]
        self.assertIsNone(d.decode('whole-section/prove','certified/whole-section',initial))
        complete=State(frozenset(),d.requires)
        self.assertEqual(d.decode('whole-section/prove','certified/whole-section',complete),d.target)
        for missing in d.requires:
            self.assertIsNone(d.decode('whole-section/prove','certified/whole-section',State(frozenset(),d.requires-{missing})))

    def test_inconclusive_is_neither_certificate_nor_logical_refutation(self):
        actions,_,initial=compile_model(self.contract,self.params)
        for a in actions:
            for o in ('+-','--'):
                effect=a.branches[o].effect
                ns=effect.apply(initial)
                self.assertFalse(effect.add)
                self.assertEqual(ns.hypotheses,initial.hypotheses)
                self.assertNotIn('route-live',ns.interfaces)
                self.assertFalse(any(other.available(ns) for other in actions))

    def test_audit_does_not_certify_lift_and_source_still_requires_analytics(self):
        actions,_,initial=compile_model(self.contract,self.params)
        by_name={a.name:a for a in actions}
        audited=by_name['source-contract-audit/prove'].branches['++'].effect.apply(initial)
        self.assertNotIn('source-derivation-conditional-on-analytics',audited.interfaces)
        self.assertTrue(by_name['source-local-lift/prove'].available(audited))
        derived=by_name['source-local-lift/prove'].branches['++'].effect.apply(audited)
        self.assertFalse(by_name['whole-section/prove'].available(derived))

    def test_no_closure_when_analytic_stage_cannot_succeed(self):
        self.params['remaining-phase-analytics/prove_q']=0
        result=solve(self.contract,self.params)
        self.assertEqual(result['success_probability'],0)
        self.assertIsNone(result['first_action'])

    def test_zero_probability_branches_are_not_traversed(self):
        class ImpossibleEffect:
            def apply(self,state):
                raise AssertionError('zero probability branch executed')
        branches={o:Branch(0,ImpossibleEffect()) for o in OUTCOMES}
        branches['++']=Branch(1,Effect(raw='ok'))
        a=Action('a',1,frozenset(),branches)
        p=Planner([a],[Decoder('a','ok',frozenset(),'target')],'target')
        self.assertEqual(p.solve_expected(State(frozenset())).success,1)

    def test_roundoff_does_not_override_cost_in_objective_projection(self):
        objective=Objective('closure',ObjectiveKind.SCIENTIFIC_TARGET,'target','reachability_then_expected_cost')
        actions=[ActionAssessment('cheap',frozenset({'target'}),1,1,.0047760300000000006),
                 ActionAssessment('expensive',frozenset({'target'}),8,8,.004776030000000001)]
        self.assertEqual(recommend(objective,actions).action,'cheap')
        # Relative-only tolerance: a tiny positive chance is NOT abandonment.
        tiny=[ActionAssessment('zero',frozenset({'target'}),0,0,0),
              ActionAssessment('tiny',frozenset({'target'}),1,1,1e-30)]
        self.assertEqual(recommend(objective,tiny).action,'tiny')

    def test_real_success_difference_still_dominates_cost(self):
        objective=Objective('closure',ObjectiveKind.SCIENTIFIC_TARGET,'target','reachability_then_expected_cost')
        actions=[ActionAssessment('cheap',frozenset({'target'}),1,1,.01),
                 ActionAssessment('better',frozenset({'target'}),8,8,.011)]
        self.assertEqual(recommend(objective,actions).action,'better')

    def test_only_proof_outcome_decodes_positive_closure(self):
        actions,decoders,initial=compile_model(self.contract,self.params)
        d=decoders[0]
        complete=State(initial.hypotheses,initial.interfaces|d.requires)
        for a in actions:
            for o,b in a.branches.items():
                if o!='++' or a.name!='whole-section/prove':
                    self.assertIsNone(d.decode(a.name,b.effect.raw,b.effect.apply(complete)))

if __name__=='__main__': unittest.main()
