#!/usr/bin/env python3
"""Correlated positive radial compactification of the actual shared facet."""
import json
import sys
import itertools
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(Path(__file__).resolve().parent))
from check_shared_internal_composite_facet import s,rational,normalize,target_jac,parameters,gradient,raw_bracket
from check_three_composite_inverse_normals import setup_A,inverse_A
PRIOR='research/benincasa/results/three_composite_normalizations.json'
FACET='research/benincasa/results/shared_internal_composite_facet.json'
INFINITY='research/benincasa/results/shared_internal_facet_infinity.json'
INVERSES='research/benincasa/results/three_composite_inverse_normals.json'


def chart(rows):
    a,A,_=parameters(rows[8]['target_runs'][0]);_,H,_=parameters(rows[9]['target_runs'][0])
    t,u,v=s.symbols('t u v');variables=[t,u,v,*a[4:]]
    maps=[1/t,u/t,v/t,*a[4:]];J=s.diag(*[1/x for x in maps])*s.Matrix(maps).jacobian(variables)*s.diag(*variables)
    assert s.factor(J.det())==-1
    substitution={a[0]:0,a[1]:1/t,a[2]:u/t,a[3]:v/t}
    C=(s.diag(t,1)*A.subs(substitution,simultaneous=True)).applyfunc(rational)
    hsub={a[0]:1/t,a[1]:0,a[2]:u/t,a[3]:v/t}
    assert C==(s.diag(t,1)*H.subs(hsub,simultaneous=True)).applyfunc(rational)
    assert C[:,2]==s.Matrix([t,0]) and C[:,3]==s.zeros(2,1)
    return a,C,variables,{'original_facet_order':['alpha2','alpha3','alpha4','alpha5','alpha6','alpha7','alpha8'],
        'radial_order':[str(z) for z in variables],'substitution':'alpha2=1/t,alpha3=u/t,alpha4=v/t; alpha5..8 unchanged',
        'log_wedge_jacobian':[[str(x) for x in row] for row in J.tolist()],'log_wedge_determinant':'-1',
        'source_row_gauge':'diag(t,1), positive for t>0; this gauge determinant is not a differential-form normalization',
        'shared_source_germ':[[str(x) for x in row] for row in C.tolist()],
        'facet_source_signs_before_radial_change':[1,-1],'radial_boundary_source_signs':[-1,1],
        'symbolic_paired_source_six_dlog_sum':'0'}


def boundary_extract(R):
    # Signed active order (5,6,7,8,-1,-2). Unique canonical gauge on this open.
    pre=s.Matrix.hstack(R[:,4],R[:,5],R[:,6],R[:,7],-R[:,0],-R[:,1])
    W=s.Matrix.hstack(pre[:,0],pre[:,-1]);assert W.det()!=0
    B=(W.inv()*pre).applyfunc(rational);assert B[1,1]!=0
    canon=(s.diag(1,1/B[1,1])*B).applyfunc(rational)
    vv=rational(canon[0,4]/canon[1,4]);uu=rational(canon[0,1]-vv)
    return [uu,vv,canon[1,2],canon[1,3],canon[1,4],canon[1,5]]


