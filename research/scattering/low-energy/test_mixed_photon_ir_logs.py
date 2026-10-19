import copy
import json
import unittest
from fractions import Fraction as Q
import check_mixed_photon_ir_logs as mixed


class MixedPhotonIRLogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=mixed.build()

    def test_receipt(self):
        self.assertEqual(self.result,json.loads(mixed.RESULT.read_text(encoding='utf-8')))
        for key,value in (('physical_right_cut_coefficient_checks',48),('log_and_counterterm_permutation_checks',384),
                          ('Ward_log_and_counterterm_checks',8),('Lorentz_log_and_counterterm_checks',2),
                          ('finite_scale_tensor_cancellation_checks',144),('physical_basis_normalization_checks',6),
                          ('Bose_projection_checks',5),('two_term_cut_polynomial_square_checks',18),
                          ('Bose_wave_square_positivity_checks',108)):
            self.assertEqual(self.result[key],value)

    def test_signed_interference_and_odd_crossing(self):
        rows=mixed.scalar_logs()
        self.assertEqual(rows['plus']['right_cut'],Q(-1,48))
        self.assertEqual(rows['minus']['crossed_log'],Q(-5,144))
        self.assertEqual(rows['plus']['crossed_log'],Q(1,18))
        self.assertEqual([rows[n]['real_log'] for n in ('minus','plus')],[Q(31,144),Q(5,144)])
        self.assertEqual([rows[n]['angular_constant'] for n in ('minus','plus')],[Q(17,3456),Q(-35,3456)])
        D,o,M,_=mixed.cut_polynomials()
        self.assertEqual((D,o,M),([Q(37,320),Q(),Q(-1,320)],Q(-13,96),[Q(),Q(),Q(-1,48)]))

    def test_running_and_scope(self):
        self.assertEqual(mixed.running_vector(),[Q(65,96),Q(2,15),Q(-1,20)])
        self.assertEqual(self.result['beta_coefficient_of_c0_c1_over_pi'],['-65/96','-2/15','1/20'])
        self.assertEqual(self.result['operator_dimension'],14)
        self.assertEqual(self.result['basis_dimension'],3)
        for key in ('interference_cut_coefficient_must_be_positive','finite_matching_selected_by_running',
                    'full_degree_6_cut_constructed','full_EFT_anomalous_dimension_matrix_constructed'):
            self.assertFalse(self.result[key])
        self.assertEqual(len(self.result['hostile_controls_refused']),8)

    def test_contract_guards(self):
        c=json.loads(mixed.CONTRACT.read_text(encoding='utf-8'))
        for key,value in c.items():
            if isinstance(value,bool):
                bad=copy.deepcopy(c);bad[key]=not value
                with self.subTest(key=key),self.assertRaises(AssertionError):mixed.validate_contract(bad)
        bad=copy.deepcopy(c);bad['normalization']='ImB_23=c0*c1*A2*A3/8'
        with self.assertRaises(AssertionError):mixed.validate_contract(bad)


if __name__=='__main__':unittest.main()
