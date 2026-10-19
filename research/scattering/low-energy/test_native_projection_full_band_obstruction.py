"""Phase identity, pole/sign guards and exact fixed-projection witness."""
import copy
from fractions import Fraction as Q
import json
import unittest
import check_native_projection_full_band_obstruction as obstruction


class FullBandObstructionTests(unittest.TestCase):
    def test_symbolic_phase_identity(self):
        self.assertTrue(obstruction.prove_phase_identity())
        with self.assertRaises(AssertionError):obstruction.prove_phase_identity(drop_cross_term=True)

    def test_pole_and_sign_guards(self):
        parent=json.loads(obstruction.preceding.RESULT.read_text(encoding='utf-8'))
        m=obstruction.model(parent['native_antisymmetric'])
        self.assertEqual(obstruction.certify_no_poles(m,Q(39,100),Q(2,5)),[5,1,0])
        with self.assertRaises(AssertionError):obstruction.certify_no_poles(m,Q(1,64),Q(2,5))
        with self.assertRaises(AssertionError):obstruction.certify_sign_change(obstruction.F(1),obstruction.F(1))

    def test_scope_guards(self):
        c=json.loads(obstruction.CONTRACT.read_text(encoding='utf-8'))
        for key in ('all_reductions_excluded','physical_outcomes_admitted','C12_protocol_renewed',
                    'exact_perfect_normalizable_packet_discrimination_claimed'):
            bad=copy.deepcopy(c);bad[key]=True
            with self.assertRaises(AssertionError):obstruction.validate_contract(bad)

    def test_actual_exact_obstruction(self):
        r=obstruction.build();w=r['rational_witness']
        self.assertEqual(r['maximal_common_frame_full_band_scattering_norm_error'],2)
        self.assertEqual(r['common_free_packet_scattering_operator_norm_error'],2)
        self.assertEqual([e['W_sign'] for e in r['endpoints']],[1,-1])
        d2=obstruction.F(*w['scattering_norm_error_squared'])
        self.assertTrue((d2-obstruction.F(Q(199,100)**2)).positive())
        self.assertTrue(r['symmetric_sector_still_exact'])
        self.assertTrue(r['preceding_low_window_bound_still_valid'])
        for key in ('all_reductions_excluded','numerical_search_used_as_proof',
                    'physical_preparation_or_detector_binding_claimed','historical_ancestor_freshness_claimed',
                    'new_live_proposition_admitted','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
            self.assertFalse(r[key],key)


if __name__=='__main__':unittest.main()
