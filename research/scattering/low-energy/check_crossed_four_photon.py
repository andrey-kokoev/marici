"""Leading crossed four-photon tensor and parity-resolved scalar partial-wave cuts."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
from itertools import combinations,permutations,product
import json
from math import comb
from pathlib import Path
import check_scalar_dispersive_response as response
import check_local_source_vertex as local

F=local.F;phase=local.phase;packet=local.packet
ROOT=response.ROOT;HOME=response.HOME
CONTRACT=HOME/'contracts/crossed-four-photon.v1.json';PROOF=HOME/'CROSSED-FOUR-PHOTON.md'
RESULT=HOME/'results/crossed-four-photon.v1.json'
PAIRINGS=((0,1,2,3),(0,2,1,3),(0,3,1,2))


def kinematics(c=Q(3,5),v=Q(4,5),E=Q(1)):
    c=F(c);v=F(v);E=F(E);assert c*c+v*v==F(1)
    return [[-E,F(),F(),-E],[-E,F(),F(),E],
            [E,E*v,F(),E*c],[E,-E*v,F(),-E*c]]


def polarizations(h,c=Q(3,5),v=Q(4,5)):
    assert len(h)==4 and all(a in (-1,1) for a in h)
    c=F(c);v=F(v);r=phase.SQ2;I=phase.IM;a,b,d,e=h
    # Incoming annihilation polarizations, outgoing creation polarizations.
    return [[F(),F(1)/r,I*a/r,F()],[F(),-F(1)/r,I*b/r,F()],
            [F(),c/r,-I*d/r,-v/r],[F(),-c/r,-I*e/r,v/r]]


def tensor_cache(ks,es):
    assert len(ks)==len(es)==4
    assert all(sum((k[i] for k in ks),F())==F() for i in range(4))
    vertices={};invariants={}
    for i,j in combinations(range(4),2):
        vertices[i,j]=local.two_amplitude([ks[i],ks[j]],[es[i],es[j]])
        p=[a+b for a,b in zip(ks[i],ks[j])]
        invariants[i,j]=packet.minkowski(p,p)
    return vertices,invariants


def tensor_terms(cache,order=(0,1,2,3)):
    vertices,invariants=cache;out=[]
    for i,j,k,l in PAIRINGS:
        ij=tuple(sorted((order[i],order[j])));kl=tuple(sorted((order[k],order[l])))
        assert invariants[ij]==invariants[kl]
        out.append((invariants[ij],2*vertices[ij]*vertices[kl]))
    return out


def coefficient_map(terms):
    out={}
    for s,a in terms:
        key=tuple(s.encoded());out[key]=out.get(key,F())+a
    return {s:a for s,a in out.items() if a!=F()}


def crossed_monomial_moment(k,J=0):
    assert isinstance(k,int) and k>=0 and J in (0,2)
    def z_moment(j):
        return Q(1,j+1) if J==0 else (Q(3,j+3)-Q(1,j+1))/2
    return Q((-1)**k,2**k)*sum((comb(k,j)*z_moment(j) for j in range(0,k+1,2)),Q())


def left_spectral_integral_box(beta,n=24):
    beta=Q(beta);assert 0<beta<=Q(1,2) and n>=1
    term=lambda k:Q(512*comb(k+4,4),2*k+3)*beta**(2*k+3)
    lo=sum((term(k) for k in range(n)),Q())
    hi=lo+term(n)/(1-3*beta*beta)
    return lo,hi


def validate_contract(c):
    assert c['schema']=='marici.scattering.crossed-four-photon.v1'
    assert c['tensor']=='2*sum_pairings det(qi,ei,qj,ej)*det(qk,ek,ql,el)*Pi((qi+qj)^2)'
    assert c['scalar_projection_measure']=='dz/2;transported_helicity_frames'
    assert c['partial_waves']=='A_minus=R(s)+C(s);A_plus=-C(s);C(s)=integral_0^1 R(-s*x)dx'
    assert c['cut_thresholds']=={'right':4,'left':-4}
    assert c['analytic_comparison_scope']=='order_g2_squared;massive_pair_loop_and_regular_local_counterterms;no_extra_massless_cut_at_this_order'
    for key in ('Bose_crossing_complete_leading_tensor_constructed','all_16_physical_helicity_assignments_retained',
                'Ward_identities_retained','scalar_right_cut_normalization_matched','crossed_left_cut_constructed',
                'free_local_subtraction_data_retained','selected_J0_parity_preserved_in_photon_elastic_block',
                'independent_dimensionful_couplings_retained'):
        assert c[key] is True,key
    for key in ('orthogonal_photon_complement_remains_identity','angular_dependence_proves_J0_to_J2_leakage',
                'scalar_parity_channels_mixed','zero_phase_Cayley_germ_matches_massive_pair_only_leading_response',
                'all_local_UV_completions_excluded','full_all_orders_crossing_and_unitarity_constructed',
                'local_interacting_QFT_constructed','contact_spectral_density_UV_extrapolation_source_licensed',
                'subtraction_constants_source_selected','native_source_licensed',
                'physical_rates_or_branching_derived','live_proposition_inventory_changed','C12_protocol_renewed',
                'high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=response.build();assert parent==json.loads(response.RESULT.read_text(encoding='utf-8')),'stale scalar response'
    ward=0;permuted=0;helicity_cases=0;matrix_cases=0;lorentz=0
    L=packet.boost(packet.velocity([F(Q(1,8)),F(Q(1,6)),F()]))
    for cosine,sine,E in ((Q(-3,5),Q(4,5),Q(1)),(Q(),Q(1),Q(1)),
                          (Q(3,5),Q(4,5),Q(1)),(Q(3,5),Q(4,5),Q(2))):
        ks=kinematics(cosine,sine,E)
        assert all(packet.minkowski(k,k)==F() for k in ks)
        for h in product((-1,1),repeat=4):
            es=polarizations(h,cosine,sine);cache=tensor_cache(ks,es);terms=tensor_terms(cache)
            assert all(packet.minkowski(k,e)==F() for k,e in zip(ks,es))
            baseline=coefficient_map(terms)
            for order in permutations(range(4)):
                assert coefficient_map(tensor_terms(cache,order))==baseline;permuted+=1
            if h[0]==h[1] and h[2]==h[3]:
                s,t,u=[a for a,_ in terms];a,b=h[0],h[2]
                expected=[a*b*s*s/2,F() if a==b else -t*t/2,F() if a==b else -u*u/2]
                assert [b for _,b in terms]==expected;matrix_cases+=1
            if h==(1,1,-1,-1):
                for i in range(4):
                    for j in range(4):
                        if i==j:continue
                        assert local.two_amplitude([ks[i],ks[j]],[ks[i],es[j]])==F();ward+=1
                boosted=tensor_cache([packet.act(L,k) for k in ks],[packet.act(L,e) for e in es])
                assert coefficient_map(tensor_terms(boosted))==baseline;lorentz+=1
            helicity_cases+=1
    moments={}
    for k in range(16):
        m0=crossed_monomial_moment(k,0);m2=crossed_monomial_moment(k,2)
        assert m0==Q((-1)**k,k+1)
        assert m2==Q((-1)**k*k*(k-1),(k+1)*(k+2)*(k+3))
        moments[str(k)]={'J0':str(m0),'J2':str(m2)}
    a4=response.coefficient(0);a5=response.coefficient(1)
    assert a4*(1+crossed_monomial_moment(4))==Q(1,5)
    assert -a4*crossed_monomial_moment(4)==Q(-1,30)
    assert a5*(1+crossed_monomial_moment(5))==Q(1,72)
    assert -a5*crossed_monomial_moment(5)==Q(1,360)
    assert a4*crossed_monomial_moment(4,2)==Q(1,105)
    assert crossed_monomial_moment(2,2)==Q(1,30)
    assert 1+crossed_monomial_moment(2)==Q(4,3)
    assert 1+crossed_monomial_moment(3)==Q(3,4)
    left={}
    for beta in (Q(1,4),Q(1,2)):
        v=4/(1-beta*beta);lo,hi=left_spectral_integral_box(beta)
        assert 0<lo<hi
        left[str(v)]={'minus_Im_Aminus_lower':str(lo/v),'minus_Im_Aminus_upper':str(hi/v),
                      'Im_Aplus_lower':str(lo/v),'Im_Aplus_upper':str(hi/v)}
        # Jacobian of integral_4^v t^3*beta(t) dt is 512*u^2/(1-u^2)^5.
        t=v;dt=8*beta/(1-beta*beta)**2
        assert t**3*beta*dt==512*beta**2/(1-beta*beta)**5
    # The geometric ratio certificate for positive spectral-integral coefficients.
    for n in range(16):
        assert 3*(n+1)*(2*n+5)-(n+5)*(2*n+3)==4*n*(n+2)>=0
    assert -2*Q(5,2)*Q(3,2)*Q(1,2)==Q(-15,4)
    assert 32*Q(2,3)/4==Q(16,3)
    refused=[]
    for name in ('orthogonal_photon_complement_remains_identity','angular_dependence_proves_J0_to_J2_leakage',
                 'scalar_parity_channels_mixed','zero_phase_Cayley_germ_matches_massive_pair_only_leading_response',
                 'all_local_UV_completions_excluded','full_all_orders_crossing_and_unitarity_constructed',
                 'local_interacting_QFT_constructed','physical_rates_or_branching_derived'):
        try:
            bad=copy.deepcopy(c);bad[name]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported crossed-tensor promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((response.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_crossed_four_photon.py'))
    return {'schema':'marici.scattering.crossed-four-photon-receipt.v1','status':'pass',
        'scope_verdict':'leading_imported_crossed_tensor_and_partial_wave_cuts_not_exact_native_scattering_dynamics',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'physical_helicity_configurations':helicity_cases,'all_outgoing_Bose_crossing_permutation_checks':permuted,
        'pair_vertex_Ward_checks':ward,'Lorentz_tensor_checks':lorentz,'equal_helicity_matrix_checks':matrix_cases,
        'exact_crossed_monomial_projection_moments':moments,'left_cut_positive_spectral_boxes':left,
        'J0_expansions':{'minus':'4*c0*s^2/3+3*c1*s^3/4+s^4/(5*pi)+s^5/(72*pi)+...',
                         'plus':'-c0*s^2/3+c1*s^3/4-s^4/(30*pi)+s^5/(360*pi)+...'},
        'zero_subtraction_J2_leading_coefficient':'minus:+1/(105*pi);plus:-1/(105*pi), multiplying s^4',
        'zero_phase_Cayley_leading_subthreshold_response':'-s^(5/2)*sqrt(4-s);nonanalytic_at_s=0',
        'leading_local_massive_pair_model_analytic_at_zero':True,
        'Cayley_third_s_derivative_leading':'-15/(4*sqrt(s))',
        'left_cut_threshold_magnitude':'(16/3)*(v-4)^(3/2)',
        'all_orders_massless_photon_cut_absent':False,'general_tensor_and_cut_argument_machine_formalized':False,
        **{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale crossed four-photon response'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','physical_helicity_configurations',
        'all_outgoing_Bose_crossing_permutation_checks','orthogonal_photon_complement_remains_identity',
        'full_all_orders_crossing_and_unitarity_constructed','hostile_controls_refused')}))


if __name__=='__main__':main()
