"""Photon Bose-carrier/invariant-amplitude dictionary; primary-text residual retained."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[3]
HOME=ROOT/'research/nima'
sys.path.insert(0,str(ROOT/'research/scattering/low-energy'))
import check_forward_photon_moments as mom
import check_forward_ir_subtraction as sub
ir=mom.ir;cut=ir.cut;ct=ir.ct
CONTRACT=HOME/'contracts/photon-normalization-v1.json'
IR_PROOF=ROOT/'research/scattering/low-energy/FORWARD-IR-SUBTRACTION.md'
WEAK_PROOF=ROOT/'research/scattering/low-energy/PACKET-WEAK-COUPLING-TAIL.md'
BORN_PROOF=ROOT/'research/scattering/low-energy/OUTGOING-BORN-MAP.md'
PROOF=HOME/'photon-normalization-v1.md'
TEST=HOME/'checkers/test_photon_normalization_v1.py'
MANIFEST=HOME/'scc-models/photon-normalization-v1.json'
RESULT=HOME/'results/photon-normalization-v1.json'


def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Q()) for j in range(len(B[0]))] for i in range(len(A))]


def adj(A):return [[A[j][i].conjugate() for j in range(len(A))] for i in range(len(A[0]))]
def scaled(A,c):return [[c*a for a in row] for row in A]


def phase_dictionary(identical_factor=Q(1,2)):
    # Coefficients with powers of pi written explicitly in labels, never numerically approximated.
    dPhi_dOmega_pi2=Q(1,32)
    dmu_to_dOmega_pi=Q(1,4)
    pi_times_c=identical_factor*dPhi_dOmega_pi2/dmu_to_dOmega_pi
    return pi_times_c


def invariant_pi_cut(g,f):
    """pi times Abs M at quadratic Born order for independent photon EFT contact coefficients."""
    return (g*g+Q(14,5)*f*f)/32,Q(5,48)*g*f,g*g/80


def direct_invariant_pi_cut(g,f):
    # Standard Born kernel, no b/2 stripping here: diag=g*s^2, off=f*(s^2+t^2+u^2).
    p=[Q(2),Q(-2),Q(2)];alpha2=[Q(),Q(),Q(1)];one_minus_alpha2=[Q(1),Q(-2),Q(1)]
    D=(g*g+f*f*mom.integrate(ct.multiply(p,p)))/32
    O=g*f*mom.integrate(p)/16
    M=g*g*mom.integrate(ct.add(ct.multiply(alpha2,alpha2),ct.multiply(one_minus_alpha2,one_minus_alpha2)))/32
    return D,O,M


def weighted_channel_pullback(M,roots):
    # v_i=roots_i^2/(16*pi); strip the common phase factor on both sides.
    W=[[roots[i]**2 if i==j else Q() for j in range(len(roots))] for i in range(len(roots))]
    U=[[roots[i] if i==j else Q() for j in range(len(roots))] for i in range(len(roots))]
    K=mm(mm(U,M),U)
    invariant_cut=mm(mm(adj(M),W),M)
    return mm(adj(K),K),mm(mm(U,invariant_cut),U)


def assert_standard_bridge(pi_times_c):
    assert pi_times_c==Q(1,16),'Bose phase-volume mismatch; do not patch internal cut coefficients'


def validate_contract(c):
    assert c['schema']=='marici.photon-normalization.v1'
    assert c['owner']=='marici.Nima'
    assert c['two_photon_measure']=='dPhi2/2!=dmu/(16*pi)'
    assert c['kernel_dictionary']=='T_red=M/(16*pi);S_Bose=I+i*T_red_operator'
    assert c['same_parameter_dictionary']=='M=(b/2)*(16*pi*A)+b^2*(16*pi*B_red)'
    assert c['same_Born_kernel_dictionary']=='lambda=16*pi*b;M=(lambda/2)*A+lambda^2*B_std;B_std=B_red/(16*pi)'
    assert c['earlier_g2_dictionary']=='b=|kappa*g2|^2*m^6/(128*pi^2)'
    assert c['common_Born_parameter_from_earlier_g2']=='lambda=|kappa*g2|^2*m^6/(8*pi)'
    for key in ('earlier_amplitude_normalized_g2_dictionary_derived','g3_remains_independent',
                'normalized_carrier_to_invariant_dictionary_derived','Bose_projection_and_phase_volume_kept_distinct',
                'same_parameter_and_reparameterized_coefficients_distinguished','standard_phase_space_Gram_regression_constructed',
                'review_target_reproduced'):
        assert c[key] is True,key
    for key in ('primary_source_regression_independently_verified','existing_reduced_coefficients_rescaled',
                'project_Dirac_coupling_equals_photon_EFT_Wilson_coefficient','physical_g2_or_g3_calibration_derived',
                'cross_sector_single_16pi_factor_derived','native_preparation_selected','physical_rates_or_branching_derived',
                'UV_completion_constructed','global_positivity_assumptions_admitted'):
        assert c[key] is False,key
    assert c['review_fixture']['primary_source_directly_verified'] is False
    assert c['review_fixture']['status']=='review_derived_targets_not_independently_transcribed_primary_equations'


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    assert_standard_bridge(phase_dictionary())
    assert 'degree n>=2' in IR_PROOF.read_text(encoding='utf-8')
    assert 'epsilon2=|lambda*g2|*m^3/(sqrt(128)*pi)' in WEAK_PROOF.read_text(encoding='utf-8')
    assert 'sqrt(Phi_in*Phi2/2!)*M^3*alpha' in BORN_PROOF.read_text(encoding='utf-8')
    b_pi_squared=Q(1,8)*Q(1,8)*Q(1,2)
    assert b_pi_squared==Q(1,128)
    assert 16*b_pi_squared==Q(1,8) and 8*b_pi_squared==Q(1,16)
    for n in (0,1):
        try:sub.analytic_coefficient({},n,Q(1,2),Q(1))
        except AssertionError:pass
        else:raise AssertionError('lower-degree coefficient formula accepted')
    # Common-amplitude optical conversion: pi * B_std = B_red/16, after lambda=16*pi*b.
    g,f=Q(1,4),Q(-1,4)
    standard=invariant_pi_cut(g,f)
    fminus,fplus,mixed=mom.pair_eigenvalues(2,2)
    reduced=((fminus+fplus)/2,(fplus-fminus)/2,mixed)
    assert reduced==(Q(19,160),Q(-5,48),Q(1,80))
    assert standard==tuple(x/16 for x in reduced)
    assert standard==tuple(map(Q,c['review_fixture']['pi_times_B_std_forward_D_O_M_for_R_s_squared']))
    gram_checks=0
    for g,f in ((Q(1),Q()),(Q(),Q(1)),(Q(1),Q(-1)),(Q(2),Q(3)),(Q(2,3),Q(-4,5))):
        D,O,M=invariant_pi_cut(g,f)
        assert (D,O,M)==direct_invariant_pi_cut(g,f)
        assert D>=abs(O) and M>=0;gram_checks+=1
    # Every allowed partial wave, including physical mixed Bose eigenvalue H (ordered diagonal H/2).
    partial_checks=0;mixed_checks=0
    for k in range(2,7):
        for l in range(2,7):
            ek=cut.equal_cross_moment(k,0);el=cut.equal_cross_moment(l,0)
            higher=sum((Q(2*J+1,8)*cut.equal_cross_moment(k,J)*cut.equal_cross_moment(l,J)
                        for J in range(2,min(k,l)+1,2)),Q())
            values=((1+ek)*(1+el)/8+higher,ek*el/8+higher,
                    sum((Q(2*J+1,16)*cut.mixed_cross_moment(k,J)*cut.mixed_cross_moment(l,J)
                         for J in range(2,min(k,l)+1)),Q()))
            assert values==mom.pair_eigenvalues(k,l);partial_checks+=1
    for J,H in ((2,Q(1,5)),(3,Q(-1,42))):
        sign=(-1)**J;A=[[H/2,sign*H/2],[sign*H/2,H/2]];squared=mm(A,A)
        assert squared[0][0]==H*H/2
        assert tuple(sum((A[i][j]*v for j,v in enumerate((Q(1),Q(sign)))),Q()) for i in range(2))==(H,sign*H)
        physical_cut=H*H/8;ordered_cut=squared[0][0]/8
        assert physical_cut==2*ordered_cut==4*((H/2)**2/8);mixed_checks+=1
    # Phase-shift convention: T_J=2*a_J. Exact S=(1+i*x)/(1-i*x) gives a=x/(1-i*x).
    phase_checks=0
    for x in (Q(),Q(1,3),Q(-2,5),Q(1)):
        real_a=x/(1+x*x);imag_a=x*x/(1+x*x)
        assert imag_a==real_a*real_a+imag_a*imag_a
        assert 2*(2*imag_a)==(2*real_a)**2+(2*imag_a)**2;phase_checks+=1
    # Distinct charged pair has v=beta/(8*pi), not photon 1/(16*pi).
    weighted_checks=0
    for u in (Q(1,2),Q(3,4),Q(1)):
        M=[[Q(1),Q(2,3)],[Q(-4,5),Q(7,3)]]
        lhs,rhs=weighted_channel_pullback(M,(Q(1),u));assert lhs==rhs;weighted_checks+=1
        beta=u*u/2;assert 2*beta==u*u
    refused=[]
    for name,value in (('omit_identical_particle_factor',Q(1)),('double_count_identical_particle_factor',Q(1,4))):
        try:assert_standard_bridge(phase_dictionary(value))
        except AssertionError:refused.append(name)
        else:raise AssertionError('phase-space hostile accepted')
    for key in ('primary_source_regression_independently_verified','existing_reduced_coefficients_rescaled',
                'project_Dirac_coupling_equals_photon_EFT_Wilson_coefficient','cross_sector_single_16pi_factor_derived',
                'physical_rates_or_branching_derived'):
        try:
            bad=copy.deepcopy(c);bad[key]=True;validate_contract(bad)
        except AssertionError:refused.append(key)
        else:raise AssertionError('unsupported normalization promotion: '+key)
    paths={CONTRACT,IR_PROOF,WEAK_PROOF,BORN_PROOF,PROOF,TEST,MANIFEST,Path(__file__).resolve()}
    for module in tuple(sys.modules.values()):
        path=getattr(module,'__file__',None)
        if path:
            p=Path(path).resolve()
            if p.suffix=='.py' and (ROOT/'research/scattering/low-energy') in p.parents:paths.add(p)
    return {'schema':'marici.photon-normalization-receipt.v1','status':'pass_with_primary_source_residual',
        'obligation':'readout_compatibility_on_declared_imported_Bose_carrier',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'normalization_pi_times_phase_weight':'1/16','b_pi_squared_per_abs_kappa_g2_m3_squared':str(b_pi_squared),
        'common_Born_lambda_pi_per_abs_kappa_g2_m3_squared':str(16*b_pi_squared),
        'invariant_Born_M_prefactor_pi_per_abs_kappa_g2_m3_squared':str(8*b_pi_squared),
        'pi_times_invariant_B_std_D_O_M':list(map(str,standard)),
        'reduced_B_D_O_M':list(map(str,reduced)),'independent_standard_phase_space_Gram_controls':gram_checks,
        'partial_wave_to_forward_checks':partial_checks,'mixed_Bose_projection_checks':mixed_checks,
        'phase_shift_convention_checks':phase_checks,'channel_weight_pullback_checks':weighted_checks,
        'E_n_domain_already_n_ge_2_in_current_project':True,
        **{k:v for k,v in c.items() if isinstance(v,bool)},
        'primary_source_residual':c['review_fixture']['retrieval_residual'],
        'reported_source_target_is_review_derived_not_primary_transcription':True,
        'general_L2_normalization_identity_machine_formalized':False,'hostile_controls_refused':refused}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale photon normalization receipt'
    else:
        RESULT.parent.mkdir(parents=True,exist_ok=True)
        RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','partial_wave_to_forward_checks','pi_times_invariant_B_std_D_O_M',
        'primary_source_regression_independently_verified','existing_reduced_coefficients_rescaled')}))


if __name__=='__main__':main()
