import copy
import json
import unittest
from fractions import Fraction as Q
import check_packet_weak_coupling_tail as tail


class PacketWeakCouplingTailTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=tail.build()

    def test_receipt(self):
        self.assertEqual(self.result,json.loads(tail.RESULT.read_text(encoding='utf-8')))
        self.assertEqual(self.result['exact_rational_quadrature_cells'],8192)
        self.assertEqual(self.result['tail_first_mass_moment'],'7/2')
        self.assertEqual(self.result['tail_second_mass_moment'],'16')

    def test_completions_differ_at_leading_order(self):
        bs=self.result['leading_constant_rational_enclosures']
        for p in (3,6):
            self.assertLess(Q(bs[f'p{p}_eta1']['upper']),Q(bs[f'p{p}_eta0']['lower']))
        self.assertEqual(self.result['tail_weak_scaling'],{'singlet_two_photon':'epsilon2^1','S_triplet_three_photon':'epsilon3^(1/2)'})

    def test_limits_and_scope(self):
        self.assertTrue(self.result['ordinary_weak_cutoff_limits_commute'])
        self.assertTrue(self.result['rescaled_weak_cutoff_limits_do_not_commute'])
        self.assertFalse(self.result['unbounded_packet_in_Born_domain'])
        self.assertFalse(self.result['physical_rates_or_branching_derived'])
        self.assertEqual(len(self.result['hostile_controls_refused']),8)
        self.assertEqual(tail.tail_weight(2),Q(1))
        for L in (3,4,16):self.assertGreater(tail.tail_weight(L),0)
        with self.assertRaises(AssertionError):tail.tail_weight(1)

    def test_contract_guards(self):
        c=json.loads(tail.CONTRACT.read_text(encoding='utf-8'))
        for key,value in c.items():
            if isinstance(value,bool):
                bad=copy.deepcopy(c);bad[key]=not value
                with self.subTest(key=key),self.assertRaises(AssertionError):tail.validate_contract(bad)
        for key,value in (('quadrature_cells_per_integral',16),('compact_delta_squared','1')):
            bad=copy.deepcopy(c);bad[key]=value
            with self.subTest(key=key),self.assertRaises(AssertionError):tail.validate_contract(bad)


if __name__=='__main__':unittest.main()
