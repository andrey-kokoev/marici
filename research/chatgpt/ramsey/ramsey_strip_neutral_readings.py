"""Distinguish one remaining incidence, one possible completion, and two possible completions with the literal poles. No neutral semantics assumed. Count matchings only on unused moving orbits of folded prism."""
import json
from pathlib import Path
from collections import Counter
from ramsey_strip_prism_proof import V,E,rep,labels
from functools import lru_cache
@lru_cache(None)
def count(S):
    if not S:return 1
    a=min(S);return sum(count(S-{a,b}) for b in S if tuple(sorted((a,b))) in E)
z=Counter()
for row in json.loads(Path(__file__).with_name('ramsey_strip_length_control.json').read_text()):
    p=row['path'];
    if (p[0],p[-1])!=(0,29):continue
    S=frozenset(V-{labels[rep(x)] for x in p[1:-1]});m=count(S);assert bool(m)==row['closes'];z[len(p)-2,m]+=1
for L in sorted({L for L,m in z}):print(L,{m:n for (l,m),n in sorted(z.items()) if l==L})
