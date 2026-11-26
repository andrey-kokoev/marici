"""Split edits into triangle constraints and coverage constraints. Test all proper subsets (max two edits) and identify whether destroying the last patch coincides with losing all one-vertex extensions."""
import json,gzip,itertools,collections
from ramsey_retention_slice import D,CAT,decode
P=D.parent;R=json.loads((P/'ramsey_block_patch_release26.json').read_text());ids={r['row'] for r in R};A={i:decode(l.strip()) for i,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rt')) if i in ids};out=[];stats=collections.Counter();half=collections.Counter()
for r in R:
 a=A[r['row']];dl=r['dl'];I=[0];
 for i,v in enumerate(a):
  if i!=dl:I.extend([s|1<<i for s in I if not s&v]);
 qs=[q for q in I if q.bit_count()==7];hits=[sum(1<<j for j,q in enumerate(qs) if q>>i&1) for i in range(27)];miss={0:(1<<len(qs))-1};
 for s in I[1:]:miss[s]=miss[s&(s-1)]&~hits[(s&-s).bit_length()-1]
 runs=[];E=r['add'];mask=((1<<27)-1)^(1<<dl)
 for k in range(len(E)+1):
  for edges in itertools.combinations(E,k):
   es=[1<<u|1<<v for u,v in edges];active=sum(1<<j for j,q in enumerate(qs) if not any(q&e==e for e in es));cov=[s for s in I if not miss[s]&active];ok=[s for s in cov if not any(s&e==e for e in es)];b=[v&mask for v in a];
   for u,v in edges:b[u]|=1<<v;b[v]|=1<<u
   patch=any(all(q>>v&1 for q in r['q']) and any(not b[v]&b[c] for c in r['c']) for v in range(27));runs.append(dict(edges=edges,extensions=len(ok),coverage_only=len(cov),patch=patch));
   if k==1 and len(E)==2:half[patch,bool(ok)]+=1
 stats[runs[0]['extensions']]+=1;out.append(dict(row=r['row'],dl=dl,runs=runs))
print(stats,half, 'full relaxed counts',min(r['runs'][-1]['coverage_only'] for r in out),max(r['runs'][-1]['coverage_only'] for r in out));(P/'ramsey_regrowth_edit_lattice.json').write_text(json.dumps(out)+'\n')
