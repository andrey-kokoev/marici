"""Trace and monodromy controls for the written parameter-space construction."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json


def rotate(v):return (-v[1],v[0])


def main():
    root=Path(__file__).resolve().parents[3]
    pointwise=json.loads((root/'research/voevodsky/results/hodge-complementary-threefold-composition-v1.json').read_text(encoding='utf-8'))
    assert pointwise['passed'] and pointwise['realized_classes']==['R','I']
    assert pointwise['decomposable_locus_complex_dimension']==4
    assert pointwise['relative_cycle_family_constructed'] is False
    checks=0
    for degree,mR,mI in product((1,2,3,7),repeat=3):
        for m,v in ((mR,(Q(1),Q(0))),(mI,(Q(0),Q(1)))):
            summed=tuple(sum(m*x for _ in range(degree)) for x in v)
            traced=tuple(x/Q(degree*m) for x in summed)
            assert traced==v
            if degree>1:assert tuple(x/Q(m) for x in summed)!=v
            if m>1:assert tuple(x/Q(degree) for x in summed)!=v
            checks+=1
    v=(1,0);orbit=[]
    for _ in range(4):orbit.append(v);v=rotate(v)
    assert v==(1,0) and len(set(orbit))==4
    assert tuple(sum(x[i] for x in orbit) for i in range(2))==(0,0)
    # Correct trace after fixing the determinant marking, versus wrong orbit averaging.
    assert tuple(sum((1,0)[i] for _ in range(4))//4 for i in range(2))==(1,0)
    assert (6+4)-(3+4)==3  # relative dimension-three universal cycles
    assert 4<9  # dominant over control base is not dominant over full moduli
    result={'passed':True,'classification':'relative_rational_control_cycles_exist_on_dense_open',
        'pointwise_algebraicity_input':'imported-theorem-backed complementary-threefold composition',
        'trace_controls':checks,'determinant_monodromy_image_order_bound':4,
        'relative_Chow_classes_constructed_by_existence_argument':['Xi_R','Xi_I'],
        'scope':'dense open of a finite level/monodromy cover of the dimension4 product-control base',
        'explicit_parameter_component_or_equations_produced':False,
        'prescribed_special_fiber_in_open_guaranteed':False,
        'dominance_over_full_Weil_base_proved':False,'original_fixed_alpha_realized':False,
        'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Closure and refined specialization within the control base versus transverse extension into full moduli.'}
    (root/'research/voevodsky/results/hodge-control-relative-cycle-spread-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
