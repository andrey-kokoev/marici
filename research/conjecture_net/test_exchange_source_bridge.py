import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
from exchange_source_bridge import source_model, validate_word, execute, ExecutionLedger, ldl
import check_exchange_source_bridge as checker


class ExchangeBridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = source_model()
        cls.controls = checker.audit()

    def test_full_source_retention_and_metric_lift(self):
        self.assertEqual(self.controls['raw_source_dimension'], 22)
        self.assertEqual(self.controls['anchor_dimension'], 16)
        self.assertEqual(self.controls['mismatch_dimension'], 6)
        self.assertEqual(self.controls['metric_unitary_port_count'], 6)
        self.assertEqual(self.controls['weighted_hamiltonian_realification_count'], 6)

    def test_noncommuting_response_and_collision_preserved(self):
        self.assertEqual(self.controls['mismatch_commutator_image_rank'], 6)
        self.assertEqual(self.controls['retained_collision_residual_rank'], 2)
        self.assertEqual(self.controls['retained_collision_word_lengths'], [6, 12])

    def test_bad_seam_rejected_before_occurrence_allocation(self):
        ledger = ExecutionLedger()
        with self.assertRaisesRegex(ValueError, 'unmatched source port seam'):
            ledger.execute(('AB', 'AD'), [0] * 22, self.model['raw'], self.model['ports'], 'batch', 'A')
        self.assertFalse(ledger.used_batches)

    def test_source_attachment_required(self):
        with self.assertRaisesRegex(ValueError, 'vertex attachment mismatch'):
            execute(('AB',), [0] * 22, self.model['raw'], self.model['ports'], 'batch', 'B')

    def test_reused_execution_identity_rejected(self):
        ledger = ExecutionLedger()
        ledger.execute(('AB',), [0] * 22, self.model['raw'], self.model['ports'], 'batch', 'A')
        with self.assertRaisesRegex(ValueError, 'already used'):
            ledger.execute(('AB',), [0] * 22, self.model['raw'], self.model['ports'], 'batch', 'A')

    def test_indefinite_metric_rejected(self):
        with self.assertRaisesRegex(ValueError, 'not positive definite'):
            ldl([[1, 0], [0, -1]])

    def test_continuous_leg_does_not_supply_free_control_switching(self):
        self.assertFalse(self.controls['free_switching_of_all_ports_supplied'])
        contract = json.loads((checker.HOME / 'contracts/exchange-source-bridge.v1.json').read_text())
        contract['boundary']['freely_switchable_six_port_controls_authorized'] = True
        with self.assertRaisesRegex(ValueError, 'boundary promotion'):
            checker.validate_contract(contract)

    def test_source_dependency_drift_rejected(self):
        pins = checker.live_source_pins()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for relative in pins:
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(checker.ROOT / relative, target)
            dependency = root / 'research/nima/checkers/check_seed_port_exchange_binding.py'
            dependency.write_text('changed source')
            with patch.object(checker, 'ROOT', root):
                with self.assertRaisesRegex(ValueError, 'stale exchange dependency'):
                    checker.live_source_pins()

    def test_full_domain_not_silently_compressed_to_C4(self):
        contract = json.loads((checker.HOME / 'contracts/exchange-source-bridge.v1.json').read_text())
        contract['target']['carrier'] = 'C4'
        with self.assertRaisesRegex(ValueError, 'domain compressed'):
            checker.validate_contract(contract)


if __name__ == '__main__':
    unittest.main()
