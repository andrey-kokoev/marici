import copy
import json
import unittest
from fractions import Fraction as Q
import check_outgoing_born_map as born


class OutgoingBornMapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=born.build()

    def test_receipt(self):
        self.assertEqual(self.result,json.loads(born.RESULT.read_text(encoding='utf-8')))
        self.assertEqual(self.result['exact_antiderivative_checks'],12)
        self.assertEqual(born.norm_constants(),(Q(1,128),Q(1,276480),Q(1,311040)))

    def test_scope(self):
        self.assertTrue(self.result['finite_compact_packet_transition_norms_constructed'])
        self.assertTrue(self.result['Born_unitarity_deficit_retained'])
        self.assertTrue(self.result['coherent_current_null_alternative_has_zero_Born_output'])
        for key in ('Born_norm_is_exact_probability','unitary_scattering_operator_constructed','physical_preparation_selected',
                    'source_selected_branching_ratio_derived','physical_outcomes_admitted'):
            self.assertFalse(self.result[key])
        self.assertEqual(len(self.result['hostile_controls_refused']),8)

    def test_contract_guards(self):
        c=json.loads(born.CONTRACT.read_text(encoding='utf-8'))
        for key,value in c.items():
            if isinstance(value,bool):
                bad=copy.deepcopy(c);bad[key]=not value
                with self.subTest(key=key),self.assertRaises(AssertionError):born.validate_contract(bad)
        for key,value in (('Fock_factorials',{'two':1,'three':1}),('coupling_mass_dimensions',{'g2':-3,'g3':-3})):
            bad=copy.deepcopy(c);bad[key]=value
            with self.subTest(key=key),self.assertRaises(AssertionError):born.validate_contract(bad)

    def test_mass_integrals(self):
        self.assertEqual(self.result['mass_integrals']['I6']['log_ratio'],'0')
        self.assertLess(Q(self.result['mass_integrals']['I3']['log_ratio']),0)
        for bounds in self.result['mass_integral_strict_rational_bounds'].values():
            lower,upper=map(Q,bounds);self.assertGreater(lower,0);self.assertGreater(upper,lower)


if __name__=='__main__':unittest.main()
