"""Extract the invariant slot of the archived P->N->E replay, then separately test its geometric incidence as a route reference."""
from collections import Counter
from ramsey_fcc_two_route_feedback import ROOT,D,left,right,run,perm
import json
f=json.loads((ROOT/'strominger/results/native-fcc-end-to-end.json').read_text())['fixture'];ops=f['operations'];slots=[i for i in range(5) if all(op['permutation'][i]==i for op in ops)];assert slots==[2];i=slots[0];alias='C1';ps=f['packets'];native={p['chart']['aliases'][alias] for p in ps};assert native=={'0,0,1,0'} and len({tuple(p['coefficients'][i]) for p in ps})==1
assert all(alias in view['marks'] for view in f['sevenViews'] if view['role'] in ['P active window','N active window','fixed N/E overlap']);anchor=tuple(2-int(x) for x in native.pop().split(','));print('PN,NE unique common fixed slot',i,'coordinate',anchor,'coefficient',ps[0]['coefficients'][i]);axis=str(1+next(k for k,x in enumerate(anchor) if x==1));a=run(left,axis);b=run(right,axis);assert a[2]==tuple(-v for v in b[2]);print('conditional axis reader',axis,a[0],b[0],a[2],b[2]);counts=Counter();dist=lambda x,y:sum((u-v)**2 for u,v in zip(x,y))
for cell in D['coarse_cells']:
    if not cell['id'].startswith('oct-'):continue
    base=tuple(map(min,zip(*cell['vertices'])));site=lambda s:tuple(v+(str(k+1) in s) for k,v in enumerate(base));delta=dist(site('14'),anchor)-dist(site('23'),anchor);counts[(delta>0)-(delta<0)]+=1
print('midpoint squared distance to fixed native site: left closer, equal, right closer',counts[-1],counts[0],counts[1])
