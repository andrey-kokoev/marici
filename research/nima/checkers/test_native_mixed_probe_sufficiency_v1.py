import json
import unittest
from copy import deepcopy

import check_native_mixed_probe_sufficiency_v1 as t


class MixedProbeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)
    def test_rejection_is_scoped(self):
        self.assertEqual(self.r['candidate_verdict'],'rejected')
        self.assertFalse(self.r['protocol_contains_all_native_operations'])
        self.assertFalse(self.r['parent_gate_resolved'])
        net=json.loads((t.HOME/'contracts/native-mixed-probe-sufficiency-conjecture-net.v1.json').read_text(encoding='utf-8'))
        self.assertEqual((net['conjectures'][0]['status'],net['conjectures'][0]['verdict']),('resolved','rejected'))
        self.assertFalse(net['parent_modified'])
    def test_full_word_space_ceiling(self):
        self.assertEqual(self.r['all_gain_and_common_witness_rank'],57)
        self.assertEqual(self.r['blind_dimension'],80)
        self.assertLessEqual(self.r['all_gain_and_common_witness_rank'],67)
        self.assertEqual(self.r['blind_dimension'],137-self.r['all_gain_and_common_witness_rank'])
        self.assertEqual(self.r['common_witness_controls'],6)
    def test_no_reset_records(self):
        self.assertEqual(self.r['no_reset_three_record_rank'],self.r['all_gain_and_common_witness_rank'])
    def test_explicit_falsifier(self):
        self.assertTrue(self.r['blind_coefficient_chain'])
        self.assertTrue(any(v!='0' for row in self.r['target_probe_response'] for v in row))
        source=t.joint.source_interfaces();b=source['boundary_source']
        x,y,s,u=[b['I']]*11,[b['I']]*11,[b['I']]*4,[b['I']]*4
        kind,i,j=source['slots'][self.r['target_probe_slot']]
        left,right=(x,y) if kind=='arrow' else (s,u)
        left[i]=b['add'](b['I'],b['H']);right[j]=b['add'](b['I'],b['K'])
        chain={int(k):t.F(v) for k,v in self.r['blind_coefficient_chain'].items()}
        actual=b['evaluate'](chain,b['residuals'](x,y,s,u,source['reference']))
        self.assertEqual([[str(v) for v in row] for row in actual],self.r['target_probe_response'])
    def test_no_physical_promotion(self):
        self.assertFalse(self.r['independent_leg_target_preparations_are_licensed_controls'])
        self.assertFalse(self.r['physical_actuation_or_readout_authorized'])
        self.assertFalse(self.r['formal_outcome_admitted'])
    def test_protocol_substitution_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        changed=deepcopy(c);changed['allowed_operations'].append('independent leg writes')
        with self.assertRaises(AssertionError):t.validate(changed)
    def test_target_reader_repair_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'));c['records']='identity reader of all137 coefficients'
        with self.assertRaises(AssertionError):t.validate(c)


if __name__=='__main__':unittest.main()
