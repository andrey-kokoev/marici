"""Enumerate every automorphism of the two shared 5-cycles; retain maps interchanging both full views in both directions."""
import json,itertools,collections
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';r=json.loads((D/'ramsey_37_anchored_pair_split.json').read_text());A,B=({x['anchor']:set(x['triples'][k]) for x in r} for k in range(2));V=set(A);cycles=[];left=set(V)
while left:
 u=min(left);c=[u];v=min(A[u]&B[u]);
 while v!=u:
  c.append(v);v,=(A[v]&B[v])-{c[-2]}
 cycles.append(c);left.difference_update(c)
assert list(map(len,cycles))==[5,5];maps=[]
for swap,s,t,i,j in itertools.product(range(2),[-1,1],[-1,1],range(5),range(5)):
 f={u:cycles[k^swap][((s,t)[k]*h+(i,j)[k])%5] for k,c in enumerate(cycles) for h,u in enumerate(c)}
 if all({f[v] for v in A[u]}==B[f[u]] and {f[v] for v in B[u]}==A[f[u]] for u in V):maps.append(f)
by={u:[f for f in maps if f[u]==u] for u in sorted(V)};out=dict(cycles=cycles,total=len(maps),fixedCounts={u:len(x) for u,x in by.items()},maps=maps);print(out);(D/'ramsey_37_center_duality.json').write_text(json.dumps(out,indent=2)+'\n')
