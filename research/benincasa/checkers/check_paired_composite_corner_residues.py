#!/usr/bin/env python3
"""Actual shared positive corner: paired unweighted iterated residues."""
import json
import sys
import itertools
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(Path(__file__).resolve().parent))
from check_shared_y1267_composite_facet import s,rational,normalize,target_jac,parameters
PRIOR='research/benincasa/results/three_composite_normalizations.json'
CORNER='research/benincasa/results/shared_y1267_composite_facet.json'
NORMALS=[(1,2,6,7),(1,2,3,5)]


def sign(order):
    remaining=list(range(8));out=1
    for e in order:out*=(-1)**remaining.index(e);remaining.remove(e)
    return out,remaining


def raw_bracket(C,Z,quad):
    complement=[i for i in range(8) if i+1 not in quad]
    return s.factor(sum(C[:,[i,j]].det()*s.Matrix.vstack(Z[i,:],Z[j,:],*[Z[k-1,:] for k in quad]).det()
        for i,j in itertools.combinations(complement,2)))


def gradient(N,Z,quad,coords):
    vals=[]
    for i,j in coords:
        E=s.zeros(2,6);E[i,j]=1
        vals.append(s.Matrix.vstack(E[0,:],N[1,:],*[Z[k-1,:] for k in quad]).det()+
                    s.Matrix.vstack(N[0,:],E[1,:],*[Z[k-1,:] for k in quad]).det())
    return s.Matrix(1,8,vals)


def symbolic_source(rows):
    a,A,_=parameters(rows[8]['target_runs'][0]);_,H,_=parameters(rows[9]['target_runs'][0])
    transition={a[0]:a[1],a[1]:0,a[5]:0}
    assert A.subs({a[0]:0,a[5]:0})==H.subs(transition,simultaneous=True)
    sigA,freeA=sign([5,0]);sigH,freeH=sign([5,1]);assert sigA==-1 and sigH==1
    # Surviving source coordinate order: A(a2,a3,a4,a5,a7,a8),
    # H(b1,b3,b4,b5,b7,b8) with b1=a2 and all others identical.
    x=s.symbols('x1:7');T=s.Matrix(x);log_transition=s.diag(*[1/z for z in T])*T.jacobian(x)*s.diag(*x)
    assert log_transition==s.eye(6) and sigA+sigH*log_transition.det()==0
    assert sign([0,5])[0]==-sigA and sign([1,5])[0]==-sigH
    return {'source_matrix_identity':'A(alpha1=alpha6=0)=H(alpha2=alpha6=0, H_alpha1=A_alpha2)',
        'A_deletion_order':[6,1],'H_deletion_order':[6,2],'A_sign':sigA,'H_sign':sigH,
        'A_remaining_order':[j+1 for j in freeA],'H_remaining_order':[j+1 for j in freeH],
        'shared_remaining_transition':'(H_alpha1,H_alpha3,H_alpha4,H_alpha5,H_alpha7,H_alpha8)=(A_alpha2,A_alpha3,A_alpha4,A_alpha5,A_alpha7,A_alpha8)',
        'log_transition_determinant':'1','symbolic_source_paired_sum':'0','reverse_both_residue_orders_flips_both_signs':True}


