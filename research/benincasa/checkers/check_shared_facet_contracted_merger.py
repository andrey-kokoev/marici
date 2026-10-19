#!/usr/bin/env python3
"""Remaining adjacent merger: genuine source facet, contracted target and fiber."""
import json
import sys
import itertools
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(Path(__file__).resolve().parent))
from check_shared_facet_direction_merger import s,rational,normalize,target_jac,parameters
from check_composite_root_normalization import derivative
PRIOR='research/benincasa/results/three_composite_normalizations.json'
FACET='research/benincasa/results/shared_internal_composite_facet.json'
PREVIOUS='research/benincasa/results/shared_facet_direction_merger.json'


def chart(rows):
    a,A,_=parameters(rows[8]['target_runs'][0]);_,H,_=parameters(rows[9]['target_runs'][0])
    t,u,v,r=s.symbols('t u v r');variables=[t,a[1],u,v,a[4],a[5],r]
    maps=[a[1],u,t*v,a[4],a[5],r/t,1/t]
    logJ=s.diag(*[1/x for x in maps])*s.Matrix(maps).jacobian(variables)*s.diag(*variables)
    assert s.factor(logJ.det())==-1
    substitution={a[0]:0,a[2]:u,a[3]:t*v,a[6]:r/t,a[7]:1/t}
    C=(s.diag(1,t)*A.subs(substitution,simultaneous=True)).applyfunc(rational)
    hs=substitution|{a[0]:a[1],a[1]:0}
    assert C==(s.diag(1,t)*H.subs(hs,simultaneous=True)).applyfunc(rational)
    C0=C.subs(t,0);assert C0[1,:]==s.Matrix([[-r,-1,0,0,0,0,0,0]])
    assert all(C0[:,list(pair)].det()==0 for pair in itertools.combinations([2,4,5,6,7],2))
    return a,C,variables,{'substitution':'alpha4=t*v,alpha7=r/t,alpha8=1/t; alpha3=u and alpha2,alpha5,alpha6 finite',
        'new_order':[str(z) for z in variables],'source_row_gauge':'diag(1,t), positive for t>0; not a form scale',
        'log_wedge_jacobian':[[str(x) for x in rr] for rr in logJ.tolist()],'log_wedge_determinant':'-1',
        'shared_source_germ':[[str(x) for x in rr] for rr in C.tolist()],
        'boundary_source_signs':[-1,1],'symbolic_paired_source_six_dlog_sum':'0',
        'target_incidence':'At t=0, Y row2 = -r*Z1-Z2. Thus the target plane meets span(Z1,Z2) in a line.',
        'incidence_dimension_bound':'Choose the line in fixed two-space (dimension1), then a second line in the five-dimensional quotient (dimension4): image dimension at most5.'}


