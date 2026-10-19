import copy
import json
import unittest
from fractions import Fraction as Q
import check_degree6_photon_ir_logs as six


class Degree6PhotonIRLogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=six.build()

    def test_receipt(self):
        self.assertEqual(self.result,json.loads(six.RESULT.read_text(encoding='utf-8')))
        for key,value in (('physical_right_cut_coefficient_checks',96),('log_and_counterterm_permutation_checks',768),
                          ('Ward_tensor_checks',16),('Lorentz_tensor_checks',4),('combined_finite_scale_cancellation_checks',576),
                          ('formal_wave_coefficient_extraction_checks',63),('angular_coefficient_extraction_checks',7),
                          ('complete_wave_square_positivity_checks',189),('scalar_and_mixed_projection_checks',10)):
            self.assertEqual(self.result[key],value)

    def test_complete_degree6_and_cancellation_loci(self):
        row=six.scalar_logs('c0_r4')
        self.assertEqual(row['minus']['right_cut'],Q(2,5))
        self.assertEqual(row['plus']['right_cut'],Q(1,60))
        self.assertEqual(row['minus']['real_log'],Q(97,210))
        self.assertEqual(row['plus']['real_log'],Q(-13,420))
        self.assertEqual(six.cancellation_data(),(Q(-1115,6208),Q(35,416),Q(-473,125440)))
        self.assertEqual(six.scalar_logs('c1_squared'),six.logs.scalar_logs(3))
        with self.assertRaises(AssertionError):six.sector_polynomials('c0_squared')

    def test_running_and_finite_freedom(self):
        self.assertEqual(six.running_vector('c0_r4'),[Q(23,60),Q(-23,40),Q(8,35),Q(-3,35),Q(1,28)])
        self.assertEqual(self.result['running_rank'],2)
        self.assertEqual(self.result['running_rank_minor'],'-1/288')
        self.assertEqual(six.invariant_covectors()[0],[Q(3,2),Q(1),Q(),Q(),Q()])
        self.assertEqual(self.result['local_basis_dimension'],5)
        self.assertEqual(self.result['operator_dimension'],16)
        for key in ('r4_spectral_control_source_licensed','finite_matching_selected_by_running',
                    'RG_invariant_values_source_selected','both_scalar_degree6_logs_cancel_for_nonzero_X_Y'):
            self.assertFalse(self.result[key])
        self.assertEqual(len(self.result['hostile_controls_refused']),8)

    def test_contract_guards(self):
        c=json.loads(six.CONTRACT.read_text(encoding='utf-8'))
        for key,value in c.items():
            if isinstance(value,bool):
                bad=copy.deepcopy(c);bad[key]=not value
                with self.subTest(key=key),self.assertRaises(AssertionError):six.validate_contract(bad)
        bad=copy.deepcopy(c);bad['r4']='source_selected_1/(6*pi)'
        with self.assertRaises(AssertionError):six.validate_contract(bad)


if __name__=='__main__':unittest.main()
