"""Regression controls for exact interpolation versus threshold preservation."""
import copy
import json
import unittest
import check_three_hidden_native_interpolant as fit


class ThreeHiddenInterpolantTests(unittest.TestCase):
    def test_inverse_affine_endpoints(self):
        F=fit.F
        N1=[[F(1)/F(i+2) if i==j else F() for j in range(3)] for i in range(3)]
        N2=[[F(1)/F(i+3) if i==j else F() for j in range(3)] for i in range(3)]
        R1,R2=fit.invert(N1),fit.invert(N2)
        G=fit.add(R2,fit.scale(F(-1),R1));T=fit.add(fit.scale(F(2),R1),fit.scale(F(-1),R2))
        fit.require_equal(fit.invert(fit.add(G,T)),N1)
        fit.require_equal(fit.invert(fit.add(fit.scale(F(2),G),T)),N2)
        with self.assertRaises(AssertionError):fit.require_equal(N1,N2)

    def test_contract_scope(self):
        c=json.loads(fit.CONTRACT.read_text(encoding='utf-8'))
        for name in ('hidden-dimension','high-energy-execution','physical-admission'):
            bad=copy.deepcopy(c)
            if name=='hidden-dimension':bad['hidden_dimension']=2
            elif name=='high-energy-execution':bad['high_energy_protocol_executed']=True
            else:bad['physical_outcomes_admitted']=True
            with self.assertRaises(AssertionError):fit.validate_contract(bad)

    def test_actual_positive_fit_and_failed_preservation(self):
        r=fit.build()
        self.assertEqual(r['minimal_hidden_dimension_for_exact_two_point_fit'],3)
        self.assertEqual(r['weighted_core_inertia'],[6,0,0])
        self.assertEqual(r['native_weighted_core_inertia'],[10,0,1])
        self.assertTrue(all(e['full_visible_resolvent_equal'] for e in r['exact_endpoint_fits']))
        self.assertEqual(r['coefficient_limit_norm_gap_in_same_frame'],2)
        self.assertEqual(r['conditional_chain_attachment_coefficient_limit'],'I3')
        for key in ('native_zero_mode_preserved','all_energy_response_identical','physical_probability_error_bound_proved',
                    'source_selected_model_claimed','new_live_proposition_admitted','C12_protocol_renewed',
                    'high_energy_protocol_executed','physical_outcomes_admitted'):
            self.assertFalse(r[key],key)


if __name__=='__main__':unittest.main()
