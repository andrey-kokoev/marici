"""Exact native-chart Hodge derivative and finite rational path controls."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
from check_hodge_fixed_sixfold_pairing import wedge
from check_hodge_deligne_lift_image import rank


def add(*terms):
    out={}
    for scale,form in terms:
        for key,c in form.items():out[key]=out.get(key,0)+scale*c
    return {key:c for key,c in out.items() if c}


def derivation(form,op):
    terms=[]
    for indices,coefficient in form.items():
        for j,i in enumerate(indices):
            term=wedge({indices[:j]:1},op.get(i,{}))
            term=wedge(term,{indices[j+1:]:1})
            terms.append((coefficient,term))
    return add(*terms)


def J(t):
    op={}
    for j,sign in enumerate((1,1,1,-1,-1,-1)):
        op[2*j]={(2*j+1,):-sign};op[2*j+1]={(2*j,):sign}
    c=(1+t*t)/(1-t*t);s=2*t/(1-t*t)
    op[2]={(3,):-c,(7,):s};op[3]={(2,):c,(6,):-s}
    op[6]={(3,):-s,(7,):c};op[7]={(2,):s,(6,):-c}
    return op


def real_imag_pair(j,k):
    return ({(2*j,2*k):1,(2*j+1,2*k+1):-1},
            {(2*j,2*k+1):1,(2*j+1,2*k):1})


def main():
    factors=[v for j in range(3) for v in real_imag_pair(j,j+3)]
    dot={2:{(7,):2},3:{(6,):-2},6:{(3,):-2},7:{(2,):2}}
    r12,s12=real_imag_pair(0,1);r45,s45=real_imag_pair(3,4)
    expected=[add((-2,s12)),add((2,r12)),add((2,s45)),add((-2,r45)),{},{}]
    actual=[derivation(f,dot) for f in factors]
    assert actual==expected
    keys=sorted({key for f in actual for key in f})
    assert rank([[f.get(key,0) for key in keys] for f in actual])==4
    R={};I={}
    for bits in product((0,1),repeat=6):
        n=sum(bits);key=tuple(2*j+b for j,b in enumerate(bits))
        (R if n%2==0 else I)[key]=(-1)**(n//2)
    E={(2*j,2*j+1):d for j,d in enumerate((1,1,1,-1,-1,-3))}
    assert not derivation(R,dot) and not derivation(I,dot) and not derivation(E,dot)
    for t in (Q(0),Q(1,8),Q(-1,8)):
        assert 1-t*t>0
        op=J(t)
        for j in range(12):
            assert derivation(derivation({(j,):1},op),op)=={(j,):-1}
        assert not derivation(E,op) and not derivation(R,op) and not derivation(I,op)
        rejected=[bool(derivation(f,op)) for f in factors]
        assert rejected==([False]*6 if t==0 else [True,True,True,True,False,False])
    result={'passed':True,'classification':'chosen_divisor_witness_fails_while_determinant_stays_Hodge',
        'direction':'P_(1,2)=t real, all other entries zero',
        'factor_derivative_rank':4,'factor_derivative_kernel_dimension':2,
        'determinant_Hodge_preserved':True,'all_algebraic_witnesses_excluded':False,
        'fixed_period_replaced':False,'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Simultaneous Hodge locus of the six fixed divisor factors in the full Weil period chart.'}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-product-witness-first-order-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
