"""All two-site deletions of one labelled 22-vertex witness. Enumerate independent core attachment profiles meeting every independent six, and compatible unordered profile pairs including copies. No symmetry or distinguished vertex imposed."""
from pathlib import Path
from itertools import combinations,combinations_with_replacement
from collections import Counter
import json
D=Path(__file__).resolve().parents[1]/'results';g=json.loads((D/'ramsey_37_dual_stars.json').read_text());N=[0]*22
for u,v in g['red_edges']:N[u]|=1<<v;N[v]|=1<<u
inds=[0]
for u in range(22):inds += [s | (1<<u) for s in inds if not s&N[u]]
assert max(s.bit_count() for s in inds)==6
records=[];full=(1<<22)-1
for u,v in combinations(range(22),2):
    deleted=(1<<u)|(1<<v);core=[s for s in inds if not s&deleted];sixes=[s for s in core if s.bit_count()==6];fives=[s for s in core if s.bit_count()==5];profiles=[s for s in core if all(s&k for k in sixes)];unhit=[sum(1<<i for i,k in enumerate(fives) if not p&k) for p in profiles];common=full
    for p in profiles:common&=p
    completions=sum(int(not (a&b))+int(not(unhit[i]&unhit[j])) for (i,a),(j,b) in combinations_with_replacement(enumerate(profiles),2));original=[N[i]&~deleted for i in (u,v)];assert all(s in profiles for s in original) and completions>=1
    records.append(dict(pair=[u,v],edge='red' if N[u]>>v&1 else 'blue',profiles=len(profiles),completions=completions,forced=[i for i in range(22) if common>>i&1]))
focus=next(r for r in records if r['pair']==[17,19]);h=Counter((r['edge'],r['profiles']==2,r['completions']==1) for r in records);print(focus,h,Counter((r['edge'],len(r['forced'])) for r in records if r['profiles']==2 and r['completions']==1));(D/'ramsey_37_pair_regrowth_controls.json').write_text(json.dumps(records,indent=2)+'\n')
