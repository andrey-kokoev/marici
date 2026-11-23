"""Test both path isomorphisms as fixed site bindings, not as state encodings. Transport the named Ramsey generators to the four seed sites; first require preservation of the unordered C/M partition. Keep cut motion separate from kind mixing."""
import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';load=lambda k:json.loads((D/(k+'.json')).read_text());p=load('ramsey_probe_cycle_cut');seed=load('four_role_static_roundtrip')['rank_orders'][0];G={'A':(1,0,3,2,4,5,6),'B':(1,0,2,3,5,4,6),'C':(0,1,4,5,2,3,6)};rows=[]
for path in p['remaining_orders']:
 bind=dict(zip(path,seed));moves={}
 for k,g in G.items():
  action={v:bind[g[i]] for i,v in bind.items()};moves[k]=dict(moved={s:t for s,t in action.items() if s!=t},kind_partition_preserved=all((s[0]==t[0])==(action[s][0]==action[t][0]) for s in seed for t in seed),cut_image=sorted([g[3],g[4]]))
 assert [k for k,v in moves.items() if v['kind_partition_preserved']]==['C'];rows.append(dict(binding=bind,moves=moves))
print(rows);(D/'ramsey_probe_path_seed_actions.json').write_text(json.dumps(rows,indent=2)+'\n')
