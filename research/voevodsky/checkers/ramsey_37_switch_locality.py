"""Canonical one-hop red-edge neighborhood: each exclusive neighbor side is red-independent, so the cross matrix up to row/column permutations and transpose is complete. Compare classes on signed change of the optimal extension cost. Prefer same-record, same-newSix hostiles where available."""
from pathlib import Path
from itertools import permutations,combinations
from collections import defaultdict,Counter
import json
H=Path(__file__).resolve().parents[1];D=H/'results';cat=(H.parent/'chatgpt/ramsey/pauli-realization-catalogues/r37_22.g6').read_text().splitlines();src=json.loads((D/'ramsey_37_switch_extension_catalogue.json').read_text())['report'];rows=[]
for g,rec in zip(cat,src):
 b=''.join(f'{ord(c)-63:06b}' for c in g[1:]);N=[set() for _ in range(22)]
 for j in range(22):
    for i in range(j):
        if b[j*(j-1)//2+i]=='1':N[i].add(j);N[j].add(i)
 def code(A,B):return min((len(A),len(B),tuple(sorted(sum(1<<k for k,x in enumerate(p) if x in N[y]) for y in B))) for p in permutations(A))
 for e in rec['deletions']:
    u,v=e['edge'];A=N[u]-{v};B=N[v]-{u};assert not A&B;key=min(code(A,B),code(B,A));rows.append(dict(local=key,record=rec['record'],**e))
sgn=lambda r:(r['after']>r['before'])-(r['after']<r['before']);groups=defaultdict(list)
for r in rows:groups[r['local']].append(r)
h=[(a,b) for rs in groups.values() for a,b in combinations(rs,2) if sgn(a)*sgn(b)==-1];h.sort(key=lambda ab:(ab[0]['record']!=ab[1]['record'],ab[0]['before']!=ab[1]['before'],ab[0]['newSix']!=ab[1]['newSix']));ex=h[0] if h else None
both=[(a,b) for a,b in h if a['newSix']==b['newSix'] and a['before']==b['before']];o=dict(local_types=len(groups),mixed_sign_types=sum(len(set(map(sgn,rs)))>1 for rs in groups.values()),opposite_sign_types=sum({-1,1}<=set(map(sgn,rs)) for rs in groups.values()),same_record_example=ex,same_baseline_and_sixes_example=next(iter(both),None));print(o);(D/'ramsey_37_switch_locality.json').write_text(json.dumps(o,indent=2)+'\n')
