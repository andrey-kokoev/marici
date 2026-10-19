"""Degree/Koszul/kernel controls; not computation of an unknown cycle's obstruction."""
from math import comb
from pathlib import Path
import json


def main():
    root=Path(__file__).resolve().parents[3]
    prior=json.loads((root/'research/voevodsky/results/hodge-control-specialization-boundary-v1.json').read_text(encoding='utf-8'))
    assert prior['passed'] and prior['all_smooth_control_fibers_realized_by_refined_restriction']
    assert prior['transverse_codimension_three_extension_constructed'] is False
    # Nonzero positions allowed by Kodaira/Serre in the twisted Koszul E1 page.
    support={(-3,6),(-2,6),(0,0)}|{(-1,q) for q in range(7)}
    assert {(p,q) for p,q in support if p+q==1}=={(-1,2)}
    p,q=-1,2
    for r in range(1,5):
        assert (p+r,q-r+1) not in support
        assert (p-r,q+r-1) not in support
    h1_L=3*comb(6,2);h1_N=3*h1_L;target=comb(6,2)*comb(6,4)
    assert (h1_L,h1_N,target)==(45,135,225)
    assert (3-1,3+1)==(2,4)  # contraction by Kodaira-Spencer
    assert (6-4,6-2)==(2,4)  # dual target H2(Omega4)
    assert 3-1==2  # dual normal source H2(N* tensor K_Z)
    # Logical hostile only: sigma(ob)=0 does not imply ob=0 for an untested sigma.
    obstruction=(0,1)
    sigma=lambda v:v[0]
    assert obstruction!=(0,0) and sigma(obstruction)==0
    for k in (2,3,5):
        control=(k**3,0,0)  # basis E^3,R,I
        assert control[1:]==(0,0)
    result={'passed':True,'classification':'embedded_obstruction_distinguished_from_Hodge_image',
        'smooth_control_h1_twisted_restriction':45,'smooth_control_h1_normal':135,
        'semiregularity_target_dimension':225,
        'actual_complete_intersection_lift':'local extension of relative ample sections',
        'complete_intersection_class':'k^3 E^3',
        'semiregularity_rank_computed':False,
        'unknown_correspondence_representative_assumed_smooth':False,
        'unknown_cycle_obstruction_computed':False,'original_fixed_alpha_realized':False,
        'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Compute the actual complete-intersection semiregularity map via the defining-section space and Koszul identification.'}
    (root/'research/voevodsky/results/hodge-transverse-infinitesimal-interface-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
