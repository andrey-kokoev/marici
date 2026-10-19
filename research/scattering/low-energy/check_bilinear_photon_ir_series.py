"""General ordered bilinear photon IR logs and certified physical-window tail bounds."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
from itertools import permutations
import json
from math import comb
from pathlib import Path
import check_degree6_photon_ir_logs as six

ct=six.ct;logs=six.logs;cut=six.cut;crossed=six.crossed;F=six.F;power=six.power
response=cut.response;ROOT=six.ROOT;HOME=six.HOME
CONTRACT=HOME/'contracts/bilinear-photon-ir-series.v1.json';PROOF=HOME/'BILINEAR-PHOTON-IR-SERIES.md'
RESULT=HOME/'results/bilinear-photon-ir-series.v1.json'


def pair_polynomials(k,l):
    """ORDERED pair: sum both (k,l) and (l,k) for a mixed monomial."""
    assert isinstance(k,int) and isinstance(l,int) and k>=2 and l>=2
    m=min(k,l);ek=cut.equal_cross_moment(k,0);el=cut.equal_cross_moment(l,0)
    d0=((1+ek)*(1+el)+ek*el)/16;o=(ek*el-(1+ek)*(1+el))/16
    D=[d0]+[Q()]*m;M=[Q()]*(m+1)
    for J in range(2,m+1):
        h=cut.mixed_cross_moment(k,J)*cut.mixed_cross_moment(l,J)
        for j,p in enumerate(logs.jacobi04(J-2)):M[j+2]+=Q(2*J+1,16)*h*p
        if J%2==0:
            e=cut.equal_cross_moment(k,J)*cut.equal_cross_moment(l,J)
            for j,p in enumerate(logs.legendre(J)):D[j]+=Q(2*J+1,8)*e*p
    return ct.trim(D),o,ct.trim(M),d0


def homogeneous_polynomials(q,coefficients):
    assert isinstance(q,int) and q>=4 and all(isinstance(k,int) and k>=2 for k in coefficients)
    D=[Q()];o=Q();M=[Q()];d0=Q()
    for k in range(2,q-1):
        l=q-k;weight=coefficients.get(k,Q())*coefficients.get(l,Q())
        if not weight:continue
        a,b,c,d=pair_polynomials(k,l)
        D=ct.add(D,ct.scale(weight,a));o+=weight*b;M=ct.add(M,ct.scale(weight,c));d0+=weight*d
    return D,o,M,d0


def scalar_logs(k,l):
    _,o,M,d0=pair_polynomials(k,l);q=k+l
    L=2*(-1)**q*sum((a/Q(q-j+1) for j,a in enumerate(M)),Q())
    K=-2*(-1)**q*sum((a/Q((q-j+1)**2) for j,a in enumerate(M)),Q())
    out={}
    for name,sign in (('minus',-1),('plus',1)):
        right=d0+sign*o;left=L+sign*2*(-1)**q*o/Q(q+1)
        out[name]={'right_cut':right,'crossed_log':left,'real_log':right+left,
                   'angular_constant':K-sign*2*(-1)**q*o/Q((q+1)**2)}
    return out


def pair_log_coefficients(cache,sigmas,k,l,order=(0,1,2,3)):
    D,o,M,_=pair_polynomials(k,l);q=k+l
    terms=crossed.tensor_terms(cache,order);hs=[sigmas[i] for i in order];out={}
    def add(s,a):
        key=tuple(s.encoded());out[key]=out.get(key,F())+a
    if len(set(hs))==1:
        for s,a in terms:add(s,-2*o*a*power(s,q-2))
    elif hs.count(1)==2:
        for index,(i,j,n,m) in enumerate(crossed.PAIRINGS):
            if hs[i]!=hs[j] or hs[n]!=hs[m]:continue
            s,a=terms[index];t,u=[terms[n][0] for n in range(3) if n!=index]
            group=sum((d*power(s,q-j-2)*power(t-u,j) for j,d in enumerate(D) if d),F())
            tp=sum((b*(-1)**j*power(s,j-2)*power(t,q-j) for j,b in enumerate(M) if b),F())
            up=sum((b*(-1)**j*power(s,j-2)*power(u,q-j) for j,b in enumerate(M) if b),F())
            add(s,2*a*group);add(t,2*a*tp);add(u,2*a*up)
            break
    return {s:a for s,a in out.items() if a!=F()}


def pair_scale_tensor(cache,sigmas,k,l):
    """Independent direct local representative for the sum of log coefficients."""
    D,o,M,_=pair_polynomials(k,l);q=k+l;terms=crossed.tensor_terms(cache)
    if len(set(sigmas))==1:return -2*o*sum((a*power(s,q-2) for s,a in terms),F())
    if sigmas.count(1)!=2:return F()
    for index,(i,j,n,m) in enumerate(crossed.PAIRINGS):
        if sigmas[i]!=sigmas[j] or sigmas[n]!=sigmas[m]:continue
        s,a=terms[index];t,u=[terms[n][0] for n in range(3) if n!=index]
        group=sum((d*power(s,q-j-2)*power(t-u,j) for j,d in enumerate(D) if d),F())
        crossed_part=sum((b*(-1)**j*power(s,j-2)*(power(t,q-j)+power(u,q-j)) for j,b in enumerate(M) if b),F())
        return 2*a*(group+crossed_part)
    return F()


def coefficient_norm(k,l):
    D,o,M,_=pair_polynomials(k,l)
    return sum((abs(a)*2**j for j,a in enumerate(D)),Q())+2*sum(map(abs,M),Q())+3*abs(o)


def input_majorant(c0,c1):return Q(16)+16*abs(Q(c0))+64*abs(Q(c1))


def tail_count(Qmax,s):
    s=Q(s);assert isinstance(Qmax,int) and Qmax>=4 and 0<=s<1
    return s**(Qmax+1)*(Q(Qmax-2)/(1-s)+s/(1-s)**2)


def kernel_tail(Qmax,s,c0=Q(),c1=Q()):
    """Entry/scalar cut bound U_Q; scale-running bound is U_Q/pi."""
    return Q(9,4)*input_majorant(c0,c1)**2*tail_count(Qmax,s)


def uniform_log_tail_half_window(Qmax,c0=Q(),c1=Q()):
    """nu=1 comparison control, 0<=s<=1/2: (1+pi+2)/pi < 7/3."""
    return Q(7,3)*kernel_tail(Qmax,Q(1,2),c0,c1)


def validate_contract(c):
    assert c['schema']=='marici.scattering.bilinear-photon-ir-series.v1'
    assert c['scope']=='pure_g2_power4;IR_momentum_series_at_fixed_coupling_order;declared_scalar_response_family'
    assert c['pair_convention']=='ordered_pairs;sum_k_l;r_k*r_l;no_extra_interference_factor'
    assert c['input_bound']=='|r_k|<=A*4^(-k);A=16+16*|c0|+64*|c1|;spectral_control_k>=4'
    assert c['domain']=='physical_helicity_entries_and_scalar_parity;0<s<1;all_physical_angles;positive_fixed_nu'
    assert c['tail']=='U_Q=(9/4)*A^2*s^(Q+1)*((Q-2)/(1-s)+s/(1-s)^2);Q>=4'
    for key in ('general_bilinear_cut_functional_constructed','general_local_scale_functional_constructed',
                'ordered_interference_normalization_retained','odd_and_even_crossing_signs_retained',
                'convergent_crossed_IR_log_series_in_certified_domain','endpoint_log_weights_controlled',
                'homogeneous_truncation_error_certified','finite_matching_data_retained',
                'independent_dimensionful_couplings_retained'):
        assert c[key] is True,key
    for key in ('certified_domain_is_maximal','all_subthreshold_convergence_derived','arbitrary_complex_kinematics_convergence_derived',
                'coupling_series_convergence_derived','finite_counterterm_series_convergence_derived',
                'spectral_control_source_licensed','full_order_g2_power4_amplitude_constructed',
                'full_EFT_anomalous_dimension_matrix_constructed','finite_matching_selected_by_running',
                'exact_scattering_operator_constructed','UV_completion_constructed','native_source_licensed',
                'physical_rates_or_branching_derived','live_proposition_inventory_changed','C12_protocol_renewed',
                'high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=six.build();assert parent==json.loads(six.RESULT.read_text(encoding='utf-8')),'stale degree-six audit'
    pi=json.loads(response.RESULT.read_text(encoding='utf-8'))['pi_from_J2_identity_box']
    assert 3<Q(pi['lower'])<Q(pi['upper'])<4
    legacy=0
    for k in (2,3,4):
        D,o,M,d0=logs.cut_polynomials(k)
        assert pair_polynomials(k,k)==(ct.trim(D),o,ct.trim(M),d0)
        assert scalar_logs(k,k)==logs.scalar_logs(k);legacy+=1
    for k,l,target in ((2,3,six.mixed.cut_polynomials()),(2,4,six.sector_polynomials('c0_r4'))):
        D,o,M,d0=pair_polynomials(k,l)
        assert (ct.scale(2,D),2*o,ct.scale(2,M),2*d0)==target;legacy+=1
    for name,row in scalar_logs(2,3).items():
        assert {key:2*v for key,v in row.items()}==six.mixed.scalar_logs()[name]
    norms=0;shapes=0
    for k in range(2,11):
        for l in range(2,11):
            m=min(k,l);D,o,M,_=pair_polynomials(k,l)
            assert pair_polynomials(k,l)==pair_polynomials(l,k)
            assert len(D)-1<=m and len(M)-1<=m and M[:2]==[0,0]
            assert all(a==0 for j,a in enumerate(D) if j%2);shapes+=1
            C=(m+1)**2*8**m
            assert coefficient_norm(k,l)<=C<=Q(9,4)*4**(k+l);norms+=1
    combinatorial=0
    for J in range(25):
        assert sum(map(abs,logs.legendre(J)),Q())<=3**J;combinatorial+=1
        if J>=2:
            assert sum(map(abs,logs.jacobi04(J-2)),Q())<=16*8**(J-2)<=8**J;combinatorial+=1
    for m in range(2,65):assert (m+1)**2<=Q(9,4)*2**m;combinatorial+=1
    spectral=0
    for n in range(65):
        assert response.coefficient(n+1)/response.coefficient(n)<Q(1,4)
        assert response.coefficient(n)/3<=Q(16,4**(n+4));spectral+=1
    # Independently extract every degree of a finite square on the normalized Bose carrier.
    extraction=0
    coeffs={2:Q(1),3:Q(-2),4:Q(1,3),5:Q(-1,7)}
    for q in range(4,11):
        D,o,M,d0=homogeneous_polynomials(q,coeffs)
        for name,sign in (('minus',-1),('plus',1)):
            amps=[Q()]*6
            for k,r in coeffs.items():amps[k]=r*cut.monomial_waves(k)['J0_'+name]
            squared=ct.multiply(amps,amps)
            assert d0+sign*o==squared[q]/8;extraction+=1
        for J in range(2,6):
            p=logs.jacobi04(J-2)
            ordered=sum((a*b/Q(i+j+3) for i,a in enumerate(M) for j,b in enumerate(p)),Q())
            amps=[Q()]*6
            for k,r in coeffs.items():amps[k]=r*cut.mixed_cross_moment(k,J)
            squared=ct.multiply(amps,amps);v=squared[q] if q<len(squared) else Q()
            assert 2*ordered==v/8;extraction+=1
    tensors=0;permuted=0;ward=0;lorentz=0;scales=0
    labels=((1,1),(-1,-1),(1,-1),(-1,1));packet=crossed.packet
    boost=packet.boost(packet.velocity([F(Q(1,8)),F(Q(1,6)),F()]))
    pairs=((2,3),(3,4),(2,5),(4,4))
    for index,(cosine,sine,E) in enumerate(((Q(3,5),Q(4,5),Q(1,2)),(Q(1),Q(),Q(1,2)))):
        ks=crossed.kinematics(cosine,sine,E)
        for inc in labels:
            for out in labels:
                h=inc+out;sigmas=(inc[0],inc[1],-out[0],-out[1]);es=crossed.polarizations(h,cosine,sine)
                cache=crossed.tensor_cache(ks,es)
                for k,l in pairs:
                    coefficients=pair_log_coefficients(cache,sigmas,k,l)
                    H=pair_scale_tensor(cache,sigmas,k,l)
                    assert H==sum(coefficients.values(),F());tensors+=1
                    for ell in (Q(-2),Q(1,3),Q(3,2)):
                        assert ell*sum(coefficients.values(),F())-ell*H==F();scales+=1
                    if index==0:
                        for order in permutations(range(4)):
                            assert pair_log_coefficients(cache,sigmas,k,l,order)==coefficients;permuted+=1
                    if index==0 and h in ((1,1,1,1),(1,1,-1,-1)):
                        for leg in range(4):
                            changed=es.copy();changed[leg]=ks[leg];altered=crossed.tensor_cache(ks,changed)
                            assert pair_log_coefficients(altered,sigmas,k,l)=={} and pair_scale_tensor(altered,sigmas,k,l)==F();ward+=1
                        transformed=crossed.tensor_cache([packet.act(boost,p) for p in ks],[packet.act(boost,e) for e in es])
                        assert pair_log_coefficients(transformed,sigmas,k,l)==coefficients and pair_scale_tensor(transformed,sigmas,k,l)==H;lorentz+=1
    # The tail count is independently summed via two geometric-series identities.
    tail_checks=0
    for s in (Q(),Q(1,4),Q(1,2),Q(3,4)):
        for N in (4,8,16,32,40,48):
            partial=sum(((q-3)*s**q for q in range(N+1,N+33)),Q())
            assert tail_count(N,s)==partial+tail_count(N+32,s);tail_checks+=1
    assert uniform_log_tail_half_window(40)<Q(1,10**7)
    assert uniform_log_tail_half_window(48)<Q(1,10**9)
    assert kernel_tail(40,Q(1,2))==Q(576*39,2**40)
    refused=[]
    for name in ('certified_domain_is_maximal','all_subthreshold_convergence_derived','arbitrary_complex_kinematics_convergence_derived',
                 'coupling_series_convergence_derived','finite_counterterm_series_convergence_derived','spectral_control_source_licensed',
                 'full_order_g2_power4_amplitude_constructed','finite_matching_selected_by_running'):
        try:
            bad=copy.deepcopy(c);bad[name]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported series promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((six.RESULT,response.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_bilinear_photon_ir_series.py'))
    return {'schema':'marici.scattering.bilinear-photon-ir-series-receipt.v1','status':'pass',
        'scope_verdict':'convergent_fixed_order_crossed_photon_IR_log_kernel_with_physical_window_tail_bound_not_full_amplitude',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'legacy_pair_controls':legacy,'pair_shape_checks':shapes,'pair_norm_bound_checks':norms,
        'combinatorial_bound_witnesses':combinatorial,'spectral_coefficient_bound_checks':spectral,
        'finite_square_projection_checks':extraction,'local_scale_tensor_checks':tensors,
        'all_outgoing_permutation_checks':permuted,'Ward_checks':ward,'Lorentz_checks':lorentz,'finite_scale_checks':scales,
        'geometric_tail_identity_checks':tail_checks,
        'zero_subtraction_spectral_control_uniform_log_tail_nu1_s_le_half':{
            str(N):str(uniform_log_tail_half_window(N)) for N in (32,40,48)},
        'all_degree_bound_and_convergence_argument_machine_formalized':False,
        **{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale bilinear photon IR series'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','pair_norm_bound_checks','local_scale_tensor_checks',
        'convergent_crossed_IR_log_series_in_certified_domain','full_order_g2_power4_amplitude_constructed','hostile_controls_refused')}))


if __name__=='__main__':main()
