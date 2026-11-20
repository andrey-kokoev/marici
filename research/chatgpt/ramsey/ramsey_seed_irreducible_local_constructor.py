"""Direct seed construction: four coordinate frames, one boundary orbit, row-fixed residual bundles, forced quotient matching. No matching enumeration or stored routes."""
from itertools import combinations
P=list(combinations(range(6),2));T=[t for t in combinations(P,3) if len(set(sum(t,())))==6];I=tuple(range(6))
def action(p):
 tr=lambda d:tuple(sorted(p[x] for x in d));return [P.index(tr(d)) for d in P]+[15+T.index(tuple(sorted(map(tr,t)))) for t in T]
move=lambda m,H:frozenset((H[i],H[j]) for i,j in m);R=action((1,0,2,3,5,4));boundary={(0,16),(7,29)};frames=[]
for hub in (2,3):
 for sign in (1,-1):
  chart={5-hub:0,0:1,1:4,5:2*sign%5,4:-2*sign%5};back={v:k for k,v in chart.items()};g=list(I)
  for x,k in chart.items():g[x]=back[(k+1)%5]
  powers=[];p=I
  for _ in range(5):powers.append(action(p));p=tuple(g[x] for x in p)
  observed=frozenset().union(*(move(boundary,H) for H in powers))
  if len(observed)==5:frames.append((hub,sign,powers,observed))
hub,sign,powers,chosen=frames[0];assert len(frames)==1
flags={(i,j) for i,d in enumerate(P) for j,t in enumerate(T,15) if d in t};bundles={frozenset().union(*(move({e},H) for H in powers)) for e in flags};todo=set(range(30))-{v for e in chosen for v in e};steps=[]
while todo:
 options=[b for b in bundles if move(b,R)==b and {v for e in b for v in e}<=todo]
 choices={v:[b for b in options if any(v in e for e in b)] for v in todo};assert all(choices.values());v=min(v for v in todo if len(choices[v])==1);bundle,=choices[v];chosen|=bundle;todo-={v for e in bundle for v in e};steps.append(sorted(bundle))
assert len(chosen)==15 and len({i for i,j in chosen})==len({j for i,j in chosen})==15 and boundary<=chosen
assert len(chosen&move(chosen,R))==10
print('selected hub/sign',hub,sign,'forced residual bundles',steps,'complete matching',sorted(chosen))
from ramsey_seed_affine_witness import m
assert chosen==m;print('matches independently derived affine witness',True)
