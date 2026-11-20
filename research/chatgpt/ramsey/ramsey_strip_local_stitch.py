"""Within the exceptional visible word pair, enumerate replacements of just one actual half, with all marks fixed, and check the unused incidence positions."""
from ramsey_strip_37_order_control import bins,ps,words,full,s,t,fill,combinations,Counter
from ramsey_strip_mixed_mod_holdout import N
key,=[k for k,c in bins.items() if len(c)==2];routes=[]
for a in ps:
 if words[a]!=key[0]:continue
 for b in ps:
    if words[b]!=key[1] or set(a)&set(b):continue
    rem=frozenset(full-{s,t}-set(a)-set(b));routes.append(((a,b),fill(rem),rem))
assert len(routes)==12;flips=[];types=Counter()
for (p,c,u),(q,d,v) in combinations(routes,2):
 shared=[i for i in (0,1) if p[i]==q[i]]
 if not shared:continue
 types[tuple(sorted((c,d)))]+=1
 if c==d:continue
 j=1-shared[0];pa,pb=(p[j],q[j]) if c else (q[j],p[j]);good,bad=(u,v) if c else (v,u);delta=[i+1 for i,(x,y) in enumerate(zip(pa,pb)) if x!=y];flips.append((len(delta),delta,pa,pb,sorted(good),sorted(bad),sorted(x for x in bad if not N[x]&bad),p[shared[0]]))
print('pair types',types,'flip distances',Counter(f[0] for f in flips));print('closest',min(flips) if flips else None)