def run(rows,a,C,variables,old):
    shift=old['positive_Z_moment_shift'];Z=s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)])
    t,aa,u,v,a5,a6,r=variables;_,A,prior=parameters(rows[8]['target_runs'][shift]);anchor=1/prior[a[7]]
    values={aa:prior[a[1]],u:prior[a[2]],v:prior[a[3]]/anchor,a5:prior[a[4]],a6:prior[a[5]],r:prior[a[6]]*anchor}
    C0=C.subs(t,0);Cp=C0.subs(values);assert Cp.rank()==2
    assert all(Cp[:,list(pair)].det()>=0 for pair in itertools.combinations(range(8),2))
    remaining=variables[1:];Y=Cp*Z;N=normalize(Y,[0,1])
    J,coords=target_jac(Y,[C.diff(z).subs(t,0).subs(values)*Z for z in variables],[0,1])
    source_coords=[(i,j) for i in range(2) for j in range(8) if j not in (0,1)]
    source_derivatives=[derivative(Cp,C.diff(z).subs(t,0).subs(values),[0,1]) for z in variables]
    JS=s.Matrix([[d[i,j] for d in source_derivatives] for i,j in source_coords])
    assert J[:,1:].rank()==5 and J.rank()==6 and JS[:,1:].rank()==6 and JS.rank()==7
    assert Y[1,:]==-values[r]*Z[0,:]-Z[1,:]
    vanished=[]
    for i,j in itertools.combinations(range(3,9),2):
        quad=(1,2,i,j);assert s.Matrix.vstack(N,*[Z[k-1,:] for k in quad]).det()==0
        vanished.append(list(quad))
    # Explicit source fiber: add the active seven-label external kernel to row1,
    # then restore its canonical column2=0 and column3=1 gauge. CZ changes only
    # by a GL(2) row transformation, so normalized target Y is exactly unchanged.
    support=[0,1,2,4,5,6,7];null=Z[support,:].T.nullspace();assert len(null)==1
    k=s.zeros(1,8)
    for j,label in enumerate(support):k[label]=null[0][j]
    assert k*Z==s.zeros(1,6) and k[3]==0
    lam=s.symbols('lambda');den=1+lam*k[2]
    family=[rational((aa+lam*k[4])/den),rational((u+lam*k[5])/den),
        rational((v*r-lam*(k[0]-r*k[1]))/(r*den)),
        rational((u*a5+lam*k[6])/(u+lam*k[5])),rational((u*a6+lam*k[7])/(u+lam*k[5])),r]
    family_sub=dict(zip(remaining,family));Cfamily=C0.subs(family_sub,simultaneous=True).applyfunc(rational)
    D=C0+s.Matrix([lam,0])*k
    G=s.diag(1/den,1)*s.Matrix([[1,lam*k[1]],[0,1]])
    assert all(rational(x)==0 for x in Cfamily-G*D)
    # Formal fiber identity uses the exact kernel equation, not fitted samples.
    assert all(rational(x)==0 for x in Cfamily*Z-G*(C0*Z))
    family_at_point=[rational(x.subs(values)) for x in family]
    Cf=Cfamily.subs(values).applyfunc(rational)
    assert all(rational(x)==0 for x in normalize(Cf*Z,[0,1])-N)
    assert any(rational(x)!=0 for x in normalize(Cf,[0,1])-normalize(Cp,[0,1]))
    direction=s.Matrix([rational(s.diff(x,lam).subs(lam,0)) for x in family_at_point])
    assert direction!=s.zeros(6,1) and J[:,1:]*direction==s.zeros(8,1)
    assert JS[:,1:]*direction!=s.zeros(JS.rows,1)
    fiber_controls=[]
    for lv in [s.Rational(1,10000),-s.Rational(1,10000)]:
        fiber_parameters=[x.subs(lam,lv) for x in family_at_point];assert all(x>0 for x in fiber_parameters)
        point=Cf.subs(lam,lv);assert all(point[:,list(pair)].det()>=0 for pair in itertools.combinations(range(8),2))
        assert normalize(point*Z,[0,1])==N
        fiber_controls.append({'lambda':str(lv),'source_parameters':[str(x) for x in fiber_parameters],'source_positive':True,'target_identical':True})
    Nt=normalize(C.subs(values)*Z,[0,1]).applyfunc(rational);arc_controls=[]
    for tv in [anchor,anchor/2]:
        subs=prior|{a[0]:0,a[2]:values[u],a[3]:tv*values[v],a[6]:values[r]/tv,a[7]:1/tv}
        assert normalize(A.subs(subs)*Z,[0,1])==Nt.subs(t,tv)
        assert all(C.subs(values).subs(t,tv)[:,list(pair)].det()>=0 for pair in itertools.combinations(range(8),2))
        arc_controls.append({'t':str(tv),'original_chart_target_identity':True,'source_positive':True})
    return {'positive_Z_moment_shift':shift,'boundary_parameters':{str(z):str(values[z]) for z in remaining},
        'boundary_parallel_class':[3,5,6,7,8],'boundary_source_tangent_rank':6,'full_source_germ_rank':7,
        'boundary_target_tangent_rank':5,'full_target_germ_rank':6,
        'target_corner_point':[str(N[i,j]) for i,j in coords],'vanishing_fixed_line_incidence_brackets':vanished,
        'source_boundary_matrix':[[str(x) for x in rr] for rr in Cp.tolist()],
        'active_external_kernel':[str(x) for x in k],
        'source_fiber_parameter_order':[str(z) for z in remaining],'symbolic_source_fiber_parameter_map':[str(x) for x in family],
        'symbolic_source_fiber_identity':'Cfamily*Z=G*(C0*Z), with source Cfamily not GL-equivalent to C0',
        'source_fiber_tangent_vector':[str(x) for x in direction],
        'fiber_controls':fiber_controls,'arc_controls':arc_controls,
        'regular_boundary_inverse_status':'rejected_by_exact_positive_source_fiber_and_target_rank5',
        'ordinary_target_six_form_residue_status':'unavailable_contracted_codimension2_image_within_internal_target_facet',
        'paired_source_six_form_sum':'0','paired_target_density_sum':None,
        'orientation_hostile_source_coefficient_sum':2,
        'disposition':'genuine_rank6_positive_source_boundary_contracts_to_rank5_target_with_explicit_fiber'}


