"""Source buffer action, Green contraction and observer moment checks."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import sympy as S


def subset(a,b):return a&b==a

def records(start,finish):
    vertices=[v for v in range(finish+1) if subset(start,v) and subset(v,finish)]
    separators=[(v,v) for v in vertices]
    for v in vertices:
        for p in range(finish.bit_length()):
            w=v|(1<<p)
            if w!=v and subset(w,finish):separators.append((v,w))
    return [(a,b) for a in separators for b in separators if subset(a[1],b[0])]


def differential(basis):
    index={x:i for i,x in enumerate(basis)}
    d=S.zeros(len(basis))
    for col,record in enumerate(basis):
        prior=0
        for j,(tail,head) in enumerate(record):
            if tail!=head:
                sign=(-1)**prior
                for vertex,coefficient in ((head,sign),(tail,-sign)):
                    image=list(record);image[j]=(vertex,vertex)
                    d[index[tuple(image)],col]+=coefficient
                prior+=1
    return d


def dual_differential(d,basis):
    out=d.T.copy()
    for col,record in enumerate(basis):
        k=sum(tail!=head for tail,head in record)
        out[:,col]*=(-1)**(k+1)
    return out


big=records(0,7);small=records(1,7)
dbig=differential(big);dsmall=differential(small)
C=S.zeros(len(big),len(small));index={x:i for i,x in enumerate(big)}
for j,x in enumerate(small):C[index[x],j]=1
assert dbig*C==C*dsmall
obig=dual_differential(dbig,big);osmall=dual_differential(dsmall,small)
assert obig*obig==S.zeros(len(big))
assert osmall*C.T==C.T*obig
# Prefix creation is NOT the contragredient chain action.
assert obig*C!=C*osmall

# Actual signed contraction of a complex feature history, not history reversal.
J=S.diag(1,-1);v=S.Matrix([1+S.I,2-S.I]);tau=S.Rational(3,2)
creation=v
mate=tau**2*v.conjugate().T*J
assert mate==creation.conjugate().T*(tau**2*J)
# Norm squared under the positive weighted carrier on input/output.
assert S.simplify((mate*mate.conjugate().T)[0]/tau**2-tau**2*(v.conjugate().T*v)[0])==0

weight_checks=0
for n in range(13):
    for ell in range(n+1):
        for p in range(5):
            for b in range(1,5):
                for retained in range(ell+1):
                    assert (1+n+ell)**p*b**retained <= (1+n)**p*(2**p*b)**ell
                    assert Fraction((1+n-ell)**p,(1+n)**p)*Fraction(1,b**retained)<=1
                    weight_checks+=1

result={'schema':'marici.grothendieck.moment-observer-source-actions.v1','passed':True,
        'vacuum_complex_sizes':[len(big),len(small)],'exact_weight_checks':weight_checks,
        'checks':{'outer_prefix_action_is_primal_chain_map':True,
                  'green_contraction_commutes_with_signed_observer_differential':True,
                  'ordinary_creation_is_not_the_observer_chain_action':True,
                  'nonreal_signed_feature_contraction_has_required_norm':True},
        'scope':'Exact typed two-seam vacuum complexes, signed feature contraction and scalar weights. Completed source actions and moment-domain stability are proved in the companion note.'}
root=Path(__file__).resolve().parents[3]
out=root/'research/grothendieck/results/moment-observer-source-actions.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
