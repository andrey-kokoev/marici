#!/usr/bin/env python3
"""Balanced infinity/zero shear chart merging positive directions (2,3,5)."""
import json
import sys
import itertools
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(Path(__file__).resolve().parent))
from check_shared_facet_mixed_radial import s,rational,normalize,target_jac,parameters,gradient,raw_bracket,setup_A,inverse_A
PRIOR='research/benincasa/results/three_composite_normalizations.json'
FACET='research/benincasa/results/shared_internal_composite_facet.json'
PREVIOUS='research/benincasa/results/shared_facet_mixed_radial.json'
INVERSES='research/benincasa/results/three_composite_inverse_normals.json'


def chart(rows):
    a,A,_=parameters(rows[8]['target_runs'][0]);_,H,_=parameters(rows[9]['target_runs'][0])
    t,u,q=s.symbols('t u q');variables=[t,a[1],u,a[4],a[5],a[6],q]
    maps=[a[1],u,1/t,a[4],a[5],a[6],t*q]
    logJ=s.diag(*[1/x for x in maps])*s.Matrix(maps).jacobian(variables)*s.diag(*variables)
    assert s.factor(logJ.det())==-1
    substitution={a[0]:0,a[2]:u,a[3]:1/t,a[7]:t*q};shear=s.Matrix([[1,-1/t],[0,1]])
    assert shear.det()==1
    C=(shear*A.subs(substitution,simultaneous=True)).applyfunc(rational)
    hs=substitution|{a[0]:a[1],a[1]:0}
    assert C==(shear*H.subs(hs,simultaneous=True)).applyfunc(rational)
    assert C[:,3]==s.zeros(2,1) and C[:,1]==s.Matrix([q,-t*q])
    return a,C,variables,{'substitution':'alpha4=1/t,alpha8=t*q,alpha3=u; alpha2,alpha5,alpha6,alpha7 finite',
        'shear':[['1','-1/t'],['0','1']],'shear_determinant':'1, not a form coefficient',
        'new_order':[str(z) for z in variables],'log_wedge_jacobian':[[str(x) for x in row] for row in logJ.tolist()],
        'log_wedge_determinant':'-1','shared_source_germ':[[str(x) for x in row] for row in C.tolist()],
        'source_boundary_signs':[-1,1],'symbolic_paired_source_six_dlog_sum':'0'}


def extract_boundary(R):
    # Column3 is horizontal, column1 is vertical at the boundary. These fix the
    # source gauge even though the original column2 gauge has become singular.
    W=s.Matrix.hstack(R[:,2],-R[:,0]);assert W.det()!=0
    B=(W.inv()*R).applyfunc(rational);assert B[1,5]!=0
    canon=(s.diag(1,1/B[1,5])*B).applyfunc(rational)
    return [canon[0,4],canon[0,5],canon[1,6],canon[1,7],-canon[1,0],canon[0,1]]


