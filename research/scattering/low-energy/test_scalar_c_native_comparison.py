"""Controls for the typed two-point comparison, including free direct-block fits."""
import copy
import json
import unittest
from fractions import Fraction as Q
import check_scalar_c_native_comparison as compare


class ScalarNativeComparisonTests(unittest.TestCase):
    def test_shifted_gram_floor(self):
        D=compare.scale(compare.F(Q(1,2)),compare.eye(3));h=[compare.F(1),compare.F(2),compare.F(3)]
        self.assertEqual(compare.certify(D,h,Q(1,4)),[3,0,0])
        with self.assertRaises(AssertionError):compare.certify(D,h,Q(1))

    def test_contract_scope_promotions_refused(self):
        c=json.loads(compare.CONTRACT.read_text(encoding='utf-8'))
        for change in ('third-hidden','physical-result','inflate-floor'):
            bad=copy.deepcopy(c)
            if change=='third-hidden':bad['candidate_class']['hidden_dimension_maximum']=3
            elif change=='physical-result':bad['physical_outcomes_admitted']=True
            else:bad['endpoint_error_floor']='1'
            with self.assertRaises(AssertionError):compare.validate_contract(bad)

    def test_native_witness_and_single_point_caveat(self):
        r=compare.build()
        self.assertEqual(r['hidden_coupling_rank'],3)
        self.assertEqual(r['shifted_Gram_inertia'],[3,0,0])
        self.assertEqual(r['endpoint_error_floor'],'1/8192')
        self.assertTrue(r['constant_visible_block_freely_refitted'])
        self.assertTrue(r['one_point_constant_fit_succeeds'])
        self.assertEqual(len(r['literal_Schur_controls']),4)
        for key in ('physical_band_error_bound_proved','all_reductions_excluded',
                    'historical_ancestor_freshness_claimed','new_live_proposition_admitted',
                    'C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
            self.assertFalse(r[key],key)


if __name__=='__main__':unittest.main()
