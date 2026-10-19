#!/usr/bin/env python3
"""Actual positive internal Y1235 facet and boundary naturality to Y1267 corner."""
import json
import sys
import itertools
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(Path(__file__).resolve().parent))
from check_paired_composite_corner_residues import (s,rational,normalize,target_jac,parameters,sign,raw_bracket,gradient)
PRIOR='research/benincasa/results/three_composite_normalizations.json'
CORNER='research/benincasa/results/paired_composite_corner_residues.json'
INTERNAL=(1,2,3,5);PHYSICAL=(1,2,6,7)


def symbolic_facet(rows):
    a,A,_=parameters(rows[8]['target_runs'][0]);_,H,_=parameters(rows[9]['target_runs'][0])
    assert A.subs(a[0],0)==H.subs({a[0]:a[1],a[1]:0},simultaneous=True)
    # The seven surviving ordered coordinates are identical under this relabeling.
    xs=s.symbols('x1:8');T=s.Matrix(xs);logJ=s.diag(*[1/x for x in xs])*T.jacobian(xs)*s.diag(*xs)
    assert logJ==s.eye(7)
    pA,freeA=sign([0]);pH,freeH=sign([1]);assert pA==1 and pH==-1 and pA+pH*logJ.det()==0
    return {'source_matrix_identity':'A_history8(alpha1=0)=H_history9(alpha2=0,H_alpha1=A_alpha2)',
        'remaining_log_transition':'(H_alpha1,H_alpha3,...,H_alpha8)=(A_alpha2,A_alpha3,...,A_alpha8)',
        'log_transition_determinant':'1','source_residue_signs':[pA,pH],'symbolic_paired_seven_dlog_sum':'0',
        'source_facet_type':'actual shared positive cell with zero column4 and parallel pair35 and triple678',
        'A_remaining_order':[j+1 for j in freeA],'H_remaining_order':[j+1 for j in freeH]}


def run(rows,old):
    shift=old['positive_Z_moment_shift'];Z=s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)])
    a,A,va=parameters(rows[8]['target_runs'][shift]);_,H,_=parameters(rows[9]['target_runs'][shift])
    va[a[0]]=0;vh=va|{a[0]:va[a[1]],a[1]:0};assert A.subs(va)==H.subs(vh)
    coords=[(i,j) for i in range(2) for j in range(6) if j not in (0,1)]
    N=normalize(A.subs(va)*Z,[0,1]);assert s.Matrix.vstack(N,*[Z[k-1,:] for k in INTERNAL]).det()==0
    grad=gradient(N,Z,INTERNAL,coords);chart_data=[]
    for history,C,values,e in [(8,A,va,0),(9,H,vh,1)]:
        parity,free=sign([e]);J,actual=target_jac(C.subs(values)*Z,[C.diff(z).subs(values)*Z for z in a],[0,1]);assert actual==coords and J.det()!=0
        F=J[:,free]*s.diag(*[values[a[j]] for j in free]);assert F.rank()==7
        assert all(C.subs(values)[:,list(pair)].det()>=0 for pair in itertools.combinations(range(8),2))
        p=raw_bracket(C,Z,INTERNAL);assert p.subs(a[e],0)==0
        pivot=s.factor((C*Z)[:,[0,1]].det());slope=s.factor(s.diff(p,a[e]).subs(values)/pivot.subs(values));assert slope!=0
        normal=grad*J;assert normal[e]==slope and all(normal[j]==0 for j in free)
        chart_data.append((history,C,values,e,parity,free,J,F,normal,p,slope))
    assert chart_data[0][7]==chart_data[1][7]
    selected=next(I for I in itertools.combinations(range(8),7) if all(d[7][list(I),:].det()!=0 for d in chart_data))
    routes=[];densities=[]
    for history,C,values,e,parity,free,J,F,normal,p,slope in chart_data:
        det=s.factor(F[list(selected),:].det());detD=s.factor(s.Matrix.vstack(normal,J[list(selected),:]).det())
        source=s.factor(parity/det);target=s.factor(slope/(s.prod(values[a[j]] for j in free)*detD));assert source==target
        densities.append(source);routes.append({'history_index':history,'deleted_alpha':e+1,'source_deletion_sign':parity,
            'raw_source_internal_bracket':str(p),'normalized_target_normal':'raw bracket / det((CZ)[:,columns1,2])',
            'normal_slope':str(slope),'boundary_log_jacobian':str(det),'full_normal_jacobian':str(detD),
            'source_residue_then_pushforward':str(source),'top_pushforward_then_target_residue':str(target)})
    assert sum(densities)==0;hostile=s.factor(-densities[0]+densities[1]);assert hostile!=0
    # Boundary naturality of the actual facet seven-form: its next residue is
    # physical Y1267. Use the old corner's common six coordinates, not the facet
    # sample's unrelated seven-coordinate density frame.
    selected6=old['selected_common_target_coordinate_indices'];vc=va|{a[5]:0};hc=vh|{a[5]:0}
    Nc=normalize(A.subs(vc)*Z,[0,1]);G=s.Matrix.vstack(gradient(Nc,Z,INTERNAL,coords),gradient(Nc,Z,PHYSICAL,coords))
    assert G.rank()==2;boundary_routes=[]
    oldroutes={r['history_index']:r for r in old['routes']}
    for history,C,values,e in [(8,A,vc,0),(9,H,hc,1)]:
        parity7,free7=sign([e]);parity6,free6=sign([e,5])
        J,actual=target_jac(C.subs(values)*Z,[C.diff(z).subs(values)*Z for z in a],[0,1]);assert actual==coords and J.det()!=0
        F6=J[:,free6]*s.diag(*[values[a[j]] for j in free6]);det6=s.factor(F6[selected6,:].det());assert det6!=0
        normals=G*J;assert all(normals[i,j]==0 for i in range(2) for j in free6)
        normalminor=normals[:,[e,5]];assert normalminor.det()!=0
        prod=s.prod(values[a[j]] for j in free6)
        D7=s.Matrix.vstack(normals[1,free7],J[selected6,free7]);det7=s.factor(D7.det());assert det7!=0
        # The residue of the facet pushforward in the physical normal includes
        # its source-to-target normal slope, not a substitution at a pole.
        physical_slope=normals[1,5]
        facet_then_boundary=s.factor(parity7*physical_slope/(prod*det7))
        source_corner=s.factor(parity6/det6);assert facet_then_boundary==source_corner
        fullD=s.Matrix.vstack(normals,J[selected6,:]);full_route=s.factor(normalminor.det()/(prod*fullD.det()));assert full_route==source_corner
        olddensity=s.Rational(oldroutes[history]['iterated_source_residue_then_pushforward'])
        assert source_corner==-olddensity
        boundary_routes.append({'history_index':history,'residue_order':'internal Y1235 first, physical Y1267 second',
            'source_deletion_order':[e+1,6],'source_deletion_sign':parity6,
            'facet_pushforward_then_physical_residue':str(facet_then_boundary),'source_corner_then_pushforward':str(source_corner),
            'top_pushforward_then_internal_then_physical':str(full_route),
            'previous_physical_then_internal_density':str(olddensity),'order_anticommutation_residual':str(source_corner+olddensity)})
    assert sum(s.Rational(r['facet_pushforward_then_physical_residue']) for r in boundary_routes)==0
    return {'positive_Z_moment_shift':shift,'positive_actual_facet':True,'target_tangent_rank':7,
        'selected_common_target_coordinate_indices':list(selected),'target_coordinate_order':[[i+1,j+1] for i,j in coords],
        'target_facet_point':[str(N[i,j]) for i,j in coords],'routes':routes,'paired_seven_form_sum':'0',
        'orientation_reversal_residual':str(hostile),'boundary_naturality_routes':boundary_routes,
        'boundary_paired_six_form_sum':'0','residue_order_anticommutation_verified':True}


