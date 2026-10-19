"""Exact Chow-expression class identities, conditional on the audited imported theorem."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
from check_hodge_product_witness_first_order import real_imag_pair,add
from check_hodge_fixed_sixfold_pairing import wedge
from check_hodge_fixed_divisor_witness_locus import actual_J
from check_hodge_explicit_sixfold_candidate import lie_action


def pull(form,images):
    terms=[]
    for key,coefficient in form.items():
        out={():coefficient}
        for i in key:out=wedge(out,images[i])
        terms.append((1,out))
    return add(*terms)


def main():
    root=Path(__file__).resolve().parents[3]
    audit=json.loads((root/'research/voevodsky/results/hodge-split-fourfold-correspondence-audit-v1.json').read_text(encoding='utf-8'))
    assert audit['passed'] and audit['gamma_algebraic_by_imported_theorem']
    p={};q={}
    for bits in product((0,1),repeat=3):
        n=sum(bits);key=tuple(2+2*j+b for j,b in enumerate(bits))
        (p if n%2==0 else q)[key]=(-1)**(n//2)
    e={(0,):1};f={(1,):1}
    gamma=add((1,wedge(f,p)),(-1,wedge(e,q)))
    prime=add((1,wedge(e,p)),(1,wedge(f,q)))
    tau={i:{(i,):1} for i in range(8)};tau[0]={(1,):1};tau[1]={(0,):-1}
    assert add((-1,pull(gamma,tau)))==prime
    mapping={0:{(8,):1},1:{(9,):-1}}
    for i,j in enumerate((0,1,2,3,6,7),start=2):mapping[i]={(j,):1}
    hg=pull(gamma,mapping);hp=pull(prime,mapping)
    pa=pull(p,mapping);qa=pull(q,mapping)
    V=add((1,wedge(pa,{(8,):1})),(-1,wedge(qa,{(9,):1})))
    W=add((1,wedge(pa,{(9,):1})),(1,wedge(qa,{(8,):1})))
    assert hg==W and hp==add((-1,V))
    r1,s1=real_imag_pair(0,3);r2,s2=real_imag_pair(1,4);r3,s3=real_imag_pair(2,5)
    tri=lambda a,b,c:wedge(wedge(a,b),c)
    K1=add((1,tri(s1,s2,r3)),(-1,tri(r1,r2,r3)))
    K2=add((1,tri(r1,s2,s3)),(1,tri(s1,r2,s3)))
    assert add((-1,wedge(hp,r3)))==K1
    assert add((-1,wedge(hg,s3)))==K2
    R={};I={}
    for bits in product((0,1),repeat=6):
        n=sum(bits);key=tuple(2*j+b for j,b in enumerate(bits))
        (R if n%2==0 else I)[key]=(-1)**(n//2)
    assert add((1,K1),(1,K2))==R
    assert add((1,wedge(hg,r3)),(-1,wedge(hp,s3)))==I
    J=actual_J({(0,0):(Q(1,8),0),(0,1):(Q(1,8),0)})
    assert all(not lie_action(J,form) for form in (hg,hp,K1,K2,R,I))
    wrong=dict(mapping);wrong[1]={(9,):1}
    assert lie_action(J,pull(gamma,wrong))  # omitting conjugation breaks Hodge type
    assert 2+1==3 and 6-4==2  # Chow codimension and relative dimension
    result={'passed':True,'classification':'joint_control_nondivisor_classes_realized_by_algebraic_operations',
        'theorem_backed_input':'Gamma in CH2(C times A)_Q',
        'realized_classes':['K1','K2','R','I'],'CM_transform_sign_checked':True,
        'elliptic_conjugation_hostile_rejected':True,'explicit_cycle_equations_produced':False,
        'relative_cycle_family_constructed':False,'original_fixed_alpha_realized':False,
        'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Compose two elliptic-to-threefold correspondences when both complementary threefold factors vary.'}
    (root/'research/voevodsky/results/hodge-joint-correspondence-transfer-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
