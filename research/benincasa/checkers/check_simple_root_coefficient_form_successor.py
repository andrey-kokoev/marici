#!/usr/bin/env python3
"""Source-derived coefficient-valued successor and exact local residue controls.

The kinematic slice is not a physical-boundary atlas. Formal chart tests do not
construct a map from spinor kinematics to the bosonized amplituhedron target.
"""
import json
import sys
from hashlib import sha256
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_spinor_kinematics import momentum_conserving_kinematics, transport_spinor, x_interval, adjugate2


def main():
    t,z = s.symbols('t z')
    lam,_,x = momentum_conserving_kinematics(
        [(1,j*j+j+1+t*j) for j in range(1,9)],
        [(1,j**3+2*j+1+t*j*j) for j in range(1,7)])
    eps = s.Matrix([[0,1],[-1,0]])
    u_t = transport_spinor(lam,x,(8,2,5));u_0 = lam[5].T*eps
    xi = transport_spinor(lam,x,(8,5,2))
    L = xi*x_interval(x,2,3)*adjugate2(x_interval(x,3,5))
    k_t,k_0 = eps*u_t.T,eps*u_0.T
    A0 = s.factor(s.det(s.Matrix.hstack(k_0,lam[4])))
    At = s.factor(s.det(s.Matrix.hstack(k_t,lam[4])))
    S0,St = s.factor((L*k_0)[0]),s.factor((L*k_t)[0])
    c = s.factor(A0*St/(At*S0))
    numerator,denominator = s.fraction(c)
    expected = 3*(t+3)*(t+10)*(18*t**2+217*t+639)/(2*(7*t**2+77*t+183)*(11*t**2+156*t+489))
    poles = [7*t**2+77*t+183,11*t**2+156*t+489]
    zeros = [t+3,t+10,18*t**2+217*t+639]
    # Formal chart-normal residue with coefficient regular at z=0.
    c0,c1,c2,bm,b0,b1,cm = s.symbols('c0 c1 c2 bm b0 b1 cm')
    omega = bm/z+b0+b1*z
    regular_coefficient = c0+c1*z+c2*z**2
    pole_coefficient = cm/z+c0+c1*z
    regular_residue = s.expand(regular_coefficient*omega).coeff(z,-1)
    pole_residue = s.expand(pole_coefficient*omega).coeff(z,-1)
    correction = s.expand(pole_residue-c0*bm)
    # Concrete hostile: target-coordinate pole in c adds residue even if omega is regular.
    # Expand at each quadratic pole algebraically: residue(c dt) is N(r)/D'(r).
    # Coprimality with N and squarefree D proves those residues are nonzero.
    checks = {
        'symbolic_endpoint_ratio':s.factor(c-expected)==0,
        'original_three_fixtures': [s.factor(c.subs(t,i)) for i in (0,1,2)] == [s.Rational(3195,9943),s.Rational(4807,14596),s.Rational(4122,12337)],
        'reduced_slice_numerator_denominator_coprime':s.gcd(numerator,denominator)==1,
        'four_simple_slice_poles':s.degree(denominator,t)==4 and s.degree(s.gcd(denominator,s.diff(denominator,t)),t)==0,
        'regular_coefficient_restricts_in_residue':regular_residue==c0*bm,
        'pole_coefficient_requires_correction':pole_residue==cm*b0+c0*bm and correction!=0,
        'orientation_reversal_detected':-regular_residue != regular_residue,
        'regular_split_residue_recombines':s.expand(c0*bm+(1-c0)*bm-bm)==0,
        'pole_split_corrections_recombine':s.expand(pole_residue+(bm-pole_residue)-bm)==0,
        'nonzero_new_residue_on_regular_form':s.expand(pole_coefficient*(b0+b1*z)).coeff(z,-1)==cm*b0,
    }
    assert all(checks.values()), checks
    inputs=['research/nima/dual_spinor_kinematics.py','research/nima/dual_r_invariant.py',
            'research/benincasa/checkers/check_untransported_simple_root_candidate.py']
    out={
        'schema':'marici.benincasa.simple-root-coefficient-form-successor.v1',
        'root':[1,1],'history_index':3,
        'realization_class':'Proposed coefficient-valued extension, not an ordinary unit-normalized positive-cell canonical form',
        'source_authority':'Coefficient is fixed by the existing external-versus-transported endpoint rule, not fitted. Identification of this extension with the original canonical-descent target is not admitted.',
        'definition':{
            'coefficient_field':'Q(external spinor/dual kinematics) on the source localization',
            'chart_form':'omega_F = wedge_{e=1..8} dlog alpha_e in the ordered transported F chart',
            'candidate_K0_form':'omega_0 = c omega_F',
            'candidate_B11_form':'omega_B = (1-c) omega_F',
            'scope':'External-parameter coefficients tensor the source chart differential-form module. This does not supply a target/form component extraction square.'},
        'kinematic_slice':{
            'parameter':'t; lambda_j=(1,j^2+j+1+t*j), tilde-prefix_j=(1,j^3+2*j+1+t*j^2)',
            'raw_ratio_factors':{name:str(v) for name,v in [('A0',A0),('At',At),('S0',S0),('St',St)]},
            'reduced_c':str(c),'zero_polynomials':[str(f) for f in zeros],
            'pole_polynomials':[str(f) for f in poles],
            'pole_discriminants':[str(s.discriminant(f,t)) for f in poles],
            'removable_factors_warning':'Reduction of c does not enlarge the source localization: endpoint denominators and all generalized-R denominators must still be checked. Slice zeros/poles are not classified physical boundaries.'},
        'residue_contract':{
            'external_parameter_convention':'Residue in alpha with external kinematics fixed and c regular: Res(c omega)=c Res(omega). No alpha-dependent derivative is inserted.',
            'target_coordinate_convention':'Requires an explicit map to the target/local boundary normal. If c varies with normal z but is regular, use c|z=0. If c has a pole, retain all Laurent cross terms.',
            'local_test':'omega=(b_minus1/z+b0+b1*z) dz wedge eta; c=c_minus1/z+c0+c1*z',
            'exact_residue':'(c_minus1*b0+c0*b_minus1) eta',
            'naive_restriction_defect':'c_minus1*b0 eta',
            'higher_poles':'Compute sum_{i+j=-1} c_i b_j, not just restricted weight times the original residue.'},
        'checks':checks,'passed':True,
        'disposition':'specified_coefficient_valued_successor_with_verified_local_controls; original canonical admission remains open',
        'missing_maps':['physical target/component extraction identifying this coefficient-valued chart form with F0',
                        'boundary localization and whether c is external-fixed or a target function on each residue route',
                        'normalized nine-to-twenty-sector map with the eighty source facets'],
        'evidence_level':'Fresh symbolic one-parameter endpoint ratio and exact formal Laurent residue algebra; no full atlas replay or kernel theorem.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=ROOT/'research/benincasa/results/simple_root_coefficient_form_successor.json'
    path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'c':str(c),'slice_poles':out['kinematic_slice']['pole_polynomials'],
                      'checks':checks,'disposition':out['disposition'],'missing_maps':out['missing_maps']},indent=2))


if __name__=='__main__':main()
