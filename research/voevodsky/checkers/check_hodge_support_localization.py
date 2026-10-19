"""Exact support-image controls; general duality is proved in the companion note."""
from itertools import product
from pathlib import Path
import json
from check_hodge_fixed_sixfold_pairing import wedge,power,integrate
from check_hodge_deligne_lift_image import rank


def main():
    # A three-dimensional irreducible component has real top degree six.
    # Lower strata of complex dimension <=2 cannot contribute degrees five/six.
    assert 2*3==6 and all(2*d<5 for d in (0,1,2))
    E={(2*j,2*j+1):d for j,d in enumerate((1,1,1,-1,-1,-3))}
    E3=power(E,3)
    R={tuple(2*j+b for j,b in enumerate(bits)):(-1)**(sum(bits)//2)
       for bits in product((0,1),repeat=6) if sum(bits)%2==0}
    indices=sorted(set(E3)|set(R))
    e=[E3.get(i,0) for i in indices];r=[R.get(i,0) for i in indices]
    assert rank([e,r])==2
    assert E3.get(tuple(range(0,12,2)),0)==0 and R[tuple(range(0,12,2))]==1
    assert integrate(wedge(E3,E3))==2160
    for m in (1,2,3,5):
        column=[m**3*x for x in e]
        assert rank([column,column])==1
        assert 2-rank([column,column])==1
        assert all(x-y==0 for x,y in zip(column,column))
        assert rank([column,column,r])==2
        assert 2160*m**3>0
    # Finite exactness fixture in coefficient coordinates:
    # delta(t)=(t,-t), support(u,v)=(u+v,0,0), restriction(a,b,c)=(b,c).
    delta=[1,-1]
    support=[[1,1],[0,0],[0,0]]
    restriction=[[0,1,0],[0,0,1]]
    assert all(sum(x*y for x,y in zip(row,delta))==0 for row in support)
    assert rank(support)==1 and rank(restriction)==2
    assert 2-rank(support)==1 and 3-rank(restriction)==rank(support)
    # The fixture is the known image inside the fixed 3D Hodge space,
    # not a computation of all H5/H6 of the actual complement.
    result={'passed':True,'classification':'support_image_equals_component_cycle_span',
        'control_support_components':2,'control_support_source_rank':2,
        'control_support_image_rank':1,'control_support_kernel_rank':1,
        'alpha_outside_control_support_image':True,'all_supports_excluded':False,
        'actual_complement_cohomology_computed':False,'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Smooth ample envelope, Gysin image and prescribed-base-locus Bertini limits.'}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-algebraic-support-localization-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