def run(rows,corner):
    shift=corner['positive_Z_moment_shift'];Z=s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)])
    a,A,_=parameters(rows[8]['target_runs'][shift]);_,H,_=parameters(rows[9]['target_runs'][shift])
    va={z:s.Rational(corner['history8_parameters'][str(z)]) for z in a};vh={z:s.Rational(corner['history9_parameters'][str(z)]) for z in a}
    assert A.subs(va)==H.subs(vh)
    N=normalize(A.subs(va)*Z,[0,1]);coords=[(i,j) for i in range(2) for j in range(6) if j not in (0,1)]
    assert all(s.Matrix.vstack(N,*[Z[k-1,:] for k in q]).det()==0 for q in NORMALS)
    grads=s.Matrix.vstack(*[gradient(N,Z,q,coords) for q in NORMALS]);assert grads.rank()==2
    chart_data=[]
    for history,C,values,order in [(8,A,va,[5,0]),(9,H,vh,[5,1])]:
        parity,free=sign(order);Y=C.subs(values)*Z
        J,actual=target_jac(Y,[C.diff(z).subs(values)*Z for z in a],[0,1]);assert actual==coords and J.det()!=0
        F=J[:,free]*s.diag(*[values[a[j]] for j in free]);assert F.rank()==6
        B=grads*J
        assert all(B[i,j]==0 for i in range(2) for j in free)
        normal_minor=B[:,order];assert normal_minor.det()!=0
        # Normals are genuine source-derived bracket divisors, not fitted planes.
        pivot=s.factor((C*Z)[:,[0,1]].det());pullbacks=[]
        for q,e in zip(NORMALS,order):
            p=raw_bracket(C,Z,q);assert p.subs(a[e],0)==0
            slope=s.factor(s.diff(p,a[e]).subs(values)/pivot.subs(values));assert slope!=0
            pullbacks.append({'target_bracket':list(q),'raw_source_pullback':str(p),'deleted_alpha':e+1,'boundary_normal_slope':str(slope)})
        chart_data.append((history,C,values,order,parity,free,J,F,B,normal_minor,pullbacks))
    assert chart_data[0][7]==chart_data[1][7]
    selected=next(I for I in itertools.combinations(range(8),6) if all(d[7][list(I),:].det()!=0 for d in chart_data))
    routes=[];densities=[]
    for history,C,values,order,parity,free,J,F,B,normal_minor,pullbacks in chart_data:
        tangentdet=s.factor(F[list(selected),:].det());source_route=s.factor(parity/tangentdet)
        D=s.Matrix.vstack(B,J[list(selected),:]);detD=s.factor(D.det());assert detD!=0
        prod=s.prod(values[a[j]] for j in free)
        top_route=s.factor(normal_minor.det()/(prod*detD));assert source_route==top_route
        # Middle route: first source residue then seven-form pushforward, followed
        # by residue in the second common target normal. First deletion has sign -1.
        remaining=[j for j in range(8) if j!=order[0]]
        D7=s.Matrix.vstack(B[1,remaining],J[list(selected),remaining]);det7=s.factor(D7.det());assert det7!=0
        second_slope=B[1,order[1]];assert second_slope!=0
        middle_route=s.factor((-1)**order[0]*second_slope/(prod*det7));assert middle_route==source_route
        densities.append(source_route)
        routes.append({'history_index':history,'source_deletion_order':[j+1 for j in order],
            'source_deletion_parity':parity,'source_normal_pullbacks':pullbacks,
            'ordered_normal_minor':[[str(v) for v in rr] for rr in normal_minor.tolist()],
            'boundary_log_jacobian':str(tangentdet),'full_common_normal_jacobian':str(detD),'middle_normal_jacobian':str(det7),
            'iterated_source_residue_then_pushforward':str(source_route),
            'first_source_residue_pushforward_then_target_second_residue':str(middle_route),
            'top_pushforward_then_two_common_target_residues':str(top_route)})
    total=s.factor(sum(densities));hostile=s.factor(-densities[0]+densities[1]);assert total==0 and hostile!=0
    return {'positive_Z_moment_shift':shift,'target_normal_order':[list(q) for q in NORMALS],
        'selected_common_target_coordinate_indices':list(selected),'target_coordinate_order':[[i+1,j+1] for i,j in coords],
        'target_corner_point':[str(N[i,j]) for i,j in coords],'routes':routes,'paired_density_sum':str(total),
        'orientation_reversal_one_route_residual':str(hostile),'one_residue_order_reversal_residual':str(hostile),
        'disposition':'paired_unweighted_local_six_form_residues_cancel_in_identical_target_coordinates'}


def main():
    prior=json.loads((ROOT/PRIOR).read_text());corner=json.loads((ROOT/CORNER).read_text())
    for receipt,checker in [(prior,'research/benincasa/checkers/check_three_composite_normalizations.py'),
                           (corner,'research/benincasa/checkers/check_shared_y1267_composite_facet.py')]:
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
        assert receipt['checker_sha256']==sha256((ROOT/checker).read_bytes()).hexdigest()
    rows={r['history_index']:r for r in prior['rows']};witness=symbolic_source(rows);runs=[run(rows,c) for c in corner['shared_corner_controls']]
    checks={'symbolic_actual_source_corner_identity':True,'symbolic_log_transition_unit_and_opposite_deletion_parities':True,
        'two_independent_genuine_bracket_normals':True,'four_three_route_iterated_residue_equalities':True,
        'two_common_target_paired_density_sums_zero':True,'orientation_and_one_route_order_reversal_hostiles_nonzero':True}
    paths=[PRIOR,CORNER,'research/benincasa/checkers/check_shared_y1267_composite_facet.py',
        'research/benincasa/checkers/check_shared_composite_physical_facet.py',
        'research/benincasa/checkers/check_three_composite_inverse_normals.py',
        'research/benincasa/checkers/check_composite_root_normalization.py']
    out={'schema':'marici.benincasa.paired-composite-corner-residues.v1','histories':[8,9],'source_witness':witness,'runs':runs,
        'checks':checks,'passed':True,'disposition':'one_actual_shared_positive_corner_has_unweighted_oriented_local_iterated_residue_cancellation',
        'claim_boundary':'Symbolic source corner/transition cancellation and two fixed-Z target differential controls with physical Y1267 then internal Y1235 normals. No weighted nine-form sector/component map, global source-chain orientation anchor or full codimension-two coverage theorem.',
        'next_action':'Extend the identified corner to its actual shared internal facet: A history8 alpha1=0 equals H history9 alpha2=0 under H_alpha1=A_alpha2 without setting alpha6=0. Verify positive rank7 image, common Y1235 normal and oriented paired seven-form cancellation, then its boundary naturality to this corner; keep weighted gates separate.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=ROOT/'research/benincasa/results/paired_composite_corner_residues.json';path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'checks':checks,'paired_sums':[r['paired_density_sum'] for r in runs],'disposition':out['disposition']},indent=2))


if __name__=='__main__':main()
