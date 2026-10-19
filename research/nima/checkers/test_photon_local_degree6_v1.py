import json
import unittest

import check_photon_local_degree6_v1 as t


class LocalDegreeSixTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_ranks_and_witness(self):
        self.assertEqual(self.r['full_coefficient_rank'],18)
        self.assertEqual(self.r['forward_rank'],8)
        self.assertEqual(len(self.r['full_rank_witness']),18)

    def test_ten_invisible_directions_retained(self):
        self.assertEqual(self.r['kernel_coordinate_names'],['f3','h3','g4prime','g5prime','f5','h5','g6prime','g6doubleprime','f6prime','h6'])
        self.assertEqual(len(self.r['forward_kernel']),10)

    def test_h6_not_inferred_zero(self):
        self.assertEqual(self.r['h6_control'],'20736/390625')
        self.assertEqual(self.r['drop_h6_full_rank'],17)

    def test_chosen_readout_requires_second_angle(self):self.assertEqual(self.r['one_angle_Phi125_witness_rank'],17)

    def test_all_helicities_and_gauge_patches(self):
        self.assertEqual(self.r['counts']['helicity'],64)
        self.assertEqual(self.r['counts']['gauge_patch'],64)
        self.assertEqual(self.r['counts']['Bose'],72)

    def test_component_Ward(self):self.assertEqual(self.r['new_component_Ward_constraints'],1536)

    def test_unearned_promotions_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('generic_degree6_log_window_tensor_constructed','off_shell_operator_basis_exhausted',
                    'finite_physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
            with self.assertRaises(AssertionError,msg=key):t.validate({**c,key:True})


if __name__=='__main__':unittest.main()
