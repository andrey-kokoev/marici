"""Weighted terminal lifts: exact source paths and a labelled tail model.

The exponential density is a test model, not a numerical theta sample.
Actual theta tail dominance is proved analytically in the companion note.
"""
from pathlib import Path
from itertools import permutations,product
from collections import defaultdict
from fractions import Fraction as Q
import importlib.util
import json
import sympy as s

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('lift',HERE/'check_controlled_ideal_factorization_lift.py')
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
f=g.f
PRIMES=(2,3,5,7,11,13,17,19)


def retract(start,column):return g.section(g.bar_column(start,column))


def gamma_squared(word,marks,background=1):
    # h(x)=exp(-x), arithmetic endpoints 2*background*product(primes).
    point=2*background;out=Q(1)
    for j,keep in zip(word,marks):
        target=point*PRIMES[j]
        if keep:out*=Q(1,2*point**2)-Q(1,2*target**2)
        point=target
    return out


def retained_starts(word,marks):
    point=2;out=[]
    for j,keep in zip(word,marks):
        if keep:out.append(point)
        point*=PRIMES[j]
    return out


def H(column):
    out=defaultdict(int)
    for (word,marks),c in column.items():
        for i,j in enumerate(word):
            before=retract(0,{(word[:i],marks[:i]):1})
            bracket=defaultdict(int,f.multiply(before,{((j,),(marks[i],)):1}))
            g.add(bracket,retract(0,{(word[:i+1],marks[:i+1]):1}),-1)
            for left,value in f.clean(bracket).items():
                out[left,(word[i+1:],marks[i+1:])]+=c*value
    return f.clean(out)


def project_factor(column,which):
    out=defaultdict(int)
    for (left,right),value in column.items():
        start=0 if which==0 else sum(1<<j for j in left[0])
        old=left if which==0 else right
        for new,c in retract(start,{old:1}).items():
            key=(new,right) if which==0 else (left,new)
            out[key]+=value*c
    return f.clean(out)


def main():
    q=s.symbols('q',positive=True)
    logder=s.Rational(9,2)+6/(2*q-3)-2*q
    assert s.simplify(5-2*q-logder-(2*q-15)/(2*(2*q-3)))==0
    t=s.symbols('t',nonnegative=True)
    assert s.simplify((2*q-15).subs(q,12+t))==9+2*t
    words=outputs=weights=0
    for n in range(1,5):
        for word in permutations(range(n)):
            for marks in product((0,1),repeat=n):
                column=retract(0,{(word,marks):1})
                assert sum(abs(c) for c in column.values())<=2**n
                old_starts=retained_starts(word,marks)
                for (newword,newmarks),coefficient in column.items():
                    assert sum(newmarks)==sum(marks)
                    assert all(a>=b for a,b in zip(retained_starts(newword,newmarks),old_starts))
                    for background in (1,11,101):
                        old=gamma_squared(word,marks,background)
                        new=gamma_squared(newword,newmarks,background)
                        assert new<=Q(4,3)**sum(marks)*old
                        weights+=1
                    outputs+=1
                words+=1
    products=0
    for left_kind,right_kind,keep in product((0,1),repeat=3):
        a=f.relation((0,1),left_kind);c=f.relation((3,4),right_kind)
        middle={((2,),(keep,)):1}
        z=f.chain_product([a,middle,c]);lift=H(z)
        reconstructed=defaultdict(int)
        for (left,right),value in lift.items():
            reconstructed[left[0]+right[0],left[1]+right[1]]+=value
        assert f.clean(reconstructed)==z
        assert not project_factor(lift,0)
        assert not project_factor(lift,1)
        products+=1
    result={'passed':True,'terminal_retraction_paths':words,
        'later_start_output_checks':outputs,'exact_model_weight_checks':weights,
        'two_factor_reconstruction_and_membership_checks':products,
        'scope':'Model weights test the lifting mechanism. The actual theta constant follows from positivity, logarithmic derivative control and the minimum prime-event length.'}
    out=HERE.parent/'results/actual-letter-factorization-lift.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
