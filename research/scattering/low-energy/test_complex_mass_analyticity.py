import copy
import json
import unittest
from fractions import Fraction as Q
import check_complex_mass_analyticity as audit


class ComplexMassAnalyticityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=audit.build()

    def test_receipt(self):
        self.assertEqual(self.result,json.loads(audit.RESULT.read_text(encoding='utf-8')))
        self.assertEqual(self.result['certified_pole_boxes'],6)
        self.assertEqual(self.result['real_open_channel_unitarity_checks'],6)
        self.assertEqual(self.result['subthreshold_elastic_checks'],8)

    def test_subthreshold_open_channel(self):
        E0=audit.elastic_entry(audit.phase.IM,0);E1=audit.elastic_entry(audit.phase.IM,1)
        self.assertEqual(E0.conjugate()*E0,audit.F(1))
        self.assertEqual(E1,audit.F(3))
        self.assertTrue(self.result['eta1_subthreshold_contractivity_failure'])
        self.assertFalse(self.result['closed_pair_channel_required_unitary_below_threshold'])
        self.assertFalse(self.result['all_local_UV_completions_excluded'])

    def test_root_enclosures_and_inputs(self):
        lo,hi=audit.eta1_target_box()
        self.assertLessEqual(lo*(1-lo)**2,4)
        self.assertGreaterEqual(hi*(1-hi)**2,4)
        box=audit.pole_box(Q(1),0)
        self.assertLess(Q(box['gamma_squared_lower']),Q(box['gamma_squared_upper']))
        for b,eta in ((0,0),(-1,1),(1,2)):
            with self.assertRaises(AssertionError):audit.pole_box(b,eta)
        with self.assertRaises(AssertionError):audit.elastic_entry(audit.F(1),2)

    def test_contract_guards(self):
        c=json.loads(audit.CONTRACT.read_text(encoding='utf-8'))
        for key,value in c.items():
            if isinstance(value,bool):
                bad=copy.deepcopy(c);bad[key]=not value
                with self.subTest(key=key),self.assertRaises(AssertionError):audit.validate_contract(bad)
        self.assertEqual(len(self.result['hostile_controls_refused']),8)
        self.assertFalse(self.result['physical_rates_or_branching_derived'])


if __name__=='__main__':unittest.main()
