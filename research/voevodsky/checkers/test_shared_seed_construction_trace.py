"""Tamper, replay and endpoint controls for the fixed record-instruction trace."""
import copy,json,unittest
from check_shared_seed_construction_trace import ROOT,SPEC,TRACE,RESULT,replay,validate_packet,compile_trace,digest_value

class TraceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spec=json.loads((ROOT/SPEC).read_text())
        cls.packet=json.loads((ROOT/TRACE).read_text())
        cls.result=json.loads((ROOT/RESULT).read_text())
    def test_complete_replay_and_endpoints(self):
        end=validate_packet(self.packet)
        self.assertEqual(end['dense_arrows'],7128);self.assertEqual(end['geometric_directed_edges'],84)
        self.assertEqual(len(self.packet['events']),11371)
        self.assertEqual(sum(self.result['instruction_counts'].values()),11371)
    def test_changed_coefficient_rejected(self):
        p=copy.deepcopy(self.packet)
        event=next(e for e in p['events'] if e['op']=='feedback_entry')
        event['result']=['0','0']
        with self.assertRaises(AssertionError):replay(self.spec,p['events'])
    def test_valid_prefix_is_not_full_construction(self):
        p=copy.deepcopy(self.packet);p['events']=p['events'][:-1];p['final_configuration_hash']=p['events'][-1]['hash']
        replay(self.spec,p['events'])  # Deliberately a valid prefix.
        with self.assertRaises(AssertionError):validate_packet(p)
    def test_future_dependency_rejected(self):
        p=copy.deepcopy(self.packet);event=next(e for e in p['events'] if e['op']=='product')
        event['inputs'][0]=event['index']
        with self.assertRaises(AssertionError):replay(self.spec,p['events'])
    def test_seed_exchange_is_required(self):
        spec=copy.deepcopy(self.spec);spec['seed_arrows'].remove('BA')
        with self.assertRaises(AssertionError):compile_trace(spec)
    def test_zero_results_and_duplicate_products_retained(self):
        self.assertEqual(self.result['retained_dense_zero_results'],3456)
        self.assertEqual(self.result['retained_comparison_zero_results'],432)
        products=[e for e in self.packet['events'] if e['op']=='product']
        self.assertEqual(len(products),72)
        self.assertLess(len({tuple(e['result']) for e in products}),len(products))
        self.assertEqual(self.result['initial_seed_arrows'],6)
        self.assertFalse(self.result['physical_mass_count_admitted'])
    def test_rehashed_wrong_result_still_rejected(self):
        events=copy.deepcopy(self.packet['events']);events[0]['result'][0]='2'
        head=digest_value(self.spec)
        for e in events:
            e['previous']=head;e.pop('hash');head=digest_value(e);e['hash']=head
        with self.assertRaises(AssertionError):replay(self.spec,events)

if __name__=='__main__':unittest.main()
