"""EF1's exact kinematics and explicit limits on its explanatory status."""
import copy
from fractions import Fraction as Q
import json
import unittest
import check_edge_face_hinge as hinge


class EdgeFaceHingeTests(unittest.TestCase):
    def test_actual_source_hinge_and_belt(self):
        r=hinge.build()
        self.assertEqual(r['perpendicular_gram'],[['6','2'],['2','6']])
        self.assertEqual(r['dihedral_cosine'],'1/3')
        self.assertEqual(r['reflected_apex'],['5/3','5/3','-5/3'])
        self.assertEqual(r['pair_and_belt_total_volume'],'16/3')
        self.assertEqual(r['face_contacts'],['ABD at +alpha','ABC at -alpha'])
        self.assertTrue(r['same_oriented_outer_boundary_verified'])

    def test_metric_rotation_is_not_a_permutation(self):
        R=[[Q(),Q(-1)],[Q(1),Q(2,3)]];G=[[Q(6),Q(2)],[Q(2),Q(6)]]
        self.assertEqual(hinge.det2(R),1)
        self.assertEqual(hinge.mm(hinge.mm(hinge.tr(R),G),R),G)
        self.assertNotEqual(hinge.mm(R,R),[[Q(1),Q()],[Q(),Q(1)]])
        self.assertEqual(hinge.mm(R,[[Q()],[Q(1)]]),[[Q(-1)],[Q(2,3)]])

    def test_assumed_finite_duration_capture_not_static_sampling(self):
        self.assertEqual(hinge.first_hit_fraction(Q()),0)
        self.assertEqual(hinge.first_hit_fraction(Q(1,21)),Q(1,21))
        self.assertEqual(hinge.first_hit_fraction(Q(1)),1)
        self.assertEqual(hinge.first_hit_fraction(Q(3)),1)
        with self.assertRaises(AssertionError):hinge.first_hit_fraction(Q(-1))

    def test_no_promotion_to_native_dynamics_or_physical_proof(self):
        c=json.loads(hinge.CONTRACT.read_text(encoding='utf-8'))
        for key in ('native_rotation_generator_constructed','finite_capture_probability_derived',
                    'static_face_alignment_has_positive_angular_measure','outgoing_photon_factorization_constructed',
                    'physical_species_binding_supplied','ratio_372_predicted','live_proposition_inventory_changed',
                    'C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
            bad=copy.deepcopy(c);bad[key]=True
            with self.assertRaises(AssertionError):hinge.validate_contract(bad)


if __name__=='__main__':unittest.main()
