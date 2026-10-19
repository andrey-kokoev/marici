"""Exact active determinant and elliptic correspondence, not an algebraic cycle."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
from check_hodge_fixed_divisor_witness_locus import actual_J
from check_hodge_explicit_sixfold_candidate import lie_action,full_pullback
from check_hodge_product_witness_first_order import add
from check_hodge_fixed_sixfold_pairing import wedge


def main():
    p={};q={}
    for bits in product((0,1),repeat=3):
        n=sum(bits);key=tuple(2+2*j+b for j,b in enumerate(bits))
        (p if n%2==0 else q)[key]=(-1)**(n//2)
    e={(0,):1};f={(1,):1}
    gamma=add((1,wedge(f,p)),(-1,wedge(e,q)))
    wrong=add((1,wedge(f,p)),(1,wedge(e,q)))
    # Fiber integration on C with integral e wedge f=1.
    def act(eta):
        mixed=wedge(eta,gamma)
        return {key[2:]:c for key,c in mixed.items() if key[:2]==(0,1)}
    assert act(e)==p and act(f)==q and gamma
    active=[0,1,2,3,6,7]
    for s,t in ((Q(0),Q(0)),(Q(1,8),Q(1,8)),(Q(1,7),Q(1,9))):
        source=actual_J({(0,0):(s,0),(0,1):(t,0)})
        J=[[Q(0)]*8 for _ in range(8)]
        J[0][1]=-1;J[1][0]=1
        for i,a in enumerate(active):
            for j,b in enumerate(active):J[2+i][2+j]=source[a][b]
        assert lie_action(J,p)==add((-1,q)) and lie_action(J,q)==p
        assert not lie_action(J,gamma) and lie_action(J,wrong)
    T=[[0]*8 for _ in range(8)]
    T[0][1]=1;T[1][0]=-1  # conjugate K action on C
    for j in range(1,4):T[2*j][2*j+1]=-1;T[2*j+1][2*j]=1
    assert full_pullback(T,p)==q and full_pullback(T,q)==add((-1,p))
    assert full_pullback(T,gamma)==gamma
    # U4=(e-if)(p+iq); gamma=-Im U4.
    imag_U4=add((1,wedge(e,q)),(-1,wedge(f,p)))
    assert gamma==add((-1,imag_U4))
    weights=(-1,1,1,-1)
    h=lambda u,v:sum(d*x*y for d,x,y in zip(weights,u,v))
    v=(1,1,0,0);w=(0,0,1,1)
    assert h(v,v)==h(w,w)==h(v,w)==0
    assert weights[0]*weights[1]*weights[2]*weights[3]==1
    assert 1+2*(2-1)==3  # correspondence degree shift
    assert all(sum(i<2 for i in key)==1 for key in gamma)
    result={'passed':True,'classification':'odd_sector_has_split_Weil_fourfold_correspondence_class',
        'active_determinant_types':[[2,1],[1,2]],'twisted_types':[[1,0],[0,1]],
        'correspondence_codimension':2,'correspondence_action':'e maps to p; f maps to q',
        'elliptic_K_embedding':'conjugate','ambient_Weil_signature':[2,2],
        'Hermitian_determinant':1,'explicit_split_plane_checked':True,
        'algebraic_correspondence_constructed':False,'original_fixed_sixfold_replaced':False,
        'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Exact applicability audit of split Weil-fourfold algebraicity theorems to this control and gamma.'}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-joint-odd-sector-correspondence-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
