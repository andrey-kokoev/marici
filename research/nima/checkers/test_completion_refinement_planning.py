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

    def test_terminal_policy_and_no_outcome_mutation(self):
        self.assertTrue(self.structure['terminal'])
        self.assertIsNone(self.result['central']['first_action'])
        self.assertEqual(self.result['central']['expected_total_effort'], 0.)
        self.assertEqual(self.result['central']['success_probability'], 1.)
        self.assertFalse(self.result['scientific_outcomes_changed'])
        self.assertEqual(self.net, load(REPO, NET))
        self.assertIsNone(self.result['continuation_action'])
        self.assertIn('recorded mixed verification level', self.result['forecast_scope'])

    def test_terminal_has_no_estimates_or_actions(self):
        self.assertEqual(self.result['rows'], [])
        self.assertEqual(build_actions(self.model, self.net, build_worlds(self.model)), [])
        self.assertEqual(self.result['canonical_action_count'], 0)

    def test_terminal_has_no_sensitivity_recommendations(self):
        self.assertEqual(self.result['sensitivity']['scenario_count'], 0)
        self.assertEqual(self.result['sensitivity']['first_action_counts'], {})
        self.assertTrue(self.result['sensitivity']['recommendation_stable'])

    def test_historical_pre_admission_policy_is_retained(self):
        net, model = copy.deepcopy(self.net), copy.deepcopy(self.model)
        target = model['claims']['target']
        node = next(n for n in net['conjectures'] if n['id'] == target)
        node['outcome'] = None
        model['required_known_proofs'].remove(target)
        model['resolved_estimates_retained'].remove(target)
        result = analyze(model, net, validate(REPO, net))
        self.assertEqual(result['central']['first_action'], 'prove/' + target)
        self.assertAlmostEqual(result['central']['success_probability'], .672)
        self.assertEqual(result['central']['expected_total_effort'], 4.)
        self.assertEqual(result['sensitivity']['scenario_count'], 27)

    def test_model_does_not_refute_general_target_from_route_failure(self):
        c = self.model['claims']
        self.assertTrue(any(w['truth'][c['target']] and not w['truth'][c['half_turn']] for w in build_worlds(self.model)))


if __name__ == '__main__':
    unittest.main()
