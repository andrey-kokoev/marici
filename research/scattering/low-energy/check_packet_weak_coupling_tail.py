"""Compact Born-error bounds and nonuniform weak-coupling limits for a normalizable mass tail."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from math import factorial
from pathlib import Path
import check_on_shell_unitary_completion as shell

born=shell.born;F=shell.F;phase=shell.phase;ROOT=shell.ROOT;HOME=shell.HOME
CONTRACT=HOME/'contracts/packet-weak-coupling-tail.v1.json'
PROOF=HOME/'PACKET-WEAK-COUPLING-TAIL.md'
RESULT=HOME/'results/packet-weak-coupling-tail.v1.json'
DELTA=Q(1,16)


def conversion(y,eta):
    y=Q(y);assert y>=0 and eta in (0,1)
    q2=y*(1+eta*y)**2
    return q2/(1+q2/4)**2


def density(M):
    M=Q(M);assert M>2
    return 30*(M-2)**2/(M-1)**6


def tail_weight(L):
    L=Q(L);assert L>=2
    r=1/(L-1)
    return 10*r**3-15*r**4+6*r**5


def round_down(q,unit):return Q((q.numerator*unit)//q.denominator,unit)
def round_up(q,unit):return -round_down(-q,unit)


def asymptotic_constant_bounds(p,eta,cells=2048):
    """Rigorous Darboux enclosure of 30*b*integral t^-4 F_eta(t^(2p)) dt."""
    assert p in (3,6) and eta in (0,1) and cells==2048
    T=Q(4 if eta==0 else 2);h=T/cells;lo=Q();hi=Q()
    def nd(t):
        z=t**(2*p);v=1+eta*z
        # Numerator and denominator have nonnegative coefficients and are increasing.
        return t**(2*p-4)*v*v,(1+z*v*v/4)**2
    aN,aD=nd(Q())
    for i in range(1,cells+1):
        bN,bD=nd(i*h)
        lo+=round_down(h*aN/bD,10**8)
        hi+=round_up(h*bN/aD,10**8)
        aN,aD=bN,bD
    degree=2*p if eta==0 else 6*p
    hi+=Q(16,3+degree)/T**(3+degree)
    factor=Q(30) if p==3 else Q(20)
    return round_down(factor*lo,100),round_up(factor*hi,100)


def validate_contract(c):
    assert c['schema']=='marici.scattering.packet-weak-coupling-tail.v1'
    assert c['compact_delta_squared']=='1/16'
    assert c['tail_mass_amplitude']=='sqrt(30)*(M-2)/(M-1)^3;M>2;m=1'
    assert c['source_choices']==['pure_singlet_S','pure_triplet_S']
    assert c['completion_controls']==['0','1'] and c['quadrature_cells_per_integral']==2048
    for key in ('independent_dimensionful_couplings_retained','coherent_bright_dark_projection_retained',
                'full_photon_profiles_and_old_band_comparison_retained','ordinary_weak_cutoff_limits_commute',
                'rescaled_weak_cutoff_limits_do_not_commute','all_exact_conversion_strengths_finite'):
        assert c[key] is True,key
    for key in ('unbounded_packet_in_Born_domain','uniform_Born_expansion_all_normalizable_packets',
                'source_envelope_selected','interaction_UV_form_factor_selected','on_shell_completion_is_local_UV_theory',
                'physical_rates_or_branching_derived','native_source_licensed','live_proposition_inventory_changed',
                'C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=shell.build();assert parent==json.loads(shell.RESULT.read_text(encoding='utf-8')),'stale on-shell control'
    mul=born.incoming.local.multiply_polynomials
    # Exact nonnegative-polynomial certificates used for the compact error estimates.
    D=mul([Q(1),Q(1,4)],[Q(1),Q(1,4)])
    assert born.add(born.scale(Q(1,2),D),[Q(-1,2),Q(-1,16)])==[Q(),Q(3,16),Q(1,32)]
    assert born.add(D,born.scale(-1,born.shift(born.derivative(D))))==[Q(1),Q(),Q(-1,16)]
    assert DELTA*(1+DELTA)**2<4
    assert 2+DELTA+(1+DELTA)**4/2<3
    # Bounds on the mass box are sufficient conditions, not assigned physical couplings.
    assert Q(1,256)**2*4**6==DELTA
    assert Q(1,32768)**2*4**10*18<DELTA
    for y in (Q(),Q(1,1024),Q(1,64),DELTA):
        f0=conversion(y,0);f1=conversion(y,1)
        assert 0<=y-f0<=y*y/2
        assert abs(f1-y)<=3*y*y
        assert 0<=f1-f0<=(2+DELTA)*y*y
        assert 0<=f0<=1 and 0<=f1<=1
    # Exact tail primitive: -d/dM tau(M)=rho(M), via r=1/(M-1).
    tau_poly=[Q(),Q(),Q(),Q(10),Q(-15),Q(6)]
    assert born.derivative(tau_poly)==[Q(),Q(),Q(30),Q(-60),Q(30)]
    assert tail_weight(Q(2))==1
    beta_int=lambda a,b:Q(factorial(a-1)*factorial(b-1),factorial(a+b-1))
    assert 30*beta_int(3,3)==1
    assert 30*(beta_int(4,2)+2*beta_int(3,3))==Q(7,2)
    assert 30*(beta_int(5,1)+4*beta_int(4,2)+4*beta_int(3,3))==16
    for L in (Q(3),Q(4),Q(8),Q(16)):
        assert 0<tail_weight(L)<1 and density(L)>0
        if L>=4:assert density(L)>=Q(15,2)/L**4
        assert density(L)<=Q(1920)/L**4
        B=2*(L+1)**2/(3*(L*L+2))
        assert Q(2,3)<=B<=1
    # Tail lower bounds imply divergent scalar M^2 and vector M^8 Born integrands.
    assert Q(15,2)*Q(1,2)==Q(15,4)
    assert Q(15,2)*Q(1,2)*Q(2,3)==Q(5,2)
    # eta=0 beta-integral constants: C_0,3=5*pi, C_0,6=5*pi/3.
    assert F(30)*2/6*Q(1,2)==F(5)
    assert F(20)*(2*phase.SQ2)/12*Q(1,4)/(phase.SQ2/2)==F(Q(5,3))
    bounds={}
    for p in (3,6):
        for eta in (0,1):
            lo,hi=asymptotic_constant_bounds(p,eta)
            assert 0<lo<hi
            bounds[f'p{p}_eta{eta}']={'lower':str(lo),'upper':str(hi)}
        # Completion freedom changes even the leading nonanalytic coefficient.
        assert Q(bounds[f'p{p}_eta1']['upper'])<Q(bounds[f'p{p}_eta0']['lower'])
    # Normalizing a finite cutoff does not create a new asymptotic strength.
    # P_infinity=(1-tau)*P_cutoff+tau*P_tail; both conditional strengths lie in [0,1].
    for L in (Q(3),Q(4),Q(8)):
        tau=tail_weight(L)
        for a,b in ((Q(),Q(1)),(Q(1),Q()),(Q(1,3),Q(2,5))):
            full=(1-tau)*a+tau*b
            assert abs(full-a)<=tau
    refused=[]
    for name in ('claim_unscaled_limits_noncommute','unbounded_packet_in_Born_domain',
                 'uniform_Born_expansion_all_normalizable_packets','source_envelope_selected',
                 'interaction_UV_form_factor_selected','on_shell_completion_is_local_UV_theory',
                 'physical_rates_or_branching_derived','reuse_compact_selected_fraction_on_entire_tail'):
        try:
            if name=='reuse_compact_selected_fraction_on_entire_tail':assert Q(1,4)==Q(1,64)
            else:
                bad=copy.deepcopy(c)
                if name=='claim_unscaled_limits_noncommute':bad['ordinary_weak_cutoff_limits_commute']=False
                else:bad[name]=True
                validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported packet-tail promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((shell.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_packet_weak_coupling_tail.py'))
    return {'schema':'marici.scattering.packet-weak-coupling-tail-receipt.v1','status':'pass',
        'scope_verdict':'conditional_packet_error_and_mass_tail_limits_for_postulated_on_shell_controls_not_physical_UV_selection',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'compact_error_certificate_constructed':True,'normalizable_unbounded_mass_counterexample_constructed':True,
        'compact_relative_Born_error_bounds':{'eta0':'delta/2','eta1':'3*delta','eta1_minus_eta0':'(2+delta)*delta'},
        'compact_delta':'1/16','tail_mass_norm':'1',
        'tail_first_mass_moment':'7/2','tail_second_mass_moment':'16',
        'normalized_cutoff_strength_error_bound':'tau(L)=10/(L-1)^3-15/(L-1)^4+6/(L-1)^5',
        'tail_weak_scaling':{'singlet_two_photon':'epsilon2^1','S_triplet_three_photon':'epsilon3^(1/2)'},
        'eta0_leading_constants':{'singlet_two_photon':'5*pi','S_triplet_three_photon':'5*pi/3'},
        'leading_constant_rational_enclosures':bounds,'exact_rational_quadrature_cells':8192,
        'compact_vs_tail_completion_order_reversed':True,
        'ordinary_iterated_limits':'0 in either order',
        'rescaled_iterated_limits':'0 with weak coupling first;positive C_eta,p with cutoff first',
        'strong_identity_limit':True,'operator_norm_identity_limit':False,
        'analytic_dominated_convergence_and_beta_integral_argument_machine_formalized':False,
        **{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale packet weak-coupling tail'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','compact_error_certificate_constructed',
        'tail_weak_scaling','ordinary_weak_cutoff_limits_commute','rescaled_weak_cutoff_limits_do_not_commute',
        'physical_rates_or_branching_derived','hostile_controls_refused')}))


if __name__=='__main__':main()