def run(rows,a,C,variables,old):
    shift=old['positive_Z_moment_shift'];Z=s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)])
    t,aa,u,a5,a6,a7,q=variables;_,A,prior=parameters(rows[8]['target_runs'][shift]);anchor=1/prior[a[3]]
    values={aa:prior[a[1]],u:prior[a[2]],a5:prior[a[4]],a6:prior[a[5]],a7:prior[a[6]],q:prior[a[7]]/anchor}
    C0=C.subs(t,0);Cp=C0.subs(values);assert Cp.rank()==2
    assert all(Cp[:,list(pair)].det()>=0 for pair in itertools.combinations(range(8),2))
    assert all(rational(C0[:,list(pair)].det())==0 for pair in [(1,2),(1,4),(2,4),(5,6),(5,7),(6,7)])
    Y=Cp*Z;N=normalize(Y,[0,1]);coords=[(i,j) for i in range(2) for j in range(6) if j not in (0,1)]
    J,actual=target_jac(Y,[C.diff(z).subs(t,0).subs(values)*Z for z in variables],[0,1]);assert actual==coords and J.rank()==7
    remaining=variables[1:];F=J[:,1:]*s.diag(*[values[z] for z in remaining]);assert F.rank()==6
    selected=next(I for I in itertools.combinations(range(8),6) if F[list(I),:].det()!=0)
    det=s.factor(F[list(selected),:].det());prod=s.prod(values[z] for z in remaining)
    inverse_data=setup_A(Z,rows[8]['superfunction_runs'][0]['matches'][0])
    # Actual boundary inverse uses the already source-authorized A fiber circuit;
    # retain a nonsingular source gauge, not the column2 canonical gauge.
    R0,_=inverse_A(C0*Z,inverse_data)
    assert all(rational(x)==0 for x in R0-C0)
    assert all(rational(x-y)==0 for x,y in zip(extract_boundary(R0),remaining))
    R,_=inverse_A(N,inverse_data);assert extract_boundary(R)==[values[z] for z in remaining]
    quad=(1,6,7,8);p=raw_bracket(C,Z,quad);assert p!=0 and p.subs(t,0)==0
    pivot=s.factor((C*Z)[:,[0,1]].det());slope=s.factor(s.diff(p,t).subs(t,0).subs(values)/pivot.subs(t,0).subs(values));assert slope!=0
    normal=gradient(N,Z,quad,coords)*J;assert normal[0]==slope and all(normal[j]==0 for j in range(1,7))
    def radial_b(target):
        R,loc=inverse_A(target,inverse_data)
        den=rational(R[:,[2,5]].det()*R[:,[0,1]].det());assert den!=0 and all(x!=0 for x in loc)
        return rational(R[:,[1,2]].det()*R[:,[0,2]].det()/den)
    assert radial_b(N)==0
    Nt=normalize(C.subs(values)*Z,[0,1]).applyfunc(rational);assert rational(radial_b(Nt)-t)==0
    h=s.symbols('h');g=[]
    for i,j in coords:
        E=s.zeros(2,6);E[i,j]=1;g.append(rational(s.diff(radial_b(N+h*E),h).subs(h,0)))
    grad=s.Matrix(1,8,g);unit=s.zeros(1,7);unit[0]=1;assert grad*J==unit
    assert raw_bracket(C,Z,(1,2,3,5))==0
    controls=[]
    for tv in [anchor,anchor/2]:
        subs=prior|{a[0]:0,a[2]:values[u],a[3]:1/tv,a[7]:tv*values[q]}
        assert normalize(A.subs(subs)*Z,[0,1])==Nt.subs(t,tv)
        assert all(C.subs(values).subs(t,tv)[:,list(pair)].det()>=0 for pair in itertools.combinations(range(8),2))
        controls.append({'t':str(tv),'original_target_identity':True,'source_positivity':True})
    D=s.Matrix.vstack(normal,J[list(selected),:]);Db=s.Matrix.vstack(grad*J,J[list(selected),:]);assert D.det()!=0 and Db.det()!=0
    routes=[];densities=[]
    for history,coefficient in [(8,-1),(9,1)]:
        source=s.factor(coefficient/det);physical=s.factor(coefficient*slope/(prod*D.det()));inverse=s.factor(coefficient/(prod*Db.det()))
        assert source==physical==inverse
        densities.append(source);routes.append({'history_index':history,'source_shear_boundary_coefficient':coefficient,
            'source_residue_then_pushforward':str(source),'facet_pushforward_then_Y1678_residue':str(physical),
            'facet_pushforward_then_actual_reciprocal_alpha4_residue':str(inverse)})
    assert sum(densities)==0;hostile=s.factor(-densities[0]+densities[1]);assert hostile!=0
    return {'positive_Z_moment_shift':shift,'boundary_parameters':{str(z):str(values[z]) for z in remaining},
        'boundary_source_matrix':[[str(x) for x in row] for row in Cp.tolist()],
        'boundary_source_support':[1,2,3,5,6,7,8],'boundary_parallel_classes':[[2,3,5],[6,7,8]],
        'boundary_target_tangent_rank':6,'full_shear_facet_germ_rank':7,
        'symbolic_source_fiber_inverse_and_boundary_parameter_identity':True,
        'physical_second_normal':list(quad),'raw_symbolic_shear_pullback':str(p),'physical_normal_slope':str(slope),
        'actual_reciprocal_alpha4_normal':'b(Y)=Delta23(C)*Delta13(C)/(Delta36(C)*Delta12(C)) on pinned A fiber inverse',
        'inverse_radial_arc_identity':'b(target_shear_arc(t))=t identically','inverse_radial_target_gradient':[str(x) for x in grad],
        'selected_common_target_coordinate_indices':list(selected),'boundary_log_jacobian':str(det),
        'physical_normal_chart_jacobian':str(s.factor(D.det())),'inverse_radial_chart_jacobian':str(s.factor(Db.det())),
        'controls':controls,'routes':routes,'paired_target_density_sum':'0',
        'orientation_reversal_residual':str(hostile),'omit_shear_log_sign_in_one_route_residual':str(hostile)}


