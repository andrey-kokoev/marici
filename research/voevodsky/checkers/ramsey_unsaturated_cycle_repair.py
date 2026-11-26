"""Nonlocal step across the exhausted two-cell shell: exchange one label cyclically among three cells, exhaust both orientations. Incremental order-cap cuts before any SAT. Canonically identify surviving incidence graphs with colored bliss, exact first-failure ladder for distinct types. Operates on requested seed index, not a global search."""
from ramsey_unsaturated_regenerate import P,cap,run,json,pairs,collections,ProcessPoolExecutor
import sys,itertools,igraph as ig
col=[0]*26+[1]*8
def key(m):
 g=ig.Graph(34,[(i,26+j) for i,s in enumerate(m) for j in range(8) if s>>j&1]);return tuple(sorted(g.permute_vertices(g.canonical_permutation(color=col)).get_edgelist()))
def cycles(m):
 R=set();subs=[[t for t in range(256) if not s&~t] for s in range(256)];base=[sum(not v&~t for v in m) for t in range(256)];tight=[t for t in range(256) if base[t]>=cap[t.bit_count()]-2];bits=[[1<<j for j in range(8) if s>>j&1] for s in range(256)];total=0
 for inds in itertools.combinations(range(26),3):
  for i,j,k in (inds,(inds[0],inds[2],inds[1])):
   a,b,c=m[i],m[j],m[k];old=(a,b,c);limits=[(t,cap[t.bit_count()]-base[t]+sum(not s&~t for s in old)) for t in tight];limits=[(t,l) for t,l in limits if l<3];
   for x,y,z in itertools.product(bits[a&~b],bits[b&~c],bits[c&~a]):
    new=(a^x^z,b^y^x,c^z^y);total+=1
    if any((not new[0]&~t)+(not new[1]&~t)+(not new[2]&~t)>l for t,l in limits):continue
    v=list(m);v[i],v[j],v[k]=new;R.add(tuple(sorted(v)))
 return total,R
if __name__=='__main__':
 idx=int(sys.argv[1]);m=json.loads((P/'ramsey_unsaturated_regenerate.json').read_text())[0]['parents'][idx];total,rs=cycles(m);uniq={key(v):v for v in sorted(rs)};ms=list(uniq.values());print(total,len(rs),len(ms),flush=True)
 with ProcessPoolExecutor(8) as ex:res=list(ex.map(run,ms,chunksize=8))
 counts=collections.Counter(r[0] for r in res);out=dict(idx=idx,attempts=total,cap_pass=len(rs),types=len(ms),counts=counts,surv=[dict(m=v,gate=r) for v,r in zip(ms,res) if r[0] in ('pair','higher','sat5')]);(P/f'ramsey_unsaturated_cycle_repair_{idx}.json').write_text(json.dumps(out)+'\n');print(counts)
