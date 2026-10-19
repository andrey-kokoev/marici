"""Exact current-profile projection retains the three-quarter orthogonal remainder."""
import copy
from fractions import Fraction as Q
import json
import unittest
import check_local_helicity_projection as projection


class LocalHelicityProjectionTests(unittest.TestCase):
    def test_shape_norms(self):
        S,P,same,mixed=projection.shape_polynomials();m=projection.m;F=projection.F
        self.assertEqual(m.simplex_integral(m.power(S,2)),F(Q(4,15)))
        self.assertEqual(m.simplex_integral(P),F(Q(1,60)))
        self.assertEqual(m.simplex_integral(same)/3,F(Q(1,72)))
        self.assertEqual([m.simplex_integral(p)/3 for p in mixed],[F(Q(1,360))]*3)

    def test_coherent_projection_coefficients(self):
        m=projection.m;F=projection.F;phase=projection.phase
        S,_,_,_=projection.shape_polynomials();h=projection.packet.tail.triplet_extra_profile()
        factor=3*phase.root(5)/2
        c0=factor*(-phase.IM)*m.simplex_integral(S)/(2*phase.SQ6)
        c1=factor*(-phase.IM)*m.simplex_integral(m.mul(h,S))/(2*phase.SQ6)
        self.assertEqual(c0,-phase.IM*phase.root(6)/8)
        self.assertEqual(c1,phase.IM/8)
        self.assertEqual(c0.conjugate()*c0+c1.conjugate()*c1,F(Q(1,4)))

    def test_fresh_full_helicity_receipt(self):
        r=projection.build()
        self.assertEqual(r,json.loads(projection.RESULT.read_text(encoding='utf-8')))
        self.assertEqual(r['closed_helicity_tensor_cases'],48)
        self.assertEqual(r['pointwise_helicity_norm_checks'],48)
        self.assertEqual(r['second_rotation_moment_checks'],16)
        self.assertEqual(r['prior_profile_span_selected_fraction'],'1/4')
        self.assertEqual(r['prior_profile_span_orthogonal_remainder'],'3/4')
        self.assertEqual(r['three_photon_norm_partition']['mixed_helicity_remainder'],'3/8')
        self.assertEqual(r['with_old_band_support_selected_fraction']['M>4'],'1/64')
        self.assertFalse(r['normalizable_incident_Dirac_packet_constructed'])
        self.assertFalse(r['branching_ratio_derived'])

    def test_no_projection_or_source_promotion(self):
        c=json.loads(projection.CONTRACT.read_text(encoding='utf-8'));projection.validate_contract(c)
        for key,value in c.items():
            if isinstance(value,bool):
                bad=copy.deepcopy(c);bad[key]=not value
                with self.assertRaises(AssertionError):projection.validate_contract(bad)


if __name__=='__main__':unittest.main()
