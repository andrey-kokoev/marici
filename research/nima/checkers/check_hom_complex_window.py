"""Exact finite integer Hom-complex controls; not RHom or a Rzk instance."""
from pathlib import Path
import hashlib
import json

# Each complex lists basis dimensions and sparse differential entries
# (source degree, target row, source column). A homogeneous map uses the
# same keys; its degree is supplied to compose/delta, never inferred.
def clean(v): return {k:c for k,c in v.items() if c}
def add(a,b,sign=1):
    c=dict(a)
    for k,v in b.items(): c[k]=c.get(k,0)+sign*v
    return clean(c)
def compose(g,p,f,q):
    out={}
    for (i,row,col),a in f.items():
        for (j,r,c),b in g.items():
            if j==i+q and c==row:
                key=(i,r,col);out[key]=out.get(key,0)+b*a
    return clean(out)
def parity(n): return 1 if n%2==0 else -1
def delta(L,M,f,n):
    return add(compose(M[1],1,f,n),compose(f,n,L[1],1),-parity(n))
def map_sample(L,M,n,seed):
    return clean({(i,r,c):((i+2)*7+r*3+c*5+seed)%7-3
                  for i,dim in L[0].items() for c in range(dim)
                  for r in range(M[0].get(i+n,0))})
def identity(L): return {(i,j,j):1 for i,d in L[0].items() for j in range(d)}
def complex_sample(scale):
    dims={i:2 for i in range(-2,3)}
    return dims,{(i,0,1):scale*(i+3) for i in range(-2,2)}
L,M,N=(complex_sample(s) for s in (1,2,3))
checks=0;wrong_sign_detected=False
for C in (L,M,N):
    assert not compose(C[1],1,C[1],1);checks+=1
for p in range(-3,4):
    for q in range(-3,4):
        for seed in range(3):
            f=map_sample(L,M,q,seed);g=map_sample(M,N,p,seed+1)
            assert not delta(L,M,delta(L,M,f,q),q+1)
            lhs=delta(L,N,compose(g,p,f,q),p+q)
            rhs=add(compose(delta(M,N,g,p),p+1,f,q),
                    compose(g,p,delta(L,M,f,q),q+1),parity(p))
            assert lhs==rhs
            wrong=add(compose(delta(M,N,g,p),p+1,f,q),
                      compose(g,p,delta(L,M,f,q),q+1))
            if p%2 and lhs!=wrong:wrong_sign_detected=True
            checks+=2
assert wrong_sign_detected;checks+=1
# T=B plus a contractible pair. B=Z in degree zero. d_T(-1)->T_0
# hits the second summand. H_0 projects that summand back to degree -1.
T=({-1:1,0:2},{(-1,1,0):1})
B=({0:1},{})
I={(0,0,0):1};P={(0,0,0):1};H={(0,0,1):1}
assert compose(P,0,I,0)==identity(B)
ip=compose(I,0,P,0)
assert add(compose(T[1],1,H,-1),compose(H,-1,T[1],1))==add(identity(T),ip,-1)
checks+=2
for n in range(-4,5):
    for seed in range(5):
        f=map_sample(L,T,n,seed)
        hf=compose(H,-1,f,n)
        lhs=add(delta(L,T,hf,n-1),compose(H,-1,delta(L,T,f,n),n+1))
        assert lhs==add(f,compose(ip,0,f,n),-1)
        assert delta(L,B,compose(P,0,f,n),n)==compose(P,0,delta(L,T,f,n),n+1)
        checks+=2
root=Path('research/nima')
source=root/'rzk/14-hom-complex-window.rzk.md'
result={'status':'passed','assertions':checks,'composition_degrees':[-3,3],
        'postcontraction_degrees':[-4,4],'wrong_odd_leibniz_sign_detected':wrong_sign_detected,
        'scope':'Finite integer complexes; independent matrix controls, not derived Hom or physical data',
        'rzk_source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root/'results/hom-complex-window-control.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
