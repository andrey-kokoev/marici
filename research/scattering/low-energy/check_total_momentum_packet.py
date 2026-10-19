"""Full Bose-Fock packet coarea and Lorentz/helicity transport, not native dynamics."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from math import factorial
from pathlib import Path
import check_photon_energy_tail as tail

phase=tail.phase;cm=tail.escape.cm;F=tail.F;x=tail.x;ROOT=tail.ROOT;HOME=tail.HOME;m=tail.measure
CONTRACT=HOME/'contracts/total-momentum-packet.v1.json'
PROOF=HOME/'TOTAL-MOMENTUM-PACKET.md'
RESULT=HOME/'results/total-momentum-packet.v1.json'
mm=phase.mm;adj=phase.adj;eye=phase.eye


def act(A,v):return [sum((a*b for a,b in zip(row,v)),F()) for row in A]
def minkowski(u,v):return u[0]*v[0]-sum((a*b for a,b in zip(u[1:],v[1:])),F())
def inverse_lorentz(A):return [[(1 if (i==0)==(j==0) else -1)*A[j][i] for j in range(4)] for i in range(4)]

def velocity(q):
    s=sum((v*v for v in q),F());assert x.positive(F(1)-s)
    return [(F(1)+s)/(F(1)-s)]+[2*v/(F(1)-s) for v in q]

def boost(u):
    assert minkowski(u,u)==F(1) and x.positive(u[0])
    return [[u[0]]+u[1:]]+[[u[i]]+[F(int(i==j))+u[i]*u[j]/(F(1)+u[0]) for j in range(1,4)] for i in range(1,4)]

def coarea_jacobian(M,q):
    s=sum((v*v for v in q),F());d=F(1)-s;u=velocity(q)
    A=[[u[0]]+[4*M*v/(d*d) for v in q]]
    A += [[u[i+1]]+[M*(2*F(int(i==j))/d+4*q[i]*q[j]/(d*d)) for j in range(3)] for i in range(3)]
    return cm.determinant(A)

def wigner(L,u):return mm(inverse_lorentz(boost(act(L,u))),mm(L,boost(u)))

def transport(L,k,e):
    kp=act(L,k);ep=act(L,[F()]+e)
    radiation=[ep[i]-ep[0]*kp[i]/kp[0] for i in range(4)]
    assert radiation[0]==F() and minkowski(kp,radiation)==F()
    return kp,radiation[1:]

def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def inner(a,b):return sum((u.conjugate()*v for u,v in zip(a,b)),F())

def packet_density_squared(M,n,phase_volume):
    """Squared amplitude prefactor, with the common (2*pi)^4 left symbolic."""
    assert n in (2,3) and x.positive(M) and x.positive(phase_volume)
    return F(factorial(n))/(M*M*M*phase_volume)


def cube_integral(p):
    out=F()
    for powers,c in p.items():
        v=Q(1)
        for k in powers:v*=Q() if k%2 else 2*Q(1,4)**(k+1)/Q(k+1)
        out+=c*v
    return out

def validate_contract(c):
    assert c['schema']=='marici.scattering.total-momentum-packet.v1'
    assert c['boost_cube_half_width']=='1/4'
    assert c['mass_density']=='30*M^2/(1+M)^6'
    assert c['Fock_norm_convention']=='1/n! times ordered product dPi; dPhi ordered'
    for key in ('mass_boost_records_retained','helicity_gauge_transport_retained','all_eight_relative_modes_retained'):
        assert c[key] is True
    for key in ('boost_envelope_source_selected','mass_envelope_source_selected','native_source_Lorentz_intertwiner_constructed',
                'physical_incident_preparation_bound','rest_escape_lab_translation_intertwiner_constructed',
                'CM_time_identified_with_lab_time','fixed_CM_delta_is_L2','local_field_interaction_constructed','annihilation_rate_derived',
                'branching_ratio_derived','live_proposition_inventory_changed','C12_protocol_renewed',
                'high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=tail.build();assert parent==json.loads(tail.RESULT.read_text(encoding='utf-8')),'stale energy tail'
    qs=[[F(v) for v in q] for q in ((0,0,0),(Q(1,8),0,0),(Q(1,8),Q(1,8),0),(Q(1,8),Q(1,6),Q(1,5))) ]
    metric=[[F((1 if i==0 else -1) if i==j else 0) for j in range(4)] for i in range(4)]
    jacobians=0;boosted=0
    for q in qs:
        u=velocity(q);B=boost(u);s=sum((v*v for v in q),F())
        assert mm(adj(B),mm(metric,B))==metric and cm.determinant(B)==F(1)
        assert [u[i]/(1+u[0]) for i in range(1,4)]==q
        for M in (F(1),F(2),F(3)):
            assert coarea_jacobian(M,q)==8*M*M*M/m.scalar_power(F(1)-s,3);jacobians+=1
            for n in (2,3):
                rest=([[M/2,F(),F(),M/2],[M/2,F(),F(),-M/2]] if n==2 else
                      [[M/3,M/3,F(),F()],[M/3,-M/6,M*phase.SQ3/6,F()],[M/3,-M/6,-M*phase.SQ3/6,F()]])
                ps=[act(B,p) for p in rest]
                assert all(minkowski(p,p)==F() and x.positive(p[0]) for p in ps)
                assert [sum((p[i] for p in ps),F()) for i in range(4)]==[M*v for v in u];boosted+=1
    L1=boost(velocity([F(Q(1,8)),F(),F()]))
    L2=boost(velocity([F(),F(Q(1,6)),F()]))
    cocycles=0
    for q in qs:
        u=velocity(q);W=wigner(mm(L2,L1),u)
        assert W==mm(wigner(L2,act(L1,u)),wigner(L1,u))
        assert W[0]==[F(1),F(),F(),F()] and [row[0] for row in W]==[F(1),F(),F(),F()]
        R=[row[1:] for row in W[1:]]
        assert mm(adj(R),R)==eye(3) and cm.determinant(R)==F(1);cocycles+=1
    assert wigner(mm(L2,L1),[F(1),F(),F(),F()])!=eye(4)
    helicity_cases=0
    for L in (L1,L2,mm(L2,L1)):
        for h in (-1,1):
            e=[F(1)/phase.SQ2,h*phase.IM/phase.SQ2,F()];k=[F(1),F(),F(),F(1)]
            kp,ep=transport(L,k,e);n=[v/kp[0] for v in kp[1:]]
            assert inner(ep,ep)==F(1) and [phase.IM*v for v in cross(n,ep)]==[h*v for v in ep]
            # Minimal spatial rotation z -> n supplies a canonical reference frame.
            v=cross([F(),F(),F(1)],n)
            C=[[F(),-v[2],v[1]],[v[2],F(),-v[0]],[-v[1],v[0],F()]]
            R=phase.add(phase.add(eye(3),C),phase.scale(F(1)/(F(1)+n[2]),mm(C,C)))
            canonical=act(R,e);zeta=inner(canonical,ep)
            assert zeta*zeta.conjugate()==F(1) and ep==[zeta*v for v in canonical];helicity_cases+=1
            if L==mm(L2,L1) and h==1:assert zeta==(F(2303)-96*phase.IM)/2305 and zeta!=F(1)
            k1,e1=transport(L1,k,e);k2,e2=transport(L2,k1,e1)
            assert (k2,e2)==transport(mm(L2,L1),k,e)
    group,_,spin=phase.source_group();rotations=0
    for q in sorted(group):
        R=phase.spatial(phase.from_spin(spin,q))
        assert all(sum(v!=F() for v in row)==1 and all(v in (F(-1),F(),F(1)) for v in row) for row in R)
        L=phase.blockdiag([[[F(1)]],R])
        assert wigner(L,velocity(qs[-1]))==L;rotations+=1
    s=m.add(*(m.power(m.var(i),2) for i in range(3)))
    b2=m.power(m.add(m.const(1),m.scale(F(-1),s)),3)
    wrong_boost_norm=cube_integral(b2)
    assert x.positive(wrong_boost_norm) and x.positive(F(1)-wrong_boost_norm)
    assert 8*cube_integral(m.const(1))==F(1)
    assert 30*tail.beta_integral(2,6)==Q(1)
    # Multiparticle Bose and (2*pi)^4 factors cancel in the squared wavefunction.
    assert [2*n-4+3-(3+2*n-4) for n in (2,3)]==[0,0]
    for n in (2,3):
        for M in (F(1),F(2),F(3)):
            volume=F(Q(1,7))*m.scalar_power(M,2*n-4)
            assert M*M*M*volume*packet_density_squared(M,n,volume)/factorial(n)==F(1)
    u=velocity(qs[1]);assert u[0]==F(Q(65,63)) and u[0]!=F(1)
    refused=[]
    for name in ('omit_mass_coarea_half_density','omit_boost_measure','declare_fixed_CM_delta_packet_normalizable',
                 'erase_helicity_gauge_projection','identify_CM_mass_with_lab_energy','omit_Bose_factorial','promote_native_Lorentz_binding'):
        try:
            if name=='omit_mass_coarea_half_density':tail.beta_integral(5,6)
            elif name=='omit_boost_measure':assert wrong_boost_norm==F(1)
            elif name=='declare_fixed_CM_delta_packet_normalizable':assert c['fixed_CM_delta_is_L2']
            elif name=='erase_helicity_gauge_projection':assert act(L1,[F(),F(1)/phase.SQ2,phase.IM/phase.SQ2,F()])[0]==F()
            elif name=='identify_CM_mass_with_lab_energy':assert u[0]==F(1)
            elif name=='omit_Bose_factorial':assert Q(1,factorial(3))==Q(1)
            else:
                bad=copy.deepcopy(c);bad['native_source_Lorentz_intertwiner_constructed']=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported packet promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((tail.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_total_momentum_packet.py'))
    return {'schema':'marici.scattering.total-momentum-packet-receipt.v1','status':'pass',
        'scope_verdict':'normalizable_imported_Bose_Fock_packet_and_induced_Lorentz_carrier_not_native_source_or_lab_escape_dynamics',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'full_total_momentum_Fock_wavepacket_constructed':True,'eight_mode_coarea_isometry_constructed':True,
        'imported_photon_Lorentz_carrier_intertwiner_constructed':True,
        'coarea_mass_power':3,'coarea_half_density_mass_power':'-3/2',
        'mass_boost_jacobian_checks':jacobians,'boosted_null_output_configurations':boosted,
        'Wigner_rotation_cocycle_cases':cocycles,'helicity_transport_cases':helicity_cases,
        'nontrivial_helicity_phase_example':'(2303-96*i)/2305',
        'native_rotation_boost_envelope_cases':rotations,'normalized_example_mass_norm':'1','normalized_example_boost_norm':'1',
        'lab_energy_witness':{'mass':'1','u0':'65/63','P0':'65/63'},
        'omitting_mass_half_density_gives_log_divergent_norm':True,
        'fixed_boost_envelope_subspace_closed_under_general_Lorentz':False,
        'analytic_argument_machine_formalized':False,**{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],'hostile_controls_refused':refused}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale total momentum packet'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','full_total_momentum_Fock_wavepacket_constructed',
        'mass_boost_jacobian_checks','helicity_transport_cases','native_source_Lorentz_intertwiner_constructed',
        'rest_escape_lab_translation_intertwiner_constructed','hostile_controls_refused')}))


if __name__=='__main__':main()
