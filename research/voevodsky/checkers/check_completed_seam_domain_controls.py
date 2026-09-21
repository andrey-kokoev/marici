"""Finite differential and endpoint-support checks for completion controls."""
from pathlib import Path
from itertools import product,combinations
from collections import defaultdict
import runpy
import json
ROOT=Path(__file__).resolve().parents[3]
src=runpy.run_path(str(ROOT/'research/nima/checkers/check_seven_event_factorization_descent.py'))
feature=src['feature']

def differential(column):
    out=defaultdict(int)
    for (markers,buffers),c in column.items():
        preceding=0
        for i,marker in enumerate(markers):
            if marker[0]!='e':continue
            _,x,y,keep=marker
            sign=(-1)**preceding
            preceding+=1
            for word,b in feature(x,y,keep).items():
                left=list(markers);words=list(buffers)
                left[i]=('v',y);words[i]=words[i]+word
                out[tuple(left),tuple(words)]+=sign*c*b
                right=list(markers);words=list(buffers)
                right[i]=('v',x);words[i+1]=word+words[i+1]
                out[tuple(right),tuple(words)]-=sign*c*b
    return {k:v for k,v in out.items() if v}

checks=0
for r in range(1,5):
    for active in product((False,True),repeat=r):
        for keeps in product((0,1),repeat=r):
            markers=tuple(('e',(1<<i)-1,(1<<(i+1))-1,keeps[i]) if active[i]
                          else ('v',(1<<i)-1) for i in range(r))
            for patterned in (False,True):
                buffers=tuple((20+i,) if patterned else () for i in range(r+1))
                vector={(markers,buffers):1}
                assert not differential(differential(vector))
                checks+=1

# Added prime coordinates cannot occur in a monotone interval with old endpoints.
interval_checks=0
for old in range(1,5):
    for x in range(1<<old):
        for y in range(1<<old):
            if x&y!=x:continue
            interval=[z for z in range(1<<(old+2)) if x&z==x and z&y==z]
            assert all(z<(1<<old) for z in interval)
            assert len(interval)==2**((y^x).bit_count())
            interval_checks+=1
result={'passed':True,'mixed_degree_d_squared_checks':checks,
 'convex_endpoint_interval_checks':interval_checks,
 'scope':'Exact finite structural checks. Bounded differential extension and endpointwise injectivity of the specified l1 completion are proved in the companion note; no uniform inverse or arbitrary inverse-limit claim.'}
out=ROOT/'research/voevodsky/results/completed-seam-domain-controls.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
