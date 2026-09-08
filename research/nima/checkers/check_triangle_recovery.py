"""Recover triangle weights from a locally separable, non-channel-additive input."""
from itertools import combinations
from functools import lru_cache
from pathlib import Path
import json
from sympy import Matrix

@lru_cache(None)
def ts(v):
    if len(v)<3:return (frozenset(),)
    out=[]
    for k in range(1,len(v)-1):
        extra=set()
        if k>1:extra.add(tuple(sorted((v[0],v[k]))))
        if k<len(v)-2:extra.add(tuple(sorted((v[k],v[-1]))))
        for a in ts(v[:k+1]):
            for b in ts(v[k:]):out.append(a|b|extra)
    return tuple(out)
n=6
T=sorted(ts(tuple(range(n))),key=lambda t:tuple(sorted(t)))
idx={t:i for i,t in enumerate(T)}
channels=sorted(set().union(*T))
A=Matrix([[int(c in t) for c in channels] for t in T])
rows=[]
for i,j in channels:
    left=ts(tuple(range(i,j+1)))
    right=ts(tuple(range(j,n))+tuple(range(i+1)))
    for l in left[1:]:
        for r in right[1:]:
            row=[0]*len(T)
            for a,b,s in [(l,r,1),(left[0],right[0],1),(l,right[0],-1),(left[0],r,-1)]:
                row[idx[a|b|{(i,j)}]]+=s
            rows.append(row)
R=Matrix(rows)
f=next(v for v in R.nullspace() if A.row_join(v).rank()>A.rank())
assert R*f==Matrix.zeros(R.rows,1)
assert A.rank()==9 and A.row_join(f).rank()==10

def increments(values):
    g={}
    for a,b in combinations(range(len(T)),2):
        if len(T[a]^T[b])!=2:continue
        old=next(iter(T[a]-T[b]));new=next(iter(T[b]-T[a]))
        q=tuple(sorted(set(old)|set(new)))
        sign=1 if old==(q[0],q[2]) else -1
        value=sign*(values[b]-values[a])
        if q in g and g[q]!=value:return None
        g[q]=value
    return g
g=increments(f)
assert g is not None and len(g)==15
h={q:(0 if 0 in q else g[(0,)+q]) for q in combinations(range(n),3)}
boundary={tuple(sorted((i,(i+1)%n))) for i in range(n)}
def faces(t):
    edges=t|boundary
    return [q for q in h if all(e in edges for e in combinations(q,2))]
constant=f[0]-sum(h[q] for q in faces(T[0]))
for q in h:
    if {0,1}<=set(q):h[q]+=constant
recovered=Matrix([sum(h[q] for q in faces(t)) for t in T])
assert recovered==f
bad=next(Matrix([int(i==k) for i in range(len(T))]) for k in range(len(T)) if increments(Matrix([int(i==k) for i in range(len(T))])) is None)
assert R*bad!=Matrix.zeros(R.rows,1)
result={'status':'passed','n':n,'triangulations':[sorted(t) for t in T],
 'input_values':list(map(str,f)),'local_residuals':list(map(str,R*f)),
 'channel_rank':9,'augmented_channel_rank':10,'context_free_quadruples':len(g),
 'triangle_weights':[{'triangle':q,'weight':str(v)} for q,v in h.items()],
 'reconstruction_residuals':list(map(str,recovered-f)),
 'nonseparable_counterexample_detected':True,
 'scope':'Exact six-point reconstruction from local-nullspace data, not a channel-weight or triangle-weight ansatz; no source provenance.'}
Path('research/nima/results/triangle_recovery.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['triangle_weights','triangulations']}))
