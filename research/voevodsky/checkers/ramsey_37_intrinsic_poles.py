"""Recover roles and full symmetry group from red edges alone; no stored partition or labeling supplied."""
import itertools,json
from collections import Counter
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';E=json.loads((D/'ramsey_37_dual_stars.json').read_text())['red_edges'];N={i:set() for e in E for i in e}
for u,v in E:N[u].add(v);N[v].add(u)
V=set(N);matches=[];types={}
for u,v in E:
 M=V-N[u]-N[v];sig=tuple(sorted(len(N[x]&M) for x in M));types[u,v]=sig
 if sig==(2,)*10:matches.append((u,v))
(u,v),=matches;L=sorted(N[u]-{v});R=N[v]-{u};M=V-N[u]-N[v];partner={i:next(iter(N[i]&R)) for i in L};assert all(len(N[i]&R)==1 for i in L) and set(partner.values())==R
components=[];left=M.copy()
while left:
 x=min(left);s={x};
 while (t:=s.union(*(N[y]&M for y in s)))!=s:s=t
 components.append(sorted(s));left-=s
pairs=lambda H:sorted(sorted(N[x]&H) for x in M);assert len(set(map(tuple,pairs(set(L)))))==10 and len(set(map(tuple,pairs(R))))==10
maps=[]
for swap in (False,True):
 for perm in itertools.permutations(L):
  f={u:v if swap else u,v:u if swap else v};
  for i,j in zip(L,perm):f[i],f[partner[i]]=(partner[j],j) if swap else (j,partner[j])
  Q=R if swap else set(L);lookup={frozenset(N[x]&Q):x for x in M};f.update({x:lookup[frozenset(f[y] for y in N[x]&set(L))] for x in M});
  if all({f[y] for y in N[x]}==N[f[x]] for x in V):maps.append(dict(swap=swap,images=[f[x] for x in sorted(V)]))
out=dict(poles=[u,v],testedEdges=len(E),regularRemainders=len(matches),middleCycles=components,pentagons=[[sorted(N[x]&set(L)) for x in comp] for comp in components],automorphisms=maps);print({k:v for k,v in out.items() if k!='automorphisms'},Counter(x['swap'] for x in maps));(D/'ramsey_37_intrinsic_poles.json').write_text(json.dumps(out,indent=2)+'\n')
