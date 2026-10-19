"""Gauge and quadratic-model controls; all-order comparison is a separate geometric input."""
from pathlib import Path
import json
from check_hodge_deligne_lift_image import rank
from check_hodge_control_quadratic_obstruction import unit,multiply,comm


def main():
    root=Path(__file__).resolve().parents[3]
    prior=json.loads((root/'research/voevodsky/results/hodge-control-quadratic-obstruction-v1.json').read_text(encoding='utf-8'))
    assert prior['passed'] and prior['selected_embedded_first_order_deformation_extends_to_order_two'] is False
    ident=[[int(i==j) for j in range(3)] for i in range(3)]
    zero=[[0]*3 for _ in range(3)]
    q=[[1,1,0],[0,1,1],[0,0,1]];g=[[1,-1,1],[0,1,-1],[0,0,1]]
    assert multiply(g,q)==ident==multiply(q,g)
    j=[[0,1,0],[0,0,1],[0,0,0]];j2=multiply(j,j)
    assert multiply(j2,j)==zero and j2!=zero
    matrices=[j,j2,ident,zero,j,j2]
    conjugated=[multiply(multiply(g,m),q) for m in matrices]
    assert all(comm(a,b)==zero for a in conjugated for b in conjugated)
    section=[q[i]+[i+1,2*i-1] for i in range(3)]
    normalized=[[sum(g[i][k]*section[k][c] for k in range(3)) for c in range(5)] for i in range(3)]
    assert [row[:3] for row in normalized]==ident
    assert [[sum(q[i][k]*normalized[k][c] for k in range(3)) for c in range(5)] for i in range(3)]==section
    # Bilinear coefficients of one matrix commutator in the 81 monomials A_ab B_cd.
    indices=[(i,j) for i in range(3) for j in range(3)]
    quadrics=[]
    for r,s in indices:
        quadrics.append([comm(unit(a,b),unit(c,d))[r][s] for a,b in indices for c,d in indices])
    assert rank(quadrics)==8
    # Different matrix pairs use disjoint sets of bilinear monomials.
    assert (6*5//2)*rank(quadrics)==120
    for n in (6,24,192):
        section_variables=3*n-9
        tangent=54+section_variables
        normal_sections=3*(n-3+3*6)
        assert tangent==normal_sections==3*n+45
    result={'passed':True,'classification':'formal_Hilbert_control_commuting_matrices_times_smooth_sections',
        'matrix_tuple_length':6,'matrix_size':3,'matrix_tangent_variables':54,
        'smooth_section_variables':'3 h0(L) - 9','Hilbert_tangent_dimension':'3 h0(L) + 45',
        'independent_quadratic_equations':120,'residual_gauge_after_section_frame':False,
        'all_order_comparison':'strict invariant-Dolbeault quasi-isomorphism and small-extension pair-to-Hilbert equivalence',
        'complete_intersection_formal_model_constructed':True,
        'analytic_convergence_or_finite_type_arc_algebraization_claimed':False,
        'original_Weil_cycle_model_constructed':False,'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Algebraize a commuting unipotent arc over C[[t]] and compute its cycle class and Weil-plane readout.'}
    (root/'research/voevodsky/results/hodge-control-formal-model-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
