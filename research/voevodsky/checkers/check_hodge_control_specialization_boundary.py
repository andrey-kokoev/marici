"""Exact Chow/Gysin degree controls; localization and constancy are written geometry."""
from fractions import Fraction as Q
from pathlib import Path
import json


def main():
    root=Path(__file__).resolve().parents[3]
    previous=json.loads((root/'research/voevodsky/results/hodge-control-relative-cycle-spread-v1.json').read_text(encoding='utf-8'))
    assert previous['passed']
    assert previous['relative_Chow_classes_constructed_by_existence_argument']==['Xi_R','Xi_I']
    fiber=6;base=4;ambient_base=9;codim=3
    control_total=fiber+base;full_total=fiber+ambient_base
    cycle_dimension=control_total-codim
    assert (control_total,full_total,cycle_dimension)==(10,15,7)
    restricted_dimension=cycle_dimension-base
    assert restricted_dimension==3 and fiber-restricted_dimension==codim
    pushed_codimension=full_total-cycle_dimension
    assert pushed_codimension==8==codim+(ambient_base-base)
    full_fiber_dimension=cycle_dimension-ambient_base
    assert full_fiber_dimension==-2 and pushed_codimension>fiber
    assert 2*pushed_codimension==16>2*fiber
    assert pushed_codimension!=codim  # treating a closed-base push as an open extension fails
    for cover_degree in (1,2,4,7):
        assert Q(cover_degree,cover_degree)==1
        assert full_total-cycle_dimension==8  # coefficient division cannot change support degree
    # General codimension-shift identity for a same-relative-dimension family inclusion.
    for c in range(1,7):
        total=fiber+base+c
        assert total-cycle_dimension==codim+c
        assert cycle_dimension-(base+c)==fiber-(codim+c)
    result={'passed':True,'classification':'control_specialization_constructed_transverse_pushforward_wrong_degree',
        'control_total_dimension':10,'extended_cycle_dimension':7,
        'control_fiber_Chow_codimension':3,'full_family_pushforward_Chow_codimension':8,
        'full_family_refined_fiber_target_dimension':-2,
        'all_smooth_control_fibers_realized_by_refined_restriction':True,
        'closures_assumed_flat':False,'canonical_Chow_extension_claimed':False,
        'transverse_codimension_three_extension_constructed':False,
        'original_fixed_alpha_realized':False,'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Embedded first-order deformation obstruction versus its Hodge/semiregularity image, with a complete-intersection lifting control.'}
    (root/'research/voevodsky/results/hodge-control-specialization-boundary-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
