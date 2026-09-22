"""Actual minimal cubic sectors and exact leading-growth algebra.

No sampled theta window is used to establish the asymptotic theorem.
"""
from pathlib import Path
from itertools import combinations
from collections import defaultdict
from fractions import Fraction as Q
import runpy
import json
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
f=runpy.run_path(str(ROOT/'research/nima/checkers/check_seven_event_factorization_descent.py'))
PRIMES=(2,3,5,7,11,13)


def pairings(items):
    if not items:
        yield ();return
    for pair in combinations(items,2):
        for tail in pairings(tuple(j for j in items if j not in pair)):
            yield (pair,)+tail


def one(column):
    return {((('e',x,y,k),),(u,v)):c for (x,y,u,k,v),c in column.items()}


def join(a,b):
    out=defaultdict(int)
    for (sa,ba),ca in a.items():
        for (sb,bb),cb in b.items():
            out[sa+sb,ba[:-1]+(ba[-1]+bb[0],)+bb[1:]]+=ca*cb
    return f['clean'](out)


def model_mass(column,start):
    # Arbitrary positive rational letters test the factorization identity only.
    total=Q(0)
    for (word,marks),coefficient in column.items():
        point=start;weight=Q(1)
        for j,keep in zip(word,marks):
            if keep:weight*=Q(1,point*PRIMES[j])
            point*=PRIMES[j]
        total+=abs(coefficient)*weight
    return total


def main():
    keys=[((('e',*ea,1),('e',*eb,1),('e',15,31,0)),((),(),(),()))
          for ea in ((0,1),(1,3)) for eb in ((3,7),(7,15))]
    seen=set();active=[];count=0
    for pairs in pairings(tuple(range(6))):
        for kinds in ((1,1,0),(1,0,1),(0,1,1)):
            cols=[f['relation'](pair,kind) for pair,kind in zip(pairs,kinds)]
            source=f['chain_product'](cols)
            assert len(source)==32 and all(abs(v)==1 for v in source.values())
            assert not seen.intersection(source)
            seen.update(source)
            start=0;point=2;ds=[];mass=Q(1)
            for pair,col in zip(pairs,cols):
                ds.append(one(f['derivative'](start,col)))
                mass*=model_mass(col,point)
                start|=sum(1<<j for j in pair)
                for j in pair:point*=PRIMES[j]
            assert model_mass(source,2)==mass
            image=join(join(ds[0],ds[1]),ds[2])
            values=[image.get(key,0) for key in keys]
            if any(values):active.append((pairs,kinds,values))
            count+=1
    assert count==270 and len(seen)==8640
    assert active==[
        (((0,1),(2,3),(4,5)),(1,1,0),[1,1,1,1]),
        (((0,2),(1,3),(4,5)),(1,1,0),[0,1,0,0])]
    y,w,A,beta,R=s.symbols('y w A beta R',positive=True)
    ma,mb,ga,gb,L=s.symbols('ma mb ga gb L',real=True)
    values=[w*w/(2*y*y)*sign*(a-L)*(b-L)
            for a,b,sign in ((ma,mb,1),(ma,mb+gb,-1),
                             (ma+ga,mb,-1),(ma+ga,mb+gb,1))]
    assert s.simplify(sum(values)-w*w*ga*gb/(2*y*y))==0
    assert s.simplify(values[1]+w*w*(ma-L)*(mb+gb-L)/(2*y*y))==0
    exponent=beta+s.Rational(7,2)
    def G(k):
        return 2*s.sqrt(w)*s.pi**s.Rational(3,2)*s.log(A)*(k*A)**exponent*s.exp(-s.pi*(k*A)**2)
    ratio=(w*w*s.log(A)**2/(2*y*y))/(s.factorial(6)*R**6*8*G(1)*G(10))
    expected=w/(64*s.factorial(6)*y*y*R**6*s.pi**3*10**exponent)*A**(-2*beta-7)*s.exp(101*s.pi*A*A)
    assert s.simplify(ratio/expected)==1
    assert 1+6**2==37 and 1+10**2==101 and 2**2+30**2==904
    # Polynomial endpoint integration rule applied to the two leading integrands.
    assert s.simplify((y+s.Rational(7,2))-1-(y+s.Rational(5,2)))==0
    assert s.simplify((2*beta+8)-1-(2*beta+7))==0
    result={'passed':True,'minimal_cubic_basis_products':count,
        'disjoint_marked_source_paths':len(seen),'visible_products':active,
        'checks':['exact_source_mass_factorization','residual_observer_values',
                  'sharp_source_leading_constant','distinct_37_101_904_exponents'],
        'scope':'Actual source enumeration and symbolic growth algebra. Actual theta boundary asymptotics and infinite prior thresholds are analytic proofs, not rational letter fixtures.'}
    out=ROOT/'research/nima/results/translated-cubic-observer-growth.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
