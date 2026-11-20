"""Apply row-invariant residual filling and actual C5 completion tests independently. Distinguish partial orbit consistency from existence of a fully invariant matching."""
from collections import Counter
from ramsey_strip_unassisted_short_prefix import base,GS,action,moved,infer
from ramsey_strip_minimal_shared_constraints import allms
from ramsey_strip_matching_restart import r
obs=set()
for i,(a,b) in enumerate(zip(base,base[1:])):
 if i%2:a,b=r[a],r[b]
 obs.add(tuple(sorted((a,b))))
active=set(base)|{r[v] for v in base};records=[]
for M in allms:
 if not obs<=M:continue
 residual=frozenset(e for e in M if not set(e)&active);rowok=len(residual)==10 and moved(residual,r)==residual
 groups=[G for G in GS if all(moved(M,action(p))==M for p in G)];records.append((M,rowok,groups))
print('route-compatible completions by (row-invariant residue, C5 groups)',Counter((ok,len(g)) for m,ok,g in records));print('partial consistent groups',len(infer(obs)),'groups with actual invariant completions',len(set(G for m,ok,gs in records for G in gs)),'after residual row condition',len(set(G for m,ok,gs in records if ok for G in gs)))
assert len(records)==13 and sum(ok for m,ok,g in records)==3
