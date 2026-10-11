import contextlib
import io
import json
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import check_completion_trig_addition as checker


class CompletionAdditionReceiptTests(unittest.TestCase):
    def receipt(self, cached=False, code=0, timeout=False, changed=False):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'results').mkdir()
            args = ['checker'] + (['--cached'] if cached else [])
            run = SimpleNamespace(returncode=code, stdout=b'check result', stderr=b'')
            hashes = {}
            def digest(path):
                hashes[path] = hashes.get(path, 0)+1
                return 'changed' if changed and hashes[path] > 1 else 'test-digest'
            with patch.object(checker, 'ROOT', root), patch.object(checker, 'closure', return_value=set()), \
                 patch.object(checker, 'digest', side_effect=digest), \
                 patch.object(checker.subprocess, 'run', return_value=run,
                              side_effect=subprocess.TimeoutExpired('agda', 1800) if timeout else None), \
                 patch('sys.argv', args), contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaises(SystemExit) as raised:
                    checker.main()
            result = json.loads(next((root/'results').glob('*.json')).read_text(encoding='utf-8'))
            return raised.exception.code, result

    def test_cached_pass_does_not_admit_proof(self):
        code, receipt = self.receipt(cached=True)
        self.assertEqual(code, 0)
        self.assertFalse(receipt['fresh_closure_completed'])
        self.assertFalse(receipt['completion_addition_laws_proved'])
        self.assertFalse(receipt['phase_addition_law_proved'])

    def test_fresh_pass_covers_all_operational_inputs(self):
        code, receipt = self.receipt()
        self.assertEqual(code, 0)
        for field in ('fresh_closure_completed', 'completion_addition_laws_proved',
                      'phase_addition_law_proved', 'all_completion_inputs',
                      'all_completion_scales_and_times', 'uses_operational_sine_cosine_and_phase'):
            self.assertIs(receipt[field], True)
        self.assertFalse(receipt['assumed_addition_law'])
        self.assertTrue({'completion-cosine-addition', 'completion-sine-addition',
                         'operational-phase-addition'} <= set(receipt['theorems']))
        self.assertIn('--ignore-interfaces', receipt['command'])
        self.assertIn('--safe', receipt['command'])

    def test_addition_is_not_pi_or_derivative(self):
        _, receipt = self.receipt()
        for field in ('arctangent_cayley_bridge_proved', 'pi_endpoints_proved',
                      'standard_pi_identification_kernel_proved', 'derivative_proved',
                      'unitary_half_turn_proved', 'full_claim_proved'):
            self.assertIs(receipt[field], False)
        self.assertIsNone(receipt['outcome'])
        self.assertIn('MachinEndpoints', receipt['remaining_obligations'])

    def test_failure_timeout_and_changing_sources_reject_proof(self):
        for kwargs, status in [({'code': 42}, 'fail'), ({'timeout': True}, 'timeout'),
                               ({'changed': True}, 'fail')]:
            with self.subTest(kwargs=kwargs):
                code, receipt = self.receipt(**kwargs)
                self.assertEqual(code, 1)
                self.assertEqual(receipt['status'], status)
                self.assertFalse(receipt['fresh_closure_completed'])
                self.assertFalse(receipt['completion_addition_laws_proved'])
                self.assertFalse(receipt['phase_addition_law_proved'])


if __name__ == '__main__':
    unittest.main()
