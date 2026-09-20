"""Exact incidence layer of a theta interval-history constructor.

Endpoints log(2),log(4),log(6),log(12); no numerical theta approximation.
Analytic injectivity and Gram positivity are proved in the companion packet.
"""
import json
from pathlib import Path
import sympy as s


def main():
    # e0:2->4, e1:4->12, e2:2->6, e3:6->12.
    endpoints=(2,4,6,12)
    edges=((2,4),(4,12),(2,6),(6,12))
    J=s.Matrix(3,4,lambda i,j:int(edges[j][0]<=endpoints[i] and endpoints[i+1]<=edges[j][1]))
    boundary=s.zeros(4,4)
    for j,(a,b) in enumerate(edges):
        boundary[endpoints.index(a),j]=-1
        boundary[endpoints.index(b),j]=1
    atom_boundary=s.zeros(4,3)
    for j in range(3):
        atom_boundary[j,j]=-1
        atom_boundary[j+1,j]=1
    h=s.Matrix([1,1,-1,-1])
    ZA=s.Matrix([[0,0,0,1]])  # chord e3; other three edges form a tree
    ZB=s.Matrix([[0,1,0,0]])  # chord e1; other three edges form a tree
    A=J.col_join(ZA)
    B=J.col_join(ZB)
    T=B*A.inv()
    expected=s.eye(4)
    expected[3,:]=s.Matrix([[0,0,1,-1]])
    # Ordered two-port projections of the common refinement.
    P23=s.Matrix([[1,0,0],[0,1,1]])
    P32=s.Matrix([[1,1,0],[0,0,1]])
    ratio_hostile=s.Matrix([0,1,-1])
    lifted=A.inv()*ratio_hostile.col_join(s.zeros(1,1))
    K=T-s.eye(4)
    r=-s.trace(K)+s.trace(K*K)/2
    checks={
        'source_boundary_matches_interval_boundary':atom_boundary*J==boundary,
        'same_one_dimensional_cycle_kernel':J.rank()==3 and boundary.rank()==3 and J*h==s.zeros(3,1) and boundary*h==s.zeros(4,1),
        'both_chord_selectors_detect_cycle':(ZA*h)[0]!=0 and (ZB*h)[0]!=0,
        'both_joint_presentations_invertible':A.det()!=0 and B.det()!=0,
        'forest_transition_exact':T==expected,
        'forest_transition_preserves_interval_packet':T[:3,:]==s.eye(4)[:3,:],
        'forest_transition_retains_cycle_coupling':T[3,2]==1 and T[3,3]==-1,
        'forest_transition_involutive':T*T==s.eye(4),
        'transition_determinant_is_frame_ratio':T.det()==B.det()/A.det()==-1,
        'source_oriented_normalization_is_unit':s.simplify(T.det()*A.det()/B.det())==1,
        'ratio_window_hostile_first_order_invisible':P23*ratio_hostile==s.zeros(2,1),
        'ratio_window_hostile_second_order_visible':P32*ratio_hostile==s.Matrix([1,-1]),
        'ratio_hostile_lifts_to_source':J*lifted==ratio_hostile and ZA*lifted==s.zeros(1,1),
        'both_orders_retain_same_total':s.ones(1,2)*P23==s.ones(1,2)*P32,
        'det3_forest_frame_coordinate':T.det()==-1 and r==4,
        'label_translation_preserves_combinatorics':all(
            int(5*a<=5*endpoints[i] and 5*endpoints[i+1]<=5*b)==J[i,j]
            for i in range(3) for j,(a,b) in enumerate(edges)),
    }
    assert all(checks.values()),checks
    result={
        'schema':'marici.nima.arithmetic-diamond-cycle-determinant.v1',
        'strength':'exact_arithmetic_interval_incidence_with_conditional_analytic_application',
        'endpoints':list(endpoints),'edges':[list(e) for e in edges],
        'J':[[int(x) for x in J.row(i)] for i in range(J.rows)],
        'forest_transition':[[str(x) for x in T.row(i)] for i in range(4)],
        'checks':checks,
        'lifted_ratio_hostile':[str(x) for x in lifted],
        'det3_frame_coordinate':{'prefactor':'-1','exponent':str(r)},
        'theta_integrals_numerically_evaluated':False,
        'analytic_premise':'injectivity of recorded T_0 on L1 supported in [log(2),infinity)',
        'unsupported':['Euler low-grade trace identification','full source four-phase successor','cutoff-uniform inverse','Haar-cycle closure'],
    }
    out=Path(__file__).resolve().parents[1]/'results/arithmetic-diamond-cycle-determinant.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
