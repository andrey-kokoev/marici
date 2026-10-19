"""Declared scalar analytic germ: subthreshold photon contractivity and certified pole boxes."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import check_bright_tail_domain as domain

shell=domain.shell;born=domain.born;phase=domain.phase;F=domain.F
ROOT=domain.ROOT;HOME=domain.HOME
CONTRACT=HOME/'contracts/complex-mass-analyticity.v1.json';PROOF=HOME/'COMPLEX-MASS-ANALYTICITY.md'
RESULT=HOME/'results/complex-mass-analyticity.v1.json'


def power(z,n):
    out=F(1)
    for _ in range(n):out=out*z
    return out


def elastic_entry(Y,eta):
    assert eta in (0,1)
    Z=Y*(F(1)+eta*Y)*(F(1)+eta*Y)
    assert F(1)+Z/4!=F()
    return (F(1)-Z/4)/(F(1)+Z/4)


def increasing_root_box(func,target,lower=Q(),upper=Q(1),steps=24):
    assert steps==24 and func(lower)<=target
    while func(upper)<target:upper*=2
    for _ in range(steps):
        mid=(lower+upper)/2;value=func(mid)
        if value==target:return mid,mid
        if value<target:lower=mid
        else:upper=mid
    assert func(lower)<=target<=func(upper)
    return lower,upper


def eta1_target_box():
    f=lambda a:a*(1-a)**2
    return increasing_root_box(f,Q(4),Q(2),Q(5,2))


def pole_box(epsilon_squared,eta):
    b=Q(epsilon_squared);assert b>0 and eta in (0,1)
    alo,ahi=(Q(4),Q(4)) if eta==0 else eta1_target_box()
    P=lambda t:b*b*t**5*(t+4)
    lo,_=increasing_root_box(P,alo*alo)
    _,hi=increasing_root_box(P,ahi*ahi)
    assert P(lo)<=alo*alo<=ahi*ahi<=P(hi)
    return {'a_lower':str(alo),'a_upper':str(ahi),'gamma_squared_lower':str(lo),'gamma_squared_upper':str(hi)}


def validate_contract(c):
    assert c['schema']=='marici.scattering.complex-mass-analyticity.v1'
    assert c['branch']=='w=sqrt(M-2)*sqrt(M+2);upper_continuation;w~M;beta=w/M'
    assert c['analytic_variable']=='M;also_track_s=M^2'
    assert c['analytic_scalar_Y']=='epsilon2^2*M^5*w(M)'
    assert c['controls']==[0,1] and c['root_bisection_steps']==24
    assert c['subthreshold_channel_test']=='open_photon_elastic_entry_only'
    assert c['conditional_domain']=='connected_first_M_quadrant_with_regular_boundary_values_above_and_below_pair_threshold'
    for key in ('eta0_subthreshold_elastic_unit_modulus','eta1_subthreshold_contractivity_failure',
                'nonremovable_imaginary_mass_poles_certified','pole_map_to_negative_s_retained',
                'source_packet_and_operator_analyticity_distinguished'):
        assert c[key] is True,key
    for key in ('identity_subthreshold_patch_matches_analytic_germ','closed_pair_channel_required_unitary_below_threshold',
                'complex_conjugation_used_as_holomorphic_continuation','all_squared_roots_are_poles',
                'all_complex_poles_classified','imaginary_mass_pole_is_positive_mass_bound_state',
                'entire_upper_M_holomorphy_is_general_QFT_axiom','source_QFT_left_hand_cut_domain_supplied',
                'source_QFT_analytic_sheet_identified',
                'source_packet_damping_repairs_operator_poles','all_local_UV_completions_excluded',
                'local_causal_scattering_realized','physical_rates_or_branching_derived','native_source_licensed',
                'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=domain.build();assert parent==json.loads(domain.RESULT.read_text(encoding='utf-8')),'stale bright-tail domain'
    sub_cases=0;above_cases=0
    for r in (F(Q(1,2)),F(1),F(2)):
        K=shell.scalar_kernel(r)
        for eta in (0,1):
            S=shell.completion(K,Q(eta))
            assert S[1][1]==elastic_entry(r*r,eta)
            assert phase.mm(phase.adj(S),S)==phase.eye(2);above_cases+=1
    for v in (F(Q(1,4)),F(1),F(2),F(4)):
        Y=phase.IM*v
        for eta in (0,1):
            Z=Y*(1+eta*Y)*(1+eta*Y)
            den=F(1)+Z/4;num=F(1)-Z/4
            E=elastic_entry(Y,eta);norm=E.conjugate()*E
            if eta==0:assert norm==F(1)
            else:
                assert Z+Z.conjugate()==-4*v*v
                assert (norm-1)*(den.conjugate()*den)==2*v*v
                assert born.incoming.x.positive(norm-1)
            assert E!=F(1);sub_cases+=1
    # Exact upper-rim witness M=sqrt(2), w=i*sqrt(2), epsilon2^2=1/8: Y=i.
    M=phase.SQ2;w=phase.IM*phase.SQ2;b=F(Q(1,8))
    assert w*w==M*M-4 and b*power(M,5)*w==phase.IM
    assert elastic_entry(phase.IM,0)==(F(15)-8*phase.IM)/17
    assert elastic_entry(phase.IM,1)==F(3)
    # Continue coefficient functions, not their pointwise complex adjoints.
    r=(F(1)+phase.IM)/phase.SQ2;assert r*r==phase.IM
    K=shell.scalar_kernel(r);assert phase.adj(K)!=K
    for eta in (0,1):
        H=phase.add(K,phase.scale(F(eta),phase.mm(K,phase.mm(K,K))))
        I=phase.eye(2)
        S=phase.mm(phase.add(I,phase.scale(phase.IM/2,H)),shell.inverse(phase.add(I,phase.scale(-phase.IM/2,H))))
        assert S[1][1]==elastic_entry(phase.IM,eta)
    # Imaginary M=i*gamma gives Y=-a, a=b*gamma^5*sqrt(gamma^2+4)>0.
    # eta1 has no a in [0,1] solving a*(1-a)^2=4, and one root above 1.
    assert Q(4,27)<4 and Q(2)*(1-Q(2))**2<4<Q(5,2)*(1-Q(5,2))**2
    for a in (Q(2),Q(9,4),Q(5,2)):
        assert (a-1)*(3*a-1)>0
    boxes={}
    previous={0:Q(),1:Q()}
    for b in (Q(1),Q(1,16),Q(1,65536)):
        boxes[str(b)]={}
        for eta in (0,1):
            box=pole_box(b,eta);boxes[str(b)][str(eta)]=box
            lo=Q(box['gamma_squared_lower']);hi=Q(box['gamma_squared_upper'])
            assert 0<lo<=hi and lo>previous[eta];previous[eta]=hi
            assert 2*lo**4*(3*lo+10)>0  # derivative of t^5*(t+4).
        assert Q(boxes[str(b)]['1']['gamma_squared_upper'])<Q(boxes[str(b)]['0']['gamma_squared_lower'])
    # D=1+Z/4, N=1-Z/4: at any certified Z=-4 root N=2, not zero.
    assert 1+Q(-4,4)==0 and 1-Q(-4,4)==2
    # Squaring alone adds an extraneous positive-real-mass solution, explicitly checked.
    M=phase.root(4);w=F(1);b=F(4)/(25*phase.root(4))
    assert w*w==M*M-4
    Y=b*power(M,5)*w;assert Y==F(4)
    assert b*b*power(M,10)*(M*M-4)==F(16)
    assert F(1)+Y/4==F(2)  # Not a pole of the eta0 elastic entry.
    refused=[]
    for name in ('identity_subthreshold_patch_matches_analytic_germ','closed_pair_channel_required_unitary_below_threshold',
                 'all_squared_roots_are_poles','imaginary_mass_pole_is_positive_mass_bound_state',
                 'entire_upper_M_holomorphy_is_general_QFT_axiom','source_packet_damping_repairs_operator_poles',
                 'all_local_UV_completions_excluded','local_causal_scattering_realized'):
        try:
            bad=copy.deepcopy(c);bad[name]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported analytic promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((domain.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_complex_mass_analyticity.py'))
    return {'schema':'marici.scattering.complex-mass-analyticity-receipt.v1','status':'pass',
        'scope_verdict':'specified_scalar_model_germ_and_conditional_open_photon_analyticity_test_not_a_general_local_QFT_no_go',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'real_open_channel_unitarity_checks':above_cases,'subthreshold_elastic_checks':sub_cases,
        'subthreshold_v1_witness':{'eta0':'(15-8*i)/17;norm_squared=1','eta1':'3;norm_squared=9'},
        'eta1_elastic_excess':'2*v^2/|1+Z/4|^2',
        'pole_boxes_by_epsilon2_squared_and_eta':boxes,'certified_pole_boxes':6,
        'pole_nonremovable_numerator':'2','squared_equation_positive_mass_extraneous_root_checked':True,
        'conditional_analyticity_obligation_failed':'eta1 analytic photon elastic continuation is not contractive on 0<M<2',
        'subthreshold_identity_patch_is_a_separate_prescription':True,
        'global_branch_and_causal_scattering_argument_machine_formalized':False,
        **{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale complex-mass audit'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','certified_pole_boxes','eta1_subthreshold_contractivity_failure',
        'all_local_UV_completions_excluded','physical_rates_or_branching_derived','hostile_controls_refused')}))


if __name__=='__main__':main()
