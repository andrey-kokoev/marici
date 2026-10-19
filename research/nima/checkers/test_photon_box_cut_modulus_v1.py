import json
import unittest
from fractions import Fraction as Q

import check_photon_box_cut_modulus_v1 as t


class BoxCutModulusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_explicit_constants(self):
        self.assertEqual(t.holder_constant(Q(1)),Q(226,21))
        self.assertEqual(self.r['certificate']['cut_diameter_coefficient'],'2713/3360')
        self.assertEqual(self.r['upper_exponent'],'1/3')

    def test_all_strata_controlled(self):
        self.assertEqual(self.r['two_point_controls'],178)
        self.assertTrue(self.r['all_leading_strata_included'])

    def test_cube_root_rational_enclosure(self):
        for q in (Q(),Q(1,1000),Q(1,10**90),Q(1)):
            hi=t.cube_root_upper(q);self.assertGreaterEqual(hi**3,q)
            if q:self.assertLessEqual(hi**3,8*q)
        self.assertEqual(t.modulus(Q(),Q(1)),0)

    def test_bounded_not_unbounded_obstruction(self):
        self.assertEqual(self.r['excluded_exponents'],'alpha>1/2')
        rows=self.r['bounded_sharpness_controls'];self.assertEqual(len(rows),4)
        self.assertTrue(all(Q(row['quartic_max_norm'])<=1 for row in rows))
        self.assertGreater(Q(rows[-1]['Lipschitz_amplification']),Q(rows[0]['Lipschitz_amplification']))

    def test_noise_is_deterministic(self):self.assertEqual(self.r['compatible_noise_cut_diameter'],'omega_M(2*epsilon)')

    def test_assumptions_required(self):
        with self.assertRaises(AssertionError):t.modulus(Q(1,100),Q(1,2))
        self.assertFalse(self.r['physical_source_box_licensed'])
        self.assertFalse(self.r['one_half_upper_modulus_derived'])

    def test_unearned_promotions_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('one_third_exponent_proved_optimal','one_half_upper_modulus_derived','physical_source_box_licensed',
                    'unique_Born_source_or_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
            with self.assertRaises(AssertionError,msg=key):t.validate({**c,key:True})


if __name__=='__main__':unittest.main()
