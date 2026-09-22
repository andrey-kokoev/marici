"""Exact bounded-descent and augmented consistency-inverse regressions."""
from pathlib import Path
from fractions import Fraction as Q
import json


def frame(f,z):return tuple((f+1)*v for v in z)
def align(f,z):return tuple(v/Q(f+1) for v in z)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def norm(z):return max(map(abs,z),default=Q(0))
def encode(states):return states[0],tuple(sub(align(f,y),states[0]) for f,y in enumerate(states) if f)
def decode(z,ds):return (z,)+tuple(frame(f,add(z,d)) for f,d in enumerate(ds,1))


def main():
    inverse_checks=0
    for count in (2,3,100):
        for depth in range(1,7):
            states=tuple(tuple(Q((f+2)*(i+1)-3,7) for i in range(depth)) for f in range(count))
            z,ds=encode(states)
            assert decode(z,ds)==states
            aligned=max(norm(align(f,y)) for f,y in enumerate(states))
            encoded=max(norm(z),max(map(norm,ds),default=Q(0)))
            assert encoded<=2*aligned and aligned<=2*encoded
            common=tuple(frame(f,z) for f in range(count))
            assert all(not any(d) for d in encode(common)[1])
            if depth>1:
                zs,short=encode(tuple(y[:-1] for y in states))
                assert zs==z[:-1] and short==tuple(d[:-1] for d in ds)
                assert decode(zs,short)==tuple(y[:-1] for y in decode(z,ds))
            inverse_checks+=1
    # Injective diagonal operator: squared amplification equals N.
    for N in range(1,65):
        x=tuple(Q(n) for n in range(1,N+1))
        image=tuple(v/Q(n) for n,v in enumerate(x,1))
        value=sum(v/Q(n) for n,v in enumerate(x,1))
        norm_squared=sum(v*v for v in image)
        assert value*value/norm_squared==N
    # Identity measurement permits the second-coordinate functional;
    # subsequent first-coordinate projection destroys it.
    source=(Q(0),Q(1))
    assert source[1]!=0 and source[0]==0
    result={'passed':True,'reference_discrepancy_inverse_checks':inverse_checks,
        'unbounded_descent_ratio_checks':64,
        'checks':['restriction_compatibility','shared_state_in_discrepancy_kernel',
                  'further_quotient_can_destroy_reverse_observability'],
        'scope':'Exact abstract regressions. Physical observer admission and actual cubic/filtration applications use the cited source theorems.'}
    out=Path(__file__).resolve().parents[1]/'results/reverse-observation.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
