"""Full Fock normalization with a genuine boost envelope and retained gauge phases."""
import copy
from fractions import Fraction as Q
import json
import unittest
import check_total_momentum_packet as packet


class TotalMomentumPacketTests(unittest.TestCase):
    def test_boost_mass_jacobian_and_inverse(self):
        F=packet.F;q=[F(Q(1,8)),F(),F()];u=packet.velocity(q)
        self.assertEqual(u[0],F(Q(65,63)))
        self.assertEqual(packet.minkowski(u,u),F(1))
        self.assertEqual(packet.act(packet.boost(u),[F(1),F(),F(),F()]),u)
        self.assertEqual(packet.coarea_jacobian(F(2),q),8*F(8)/(F(1)-q[0]*q[0])/(F(1)-q[0]*q[0])/(F(1)-q[0]*q[0]))
        with self.assertRaises(AssertionError):packet.velocity([F(1),F(),F()])

    def test_cube_and_missing_mass_density(self):
        self.assertEqual(8*packet.cube_integral(packet.m.const(1)),packet.F(1))
        self.assertEqual(30*packet.tail.beta_integral(2,6),Q(1))
        with self.assertRaises(AssertionError):packet.tail.beta_integral(5,6)

    def test_fresh_Fock_packet_receipt(self):
        r=packet.build()
        self.assertEqual(r,json.loads(packet.RESULT.read_text(encoding='utf-8')))
        self.assertTrue(r['full_total_momentum_Fock_wavepacket_constructed'])
        self.assertTrue(r['imported_photon_Lorentz_carrier_intertwiner_constructed'])
        self.assertEqual(r['mass_boost_jacobian_checks'],12)
        self.assertEqual(r['boosted_null_output_configurations'],24)
        self.assertEqual(r['helicity_transport_cases'],6)
        self.assertEqual(r['nontrivial_helicity_phase_example'],'(2303-96*i)/2305')
        self.assertEqual(r['Wigner_rotation_cocycle_cases'],4)
        self.assertFalse(r['native_source_Lorentz_intertwiner_constructed'])
        self.assertFalse(r['rest_escape_lab_translation_intertwiner_constructed'])
        self.assertFalse(r['branching_ratio_derived'])

    def test_retention_and_physical_promotion_guards(self):
        c=json.loads(packet.CONTRACT.read_text(encoding='utf-8'));packet.validate_contract(c)
        for key,value in c.items():
            if isinstance(value,bool):
                bad=copy.deepcopy(c);bad[key]=not value
                with self.assertRaises(AssertionError):packet.validate_contract(bad)


if __name__=='__main__':unittest.main()
