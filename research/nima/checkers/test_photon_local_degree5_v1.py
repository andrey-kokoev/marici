from fractions import Fraction as Q
import json
import unittest

import check_photon_local_degree5_v1 as t


class LocalDegreeFiveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_full_and_forward_ranks(self):
        self.assertEqual(self.r['full_coefficient_rank'],12)
        self.assertEqual(self.r['forward_rank'],6)
        self.assertEqual(len(t.base.reduced_rows([[Q(x) for x in r] for r in self.r['full_rank_witness']])[1]),12)

    def test_six_exact_kernel_directions(self):
        self.assertEqual(self.r['kernel_coordinate_names'],['f3','h3','g4prime','g5prime','f5','h5'])
        self.assertEqual(len(t.base.nullspace(t.forward_map())),6)

    def test_kernel_not_zero_off_forward(self):
        self.assertEqual(len(t.base.reduced_rows([[Q(x) for x in r] for r in self.r['invisible_rank_six_witness']])[1]),6)

    def test_single_minus_h5_cannot_be_erased(self):
        self.assertEqual(self.r['h5_control'],'138528/390625')
        self.assertEqual(self.r['drop_h5_full_rank'],11)
        self.assertTrue(all(r[11]==0 for r in t.forward_map()))

    def test_all_helicities_and_component_Ward(self):
        self.assertEqual(self.r['counts']['helicity'],64)
        self.assertEqual(self.r['counts']['Bose'],72)
        self.assertEqual(self.r['new_component_Ward_constraints'],1024)

    def test_old_basis_and_forward_rows_preserved(self):
        a,b,q=t.base.cm();e=t.base.polarizations(a,b,t.base.PHI[0])
        self.assertEqual(t.covariants(q,e)[:8],t.base.covariants(q,e))
        self.assertEqual(tuple(tuple(r[:8]) for r in t.forward_map()[:5]),t.base.forward_map())

    def test_scope_promotions_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for k in ('degree_five_log_window_tensor_constructed','general_dim10_Born_loop_inventory_derived',
                  'finite_physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
            with self.assertRaises(AssertionError,msg=k):t.validate({**c,k:True})


if __name__=='__main__':unittest.main()
