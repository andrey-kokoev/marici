"""Cayley on-shell controls sharing the Born map, with elastic and dark channels retained."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import check_outgoing_born_map as born

incoming=born.incoming;phase=born.phase;F=born.F;x=born.x
ROOT=born.ROOT;HOME=born.HOME
CONTRACT=HOME/'contracts/on-shell-unitary-completion.v1.json'
PROOF=HOME/'ON-SHELL-UNITARY-COMPLETION.md'
RESULT=HOME/'results/on-shell-unitary-completion.v1.json'
mm=phase.mm;adj=phase.adj;eye=phase.eye;add=phase.add;scale=phase.scale


def inverse(A):
    n=len(A);assert all(len(row)==n for row in A)
    I=eye(n);rows=[list(row)+I[i] for i,row in enumerate(A)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if rows[i][j]!=F()),None)
        assert pivot is not None,'singular matrix'
        rows[j],rows[pivot]=rows[pivot],rows[j]
        d=rows[j][j];rows[j]=[v/d for v in rows[j]]
        for i in range(n):
            if i==j:continue
            d=rows[i][j]
            rows[i]=[a-d*b for a,b in zip(rows[i],rows[j])]
    out=[row[n:] for row in rows];assert mm(A,out)==I
    return out


def completion(K,eta=Q(),coupling=Q(1)):
    assert adj(K)==K and eta in (Q(),Q(1)) and isinstance(coupling,Q)
    K3=mm(K,mm(K,K))
    H=add(scale(F(coupling),K),scale(F(eta*coupling**3),K3))
    return cayley(H)


def cayley(H):
    assert adj(H)==H
    I=eye(len(H));return mm(add(I,scale(phase.IM/2,H)),inverse(add(I,scale(-phase.IM/2,H))))


def scalar_kernel(a):return [[F(),phase.IM*a],[-phase.IM*a,F()]]


def vector_kernel(M,a):
    jS=2*phase.SQ2*F(M+1)/3;jD=F(-2*(M-2)/3)
    K=[[F(),F(),-a*jS],[F(),F(),-a*jD],[-a*jS,-a*jD,F()]]
    return K,jS,jD


def rank_one_kernel(v):
    n=len(v);K=[[F() for _ in range(n+1)] for _ in range(n+1)]
    for i,a in enumerate(v):K[i+1][0]=a;K[0][i+1]=a.conjugate()
    return K


def validate_contract(c):
    assert c['schema']=='marici.scattering.on-shell-unitary-completion.v1'
    assert c['completion_family']=='Cayley(lambda*K+eta*lambda^3*K^3)'
    assert c['eta_controls']==['0','1']
    assert c['active_fiber_dimension']==11 and c['source_spin_orbital_dimension']==7
    for key in ('same_Born_and_second_order_terms','incoming_survival_and_adjoint_retained',
                'coherent_S_D_dark_states_retained','full_photon_profiles_and_complements_retained',
                'old_band_comparison_restriction_retained','full_mass_velocity_carrier_retained'):
        assert c[key] is True,key
    for key in ('completion_parameter_source_selected','all_unitary_completions_preserve_dark_states',
                'second_order_phase_fixed_by_Born','Born_expansion_uniform_all_masses','QFT_loop_forward_amplitude_derived',
                'local_cluster_dynamics_proved','spacetime_scattering_Hamiltonian_constructed',
                'UV_local_completion_constructed','native_source_licensed','physical_rate_or_branching_derived',
                'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=born.build();assert parent==json.loads(born.RESULT.read_text(encoding='utf-8')),'stale Born map'
    unitary=0;optical=0;dark_cases=0;forward=0
    for M in (Q(3),Q(10,3),Q(4)):
        for a2,a3 in ((Q(),Q()),(Q(1,3),Q(1,7)),(Q(-1),Q(1,3))):
            Ks=scalar_kernel(F(a2));Kt,jS,jD=vector_kernel(M,F(a3));N2=jS*jS+jD*jD
            assert N2==F(Q(4,3)*(M*M+2))
            dark=[[ -jD],[jS],[F()]]
            assert mm(Kt,dark)==[[F()] for _ in range(3)]
            for K in (Ks,Kt):
                I=eye(len(K));K2=mm(K,K);S1=scale(phase.IM,K);S2=scale(F(Q(-1,2)),K2)
                zero=[[F() for _ in row] for row in I]
                assert add(add(S2,adj(S2)),mm(adj(S1),S1))==zero
                # Denominator times the expansion equals the numerator through order two.
                assert add(S1,scale(-phase.IM/2,K))==scale(phase.IM/2,K)
                assert add(S2,mm(scale(-phase.IM/2,K),S1))==zero
                forward+=1
                for eta in (Q(),Q(1)):
                    for coupling in (Q(1,2),Q(1)):
                        S=completion(K,eta,coupling)
                        assert mm(adj(S),S)==I and mm(S,adj(S))==I;unitary+=1
                        T=scale(-phase.IM,add(S,scale(F(-1),I)))
                        assert add(T,scale(F(-1),adj(T)))==scale(phase.IM,mm(adj(T),T));optical+=1
                        if len(K)==3:
                            assert mm(S,dark)==dark;dark_cases+=1
            # Forward source block includes coherent S/D mixing, not two averaged probabilities.
            K2=mm(Kt,Kt)
            assert K2[0][1]==F(a3*a3)*jS*jD
            assert K2[0][0]==F(a3*a3)*jS*jS and K2[1][1]==F(a3*a3)*jD*jD
    # Same first and second order, different finite conversion at a fixed reduced coupling.
    K=scalar_kernel(F(1));S0=completion(K);S1=completion(K,Q(1))
    p0=S0[1][0].conjugate()*S0[1][0];p1=S1[1][0].conjugate()*S1[1][0]
    assert p0==F(Q(16,25)) and p1==F(1) and S0!=S1
    # Outside the polynomial-in-K family, an O(lambda^3) coupling can lift the old dark state.
    Kb=[[F(),F(),F(1)],[F(),F(),F()],[F(1),F(),F()]]
    L=[[F(),F(),F()],[F(),F(),F(1)],[F(),F(1),F()]]
    lifted=cayley(add(Kb,L))  # H(lambda)=lambda*Kb+lambda^3*L, here lambda=1.
    assert mm(adj(lifted),lifted)==eye(3)
    assert lifted[2][1].conjugate()*lifted[2][1]==F(Q(4,9))
    # The complete outgoing triplet profile is coherent across all three retained blocks.
    v=[-phase.IM*phase.root(6)/8,phase.IM/8,phase.SQ3/2]
    assert incoming.packet.inner(v,v)==F(1)
    Kfull=rank_one_kernel([-a for a in v])
    e=[F(1),F(),F()];dot=incoming.packet.inner(v,e)
    w=[[F()]]+[[a-b*dot] for a,b in zip(e,v)]
    assert mm(Kfull,w)==[[F()] for _ in range(4)]
    for eta in (Q(),Q(1)):
        S=completion(Kfull,eta);assert mm(adj(S),S)==eye(4) and mm(S,w)==w
        photon=[S[i][0] for i in range(1,4)]
        total=incoming.packet.inner(photon,photon)
        selected=sum((a.conjugate()*a for a in photon[:2]),F())
        assert selected==total/4 and total-selected==3*total/4
    # Dark source weight in a pure S-wave triplet is preparation-dependent and nonzero.
    def dark_weight(M):return (M-2)**2/(3*(M*M+2))
    assert dark_weight(Q(3))==Q(1,33) and dark_weight(Q(4))==Q(2,27)
    # d/dM dark_weight = 4*(M-2)*(M+1)/(3*(M^2+2)^2) > 0 for M>2.
    for M in (Q(3),Q(10,3),Q(4)):
        assert 4*(M-2)*(M+1)>0 and Q(1,33)<=dark_weight(M)<=Q(2,27)
    # All other angular/Fock channels are direct-summed with identity, not deleted.
    extended=phase.blockdiag([S0,eye(2)])
    assert mm(adj(extended),extended)==eye(4)
    refused=[]
    for name in ('delete_elastic_forward_term','replace_dark_by_complete_conversion','erase_photon_complement',
                 'completion_parameter_source_selected','all_unitary_completions_preserve_dark_states',
                 'QFT_loop_forward_amplitude_derived','local_cluster_dynamics_proved','physical_rate_or_branching_derived'):
        try:
            if name=='delete_elastic_forward_term':assert mm(adj(add(eye(2),scale(phase.IM,K))),add(eye(2),scale(phase.IM,K)))==eye(2)
            elif name=='replace_dark_by_complete_conversion':assert Q(1,33)==0
            elif name=='erase_photon_complement':assert incoming.packet.inner([z[0] for z in w],[z[0] for z in w])==F()
            else:
                bad=copy.deepcopy(c);bad[name]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported on-shell promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((born.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_on_shell_unitary_completion.py'))
    return {'schema':'marici.scattering.on-shell-unitary-completion-receipt.v1','status':'pass',
        'scope_verdict':'two_postulated_on_shell_unitary_controls_not_local_scattering_dynamics_or_selected_physics',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'on_shell_unitary_controls_constructed':True,'forward_elastic_unitarity_condition_constructed':True,
        'common_expansion':'I+i*lambda*K-lambda^2*K^2/2+O(lambda^3)',
        'general_second_order_freedom':'-K^2/2+i*B;B=B^dagger',
        'exact_unitarity_checks':unitary,'exact_optical_theorem_checks':optical,
        'second_order_forward_checks':forward,'dark_state_identity_checks':dark_cases,
        'fixed_reduced_coupling_conversion_witness':{'eta_0':'16/25','eta_1':'1'},
        'pure_S_triplet_dark_weight':'(M-2*m)^2/(3*(M^2+2*m^2))',
        'declared_compact_packet_dark_retention_lower_bound':'1/33',
        'higher_order_dark_lifting_conversion_witness':'4/9',
        'direct_integral_domain_and_Poincare_argument_machine_formalized':False,
        **{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale on-shell completion'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','on_shell_unitary_controls_constructed','exact_unitarity_checks',
        'fixed_reduced_coupling_conversion_witness','physical_rate_or_branching_derived','hostile_controls_refused')}))


if __name__=='__main__':main()
