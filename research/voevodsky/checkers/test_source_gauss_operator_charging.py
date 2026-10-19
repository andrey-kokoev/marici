"""Exact controls for the new, explicitly excluded charging candidate."""
from fractions import Fraction as F
import unittest
from check_source_gauss_operator_charging import construct,response,positive_definite,ground_bounds,read,digest,OUT

class ChargingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.model=construct(F(3,5),F(1,5))
    def test_common_fixture_energies(self):
        self.assertEqual(self.model['proton_energy'],'32/175')
        self.assertEqual(self.model['elementary_energy'],'11/50')
        self.assertEqual(self.model['proton_per_elementary'],'64/77')
        self.assertEqual(self.model['belt_distinct_diagonal_count'],3)
    def test_ldl_detects_sign_and_singular_boundary(self):
        self.assertTrue(positive_definite([[F(2),F(-1)],[F(-1),F(2)]]))
        self.assertFalse(positive_definite([[F(1),F(-1)],[F(-1),F(1)]]))
        self.assertFalse(positive_definite([[F(1),F(2)],[F(2),F(1)]]))
    def test_ground_interval_against_exact_two_site_root(self):
        lo,hi=ground_bounds([[F(1),F(-1)],[F(-1),F(1)]],[F(1),F(1)],[F(0),F(2)])
        self.assertLess(hi-lo,F(1,10**23))
        self.assertGreaterEqual((2-lo)**2,2);self.assertLessEqual((2-hi)**2,2)
        lo,hi=ground_bounds([[F(1),F(-1)],[F(-1),F(1)]],[F(1),F(1)],[F(3),F(3)])
        self.assertEqual((lo,hi),(3,3))
    def test_gauss_response_relabeling(self):
        edges=[(0,1,F(1)),(1,2,F(1))];ports=[0,2]
        C=response(3,edges,ports);perm=[2,0,1]
        Cp=response(3,[(perm[i],perm[j],w) for i,j,w in edges],[perm[i] for i in ports])
        self.assertTrue(all(C[i][j]==Cp[perm[i]][perm[j]] for i in range(3) for j in range(3)))
    def test_variance_is_retained(self):
        self.assertEqual(self.model['charge_variance_energy_difference'],'9/200')
        C=response(2,[(0,1,F(1))],[0,1]);rho=[F(1,3),F(2,3)]
        gap=sum(r*C[i][i] for i,r in enumerate(rho))-sum(rho[i]*C[i][j]*rho[j] for i in range(2) for j in range(2))
        self.assertGreater(gap,0)
    def test_scale_free_bound_and_held_out_failure(self):
        cp=F(self.model['proton_capacitance_diagonal'])
        self.assertEqual(cp,F(29,105))
        for beta in (F(1,1000),F(3,5),F(1000)):
            for eta in (F(0),F(1,5),F(1000)):
                ratio=(beta*cp+eta)/(2*beta/5+eta)
                self.assertGreaterEqual(ratio,F(29,42));self.assertLess(ratio,1)
        lo,hi=map(F,self.model['belt_minus_proton_per_elementary_interval'])
        self.assertLess(hi-lo,F(1,10**22));self.assertLess(hi,F(2530989,1000000))
    def test_result_provenance_and_nonadmission(self):
        result=read(OUT);self.assertTrue(result['verification_passed'])
        self.assertEqual(result['candidate_mass_conjecture'],'refuted_within_declared_reduced_electrostatic_branch')
        self.assertFalse(result['physical_admission']);self.assertFalse(result['parameters_fitted_back_into_model'])
        for path,h in result['source_hashes'].items():
            with self.subTest(path=path):self.assertEqual(digest(path),h)

if __name__=='__main__':unittest.main()
