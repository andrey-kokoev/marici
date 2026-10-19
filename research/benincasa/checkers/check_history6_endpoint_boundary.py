#!/usr/bin/env python3
"""History6 endpoint ratio and external-fixed coefficient boundary extraction.

The spinor coefficient and positive bosonized Z are independent base data;
no physical identification of these external spaces is silently supplied.
"""
import json
import sys
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
sys.path.insert(0,str(ROOT/'research/nima'))
sys.path.insert(0,str(Path(__file__).resolve().parent))
import sympy as s
from check_untransported_simple_root_candidate import retain
from dual_r_invariant import generalized_r
from dual_spinor_kinematics import angle, momentum_conserving_kinematics, transport_spinor, x_interval, adjugate2
from nnmhv_coherence_paths import compile_nnmhv_histories, terminal_r_state
CORNER='research/benincasa/results/history6_common_corner.json'


def coefficient(t):
    lam,_,x=momentum_conserving_kinematics(
        [(1,j*j+j+1+t*j) for j in range(1,9)],
        [(1,j**3+2*j+1+t*j*j) for j in range(1,7)])
    eps=s.Matrix([[0,1],[-1,0]])
    ut=transport_spinor(lam,x,(8,2,6));u0=lam[6].T*eps
    xi=transport_spinor(lam,x,(8,6,2))
    L=xi*x_interval(x,2,3)*adjugate2(x_interval(x,3,6))
    kt,k0=eps*ut.T,eps*u0.T
    factors={name:s.factor(q) for name,q in [
        ('A0',s.det(s.Matrix.hstack(k0,lam[5]))),
        ('At',s.det(s.Matrix.hstack(kt,lam[5]))),('S0',(L*k0)[0]),('St',(L*kt)[0])]}
    c=s.factor(factors['A0']*factors['St']/(factors['At']*factors['S0']))
    return c,factors


def evaluate(shift,c_symbol,t):
    lam,_,x=momentum_conserving_kinematics(
        [(1,j*j+j+1+shift*j) for j in range(1,9)],
        [(1,j**3+2*j+1+shift*j*j) for j in range(1,7)])
    eps=s.Matrix([[0,1],[-1,0]])
    h=compile_nnmhv_histories(8)[6];st=terminal_r_state(h)
    assert h.outer_pair==(2,6) and h.inner_pair==(3,6) and h.inner_prefix==(6,2)
    assert st.upper_spinor.vertices==(8,2,6) and st.lower_spinor.vertices==(2,)
    _,outer=generalized_r(lam,x,8,(),h.outer_pair,lam[1].T*eps,lam[6].T*eps)
    lower=transport_spinor(lam,x,st.lower_spinor.vertices)
    pt,updated=generalized_r(lam,x,8,h.inner_prefix,h.inner_pair,lower,transport_spinor(lam,x,st.upper_spinor.vertices))
    p0,unupdated=generalized_r(lam,x,8,h.inner_prefix,h.inner_pair,lower,lam[6].T*eps)
    c=s.factor(unupdated['prefactor']/updated['prefactor'])
    assert c==s.factor(c_symbol.subs(t,shift)) and c not in (0,1,-1)
    assert updated['xi_coefficients']==unupdated['xi_coefficients']
    assert set(pt)==set(p0) and all(s.factor(p0[k]-c*pt[k])==0 for k in pt)
    q=updated['xi_coefficients'];qo=outer['xi_coefficients']
    wedge=qo.get(2,0)*q.get(3,0)-qo.get(3,0)*q.get(2,0)
    selector=s.factor(wedge**4/angle(lam,2,3)**4);assert selector!=0
    K=s.factor(outer['prefactor']*updated['prefactor']*selector)
    K0=s.factor(outer['prefactor']*unupdated['prefactor']*selector);B=s.factor(K-K0)
    assert K0==c*K and B==(1-c)*K
    assert all(v!=0 for meta in (outer,updated,unupdated) for v in meta['denominator_factors'])
    return {'shift':shift,'c':str(c),'outer':retain(outer),'transported_inner':retain(updated),
        'untransported_inner':retain(unupdated),'inner_sparse_polynomial_coefficients_checked':len(pt),
        'component':{'selector':'product_A eta2^A eta3^A / <23>^4','K':str(K),'K0':str(K0),'B22':str(B)}}


