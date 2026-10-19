"""Exact conservation counterexamples, exceptional placements, and scope guards."""
import copy
from fractions import Fraction as Q
import json
import unittest
import check_normal_direction_contact as contact


class NormalDirectionContactTests(unittest.TestCase):
    def test_rational_chart_preserves_rigid_tetrahedron(self):
        P,D=contact.points_polynomial()
        for r in (Q(1,2),Q(2),Q(-2)):
            points={k:tuple(contact.peval(v,r)/contact.peval(D,r) for v in p) for k,p in P.items()}
            for cell in ('ABCD','ABEF'):
                for i,a in enumerate(cell):
                    for b in cell[i+1:]:
                        v=contact.hinge.sub(points[a],points[b]);self.assertEqual(contact.hinge.dot(v,v),8)
        self.assertEqual(len(contact.partitions()),10)

    def test_original_template_has_all_angle_obstruction(self):
        P,D=contact.points_polynomial()
        cross=contact.pcross(contact.pnormal(P,'ACE'),contact.pnormal(P,'BDF'))
        expected=contact.ps(-128,contact.pm([Q(),Q(),Q(2),Q(),Q(1)],contact.pm(D,D)))
        self.assertEqual(cross[2],expected)
        for r in (Q(1,2),Q(2),Q(-2)):
            self.assertLess(contact.peval(cross[2],r),0)
        self.assertEqual(contact.ipoly([Q(1),Q(-1)],(Q(2),Q(3))),(Q(-2),Q(-1)))

    def test_full_counterexample_and_three_ray_permission(self):
        r=contact.build()
        self.assertEqual(len(r['complementary_triangle_partition_audits']),10)
        self.assertEqual(r['minimum_unoriented_angle_sine_squared'],'104/729')
        self.assertEqual(r['half_angle_cone_threshold_sine_squared'],'1/27')
        self.assertEqual(len(r['nondegenerate_parallel_partitions_at_pi']),4)
        self.assertEqual(r['already_present_input_face_pairs_at_pi'],[['ACD','BEF'],['AEF','BCD']])
        self.assertEqual(r['face_three_cm_energy_fractions'],['1/3']*3)
        self.assertFalse(r['fully_specified_contact_generator_constructed'])
        self.assertFalse(r['EF1_as_a_whole_refuted'])
        for row in r['complementary_triangle_partition_audits']:
            lo,hi=map(Q,row['common_interval_component_enclosure']);self.assertGreater(lo*hi,0)

    def test_no_general_photon_or_branching_promotion(self):
        c=json.loads(contact.CONTRACT.read_text(encoding='utf-8'))
        for key in ('normal_direction_map_source_derived','fully_specified_contact_generator_constructed',
                    'all_two_triangle_constructions_excluded','EF1_as_a_whole_refuted','three_photon_production_derived',
                    'branching_ratio_derived','live_proposition_inventory_changed','C12_protocol_renewed',
                    'high_energy_protocol_executed','physical_outcomes_admitted'):
            bad=copy.deepcopy(c);bad[key]=True
            with self.assertRaises(AssertionError):contact.validate_contract(bad)


if __name__=='__main__':unittest.main()
