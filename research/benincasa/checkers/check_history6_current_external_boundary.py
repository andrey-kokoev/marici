#!/usr/bin/env python3
"""Typed conditional transverse external-current boundary and radial anticommutation."""
import itertools
import json
from hashlib import sha256
from pathlib import Path
from check_history6_boundary_berezin_current import s, normalize, berezin_pair
ROOT=Path(__file__).resolve().parents[3]
ADMISSION='research/benincasa/results/history6_current_contour_admission.json'
TRANSPORT='research/benincasa/results/history6_current_gl3_transport.json'
LATTICE='research/benincasa/results/history6_current_projective_lattice.json'
CHART='research/benincasa/results/history6_common_corner.json'


def main():
    receipts={p:json.loads((ROOT/p).read_text()) for p in (ADMISSION,TRANSPORT,LATTICE,CHART)}
    for receipt in receipts.values():
        assert receipt['passed']
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    assert receipts[ADMISSION]['physical_admitted'] is False
    b=s.symbols('b1:9');b1,x,y,z,b5,b6,b7,b8=b
    C=s.Matrix([[s.sympify(q,locals={str(q):q for q in b}) for q in row] for row in receipts[CHART]['source_chart']])[:,[0,1,2,4,5,7]]
    D=normalize(C,[0,1]).applyfunc(s.factor);X=D[:,2:]
    # Actual source inverse from complementary bosonic incidence block Xstar.
    inverse=[-X[0,0]/X[1,0]]+[X[0,j-1]/X[1,j-1]-X[0,j]/X[1,j] for j in range(1,4)]+list(X[1,:])
    inverse=[s.factor(q) for q in inverse];assert inverse==list(b)
    normal_jac=s.Matrix([[s.diff(inverse[i],q) for q in b] for i in (1,2,3)])
    assert normal_jac==s.Matrix([[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0]])
    r,zeta,k,t=s.symbols('r s rho tau')
    F=[(r+zeta+1)/(r*(r+zeta)*(zeta+1)),1/(zeta*(r+zeta)*(zeta+1))]
    centers=[('p36_center',{x:0,y:0},z,{r:k*t,zeta:t},[-1/(k*(k+1)),-1/(k+1)]),
             ('p58_center',{y:0,z:0},x,{r:1/t,zeta:k},[-1/(k+1),-1/(k*(k+1))])]
    boundary_forms={}
    for name,center,remaining,sub,fiber in centers:
        jac=s.factor(s.Matrix([sub[r],sub[zeta]]).jacobian([k,t]).det())
        boundary=[s.factor(s.residue(-jac*q.subs(sub,simultaneous=True),t,0)) for q in F]
        assert boundary==fiber;boundary_forms[name]=boundary
    pairs=list(itertools.combinations(range(6),2));sector=[s.factor(D[:,list(p)].det()) for p in pairs]
    numerators=[(f'pair_{p[0]}_{p[1]}_four_sectors',q**4) for p,q in zip(pairs,sector)]
    numerators += [('mixed_sectors_1',sector[0]*sector[3]*sector[6]*sector[10]),
                   ('mixed_sectors_2',sector[4]*sector[5]*sector[8]*sector[14])]
    all_runs=[]
    for M in (s.eye(4),s.diag(2,3,5,7)):
        values=dict(zip(b,map(s.Integer,[2,0,0,0,5,7,11,13])))
        external=M*(-X.subs(values).T).row_join(s.eye(4));constraints=D*external.T
        coords=[(i,j) for i in range(2) for j in range(4)]
        Jmatrix=s.Matrix([[s.diff(constraints[i,j],q).subs(values) for q in b] for i,j in coords])
        J=s.factor(M.det()**2*b5*b6*b7*b8)
        assert Jmatrix.det()==J.subs(values) and Jmatrix.det()!=0
        assert D.subs(values)*external.T==s.zeros(2,4)
        full_component=berezin_pair(D.subs(values)[:,[0,5]])
        assert full_component==b8.subs(values)**4!=0
        base=b1*b5*b6*b7*b8
        runs=[]
        for label,N in numerators:
            U=s.factor(N/(base*J));U0=s.factor(U.subs({x:0,y:0,z:0}))
            routes=[]
            for name,center,remaining,sub,fiber in centers:
                # D_remaining(C)=ordered delta3 * Res_remaining(
                # dnu_remaining wedge C), normal first, on this family.
                # This is a DECLARED conditional holomorphic boundary
                # operation, not an assumed physical delta prescription.
                family=[s.factor(U.subs(center)*q/remaining) for q in fiber]
                external_route=[s.factor(s.residue(q,remaining,0)) for q in family]
                triple_route=[s.factor(-U0*q) for q in boundary_forms[name]]
                assert all(s.factor(a+b)==0 for a,b in zip(external_route,triple_route))
                # Equal-sign promotion is hostile whenever a component is
                # nonzero; it contradicts the two radial residue orders.
                hostile=[s.factor(a-b) for a,b in zip(external_route,triple_route)]
                transport=next(item for item in receipts[TRANSPORT]['both_P1_boundary_maps'] if item['center']==name)
                tubes=s.Matrix(transport['tube_columns_local_loop_zero_minus1'])
                period=s.Matrix(receipts[LATTICE]['split_period_matrix'])*tubes
                local_period=s.Matrix([[s.residue(q,k,p) for p in (0,-1)] for q in fiber])
                assert period==local_period
                for i in range(2):
                    for j,pole in enumerate((0,-1)):
                        assert s.factor(s.residue(external_route[i],k,pole)+(-U0*period[i,j]))==0
                routes.append({'center':name,'missing_external_normal':str(remaining),
                    'external_transverse_route':[str(q.subs(values)) for q in external_route],
                    'projective_radial_route':[str(q.subs(values)) for q in triple_route],
                    'anticommutator_defects':['0','0'],
                    'equal_sign_hostile_defects':[str(q.subs(values)) for q in hostile]})
            runs.append({'fermion_component':label,'center_coefficient':str(U0.subs(values)),'routes':routes})
        assert any(any(q!='0' for q in route['equal_sign_hostile_defects']) for item in runs for route in item['routes'])
        all_runs.append({'bosonic_complement_det':str(M.det()),'actual_constraint_Jacobian':str(Jmatrix.det()),
            'normalized_Berezin_chi1_chi8':str(full_component),'component_tests':runs})
    # A general holomorphic prefactor makes the same point: transverse
    # residue uses its support value, not derivatives or a fitted selector.
    h0,h1,h2=s.symbols('h0 h1 h2');jet=h0+h1*z+h2*z**2
    assert s.residue(jet/z,z,0)==h0
    paths=[ADMISSION,TRANSPORT,LATTICE,CHART,'research/benincasa/checkers/check_history6_current_contour_admission.py']
    out={'schema':'marici.benincasa.history6-current-external-boundary.v1','history_index':6,
        'inverse_incidence_normals':'For Xstar from Cz=0, b1=-X00/X10; nu2=X00/X10-X01/X11; nu3=X01/X11-X02/X12; nu4=X02/X12-X03/X13; scales b5..b8 are row2 entries.',
        'normal_independence':'Actual inverse composed with source chart is identity; ordered nu2,nu3,nu4 derivative matrix is the corresponding three identity rows. All scales and detM localized nonzero.',
        'conditional_boundary_operation':'D_missing(C)=ordered_delta(nu2,nu3,nu4)*Res_nu_missing(dnu_missing wedge coefficient_one_form), with normal differential first; center families use their explicit meromorphic 1/nu_missing coefficient. This is an explicit holomorphic extension, not a sourced physical measure.',
        'type_before':'P1-valued source7 incidence current: fiber1 minus external codim2=-1.',
        'type_after':'Both routes are source6 incidence currents: fiber1 minus external codim3=-2=6-8; fermionicdegree8, Berezin2880 unchanged. Not equal to the unresidued P2-valued source7 current.',
        'after_direction_period':'Fiber0 minus external codim3=-3, matching the conditional contour contract.',
        'route_law':'D_missing(E7_P1_family) = - Res_tau(E7_P2_triple) in fixed ordered external normals; the minus is the exchange of the two radial residue operations.',
        'support_amplitude':'U=N/(b1*b5*b6*b7*b8*J), holomorphic in nu2,nu3,nu4. P1 family coefficient U|two_normals=0 / nu_missing; triple amplitude U|three_normals=0.',
        'runs':all_runs,'component_factorization':'All15 same-sector fourth powers and two mixed products checked. The universal full numerator has holomorphic polynomial coefficients; transverse residue is support evaluation, so the route law extends to every mixed SU4 component by the same analytic identity.',
        'passed':True,'physical_admitted':False,
        'claim_boundary':'Typed conditional external-normal boundary compatibility and oriented anticommution at both centers with actual inverse-incidence normals/Jacobians. Not a physically selected external contour prescription or global gluing.',
        'next_action':'Freshly replay the local covariance, cycle and typed-boundary suite, audit owning source/contract for a genuinely selected full physical lift and external prescription, and record a closure report separating constructed conditional mathematics from unresolved physical selection/global attachment. No source choice may be fabricated from successful local checks.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_current_external_boundary.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'actual_normal_inverse_and_independence':True,'bosonic_incidence_fixtures':2,
        'component_route_cases':len(numerators)*2*2,'typed_route_grade':-2,'post_period_grade':-3,
        'physical_admitted':False},indent=2))

if __name__=='__main__':main()
