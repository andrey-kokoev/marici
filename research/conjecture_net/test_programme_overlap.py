import json
import unittest
from check_programme_overlap import HOME, validate_contract, validate_attachment, coefficient_audit


class OverlapTests(unittest.TestCase):
    def setUp(self):
        self.contract = json.loads((HOME / 'contracts/programme-overlaps.v1.json').read_text())
        self.hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v5.json').read_text())
        self.terms = json.loads((HOME / 'contracts/programme-terms.v4.json').read_text())

    def test_candidate_overlap(self):
        validate_contract(self.contract)
        validate_attachment(self.hierarchy, self.terms, self.contract)

    def test_complete_coefficient_controls(self):
        result = coefficient_audit()
        self.assertEqual(result['hermitian_basis_size'], 16)
        self.assertEqual(result['readout_coefficient_identities'], 576)

    def test_energy_factor_two_cannot_disappear(self):
        self.contract['overlaps'][0]['readouts'][2]['law'] = 'z* H z=E_H(x)'
        with self.assertRaisesRegex(ValueError, 'energy normalization'):
            validate_contract(self.contract)

    def test_intensity_is_not_authorized_probability(self):
        self.contract['overlaps'][0]['readouts'][3]['physical_authorization'] = True
        with self.assertRaisesRegex(ValueError, 'promoted to physical'):
            validate_contract(self.contract)

    def test_normalization_does_not_supply_born_rule(self):
        self.contract['physical_readout_gate']['normalization_is_born_rule'] = True
        with self.assertRaisesRegex(ValueError, 'physical promotion'):
            validate_contract(self.contract)

    def test_compton_bridge_cannot_be_assumed(self):
        self.hierarchy['overlap_status']['compton_source_bridge'] = 'identity'
        with self.assertRaisesRegex(ValueError, 'physical overlap overclaim'):
            validate_attachment(self.hierarchy, self.terms, self.contract)

    def test_kernel_transport_not_inferred(self):
        self.contract['overlaps'][0]['kernel_observable_transport_proved'] = True
        with self.assertRaisesRegex(ValueError, 'overclaim'):
            validate_contract(self.contract)


if __name__ == '__main__':
    unittest.main()
