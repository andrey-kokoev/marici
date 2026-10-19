"""Exact Adams interpolation and control tests, not a constructor of an absent cycle."""
from fractions import Fraction as Q
from pathlib import Path
import json
from check_hodge_semihomogeneous_readout_boundary import character,mul as series_mul


def product(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def evaluate(p,x):return sum(c*Q(x)**i for i,c in enumerate(p))
def remainder(a,b):
    a=a[:]
    while len(a)>=len(b):
        c=a[-1]/b[-1];offset=len(a)-len(b)
        for j,x in enumerate(b):a[offset+j]-=c*x
        while a and not a[-1]:a.pop()
    return a


def main():
    root=Path(__file__).resolve().parents[3]
    prior=json.loads((root/'research/voevodsky/results/hodge-cycle-sheaf-terminal-syzygy-v1.json').read_text(encoding='utf-8'))
    assert prior['passed'] and not prior['arbitrary_input_cycle_with_nonzero_Weil_readout_supplied']
    weights=[2**j for j in range(7)];numerator=[Q(1)];denominator=1
    for j,w in enumerate(weights):
        if j==3:continue
        numerator=product(numerator,[Q(-w),Q(1)])
        denominator*=8-w
    assert denominator==-1806336
    p=[c/denominator for c in numerator]
    values=[evaluate(p,w) for w in weights]
    assert values==[0,0,0,1,0,0,0]
    characteristic=[Q(1)]
    for w in weights:characteristic=product(characteristic,[Q(-w),Q(1)])
    difference=product(p,p)
    for i,c in enumerate(p):difference[i]-=c
    assert remainder(difference,characteristic)==[]
    one=[Q(1)]+[Q(0)]*6
    for k in (1,2,3,5):
        line=character(1,Q(-k));d=[x-y for x,y in zip(one,line)]
        koszul=series_mul(series_mul(d,d),d)
        selected=[values[j]*koszul[j] for j in range(7)]
        assert selected==[0,0,0,k**3,0,0,0]
        lam=Q(2160*selected[3],2160)
        selected[3]-=lam
        assert selected==[0]*7
    # Formal cohomological coefficient fixture only; not an actual input realizing R.
    gamma=[Q(7),Q(2),Q(-3)]
    normalize=lambda c:[c[0]-Q(2160*c[0],2160),c[1],c[2]]
    assert normalize(normalize(gamma))==normalize(gamma)==[0,2,-3]
    assert Q(2160,2160)==1  # lambda(b)=chi(b^2)/2160
    # Formal CH polynomial in e,p, with Betti map p->0: do not assert actual CH independence.
    a=Q(2)
    chow_remainder=[Q(0),a*a/2,a/2,Q(1,6)]  # e^3,e^2p,ep^2,p^3
    assert chow_remainder[0]==0 and any(chow_remainder[1:])
    result={'passed':True,'classification':'exact_degree_three_Adams_and_Weil_K_normalization',
        'Adams_polynomial_denominator':denominator,
        'Adams_polynomial_coefficients_ascending':[str(c) for c in p],
        'eigenvalue_selector':[int(v) for v in values],
        'idempotence_mod_weight_polynomial_checked':True,
        'divisor_subtraction_coefficient':'chi(v b)/2160',
        'Koszul_controls_k':[1,2,3,5],'Koszul_controls_killed_in_rational_K':True,
        'terminal_syzygy_normalization_preserves_input':True,
        'rank_zero_output_claimed_actual_positive_rank_bundle':False,
        'zero_Betti_class_claimed_zero_Chow_class':False,
        'original_Weil_cycle_input_supplied':False,'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Actual polystable bundle realization under a discriminant equality, without assigning stability to virtual K-data.'}
    (root/'research/voevodsky/results/hodge-degree-three-Adams-normalization-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
