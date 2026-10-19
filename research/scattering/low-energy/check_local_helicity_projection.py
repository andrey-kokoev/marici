"""Exact full-helicity norms and retained-mode projections of the local current candidates."""
import argparse
import copy
from fractions import Fraction as Q
from itertools import product
import hashlib
import json
from pathlib import Path
import check_local_source_vertex as local

F=local.F;phase=local.phase;cm=local.cm;packet=local.packet;m=packet.m;ROOT=local.ROOT;HOME=local.HOME
CONTRACT=HOME/'contracts/local-helicity-projection.v1.json'
PROOF=HOME/'LOCAL-HELICITY-PROJECTION.md'
RESULT=HOME/'results/local-helicity-projection.v1.json'


def closed_amplitude(ks,helicities):
    M=sum((k[0] for k in ks),F());N=[F(),F(),F(1)]
    ys=[F(1)-2*k[0]/M for k in ks]
    out=[F(),F(),F()]
    for i,k in enumerate(ks):
        j,l=[j for j in range(3) if j!=i]
        if helicities[j]!=helicities[l]:continue
        tangent=local.three.cross(N,local.three.direction(k));a=ys[i]*(F(1)-ys[i])
        for r in range(3):out[r]+=a*(tangent[r]+phase.IM*helicities[i]*N[r])
    return [F()]+[m.scalar_power(M,4)*v/(2*phase.SQ2) for v in out]


def shape_polynomials():
    ys=[m.var(i) for i in range(3)];S2=m.add(*(m.power(y,2) for y in ys))
    S=m.add(m.const(1),m.scale(F(-1),S2));P=m.mul(ys[0],m.mul(ys[1],ys[2]))
    aa=[m.mul(y,m.add(m.const(1),m.scale(F(-1),y))) for y in ys]
    same=m.scale(F(Q(1,4)),m.add(m.power(S,2),m.scale(F(-6),P)))
    mixed=[m.scale(F(Q(1,4)),m.power(a,2)) for a in aa]
    return S,P,same,mixed


