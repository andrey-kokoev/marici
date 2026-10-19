import copy
import json
import unittest
from fractions import Fraction as Q
import check_incoming_dirac_packet as incoming


class IncomingDiracPacketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=incoming.build()

    def test_fresh_receipt(self):
        self.assertEqual(self.result,json.loads(incoming.RESULT.read_text(encoding='utf-8')))
        self.assertEqual(self.result['CM_spinor_current_cases'],9)
        self.assertEqual(self.result['boosted_current_cases'],27)
        self.assertEqual(self.result['individual_massive_Wigner_rotation_cases'],54)

    def test_scope(self):
        self.assertTrue(self.result['normalizable_incoming_Dirac_pair_packet_constructed'])
        self.assertTrue(self.result['pseudoscalar_vector_currents_of_declared_packet_constructed'])
        for key in ('physical_incident_preparation_selected','outgoing_Born_map_constructed','unitary_interacting_QFT_constructed',
                    'branching_ratio_derived','physical_outcomes_admitted'):
            self.assertFalse(self.result[key])
        self.assertEqual(len(self.result['hostile_controls_refused']),7)

    def test_guards(self):
        c=json.loads(incoming.CONTRACT.read_text(encoding='utf-8'))
        for key,value in c.items():
            if isinstance(value,bool):
                bad=copy.deepcopy(c);bad[key]=not value
                with self.subTest(key=key),self.assertRaises(AssertionError):incoming.validate_contract(bad)

    def test_mass_threshold(self):
        self.assertEqual(incoming.threshold_beta_squared(Q(10,3)),Q(16,25))
        for mass in (Q(-1),Q(0),Q(1),Q(2)):
            with self.subTest(M=mass),self.assertRaises(AssertionError):incoming.threshold_beta_squared(mass)


if __name__=='__main__':unittest.main()
