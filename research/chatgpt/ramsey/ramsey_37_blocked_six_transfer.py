"""Transfer the unchanged blocked-six + direct-edge veto: every catalogued 22-parent, delete its final site, root at zero; all pairs with opposite root signs. Oracle: all exact legal borders."""
import networkx as nx,json
from pathlib import Path
from collections import Counter
D=Path(__file__).parent;counts=Counter();first=None;fail=[]
for num,line in enumerate((D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines(),1):
    g=nx.from_graph6_bytes(line);assert len(g)==22;h=[sum(1<<j for j in g[i] if j<21) for i in range(21)];I=[0]
    for i,r in enumerate(h):I.extend([s|1<<i for s in I if not r&s]);
    T=[s for s in I if s.bit_count()==6];B=[s for s in I if all(s&t for t in T)];assert B and max(s.bit_count() for s in I)==6;miss=0
    for a in range(1,21):
        for c in range(1,21):
            if not (h[0]>>a&1) or h[0]>>c&1:continue
            q=1<<a|1<<c;ok=any(s&q==q for s in B);edge=h[a]>>c&1;six=any(not t&~(h[a]|h[c]) for t in T);assert not (ok and (edge or six));k='legal' if ok else 'both' if edge and six else 'edge' if edge else 'six' if six else 'miss';counts[k]+=1
            if k=='miss':
                miss+=1
                if first is None:
                    from itertools import combinations
                    S=[s for s in I if s&q==q];H={t:sum(1<<j for j,s in enumerate(S) if s&t) for t in T};assert all(H.values());rows=next(((t,u) for t,u in combinations(T,2) if not H[t]&H[u]),());labels=lambda t:[j for j in range(21) if t>>j&1];first=dict(record=num,pair=[a,c],legal_borders=len(B),independent_sixes=len(T),two_set_certificate=[labels(t) for t in rows],available_hits=[labels(t&~(h[a]|h[c])) for t in rows])
    if miss:fail.append(num)
r=dict(records=num,counts=dict(counts),first_miss=first,records_with_misses=fail);print(num,counts,first,len(fail));D.joinpath('ramsey_37_blocked_six_transfer.json').write_text(json.dumps(r,indent=2)+'\n')
