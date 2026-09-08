import copy,json,unittest
from pathlib import Path
from rh_net_state_compiler import compile_rh_net_state
from rh_net_semantic_views import compile_semantic_views
ROOT=Path(__file__).resolve().parents[3]
class TestSemanticViews(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.c=json.loads((ROOT/'research/aspect/contracts/theta-rh-interaction-net-state.v2.json').read_text())
 def test_full_contract(self):self.assertTrue(compile_rh_net_state(self.c)['passed'])
 def test_seed_invariance(self):
  a=compile_semantic_views(self.c);b=copy.deepcopy(self.c);b['display_seed']=92831;z=compile_semantic_views(b)
  self.assertEqual([(n['id'],n['semantic_plane']) for n in a['span']['nodes']],[(n['id'],n['semantic_plane']) for n in z['span']['nodes']]);self.assertEqual(a['span']['fibers'],z['span']['fibers'])
 def test_equivalence_removal(self):
  a=copy.deepcopy(self.c);a['visualization_contract']['admitted_equivalences']=[['theta_koszul_divisor_complex','centered_trace_class_seam_return']];over=compile_semantic_views(a);b=copy.deepcopy(a);b['visualization_contract']['admitted_equivalences']=[];z=compile_semantic_views(b)
  q='centered_incidence_range_closure_typing';self.assertEqual(over['span']['fibers'][q]['presentation_classification'],'overpresentation');self.assertEqual(z['span']['fibers'][q]['presentation_classification'],'unresolved_comparison')
 def test_detecting_requirement_removal_does_not_merge(self):
  a=compile_semantic_views(self.c);b=copy.deepcopy(self.c);b['visualization_contract']['requirement_edges']=[e for e in b['visualization_contract']['requirement_edges'] if e['relation']!='detects'];z=compile_semantic_views(b)
  self.assertEqual({n['id'] for n in a['span']['nodes']},{n['id'] for n in z['span']['nodes']});self.assertLess(len(z['requirement_dual']['edges']),len(a['requirement_dual']['edges']))
 def test_same_payload_and_unclassified(self):
  a=compile_semantic_views(self.c);self.assertTrue(a['views_from_same_payload']);self.assertTrue(a['unclassified']);self.assertTrue(all(n['semantic_depth']==760 for n in a['span']['nodes'] if n['id'] in a['unclassified']))
 def test_witness_backed_fibers(self):
  a=compile_semantic_views(self.c);self.assertTrue(all(f['witnesses'] for f in a['span']['fibers'].values() if f['realization_fiber'] or f['presentation_fiber']))
 def test_simulation_cannot_mutate_contract(self):
  before=json.dumps(self.c,sort_keys=True);work=copy.deepcopy(compile_semantic_views(self.c));work['span']['nodes'][0]['status']='simulated';self.assertEqual(before,json.dumps(self.c,sort_keys=True))
if __name__=='__main__':unittest.main()
