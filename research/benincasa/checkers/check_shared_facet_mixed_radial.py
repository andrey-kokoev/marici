#!/usr/bin/env python3
"""Positive mixed radial scaling recovering the baseline-column6 boundary."""
import json
import sys
import itertools
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(Path(__file__).resolve().parent))
from check_shared_facet_correlated_radial import s,rational,normalize,target_jac,parameters,gradient,raw_bracket,setup_A,inverse_A
PRIOR='research/benincasa/results/three_composite_normalizations.json'
FACET='research/benincasa/results/shared_internal_composite_facet.json'
PREVIOUS='research/benincasa/results/shared_facet_correlated_radial.json'
INVERSES='research/benincasa/results/three_composite_inverse_normals.json'


def chart(rows):
    a,A,_=parameters(rows[8]['target_runs'][0]);_,H,_=parameters(rows[9]['target_runs'][0])
    t,u,v,w,r,q=s.symbols('t u v w r q');variables=[t,a[1],u,v,w,r,q]
    maps=[a[1],t*u,t*v,w/t,1/t,r/t,q/t]
    logJ=s.diag(*[1/x for x in maps])*s.Matrix(maps).jacobian(variables)*s.diag(*variables)
    assert s.factor(logJ.det())==-1
    substitution={a[0]:0,a[2]:t*u,a[3]:t*v,a[4]:w/t,a[5]:1/t,a[6]:r/t,a[7]:q/t}
    C=(s.diag(1,t)*A.subs(substitution,simultaneous=True)).applyfunc(rational)
    hs=substitution|{a[0]:a[1],a[1]:0}
    assert C==(s.diag(1,t)*H.subs(hs,simultaneous=True)).applyfunc(rational)
    assert C[:,3]==s.zeros(2,1) and all(rational(x)==0 for x in C[:,5]-s.Matrix([t*(u+v),t]))
    return a,C,variables,{'substitution':'alpha2 finite; alpha3=t*u,alpha4=t*v,alpha5=w/t,alpha6=1/t,alpha7=r/t,alpha8=q/t',
        'original_facet_order':['alpha2','alpha3','alpha4','alpha5','alpha6','alpha7','alpha8'],
        'mixed_order':[str(z) for z in variables],'log_wedge_jacobian':[[str(x) for x in row] for row in logJ.tolist()],
        'log_wedge_determinant':'-1','source_row_gauge':'diag(1,t); positive for t>0; not a form coefficient',
        'shared_source_germ':[[str(x) for x in row] for row in C.tolist()],
        'source_boundary_signs':[-1,1],'symbolic_paired_source_six_dlog_sum':'0'}


def extract_boundary(R):
    # Active source order (3,5,7,8,-1,-2), lower entry at column8 fixed to 1.
    pre=s.Matrix.hstack(R[:,2],R[:,4],R[:,6],R[:,7],-R[:,0],-R[:,1])
    W=s.Matrix.hstack(pre[:,0],pre[:,-1]);assert W.det()!=0
    B=(W.inv()*pre).applyfunc(rational);assert B[1,3]!=0
    canon=(s.diag(1,1/B[1,3])*B).applyfunc(rational)
    v=rational(canon[0,4]/canon[1,4]);u=rational(canon[0,3]-v)
    return [canon[0,1],u,v,canon[1,2],canon[1,4],canon[1,5]]


