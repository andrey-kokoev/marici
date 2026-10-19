import json
import unittest
from pilot_carrier import (LABELS, Operation, Schedule, PathRecord, TickFragment,
                           Occurrence, promote, basis, intensity)
from check_pilot_carrier_interface import HOME, record_audit, validate_contract, validate_dossier


class PilotCarrierTests(unittest.TestCase):
    def test_exact_record_audit(self):
        result = record_audit()
        self.assertEqual(result['path_records_audited'], 124)
        self.assertEqual(result['composable_associativity_triples_audited'], 1372)
        self.assertEqual(result['fixed_source_tick_tag_cases'], 16)

    def test_source_dossier(self):
        validate_dossier(json.loads((HOME / 'contracts/pilot-source-records.v1.json').read_text()))

    def test_fitted_input_cannot_enter_unreviewed(self):
        dossier = json.loads((HOME / 'contracts/pilot-source-records.v1.json').read_text())
        dossier['fitting_inputs'].append('physical-answer')
        with self.assertRaisesRegex(ValueError, 'new physical inputs'):
            validate_dossier(dossier)

    def test_source_origin_drift_rejected(self):
        dossier = json.loads((HOME / 'contracts/pilot-source-records.v1.json').read_text())
        dossier['records'][0]['origin']['integrity_or_version'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'stale source origin'):
            validate_dossier(dossier)

    def test_wrong_source_type_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Bool x Bool'):
            PathRecord((0, 0), ())

    def test_noncomposable_paths_rejected(self):
        first = PathRecord(LABELS[0], (Operation.LEFT,))
        with self.assertRaisesRegex(ValueError, 'noncomposable'):
            first.then(PathRecord(LABELS[0], (Operation.RIGHT,)))

    def test_identity_endpoint_does_not_erase_history(self):
        empty = PathRecord(LABELS[0], ())
        loop = PathRecord(LABELS[0], (Operation.LEFT, Operation.LEFT))
        self.assertEqual(empty.target, loop.target)
        self.assertNotEqual(empty, loop)

    def test_same_record_occurrences_both_retained(self):
        path = PathRecord(LABELS[0], ())
        occurrences = (Occurrence('first', path), Occurrence('second', path))
        family = promote(occurrences, 'source', 'batch-1')[0]
        self.assertEqual(family.members, occurrences)

    def test_duplicate_occurrence_ids_rejected(self):
        item = Occurrence('same', PathRecord(LABELS[0], ()))
        with self.assertRaisesRegex(ValueError, 'duplicate occurrence'):
            promote((item, item), 'target', 'batch-1')

    def test_grouping_key_not_inferred(self):
        with self.assertRaisesRegex(ValueError, 'explicitly source or target'):
            promote((), 'automatic', 'batch-1')

    def test_batch_namespace_required(self):
        with self.assertRaisesRegex(ValueError, 'batch namespace'):
            promote((), 'source', '')

    def test_tick_equal_tags_are_valid(self):
        tick = TickFragment(LABELS[0], Schedule.LEFT_FIRST, Schedule.LEFT_FIRST)
        self.assertEqual(tick.seam_labels[0], tick.seam_labels[1])
        self.assertEqual(tick, TickFragment.rebuild(tick.source, tick.tags))

    def test_intensity_is_not_full_state(self):
        vector = basis(LABELS[0])
        opposite = tuple(-value for value in vector)
        self.assertNotEqual(vector, opposite)
        self.assertEqual(intensity(vector), intensity(opposite))

    def test_universal_carrier_promotion_rejected(self):
        contract = json.loads((HOME / 'contracts/pilot-carrier-interface.v1.json').read_text())
        contract['evidence_boundary']['universal_carrier_embedding_proved'] = True
        with self.assertRaisesRegex(ValueError, 'overclaim'):
            validate_contract(contract)


if __name__ == '__main__':
    unittest.main()
