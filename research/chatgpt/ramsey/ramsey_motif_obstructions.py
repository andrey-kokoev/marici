"""Derive unit clauses on each motif bit from seven-address blue obstructions, conditional only on the 6-label backbone. No completed wiring input."""
from ramsey_seven_incidence_radius import *
from collections import Counter

def addr(i):return ''.join(str(v) for v in range(7) if S[i]>>v&1)
s=z3.SolverFor('QF_FD');s.add(*(c for cs in clauses[:7] for c in cs));frames=[0,2,5,7];B=[backbone(s,k) for k in frames];motif={i for i,(a,b) in enumerate(E) if S[-1] in (S[a],S[b]) or S[a]|S[b]==S[-1]};assert all(set(range(80))-row.keys()==motif for row in B)
covered={i:{} for i in motif}
for J in combinations(range(19),7):
    ids=[E.index(e) for e in combinations(J,2) if e in ix];t=motif.intersection(ids)
    if len(t)!=1:continue
    i,=t;f=sum(1<<h for h,row in enumerate(B) if not any(row.get(v,0) for v in ids));
    if f:covered[i].setdefault(f,[]).append(J)
out={}
for i,groups in sorted(covered.items()):
    masks=list(groups);cover=next(t for size in range(1,5) for t in combinations(masks,size) if reduce(or_,t)==15);res=[{'addresses':list(map(addr,groups[t][0])),'frames':[frames[h] for h in range(4) if t>>h&1]} for t in cover];out[str(i)]=res;print(tuple(map(addr,E[i])),{format(t,'04b'):len(v) for t,v in groups.items()},res)
# Uniform rule, independent of the certificate enumeration or knowledge of the motif.
stars={v:[i for i,m in enumerate(S) if m>>v&1] for v in range(7)};added=0
for v,A in stars.items():
    if len(A)!=6:continue
    for i in set(range(19))-set(A):
        s.add(z3.Or(*[ix[e] for j in A for e in [tuple(sorted((i,j)))] if e in ix]));added+=1
rows=[backbone(s,k) for k in range(8)];print('star rules',added,'forced links',list(map(len,rows)));assert all(len(rows[k])==80 for k in frames)
out['star_rule_check']={'rules':added,'determined':list(map(len,rows))};(D/'ramsey_motif_obstructions.json').write_text(json.dumps(out)+'\n')