def run(rows,a,C,variables,old):
    shift=old['positive_Z_moment_shift'];Z=s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)])
    t,aa,u,v,w,r,q=variables;_,A,prior=parameters(rows[8]['target_runs'][shift])
    anchor=1/prior[a[5]]
    values={aa:prior[a[1]],u:prior[a[2]]/anchor,v:prior[a[3]]/anchor,
            w:prior[a[4]]*anchor,r:prior[a[6]]*anchor,q:prior[a[7]]*anchor}
    C0=C.subs(t,0);assert C0[:,3]==C0[:,5]==s.zeros(2,1)
    Cp=C0.subs(values);assert Cp.rank()==2
    assert all(Cp[:,list(pair)].det()>=0 for pair in itertools.combinations(range(8),2))
    Y=Cp*Z;N=normalize(Y,[0,1]);coords=[(i,j) for i in range(2) for j in range(6) if j not in (0,1)]
    J,actual=target_jac(Y,[C.diff(z).subs(t,0).subs(values)*Z for z in variables],[0,1]);assert actual==coords and J.rank()==7
    remaining=variables[1:];F=J[:,1:]*s.diag(*[values[z] for z in remaining]);assert F.rank()==6
    selected=next(I for I in itertools.combinations(range(8),6) if F[list(I),:].det()!=0)
    tangentdet=s.factor(F[list(selected),:].det());prod=s.prod(values[z] for z in remaining)
    # Six-active-label boundary inverse, independent of target scalar matching.
    support=[0,1,2,4,6,7];L=s.zeros(6,8);left=Z[support,:].inv()
    for j,label in enumerate(support):L[:,label]=left[:,j]
    assert L*Z==s.eye(6) and all(rational(x)==0 for x in C0*Z*L-C0)
    assert all(rational(x-y)==0 for x,y in zip(extract_boundary(C0*Z*L),remaining))
    assert extract_boundary(N*L)==[values[z] for z in remaining]
    physical=(1,2,7,8);p=raw_bracket(C,Z,physical);assert p!=0 and p.subs(t,0)==0
    pivot=s.factor((C*Z)[:,[0,1]].det());slope=s.factor(s.diff(p,t).subs(t,0).subs(values)/pivot.subs(t,0).subs(values));assert slope!=0
    gphysical=gradient(N,Z,physical,coords);normal=gphysical*J
    assert normal[0]==slope and all(normal[j]==0 for j in range(1,7))
    inverse_data=setup_A(Z,rows[8]['superfunction_runs'][0]['matches'][0])
    def radial_b(target):
        R,loc=inverse_A(target,inverse_data);den=rational(R[:,[2,7]].det())
        assert all(x!=0 for x in loc) and den!=0
        return rational(R[:,[2,5]].det()/den)
    assert radial_b(N)==0
    Nt=normalize(C.subs(values)*Z,[0,1]).applyfunc(rational)
    assert rational(radial_b(Nt)-t)==0
    h=s.symbols('h');g=[]
    for i,j in coords:
        E=s.zeros(2,6);E[i,j]=1;g.append(rational(s.diff(radial_b(N+h*E),h).subs(h,0)))
    grad=s.Matrix(1,8,g);unit=s.zeros(1,7);unit[0]=1;assert grad*J==unit
    assert raw_bracket(C,Z,(1,2,3,5))==0
    controls=[]
    for tv in [anchor,anchor/2]:
        subs={a[0]:0,a[1]:values[aa],a[2]:tv*values[u],a[3]:tv*values[v],a[4]:values[w]/tv,
              a[5]:1/tv,a[6]:values[r]/tv,a[7]:values[q]/tv}
        assert normalize(A.subs(subs)*Z,[0,1])==Nt.subs(t,tv)
        assert all(C.subs(values).subs(t,tv)[:,list(pair)].det()>=0 for pair in itertools.combinations(range(8),2))
        controls.append({'t':str(tv),'source_positivity':True,'original_facet_target_identity':True})
    D=s.Matrix.vstack(normal,J[list(selected),:]);Db=s.Matrix.vstack(grad*J,J[list(selected),:]);assert D.det()!=0 and Db.det()!=0
    routes=[];densities=[]
    for history,coefficient in [(8,-1),(9,1)]:
        source=s.factor(coefficient/tangentdet);bracket=s.factor(coefficient*slope/(prod*D.det()));inverse=s.factor(coefficient/(prod*Db.det()))
        assert source==bracket==inverse
        densities.append(source);routes.append({'history_index':history,'source_mixed_boundary_coefficient':coefficient,
            'mixed_source_residue_then_pushforward':str(source),'facet_pushforward_then_Y1278_residue':str(bracket),
            'facet_pushforward_then_actual_inverse_radial_residue':str(inverse)})
    assert sum(densities)==0;hostile=s.factor(-densities[0]+densities[1]);assert hostile!=0
    return {'positive_Z_moment_shift':shift,'mixed_parameters':{str(z):str(values[z]) for z in remaining},
        'boundary_source_support':[j+1 for j in support],'boundary_parallel_classes':[[3,5],[7,8]],
        'boundary_source_matrix':[[str(x) for x in row] for row in Cp.tolist()],
        'boundary_target_tangent_rank':6,'full_mixed_facet_germ_rank':7,
        'boundary_left_inverse':[[str(x) for x in row] for row in L.tolist()],
        'symbolic_boundary_inverse_parameter_identity':True,
        'physical_second_normal':list(physical),'raw_symbolic_mixed_pullback':str(p),'physical_normal_slope':str(slope),
        'actual_inverse_radial_normal':'b(Y)=Delta36(C_recovered)/Delta38(C_recovered) on pinned A source-fiber circuit',
        'inverse_radial_arc_identity':'b(target_mixed_arc(t))=t identically','inverse_radial_target_gradient':[str(x) for x in grad],
        'selected_common_target_coordinate_indices':list(selected),'boundary_log_jacobian':str(tangentdet),
        'physical_normal_chart_jacobian':str(s.factor(D.det())),'inverse_radial_chart_jacobian':str(s.factor(Db.det())),
        'controls':controls,'routes':routes,'paired_target_density_sum':'0',
        'orientation_reversal_residual':str(hostile),'omit_mixed_log_sign_in_one_route_residual':str(hostile)}


