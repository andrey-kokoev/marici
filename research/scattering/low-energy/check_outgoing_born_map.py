"""Full photon Born maps, exact compact-packet transition norms and unitarity deficit."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import check_incoming_dirac_packet as incoming

projection=incoming.projection;phase=incoming.phase;F=incoming.F;x=incoming.x
ROOT=incoming.ROOT;HOME=incoming.HOME
CONTRACT=HOME/'contracts/outgoing-born-map.v1.json';PROOF=HOME/'OUTGOING-BORN-MAP.md'
RESULT=HOME/'results/outgoing-born-map.v1.json'


def clean(p):
    p=list(map(Q,p))
    while p and not p[-1]:p.pop()
    return p


def add(*ps):
    out=[Q()] * max((len(p) for p in ps),default=0)
    for p in ps:
        for i,a in enumerate(p):out[i]+=a
    return clean(out)


def scale(a,p):return clean([a*v for v in p])
def shift(p,n=1):return [Q()]*n+list(p) if p else []
def derivative(p):return clean([i*a for i,a in enumerate(p)][1:])
def evaluate(p,t):return sum((v*t**i for i,v in enumerate(p)),Q())


def primitive(n):
    """Integral M^n sqrt(M^2-4) dM = sqrt(M^2-4)*p(M)+l*log(M+sqrt(M^2-4))."""
    assert isinstance(n,int) and n>=0
    if n==0:return [Q(),Q(1,2)],Q(-2)
    if n==1:return [Q(-4,3),Q(),Q(1,3)],Q()
    p,l=primitive(n-2)
    return scale(Q(1,n+2),add(shift([Q(-4),Q(),Q(1)],n-1),scale(4*(n-1),p))),Q(4*(n-1),n+2)*l


def integral(n):
    p,l=primitive(n)
    algebraic=2*phase.SQ3*F(evaluate(p,Q(4)))-phase.root(4)*F(evaluate(p,Q(3)))
    return algebraic,l


def encoded_integral(value):
    a,l=value
    assert all(v==0 for i,v in enumerate(a.v) if i not in (2,4))
    return {'sqrt3':str(a.v[2]),'sqrt5':str(a.v[4]),'log_ratio':str(l)}


def plain_integral(n):return Q(4**(n+1)-3**(n+1),n+1)


def norm_constants():
    # Phi_in=beta/(8*pi), Phi2=1/(8*pi), Phi3=M^2/(256*pi^3).
    c2=Q(1,8)*Q(1,8)*Q(1,2)*Q(1,2)*2
    c3=Q(1,8)*Q(1,256)*Q(1,6)*Q(2,45)
    c3s=c3*Q(8,9)
    return c2,c3,c3s


def relative_coefficient_map(M,alpha,cS,cD,g2,g3):
    """Return f2,f3 divided by a*b*sqrt(Phi_in*Phi_n/n!), with m=1."""
    M=F(M);assert x.positive(M-2) and len(cS)==len(cD)==3
    jS=2*phase.SQ2*(M+1)/3;jD=-2*(M-2)/3
    M2=M*M;M3=M2*M;M4=M2*M2
    return (g2*M3*alpha,
            [-phase.IM*g3*M4*phase.root(5)/15*(jS*s+jD*d) for s,d in zip(cS,cD)])


def validate_contract(c):
    assert c['schema']=='marici.scattering.outgoing-born-map.v1'
    assert c['amplitude_convention']=='Psi2=i*g2*Ptilde*A2out;Psi3=i*g3*Jtilde_mu*A3out^mu'
    assert c['coupling_mass_dimensions']=={'g2':-3,'g3':-6}
    assert c['declared_mass_box']==['3','4'] and c['declared_fermion_mass']=='1'
    assert c['Fock_factorials']=={'two':2,'three':6}
    for key in ('full_helicity_profiles_retained','old_band_restriction_retained','incoming_threshold_and_coarea_retained',
                'coherent_S_D_interference_retained','adjoint_and_elastic_channels_required'):
        assert c[key] is True,key
    for key in ('Born_norm_is_exact_probability','unitary_scattering_operator_constructed','second_order_forward_amplitude_constructed',
                'finite_packet_is_UV_completion','independent_dimensionful_couplings_equated','physical_preparation_selected',
                'native_Dirac_source_licensed','physical_annihilation_rate_derived','source_selected_branching_ratio_derived',
                'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=incoming.build();assert parent==json.loads(incoming.RESULT.read_text(encoding='utf-8')),'stale incoming packet'
    c2,c3,c3s=norm_constants()
    assert (c2,c3,c3s)==(Q(1,128),Q(1,276480),Q(1,311040))
    assert c3s/c2==Q(1,2430)
    # Antiderivatives checked by exact polynomial differentiation after multiplying by sqrt(M^2-4).
    R=[Q(-4),Q(),Q(1)]
    for n in range(12):
        p,l=primitive(n)
        dp=derivative(p)
        lhs=add(shift(p),shift(dp,2),scale(-4,dp),[l])
        assert lhs==clean(shift(R,n))
    I6=integral(5)
    # Independent t=M^2-4 substitution for the pseudoscalar mass integral.
    def alternate(t,root_t):return root_t*(F(t**3)/7+F(Q(8,5)*t*t)+F(Q(16,3)*t))
    assert I6==(alternate(Q(12),2*phase.SQ3)-alternate(Q(5),phase.root(4)),Q())
    odd11,log11=integral(11);even10,log10=integral(10);odd9,log9=integral(9)
    I3=(odd11+2*even10+odd9,log11+2*log10+log9)
    assert log11==log9==0 and I3[1]<0
    U6=plain_integral(6);U3=plain_integral(12)+2*plain_integral(11)+plain_integral(10)
    L6=Q(2,3)*U6;L3=Q(2,3)*U3
    assert Q(5,9)>Q(4,9) and Q(3,4)<1  # 2/3 < beta(M) < 1 over the box.
    assert 0<L6<U6 and 0<L3<U3
    # pi < 22/7 implies pi^2 < 10; at g2*m^3=1 a pure-singlet norm already exceeds one.
    assert Q(22,7)**2<10 and c2*L6/10>1
    # Norm cancellation in d^4P and the Fock lift. pi factors cancel in the coarea; do not drop n!.
    for M in (Q(3),Q(10,3),Q(4)):
        for phi_out,nfact in ((Q(1,8),2),(M*M/Q(256),6)):
            beta2=incoming.threshold_beta_squared(M);assert beta2>0
            phi_in=Q(1,8)  # beta and pi tracked separately.
            K2=phi_in/M**3
            assert M**3*K2*phi_out/nfact==phi_in*phi_out/nfact
            A2=M**4/2;Ps2=2*M*M;A3=Q(2,45)*M**8
            assert phi_in*Q(1,8)*Ps2*A2/2==c2*M**6
            assert phi_in*(M*M/256)*A3/6==c3*M**10
        a=2*(M+1)/3;b=M-2;jS=phase.SQ2*F(a);jD=F(-2*b/3)
        assert jS*(-jD)+jD*jS==F()
        assert x.positive(jS*jS*jD*jD)  # An incoherent mixture loses that exact cancellation.
        g2=F(1);g3=F(2)  # Independent reference values in their respective declared mass units.
        f2,f3=relative_coefficient_map(M,F(1),[F()]*3,[F()]*3,g2,g3)
        assert f2.conjugate()*f2==g2*g2*M**6 and f3==[F()]*3
        f2,f3=relative_coefficient_map(M,F(),[F(1),F(),F()],[F()]*3,g2,g3)
        assert f2==F() and f3[0].conjugate()*f3[0]==g3*g3*Q(2,45)*M**8*jS*jS
        f2,f3=relative_coefficient_map(M,F(),[-jD,F(),F()],[jS,F(),F()],g2,g3)
        assert f2==F() and f3==[F()]*3
    # Output relative directions and phases are not replaced by selected-mode norms.
    coefficients=[-phase.IM*phase.root(6)/8,phase.IM/8,phase.SQ3/2]
    assert sum((v.conjugate()*v for v in coefficients),F())==F(1)
    assert sum((v.conjugate()*v for v in coefficients[:2]),F())==F(Q(1,4))
    assert phase.IM*(-phase.IM)==F(1) and phase.IM*F(-1)==-phase.IM
    # A two-channel first-order block is not unitary; its second-order deficit is retained.
    K=[[F(),F(Q(1,3))],[F(Q(1,3)),F()]]
    S1=phase.add(phase.eye(2),phase.scale(phase.IM,K))
    assert phase.mm(phase.adj(S1),S1)==phase.add(phase.eye(2),phase.mm(K,K))
    assert phase.mm(phase.adj(S1),S1)!=phase.eye(2)
    refused=[]
    for name in ('drop_three_photon_factorial','erase_mass_growth','erase_orthogonal_photon_output',
                 'Born_norm_is_exact_probability','finite_packet_is_UV_completion',
                 'independent_dimensionful_couplings_equated','physical_preparation_selected','unitary_scattering_operator_constructed'):
        try:
            if name=='drop_three_photon_factorial':assert 6*c3s==c3s
            elif name=='erase_mass_growth':assert Q(3)**6==1
            elif name=='erase_orthogonal_photon_output':assert Q(1,4)==1
            else:
                bad=copy.deepcopy(c);bad[name]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported Born promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((incoming.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_outgoing_born_map.py'))
    return {'schema':'marici.scattering.outgoing-born-map-receipt.v1','status':'pass',
        'scope_verdict':'full_first_order_photon_output_for_declared_imported_packet_not_unitary_scattering_or_physical_rates',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'full_outgoing_Born_maps_constructed':True,'finite_compact_packet_transition_norms_constructed':True,
        'S_wave_norms':{'two':'|g2|^2*|alpha|^2*I6/(128*pi^2)',
                        'three':'|g3|^2*||c||^2*I3/(311040*pi^4)'},
        'general_S_D_three_norm_integrand':'|g3|^2*|a(M)|^2*beta*M^10*||jS*cS+jD*cD||^2/(276480*pi^4)',
        'mass_integrals':{'I6':encoded_integral(I6),'I3':encoded_integral(I3),
                          'log_argument':'(4+2*sqrt(3))/(3+sqrt(5))'},
        'mass_integral_strict_rational_bounds':{'I6':[str(L6),str(U6)],'I3':[str(L3),str(U3)]},
        'exact_antiderivative_checks':12,
        'pure_singlet_unit_reference_coupling_Born_norm_exceeds_one':True,
        'Born_unitarity_deficit_retained':True,'coherent_current_null_alternative_has_zero_Born_output':True,
        'three_photon_retained_selected_and_remainder':['1/4','3/4'],
        'source_selected_absolute_strength_or_ratio':False,'analytic_scattering_argument_machine_formalized':False,
        **{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale outgoing Born map'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','full_outgoing_Born_maps_constructed','exact_antiderivative_checks',
        'Born_unitarity_deficit_retained','source_selected_branching_ratio_derived','hostile_controls_refused')}))


if __name__=='__main__':main()
