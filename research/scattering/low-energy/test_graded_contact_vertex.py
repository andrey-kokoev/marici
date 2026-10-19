"""Added CAR grading, minus-swap derivation, Hermitian contact and recurrence."""
import copy
from fractions import Fraction as Q
import json
import unittest
import check_graded_contact_vertex as contact


class GradedContactVertexTests(unittest.TestCase):
    def test_creation_sign_and_occupancy(self):
        F=contact.F
        a0=contact.creation(0);a2=contact.creation(2)
        self.assertEqual(a0[1][0],F(1))
        self.assertEqual(a2[5][1],F(-1))
        self.assertEqual(contact.mm(a0,a0),contact.zeros(16,16))
        self.assertEqual(contact.add(contact.mm(a0,a2),contact.mm(a2,a0)),contact.zeros(16,16))
        with self.assertRaises(AssertionError):contact.creation(4)

    def test_exterior_flip_derives_minus_swap(self):
        F=contact.F
        S=[[F(int(i==(j+2)%4)) for j in range(4)] for i in range(4)]
        C=contact.exterior(S);E=contact.neutral_embedding()
        swap=[[F(int((i//2,i%2)==(j%2,j//2))) for j in range(4)] for i in range(4)]
        self.assertEqual(C[0][0],F(1))
        self.assertEqual(contact.mm(C,E),contact.mm(E,contact.scale(F(-1),swap)))
        self.assertEqual(contact.exterior(contact.eye(4)),contact.eye(16))

    def test_source_vertex_symmetry_and_recurrence(self):
        r=contact.build()
        self.assertTrue(r['self_adjoint_contact_vertex_constructed'])
        self.assertEqual(r['native_rotation_cases'],24)
        self.assertEqual(r['complex_contact_intertwiner_dimension'],2)
        self.assertEqual(r['retained_ordered_raw_pair_complement_rank'],60)
        self.assertTrue(r['resonant_free_energy_label_commutator_verified'])
        self.assertTrue(r['positive_total_energy_label_trial_verified'])
        self.assertEqual(r['declared_total_energy_label'],'3')
        examples=r['exact_recurrent_transfer_counterexamples']
        self.assertEqual(examples[0]['singlet_survival_two_three'],['0','1','0'])
        self.assertEqual(examples[0]['triplet_survival_two_three'],['1','0','0'])
        self.assertEqual(examples[1]['triplet_survival_two_three'],['0','0','1'])
        self.assertFalse(r['CAR_statistics_native_derived'])
        self.assertFalse(r['irreversible_annihilation_constructed'])

    def test_no_native_or_rate_promotion(self):
        c=json.loads(contact.CONTRACT.read_text(encoding='utf-8'));contact.validate_contract(c)
        bad=copy.deepcopy(c);bad['survival_and_spectator_records_retained']=False
        with self.assertRaises(AssertionError):contact.validate_contract(bad)
        for key in ('CAR_statistics_native_derived','charge_conjugation_native_selected','native_joint_contact_licensed',
                    'physical_electron_positron_preparation_bound','couplings_source_selected',
                    'irreversible_annihilation_constructed','outgoing_spatial_continuum_constructed','local_field_interaction_constructed',
                    'full_Fock_wavepacket_constructed','one_step_transfer_is_annihilation_rate','branching_ratio_derived',
                    'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
            bad=copy.deepcopy(c);bad[key]=True
            with self.assertRaises(AssertionError):contact.validate_contract(bad)


if __name__=='__main__':unittest.main()
