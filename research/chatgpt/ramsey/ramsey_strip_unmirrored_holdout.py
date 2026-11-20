"""Relax exact reflected return: two disjoint equal-length half-routes with the same two mark counts. Keep the literal row poles but allow other fixed nodes inside a path. Test ordinary shared residual completion (no global swap symmetry imposed), using the same test on mirrored controls."""
from ramsey_strip_mixed_mod_holdout import *
from collections import defaultdict
s,t=0,29;br=(0,15,9,29);fixed={0,9,14,15,26,29};groups=defaultdict(list);full=set(range(30));base={(z['length'],sum(z['counts'])) for z in json.loads((H/'ramsey_strip_length_control.json').read_text())}
def walk(p):
 for x in N[p[-1]]-set(p):
    if x==t:
        cnt=tuple(sum(tuple(dist[v][i] for i in br) in rule for v in p[1:]) for rule in rules);groups[len(p),cnt].append(tuple(p[1:]));continue
    if len(p)<13:walk(p+[x])
walk([s]);
@lru_cache(None)
def fill(rem):
 if not rem:return True
 x=min(rem);return any(fill(rem-{x,y}) for y in N[x]&rem)
h=Counter();example=None
for (l,c),ps in sorted(groups.items()):
 for a,b in combinations(ps,2):
    if set(a)&set(b):continue
    S=sum(c);ok=fill(frozenset(full-{s,t}-set(a)-set(b)));pred=(l%3,S%4) not in {(0,0),(2,1)}
    h[l,S,ok,pred]+=1
    if example is None and (l,S) not in base and ok!=pred:example=(l,c,a,b,ok,pred)
print('new example',example);print('new groups',[(k,v) for k,v in sorted(h.items()) if k[:2] not in base]);print('total,wrong',sum(h.values()),sum(n for (l,S,o,p),n in h.items() if o!=p));print('mixed',[(l,S) for l,S,o,p in h if o and (l,S,False,p) in h])
