"""Formal K-class and Chern arithmetic; test coefficients do not assert cycle existence."""
from fractions import Fraction as Q
from pathlib import Path
import json
from check_hodge_semihomogeneous_readout_boundary import character,mul


def main():
    root=Path(__file__).resolve().parents[3]
    prior=json.loads((root/'research/voevodsky/results/hodge-semihomogeneous-readout-boundary-v1.json').read_text(encoding='utf-8'))
    assert prior['passed'] and not prior['all_algebraic_bundles_in_generated_class_claimed']
    one=[Q(1)]+[Q(0)]*6
    for k in (2,3,5):
        line=character(1,Q(-k))
        diff=[x-y for x,y in zip(one,line)]
        koszul=mul(mul(diff,diff),diff)
        assert koszul[:3]==[0,0,0] and koszul[3]==k**3
    # Formal placeholder for a leading codimension-three class; not a supplied cycle.
    z=[Q(7),Q(2),Q(-3)]
    ns=[2,6,8,10,5,12];ms=[1,2,3,4,5,6]
    sums=[sum(Q((-1)**i*ns[i]*ms[i]**j) for i in range(6)) for j in range(4)]
    k3=[z[0]+sums[3]/6,z[1],z[2]]
    ch1=sums[1];ch2=-sums[2]/2
    c3=[2*k3[0]-ch1*ch2+ch1**3/6,2*k3[1],2*k3[2]]
    expected=[2*z[0]+sums[3]/3+sums[1]*sums[2]/2+sums[1]**3/6,2*z[1],2*z[2]]
    assert c3==expected and k3[1:]==z[1:]
    for d in (3,6):
        presentation=sum(Q((-1)**i*ns[i]*(-ms[i])**3,6) for i in range(d))
        terminal=[(-1)**d*(z[0]-presentation),(-1)**d*z[1],(-1)**d*z[2]]
        recovered=[presentation+(-1)**d*terminal[0],(-1)**d*terminal[1],(-1)**d*terminal[2]]
        assert recovered==z and terminal[1:]==[(-1)**d*x for x in z[1:]]
    result={'passed':True,'classification':'unknown_cycle_readout_retained_in_terminal_vector_bundle',
        'safe_number_of_ample_twist_presentations':6,'terminal_sign':1,
        'terminal_ch3':'[Z] + S3 e^3/6','terminal_c3_Weil_readout_factor':2,
        'terminal_bundle_assumed_semihomogeneous_or_line_generated':False,
        'complete_intersection_Koszul_terminal_step':3,'complete_intersection_terminal_sign':-1,
        'arbitrary_input_cycle_with_nonzero_Weil_readout_supplied':False,
        'reduction_claimed_as_new_universal_obstruction':False,
        'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Explicit degree-three rational Adams projector and divisor subtraction on supplied K-classes.'}
    (root/'research/voevodsky/results/hodge-cycle-sheaf-terminal-syzygy-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