def main():
    prior=json.loads((ROOT/PRIOR).read_text());facet=json.loads((ROOT/FACET).read_text());previous=json.loads((ROOT/PREVIOUS).read_text());inv=json.loads((ROOT/INVERSES).read_text())
    for receipt,checker in [(prior,'research/benincasa/checkers/check_three_composite_normalizations.py'),
        (facet,'research/benincasa/checkers/check_shared_internal_composite_facet.py'),
        (previous,'research/benincasa/checkers/check_shared_facet_mixed_radial.py'),
        (inv,'research/benincasa/checkers/check_three_composite_inverse_normals.py')]:
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
        assert receipt['checker_sha256']==sha256((ROOT/checker).read_bytes()).hexdigest()
    rows={r['history_index']:r for r in prior['rows']};a,C,variables,witness=chart(rows);runs=[run(rows,a,C,variables,old) for old in facet['runs']]
    checks={'symbolic_shear_log_wedge_minus_one':True,'shared_positive_finite_source_germ':True,
        'merged_parallel_class235_and_two_rank6_boundaries':True,'two_rank7_facet_germs':True,
        'symbolic_actual_fiber_inverse_and_six_parameter_boundary_inverse':True,
        'physical_Y1678_and_reciprocal_alpha4_actual_normals':True,
        'two_exact_inverse_arc_identities_four_three_route_equalities_two_paired_sums_zero':True,
        'orientation_and_missing_log_sign_hostiles_nonzero':True}
    paths=[PRIOR,FACET,PREVIOUS,INVERSES,'research/benincasa/checkers/check_shared_facet_mixed_radial.py',
        'research/benincasa/checkers/check_shared_internal_composite_facet.py',
        'research/benincasa/checkers/check_three_composite_inverse_normals.py']
    out={'schema':'marici.benincasa.shared-facet-direction-merger.v1','source_witness':witness,'runs':runs,'checks':checks,'passed':True,
        'disposition':'adjacent235_direction_merger_positive_rank6_boundary_and_unweighted_paired_cancellation_constructed',
        'claim_boundary':'One balanced shear compactification of the actual shared Y1235 facet at two fixed Z; symbolic source wedge/inverse and local unweighted residues. Not complete invariant atlas, weighted component/sector comparison or global chain orientation.',
        'next_action':'Test the other omitted direction merger (3,5) with (6,7,8): alpha4=t*v,alpha7=r/t,alpha8=1/t, alpha3=u and alpha2,alpha5,alpha6 finite; normalize by diag(1,t). Derive the source wedge and classify source rank6 versus target contraction before any normal or residue claim. Then assemble the rank-two primitive boundary census, keeping contractions distinct.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=ROOT/'research/benincasa/results/shared_facet_direction_merger.json';path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'checks':checks,'paired_sums':[r['paired_target_density_sum'] for r in runs],'disposition':out['disposition']},indent=2))


if __name__=='__main__':main()