def run(rows,a,C,variables,old):
    shift=old['positive_Z_moment_shift'];Z=s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)])
    _,_,prior=parameters(rows[8]['target_runs'][shift]);t,u,v=variables[:3]
    values={u:prior[a[2]]/prior[a[1]],v:prior[a[3]]/prior[a[1]],**{z:prior[z] for z in a[4:]}}
    C0=C.subs(t,0);Y=C0.subs(values)*Z;N=normalize(Y,[0,1]);coords=[(i,j) for i in range(2) for j in range(6) if j not in (0,1)]
    assert C0[:,2]==C0[:,3]==s.zeros(2,1)
    assert all(C0.subs(values)[:,list(pair)].det()>=0 for pair in itertools.combinations(range(8),2))
    assert C0.subs(values).rank()==2
    J,actual=target_jac(Y,[C.diff(z).subs(t,0).subs(values)*Z for z in variables],[0,1]);assert actual==coords and J.rank()==7
    remaining=variables[1:];F=J[:,1:]*s.diag(*[values[z] for z in remaining]);assert F.rank()==6
    selected=next(I for I in itertools.combinations(range(8),6) if F[list(I),:].det()!=0)
    det=s.factor(F[list(selected),:].det());prod=s.prod(values[z] for z in remaining)
    # Explicit boundary inverse: the six active external vectors are a basis.
    support=[0,1,4,5,6,7];L=s.zeros(6,8);left=Z[support,:].inv()
    for j,label in enumerate(support):L[:,label]=left[:,j]
    assert L*Z==s.eye(6) and all(rational(x)==0 for x in C0*Z*L-C0)
    assert all(rational(x-y)==0 for x,y in zip(boundary_extract(C0*Z*L),remaining))
    assert boundary_extract(N*L)==[values[z] for z in remaining]
    # Actual physical normal, with a symbolic pullback on the radial germ.
    quad=(1,2,4,5);p=raw_bracket(C,Z,quad);assert p.subs(t,0)==0 and p!=0
    pivot=s.factor((C*Z)[:,[0,1]].det());slope=s.factor(s.diff(p,t).subs(t,0).subs(values)/pivot.subs(t,0).subs(values));assert slope!=0
    gphysical=gradient(N,Z,quad,coords);normal=gphysical*J
    assert normal[0]==slope and all(normal[j]==0 for j in range(1,7))
    # Genuine rational radial inverse on the ambient A fiber circuit. Unlike
    # canonical extraction, this ratio remains regular when column3 is zero.
    inverse_data=setup_A(Z,rows[8]['superfunction_runs'][0]['matches'][0])
    def radial_b(target):
        R,loc=inverse_A(target,inverse_data);d25=rational(R[:,[1,4]].det())
        assert all(x!=0 for x in loc) and d25!=0
        return rational(R[:,[1,2]].det()/d25)
    assert radial_b(N)==0
    Nt=normalize(C.subs(values)*Z,[0,1]).applyfunc(rational)
    assert rational(radial_b(Nt)-t)==0
    h=s.symbols('h');grad=[]
    for i,j in coords:
        E=s.zeros(2,6);E[i,j]=1
        grad.append(rational(s.diff(radial_b(N+h*E),h).subs(h,0)))
    grad=s.Matrix(1,8,grad);unit=s.zeros(1,7);unit[0]=1;assert grad*J==unit
    # The compact radial family itself stays on the actual internal facet.
    assert raw_bracket(C,Z,(1,2,3,5))==0
    arc_controls=[]
    for tv in [1/prior[a[1]],1/(2*prior[a[1]])]:
        substitutions=prior|{a[0]:0,a[1]:1/tv,a[2]:values[u]/tv,a[3]:values[v]/tv}
        _,A,_=parameters(rows[8]['target_runs'][shift])
        assert normalize(A.subs(substitutions)*Z,[0,1])==Nt.subs(t,tv)
        assert all(C.subs(values).subs(t,tv)[:,list(pair)].det()>=0 for pair in itertools.combinations(range(8),2))
        arc_controls.append({'t':str(tv),'source_positivity':True,'original_chart_target_identity':True})
    routes=[];densities=[]
    for history,coefficient in [(8,-1),(9,1)]:
        source=s.factor(coefficient/det)
        D=s.Matrix.vstack(normal,J[list(selected),:]);Dinv=s.Matrix.vstack(grad*J,J[list(selected),:])
        physical=s.factor(coefficient*slope/(prod*D.det()));inverse=s.factor(coefficient/(prod*Dinv.det()))
        assert source==physical==inverse
        densities.append(source);routes.append({'history_index':history,'radial_source_coefficient':coefficient,
            'radial_source_residue_then_pushforward':str(source),'facet_pushforward_then_Y1245_residue':str(physical),
            'facet_pushforward_then_actual_inverse_radial_residue':str(inverse),
            'physical_normal_chart_jacobian':str(s.factor(D.det())),'inverse_radial_chart_jacobian':str(s.factor(Dinv.det()))})
    assert sum(densities)==0;hostile=s.factor(-densities[0]+densities[1]);assert hostile!=0
    return {'positive_Z_moment_shift':shift,'radial_parameters':{str(z):str(values[z]) for z in remaining},
        'target_pivot':[1,2],'boundary_target_tangent_rank':6,'full_facet_radial_germ_rank':7,
        'boundary_source_support':[i+1 for i in support],'boundary_parallel_class':[6,7,8],
        'boundary_left_inverse':[[str(x) for x in row] for row in L.tolist()],
        'symbolic_boundary_inverse_parameter_identity':True,'boundary_target_point':[str(N[i,j]) for i,j in coords],
        'physical_second_normal':list(quad),'raw_symbolic_radial_pullback':str(p),'physical_normal_slope':str(slope),
        'actual_inverse_radial_normal':'b(Y)=Delta23(C_recovered)/Delta25(C_recovered) on the pinned A source-fiber inverse circuit',
        'inverse_radial_arc_identity':'b(target_radial_arc(t))=t identically',
        'inverse_radial_target_gradient':[str(x) for x in grad],
        'selected_common_target_coordinate_indices':list(selected),'boundary_log_jacobian':str(det),
        'arc_controls':arc_controls,'routes':routes,'paired_target_density_sum':'0',
        'omit_radial_sign_in_one_route_residual':str(hostile),'orientation_reversal_residual':str(hostile)}


