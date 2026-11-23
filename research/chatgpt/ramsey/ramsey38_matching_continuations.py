"""Exact named deletion/reattachment continuations; compare alignments and stabilizer of initial named wiring."""
from pathlib import Path
from itertools import permutations,combinations
from collections import Counter
import json
D=Path(__file__).parent;r=json.loads((D/'ramsey_seven_all_wirings.json').read_text());S=r['address_masks'];E=list(map(tuple,r['edge_order']));W=sorted(r['wirings']);V=range(27);ls=lambda s:[i for i in V if s>>i&1];P={}
for p in permutations(range(7)):
 T=[sum(1<<p[i] for i in range(7) if s>>i&1) for s in S];
 if set(T)!=set(S):continue
 m=list(map(S.index,T));e=[E.index(tuple(sorted((m[i],m[j])))) for i,j in E];P[p]=[W.index(sum((w>>i&1)<<j for i,j in enumerate(e))) for w in W]
C=P[(0,1,4,5,2,3,6)];L=P[(0,1,2,3,5,4,6)];J=[L[C[L[i]]] for i in range(8)];data=[]
for w in W:
 H=[0]*27
 def link(i,j):H[i]|=1<<j;H[j]|=1<<i
 for i in range(7):link(0,1+i)
 for i,s in enumerate(S):
  for j in ls(s):link(8+i,1+j)
 for i,(a,b) in enumerate(E):
  if w>>i&1:link(8+a,8+b)
 I=[0]
 for i,h in enumerate(H):I.extend([s|1<<i for s in I if not s&h]);
 assert max(s.bit_count() for s in I)==7 and not any(H[a]&H[b] for a,b in combinations(V,2) if H[a]>>b&1);T=[s for s in I if s.bit_count()==7];F={}
 for d in range(1,27):
  t=[s for s in T if not s>>d&1];F[d]={s for s in I if not s>>d&1 and all(s&q for q in t)};assert H[d] in F[d]
 data.append((H,F,T))
stats=Counter();ex=None;fixed_inputs=[]
for i in range(8):
 a,b=C[i],J[i];assert a!=b;fixed_inputs.append(any(g[i]==i and g[a]==b for g in P.values()));h,f,t=data[a];k,g,u=data[b]
 for d in range(1,27):
  stats['queries']+=1;stats['different_counts']+=len(f[d])!=len(g[d]);stats['different_sets']+=f[d]!=g[d];z=(f[d]^g[d])-{h[d],k[d]};stats['nonrestoration_difference']+=bool(z)
  if not z or ex or d not in (1,2,3,4,7):continue
  s=min(z);ok=s in f[d];bad=k if ok else h;holes=u if ok else t;ex=dict(input_index=i,output_indices=[a,b],deleted=d,support=ls(s),legal=[ok,not ok],counts=[len(f[d]),len(g[d])],failed_red_pair=next(([x,y] for x,y in combinations(ls(s),2) if bad[x]>>y&1),None),missed_seven=next((ls(q) for q in holes if not q>>d&1 and not q&s),None))
o=dict(stats=stats,example=ex,stabilizer_interchanges_for_inputs=fixed_inputs,source_pair_orbits=[len({(g[0],g[z]) for g in P.values()}) for z in [C[0],J[0]]]);print(o);(D/'ramsey38_matching_continuations.json').write_text(json.dumps(o,indent=2)+'\n')
