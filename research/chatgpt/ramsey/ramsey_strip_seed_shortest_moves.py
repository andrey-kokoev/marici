"""Generate shortest local reroutings (a cage octagon) with literal poles and reflected entry/exit. Do not read mark profiles, target windows or closure when generating. Compare the eight previously observed stitches only after generation."""
from itertools import combinations
from collections import defaultdict,Counter
from ramsey_strip_first_generator import N,r,fixed
from functools import lru_cache
s,t=0,29;paths=[]
def walk(p):
 if len(p)==11:
    if t in N[p[-1]]:paths.append(p[1:])
    return
 for y in N[p[-1]]-{t}-set(p):walk(p+(y,))
walk((s,));full=set(range(30))-{s,t}
@lru_cache(None)
def matches(rem):
 if not rem:return True
 v=min(rem);return any(matches(rem-{v,u}) for u in N[v]&rem)
families=defaultdict(set);windows=Counter()
for h in paths:
 options=[p for p in paths if p[0]==r[h[0]] and p[-1]==r[h[-1]] and not set(p)&set(h)];
 for a,b in combinations(options,2):
    delta=[i for i in range(10) if a[i]!=b[i]]
    if len(delta)!=3 or delta[-1]-delta[0]!=2:continue
    z=(h,*sorted((a,b)));families['seed'].add(z);fa=matches(frozenset(full-set(h)-set(a)));fb=matches(frozenset(full-set(h)-set(b)));windows[delta[0]+1,fa!=fb]+=1
    if fa!=fb:families['flips'].add(z)
    if all(len(set(path)&fixed)==1 for path in (h,a,b)):
        families['one_fixed'].add(z)
        if fa!=fb:families['one_fixed_flip'].add(z)
print('candidate counts', {k:len(v) for k,v in families.items()},'windows',windows)
from ramsey_strip_local_stitch import flips
target={(h,*sorted((a,b))) for _,idx,a,b,_,__,iso,h in flips};assert len(target)==8 and target<=families['one_fixed_flip'];print('target hits',{k:len(target&v) for k,v in families.items()})
# Local nomination: a vertex unused by either route choice already has only one
# neighbor outside the common half. Just one alternative consumes that neighbor.
nominees=set()
for z in families['one_fixed']:
 h,a,b=z;rest=full-set(h)
 for v in rest-set(a)-set(b):
    ns=N[v]&rest
    if len(ns)==1 and bool(ns&set(a))!=bool(ns&set(b)):nominees.add(z)
assert nominees==target;print('local nominations',len(nominees))
