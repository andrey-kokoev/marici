"""Recompute signed port witnesses from each admissible cover of the middle graph. No stored successor or signed readouts are used. Frame means an ordered family pair and one source star. Record ordered red-link endpoint pairs separately from port counts."""
from collections import Counter
import json
from ramsey_37_middle_support_recovery import pairs,E,D
counts=Counter();records=[]
for pair in pairs:
    for F,G in [pair,pair[::-1]]:
        mate={next(t for t in G if not t&s):s for s in F}
        step={s:mate[next(t for t in G if len(t&s)==1)] for s in F}
        for s in F:
            q=s;hits={};ns=Counter()
            for d in [1,2,-2,-1]:
                q=step[q];u,=s&q;v,=step[s]&step[q];support=lambda h:sum(len(h&t) for t in G if u in t);z=support(q)-support(s);assert z in [-1,1]
                if tuple(sorted((u,v))) in E:
                    key=('A' if d>0 else 'B')+('+' if z>0 else '-');ns[key]+=1;hits[key]=[u,v]
            val=tuple(ns[k] for k in ('A+','A-','B+','B-'));counts[val]+=1;records.append((hits['A+'],hits['B-'],sorted(s)))
assert len(records)==200 and counts=={(1,0,0,1):200};pairs_seen=sorted({(tuple(a),tuple(b)) for a,b,s in records});out=dict(frames=len(records),counts=[1,0,0,1],distinct_ordered_witness_pairs=len(pairs_seen),A_links=len({a for a,b in pairs_seen}),B_links=len({b for a,b in pairs_seen}),examples=pairs_seen[:4]);print(out);(D/'ramsey_37_port_value_vs_identity.json').write_text(json.dumps(out,indent=2)+'\n')
