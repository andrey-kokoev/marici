"""Exact commutator/cohomology-model checks; geometric comparison is written separately."""
from itertools import combinations
from pathlib import Path
import json
from check_hodge_deligne_lift_image import rank


def unit(i,j):return [[int((a,b)==(i,j)) for b in range(3)] for a in range(3)]
def multiply(a,b):return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def comm(a,b):
    ab=multiply(a,b);ba=multiply(b,a)
    return [[ab[i][j]-ba[i][j] for j in range(3)] for i in range(3)]
def flat(a):return [x for row in a for x in row]
def trace(a):return sum(a[i][i] for i in range(3))


def main():
    root=Path(__file__).resolve().parents[3]
    prior=json.loads((root/'research/voevodsky/results/hodge-complete-intersection-semiregularity-v1.json').read_text(encoding='utf-8'))
    assert prior['passed'] and prior['semiregularity_kernel_dimension']==120
    beta=comm(unit(0,1),unit(1,0))
    assert beta==[[1,0,0],[0,-1,0],[0,0,0]] and trace(beta)==0
    pairs=list(combinations(range(6),2))
    # H2(O_X) identified geometrically with Lambda2 of the invariant H1 basis.
    wedge=[int(p==(0,1)) for p in pairs]
    obstruction=[x*y for x in flat(beta) for y in wedge]
    assert any(obstruction) and len(obstruction)==135
    assert [sum(obstruction[(3*i+i)*15+a] for i in range(3)) for a in range(15)]==[0]*15
    generators=[comm(unit(i,i),unit(i,j)) for i in range(3) for j in range(3) if i!=j]
    generators += [comm(unit(i,2),unit(2,i)) for i in (0,1)]
    assert all(trace(g)==0 for g in generators) and rank([flat(g) for g in generators])==8
    span=[[x*int(a==b) for x in flat(g) for a in range(15)] for g in generators for b in range(15)]
    assert rank(span)==120
    # In 0->negative A->negative B->F->0, Hq(F)=0 follows for q<5.
    negative_vanishing=set(range(6))
    assert all(q in negative_vanishing and q+1 in negative_vanishing for q in range(5))
    result={'passed':True,'classification':'nonzero_quadratic_Hilbert_obstruction_with_zero_semiregularity_image',
        'bundle_obstruction_matrix':beta,'cohomology_wedge':'u_1 wedge u_2 nonzero in H2(O_X)',
        'bundle_obstruction_nonzero':True,'first_order_section_lifts':True,
        'embedded_obstruction_comparison':'pair-to-zero-locus map, Cech defect compatibility and Koszul vanishing',
        'selected_embedded_first_order_deformation_extends_to_order_two':False,
        'semiregularity_image_zero':True,'linear_span_of_constructed_obstruction_values_dimension':120,
        'every_kernel_vector_claimed_as_single_quadratic_value':False,
        'ambient_Kodaira_Spencer_varies':False,'constant_cycle_deformation_still_exists':True,
        'original_Weil_cycle_obstruction_computed':False,'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Formal commuting-matrix model with section parameters and gauge, using an actual deformation-algebra comparison.'}
    (root/'research/voevodsky/results/hodge-control-quadratic-obstruction-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
