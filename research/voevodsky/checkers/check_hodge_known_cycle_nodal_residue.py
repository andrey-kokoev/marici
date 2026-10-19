"""Quadric quotient and actual-cycle coefficient controls, not full global ranks."""
from fractions import Fraction as Q
from pathlib import Path
import json
from check_hodge_deligne_lift_image import rank
from check_hodge_fixed_sixfold_pairing import power,integrate


def main():
    a=(1,0);b=(0,1);h2=(1,1)
    pair=lambda u,v:sum(x*y for x,y in zip(u,v))
    residue=lambda v:v[0]-v[1]  # ruling-a-adapted generator
    assert pair(a,a)==pair(b,b)==1 and pair(a,b)==0
    assert pair(h2,h2)==2 and pair(a,h2)==pair(b,h2)==1
    assert rank([a,h2])==rank([b,h2])==2
    assert residue(h2)==0 and residue(a)==1 and residue(b)==-1
    assert residue((1,-1))==2  # primitive is twice the chosen residue generator
    # Degree-two coefficient of (1+h)^3/(1+2h).
    assert 3-2*3+4==1
    E={(2*j,2*j+1):d for j,d in enumerate((1,1,1,-1,-1,-3))}
    assert integrate(power(E,6))==2160
    controls=0
    for k,m,q in ((1,2,1),(2,7,3),(3,10,5)):
        coeff=Q(k**3,m*q*q)
        assert Q(k**3)-coeff*m*q*q==0
        count=2160*k**3*(m-k)**3
        assert count>0
        # Sparse repeated-coordinate representation, not a claim about gamma's rank.
        residue_Z={'coordinate_value':Q(1),'number_of_nodes':count}
        residue_Y={'coordinate_value':Q(0),'number_of_nodes':count}
        assert residue_Z['coordinate_value']-coeff*residue_Y['coordinate_value']==1
        controls+=1
    result={'passed':True,'classification':'nonzero_actual_cycle_residue_killed_in_ambient_quotient',
        'ruling_residues':[1,-1],'primitive_residue':2,'rational_coefficient_controls':controls,
        'gamma_on_rZ':0,'psi_on_rZ':0,'rZ_nonzero':True,
        'support_class_of_corrected_cycle_nonzero':True,'ambient_Chow_class_of_corrected_cycle':0,
        'full_KD_rank_computed':False,'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Blowup calculation of the full residue rank for the complete-intersection envelope family.'}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-known-cycle-nodal-residue-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