def main():
    t=s.Symbol('t');c,factors=coefficient(t);num,den=s.fraction(c)
    runs=[evaluate(shift,c,t) for shift in (0,1,2)]
    assert len({r['c'] for r in runs})==3
    assert s.gcd(num,den)==1 and s.degree(s.gcd(den,s.diff(den,t)),t)==0
    corner=json.loads((ROOT/CORNER).read_text())
    assert corner['passed'] and corner['derived_reference_coefficient']=='1'
    for p,h in corner['source_sha256'].items(): assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    assert corner['checker_sha256']==sha256((ROOT/'research/benincasa/checkers/check_history6_common_corner.py').read_bytes()).hexdigest()
    boundary=[]
    # Relative differential forms over the external base: dc=0 in the b and Y
    # directions. Existing actual normal/Jacobian squares can be tensored by c.
    for r in runs:
        weight=s.Rational(r['c'])
        for q in corner['runs']:
            D=s.Rational(q['source_corner_then_pushforward'])
            assert D==s.Rational(q['top_pushforward_then_target_residues'])==s.Rational(q['first_source_residue_then_target_residue'])
            d0=weight*D;db=(1-weight)*D
            assert d0+db==D and -2*d0!=0
            only_K0=(weight-1)*D;assert only_K0!=0
            boundary.append({'spinor_shift':r['shift'],'independent_positive_Z_shift':q['positive_Z_moment_shift'],
                'K0_three_route_density':str(d0),'B22_three_route_density':str(db),
                'K0_plus_B22_minus_transported':'0','H5_A8_H9_plus_K0_residual':str(only_K0),
                'H5_A8_H9_plus_K0_plus_B22_residual':'0','K0_orientation_flip_defect':str(-2*d0)})
    # A pole in an externally parametrized coefficient cannot be restricted
    # naively if a later extraction turns that parameter into a normal.
    z=s.Symbol('z');cm,c0,wm,w0=s.symbols('cm c0 wm w0')
    pole_res=s.expand((cm/z+c0)*(wm/z+w0)).coeff(z,-1)
    assert pole_res==cm*w0+c0*wm and pole_res-c0*wm==cm*w0
    sources=[CORNER,'research/benincasa/checkers/check_history6_common_corner.py',
        'research/nima/dual_r_invariant.py','research/nima/dual_spinor_kinematics.py',
        'research/nima/nnmhv_coherence_paths.py','research/benincasa/checkers/check_untransported_simple_root_candidate.py']
    out={'schema':'marici.benincasa.history6-endpoint-boundary.v1','history_index':6,'root':[2,2],
        'symbolic_endpoint_identity':{'xi_path':[8,6,2],'transported_upper_path':[8,2,6],'omitted_update_upper_path':[6],
            'L':'xi*x23*adjugate(x36)','A':'det[epsilon*u^T,lambda5]','S':'L*epsilon*u^T',
            'c':'A0*St/(At*S0)','full_superfunctions':'F0=c Ft; Ft-F0=(1-c)Ft',
            'reason':'Boundary endpoint enters angle_b and denominator factor 1 only; eta linear form is endpoint independent.'},
        'slice':{'parameter':'t in the existing momentum-conserving spinor family',
            'raw_endpoint_factors':{k:str(v) for k,v in factors.items()},'reduced_c':str(c),
            'zero_factorization':str(s.factor(num)),'pole_factorization':str(s.factor(den)),
            'simple_pole_count':int(s.degree(den,t)),
            'source_localization':'All outer and both inner denominators nonzero; At*S0 and <23> nonzero. Cancellation in reduced c does not enlarge this domain. Slice divisors are not identified physical facets.'},
        'runs':runs,'boundary_extraction':{
            'domain':'Q(external spinor data) tensor relative chart differential forms on the F branch; positive bosonized Z is independent base data.',
            'top_forms':'omega0=c omegaF; omegaB22=(1-c)omegaF, proposed coefficient-valued extension, not unit canonical admission',
            'differential_pushforward':'E_dR(f omegaF)=f (CZ)_*omegaF, target pivot12 and row-major free coordinates; coefficient is external-fixed.',
            'boundary_map':'E_dR,corner(f Res_b4 Res_b2 omegaF)=f (CZ_corner)_*(Res_b4 Res_b2 omegaF)',
            'source_corner':'b2=b4=0; source deletion order b2 then b4; parity -1; reference transition -1',
            'target_normals':['Y1268','Y1235'],'relative_normal_residue':'With external base fixed, c has no b/target-normal dependence, so each actual three-route square tensors by c or 1-c.',
            'top_component_map':'On the named generator only: omega0 -> c Ft -> K0; omegaB22 -> (1-c)Ft -> B22. Verified scalar superfunction extraction, not a boundary-superfunction map.',
            'pole_warning':'If a later map makes c depend on a target normal, recompute Laurent extraction; pole correction cm*w0 is not optional.'},
        'boundary_runs':boundary,'passed':True,
        'not_constructed':['ordinary untransported canonical-cell admission','map identifying spinor coefficient base with bosonized external Z','boundary supercomponent extraction','global BCFW orientation/covering','weighted nine-to-sector comparison'],
        'next_action':'Construct a source-authorized link between the external spinor coefficient and bosonized boundary extraction, or test ordinary seed admission of history6 F0; do not promote the external-fixed tensor square to the original weighted map.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in sources},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=ROOT/'research/benincasa/results/history6_endpoint_boundary.json'
    path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'c':str(c),'fixture_ratios':[r['c'] for r in runs],
        'pole_factorization':str(s.factor(den)),'boundary_product_base_tests':len(boundary),'not_constructed':out['not_constructed']},indent=2))

if __name__=='__main__': main()
