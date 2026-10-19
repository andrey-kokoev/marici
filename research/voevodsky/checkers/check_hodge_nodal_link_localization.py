"""Link Gysin ranks and typed local-to-global fixtures, not actual global ranks."""
from math import comb
from pathlib import Path
import json
from check_hodge_deligne_lift_image import rank


def link_betti(n):
    base=lambda q:int(q in (0,n))
    # Euler class of TS^n is nonzero precisely for even n (over Q).
    e_rank=lambda source:int(n%2==0 and source==0)
    return {q:base(q)-e_rank(q-n)+base(q-n+1)-e_rank(q-n+1)
            for q in range(2*n)}


def matmul(A,B):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]


def main():
    link={q:b for q,b in link_betti(5).items() if b}
    assert link=={0:1,4:1,5:1,9:1}
    local={q+1:b for q,b in link.items() if q>0}
    assert local=={5:1,6:1,10:1}
    # Parity control: discarding the Euler map would give wrong extra groups.
    assert {q:b for q,b in link_betti(4).items() if b}=={0:1,7:1}
    inclusion=[[1],[0],[0]]
    residue=[[0,1,0],[0,0,1],[0,1,1]]
    gamma=[[1,1,-1]]
    phi=[[1,0,0],[0,1,0]]
    ambient_quotient=[[0,1]]
    assert matmul(residue,inclusion)==[[0],[0],[0]]
    assert matmul(gamma,residue)==[[0,0,0]]
    assert 3-rank(residue)==rank(inclusion)==1
    assert rank(residue)==3-rank(gamma)==2
    assert matmul(ambient_quotient,matmul(phi,inclusion))==[[0]]
    # A genuine nonzero residue in the fixture is killed in the ambient quotient.
    h=[[0],[0],[1]]
    assert matmul(residue,h)==[[0],[1],[1]]
    assert matmul(ambient_quotient,matmul(phi,h))==[[0]]
    assert matmul(ambient_quotient,matmul(phi,[[0],[1],[0]]))==[[1]]
    assert (comb(12,4),comb(12,6),comb(12,6)-comb(12,4))==(495,924,429)
    result={'passed':True,'classification':'nodal_local_terms_require_two_global_maps',
        'node_link_betti':link,'node_local_cohomology_ranks':local,
        'ambient_primitive_quotient_dimension':429,
        'fixture_local_rank':3,'fixture_global_residue_rank':2,'fixture_extra_ambient_rank':1,
        'actual_gamma_or_psi_computed':False,'alpha_support_membership_decided':False,
        'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Local residue of the known algebraic threefold at each envelope node.'}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-nodal-link-localization-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
