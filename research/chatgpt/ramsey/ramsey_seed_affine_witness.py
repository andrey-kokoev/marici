"""End-to-end witness from boundary-selected affine formula. No stored strip, matching census, graph catalogue or JSON input. Exhaustively verifies both row-related output graphs."""
from itertools import combinations
from ramsey_seed_boundary_equations import partition,hits
P=list(combinations(range(6),2));T=[t for t in combinations(P,3) if len(set(sum(t,())))==6];hub,sign,a=hits[0];chart={5-hub:0,0:1,1:4,5:2*sign%5,4:-2*sign%5}
m=frozenset((i,15+T.index(tuple(sorted(tuple(sorted(b)) for b in partition(hub,chart,a,frozenset(d)))))) for i,d in enumerate(P));assert len(m)==15 and len({j for i,j in m})==15 and all(P[i] in T[j-15] for i,j in m)
r6=(1,0,2,3,5,4);tr=lambda d:tuple(sorted(r6[x] for x in d));r=[P.index(tr(d)) for d in P]+[15+T.index(tuple(sorted(map(tr,t)))) for t in T];mate=frozenset((r[i],r[j]) for i,j in m);assert len(m&mate)==10
for row,M in enumerate((m,mate)):
 removed={tuple(sorted(P.index(d) for d in T[j-15] if d!=P[i])) for i,j in M};red={(0,1+i) for i in range(6)}|{(1+i,7+j) for j,d in enumerate(P) for i in d}|{(7+i,7+j) for i,j in combinations(range(15),2) if not set(P[i])&set(P[j]) and (i,j) not in removed};N=[0]*22
 for i,j in red:N[i]|=1<<j;N[j]|=1<<i
 triangles=sum(bool(N[i]>>j&1 and N[j]>>k&1 and N[i]>>k&1) for i,j,k in combinations(range(22),3))
 def independent(mask,k):
  if not k:return 1
  if mask.bit_count()<k:return 0
  total=0
  while mask:
   bit=mask&-mask;mask^=bit;v=bit.bit_length()-1;total+=independent(mask&~N[v],k-1)
  return total
 sevens=independent((1<<22)-1,7);assert len(red)==66 and triangles==sevens==0;print('row',row,'matching flags',len(M),'red edges',len(red),'triangles',triangles,'blue sevens',sevens)
# Derive route only after constructing the matching pair.
adj={}
for i,j in m^mate:adj.setdefault(i,set()).add(j);adj.setdefault(j,set()).add(i)
p=[0,16]
while p[-1]!=29:
 nxt,=adj[p[-1]]-{p[-2]};p.append(nxt)
assert p==[0,16,13,19,7,29];print('derived active half',p)
