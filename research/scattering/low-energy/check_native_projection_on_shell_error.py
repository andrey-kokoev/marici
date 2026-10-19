"""Exact algebra supporting a narrow on-shell/outgoing-packet comparison."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import check_native_projection_time_error as time_error

p=time_error.project;ROOT=p.ROOT;HOME=Path(__file__).resolve().parent
CONTRACT=HOME/'contracts/native-projection-on-shell-error.v1.json'
PROOF=HOME/'NATIVE-PROJECTION-ON-SHELL-ERROR.md'
RESULT=HOME/'results/native-projection-on-shell-error.v1.json'
F,mm,eye,scale,invert=p.F,p.mm,p.eye,p.scale,p.invert
transpose,decode,difference,zeros=p.transpose,p.decode,p.difference,p.zeros
quad=time_error.quadratic


def equal(A,B):assert A==B,'on-shell support identity failed'

def packet_error_squared_bound(epsilon,alpha_squared):
    assert 0<epsilon<=Q(1,64),'outside certified energy window'
    assert 0<=alpha_squared<=1,'normalized incoming weight required'
    return Q(4,9)*epsilon*alpha_squared

def effect_error_squared_bound(epsilon,alpha_squared):
    return 4*packet_error_squared_bound(epsilon,alpha_squared)

def validate_contract(c):
    assert c['schema']=='marici.scattering.native-projection-on-shell-error.v1'
    assert ROOT/c['projection_certificate']==p.RESULT
    assert ROOT/c['preceding_time_certificate']==time_error.RESULT
    assert Q(c['energy_window_upper'])==Q(1,64)
    assert Q(c['native_antisymmetric_gap_lower_bound'])==Q(1,8)
    assert Q(c['reduced_antisymmetric_gap_lower_bound'])==Q(1,4)
    assert Q(c['coefficient_upper_bound'])==Q(2,3)
    for key in ('full_band_small_error_claimed','live_proposition_inventory_changed','C12_protocol_renewed',
                'high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def sector(K,H,dimension,gap):
    n=len(K);seed=[[F(int(i==1)-int(i==2))] for i in range(n)]
    B=p.cyclic(K,[sum(seed,[])]);assert len(B[0])==dimension
    G=mm(mm(transpose(B),H),B);L=mm(mm(invert(G),transpose(B)),H)
    A=mm(mm(L,K),B);u=mm(L,seed);norm=quad(u,G)
    equal(mm(L,B),eye(dimension));equal(mm(B,u),seed);equal(mm(K,B),mm(B,A))
    equal(mm(G,A),transpose(mm(G,A)))
    assert p.inertia(G)==(dimension,0,0)
    assert p.inertia(mm(G,difference(A,scale(F(gap),eye(dimension)))))==(dimension,0,0)
    assert norm==F(40)
    P=[[F(int(i==j and i<3)) for j in range(n)] for i in range(n)]
    pa=scale(F(1)/norm,mm(mm(u,transpose(u)),G))
    equal(mm(P,B),mm(B,pa))
    visible=p.cyclic(K,[[F(int(i==j)) for i in range(n)] for j in range(3)])
    assert len(visible[0])==n
    m0=mm(mm(mm(transpose(u),G),invert(A)),u)[0][0]/norm;assert m0.positive()
    return {'B':B,'L':L,'G':G,'A':A,'u':u,'norm':norm,'m0':m0,'gap':gap}


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=time_error.build();assert parent==json.loads(time_error.RESULT.read_text(encoding='utf-8')),'stale time certificate'
    projection=json.loads(p.RESULT.read_text(encoding='utf-8'))
    src=json.loads(p.base.algebra.lower.SOURCE.read_text(encoding='utf-8'))
    K=decode(src['joint_generator']);h=[F(*v) for v in src['gram_diagonal']]
    H=[[h[i] if i==j else F() for j in range(11)] for i in range(11)]
    Kr=decode(projection['reduced_core']);Hr=decode(projection['full_metric']);E=decode(projection['embedding'])
    native=sector(K,H,6,Q(c['native_antisymmetric_gap_lower_bound']))
    reduced=sector(Kr,Hr,3,Q(c['reduced_antisymmetric_gap_lower_bound']))
    T=mm(mm(native['L'],E),reduced['B'])
    equal(mm(native['B'],T),mm(E,reduced['B']))
    equal(mm(mm(transpose(T),native['G']),T),reduced['G'])
    Tsharp=mm(mm(invert(reduced['G']),transpose(T)),native['G'])
    equal(mm(Tsharp,T),eye(3));equal(mm(mm(Tsharp,native['A']),T),reduced['A'])
    equal(native['u'],mm(T,reduced['u']))
    Qn=mm(native['B'],native['L']);Qr=mm(reduced['B'],reduced['L'])
    equal(Qr,difference(eye(8),decode(parent['symmetric_core_projector'])))
    equal(mm(Qn,E),mm(E,Qr))
    R=difference(mm(K,E),mm(E,Kr));equal(mm(R,difference(eye(8),Qr)),zeros(11,8))
    Qa=difference(eye(3),decode(parent['symmetric_port_projector']))
    HP=[row[:3] for row in H[:3]]
    equal(mm(Qa,Qa),Qa);equal(mm(HP,Qa),transpose(mm(HP,Qa)))
    # This commutation means the same Qa survives canonical flux whitening.
    equal(mm(HP,Qa),mm(Qa,HP));assert p.rank(Qa)==1
    mn,mr=native['m0'],reduced['m0'];delta0=mn-mr;assert delta0.positive()
    e=difference(mm(invert(native['A']),native['u']),mm(mm(T,invert(reduced['A'])),reduced['u']))
    assert quad(e,mm(native['G'],native['A']))/native['norm']==delta0
    factor=Q(1)/(1-Q(c['energy_window_upper'])/native['gap']);assert factor==Q(8,7)
    envelope=F(factor)*mn-mr
    assert envelope.positive() and (F(Q(c['coefficient_upper_bound'])/2)-envelope).positive()
    profiles={}
    for name,seed,expected in (('belt',[1,0,0],Q(0)),('carrier_sum',[0,1,1],Q(0)),
                              ('carrier_difference',[0,1,-1],Q(1)),('carrier_1',[0,1,0],Q(1,2)),
                              ('carrier_2',[0,0,1],Q(1,2))):
        v=[[F(x)] for x in seed];assert quad(mm(Qa,v),HP)/quad(v,HP)==F(expected)
        profiles[name]={'alpha_in_squared':str(expected)}
    controls=[]
    for name in ('erase-leading-error','alter-computed-envelope','enlarge-certified-window','promote-to-full-band','admit-physical-outcomes'):
        try:
            if name=='erase-leading-error':assert delta0==F()
            elif name=='alter-computed-envelope':assert envelope==F(Q(1,4))
            elif name=='enlarge-certified-window':packet_error_squared_bound(Q(1,32),Q(1))
            else:
                bad=copy.deepcopy(c)
                bad['full_band_small_error_claimed' if name=='promote-to-full-band' else 'physical_outcomes_admitted']=True
                validate_contract(bad)
        except AssertionError:controls.append(name)
        else:raise AssertionError('hostile on-shell control accepted: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((time_error.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_native_projection_on_shell_error.py'))
    def payload(s):
        return {'dimension':len(s['A']),'gap_lower_bound':str(s['gap']),
            'operator':p.base.encoded(s['A']),'metric':p.base.encoded(s['G']),
            'port_vector':p.base.encoded(s['u']),'port_norm_squared':s['norm'].encoded(),
            'zero_energy_compliance':s['m0'].encoded()}
    return {'schema':'marici.scattering.native-projection-on-shell-error-receipt.v1','status':'pass',
        'scope_verdict':'conditional_low_window_on_shell_and_outgoing_packet_error',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'native_antisymmetric':payload(native),'reduced_antisymmetric':payload(reduced),
        'antisymmetric_compression_embedding':p.base.encoded(T),'antisymmetric_port_projector':p.base.encoded(Qa),
        'full_visible_cyclic_dimensions':[11,8],'symmetric_scattering_exact_on_open_band':True,
        'zero_energy_compliance_gap':delta0.encoded(),'compliance_error_envelope':envelope.encoded(),
        'leading_error_coefficient_over_i':(2*delta0).encoded(),
        'pointwise_sqrt_energy_order_sharp_in_antisymmetric_channel':True,
        'energy_window_upper':c['energy_window_upper'],'on_shell_norm_error_bound':c['on_shell_norm_error_bound'],
        'outgoing_packet_norm_error_bound':c['outgoing_packet_norm_error_bound'],
        'outgoing_effect_probability_error_bound':c['outgoing_effect_probability_error_bound'],
        'normalized_incoming_preparations':profiles,
        'window_endpoint_packet_norm_error_per_alpha_in':'1/12',
        'window_endpoint_effect_probability_error_per_alpha_in':'1/6',
        'full_band_small_error_claimed':False,'all_energy_identity_claimed':False,
        'analytic_argument_machine_formalized':False,'physical_energy_or_detector_binding_claimed':False,
        'native_owner_solver_replayed':False,'historical_ancestor_freshness_claimed':False,
        'new_live_proposition_admitted':False,'C12_protocol_renewed':False,
        'high_energy_protocol_executed':False,'physical_outcomes_admitted':False,
        'hostile_controls_refused':controls}


def main():
    a=argparse.ArgumentParser(description=__doc__);a.add_argument('--check',action='store_true');args=a.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale native projection on-shell certificate'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    keys=('status','energy_window_upper','on_shell_norm_error_bound','outgoing_packet_norm_error_bound',
          'pointwise_sqrt_energy_order_sharp_in_antisymmetric_channel','full_band_small_error_claimed','hostile_controls_refused')
    print(json.dumps({k:r[k] for k in keys}))


if __name__=='__main__':main()
