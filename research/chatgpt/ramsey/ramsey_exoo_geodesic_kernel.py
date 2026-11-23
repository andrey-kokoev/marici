"""Check support-bridge theorem hypotheses on Exoo's seed and deletion controls. For 35 compare explicit CNF with all 2^14 assignments and archived 198 words."""
from exoo39_symbolic_relations import edges
from itertools import combinations
from pathlib import Path
from functools import reduce
from operator import and_,or_
from collections import deque,Counter
import json
D=Path(__file__).parent;E=edges();H=[sum(1<<j for j in range(39) if tuple(sorted((i,j))) in E) for i in range(39)];I=[0]
for i,h in enumerate(H):I.extend([s|1<<i for s in I if not s&h]);
nines=[s for s in I if s.bit_count()==9];ls=lambda s:[i for i in range(39) if s>>i&1];ind=lambda s:not any(H[i]&s for i in ls(s));minimal=lambda xs:sorted(s for s in xs if not any(t!=s and t&s==t for t in xs));ctl=[]
for r in range(39):
    T=[s for s in nines if not s>>r&1];B={s for s in I if not s>>r&1 and all(s&t for t in T)};fixed=reduce(and_,B);M=reduce(or_,B)^fixed;small=minimal(B);compat=all(ind(u|v) for u,v in combinations(small,2));row=dict(vertex=r,states=len(B),minimal=len(small),compatible=compat)
    if not compat:
        fail=None
        for a in B:
            for b in B:
                if a!=b and not any(a^(1<<v) in B for v in ls(a^b)):fail=[ls(a),ls(b)];break
            if fail:break
        row.update(isometric=not fail,stuck=fail)
    ctl.append(row)
    if r!=35:continue
    prev=json.loads((D/'ramsey_exoo_chart22_words.json').read_text());F=ls(M);assert F==prev['probes'] and {''.join(str(s>>i&1) for i in F) for s in B}==set(prev['words']);rows=minimal({t&M for t in T if not t&fixed});minima=[s^fixed for s in small];assert set(minima)=={1<<29,sum(1<<i for i in (1,15,33))};ok=0
    for z in range(1<<len(F)):
        s=sum(1<<v for j,v in enumerate(F) if z>>j&1);live=ind(s) and all(s&((1<<29)|(1<<i)) for i in (1,15,33));assert live==((s|fixed) in B);ok+=live
    result=dict(fixed=ls(fixed),variables=F,raw_minimal_rows=list(map(ls,rows)),minimal_supports=list(map(ls,minima)),conflicts=[e for e in sorted(E) if all(v in F for v in e)],cnf_states=ok)
result['deletion_controls']=ctl;print({k:v for k,v in result.items() if k!='deletion_controls'},Counter((a['compatible'],a.get('isometric',True)) for a in ctl),[r['vertex'] for r in ctl if not r['compatible']]);(D/'ramsey_exoo_geodesic_kernel.json').write_text(json.dumps(result,indent=2)+'\n')
