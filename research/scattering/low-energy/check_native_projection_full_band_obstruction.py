"""Exact pole-free phase crossing: fixed projection has full-band error 2."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import check_native_projection_on_shell_error as preceding

p=preceding.p;ROOT=p.ROOT;HOME=Path(__file__).resolve().parent
CONTRACT=HOME/'contracts/native-projection-full-band-obstruction.v1.json'
PROOF=HOME/'NATIVE-PROJECTION-FULL-BAND-OBSTRUCTION.md'
RESULT=HOME/'results/native-projection-full-band-obstruction.v1.json'
F,mm,eye,scale,invert=p.F,p.mm,p.eye,p.scale,p.invert
transpose,decode,difference=p.transpose,p.decode,p.difference


def padd(*polys):
    result={}
    for poly in polys:
        for k,v in poly.items():result[k]=result.get(k,Q(0))+v
    return {k:v for k,v in result.items() if v}
def pscale(c,poly):return {k:c*v for k,v in poly.items() if c*v}
def pmul(a,b):
    result={}
    for i,x in a.items():
        for j,y in b.items():
            k=tuple(u+v for u,v in zip(i,j));result[k]=result.get(k,Q(0))+x*y
    return {k:v for k,v in result.items() if v}

def prove_phase_identity(drop_cross_term=False):
    one={(0,0,0):Q(1)};e={(1,0,0):Q(1)};x={(0,1,0):Q(1)};y={(0,0,1):Q(1)}
    dn=padd(one,pmul(e,x),pmul(e,pmul(x,x)))
    dr=padd(one,pmul(e,y),pmul(e,pmul(y,y)))
    w=padd(one,pmul(e,pmul(x,y)))
    if not drop_cross_term:w=padd(w,pscale(Q(1,2),pmul(e,padd(x,y))))
    gamma2=pmul(e,padd(pscale(Q(4),one),pscale(Q(-1),e)))
    delta=padd(x,pscale(Q(-1),y))
    residual=padd(pmul(dn,dr),pscale(Q(-1),pmul(w,w)),
                  pscale(Q(-1,4),pmul(gamma2,pmul(delta,delta))))
    assert residual=={},'phase identity is not a polynomial identity'
    return True

def model(payload):
    return {'A':decode(payload['operator']),'G':decode(payload['metric']),
            'u':decode(payload['port_vector']),'norm':F(*payload['port_norm_squared'])}
def shifted(m,E):return difference(m['A'],scale(F(E),eye(len(m['A']))))
def certify_no_poles(m,a,b):
    assert 0<a<b<4,'invalid open-band bracket'
    left=p.inertia(mm(m['G'],shifted(m,a)));right=p.inertia(mm(m['G'],shifted(m,b)))
    assert left==right and left[2]==0,'closed-core pole in bracket or at endpoint'
    return list(left)
def compliance(m,E):
    return mm(mm(mm(transpose(m['u']),m['G']),invert(shifted(m,E))),m['u'])[0][0]/m['norm']
def certify_sign_change(left,right):
    assert left.positive() and (-right).positive(),'missing strict phase sign change'
def evaluate(native,reduced,E):
    mn,mr=compliance(native,E),compliance(reduced,E);e=F(E)
    dn=F(1)+e*mn+e*mn*mn;dr=F(1)+e*mr+e*mr*mr
    assert dn.positive() and dr.positive()
    w=F(1)+F(E/2)*(mn+mr)+e*mn*mr
    delta=mn-mr;d2=F(E*(4-E))*delta*delta/(dn*dr)
    assert F(4)-d2==F(4)*w*w/(dn*dr)
    return {'mn':mn,'mr':mr,'dn':dn,'dr':dr,'w':w,'d2':d2}
def exact_phase(m,E,gamma,D):
    a=F(1)+F(E/2)*m;b=F(gamma/2)*m
    real=(a*a-b*b)/D;imag=2*a*b/D
    assert real*real+imag*imag==F(1)
    return real,imag

def validate_contract(c):
    assert c['schema']=='marici.scattering.native-projection-full-band-obstruction.v1'
    assert ROOT/c['preceding_certificate']==preceding.RESULT
    assert [Q(v) for v in c['root_bracket']]==[Q(39,100),Q(2,5)]
    assert Q(c['rational_witness_energy'])==Q(2,5)
    assert Q(c['rational_witness_norm_error_strict_lower_bound'])==Q(199,100)
    for key in ('exact_perfect_normalizable_packet_discrimination_claimed','all_reductions_excluded',
                'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=preceding.build();assert parent==json.loads(preceding.RESULT.read_text(encoding='utf-8')),'stale on-shell parent'
    prove_phase_identity()
    native=model(parent['native_antisymmetric']);reduced=model(parent['reduced_antisymmetric'])
    a,b=[Q(v) for v in c['root_bracket']]
    inertias={'native':certify_no_poles(native,a,b),'reduced':certify_no_poles(reduced,a,b)}
    assert inertias=={'native':[5,1,0],'reduced':[2,1,0]}
    left,right=evaluate(native,reduced,a),evaluate(native,reduced,b)
    certify_sign_change(left['w'],right['w'])
    E=Q(c['rational_witness_energy']);gamma=Q(6,5);assert gamma*gamma==E*(4-E)
    witness=right;assert E==b
    sn=exact_phase(witness['mn'],E,gamma,witness['dn'])
    sr=exact_phase(witness['mr'],E,gamma,witness['dr'])
    real=sn[0]-sr[0];imag=sn[1]-sr[1]
    assert real*real+imag*imag==witness['d2']
    lower=Q(c['rational_witness_norm_error_strict_lower_bound'])
    assert (witness['d2']-F(lower*lower)).positive()
    overlap_real=(F(1)+sn[0]*sr[0]+sn[1]*sr[1])/2
    overlap_imag=(sn[0]*sr[1]-sn[1]*sr[0])/2
    overlap_squared=overlap_real*overlap_real+overlap_imag*overlap_imag
    probability_gap=F(1)-overlap_squared
    assert probability_gap==witness['d2']/4
    assert (probability_gap-F(Q(39601,40000))).positive()
    controls=[]
    for name in ('drop-contact-cross-term','cross-a-pole','erase-sign-change','exclude-all-reductions','admit-physical-outcomes'):
        try:
            if name=='drop-contact-cross-term':prove_phase_identity(drop_cross_term=True)
            elif name=='cross-a-pole':certify_no_poles(native,Q(1,64),b)
            elif name=='erase-sign-change':certify_sign_change(left['w'],left['w'])
            else:
                bad=copy.deepcopy(c)
                bad['all_reductions_excluded' if name=='exclude-all-reductions' else 'physical_outcomes_admitted']=True
                validate_contract(bad)
        except AssertionError:controls.append(name)
        else:raise AssertionError('hostile full-band control accepted: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((preceding.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_native_projection_full_band_obstruction.py'))
    endpoints=[]
    for energy,data,sign in ((a,left,1),(b,right,-1)):
        endpoints.append({'energy':str(energy),'native_compliance':data['mn'].encoded(),
            'reduced_compliance':data['mr'].encoded(),'phase_sum_numerator_W':data['w'].encoded(),
            'W_sign':sign,'scattering_norm_error_squared':data['d2'].encoded()})
    return {'schema':'marici.scattering.native-projection-full-band-obstruction-receipt.v1','status':'pass',
        'scope_verdict':'maximal_full_band_discrepancy_for_fixed_native_projection',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'root_bracket':c['root_bracket'],'root_existence_not_uniqueness':True,
        'pole_free_weighted_inertias_at_both_endpoints':inertias,'endpoints':endpoints,
        'universal_phase_polynomial_identity_verified':True,
        'rational_witness':{'energy':str(E),'Gamma':str(gamma),
            'native_phase':{'real':sn[0].encoded(),'imag':sn[1].encoded()},
            'reduced_phase':{'real':sr[0].encoded(),'imag':sr[1].encoded()},
            'scattering_norm_error_squared':witness['d2'].encoded(),'norm_error_strict_lower_bound':str(lower),
            'mixed_input_common_effect_probability_gap':probability_gap.encoded(),
            'probability_gap_strict_lower_bound':'39601/40000'},
        'maximal_common_frame_full_band_scattering_norm_error':2,
        'common_free_packet_scattering_operator_norm_error':2,
        'symmetric_sector_still_exact':True,'preceding_low_window_bound_still_valid':True,
        'arbitrarily_accurate_normalized_packet_discrimination_exists':True,
        'exact_perfect_normalizable_packet_discrimination_claimed':False,
        'numerical_search_used_as_proof':False,'analytic_argument_machine_formalized':False,
        'all_reductions_excluded':False,'physical_preparation_or_detector_binding_claimed':False,
        'native_owner_solver_replayed':False,'historical_ancestor_freshness_claimed':False,
        'new_live_proposition_admitted':False,'C12_protocol_renewed':False,
        'high_energy_protocol_executed':False,'physical_outcomes_admitted':False,
        'hostile_controls_refused':controls}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale native projection full-band obstruction'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    keys=('status','root_bracket','maximal_common_frame_full_band_scattering_norm_error',
          'symmetric_sector_still_exact','preceding_low_window_bound_still_valid','hostile_controls_refused')
    print(json.dumps({k:r[k] for k in keys}))


if __name__=='__main__':main()
