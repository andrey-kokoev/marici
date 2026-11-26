"""Compare three tied wedge profiles against actual blue-eight damage and local repair success. Keep earlier repairs, root partition and new red links. With <=3 further edits two of them must include the target and one side of its preexisting red wedge."""
import itertools,json,collections
from ramsey_retention_slice import D,decode,check,has
P=D.parent;z=json.loads((P/'ramsey_38_reverse_seed.json').read_text());g=decode(next(r['graph6'] for r in json.loads(D.read_text()) if (r['l'],r['k'])==(3,8)));g.append(z['best'][1]['red_core']|1<<22|1<<26)
for i in range(27):
 if g[-1]>>i&1:g[i]|=1<<27
for i,j in [(5,22),(21,26)]:g[i]^=1<<j;g[j]^=1<<i
C=z['core_mask']|1<<27;J=z['neighbor_mask'];F=(1<<28)-1;freeze={(5,22),(21,26),(22,27),(26,27)};E=set(itertools.combinations(range(28),2))-freeze;E={e for e in E if z['root'] not in e}
def count(a,p,k):
 if not k:return 1
 total=0
 while p.bit_count()>=k:b=p&-p;p^=b;total+=count(a,p&~a[b.bit_length()-1],k-1)
 return total
out=[]
for u,v in [(4,24),(7,13),(7,14)]:
 w=(g[u]&g[v]).bit_length()-1;assert g[u]&g[v]==1<<w;target=(u,v);p=F&~(g[u]|g[v]|1<<u|1<<v);r=dict(edge=target,blue4=count(g,p,2),blue8=count(g,p,6));out.append(r);seen=set();ok=[];best=None
 for second in [tuple(sorted((u,w))),tuple(sorted((v,w)))]:
  for third in E-{target,second}:
   edits=tuple(sorted((target,second,third)))
   if edits in seen:continue
   seen.add(edits);a=g.copy()
   for i,j in edits:a[i]^=1<<j;a[j]^=1<<i
   if has(a,F,3) or not check(a,F>>1,3,8) or not check(a,C,3,7):continue
   e=sum((a[i]&C).bit_count() for i in range(28) if C>>i&1)//2
   if not 45<=e<=49:continue
   if any(not(a[i]&J) for i in range(28) if C>>i&1) or any(not(a[i]>>j&1) and ((a[i]|a[j])&J).bit_count()<2 for i,j in itertools.combinations([i for i in range(28) if C>>i&1],2)):continue
   n=count(a,F,8);ok.append((edits,n));best=n if best is None else min(n,best)
 r.update(legal_repair_count=len(ok),best_remaining=best,repairs=ok);print(target,r['blue4'],r['blue8'],len(ok),best,flush=True)
(P/'ramsey_38_tet_repair_outcomes.json').write_text(json.dumps(dict(baseline_blue8=count(g,F,8),rows=out),indent=1)+'\n')
