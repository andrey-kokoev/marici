import unittest
from bayesian_outcome_planner import Planner, action_metrics, likelihood


def action(name, claim, intent='prove', cost=1, sensitivity=1., requires=()):
    return dict(id=name, claim=claim, intent=intent, cost=cost, sensitivity=sensitivity, requires=list(requires))


class BayesianPlannerTests(unittest.TestCase):
    def test_sound_attempt_outcomes(self):
        p, r = action('p', 't', sensitivity=.7), action('r', 't', 'reject', sensitivity=.2)
        self.assertEqual(likelihood(p, False, '++'), 0)
        self.assertEqual(likelihood(r, True, '-+'), 0)
        self.assertAlmostEqual(likelihood(p, True, '+-'), .3)
        self.assertAlmostEqual(likelihood(r, False, '--'), .8)

    def test_joint_dependency_not_independent_marginals(self):
        worlds = [{'probability': .5, 'truth': {'r': b, 'f': b}} for b in (True, False)]
        result = Planner(worlds, [action('r-proof', 'r'), action('f-proof', 'f', requires=['r'])], 'f', budget=2).solve()
        self.assertAlmostEqual(result['success_probability'], .5)
        self.assertAlmostEqual(result['expected_total_effort'], 1.5)
        self.assertEqual(result['success_branch_trace'], ['r-proof', 'f-proof'])

    def test_probability_one_does_not_supply_a_certificate(self):
        result = Planner([{'probability': 1., 'truth': {'r': True, 'f': True}}],
                         [action('r', 'r'), action('f', 'f', requires=['r'])], 'f', budget=2).solve()
        self.assertEqual(result['success_branch_trace'], ['r', 'f'])
        self.assertEqual(result['expected_total_effort'], 2)

    def test_budget_can_make_portfolio_unreachable(self):
        result = Planner([{'probability': 1., 'truth': {'r': True, 'f': True}}],
                         [action('r', 'r', cost=2), action('f', 'f', cost=2, requires=['r'])], 'f', budget=3).solve()
        self.assertIsNone(result['first_action'])
        self.assertEqual(result['success_probability'], 0)

    def test_rejection_can_save_expected_work(self):
        worlds = [{'probability': .1, 'truth': {'t': True}}, {'probability': .9, 'truth': {'t': False}}]
        result = Planner(worlds, [action('prove', 't', cost=100), action('reject', 't', 'reject')], 't', budget=101).solve()
        self.assertEqual(result['first_action'], 'reject')
        self.assertAlmostEqual(result['success_probability'], .1)
        self.assertAlmostEqual(result['expected_total_effort'], 11.)

    def test_assembly_can_be_useful_without_information_gain(self):
        worlds = [{'probability': 1., 'truth': {'f': True}}]
        a = action('assembly', 'f', sensitivity=.9)
        metrics = action_metrics(worlds, a, 'f')
        self.assertEqual(metrics['claim_information_bits'], 0)
        self.assertAlmostEqual(Planner(worlds, [a], 'f').solve()['success_probability'], .9)

    def test_bad_likelihood_rejected(self):
        with self.assertRaises(ValueError):
            Planner([{'probability': 1., 'truth': {'t': True}}], [action('p', 't', sensitivity=1.1)], 't')

if __name__ == '__main__':
    unittest.main()
