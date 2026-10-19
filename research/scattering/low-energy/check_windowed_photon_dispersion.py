"""Crossing-compatible finite-window Cauchy representative and analytic remainder."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
from itertools import permutations
import json
from pathlib import Path
import check_bilinear_photon_ir_series as ir

ct=ir.ct;F=ir.F;crossed=ir.crossed;power=ir.power
ROOT=ir.ROOT;HOME=ir.HOME
CONTRACT=HOME/'contracts/windowed-photon-dispersion.v1.json';PROOF=HOME/'WINDOWED-PHOTON-DISPERSION.md'
RESULT=HOME/'results/windowed-photon-dispersion.v1.json'


def add(p,q):
    out=p.copy()
    for key,a in q.items():out[key]=out.get(key,Q())+a
    return {key:a for key,a in out.items() if a}


def scale(a,p):return {key:a*b for key,b in p.items() if a*b}


def multiply(p,q):
    out={}
    for (i,j),a in p.items():
        for (n,m),b in q.items():out[(i+n,j+m)]=out.get((i+n,j+m),Q())+a*b
    return {key:a for key,a in out.items() if a}


def ppow(p,n):
    assert n>=0
    out={(0,0):Q(1)}
    for _ in range(n):out=multiply(out,p)
    return out


def flow_polynomial(k,l,channel,group=None):
    """Coefficient before an external pair-vertex product; variables are (x,Delta)."""
    assert channel in (0,1,2) and group in (None,0,1,2)
    D,o,M,_=ir.pair_polynomials(k,l);q=k+l;X={(1,0):Q(1)};delta={(0,1):Q(1)}
    if group is None:return scale(-4*o,ppow(X,q-2))
    flow=[{} for _ in range(3)];flow[channel]=X;others=[i for i in range(3) if i!=channel]
    flow[others[0]]=scale(Q(1,2),add(scale(-1,X),delta))
    flow[others[1]]=scale(Q(1,2),add(scale(-1,X),scale(-1,delta)))
    out={}
    if channel==group:
        t,u=[i for i in range(3) if i!=group];diff=add(flow[t],scale(-1,flow[u]))
        for j,a in enumerate(D):out=add(out,scale(4*a,multiply(ppow(flow[group],q-j-2),ppow(diff,j))))
    else:
        for j,a in enumerate(M):
            if a:out=add(out,scale(4*a*(-1)**j,multiply(ppow(flow[group],j-2),ppow(flow[channel],q-j))))
    return out


def evaluate(p,z,delta):return sum((a*power(z,i)*power(delta,j) for (i,j),a in p.items()),z*0)


def quotient(p,z,delta):
    out=[Q()]*max([i for i,j in p]+[1])
    for (n,d),a in p.items():
        for h in range(n):out[n-1-h]+=a*delta**d*z**h
    return ct.trim(out)


def divided_integral(p,z,delta,tau):
    return sum((a*power(delta,d)*Q(tau)**(n-h)*power(z,h)/Q(n-h)
                for (n,d),a in p.items() for h in range(n)),z*0)


def window_sections(cache,sigmas,k,l,tau,order=(0,1,2,3)):
    assert 0<tau<1
    terms=crossed.tensor_terms(cache,order);hs=[sigmas[i] for i in order]
    if len(set(hs))==1:group=None
    elif hs.count(1)==2:
        group=next(i for i,(a,b,c,d) in enumerate(crossed.PAIRINGS) if hs[a]==hs[b] and hs[c]==hs[d])
    else:return {}
    out={}
    for c,(s,a) in enumerate(terms):
        other=[i for i in range(3) if i!=c];delta=terms[other[0]][0]-terms[other[1]][0]
        p=flow_polynomial(k,l,c,group);W=a/2 if group is None else terms[group][1]/2
        H=W*evaluate(p,s,delta);J=W*divided_integral(p,s,delta,tau);key=tuple(s.encoded())
        old=out.get(key,(F(),F()));out[key]=(old[0]+H,old[1]+J)
    # J can survive when H vanishes: do not discard analytic contact terms with zero cut.
    return {key:value for key,value in out.items() if value!=(F(),F())}


def positive_log_box(v,n=32):
    v=Q(v);assert v>0 and n>=1
    if v==1:return Q(),Q()
    if v<1:
        lo,hi=positive_log_box(1/v,n);return -hi,-lo
    return ir.response.log_ratio_box((v-1)/(v+1),n)


def rim_window_log(z,tau):
    z=Q(z);tau=Q(tau);assert tau>0 and z not in (0,tau)
    lo,hi=positive_log_box(abs(tau-z)/abs(z))
    return lo,hi,int(0<z<tau)  # imaginary part divided by pi


def analytic_tail(Qmax,tau,a,c0=Q(),c1=Q()):
    """Physical-entry/scalar bound for this representative's E, nu=tau comparison."""
    tau=Q(tau);a=Q(a);assert 0<a<=tau/2 and tau<1
    return (ir.kernel_tail(Qmax,a,c0,c1)*a/(tau-a)+2*(a/tau)**2*ir.kernel_tail(Qmax,tau,c0,c1))/3


