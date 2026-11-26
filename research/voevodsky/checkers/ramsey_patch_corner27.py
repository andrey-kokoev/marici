"""Corner-distance characterization. Enumerate the common exterior blockers, count which corners are further than two red steps, and compare predicted exact patch counts with endpoint search."""
import json,collections,gzip,itertools,functools
from ramsey_retention_slice import CAT,D,decode
P=D.parent;R=json.loads((P/'ramsey_patch_edge27.json').read_text());ids={r['row'] for r in R};A={i:decode(s.strip()) for i,s in enumerate(gzip.open(CAT/'r38_27.g6.gz','rt')) if i in ids};F=(1<<27)-1;out=[];hist=collections.Counter();motif=collections.Counter();freq=collections.Counter()
for r in R:
 a=A[r['row']];c=r['c'];U=F&~functools.reduce(int.__or__,[a[i] for i in c]);V=[v for v in range(27) if U>>v&1];Q=[sum(1<<v for v in q) for q in itertools.combinations(V,5) if all(not a[i]>>j&1 for i,j in itertools.combinations(q,2))];T=functools.reduce(int.__and__,Q);rv=[]
 for v in V:
  near=[i for i in c if not a[i]&a[v]];rv.append(dict(v=v,common=bool(T>>v&1),compatible=near,deg=(a[v]&U).bit_count()));freq[bool(T>>v&1),len(near)]+=1
 predict=sum(len(z['compatible']) for z in rv if z['common']);assert 2*predict==r['count'];good=[z for z in rv if z['common'] and z['compatible']];hist[len(Q),T.bit_count(),len(good)]+=1;motif[r['n'],all(z['deg']==0 for z in good),any(z['deg']==0 for z in good)]+=1;out.append(dict(row=r['row'],c=c,U=U,quintuples=Q,common=T,vertices=rv))
print('patterns',hist,'isolated',motif,'freq',freq);(P/'ramsey_patch_corner27.json').write_text(json.dumps(out)+'\n')
