"""Compare the 12 mixed realizations to the literal row swap, not just the chosen endpoints. Distance is total changed interior positions in the two paths (permitting exchange of halves); endpoints and visit order fixed."""
import json
from collections import Counter
from pathlib import Path
from ramsey_strip_local_stitch import routes
from ramsey_strip_first_generator import r,fixed
H=Path(__file__).parent
sw=lambda p:tuple(r[i] for i in p)
seed=[]
for z in json.loads((H/'ramsey_strip_closure_control.json').read_text()):
    p=z['path'];
    if (p[0],p[-1])==(0,29):
        a=tuple(p[1:-1]);seed.extend([(a,sw(a)),(sw(a),a)])
h=Counter();fixed_hits=Counter();overlap=Counter();sym=Counter()
for (a,b),ok,_ in routes:
    dif=lambda x,y:sum(i!=j for i,j in zip(x,y));h[ok,min(dif(a,c)+dif(b,d) for c,d in seed)]+=1;fixed_hits[tuple(sorted((len(set(a)&fixed),len(set(b)&fixed))))]+=1;overlap[len(set(a)&set(sw(b)))]+=1;sym[ok,tuple(i for i,(x,y) in enumerate(zip(a,sw(b)),1) if x==y)]+=1
print('nearest seed strip distances',h,'interior fixed hits',fixed_hits,'reflected overlap',overlap,'aligned visits',sym)
