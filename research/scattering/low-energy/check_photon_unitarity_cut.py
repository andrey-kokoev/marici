"""Subthreshold photon optical cuts on the Bose carrier and scoped IR-window dispersion."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from math import comb,factorial
from pathlib import Path
import check_crossed_four_photon as crossed

response=crossed.response;F=crossed.F;phase=crossed.phase
ROOT=crossed.ROOT;HOME=crossed.HOME
CONTRACT=HOME/'contracts/photon-unitarity-cut.v1.json';PROOF=HOME/'PHOTON-UNITARITY-CUT.md'
RESULT=HOME/'results/photon-unitarity-cut.v1.json'
WAVES=('J0_minus','J0_plus','J2_minus','J2_plus','J2_mixed')


def equal_cross_moment(k,J):
    assert isinstance(k,int) and k>=2 and isinstance(J,int) and J>=0 and J%2==0
    return (-1)**k*sum((Q((-1)**m*comb(J,m)*comb(J+m,m),k+m+1) for m in range(J+1)),Q())


def mixed_cross_moment(k,J):
    assert isinstance(k,int) and k>=2 and isinstance(J,int) and J>=2
    n=J-2;poly=[Q()]*(n+1)
    for m in range(n+1):
        for j in range(n-m+1):
            poly[m+j]+=comb(n,m)*comb(n+4,n-m)*comb(n-m,j)*(-1)**(n-m-j)
    return (-1)**k*sum((a/Q(k+j+3) for j,a in enumerate(poly)),Q())


def monomial_waves(k):
    e0=equal_cross_moment(k,0);e2=equal_cross_moment(k,2)
    return dict(zip(WAVES,(1+e0,-e0,e2,-e2,mixed_cross_moment(k,2))))


def zero_subtraction_wave_box(name,s,n=32):
    assert name in WAVES and 0<s<4 and n>=1
    total=sum((response.coefficient(j)*Q(s)**(j+4)*monomial_waves(j+4)[name] for j in range(n)),Q())
    factor=2 if name=='J0_minus' else 1
    error=factor*response.coefficient(n)*Q(s)**(n+4)/(1-Q(s)/4)
    return total-error,total+error  # pi-scaled A.


def ir_window_polynomial(q,mu=Q(1)):
    assert isinstance(q,int) and q>=4 and q%2==0 and 0<mu<4
    return {p:Q(mu)**(q-p)/Q(q-p) for p in range(2,q)}


def zero_point_IR_subtractions_exist(q,n):
    assert isinstance(q,int) and q>=4 and isinstance(n,int) and n>=0
    return n<=q


def validate_contract(c):
    assert c['schema']=='marici.scattering.photon-unitarity-cut.v1'
    assert c['window']=='0<s<4;pure_g2_power4_coefficient;only_photon_pair_at_retained_order'
    assert c['normalization']=='T=(b/2)*A+b^2*B+...;b=epsilon2^2;ImB=A_dagger*A/8'
    assert c['Bose_carriers']=='J0:2;J1:0;even_J>=2:3;odd_J>=3:1'
    assert c['IR_right_cut_log']=='-(kappa/pi)*s^q*log(-s);ImB~kappa*s^q'
    for key in ('full_helicity_sums_on_Bose_carrier_retained','orthogonal_scalar_photon_cut_retained',
                'general_J_projection_moments_constructed','real_subtraction_data_retained',
                'finite_IR_window_distinguished_from_UV_completion','independent_dimensionful_couplings_retained'):
        assert c[key] is True,key
    for key in ('single_ordered_entry_squared_is_full_Bose_cut','extra_open_channels_can_reduce_fixed_photon_cut',
                'leading_photon_complement_may_be_deleted','arbitrary_zero_point_oversubtraction_allowed',
                'right_cut_log_is_already_full_crossed_IR_germ','massless_cut_absent_at_all_orders',
                'higher_order_cut_repairs_order_g2_squared_Cayley_germ','pointwise_unitarity_supplies_dispersion',
                'crossed_order_g2_power4_cuts_constructed','all_orders_scattering_constructed',
                'subtraction_constants_source_selected','local_interacting_QFT_constructed','native_source_licensed',
                'physical_rates_or_branching_derived','live_proposition_inventory_changed','C12_protocol_renewed',
                'high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=crossed.build();assert parent==json.loads(crossed.RESULT.read_text(encoding='utf-8')),'stale crossed tensor'
    # Full ordered helicity kernel, before imposing the Bose quotient.
    labels=((1,1),(-1,-1),(1,-1),(-1,1));matrix_checks=0
    for cosine,sine,E in ((Q(),Q(1),Q(1)),(Q(3,5),Q(4,5),Q(1)),(Q(3,5),Q(4,5),Q(2))):
        ks=crossed.kinematics(cosine,sine,E);matrices=[[[F() for _ in labels] for _ in labels] for _ in range(3)]
        s=F(4*E*E);t=-s*(1-cosine)/2;u=-s*(1+cosine)/2
        for i,out in enumerate(labels):
            for j,inc in enumerate(labels):
                terms=crossed.tensor_terms(crossed.tensor_cache(ks,crossed.polarizations(inc+out,cosine,sine)))
                for n in range(3):
                    matrices[n][i][j]=sum((a*response.analytic.power(y,n) for y,a in terms),F())
        for n,M in enumerate(matrices):
            R=lambda y:response.analytic.power(y,n+2)
            rs,rt,ru=R(s),R(t),R(u);z=F()
            expected=[[rs/2,-(rs+rt+ru)/2,z,z],[-(rs+rt+ru)/2,rs/2,z,z],
                      [z,z,ru/2,rt/2],[z,z,rt/2,ru/2]]
            assert M==expected;matrix_checks+=1
    moment_checks=0
    for k in range(2,13):
        for J in (0,2,4,6):
            expected=Q() if k<J else Q((-1)**(k+J)*factorial(k)**2,factorial(k-J)*factorial(k+J+1))
            assert equal_cross_moment(k,J)==expected;moment_checks+=1
        for J in range(2,8):
            expected=Q() if k<J else Q((-1)**k*factorial(k-2)*factorial(k+2),factorial(k-J)*factorial(k+J+1))
            assert mixed_cross_moment(k,J)==expected;moment_checks+=1
    # Coherent normalized Bose vector, not a single ordered helicity component.
    for J,D in ((2,Q(1,10)),(3,Q(-1,84))):
        sign=(-1)**J;A=[[F(D),F(sign*D)],[F(sign*D),F(D)]]
        v=[[F(1)/phase.SQ2],[F(sign)/phase.SQ2]]
        out=phase.mm(A,v);norm=phase.mm(phase.adj(out),out)[0][0]
        assert norm==F(4*D*D) and norm!=F(D*D)
        forbidden=[[F(1)/phase.SQ2],[-F(sign)/phase.SQ2]]
        assert phase.mm(A,forbidden)==[[F()],[F()]]
    regimes={}
    expected_cuts=((Q(2,9),Q(1,72),Q(1,7200),Q(1,7200),Q(1,200)),
                   (Q(9,128),Q(1,128),Q(1,3200),Q(1,3200),Q(1,288)),
                   (Q(1,200),Q(1,7200),Q(1,88200),Q(1,88200),Q(1,14112)))
    for index,(case,k,r,common) in enumerate((('c0_nonzero',2,Q(1),'c0^2'),
                                             ('c0_zero_c1_nonzero',3,Q(1),'c1^2'),
                                             ('both_zero',4,Q(1,6),'1/pi^2'))):
        amplitudes={w:r*a for w,a in monomial_waves(k).items()}
        cuts={w:a*a/8 for w,a in amplitudes.items()}
        assert tuple(cuts[w] for w in WAVES)==expected_cuts[index]
        regimes[case]={'IR_power':2*k,'common_factor':common,'ImB_leading_coefficients':{w:str(a) for w,a in cuts.items()}}
    # Certified full subthreshold cut values for the zero-subtraction control.
    # The crossed receipt inherits hashes, not the parent's result fields; use its checked parent receipt.
    r_receipt=json.loads(response.RESULT.read_text(encoding='utf-8'))
    pi_lo=Q(r_receipt['pi_from_J2_identity_box']['lower']);pi_hi=Q(r_receipt['pi_from_J2_identity_box']['upper'])
    cut_boxes={}
    for s in (Q(1),Q(2)):
        cut_boxes[str(s)]={}
        for w in WAVES:
            lo,hi=zero_subtraction_wave_box(w,s)
            lower=Q() if lo<=0<=hi else min(lo*lo,hi*hi)
            upper=max(lo*lo,hi*hi)
            assert 0<lower<=upper
            cut_boxes[str(s)][w]={'ImB_lower':str(lower/(8*pi_hi*pi_hi)),'ImB_upper':str(upper/(8*pi_lo*pi_lo))}
    logs={};identities=0
    log2_lo,log2_hi=response.log_ratio_box(Q(1,3))
    for q in (4,6,8):
        p=ir_window_polynomial(q);poly=sum((a*(-1)**j for j,a in p.items()),Q())
        assert 0<poly+log2_lo<poly+log2_hi
        logs[str(q)]={'pi_scaled_BIR_over_kappa_at_s_minus1_lower':str(poly+log2_lo),
                      'pi_scaled_BIR_over_kappa_at_s_minus1_upper':str(poly+log2_hi)}
        assert zero_point_IR_subtractions_exist(q,q) and not zero_point_IR_subtractions_exist(q,q+1)
        for s in (Q(-1,2),Q(-1),Q(-2)):
            for t in (Q(),Q(1,2),Q(1)):
                lhs=s*s*t**(q-2)/(t-s)
                rhs=sum((s**j*t**(q-j-1) for j in range(2,q)),Q())+s**q/(t-s)
                assert lhs==rhs;identities+=1
    refused=[]
    for name in ('single_ordered_entry_squared_is_full_Bose_cut','extra_open_channels_can_reduce_fixed_photon_cut',
                 'leading_photon_complement_may_be_deleted','arbitrary_zero_point_oversubtraction_allowed',
                 'right_cut_log_is_already_full_crossed_IR_germ','higher_order_cut_repairs_order_g2_squared_Cayley_germ',
                 'pointwise_unitarity_supplies_dispersion','all_orders_scattering_constructed'):
        try:
            bad=copy.deepcopy(c);bad[name]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported photon-cut promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((crossed.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_photon_unitarity_cut.py'))
    return {'schema':'marici.scattering.photon-unitarity-cut-receipt.v1','status':'pass',
        'scope_verdict':'conditional_subthreshold_order_g2_power4_photon_cut_on_Bose_carrier_not_full_crossed_or_unitary_dynamics',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'full_helicity_matrix_checks':matrix_checks,'general_J_moment_checks':moment_checks,
        'mixed_Bose_norm_squared_over_single_ordered_diagonal_squared':'4',
        'IR_regimes':regimes,'zero_subtraction_cut_boxes':cut_boxes,'IR_window_log_witnesses':logs,
        'IR_window_log_witness_scope':'leading_monomial_density_not_the_full_cut_spectrum',
        'IR_integrand_division_checks':identities,'general_J_and_dispersion_argument_machine_formalized':False,
        **{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale photon unitarity cut'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','full_helicity_matrix_checks','general_J_moment_checks',
        'orthogonal_scalar_photon_cut_retained','all_orders_scattering_constructed','hostile_controls_refused')}))


if __name__=='__main__':main()
