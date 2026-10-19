#!/usr/bin/env python3
"""Localized boundary Berezin/incidence current, retaining exceptional direction.

Holomorphic delta symbols are normalized algebraic constraint currents, not
real Dirac measures or ordinary bosonized target forms. Target change explicit.
"""
import json
import itertools
from hashlib import sha256
from pathlib import Path
from check_three_composite_internal_gluings import s, normalize
from check_history6_bosonization_bridge import bos_entry, wedge, add, power4_full, normalization
ROOT=Path(__file__).resolve().parents[3]
GENERIC='research/benincasa/results/history6_generic_top_bridge.json'
DIRECTIONS='research/benincasa/results/history6_directional_boundaries.json'
CHART='research/benincasa/results/history6_common_corner.json'
SOURCE='research/sources/nima/papers/six-point-nmhv/1212.5605/positive_grassmannian_update.tex'


def berezin_pair(Q):
    # Test the actual normalized operator on arbitrary two-generator fermion
    # rows, not a scalar rule merely declared to reproduce a desired residue.
    a,b=bos_entry(0,list(Q[0,:])),bos_entry(0,list(Q[1,:]))
    c,d=bos_entry(1,list(Q[0,:])),bos_entry(1,list(Q[1,:]))
    determinant=wedge(a,d)
    for mask,value in wedge(b,c).items():add(determinant,mask,-value)
    return s.factor(power4_full(determinant)/normalization())


