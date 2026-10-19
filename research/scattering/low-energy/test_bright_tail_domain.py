import copy
import json
import unittest
from fractions import Fraction as Q
import check_bright_tail_domain as domain


class BrightTailDomainTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=domain.build()

    def test_receipt(self):
        self.assertEqual(self.result,json.loads(domain.RESULT.read_text(encoding='utf-8')))
        self.assertEqual(self.result['critical_power_log_cases'],40)
        self.assertEqual(self.result['exact_tail_moment_comparisons'],72)

    def test_critical_boundaries(self):
        self.assertFalse(domain.bright_tail_moment_finite(6,1,Q(13,2),Q(1,2)))
        self.assertTrue(domain.bright_tail_moment_finite(6,1,Q(13,2),Q(3,4)))
        self.assertTrue(domain.bright_tail_moment_finite(6,2,14))
        self.assertFalse(domain.bright_tail_moment_finite(6,3,14))
        with self.assertRaises(AssertionError):domain.power_tail_moment(27,4)

    def test_controls_and_scope(self):
        self.assertEqual(domain.power_tail_moment(0,4),1)
        self.assertEqual(domain.exponential_tail_moment(0,4),1)
        self.assertTrue(self.result['heavy_dark_tail_in_all_kernel_power_domains'])
        self.assertEqual(self.result['exponential_eta0_probability_Taylor_radius'],'0')
        self.assertFalse(self.result['interaction_form_factor_derived'])
        self.assertFalse(self.result['physical_rate_or_branching_derived'])
        self.assertEqual(len(self.result['hostile_controls_refused']),8)

    def test_contract_guards(self):
        c=json.loads(domain.CONTRACT.read_text(encoding='utf-8'))
        for key,value in c.items():
            if isinstance(value,bool):
                bad=copy.deepcopy(c);bad[key]=not value
                with self.subTest(key=key),self.assertRaises(AssertionError):domain.validate_contract(bad)
        for key,value in (('power_tail_amplitude_exponent',3),('critical_log_condition','s>=1/2')):
            bad=copy.deepcopy(c);bad[key]=value
            with self.subTest(key=key),self.assertRaises(AssertionError):domain.validate_contract(bad)


if __name__=='__main__':unittest.main()
