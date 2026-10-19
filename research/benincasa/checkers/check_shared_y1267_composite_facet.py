#!/usr/bin/env python3
"""Y1267 positive facet nonoverlap and an actual shared codimension-two corner."""
import json
import sys
import itertools
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(Path(__file__).resolve().parent))
from check_shared_composite_physical_facet import (s,rational,normalize,target_jac,setup_A,setup_H,inverse_A,inverse_H,extract,parameters)
PRIOR='research/benincasa/results/three_composite_normalizations.json'
INVERSES='research/benincasa/results/three_composite_inverse_normals.json'
PREVIOUS='research/benincasa/results/shared_composite_physical_facet.json'


def symbolic_transitions(rows,Z):
    a,A,_=parameters(rows[8]['target_runs'][0]);_,H,_=parameters(rows[9]['target_runs'][0])
    basis=[0,1,2,4,5,6];L=s.zeros(6,8);left=Z[basis,:].inv()
    for j,label in enumerate(basis):L[:,label]=left[:,j]
    assert L*Z==s.eye(6)
    relation=Z[3,:]*left;assert list(relation)==[s.Rational(1,20),-s.Rational(3,10),s.Rational(3,4),s.Rational(3,4),-s.Rational(3,10),s.Rational(1,20)]
    Y=A.subs(a[5],0)*Z;R=(Y*L).applyfunc(rational)
    assert R[:,3]==R[:,7]==s.zeros(2,1) and R[:,[2,4]].det()==0
    forward,_,_=extract(R,rows[9]['superfunction_runs'][0]['matches'][0])
    expected=-a[0]*(6*a[4]+1)/(5*a[4]*(3*a[0]+4))
    assert rational(forward[1]-expected)==0
    # Reverse lift on the seven active labels. Kernel fixed by the same relation.
    k=s.zeros(1,8);k[3]=1
    for j,label in enumerate(basis):k[label]=-relation[j]
    assert k*Z==s.zeros(1,6)
    q=-20*a[1]*a[4]/(6*a[4]+1);S=(H.subs(a[5],0)+s.Matrix([q,0])*k).applyfunc(rational)
    assert all(rational(v)==0 for v in S*Z-H.subs(a[5],0)*Z)
    assert S[:,7]==s.zeros(2,1)
    assert all(rational(S[:,list(pair)].det())==0 for pair in [(2,3),(2,4),(5,6)])
    reverse,_,_=extract(S,rows[8]['superfunction_runs'][0]['matches'][0])
    expected_reverse=-20*a[1]*a[4]/(15*a[1]*a[4]+6*a[4]+1)
    assert rational(reverse[0]-expected_reverse)==0
    for expression,variables in [(expected,(a[0],a[4])),(expected_reverse,(a[1],a[4]))]:
        num,den=s.fraction(s.factor(-expression))
        assert all(c>0 for c in s.Poly(num,*variables).coeffs()) and all(c>0 for c in s.Poly(den,*variables).coeffs())
    # The zero of the sign obstruction identifies a common source corner exactly.
    hcorner={a[0]:a[1],a[1]:0,a[5]:0}
    assert A.subs({a[0]:0,a[5]:0})==H.subs(hcorner,simultaneous=True)
    assert all(rational(v.subs(a[0],0)-w)==0 for v,w in zip(forward,[a[1],0,a[2],a[3],a[4],0,a[6],a[7]]))
    return {'external_Z4_basis_relation':[str(v) for v in relation],
        'A_to_H_parameters':[str(s.factor(v)) for v in forward],
        'H_to_A_parameters':[str(s.factor(v)) for v in reverse],
        'forward_negative_parameter':'H alpha2=-A alpha1*(6*A alpha5+1)/(5*A alpha5*(3*A alpha1+4))',
        'reverse_negative_parameter':'A alpha1=-20*H alpha2*H alpha5/(15*H alpha2*H alpha5+6*H alpha5+1)',
        'strict_positive_coefficient_sign_certificates':True,
        'common_corner':'A(history8): alpha1=alpha6=0; H(history9): alpha2=alpha6=0',
        'common_corner_transition':'H alpha1=A alpha2; alpha3,alpha4,alpha5,alpha7,alpha8 unchanged; both vanished pairs zero',
        'common_corner_source_matrix_identity':True}