def main():
    prior=json.loads((ROOT/PRIOR).read_text());corner=json.loads((ROOT/CORNER).read_text())
    for receipt,checker in [(prior,'research/benincasa/checkers/check_three_composite_normalizations.py'),
                           (corner,'research/benincasa/checkers/check_paired_composite_corner_residues.py')]:
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
        assert receipt['checker_sha256']==sha256((ROOT/checker).read_bytes()).hexdigest()
    rows={r['history_index']:r for r in prior['rows']};witness=symbolic_facet(rows);runs=[run(rows,old) for old in corner['runs']]
    checks={'symbolic_actual_positive_shared_facet_and_unit_log_transition':True,
        'two_positive_rank7_common_target_images':True,'four_genuine_internal_normal_residue_squares':True,
        'two_paired_seven_form_sums_zero':True,'orientation_hostiles_nonzero':True,
        'four_three_route_boundary_naturality_equalities':True,'old_corner_receipt_preserved_with_order_anticommutation':True}
    paths=[PRIOR,CORNER,'research/benincasa/checkers/check_paired_composite_corner_residues.py',
        'research/benincasa/checkers/check_shared_y1267_composite_facet.py',
        'research/benincasa/checkers/check_shared_composite_physical_facet.py',
        'research/benincasa/checkers/check_composite_root_normalization.py']
    out={'schema':'marici.benincasa.shared-internal-composite-facet.v1','histories':[8,9],'target_internal_divisor':list(INTERNAL),
        'source_witness':witness,'runs':runs,'checks':checks,'passed':True,
        'disposition':'actual_positive_internal_facet_unweighted_paired_cancellation_and_corner_boundary_naturality_constructed',
        'claim_boundary':'Symbolic source facet/transition cancellation, two fixed-Z seven-form target squares and boundary naturality to one corner. Not weighted nine-form cancellation, component extraction, global BCFW orientation or complete invariant boundary coverage.',
        'next_action':'Screen all seven coordinate boundary faces of this actual shared positive facet using the common source transition. Classify rank6 versus contracted target images and actual second normals; retain undefined inverse/full-rank cases rather than reusing the corner normal assumptions. Expand paired iterated residue coverage only for admitted local branches.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=ROOT/'research/benincasa/results/shared_internal_composite_facet.json';path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'checks':checks,'paired_sums':[r['paired_seven_form_sum'] for r in runs],
        'disposition':out['disposition']},indent=2))


if __name__=='__main__':main()