def validate_contract(c):
    assert c['schema']=='marici.scattering.local-helicity-projection.v1'
    assert c['outgoing_coefficient_convention']=='complex_conjugate_of_local_Ward_tensor'
    assert c['conditional_shape_measure']=='2*dy1*dy2 times normalized SO3 Haar'
    assert c['old_equal_helicity_choice']==1
    for key in ('all_eight_helicity_assignments_retained','orthogonal_profile_remainder_retained','old_band_mass_support_retained'):
        assert c[key] is True
    for key in ('normalizable_incident_Dirac_packet_constructed','physical_source_current_matrix_element_bound',
                'native_Dirac_source_licensed','local_candidate_closes_on_prior_selected_profiles',
                'projection_fraction_is_annihilation_branching','selected_profile_projection_preserves_microcausality',
                'UV_source_form_factor_selected','self_adjoint_interacting_QFT_constructed',
                'annihilation_rate_derived','branching_ratio_derived','live_proposition_inventory_changed',
                'C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=local.build();assert parent==json.loads(local.RESULT.read_text(encoding='utf-8')),'stale local source vertex'
    S,P,same,mixed=shape_polynomials();h=packet.tail.triplet_extra_profile()
    assert m.simplex_integral(m.power(S,2))==F(Q(4,15))
    assert m.simplex_integral(P)==F(Q(1,60))
    same_each=m.simplex_integral(same)/3
    mixed_each=[m.simplex_integral(p)/3 for p in mixed]
    assert same_each==F(Q(1,72)) and mixed_each==[F(Q(1,360))]*3
    mixed_total=2*sum(mixed_each,F());total=2*same_each+mixed_total
    assert mixed_total==F(Q(1,60)) and total==F(Q(2,45))
    coeff0=-phase.IM*m.simplex_integral(S)/(2*phase.SQ6)
    coeff1=-phase.IM*m.simplex_integral(m.mul(h,S))/(2*phase.SQ6)
    selected=coeff0.conjugate()*coeff0+coeff1.conjugate()*coeff1
    assert coeff0.conjugate()*coeff0==F(Q(1,96)) and coeff1.conjugate()*coeff1==F(Q(1,1440))
    assert selected==F(Q(1,90)) and selected/total==F(Q(1,4))
    assert coeff1.conjugate()*coeff1/total==F(Q(1,64))  # Above the old band, only the added profile is available.
    normal=m.scale(F(Q(1,24)),m.power(S,2))
    assert m.simplex_integral(normal)==selected
    # The two selected shape polynomials span the complete +++ normal part.
    reconstructed=m.add(m.const(Q(1,2)),m.scale(-F(1)/(2*phase.root(6)),h))
    assert reconstructed==S
    in_plane=same_each-selected;assert in_plane==F(Q(1,360))
    normalize=3*phase.root(5)/2
    assert normalize*normalize*total==F(1)
    assert normalize*coeff0==-phase.IM*phase.root(6)/8 and normalize*coeff1==phase.IM/8
    residual_coefficient=phase.SQ3/2
    assert normalize*normalize*selected+residual_coefficient*residual_coefficient==F(1)
    fractions={'selected_old_normal':F(Q(15,64)),'selected_added_normal':F(Q(1,64)),
               'same_plus_in_plane_remainder':F(Q(1,16)),'all_minus_remainder':F(Q(5,16)),
               'mixed_helicity_remainder':F(Q(3,8))}
    assert sum(fractions.values(),F())==F(1)
    assert same_each/total==F(Q(5,16)) and mixed_total/total==F(Q(3,8))
    configs=[[[F(1),F(1),F(),F()],[F(1),-F(1)/2,phase.SQ3/2,F()],[F(1),-F(1)/2,-phase.SQ3/2,F()]],
             [[F(1),F(1),F(),F()],[F(1),F(),F(1),F()],[phase.SQ2,F(-1),F(-1),F()]]]
    group,_,spin=phase.source_group();rotations=[phase.spatial(phase.from_spin(spin,q)) for q in sorted(group)]
    checks=0;norm_checks=0;moment_checks=0
    for base in configs:
        for t in (F(1),F(2),F(3)):
            ks=[[t*v for v in k] for k in base];M=sum((k[0] for k in ks),F())
            ys=[F(1)-2*k[0]/M for k in ks]
            frames={h:local.three.helicity_frame(ks,[F(),F(),F(1)],h) for h in (-1,1)}
            for helicities in product((-1,1),repeat=3):
                es=[[F()]+frames[h][i] for i,h in enumerate(helicities)]
                A=local.three_amplitude(ks,es);assert A==closed_amplitude(ks,helicities);checks+=1
                poly=same if len(set(helicities))==1 else mixed[next(i for i in range(3) if helicities.count(helicities[i])==1)]
                norm=sum((v.conjugate()*v for v in A[1:]),F())
                assert norm==m.scalar_power(M,8)*m.evaluate(poly,ys);norm_checks+=1
                if t==F(1):
                    outgoing=[v.conjugate() for v in A[1:]];N=[F(),F(),F(1)]
                    average=[[F() for _ in range(3)] for _ in range(3)]
                    angular_gram=[[F() for _ in range(3)] for _ in range(3)]
                    for R in rotations:
                        nr=cm.act(R,N);ar=cm.act(R,outgoing)
                        for i in range(3):
                            for j in range(3):
                                average[i][j]+=nr[i]*ar[j]/len(rotations)
                                angular_gram[i][j]+=ar[i].conjugate()*ar[j]/len(rotations)
                    assert angular_gram==[[F(int(i==j))*norm/3 for j in range(3)] for i in range(3)]
                    assert average==[[F(int(i==j))*outgoing[2]/3 for j in range(3)] for i in range(3)];moment_checks+=1
    # Two-photon pseudoscalar, unit M, opposite directions, transported helicity frames.
    ks=[[F(1)/2,F(),F(),F(1)/2],[F(1)/2,F(),F(),-F(1)/2]]
    two_coeffs={}
    for h1,h2 in product((-1,1),repeat=2):
        es=[[F(),F(1)/phase.SQ2,h1*phase.IM/phase.SQ2,F()],
            [F(),F(1)/phase.SQ2,-h2*phase.IM/phase.SQ2,F()]]
        a=local.two_amplitude(ks,es).conjugate()
        assert a==(phase.IM*h1/2 if h1==h2 else F())
        two_coeffs[str((h1,h2))]=a
    two_norm=sum((v.conjugate()*v for v in two_coeffs.values()),F())
    assert two_norm==F(Q(1,2))
    added_two=two_coeffs[str((-1,-1))]
    assert added_two.conjugate()*added_two/two_norm==F(Q(1,2))
    refused=[]
    for name in ('erase_mixed_helicity_norm','declare_selected_profile_complete','drop_all_minus_sector',
                 'ignore_old_band_mass_support','projection_is_branching','promote_incident_source_binding'):
        try:
            if name=='erase_mixed_helicity_norm':assert mixed_total==F()
            elif name=='declare_selected_profile_complete':assert selected==total
            elif name=='drop_all_minus_sector':assert same_each==F()
            else:
                bad=copy.deepcopy(c)
                key={'ignore_old_band_mass_support':'old_band_mass_support_retained',
                     'projection_is_branching':'projection_fraction_is_annihilation_branching',
                     'promote_incident_source_binding':'physical_source_current_matrix_element_bound'}[name]
                bad[key]=name!='ignore_old_band_mass_support';validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported profile promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((local.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_local_helicity_projection.py'))
    return {'schema':'marici.scattering.local-helicity-projection-receipt.v1','status':'pass',
        'scope_verdict':'full_relative_helicity_projection_of_specific_imported_current_vertices_not_incident_preparation_or_rates',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'closed_helicity_tensor_cases':checks,'pointwise_helicity_norm_checks':norm_checks,
        'second_rotation_moment_checks':moment_checks,
        'three_photon_squared_norm_per_current_component':'(2/45)*M^8',
        'three_photon_normalized_full_helicity_isometry_constructed':True,
        'normalized_selected_coefficients':['-i*sqrt(15)/8','i/8'],
        'one_additional_orthogonal_triplet_retains_this_candidate_output':True,
        'normalized_residual_triplet_coefficient':'sqrt(3)/2',
        'three_photon_norm_partition':{k:str(v.v[0]) for k,v in fractions.items()},
        'prior_profile_span_selected_fraction':'1/4','prior_profile_span_orthogonal_remainder':'3/4',
        'with_old_band_support_selected_fraction':{'0<M<4':'1/4','M>4':'1/64'},
        'two_photon_squared_norm_per_pseudoscalar_current':'M^4/2',
        'normalized_two_photon_state':'i*(|++>-|-->)/sqrt(2)',
        'two_photon_selected_fraction_with_old_band_support':{'0<M<4':'1','M>4':'1/2'},
        'analytic_Haar_and_helicity_argument_machine_formalized':False,**{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale local helicity projection'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','closed_helicity_tensor_cases','prior_profile_span_selected_fraction',
        'prior_profile_span_orthogonal_remainder','normalizable_incident_Dirac_packet_constructed',
        'branching_ratio_derived','hostile_controls_refused')}))


if __name__=='__main__':main()