def compare(rows,Z,shift,donor,receiver):
    a,C,vals=parameters(rows[donor]['target_runs'][shift]);_,D,_=parameters(rows[receiver]['target_runs'][shift]);e=5;vals[a[e]]=0
    N=normalize(C.subs(vals)*Z,[0,1]);emb=rows[receiver]['superfunction_runs'][0]['matches'][0]
    R,loc=inverse_A(N,setup_A(Z,emb)) if receiver==8 else inverse_H(N,setup_H(Z,emb))
    pars,gauge,_=extract(R,emb);rv=dict(zip(a,pars))
    assert pars[e]==0 and all(pars[j]!=0 for j in range(8) if j!=e) and all(v!=0 for v in loc+gauge)
    assert normalize(D.subs(rv)*Z,[0,1])==N
    if donor==8:assert pars[1]==-vals[a[0]]*(6*vals[a[4]]+1)/(5*vals[a[4]]*(3*vals[a[0]]+4))
    else:assert pars[0]==-20*vals[a[1]]*vals[a[4]]/(15*vals[a[1]]*vals[a[4]]+6*vals[a[4]]+1)
    coords=[(i,j) for i in range(2) for j in range(6) if j not in (0,1)];free=[j for j in range(8) if j!=e];Js=[];LJs=[]
    for chart,values in [(C,vals),(D,rv)]:
        J,actual=target_jac(chart.subs(values)*Z,[chart.diff(z).subs(values)*Z for z in a],[0,1]);assert actual==coords and J.det()!=0
        Js.append(J);LJs.append(J[:,free]*s.diag(*[values[a[j]] for j in free]))
    selected=next(I for I in itertools.combinations(range(8),7) if all(J[list(I),:].det()!=0 for J in LJs))
    quad=[0,1,5,6];assert s.Matrix.vstack(N,Z[quad,:]).det()==0
    grad=[]
    for i,j in coords:
        E=s.zeros(2,6);E[i,j]=1
        grad.append(s.Matrix.vstack(E[0,:],N[1,:],Z[quad,:]).det()+s.Matrix.vstack(N[0,:],E[1,:],Z[quad,:]).det())
    grad=s.Matrix(1,8,grad);routes=[];densities=[]
    for J,LJ,values in zip(Js,LJs,[vals,rv]):
        normals=grad*J;slope=normals[e];assert slope!=0 and all(normals[j]==0 for j in free)
        det=s.factor(LJ[list(selected),:].det());detD=s.factor(s.Matrix.vstack(normals,J[list(selected),:]).det())
        route=s.factor((-1)**e/det);targetroute=s.factor(slope/(s.prod(values[a[j]] for j in free)*detD));assert route==targetroute and -route!=targetroute
        densities.append(route);routes.append({'source_residue_then_pushforward':str(route),'top_pushforward_then_shared_bracket_residue':str(targetroute),
            'source_deletion_sign':(-1)**e,'normal_slope':str(slope),'boundary_log_jacobian':str(det),'orientation_failure_residual':str(-route-targetroute)})
    difference=s.factor(densities[0]-densities[1]);total=s.factor(sum(densities));assert difference!=0 and total!=0
    dm=[C.subs(vals)[:,list(pair)].det() for pair in itertools.combinations(range(8),2)]
    rm={','.join(str(j+1) for j in pair):s.factor(D.subs(rv)[:,list(pair)].det()) for pair in itertools.combinations(range(8),2)}
    assert all(v>=0 for v in dm) and any(v<0 for v in rm.values())
    return {'positive_Z_moment_shift':shift,'donor_history':donor,'receiver_history':receiver,'shared_divisor':'Y1267=0','source_boundary':'alpha6=0',
        'receiver_parameters':{str(z):str(rv[z]) for z in a},'receiver_localization_values':[str(v) for v in loc+gauge],
        'receiver_negative_minors':{k:str(v) for k,v in rm.items() if v<0},'algebraic_overlap_regular':True,'positive_overlap':False,
        'selected_common_target_coordinate_indices':list(selected),'target_boundary_point':[str(N[i,j]) for i,j in coords],
        'routes':routes,'receiver_over_donor_density_ratio':str(s.factor(densities[1]/densities[0])),
        'density_sum':str(total),'density_difference':str(difference),
        'residual_disposition':'outside receiving positive branch; not an admitted weighted cancellation counterexample'}


