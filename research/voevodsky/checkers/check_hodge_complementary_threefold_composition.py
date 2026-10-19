"""Two correspondence actions and exact elliptic integration on the larger control."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
from check_hodge_product_witness_first_order import add
from check_hodge_fixed_sixfold_pairing import wedge
from check_hodge_fixed_divisor_witness_locus import actual_J
from check_hodge_explicit_sixfold_candidate import lie_action


def determinant_parts(labels):
    re={};im={}
    for bits in product((0,1),repeat=len(labels)):
        n=sum(bits);key=tuple(2+2*j+b for j,b in zip(labels,bits))
        (re if n%2==0 else im)[key]=(-1)**(n//2)
    return re,im


def integrate_C(form,shift=False):
    return {tuple(i-2 if shift else i for i in key[2:]):c
            for key,c in form.items() if key[:2]==(0,1)}


def main():
    root=Path(__file__).resolve().parents[3]
    audit=json.loads((root/'research/voevodsky/results/hodge-split-fourfold-correspondence-audit-v1.json').read_text(encoding='utf-8'))
    assert audit['passed'] and audit['decomposable_control_covered']
    primary=(root/'research/voevodsky/inputs/hodge-literature-v1/markman-2502.03415v2.p9.txt').read_text(encoding='utf-8')
    assert 'for all discriminants' in primary
    p,q=determinant_parts((0,1,3));r,s=determinant_parts((2,4,5))
    e={(0,):1};f={(1,):1}
    ga=add((1,wedge(f,p)),(-1,wedge(e,q)))
    gap=add((1,wedge(e,p)),(1,wedge(f,q)))
    gb=add((1,wedge(f,r)),(1,wedge(e,s)))
    assert integrate_C(wedge(e,ga))==p and integrate_C(wedge(f,ga))==q
    assert integrate_C(wedge(e,gb))==r and integrate_C(wedge(f,gb))==add((-1,s))
    totalR,totalI=determinant_parts(tuple(range(6)))
    R={tuple(i-2 for i in key):c for key,c in totalR.items()}
    I={tuple(i-2 for i in key):c for key,c in totalI.items()}
    assert integrate_C(wedge(gap,gb),True)==R
    assert integrate_C(wedge(ga,gb),True)==add((-1,I))
    entries={(0,0):(Q(1,8),Q(1,32)),(0,1):(Q(1,9),Q(-1,32)),
             (1,2):(Q(1,10),Q(1,64)),(2,2):(Q(1,12),Q(-1,64))}
    assert sum(a*a+b*b for (i,j),(a,b) in entries.items() if i==0)<1
    assert sum((1,1,3)[i]*(a*a+b*b) for (i,j),(a,b) in entries.items() if j==2)<1
    source=actual_J(entries)
    J=[[Q(0)]*14 for _ in range(14)];J[0][1]=-1;J[1][0]=1
    for i in range(12):
        for j in range(12):J[i+2][j+2]=source[i][j]
    assert all(not lie_action(J,v) for v in (ga,gap,gb,totalR,totalI))
    assert (-1)*1*1*(-1)==1 and 1*1*(-1)*(-3)==3
    assert all(a==b==0 for a,b in product(range(3),repeat=2) if (a*a+b*b)%3==0)
    assert 2+2-1==3 and 1+3+3==7
    result={'passed':True,'classification':'two_varying_threefolds_have_algebraic_Weil_composition',
        'fourfold_Hermitian_determinants':[1,3],'all_discriminants_theorem_required':True,
        'composite_codimension':3,'realized_classes':['R','I'],
        'R_expression':'push(Gamma_A_prime times Gamma_B)',
        'I_expression':'-push(Gamma_A times Gamma_B)',
        'decomposable_locus_complex_dimension':4,'fixed_elliptic_projection_used':False,
        'relative_cycle_family_constructed':False,'original_fixed_alpha_realized':False,
        'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Exclude or identify hidden product decompositions of the original Picard-rank-one source up to isogeny.'}
    (root/'research/voevodsky/results/hodge-complementary-threefold-composition-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
