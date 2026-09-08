"""Exact rational and Gaussian-rational triangle recovery, without roots."""
import json
from itertools import combinations
from pathlib import Path
from sympy import I, Integer, Matrix, prod, simplify

source=Path('research/nima/results/triangle_recovery.json')
data=json.loads(source.read_text(encoding='utf-8'))
assert data['status']=='passed'
T=[frozenset(tuple(c) for c in t) for t in data['triangulations']]
f=list(map(Integer,data['input_values']))
n=6
boundary={tuple(sorted((i,(i+1)%n))) for i in range(n)}
triples=list(combinations(range(n),3))
faces=[[q for q in triples if all(e in t|boundary for e in combinations(q,2))] for t in T]
channels=sorted(set().union(*T))
A=Matrix([[int(c in t) for c in channels] for t in T])
z=next(z for z in A.T.nullspace() if (z.T*Matrix(f))[0]!=0)

def recover(w):
    assert all(v!=0 for v in w)
    g={}
    for a,b in combinations(range(len(T)),2):
        if len(T[a]^T[b])!=2:continue
        old=next(iter(T[a]-T[b]));new=next(iter(T[b]-T[a]))
        q=tuple(sorted(set(old)|set(new)))
        ratio=simplify(w[b]/w[a]) if old==(q[0],q[2]) else simplify(w[a]/w[b])
        if q in g and simplify(g[q]-ratio)!=0:return None
        g[q]=ratio
    h={q:Integer(1) if 0 in q else g[(0,)+q] for q in triples}
    constant=simplify(w[0]/prod(h[q] for q in faces[0]))
    for q in triples:
        if {0,1}<=set(q):h[q]=simplify(h[q]*constant)
    residuals=[simplify(prod(h[q] for q in fs)-value) for fs,value in zip(faces,w)]
    assert all(v==0 for v in residuals)
    return h

records=[]
for label,base in [('positive',Integer(2)),('signed',Integer(-2)),('complex',1+I)]:
    w=[base**v for v in f]
    h=recover(w)
    assert h is not None
    # The selected global character is integral for this witness.
    assert all(v.q==1 for v in z)
    obstruction=simplify(prod(w[i]**int(z[i]) for i in range(len(w))))
    assert simplify(obstruction-1)!=0
    records.append({'case':label,'global_channel_character':str(obstruction),
      'triangle_weights':[{'triangle':q,'weight':str(h[q])} for q in triples],
      'reconstructed_values':len(w)})
bad=[Integer(1)]*len(T)
bad[0]=Integer(2)
assert recover(bad) is None
result={'status':'passed','cases':records,'nonseparable_input_rejected':True,
 'operations':'multiplication and inversion only; no logarithms or root choices',
 'scope':'Three exact six-point examples; generic proof uses simplex contraction in an abelian group of units.'}
Path('research/nima/results/multiplicative_triangle_recovery.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','cases':[{k:v for k,v in r.items() if k!='triangle_weights'} for r in records],'nonseparable_input_rejected':True}))
