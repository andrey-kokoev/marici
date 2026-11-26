"""Receipt coverage for the final codegree-three root-pair case. Not an independent enumeration or verification of the smaller catalogues."""
from pathlib import Path
import json,collections,hashlib
P=Path(__file__).resolve().parents[1]/'results'
def load(path):return json.loads(path.read_text())
src=load(P/'ramsey_38_common49.json');hs=set(src['triples']);assert len(hs)==23548
manifest=set(load(P/'ramsey_38_degree4_children49.json'));assert len(manifest)==src['total']==60244 and hs<=manifest
covered=set();strata={}
for e in range(25,34):
 expected={h for h in hs if int(h,16).bit_count()==e}
 if e==33:
  rows=load(P/'ramsey_38_pair33_side.json');assert all(n==0 and not paired for n,paired in rows.values());entry=dict(cores=len(rows),reason='no legal side')
 else:
  rows={}
  for f in (P/f'ramsey_38_final_join_{e}_parts').glob('*.json'):
   sub=load(f);assert not rows.keys()&sub.keys();rows.update(sub)
  assert all(len(v)==7 and v[-1]==0 for v in rows.values());entry=dict(cores=len(rows),counts=[sum(v[k]>0 for v in rows.values()) for k in range(7)],totals=[sum(v[k] for v in rows.values()) for k in range(7)]);assert entry==load(P/f'ramsey_38_final_join_{e}.json')
 assert set(rows)==expected and not covered&expected;covered.update(expected);entry['key_digest']=hashlib.sha256('\n'.join(sorted(expected)).encode()).hexdigest();strata[e]=entry
assert covered==hs;out=dict(candidates=src['total'],passed_inner_codegree=src['codegree_pass'],passed_common_triple=len(hs),strata=strata);(P/'ramsey_38_final_coverage.json').write_text(json.dumps(out)+'\n');print('all',len(covered),'new regular presentations',sum(strata[e]['totals'][4] for e in range(25,29)))
