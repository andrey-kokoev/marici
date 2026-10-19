"""Exact finite controls for the rim point-sector audit."""
import unittest
from fractions import Fraction as Q
import check_rim_bound_sector as rim


class RimPointSectorTests(unittest.TestCase):
    def test_off_diagonal_pivot_and_null_direction(self):
        self.assertEqual(rim.inertia([[Q(0),Q(1),Q(0)],[Q(1),Q(0),Q(0)],[Q(0),Q(0),Q(0)]]),(1,1,1))
        self.assertEqual(rim.inertia([[Q(1),Q(1)],[Q(1),Q(1)]]),(1,0,1))

    def test_congruence_preserves_inertia(self):
        D=[[Q(d if i==j else 0) for j in range(4)] for i,d in enumerate((2,-3,0,5))]
        C=[[Q(int(i==j or j==i+1)) for j in range(4)] for i in range(4)]
        self.assertEqual(rim.inertia(rim.mm(rim.mm(rim.tr(C),D),C)),(2,1,1))

    def test_nullspace_witness(self):
        A=[[Q(1),Q(2),Q(0),Q(1)],[Q(0),Q(0),Q(1),Q(1)]]
        N=rim.nullspace(A)
        self.assertEqual(len(N[0]),2)
        self.assertTrue(rim.zeros(rim.mm(A,N)))
        self.assertEqual(len(rim.rref(rim.tr(N))[1]),2)

    def test_full_fixture_count_and_verification_boundary(self):
        r,_=rim.finite_audit()
        self.assertEqual((r['total_point_subspace_dimension'],r['embedded_point_modes_counted_with_multiplicity']),(21,13))
        self.assertEqual(r['point_modes_below_threshold_counted_with_multiplicity'],8)
        self.assertEqual(r['dark_core_inertia'],[13,0,6])
        intervals=[list(map(Q,b['energy_interval'])) for b in r['certified_accessible_bound_brackets']]
        self.assertLess(intervals[0][1],intervals[1][0])
        for lo,hi in intervals:
            self.assertTrue(0<lo<hi<Q(1,2))
            self.assertLessEqual(hi-lo,Q(1,10**12))
        self.assertFalse(r['singular_continuous_absence_proved_here'])
        self.assertFalse(r['wave_operator_completeness_proved_here'])
        self.assertFalse(r['new_live_proposition_admitted'])
        self.assertFalse(r['C12_protocol_renewed'])


if __name__=='__main__':unittest.main()
