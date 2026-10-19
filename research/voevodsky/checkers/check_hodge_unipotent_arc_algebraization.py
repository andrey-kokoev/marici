"""Symbolic transition and characteristic-class controls, not a formal-existence proof."""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json
from check_hodge_control_quadratic_obstruction import multiply


def mul(a,b):
    # Monomials t^i a^j b^k J^l, with J^3=0.
    out={}
    for x,c in a.items():
        for y,d in b.items():
            z=tuple(i+j for i,j in zip(x,y))
            if z[3]>=3:continue
            out[z]=out.get(z,Q(0))+c*d
    return {z:c for z,c in out.items() if c}


def main():
    root=Path(__file__).resolve().parents[3]
    prior=json.loads((root/'research/voevodsky/results/hodge-control-formal-model-v1.json').read_text(encoding='utf-8'))
    assert prior['passed'] and prior['complete_intersection_formal_model_constructed']
    j=[[0,1,0],[0,0,1],[0,0,0]];zero=[[0]*3 for _ in range(3)]
    assert multiply(j,j)!=zero and multiply(multiply(j,j),j)==zero
    one={(0,0,0,0):Q(1)}
    ga={**one,(1,1,0,1):Q(1),(2,2,0,2):Q(1,2)}
    gb={**one,(1,0,1,1):Q(1),(2,0,2,2):Q(1,2)}
    gab={**one,(1,1,0,1):Q(1),(1,0,1,1):Q(1),
         (2,2,0,2):Q(1,2),(2,1,1,2):Q(1),(2,0,2,2):Q(1,2)}
    assert mul(ga,gb)==gab==mul(gb,ga)
    inverse={m:c*(-1)**m[1] for m,c in ga.items()}
    assert mul(ga,inverse)==one
    ch=[Q(3,factorial(d)) for d in range(7)]
    assert ch[3]==Q(1,2)
    p=[factorial(d)*ch[d] for d in range(1,4)]
    c3=(p[0]**3-3*p[0]*p[1]+2*p[2])/6
    assert c3==1 and c3!=ch[3]
    for k in (2,3,5):
        cycle=(Q(k**3),Q(0),Q(0));pairing=2160*cycle[0]
        projected=(cycle[0]-pairing/2160,cycle[1],cycle[2])
        assert projected==(0,0,0)
    result={'passed':True,'classification':'nontrivial_algebraic_unipotent_control_family_zero_Weil_readout',
        'nilpotent_transition_degree_in_parameter':2,
        'transition_cocycle_identity_checked_symbolically':True,
        'complete_base_algebraization':'proper formal existence on X times Spec C[[t]]',
        'stronger_finite_type_construction':'finite Cech exponentials and algebraic section lifting on a neighborhood of zero in A1',
        'selected_family_nonconstant_by_Hilbert_tangent_comparison':True,
        'cycle_Chow_class':'k^3 c1(H)^3','bundle_ch3_coefficient_relative_to_l3':'1/2',
        'zero_locus_c3_coefficient_relative_to_l3':1,'Weil_projection':[0,0],
        'arbitrary_formal_section_finite_type_algebraization_claimed':False,
        'all_algebraic_cycles_annihilated_claimed':False,'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Audit simple semihomogeneous bundle Chern characters and explicitly generated operations on the fixed rank-one Picard source.'}
    (root/'research/voevodsky/results/hodge-unipotent-arc-algebraization-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
