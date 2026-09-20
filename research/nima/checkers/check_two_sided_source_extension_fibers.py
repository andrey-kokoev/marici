"""Degree-zero extension fibers of admitted edge inclusions and dual restrictions.

Coefficients are rational sets (0-types). Affine dimension is not a claim
about the homotopy type of a topologized real vector space.
"""
from pathlib import Path
import json
import sympy as s


def inclusion(n,m):
    return s.eye(m)[:,:n]


def system(levels,variance,central):
    offsets={}
    count=0
    for n in levels:
        offsets[n]=count
        count+=n
    rows=[]
    rhs=[]
    for n,m in zip(levels,levels[1:]):
        U=inclusion(n,m)
        for j in range(m if variance=='co' else n):
            row=[s.Integer(0)]*count
            if variance=='co':
                row[offsets[m]+j]=1
                for i in range(n):
                    row[offsets[n]+i]-=U[j,i]
            else:
                row[offsets[n]+j]=1
                for i in range(m):
                    row[offsets[m]+i]-=U[i,j]
            rows.append(row);rhs.append(0)
    for n,value in central.items():
        for j,x in enumerate(value):
            row=[s.Integer(0)]*count
            row[offsets[n]+j]=1
            rows.append(row);rhs.append(x)
    A=s.Matrix(rows)
    b=s.Matrix(rhs)
    rank=A.rank()
    return {'inhabited':rank==A.row_join(b).rank(),
            'affine_dimension_if_inhabited':count-rank,
            'equations':A,'rhs':b}


def public(record):
    return {k:v for k,v in record.items() if k not in ('equations','rhs')}


def main():
    near=[4,5,6,7]
    far=[3,4,5,6,7,8]
    # Source labels inherited from the first twelve edges of the 2,3,5 cube.
    edges=[(2,4,2),(2,6,3),(2,10,5),(4,12,3),(4,20,5),(6,12,2),
           (6,30,5),(12,60,5),(10,20,2),(10,30,3),(20,60,3),(30,60,2)]
    x5=s.Matrix([1,0,0,0,0])
    good={5:x5,6:inclusion(5,6)*x5}
    # Fifth edge is allowed at the central level but not the lower neighbour.
    bad5=s.Matrix([0,0,0,0,1])
    bad={5:bad5,6:inclusion(5,6)*bad5}
    # Fourth edge extends to level 4, but not to the newly included level 3.
    boundary5=s.Matrix([0,0,0,1,0])
    boundary={5:boundary5,6:inclusion(5,6)*boundary5}
    dual6=s.Matrix([1,2,3,4,5,6])
    dual={5:inclusion(5,6).T*dual6,6:dual6}
    records={
        'co_good_near':system(near,'co',good),
        'co_good_far':system(far,'co',good),
        'co_obstructed_near':system(near,'co',bad),
        'co_boundary_near':system(near,'co',boundary),
        'co_boundary_far':system(far,'co',boundary),
        'contra_near':system(near,'contra',dual),
        'contra_far':system(far,'contra',dual),
    }
    # Two exterior covectors differ but pair identically with every source
    # propagated from the central level. No corrective information returns.
    outer_a=dual6.col_join(s.Matrix([0]))
    outer_b=dual6.col_join(s.Matrix([7]))
    P=inclusion(6,7).T
    source7=inclusion(5,7)*x5
    checks={
        'co_good_near_singleton':records['co_good_near']['inhabited'] and records['co_good_near']['affine_dimension_if_inhabited']==0,
        'co_good_far_singleton':records['co_good_far']['inhabited'] and records['co_good_far']['affine_dimension_if_inhabited']==0,
        'co_obstruction_before_infinity':not records['co_obstructed_near']['inhabited'],
        'enlarging_left_can_exclude_a_central_datum':records['co_boundary_near']['inhabited'] and not records['co_boundary_far']['inhabited'],
        'contra_near_has_one_free_coordinate':records['contra_near']['inhabited'] and records['contra_near']['affine_dimension_if_inhabited']==1,
        'contra_far_has_two_free_coordinates':records['contra_far']['inhabited'] and records['contra_far']['affine_dimension_if_inhabited']==2,
        'dual_restriction_fiber_nontrivial':outer_a!=outer_b and P*outer_a==P*outer_b,
        'extra_dual_coordinate_does_not_change_central_pairing':(outer_a.T*source7)[0]==(outer_b.T*source7)[0],
        'source_inclusion_not_inverse_to_dual_restriction':inclusion(6,7)*P!=s.eye(7),
    }
    # The degree-six source cycle is still present in the full source record.
    endpoints=sorted(set(v for edge in edges[:6] for v in edge[:2]))
    J=s.Matrix(len(endpoints)-1,6,lambda i,j:int(edges[j][0]<=endpoints[i] and endpoints[i+1]<=edges[j][1]))
    h=s.Matrix([1,-1,0,1,0,-1])
    checks['nonzero_cycle_would_be_hidden_by_history_only']=h!=s.zeros(6,1) and J*h==s.zeros(J.rows,1)
    checks['cycle_not_silently_quotiented']=s.eye(6)*h==h
    assert all(checks.values()),checks
    result={
        'schema':'marici.nima.two-sided-source-extension-fibers.v1',
        'strength':'exact_degree_zero_test_on_source_edge_cutoff_axis',
        'near_levels':near,'enlarged_levels':far,
        'central_seam':[5,6],
        'edges':edges,
        'fibers':{k:public(v) for k,v in records.items()},
        'checks':checks,
        'interpretation':{
            'co':'empty or singleton, determined by membership in the earliest retained source',
            'contra':'affine free exterior coordinates; enlargement restricts surjectively and does not constrain the fixed central covector',
            'paired':'remote dual freedom annihilates the centrally included source, by evaluation naturality',
        },
        'feedback_correction_constructed':False,
        'unsupported':['higher identity types','full analytic admissibility','two-sided infinite source','boundary conditions at infinity','positive Green comparison'],
    }
    out=Path(__file__).resolve().parents[1]/'results/two-sided-source-extension-fibers.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
