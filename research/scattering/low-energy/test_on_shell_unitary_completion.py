import copy
import json
import unittest
from fractions import Fraction as Q
import check_on_shell_unitary_completion as shell


class OnShellUnitaryCompletionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=shell.build()

    def test_receipt(self):
        self.assertEqual(self.result,json.loads(shell.RESULT.read_text(encoding='utf-8')))
        self.assertEqual(self.result['exact_unitarity_checks'],72)
        self.assertEqual(self.result['exact_optical_theorem_checks'],72)
        self.assertEqual(self.result['second_order_forward_checks'],18)
        self.assertEqual(self.result['dark_state_identity_checks'],36)

    def test_same_Born_different_finite_completion(self):
        witness=self.result['fixed_reduced_coupling_conversion_witness']
        self.assertEqual(witness,{'eta_0':'16/25','eta_1':'1'})
        K=shell.scalar_kernel(shell.F(1))
        self.assertEqual(shell.completion(K,Q(),Q()),shell.eye(2))
        self.assertNotEqual(shell.completion(K),shell.completion(K,Q(1)))

    def test_scope(self):
        self.assertTrue(self.result['on_shell_unitary_controls_constructed'])
        for key in ('completion_parameter_source_selected','local_cluster_dynamics_proved','physical_rate_or_branching_derived',
                    'all_unitary_completions_preserve_dark_states','Born_expansion_uniform_all_masses','physical_outcomes_admitted'):
            self.assertFalse(self.result[key])
        self.assertEqual(len(self.result['hostile_controls_refused']),8)
        self.assertEqual(self.result['higher_order_dark_lifting_conversion_witness'],'4/9')

    def test_contract_guards(self):
        c=json.loads(shell.CONTRACT.read_text(encoding='utf-8'))
        for key,value in c.items():
            if isinstance(value,bool):
                bad=copy.deepcopy(c);bad[key]=not value
                with self.subTest(key=key),self.assertRaises(AssertionError):shell.validate_contract(bad)
        for key,value in (('active_fiber_dimension',8),('eta_controls',['0'])):
            bad=copy.deepcopy(c);bad[key]=value
            with self.subTest(key=key),self.assertRaises(AssertionError):shell.validate_contract(bad)


if __name__=='__main__':unittest.main()
