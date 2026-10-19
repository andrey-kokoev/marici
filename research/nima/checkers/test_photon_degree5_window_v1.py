from fractions import Fraction as Q
import json
import unittest

import check_photon_degree5_window_v1 as t


class DegreeFiveWindowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_all_helicities_and_permutations(self):
        self.assertEqual(self.r['counts']['helicity'],64)
        self.assertEqual(self.r['counts']['Bose'],72)

    def test_full_component_identities(self):
        self.assertEqual(self.r['counts']['Ward'],768)
        self.assertEqual(self.r['counts']['flow'],256)

    def test_odd_scale_flow(self):
        self.assertEqual(self.r['scale_flow_G5_G5prime_F5_H5'],['-1/120','1/320','65/3072','0'])
        self.assertEqual(self.r['even_sign_forbidden_forward_O_flow'],'13/768')

    def test_degree5_lower_polynomial_not_degree4(self):
        r,_=t.shifts(Q(1,2))
        self.assertEqual(r[0],Q(11,46080));self.assertEqual(r[2],Q(1,960))
        self.assertEqual(r[5],Q(11,3840));self.assertEqual(r[7],-Q(13,6144))

    def test_Cauchy_coefficients_and_rims(self):
        self.assertEqual(self.r['counts']['forward_polynomial'],9)
        self.assertEqual(self.r['counts']['forward_series'],21)
        self.assertEqual(self.r['counts']['rim'],12)

    def test_two_variable_tail_domain(self):
        self.assertLess(t.tail_bound(12,Q(1,16),Q(1,2)),Q(1,10**10))
        with self.assertRaises(AssertionError):t.tail_bound(12,Q(1,4),Q(1,2))

    def test_physical_or_general_inventory_not_promoted(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('general_dim10_Born_cut_inventory_derived','interference_cut_assumed_positive',
                    'finite_physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
            with self.assertRaises(AssertionError,msg=key):t.validate({**c,key:True})


if __name__=='__main__':unittest.main()
