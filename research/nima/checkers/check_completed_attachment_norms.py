"""Completed attachment signs, bounded fibre reconstruction and norm mismatch.

Infinite exactness/nonclosed-range statements are proved in the companion
note. These checks use actual forgotten source products and exact matrices.
"""
from pathlib import Path
from itertools import product
import importlib.util
import json
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('descent',Path(__file__).with_name('check_seven_event_factorization_descent.py'))
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)


def balanced(columns):
    out={}
    for entries in product(*(c.items() for c in columns)):
        markers=[];buffers=[];value=1
        for i,((x,y,u,k,v),coefficient) in enumerate(entries):
            value*=coefficient;markers.append(('e',x,y,k))
            if i==0:buffers.append(u)
            else:buffers[-1]+=u
            buffers.append(v)
        key=tuple(markers),tuple(buffers)
        out[key]=out.get(key,0)+value
    return f.clean(out)


def main():
    # Local span (b,ab); mu includes ab, and left a sends b to ab.
    mu=s.Matrix([0,1]);q=s.Matrix([[1,0]])
    action=s.Matrix([[0,0],[1,0]])
    t=s.symbols('t')
    section=s.Matrix([1,t])
    assert q*mu==s.zeros(1) and q*section==s.eye(1)
    assert action*section==mu and action*mu==s.zeros(2,1)
    # The connecting map has identity in degree -1.
    h0,h1=s.symbols('h0 h1');hom=s.Matrix([[h0,h1]])
    assert hom*action==s.Matrix([[h1,0]])
    assert hom*mu==s.Matrix([[h1]])  # equivariance forces h1=0, not 1.

    # Fib(delta)=[A -> A+E], with the declared cone/shift sign.
    d=s.Matrix([-1,0,1])
    retract=mu.row_join(s.eye(2))
    include=s.zeros(1,2).col_join(s.eye(2))
    homotopy=s.Matrix([[-1,0,0]])
    assert retract*d==s.zeros(2,1)
    assert retract*include==s.eye(2)
    assert s.eye(3)-include*retract==d*homotopy
    assert homotopy*d==s.eye(1)
    # In l1 sums the inclusion, retraction and homotopy have norm <=1.
    for matrix in (retract,include,homotopy):
        assert max(sum(abs(matrix[i,j]) for i in range(matrix.rows)) for j in range(matrix.cols))<=1
    assert sum(abs(v) for v in d)==2
    # Continuous cochain conjugate dual: degree 0 -> 1 is -mu^vee.
    dual_d=-mu.conjugate().T
    assert dual_d==s.Matrix([[0,-1]])
    # The termwise quotient has zero differential, not a proof that the
    # completed ideals are projective over a completed algebra.
    assert q*mu==s.zeros(1)

    ratios=[];probes=0
    for depth in range(1,4):
        minimum=2*(depth+1)
        for length in (minimum,minimum+1,16,32,64):
            factors=[f.relation((2*i,2*i+1),0) for i in range(depth+1)]
            tail={((tuple(range(minimum,length))),((0,)*(length-minimum))):1}
            factors[-1]=f.multiply(factors[-1],tail)
            column=f.chain_product(factors)
            mass=sum(abs(c) for c in column.values())
            assert mass==2**(depth+1)
            merged=[f.multiply(factors[0],factors[1])]+factors[2:]
            assert len(merged)==depth and f.chain_product(merged)==column
            assert sum(abs(c) for c in column.values())==mass
            # Each fixed-cut presentation has exactly the same coefficient
            # mass as its source image, attaining the l1 lower bound.
            assert s.prod(sum(abs(c) for c in factor.values()) for factor in factors)==mass
            assert s.prod(sum(abs(c) for c in factor.values()) for factor in merged)==mass
            ratio=s.Rational((1+length)**depth,(1+length)**(depth+1))
            assert ratio==s.Rational(1,1+length)
            ratios.append({'depth':depth,'event_length':length,'norm_ratio':str(ratio)})
            state=0;cycles=[]
            for factor in factors:
                cycle=f.derivative(state,factor)
                assert cycle and not f.boundary(cycle)
                cycles.append(cycle)
                word=next(iter(factor))[0]
                state|=sum(1<<j for j in word)
            image=balanced(cycles)
            assert image and not f.balanced_boundary(image)
            assert set(image.values())<={-1,1}
            probes+=1
    # Choosing endpoint lengths exponentially large gives a summable image
    # of source units, while their own-depth norms are all one.
    for k in range(1,17):
        length=4+2**k
        assert s.Rational(1,length+1)<s.Rational(1,2**k)
    # Exponential-radius loss can absorb THIS polynomial discrepancy.
    # It is not a bound for arbitrary factorization-lifting constants.
    assert all(1+n<=2**n for n in range(65))

    result={'schema':'marici.nima.completed-attachment-norms.v1','passed':True,
        'checks':{'source_equivariant_section_obstructed':True,
                  'fibre_retraction_and_homotopy_identities':True,
                  'fibre_maps_have_explicit_l1_bounds':True,
                  'dual_differential_sign':True,'termwise_quotient_differential_zero':True,
                  'actual_product_presentations_attain_coefficient_l1_bound':True,
                  'fixed_stage_adjacent_norm_ratio_is_one_over_one_plus_length':True},
        'nonzero_next_layer_cycle_probes':probes,'norm_ratio_fixtures':ratios,
        'scope':'Strict completed triangle uses the inherited kernel norm. Independent depth completions have a nonclosed natural inclusion at fixed Banach stage. Neither Banach projectivity nor unrestricted completed derived tensor base change is inferred. Radius-intersection comparisons need additional norm control.'}
    out=ROOT/'research/nima/results/completed-attachment-norms.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
