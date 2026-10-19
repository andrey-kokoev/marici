"""Metric projection controls and source-specific preservation checks."""
import copy
import json
import unittest
import check_ground_preserving_native_projection as project


class NativeProjectionTests(unittest.TestCase):
    def test_canonical_basis(self):
        F=project.F;s=project.Span(3)
        s.add([F(1),F(2),F(0)],{'seed':0});s.add([F(0),F(1),F(3)],{'seed':1})
        rows=project.canonical_rows(s)
        self.assertEqual(rows,[[F(1),F(0),F(-6)],[F(0),F(1),F(3)]])
        self.assertEqual(project.rank(rows),2)

    def test_weighted_energy_error(self):
        F=project.F
        HQ=[[F(1),F(),F()],[F(),F(2),F()],[F(),F(),F(3)]]
        A=[[F(2),F(),F()],[F(),F(3),F()],[F(),F(),F(4)]]
        B=[[F(1)],[F(1)],[F()]];X=project.mm(project.invert(A),B)
        Xr=[[F(1)/F(2)],[F()],[F()]];err=project.difference(X,Xr)
        delta=project.mm(project.mm(project.transpose(B),HQ),err)
        energy=project.mm(project.mm(project.mm(project.transpose(err),HQ),A),err)
        project.require_equal(delta,energy)
        self.assertEqual(delta,[[F(2)/F(3)]])

    def test_contract_scope(self):
        c=json.loads(project.CONTRACT.read_text(encoding='utf-8'))
        for name in ('partial-visible','physical-admission'):
            bad=copy.deepcopy(c)
            if name=='partial-visible':bad['visible_coordinates']=[0]
            else:bad['physical_outcomes_admitted']=True
            with self.assertRaises(AssertionError):project.validate_contract(bad)

    def test_native_endpoint_and_ground_projection(self):
        r=project.build()
        self.assertEqual((r['full_core_dimension'],r['hidden_dimension']),(8,5))
        self.assertEqual(r['ground_added_hidden_dimension'],0)
        self.assertEqual(r['weighted_core_inertia'],[7,0,1])
        self.assertEqual(r['minimal_hidden_dimension_in_native_orthogonal_projection_class'],5)
        self.assertTrue(r['ground_visible_direction_and_norm_preserved'])
        self.assertEqual(r['coefficient_limit_norm_gap'],0)
        self.assertEqual(r['symmetric_core_sector_dimension'],5)
        self.assertGreater(r['global_intertwining_residual_rank'],0)
        for e in r['evaluations']:
            if e['z'] in ('-1','-2'):self.assertTrue(e['full_visible_resolvent_equal'])
        for key in ('global_minimum_ground_preserving_hidden_dimension_claimed','all_energy_full_response_identical',
                    'explicit_positive_band_packet_error_bound_proved','source_operation_licensing_claimed',
                    'C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
            self.assertFalse(r[key],key)


if __name__=='__main__':unittest.main()
