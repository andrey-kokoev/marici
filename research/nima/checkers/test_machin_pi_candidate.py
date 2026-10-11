from fractions import Fraction as F
import unittest
from unittest.mock import patch
import check_machin_pi_candidate as checker


class MachinArithmeticTests(unittest.TestCase):
    def test_exact_rotations_and_enclosure(self):
        result = checker.exact_audit()
        self.assertEqual(result['quarter_rotation'], ['0', '1'])
        self.assertEqual(result['half_rotation'], ['-1', '0'])
        center = F(result['candidate_center_rational'])
        radius = F(result['tail_radius_rational'])
        self.assertTrue(3 < center-radius < center+radius < 4)
        self.assertLess(radius, F(1, 10**10))

    def test_cayley_unit_norm(self):
        for q in (F(1, 5), F(1, 239), F(-1, 2)):
            a, b = checker.cayley(q)
            self.assertEqual(a*a+b*b, 1)

    def test_tail_bound_samples_do_not_replace_kernel_bound(self):
        for q in (F(1, 2), F(1, 5), F(1, 239), F(-1, 2)):
            for m in range(12):
                self.assertLessEqual(abs(checker.partial(q, 20)-checker.partial(q, m)), F(1, 2**m))

    def test_wrong_rotation_is_rejected(self):
        with patch.object(checker, 'cayley', return_value=(F(1), F(0))):
            with self.assertRaisesRegex(ValueError, 'rotation arithmetic failed'):
                checker.exact_audit()

if __name__ == '__main__':
    unittest.main()
