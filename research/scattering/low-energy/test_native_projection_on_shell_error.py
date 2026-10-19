"""Exact support, rational packet envelopes and comparison-scope controls."""
import copy
from fractions import Fraction as Q
import json
import unittest
import check_native_projection_on_shell_error as shell


class OnShellErrorTests(unittest.TestCase):
    def test_packet_bounds(self):
        self.assertEqual(shell.packet_error_squared_bound(Q(1,64),Q(1)),Q(1,144))
        self.assertEqual(shell.packet_error_squared_bound(Q(1,64),Q(1,2)),Q(1,288))
        self.assertEqual(shell.effect_error_squared_bound(Q(1,64),Q(1)),Q(1,36))
        self.assertEqual(shell.packet_error_squared_bound(Q(1,256),Q(1)),Q(1,576))
        self.assertEqual(shell.packet_error_squared_bound(Q(1,64),Q(0)),0)

    def test_window_and_normalization_guards(self):
        for epsilon,weight in ((Q(0),Q(1)),(Q(-1,64),Q(1)),(Q(1,32),Q(1)),
                               (Q(1,64),Q(-1)),(Q(1,64),Q(2))):
            with self.assertRaises(AssertionError):shell.packet_error_squared_bound(epsilon,weight)

    def test_contract_scope(self):
        c=json.loads(shell.CONTRACT.read_text(encoding='utf-8'))
        for key in ('full_band_small_error_claimed','physical_outcomes_admitted','C12_protocol_renewed'):
            bad=copy.deepcopy(c);bad[key]=True
            with self.assertRaises(AssertionError):shell.validate_contract(bad)
        bad=copy.deepcopy(c);bad['energy_window_upper']='1/32'
        with self.assertRaises(AssertionError):shell.validate_contract(bad)

    def test_actual_sector_and_envelope(self):
        r=shell.build();gap=shell.F(*r['zero_energy_compliance_gap']);D=shell.F(*r['compliance_error_envelope'])
        self.assertTrue(gap.positive());self.assertTrue((shell.F(Q(1,3))-D).positive())
        self.assertEqual(r['native_antisymmetric']['dimension'],6)
        self.assertEqual(r['reduced_antisymmetric']['dimension'],3)
        self.assertEqual(r['full_visible_cyclic_dimensions'],[11,8])
        self.assertTrue(r['pointwise_sqrt_energy_order_sharp_in_antisymmetric_channel'])
        self.assertEqual(r['window_endpoint_packet_norm_error_per_alpha_in'],'1/12')
        for key in ('full_band_small_error_claimed','physical_energy_or_detector_binding_claimed',
                    'historical_ancestor_freshness_claimed','new_live_proposition_admitted','C12_protocol_renewed',
                    'high_energy_protocol_executed','physical_outcomes_admitted'):
            self.assertFalse(r[key],key)


if __name__=='__main__':unittest.main()
