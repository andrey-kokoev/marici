import copy
import json
import unittest
from admit_structural_overlap import ROOT, ACCEPTANCE, POINTER, validate_acceptance, check
from check_programme_admission import HOME, validate
from outcome_reference import OutcomeReferenceError, load, resolve


class AdmissionTests(unittest.TestCase):
    def setUp(self):
        self.acceptance = load(ROOT, ACCEPTANCE)
        self.hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v6.json').read_text())

    def test_live_scoped_admission(self):
        resolved = check()
        self.assertEqual(resolved['outcome'], '++')
        self.assertFalse(resolved['verification']['new_transport_kernel_proved'])
        self.assertFalse(resolved['verification']['physical_readout_authorized'])
        result = validate(self.hierarchy)
        self.assertIsNone(result['root_outcome'])
        self.assertFalse(result['parent_obligation_discharged'])

    def test_acceptance_required(self):
        self.acceptance['accepted'] = False
        with self.assertRaisesRegex(OutcomeReferenceError, 'explicit acceptance'):
            validate_acceptance(self.acceptance)

    def test_acceptance_kernel_overclaim_rejected(self):
        self.acceptance['accepted_verification']['new_transport_kernel_proved'] = True
        with self.assertRaisesRegex(OutcomeReferenceError, 'verification overclaim'):
            validate_acceptance(self.acceptance)

    def test_consumer_kernel_upgrade_rejected(self):
        pointer = load(ROOT, POINTER)
        pointer['accepted_verification']['new_transport_kernel_proved'] = True
        with self.assertRaisesRegex(OutcomeReferenceError, 'verification-level mismatch'):
            resolve(ROOT, pointer)

    def test_root_promotion_rejected(self):
        self.hierarchy['root']['outcome'] = '++'
        with self.assertRaisesRegex(OutcomeReferenceError, 'programme outcome/scope changed'):
            validate(self.hierarchy)

    def test_parent_discharge_rejected(self):
        self.hierarchy['admitted_prerequisite_links'][0]['discharges_parent_obligation'] = True
        with self.assertRaisesRegex(OutcomeReferenceError, 'parent closure'):
            validate(self.hierarchy)

    def test_wrong_acceptance_scope_rejected(self):
        self.acceptance['scope_id'] = 'all-physics'
        with self.assertRaisesRegex(OutcomeReferenceError, 'scope mismatch'):
            validate_acceptance(self.acceptance)


if __name__ == '__main__':
    unittest.main()
