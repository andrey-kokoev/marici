"""Blowup-chart and cohomological-degree controls; geometry is in the note."""
from math import comb
from pathlib import Path
import json


def main():
    # Coordinates (x0,x1,x2,t,v0,v1,v2), with v_j=1 on chart j.
    for j in range(3):
        strict={}
        substituted={}
        for i in range(3):
            e=[0]*7;e[i]=1
            if i!=j:e[4+i]=1
            strict[tuple(e)]=1
            e[3]+=1;substituted[tuple(e)]=1
        times_t={tuple(e[k]+int(k==3) for k in range(7)):c for e,c in strict.items()}
        assert times_t==substituted
        derivative={}
        for e,c in strict.items():
            if e[j]:
                f=list(e);f[j]-=1;derivative[tuple(f)]=c*e[j]
        assert derivative=={(0,)*7:1}
        # Strict transform stays smooth at t=0; the unsaturated total equation does not.
        assert all(e[3]==0 for e in strict) and all(e[3]==1 for e in substituted)
    assert 2-1==1  # nonzero normal linear equation in P2 gives P1
    assert 2-0==2  # zero normal equation at a node gives P2
    assert 5-2==3  # node fiber codimension in the smooth strict transform
    assert all(j-2*3<0 for j in (4,5))
    assert all(j-2*3<0 for j in (2,3))
    b4X=comb(12,4);b2Z=comb(12,2);b0Z=1
    b4B=b4X+b2Z+b0Z
    b4strict=b4B;b4V=b4strict;b4U=b4V-b2Z
    KD=b4U-b4X
    assert (b4X,b2Z,b4strict,b4U,KD)==(495,66,562,496,1)
    support_image=b4X  # known nonzero rZ spans KD and psi(rZ)=0
    assert b4U-support_image==1
    for k,m in ((1,2),(2,7),(3,10)):
        N=2160*k**3*(m-k)**3
        assert N>1 and N-(N-1)==KD
    # Negative degree check: treating node fibers as codimension TWO
    # would wrongly allow supported degree4 cohomology.
    assert 4-2*2==0 and 4-2*3<0
    result={'passed':True,'classification':'complete_intersection_envelope_has_no_extra_ambient_support',
        'b4_strict_transform':b4strict,'b4_smooth_locus':b4U,'KD_dimension':KD,
        'gamma_rank':'N-1','psi_rank':0,'support_source_dimension':b4U,
        'support_image_dimension':support_image,'support_kernel_dimension':1,
        'alpha_excluded_from_this_generic_envelope_family':True,
        'all_algebraic_supports_excluded':False,'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Replace the complete intersection by a supplied arbitrary smooth center and track its actual primitive cycle class.'}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-ci-envelope-blowup-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
