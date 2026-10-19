"""Read-only charge audit, raw-complement retention and preparation ambiguity."""
import copy
from fractions import Fraction as Q
import json
import unittest
import check_native_charge_preparation as charge


class NativeChargePreparationTests(unittest.TestCase):
    def test_marginals_do_not_determine_pair_state(self):
        F=charge.F;a=F(1)/charge.phase.SQ2
        singlet=[F(),a,-a,F()];rho=charge.projector(singlet)
        mixed=charge.scale(F(Q(1,4)),charge.eye(4))
        self.assertNotEqual(rho,mixed)
        for keep in (0,1):
            self.assertEqual(charge.partial_trace(rho,keep),charge.scale(F(Q(1,2)),charge.eye(2)))
            self.assertEqual(charge.partial_trace(mixed,keep),charge.partial_trace(rho,keep))
        with self.assertRaises(AssertionError):charge.partial_trace(mixed,2)

    def test_pseudoreal_map_is_not_complex_linear(self):
        F=charge.F;A=[[F(),F(-1)],[F(1),F()]];z=[F(1),F()]
        theta=lambda v:charge.matrix_act(A,[a.conjugate() for a in v])
        self.assertEqual(theta(theta(z)),charge.three.times(F(-1),z))
        self.assertEqual(theta(charge.three.times(charge.phase.IM,z)),charge.three.times(-charge.phase.IM,theta(z)))
        self.assertNotEqual(theta(charge.three.times(charge.phase.IM,z)),charge.three.times(charge.phase.IM,theta(z)))

    def test_fresh_source_audit_and_flip(self):
        r=charge.build()
        self.assertEqual(r['native_group_cases'],24)
        self.assertTrue(r['linear_raw_flip_unitary_constructed'])
        self.assertTrue(r['raw_flip_fixed_protocol_word_excluded'])
        self.assertTrue(r['stored_negative_protocol_annihilates_positive_code'])
        self.assertEqual(r['raw_complement_dimension_retained'],4)
        self.assertEqual(r['existing_source_Choi_witness_replayed'],'-1/2')
        self.assertEqual(len(r['inspected_source_receipts']),4)
        self.assertEqual(r['pair_swap_sign_counterexamples'][0]['conditional_photon_C_selection'],'singlet_three_triplet_two')
        self.assertEqual(r['pair_swap_sign_counterexamples'][1]['conditional_photon_C_selection'],'singlet_two_triplet_three')
        self.assertTrue(r['owner_files_unchanged'])
        self.assertFalse(r['source_pair_preparation_distribution_selected'])
        flip=charge.decode(r['linear_raw_flip'])
        self.assertEqual(charge.mm(charge.adj(flip),flip),charge.eye(8))

    def test_no_physical_or_statistics_promotion(self):
        c=json.loads(charge.CONTRACT.read_text(encoding='utf-8'));charge.validate_contract(c)
        for key in ('raw_flip_native_word_licensed','Pauli_polarization_identified_with_electromagnetic_charge',
                    'antiunitary_reversal_is_quantum_channel','unitary_pair_charge_conjugation_selected',
                    'fermionic_statistics_source_derived','source_pair_preparation_distribution_selected',
                    'photon_number_charge_parity_source_bound','physical_electron_positron_preparation_bound',
                    'contact_generator_constructed','branching_ratio_derived','live_proposition_inventory_changed',
                    'C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
            bad=copy.deepcopy(c);bad[key]=True
            with self.assertRaises(AssertionError):charge.validate_contract(bad)


if __name__=='__main__':unittest.main()