def main():
    prior=json.loads((ROOT/PRIOR).read_text());facet=json.loads((ROOT/FACET).read_text());previous=json.loads((ROOT/PREVIOUS).read_text())
    for receipt,checker in [(prior,'research/benincasa/checkers/check_three_composite_normalizations.py'),
        (facet,'research/benincasa/checkers/check_shared_internal_composite_facet.py'),
        (previous,'research/benincasa/checkers/check_shared_facet_direction_merger.py')]:
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
        assert receipt['checker_sha256']==sha256((ROOT/checker).read_bytes()).hexdigest()
    rows={r['history_index']:r for r in prior['rows']};a,C,variables,witness=chart(rows)
    runs=[run(rows,a,C,variables,old) for old in facet['runs']]
    checks={'symbolic_shared_source_germ_and_log_wedge_minus_one':True,
        'two_positive_source_rank6_boundaries_and_rank7_germs':True,'two_target_rank5_boundaries_and_rank6_germs':True,
        'fixed_two_space_line_incidence_and_thirty_bracket_checks':True,
        'symbolic_nontrivial_source_fiber_identity_and_two_exact_null_tangents':True,
        'four_positive_same_target_fiber_controls':True,'four_positive_original_chart_arc_controls':True,
        'source_pair_cancellation_and_orientation_hostile_retained':True,'ordinary_target_six_form_unavailability_not_false_zero':True}
    paths=[PRIOR,FACET,PREVIOUS,'research/benincasa/checkers/check_shared_facet_direction_merger.py',
        'research/benincasa/checkers/check_shared_internal_composite_facet.py',
        'research/benincasa/checkers/check_composite_root_normalization.py']
    out={'schema':'marici.benincasa.shared-facet-contracted-merger.v1','source_witness':witness,'runs':runs,'checks':checks,'passed':True,
        'disposition':'last_adjacent_source_direction_merger_is_target_contracted_with_exact_positive_fiber',
        'claim_boundary':'One actual primitive positive source merger, symbolic wedge/fiber identities and exact ranks at two fixed Z. Source cancellation does not give an ordinary target six-form square for a rank5 image; no weighted/global theorem or complete census yet.',
        'next_action':'Assemble the invariant primitive boundary census of this one rank-two source cell: active support7 with cyclic classes (1),(2),(3,5),(6,7,8), dimension m+r-4. Enumerate member deletions in nonsingleton classes and adjacent direction mergers; attach the five finite and three compactified regular receipts plus this contracted merger. Prove the one-step codimension1 enumeration and distinguish lower-dimensional coordinate contractions from primitive facets.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=ROOT/'research/benincasa/results/shared_facet_contracted_merger.json';path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'checks':checks,'ranks':[{'source':r['boundary_source_tangent_rank'],'target':r['boundary_target_tangent_rank']} for r in runs],
        'disposition':out['disposition']},indent=2))


if __name__=='__main__':main()
