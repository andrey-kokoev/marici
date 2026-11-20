"""Diagnostic only: recover minimal arity of clauses needed to describe which locally legal assignments complete. Exact outputs used to form projections, never advertised as a predictor. Empty relation corresponds to already dead host, so exclude it. Bits denote flips relative to input (arity invariant to bit complements)."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json,sys
D=Path(__file__).parent
for name in sys.argv[1:] or ['ramsey_four_open_audit.json']:
    rows=json.loads((D/name).read_text());hist=Counter();cases={};dead=0
    for r in rows:
        E=set(r['exact']);L=set(r['allowed']);
        if not E:dead+=1;continue
        levels=[]
        for k in range(5):
            masks=[sum(1<<i for i in inds) for inds in combinations(range(4),k)];pred={x for x in L if all(any((x^e)&m==0 for e in E) for m in masks)};assert E<=pred;levels.append(sorted(pred-E))
        arity=next(k for k,d in enumerate(levels) if not d);hist[arity]+=1;cases.setdefault(arity,dict(index=r['index'],exact=sorted(E),false_after_previous=levels[arity-1] if arity else []))
    print(name,'dead:',dead,'minimum arities:',sorted(hist.items()),'counterexamples:',cases)