def main():
    generic=json.loads((ROOT/GENERIC).read_text());directions=json.loads((ROOT/DIRECTIONS).read_text());chart=json.loads((ROOT/CHART).read_text())
    for receipt in (generic,directions,chart):
        assert receipt['passed']
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    text=(ROOT/SOURCE).read_text(encoding='utf-8')
    assert r'\label{general_on_shell_function_momentum_twistors}' in text
    assert '4\\hat{k}' in text
    b=s.symbols('b1:9');b1,b2,b3,b4,b5,b6,b7,b8=b
    C=s.Matrix([[s.sympify(q,locals={str(z):z for z in b}) for q in row] for row in chart['source_chart']])[:,[0,1,2,4,5,7]]
    D=normalize(C,[0,1]).applyfunc(s.factor)
    X=D[:,2:]
    coords=[(i,j) for i in range(2) for j in range(4)]
    J=s.Matrix([[s.diff(X[i,j],z) for z in b] for i,j in coords])
    jac=s.factor(J.det());assert jac==b5*b6*b7*b8
    # Fix complementary bosonic columns M. Incidence constraints are
    # D z = (X-X_star) M^T; determinant of the eight constraints is det(M)^2
    # times the source-chart ordinary Jacobian, at their actual common zero.
    runs=[]
    for values,M in [([2,3,0,7,11,13,17,19],s.eye(4)),
                     ([3,5,0,11,13,17,19,23],s.diag(2,3,5,7))]:
        v=dict(zip(b,map(s.Integer,values)));Xstar=X.subs(v)
        z=M*(-Xstar.T).row_join(s.eye(4))
        assert D.subs(v)*z.T==s.zeros(2,4)
        constraints=D*z.T
        constraintJac=s.Matrix([[s.diff(constraints[i,j],u).subs(v) for u in b] for i,j in coords])
        det=s.factor(constraintJac.det());assert det==M.det()**2*jac.subs(v) and det!=0
        # Generic top incidence kernel coefficient for the chi1/chi8 pair in
        # every SU4 sector. All other fermion components use the same map by
        # the proved universal two-row identity (no boundary degree shortcut).
        Q=D[:,[0,5]];n=berezin_pair(Q)
        assert n==s.factor(Q.det()**4)==b8**4
        top=s.factor(n/(s.prod(b)*M.det()**2*jac))
        g=b3*(b2+b3+b4)/((b2+b3)*(b3+b4))
        regular0=s.factor(s.residue(g*top,b3,0));regularB=s.factor(s.residue((1-g)*top,b3,0))
        regularF=s.factor(s.residue(top,b3,0));assert regular0==0 and regularB==regularF
        expected=s.factor(n.subs(b3,0)/(s.prod(u for u in b if u!=b3)*M.det()**2*jac.subs(b3,0)))
        assert regularB==expected
        # Six integrated base variables at the external codimension-two
        # support nu2=nu3=0; rho remains a differential variable.
        center={b2:0,b3:0};base=[b1,b4,b5,b6,b7,b8]
        A=s.factor(n.subs(center)/(s.prod(base)*M.det()**2*jac.subs(center)))
        rho=s.Symbol('rho');fiber0=-A/(rho*(1+rho));fiberB=-A/(1+rho)
        endpoint0=s.factor(s.residue(fiber0,rho,0));endpointB=s.factor(s.residue(fiberB,rho,0))
        pole0=s.factor(s.residue(fiber0,rho,-1));poleB=s.factor(s.residue(fiberB,rho,-1))
        u=s.Symbol('u');inverse0=s.factor(fiber0.subs(rho,1/u)*(-1/u**2));inverseB=s.factor(fiberB.subs(rho,1/u)*(-1/u**2))
        infinity0=s.factor(s.residue(inverse0,u,0));infinityB=s.factor(s.residue(inverseB,u,0))
        coeffs=[(endpoint0,endpointB),(pole0,poleB),(infinity0,infinityB)]
        assert coeffs==[(-A,s.Integer(0)),(A,-A),(s.Integer(0),A)]
        assert sum(pair[0] for pair in coeffs)==sum(pair[1] for pair in coeffs)==0
        for result,pair in zip(directions['directional_source_and_decorated_target_routes'],coeffs):
            assert pair[0]==s.Rational(result['exceptional_then_direction_K0'])*A
            assert pair[1]==s.Rational(result['exceptional_then_direction_B22'])*A
        # Source exceptional order (b1,rho,b4,..) -> drho first gives minus1.
        # The codimension-two constraint current is ordered delta(nu2)
        # delta(nu3); both residue signs are kept, rather than fitted.
        runs.append({'complementary_bosonic_matrix':[[str(q) for q in row] for row in M.tolist()],
            'source_boundary_parameters':{str(z):str(q) for z,q in v.items()},
            'incidence_constraint_Jacobian':str(det),'constraint_current_order':'row1 four constraints then row2 four constraints',
            'normalized_Berezin_chi1_chi8_coefficient':str(n),
            'regular_boundary_K0_current_coefficient':'0','regular_boundary_B22_current_coefficient':str(regularB.subs(v)),
            'exceptional_shared_fermionic_current_coefficient':str(A.subs(v)),
            'exceptional_K0_rho_one_form':str(s.factor(fiber0.subs(v))),
            'exceptional_B22_rho_one_form':str(s.factor(fiberB.subs(v))),
            'directional_current_coefficients':[[str(s.factor(q.subs(v))) for q in pair] for pair in coeffs]})
    paths=[GENERIC,DIRECTIONS,CHART,SOURCE,'research/benincasa/checkers/check_history6_generic_top_bridge.py',
        'research/benincasa/checkers/check_history6_bosonization_bridge.py','research/nima/momentum_twistor_super.py']
    out={'schema':'marici.benincasa.history6-boundary-berezin-current.v1','history_index':6,
        'source_authority':{'path':SOURCE,'equation':'general_on_shell_function_momentum_twistors',
            'kernel':'delta^{8|8}(C dot (z,chi)); source dimension minus8 is the bosonic form/current degree',
            'extension_status':'Localized holomorphic incidence-current extension of the sourced delta integral to boundary support; not a claim that the source paper supplies an ordinary negative-degree on-shell function.'},
        'delta_convention':'Ordered algebraic holomorphic constraint currents; delta(A nu)=det(A)^(-1) delta(nu). No absolute-value Jacobian or unchosen real contour is used.',
        'top_normalization':'In C12 gauge J_constraints=det(M)^2*b5*b6*b7*b8. Fermionic factor N=product_A((Cstar chi)_1^A wedge (Cstar chi)_2^A)=[phi_top]det2(phi Cstar chi)^4/2880.',
        'regular_boundary_map':{'source':'Res_b3 omega_split, seven logarithmic variables, fermionic degree8',
            'codomain':'Fermionic-degree8 external codimension-one constraint current delta(nu3), nu3=b3(Cstar(z)); no ordinary generic superfunction is asserted.',
            'formula':'E7(B22)=delta(nu3)*N/(product_b_except3 * J_constraints) evaluated on nu3=0; E7(K0)=0 on the regular b2*b4 nonzero localization.',
            'normal':'nu3, source coefficient parity+1; multiplying the top map by dnu3 then taking its scalar residue gives the same current coefficient.'},
        'exceptional_direction_retaining_map':{'source':'Res_T radial omega_split in order(b1,rho,b4,b5,b6,b7,b8)',
            'codomain':'Fermionic-degree8 external codimension-two current delta(nu2)delta(nu3) valued in meromorphic one-forms of retained rho.',
            'formula':'E7(K0)=-A delta(nu2)delta(nu3) drho/[rho(1+rho)]; E7(B22)=-A delta(nu2)delta(nu3) drho/(1+rho), A=N/(b1*b4*b5*b6*b7*b8*J_constraints)|center.',
            'orientation':'rho moves across b1 to the front with signminus1; constraint normal order nu2 then nu3 fixed.',
            'grading':'source7 minus eight bosonic constraints=-1; fiber differential degree1 minus external constraint codimension2=-1. Fermionic degree remains8 and full Berezin factor2880 is retained.',
            'localization':'b1,b4,b5,b6,b7,b8 and det(M) nonzero; rho retained. rho=-1 extra meromorphic pole cannot be dropped or relabeled positive.',
            'not_an_ordinary_target_form':True},
        'runs':runs,'passed':True,
        'claim_boundary':'Constructed local distribution-valued boundary Berezin/incidence maps with exact Jacobian, normalized exterior-algebra coefficients and retained direction; not an ordinary bosonized blowdown seven-form, globally defined contour/current cycle, superamplitude theorem or weighted-sector admission.',
        'next_action':'Verify covariance under changes of the source/kernel pivot and external normal coordinates, including determinant/sign factors, before gluing these local incidence currents or comparing them to a physical boundary contour prescription.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_boundary_berezin_current.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'codomain':'external constraint currents valued in full fermionic degree8; exceptional current retains rho one-form',
        'normalization':2880,'runs':runs,'scope':out['claim_boundary']},indent=2))

if __name__=='__main__':main()
