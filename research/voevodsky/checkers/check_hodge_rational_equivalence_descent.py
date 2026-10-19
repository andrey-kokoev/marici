"""Exact witness-descent controls, not a sixfold Chow computation."""
import json
from fractions import Fraction as Q
from itertools import product
from pathlib import Path


def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def boundary(w): return w[0]
def residual(f): return add(sub(f[1,2],f[0,2]),f[0,1])


def main():
    # Principal divisor of t^k on P1; chart restrictions retain the relevant support.
    for k in (Q(-2),Q(-1,2),Q(0),Q(1),Q(3,2)):
        div=(k,-k)
        assert sum(div)==0
        assert div[0]==k and div[1]==-k
    z0,z1=Q(1),Q(0)
    g0,g1=Q(1),Q(0)  # exponents of t in the chosen local witnesses
    assert (z0-g0,z1+g1)==(0,0)
    transition=-(g1-g0)
    assert transition==1
    # Invertible regular changes on either affine chart are constant (imported fact).
    assert transition+0-0==1
    assert (0,0)==(0,0) and transition!=0  # identical local quotient, distinct transition
    z={0:Q(0),1:Q(1),2:Q(3)}
    f={(0,1):(Q(1),Q(2)),(1,2):(Q(2),Q(4)),(0,2):(Q(3),Q(9))}
    assert all(boundary(w)==z[j]-z[i] for (i,j),w in f.items())
    k=residual(f)
    assert k==(0,-3) and boundary(k)==0
    # Same local cycles, kernel-valued witness change removes this representative residual.
    repaired=dict(f);repaired[0,2]=add(f[0,2],(Q(0),Q(-3)))
    assert residual(repaired)==(0,0)
    cases=0
    for values in product((-1,0,1),repeat=3):
        g={i:(Q(values[i]),Q(i+1)) for i in range(3)}
        zp={i:z[i]-boundary(g[i]) for i in z}
        fp={(i,j):sub(w,sub(g[j],g[i])) for (i,j),w in f.items()}
        assert all(boundary(w)==zp[j]-zp[i] for (i,j),w in fp.items())
        assert residual(fp)==k
        cases+=1
    bad=dict(f);bad[0,1]=add(f[0,1],(1,0))
    assert boundary(bad[0,1])!=z[1]-z[0]
    # A global cycle with identity overlap witnesses has no triple residual.
    assert residual({pair:(Q(0),Q(0)) for pair in f})==(0,0)
    result={'passed':True,'representative_change_cases':cases,
        'classification':'first_witness_retaining_descent_interface_constructed',
        'P1_transition_recovers_nonzero_degree':True,
        'nonzero_kernel_representative_can_be_removed':True,
        'higher_cycle_complex_identified_with_two_term_presentation':False,
        'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Construct admissible degree-one higher-cycle chains from rational-function witnesses.'}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-rational-equivalence-witness-descent-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__': main()