def corner_rank(rows,Z,shift):
    a,A,values=parameters(rows[8]['target_runs'][shift]);values[a[0]]=values[a[5]]=0
    _,H,_=parameters(rows[9]['target_runs'][shift]);hv=values|{a[0]:values[a[1]],a[1]:0}
    assert A.subs(values)==H.subs(hv)
    J,_=target_jac(A.subs(values)*Z,[A.diff(z).subs(values)*Z for z in a],[0,1]);free=[1,2,3,4,6,7]
    rank=J[:,free].rank();assert rank==6 and J.rank()==8
    C=A.subs(values);assert all(C[:,list(pair)].det()>=0 for pair in itertools.combinations(range(8),2))
    return {'positive_Z_moment_shift':shift,'history8_parameters':{str(z):str(values[z]) for z in a},
        'history9_parameters':{str(z):str(hv[z]) for z in a},'source_matrix_equality':True,'source_positivity':True,
        'target_tangent_rank':rank,'ordinary_full_target_rank':J.rank(),
        'disposition':'actual shared positive codimension-two source corner with six-dimensional target image; paired iterated residues not yet computed'}


def main():
    prior=json.loads((ROOT/PRIOR).read_text());inverses=json.loads((ROOT/INVERSES).read_text());prev=json.loads((ROOT/PREVIOUS).read_text())
    for receipt,checker in [(prior,'research/benincasa/checkers/check_three_composite_normalizations.py'),
        (inverses,'research/benincasa/checkers/check_three_composite_inverse_normals.py'),
        (prev,'research/benincasa/checkers/check_shared_composite_physical_facet.py')]:
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
        assert receipt['checker_sha256']==sha256((ROOT/checker).read_bytes()).hexdigest()
    rows={r['history_index']:r for r in prior['rows']};runs=[];certificates=[];corners=[]
    for shift in (0,1):
        Z=s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)])
        certificates.append({'positive_Z_moment_shift':shift,**symbolic_transitions(rows,Z)})
        for donor,receiver in [(8,9),(9,8)]:runs.append(compare(rows,Z,shift,donor,receiver))
        corners.append(corner_rank(rows,Z,shift))
    checks={'four_regular_same_target_algebraic_overlaps':True,'eight_shared_normal_local_residue_squares':True,
        'four_positive_facet_interiors_rejected':True,'four_symbolic_directional_sign_certificates':True,
        'nonzero_algebraic_sums_differences_and_orientation_hostiles_retained':True,
        'symbolic_common_positive_corner_source_identity':True,'two_corner_tangent_rank6_full_rank8_controls':True}
    paths=[PRIOR,INVERSES,PREVIOUS,'research/benincasa/checkers/check_shared_composite_physical_facet.py',
        'research/benincasa/checkers/check_three_composite_inverse_normals.py','research/benincasa/checkers/check_composite_nonlinear_target_normal.py',
        'research/benincasa/checkers/check_composite_root_normalization.py']
    out={'schema':'marici.benincasa.shared-y1267-composite-facet.v1','histories':[8,9],'runs':runs,'symbolic_transitions':certificates,
        'shared_corner_controls':corners,'checks':checks,'passed':True,
        'disposition':'positive_facet_interiors_nonoverlapping_but_actual_shared_positive_codimension_two_corner_identified',
        'claim_boundary':'Fixed-Z rational inverse/transition algebra and common target residues. Shared corner is actual source-matrix equality, not equal divisor labels. No paired iterated residue or weighted nine-form cancellation theorem is asserted.',
        'next_action':'Compute paired iterated residues at history8 alpha1=alpha6=0 and history9 alpha2=alpha6=0, taking alpha6 residue first in both. Use the explicit shared corner transition, common six-dimensional target entries and fixed deletion parity; test orientation reversal. Keep unweighted local cancellation distinct from missing weighted component/sector map.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=ROOT/'research/benincasa/results/shared_y1267_composite_facet.json';path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'checks':checks,'disposition':out['disposition']},indent=2))


if __name__=='__main__':main()
