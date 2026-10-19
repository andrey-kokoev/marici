import copy
import json
import unittest
from check_structural_pilot_transport import (CONTRACT, algebra_audit, validate_contract,
                                            realify, identity, zeros, mul, scale)


class StructuralTransportTests(unittest.TestCase):
    def setUp(self):
        self.contract = json.loads(CONTRACT.read_text(encoding='utf-8'))

    def test_contract_scope(self):
        validate_contract(self.contract)

    def test_exact_basis_and_native_algebra(self):
        result = algebra_audit()
        self.assertEqual(result['composition_basis_pairs'], 1024)
        self.assertEqual(result['state_action_basis_pairs'], 256)

    def test_missing_pi_scale_rejected(self):
        self.contract['common_witness']['generators_t'] = 'H_j=Q_j'
        with self.assertRaisesRegex(ValueError, 'scale changed'):
            validate_contract(self.contract)

    def test_inverse_return_substitution_rejected(self):
        self.contract['common_witness']['return_convention'] = 'inverse-phase time reversal'
        with self.assertRaisesRegex(ValueError, 'orientation changed'):
            validate_contract(self.contract)

    def test_false_kernel_promotion_rejected(self):
        self.contract['verification_boundary']['new_realification_kernel_proved'] = True
        with self.assertRaisesRegex(ValueError, 'overclaim'):
            validate_contract(self.contract)

    def test_physical_promotion_rejected(self):
        self.contract['verification_boundary']['physical_recovery_verified'] = True
        with self.assertRaisesRegex(ValueError, 'overclaim'):
            validate_contract(self.contract)

    def test_wrong_coordinate_order_rejected(self):
        self.contract['common_witness']['labels'] = ['00', '10', '01', '11']
        with self.assertRaisesRegex(ValueError, 'coordinate order'):
            validate_contract(self.contract)

    def test_minus_i_generator_sign(self):
        # Multiplication by -i sends (q,p) to (p,-q), not (-p,q).
        actual = realify(zeros(1), scale(-1, identity(1)))
        self.assertEqual(actual, [[0, 1], [-1, 0]])
        self.assertNotEqual(actual, scale(-1, actual))


if __name__ == '__main__':
    unittest.main()