def main():
    prior=json.loads((ROOT/PRIOR).read_text());facet=json.loads((ROOT/FACET).read_text());previous=json.loads((ROOT/PREVIOUS).read_text());inv=json.loads((ROOT/INVERSES).read_text())
    for receipt,checker in [(prior,'research/benincasa/checkers/check_three_composite_normalizations.py'),
        (facet,'research/benincasa/checkers/check_shared_internal_composite_facet.py'),
        (previous,'research/benincasa/checkers/check_shared_facet_correlated_radial.py'),
        (inv,'research/benincasa/checkers/check_three_composite_inverse_normals.py')]:
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
        assert receipt['checker_sha256']==sha256((ROOT/checker).read_bytes()).hexdigest()
    rows={r['history_index']:r for r in prior['rows']};a,C,variables,witness=chart(rows)
    runs=[run(rows,a,C,variables,old) for old in facet['runs']]
    checks={'symbolic_mixed_log_wedge_determinant_minus_one':True,'shared_positive_finite_source_germ':True,
        'two_rank6_boundaries_rank7_mixed_facet_germs':True,'symbolic_six_support_boundary_inverse':True,
        'physical_Y1278_and_actual_inverse_radial_normals':True,'two_exact_inverse_mixed_arc_identities':True,
        'four_three_route_equalities_two_paired_sums_zero':True,'orientation_and_missing_log_sign_hostiles_nonzero':True}
    paths=[PRIOR,FACET,PREVIOUS,INVERSES,'research/benincasa/checkers/check_shared_facet_correlated_radial.py',
        'research/benincasa/checkers/check_shared_internal_composite_facet.py',
        'research/benincasa/checkers/check_three_composite_inverse_normals.py']
    out={'schema':'marici.benincasa.shared-facet-mixed-radial.v1','source_witness':witness,'runs':runs,'checks':checks,'passed':True,
        'disposition':'baseline_column6_positive_rank6_mixed_boundary_and_unweighted_paired_cancellation_constructed',
        'claim_boundary':'One mixed radial compactification of the actual Y1235 source facet at two fixed Z, symbolic source wedge/boundary inverse and local paired six-form cancellation. Not full invariant compactified atlas, weighted comparison or global orientation.',
        'next_action':'Test the remaining adjacent direction merger: alpha4=1/t, alpha8=t*q, alpha3=u finite and alpha2,alpha5,alpha6,alpha7 finite. Use source shear [[1,-1/t],[0,1]] to obtain a finite positive germ. Derive its wedge sign and test the merged parallel class (2,3,5), candidate physical Y1678 and actual reciprocal-alpha4 inverse normal before residues.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=ROOT/'research/benincasa/results/shared_facet_mixed_radial.json';path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'checks':checks,'paired_sums':[r['paired_target_density_sum'] for r in runs],'disposition':out['disposition']},indent=2))


if __name__=='__main__':main()
