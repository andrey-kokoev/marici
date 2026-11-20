"""Drop fixed-visit filter. Nominate by threatened leaf and its intrinsic chord length, across all 80 shortest seed-compatible substitutions. Record exact interior fixed positions and check a seed-side interpretation via the two endpoint alternatives."""
from ramsey_strip_seed_shortest_moves import families,target,full,s,t,fixed,N,Counter
from collections import defaultdict
from ramsey_strip_first_generator import r
separated=set();overlaps=Counter()
H=Counter();F=Counter();nom=defaultdict(set);pattern=Counter()
for z in families['seed']:
 h,a,b=z;hp=(s,)+h+(t,);rest=full-set(h);spans=[]
 for v in rest-set(a)-set(b):
    ns=N[v]&rest
    if len(ns)!=1 or bool(ns&set(a))==bool(ns&set(b)):continue
    i,j=[k for k,x in enumerate(hp) if x in N[v]];spans.append(j-i);nom[j-i].add(z)
 delta=[i for i in range(10) if a[i]!=b[i]];i,j=delta[0],delta[-1];O=set((s,*a,t)[i:j+3])|set((s,*b,t)[i:j+3]);assert len(O)==8;size=len(O&{r[x] for x in O});overlaps[size]+=1
 if not size:separated.add(z)
 flags=tuple(tuple(x for x in p if x in fixed) for p in z);F[flags]+=1;H[tuple(sorted(spans)),z in target]+=1
 # complementary pole pair (fan at stationary N, partition pairing through the moving R corners)
 comp={14,26};cross=all({x for x in h+p}&comp==comp for p in (a,b));pattern[cross,z in families['one_fixed']]+=1
assert separated==families['one_fixed'] and separated&set.union(*nom.values())==target;print('octagon overlaps',overlaps)
print('threats x exceptional',H,'fixed flags',F,'compulsory complement coverage x exactly one',pattern,'span eight exactly exceptional?',nom[8]==target)
