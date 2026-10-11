import contextlib
from fractions import Fraction as F
import io
import json
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import check_trig_addition_foundations as checker


class AdditionFoundationTests(unittest.TestCase):
    def test_distinct_inputs_and_residuals(self):
        audit = checker.exact_audit()
        self.assertEqual(audit['status'], 'pass')
        self.assertEqual(audit['input_pairs'], 25)
        self.assertEqual(audit['coefficient_cases'], 325)
        self.assertEqual(audit['residual_cases'], 125)

    def test_zero_coefficients(self):
        for n in range(10):
            self.assertEqual(checker.cosine_term(F(0), n), int(n == 0))
            self.assertEqual(checker.sine_term(F(0), n), 0)

    def test_broken_sine_sign_rejected(self):
        original = checker.sine_term
        with patch.object(checker, 'sine_term', side_effect=lambda q, n: abs(original(q, n))):
            with self.assertRaisesRegex(ValueError, 'coefficient mismatch'):
                checker.exact_audit()

    def receipt(self, cached=False, code=0, timeout=False):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'results').mkdir()
            args = ['checker'] + (['--cached'] if cached else [])
            run = SimpleNamespace(returncode=code, stdout=b'check result', stderr=b'')
            with patch.object(checker, 'ROOT', root), patch.object(checker, 'closure', return_value=set()), \
                 patch.object(checker, 'digest', return_value='test-digest'), \
                 patch.object(checker, 'exact_audit', return_value={'status': 'pass'}), \
                 patch.object(checker.subprocess, 'run', return_value=run,
                              side_effect=subprocess.TimeoutExpired('agda', 1800) if timeout else None), \
                 patch('sys.argv', args), contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaises(SystemExit) as raised:
                    checker.main()
            result = json.loads(next((root/'results').glob('*.json')).read_text(encoding='utf-8'))
            return raised.exception.code, result

    def test_cached_pass_cannot_be_fresh(self):
        code, receipt = self.receipt(cached=True)
        self.assertEqual(code, 0)
        self.assertFalse(receipt['fresh_closure_completed'])
        self.assertFalse(receipt['distinct_input_coefficients_freshly_proved'])

    def test_fresh_pass_is_not_completion_addition_or_endpoint_proof(self):
        code, receipt = self.receipt()
        self.assertEqual(code, 0)
        self.assertTrue(receipt['fresh_closure_completed'])
        for field in ('completion_addition_laws_proved', 'arctangent_cayley_bridge_proved',
                      'pi_endpoints_proved', 'standard_pi_identification_kernel_proved',
                      'unitary_half_turn_proved', 'full_claim_proved'):
            self.assertIs(receipt[field], False)
        self.assertIsNone(receipt['outcome'])

    def test_failure_and_timeout_do_not_admit_component(self):
        for kwargs, status in [({'code': 42}, 'fail'), ({'timeout': True}, 'timeout')]:
            with self.subTest(status=status):
                code, receipt = self.receipt(**kwargs)
                self.assertEqual(code, 1)
                self.assertEqual(receipt['status'], status)
                self.assertFalse(receipt['fresh_closure_completed'])
                self.assertFalse(receipt['rational_partial_sum_transfer_freshly_proved'])


if __name__ == '__main__':
    unittest.main()