def main():
    prior=json.loads((ROOT/PRIOR).read_text());facet=json.loads((ROOT/FACET).read_text());infinity=json.loads((ROOT/INFINITY).read_text());inv=json.loads((ROOT/INVERSES).read_text())
    for receipt,checker in [(prior,'research/benincasa/checkers/check_three_composite_normalizations.py'),
        (facet,'research/benincasa/checkers/check_shared_internal_composite_facet.py'),
        (infinity,'research/benincasa/checkers/check_shared_internal_facet_infinity.py'),
        (inv,'research/benincasa/checkers/check_three_composite_inverse_normals.py')]:
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
        assert receipt['checker_sha256']==sha256((ROOT/checker).read_bytes()).hexdigest()
    rows={r['history_index']:r for r in prior['rows']};a,C,variables,witness=chart(rows)
    runs=[run(rows,a,C,variables,old) for old in facet['runs']]
    checks={'symbolic_radial_log_wedge_determinant_minus_one':True,'shared_positive_source_germ_identity':True,
        'two_rank6_boundaries_and_rank7_radial_germs':True,'symbolic_and_sample_six_support_boundary_inverse':True,
        'physical_Y1245_and_actual_rational_radial_normals':True,'two_exact_radial_inverse_arc_identities':True,
        'four_three_route_residue_equalities_and_two_paired_sums_zero':True,'orientation_and_missing_radial_sign_hostiles_nonzero':True}
    paths=[PRIOR,FACET,INFINITY,INVERSES,'research/benincasa/checkers/check_shared_internal_composite_facet.py',
        'research/benincasa/checkers/check_shared_internal_facet_infinity.py',
        'research/benincasa/checkers/check_three_composite_inverse_normals.py',
        'research/benincasa/checkers/check_composite_root_normalization.py']
    out={'schema':'marici.benincasa.shared-facet-correlated-radial.v1','source_witness':witness,'runs':runs,'checks':checks,'passed':True,
        'disposition':'new_positive_rank6_correlated_infinity_boundary_and_unweighted_paired_residue_cancellation_constructed',
        'claim_boundary':'One explicit correlated radial chart of the actual shared Y1235 facet, two fixed Z, symbolic source wedge and boundary inverse, local six-form squares. Not complete compactified atlas, weighted component/sector comparison or global chain orientation.',
        'next_action':'Test the omitted baseline-column6 boundary with mixed scaling alpha3=t*u,alpha4=t*v,alpha5=w/t,alpha6=1/t,alpha7=r/t,alpha8=q/t and alpha2 finite. Normalize source by diag(1,t), derive the source log wedge Jacobian, and test the finite extra-zero-column6 image, rank and actual second normal before residue comparisons.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=ROOT/'research/benincasa/results/shared_facet_correlated_radial.json';path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'checks':checks,'paired_sums':[r['paired_target_density_sum'] for r in runs],'disposition':out['disposition']},indent=2))


if __name__=='__main__':main()