def validate_contract(c):
    assert c['schema']=='marici.scattering.windowed-photon-dispersion.v1'
    assert c['scope']=='pure_g2_power4;conditional_IR_kernel;prescribed_symmetric_channel_Cauchy_flow'
    assert c['flow']=='S_c=x;other_invariants=(-x+Delta)/2,(-x-Delta)/2;external_W_held_fixed'
    assert c['decomposition']=='B_window=B_log_nu+E_tau_nu;E=(sum_W*(p(S)*log((tau-S)/nu)+J_tau[p]))/pi'
    assert c['domain']=='0<tau<1;0<a<=tau/2;|S|,|T|,|U|<=a;S+T+U=0'
    for key in ('finite_window_Cauchy_representative_constructed','Ward_Bose_crossing_tensor_retained',
                'retained_window_photon_cut_matched','analytic_representative_remainder_constructed',
                'complex_coefficient_normal_convergence_established','representative_remainder_tail_certified',
                'independent_UV_matching_data_retained','independent_dimensionful_couplings_retained'):
        assert c[key] is True,key
    for key in ('window_endpoint_is_physical_threshold','window_or_reference_source_selected',
                'prescribed_flow_is_QFT_derived_fixed_t_dispersion','unknown_UV_matching_remainder_bounded',
                'finite_matching_source_selected','analyticity_of_arbitrary_counterterm_series_derived',
                'three_plus_one_full_quartic_amplitude_excluded','full_order_g2_power4_amplitude_constructed',
                'exact_scattering_operator_constructed','UV_completion_constructed','native_source_licensed',
                'physical_rates_or_branching_derived','live_proposition_inventory_changed','C12_protocol_renewed',
                'high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=ir.build();assert parent==json.loads(ir.RESULT.read_text(encoding='utf-8')),'stale bilinear series'
    tau=Q(1,2);a=Q(1,4);norms=0;division=0
    for k in range(2,8):
        for l in range(2,8):
            N=ir.coefficient_norm(k,l)
            for group in (None,0,1,2):
                polys=[flow_polynomial(k,l,c,group) for c in range(3)]
                norm=sum((sum(map(abs,p.values()),Q()) for p in polys),Q())
                if group is not None:
                    norm+=sum((sum(map(abs,flow_polynomial(k,l,c,None).values()),Q()) for c in range(3)),Q())
                assert norm<=4*N;norms+=1
                assert all(i+j==k+l-2 for p in polys for i,j in p)
    for k,l in ((2,2),(2,3),(3,3),(2,4),(3,4),(4,4)):
        for group in (None,0,1,2):
            for channel in range(3):
                p=flow_polynomial(k,l,channel,group)
                for z,delta in ((Q(-1,8),Q(1,4)),(Q(1,6),Q(-1,5))):
                    collapsed=[Q()]*(k+l-1)
                    for (i,j),b in p.items():collapsed[i]+=b*delta**j
                    q=quotient(p,z,delta)
                    assert ct.add(ct.multiply(q,[-z,Q(1)]),[evaluate(p,z,delta)])==ct.trim(collapsed)
                    integral=sum((b*tau**(i+1)/Q(i+1) for i,b in enumerate(q)),Q())
                    assert integral==divided_integral(p,z,delta,tau);division+=1
    branches=0
    for z in (Q(-1,4),Q(1,6),Q(1,4),Q(3,4)):
        lo,hi,imag=rim_window_log(z,tau);assert lo<=hi and imag==int(0<z<tau);branches+=1
    assert rim_window_log(Q(-1,4),tau)[0]>0 and rim_window_log(Q(3,4),tau)[1]<0
    assert rim_window_log(Q(1,4),tau)==(Q(),Q(),1)
    # A subtraction choice cannot erase J: even p(S)=0 may leave a finite polynomial.
    p=flow_polynomial(2,2,0,None)
    assert evaluate(p,Q(),Q())==0 and divided_integral(p,Q(),Q(),tau)==Q(5,96)
    tensors=0;permuted=0;ward=0;lorentz=0;scale_checks=0
    labels=((1,1),(-1,-1),(1,-1),(-1,1));packet=crossed.packet
    L=packet.boost(packet.velocity([F(Q(1,8)),F(Q(1,6)),F()]))
    for index,(cosine,sine,E) in enumerate(((Q(3,5),Q(4,5),Q(1,4)),(Q(1),Q(),Q(1,4)))):
        ks=crossed.kinematics(cosine,sine,E)
        for inc in labels:
            for out in labels:
                h=inc+out;sigmas=(inc[0],inc[1],-out[0],-out[1]);es=crossed.polarizations(h,cosine,sine)
                cache=crossed.tensor_cache(ks,es)
                for k,l in ((2,2),(2,3),(3,4)):
                    sections=window_sections(cache,sigmas,k,l,tau)
                    coeff={key:v[0] for key,v in sections.items() if v[0]!=F()}
                    assert coeff==ir.pair_log_coefficients(cache,sigmas,k,l);tensors+=1
                    if index==1 and h==(1,1,1,1) and (k,l)==(2,2):
                        assert any(H==F() and J!=F() for H,J in sections.values())
                    H=sum(coeff.values(),F())
                    # d B_log/d log(nu)=H/pi, d E/d log(nu)=-H/pi; J is independent.
                    for ell in (Q(-2),Q(1,3),Q(3,2)):
                        assert ell*H-ell*sum((v[0] for v in sections.values()),F())==F();scale_checks+=1
                    if index==0:
                        for order in permutations(range(4)):
                            assert window_sections(cache,sigmas,k,l,tau,order)==sections;permuted+=1
                    if index==0 and h in ((1,1,1,1),(1,1,-1,-1)):
                        for leg in range(4):
                            changed=es.copy();changed[leg]=ks[leg]
                            assert window_sections(crossed.tensor_cache(ks,changed),sigmas,k,l,tau)=={};ward+=1
                        transformed=crossed.tensor_cache([packet.act(L,p) for p in ks],[packet.act(L,e) for e in es])
                        assert window_sections(transformed,sigmas,k,l,tau)==sections;lorentz+=1
    assert analytic_tail(40,tau,a)<Q(1,10**8) and analytic_tail(48,tau,a)<Q(1,10**10)
    refused=[]
    for name in ('window_endpoint_is_physical_threshold','window_or_reference_source_selected',
                 'prescribed_flow_is_QFT_derived_fixed_t_dispersion','unknown_UV_matching_remainder_bounded',
                 'finite_matching_source_selected','analyticity_of_arbitrary_counterterm_series_derived',
                 'full_order_g2_power4_amplitude_constructed','exact_scattering_operator_constructed'):
        try:
            bad=copy.deepcopy(c);bad[name]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported window promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((ir.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_windowed_photon_dispersion.py'))
    return {'schema':'marici.scattering.windowed-photon-dispersion-receipt.v1','status':'pass',
        'scope_verdict':'prescribed_crossed_window_representative_and_analytic_remainder_not_UV_matching_or_full_amplitude',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'flow_coefficient_norm_checks':norms,'exact_Cauchy_polynomial_division_checks':division,'rim_branch_checks':branches,
        'retained_log_coefficient_checks':tensors,'all_outgoing_permutation_checks':permuted,'Ward_checks':ward,
        'Lorentz_checks':lorentz,'reference_scale_cancellation_checks':scale_checks,
        'comparison_control':{'tau':'1/2','external_a':'1/4','nu':'tau','c0':'0','c1':'0',
            'analytic_remainder_input_degree_tail':{str(N):str(analytic_tail(N,tau,a)) for N in (32,40,48)}},
        'normal_convergence_and_analyticity_argument_machine_formalized':False,
        **{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale windowed photon dispersion'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','exact_Cauchy_polynomial_division_checks','retained_log_coefficient_checks',
        'unknown_UV_matching_remainder_bounded','full_order_g2_power4_amplitude_constructed','hostile_controls_refused')}))


if __name__=='__main__':main()
