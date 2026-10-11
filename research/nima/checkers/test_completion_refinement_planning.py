import copy
import unittest
from check_completion_refinement_net import validate
from check_completion_refinement_planning import REPO, MODEL, NET, analyze, build_actions, build_worlds
from outcome_reference import load


class PlanningTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.net, cls.model = load(REPO, NET), load(REPO, MODEL)
        cls.structure = validate(REPO, cls.net)
        cls.result = analyze(cls.model, cls.net, cls.structure)

    def test_central_policy_and_no_outcome_mutation(self):
        self.assertEqual(self.result['central']['first_action'], 'prove/operational-spectral-whole-return-certificate')
        self.assertAlmostEqual(self.result['central']['success_probability'], .672)
        self.assertAlmostEqual(self.result['central']['expected_total_effort'], 4.0)
        self.assertFalse(self.result['scientific_outcomes_changed'])
        self.assertEqual(self.net, load(REPO, NET))
        self.assertIsNone(self.result['continuation_action'])
        self.assertNotIn(self.model['claims']['regularity'], {r['claim'] for r in self.result['rows']})
        self.assertIn('not a measured remaining budget', self.result['forecast_scope'])
        self.assertNotIn(self.model['claims']['pi'], {r['claim'] for r in self.result['rows']})
        self.assertTrue(all(w['truth'][self.model['claims']['pi']] for w in self.result['joint_worlds']))

    def test_dependent_priors_are_coherent(self):
        rows = {r['claim']: r for r in self.result['rows']}
        c = self.model['claims']
        self.assertNotIn(c['flow'], rows)
        self.assertNotIn(c['half_turn'], rows)
        self.assertAlmostEqual(rows[c['target']]['subjective_probability_true'], .96)
        self.assertEqual(rows[c['target']]['proof_route_effort_if_all_successful'], 4)

    def test_no_duplicate_flow_rejection_experiment(self):
        actions = build_actions(self.model, self.net, build_worlds(self.model))
        self.assertEqual(len(actions), 2)
        self.assertNotIn('prove/operational-unitary-half-turn', {a['id'] for a in actions})
        self.assertNotIn('prove/completion-phase-metric-regularity', {a['id'] for a in actions})
        self.assertNotIn('prove/completion-unit-circle-flow', {a['id'] for a in actions})
        self.assertNotIn('reject/completion-unit-circle-flow', {a['id'] for a in actions})

    def test_conditioned_sensitivity_selects_whole_return_assembly(self):
        s = self.result['sensitivity']
        self.assertEqual(s['scenario_count'], 27)
        self.assertTrue(s['recommendation_stable'])
        self.assertEqual(sum(s['first_action_counts'].values()), 27)

    def test_model_does_not_refute_general_target_from_route_failure(self):
        c = self.model['claims']
        self.assertTrue(any(w['truth'][c['target']] and not w['truth'][c['half_turn']] for w in build_worlds(self.model)))

if __name__ == '__main__':
    unittest.main()
