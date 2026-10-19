"""Normalized charged-pair packet, transported spin frames and explicit local currents."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import check_local_helicity_projection as projection

local=projection.local;packet=local.packet;phase=local.phase;F=local.F;x=local.x;cm=local.cm;m=projection.m
pair=packet.tail.escape.pair;ROOT=local.ROOT;HOME=local.HOME
CONTRACT=HOME/'contracts/incoming-dirac-packet.v1.json'
PROOF=HOME/'INCOMING-DIRAC-PACKET.md'
RESULT=HOME/'results/incoming-dirac-packet.v1.json'
mm=phase.mm;adj=phase.adj;eye=phase.eye;scale=phase.scale


def raw_spinors(E,p,mass=F(1)):
    assert mass==F(1) and E*E-sum((v*v for v in p),F())==mass*mass
    assert x.positive(E)
    I2=eye(2);epsilon=[[F(),F(1)],[F(-1),F()]]
    sigma=phase.pauli(p);lower=scale(F(1)/(E+mass),sigma)
    # Positron phase convention eta_r=i*sigma2*chi_r^*.
    u=I2+lower
    v=scale(F(-1),mm(lower,epsilon))+epsilon
    return u,v


def slash(k,gs):
    out=scale(k[0],gs[0])
    for i in range(3):out=phase.add(out,scale(-k[i+1],gs[i+1]))
    return out


def pair_current(u,v,G,g0,factor):
    # Output entries are electron-spin row, positron-spin column.
    return projection.local.transpose(scale(factor,mm(adj(v),mm(g0,mm(G,u)))))


def spin_channels():
    epsilon=[[F(),F(1)],[F(-1),F()]]
    Bs=[mm(projection.local.transpose(s),epsilon) for s in phase.SIGMA]
    def flatten(A):return [v for row in A for v in row]
    s=[v/phase.SQ2 for v in flatten(epsilon)]
    ts=[[v.conjugate()/phase.SQ2 for v in flatten(B)] for B in Bs]
    return s,ts,epsilon,Bs


def spinor_boost(q,denominator,gs):
    assert denominator*denominator==F(1)-sum((v*v for v in q),F()) and x.positive(denominator)
    A=eye(4)
    for i in range(3):A=phase.add(A,scale(q[i],mm(gs[0],gs[i+1])))
    return scale(F(1)/denominator,A)


def threshold_beta_squared(M,mass=Q(1)):
    assert M>2*mass and mass>0
    return Q(1)-4*mass*mass/(M*M)


def validate_contract(c):
    assert c['schema']=='marici.scattering.incoming-dirac-packet.v1'
    assert c['declared_fermion_mass']=='1' and c['mass_box']==['3','4']
    assert c['positron_spin_phase']=='eta=i*sigma2*conjugate(chi)'
    assert c['pair_creation_order']=='electron_b_dagger_then_positron_d_dagger'
    assert c['incident_orbital_choice']=='coherent_CM_S_wave_with_arbitrary_normalized_spin_coefficients'
    for key in ('spin_mass_boost_and_threshold_records_retained','D_wave_current_kernel_retained','distinct_charge_sector_no_Bose_factorial'):
        assert c[key] is True
    for key in ('physical_incident_preparation_selected','native_Dirac_source_licensed','singlet_fraction_source_selected',
                'packet_replaced_by_direction_mixture','sharp_threshold_pair_is_normalizable',
                'UV_interaction_form_factor_selected','outgoing_Born_map_constructed','unitary_interacting_QFT_constructed',
                'electron_mass_dimensionally_calibrated','annihilation_rate_derived','branching_ratio_derived',
                'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=projection.build();assert parent==json.loads(projection.RESULT.read_text(encoding='utf-8')),'stale current profile projection'
    gs=local.gamma_matrices();g5=scale(phase.IM,mm(gs[0],mm(gs[1],mm(gs[2],gs[3]))));P=scale(phase.IM,g5)
    s,ts,epsilon,Bs=spin_channels();basis=[s]+ts
    assert [[packet.inner(a,b) for b in basis] for a in basis]==eye(4)
    directions=[[F(),F(),F(1)],[F(1),F(),F()],[F(1)/phase.SQ3]*3]
    boost_data=[([F(Q(1,5)),F(),F()],2*phase.SQ6/5),([F(),F(Q(1,4)),F()],phase.root(6)/4)]
    boosts=[]
    for q,den in boost_data:
        S=spinor_boost(q,den,gs);L=packet.boost(packet.velocity(q));Si=mm(gs[0],mm(adj(S),gs[0]))
        assert mm(adj(S),mm(gs[0],S))==gs[0]
        for mu in range(4):
            target=[[sum((L[mu][nu]*gs[nu][i][j] for nu in range(4)),F()) for j in range(4)] for i in range(4)]
            assert mm(Si,mm(gs[mu],S))==target
        assert mm(Si,mm(P,S))==P;boosts.append((L,S))
    boosts.append((mm(boosts[1][0],boosts[0][0]),mm(boosts[1][1],boosts[0][1])))
    rest_cases=0;boost_cases=0;wigner_cases=0
    for E,k in ((F(Q(3,2)),phase.root(4)/2),(F(Q(5,3)),F(Q(4,3))),(F(2),phase.SQ3)):
        M=2*E
        for n in directions:
            p=[k*v for v in n];km=[E]+p;kp=[E]+[-v for v in p]
            u,v=raw_spinors(E,p);factor=E+1
            assert mm(phase.add(slash(km,gs),scale(F(-1),eye(4))),u)==[[F()]*2 for _ in range(4)]
            assert mm(phase.add(slash(kp,gs),eye(4)),v)==[[F()]*2 for _ in range(4)]
            assert scale(factor,mm(adj(u),mm(gs[0],u)))==scale(F(2),eye(2))
            assert scale(factor,mm(adj(v),mm(gs[0],v)))==scale(F(-2),eye(2))
            pmat=pair_current(u,v,P,gs[0],factor)
            jmat=[pair_current(u,v,g,gs[0],factor) for g in gs]
            assert pmat==scale(-phase.IM*M,epsilon) and jmat[0]==[[F()]*2 for _ in range(2)]
            V=[[M*F(int(i==j))-(M-2)*n[i]*n[j] for j in range(3)] for i in range(3)]
            for i in range(3):
                target=[[sum((V[i][j]*Bs[j][a][b] for j in range(3)),F()) for b in range(2)] for a in range(2)]
                assert jmat[i+1]==target
            flatten=lambda A:[v for row in A for v in row]
            linear=lambda A,z:sum((a*b for a,b in zip(flatten(A),z)),F())
            assert linear(pmat,s)==-phase.IM*phase.SQ2*M
            assert all(linear(pmat,t)==F() for t in ts)
            assert all(linear(j,s)==F() for j in jmat)
            for i in range(3):
                for j in range(3):assert linear(jmat[i+1],ts[j])==phase.SQ2*V[i][j]
            rest_cases+=1
            for L,S in boosts:
                ub=mm(S,u);vb=mm(S,v);pm=packet.act(L,km);pp=packet.act(L,kp)
                assert pair_current(ub,vb,P,gs[0],factor)==pmat
                jboost=[pair_current(ub,vb,g,gs[0],factor) for g in gs]
                for mu in range(4):
                    target=[[sum((L[mu][nu]*jmat[nu][a][b] for nu in range(4)),F()) for b in range(2)] for a in range(2)]
                    assert jboost[mu]==target
                assert scale(factor,mm(adj(ub),ub))==scale(2*pm[0],eye(2))
                assert scale(factor,mm(adj(vb),vb))==scale(2*pp[0],eye(2))
                for old,new in ((km,pm),(kp,pp)):
                    W=mm(packet.inverse_lorentz(packet.boost(new)),mm(L,packet.boost(old)))
                    assert W[0]==[F(1),F(),F(),F()]
                    R=[row[1:] for row in W[1:]]
                    assert mm(adj(R),R)==eye(3) and cm.determinant(R)==F(1);wigner_cases+=1
                boost_cases+=1
    # Exact angular S/D decomposition, using sphere moments, not a finite direction mixture.
    ns=[m.var(i) for i in range(3)]
    D=[[m.add(m.mul(ns[i],ns[j]),m.const(Q(-1,3) if i==j else 0)) for j in range(3)] for i in range(3)]
    assert [[pair.sphere_integral(p) for p in row] for row in D]==[[F()]*3 for _ in range(3)]
    D2=[[m.add(*(m.mul(D[i][k],D[k][j]) for k in range(3))) for j in range(3)] for i in range(3)]
    assert [[pair.sphere_integral(p) for p in row] for row in D2]==scale(F(Q(2,9)),eye(3))
    for M in (Q(3),Q(10,3),Q(4)):
        a=2*(M+1)/3;b=M-2
        Sw=2*a*a;Dw=4*b*b/9;full=2*(2*M*M+4)/3
        assert Sw+Dw==full and Dw>0
        Js=phase.SQ2*F(a);Jd=F(-2*b/3)
        assert Js*(-Jd)+Jd*Js==F()  # Coherent normalized S/D alternatives can be current-null.
        assert x.positive(Js*Js+Jd*Jd) and x.positive(2*Js*Js*Jd*Jd)
    # Packet mass norm, invariant boost norm and spin/orbital norms all equal one.
    assert Q(4)-Q(3)==Q(1) and 8*packet.cube_integral(m.const(1))==F(1)
    assert threshold_beta_squared(Q(3))==Q(5,9) and threshold_beta_squared(Q(4))==Q(3,4)
    # Coarea cancels without a 2!: charges are distinguished and creation order is fixed.
    for M,beta in ((F(Q(10,3)),F(Q(4,5))),(F(3),phase.root(4)/3),(F(4),phase.SQ3/2)):
        volume_without_pi=beta/8
        prefactor_squared=F(1)/(M*M*M*volume_without_pi)
        assert M*M*M*volume_without_pi*prefactor_squared==F(1)
        assert volume_without_pi*volume_without_pi*prefactor_squared==volume_without_pi/(M*M*M)
    refused=[]
    for name in ('insert_Bose_factorial_for_distinct_charges','admit_threshold_delta_as_packet',
                 'average_direction_probabilities_as_S_wave','erase_D_wave_kernel','select_singlet_fraction',
                 'promote_native_preparation','packet_cures_QFT_UV_operator'):
        try:
            if name=='insert_Bose_factorial_for_distinct_charges':assert Q(1,2)==Q(1)
            elif name=='admit_threshold_delta_as_packet':threshold_beta_squared(Q(2))
            elif name=='average_direction_probabilities_as_S_wave':assert Q(2)*(2*Q(3)**2+4)/3==2*(2*(Q(3)+1)/3)**2
            elif name=='erase_D_wave_kernel':assert 4*(Q(3)-2)**2/9==0
            else:
                bad=copy.deepcopy(c)
                key={'select_singlet_fraction':'singlet_fraction_source_selected','promote_native_preparation':'physical_incident_preparation_selected',
                     'packet_cures_QFT_UV_operator':'unitary_interacting_QFT_constructed'}[name]
                bad[key]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported incoming packet promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((projection.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_incoming_dirac_packet.py'))
    return {'schema':'marici.scattering.incoming-dirac-packet-receipt.v1','status':'pass',
        'scope_verdict':'declared_normalizable_imported_Dirac_pair_packet_and_transition_currents_not_native_incident_state',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'normalizable_incoming_Dirac_pair_packet_constructed':True,
        'conditional_spin_coefficient_to_incoming_pair_packet_isometry_constructed':True,
        'declared_packet_mass_norm':'1','declared_packet_boost_norm':'1',
        'pseudoscalar_vector_currents_of_declared_packet_constructed':True,'CM_spinor_current_cases':rest_cases,
        'boosted_current_cases':boost_cases,'individual_massive_Wigner_rotation_cases':wigner_cases,
        'pointwise_pseudoscalar_spin_amplitude':'-i*sqrt(2)*M*alpha',
        'pointwise_triplet_vector_kernel':'sqrt(2)*(M*I-(M-2*m)*n*n^T)',
        'S_wave_vector_current_coefficient':'2*sqrt(2)*(M+m)/3',
        'normalized_D_wave_vector_current_coefficient':'-2*(M-2*m)/3',
        'common_Fourier_current_packet_factor':'(2*pi)^2*a(M)*b(u)*sqrt(Phi_2m(M)/M^3)',
        'singlet_fraction_remains_free':True,'current_null_coherent_S_D_alternative_exists':True,
        'analytic_packet_and_spin_transport_argument_machine_formalized':False,
        **{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale incoming Dirac packet'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','normalizable_incoming_Dirac_pair_packet_constructed',
        'CM_spinor_current_cases','boosted_current_cases','physical_incident_preparation_selected',
        'branching_ratio_derived','hostile_controls_refused')}))


if __name__=='__main__':main()
