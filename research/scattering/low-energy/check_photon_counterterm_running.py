"""Local on-shell counterterm representatives and scale cancellation for crossed IR logs."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
from itertools import permutations
import json
from math import comb,factorial
from pathlib import Path
import check_crossed_photon_ir_logs as logs

F=logs.F;phase=logs.phase;crossed=logs.crossed;power=logs.power
ROOT=logs.ROOT;HOME=logs.HOME
CONTRACT=HOME/'contracts/photon-counterterm-running.v1.json';PROOF=HOME/'PHOTON-COUNTERTERM-RUNNING.md'
RESULT=HOME/'results/photon-counterterm-running.v1.json'


def trim(p):
    p=list(p)
    while len(p)>1 and not p[-1]:p.pop()
    return p


def add(p,q):
    out=[Q()] * max(len(p),len(q))
    for i,a in enumerate(p):out[i]+=a
    for i,a in enumerate(q):out[i]+=a
    return trim(out)


def scale(a,p):return trim([a*b for b in p])


def multiply(p,q):
    out=[Q()]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):out[i+j]+=a*b
    return trim(out)


def poly_power(p,n):
    out=[Q(1)]
    for _ in range(n):out=multiply(out,p)
    return out


def basis_polynomials(q):
    assert q in (4,6,8)
    weights=[(a,b) for b in range(q//3+1) for a in range(q//2+1) if 2*a+3*b==q]
    e2=[Q(-1),Q(-1),Q(-1)];e3=[Q(),Q(-1),Q(-1)]
    all_same=[multiply(poly_power(e2,a),poly_power(e3,b)) for a,b in weights]
    mixed=[poly_power(e3,j) for j in range(q//2)]
    return weights,all_same,mixed


def decompose(target,basis):
    assert len({len(trim(p)) for p in basis})==len(basis),'dependent degree ordering'
    residual=trim(target);coeffs=[Q()]*len(basis)
    for i in sorted(range(len(basis)),key=lambda i:len(basis[i]),reverse=True):
        p=trim(basis[i]);degree=len(p)-1
        a=(residual[degree] if degree<len(residual) else Q())/p[-1]
        coeffs[i]=a;residual=add(residual,scale(-a,p))
    assert residual==[Q()],'outside declared on-shell basis'
    return coeffs


def scale_polynomials(k):
    D,o,M,_=logs.cut_polynomials(k);q=2*k
    same=scale(o,add(add([Q(1)],poly_power([Q(),Q(1)],q)),poly_power([Q(-1),Q(-1)],q)))
    mixed=[Q()]*(q+1)
    for j,d in enumerate(D):
        for m in range(j+1):mixed[m]+=d*comb(j,m)*2**m
    for j,a in enumerate(M):
        mixed[q-j]+=a*(-1)**j
        for m in range(q-j+1):mixed[m]+=a*(-1)**q*comb(q-j,m)
    return trim(same),trim(mixed)


def running_vectors(k):
    q=2*k;_,same,mixed=basis_polynomials(q);S,M=scale_polynomials(k)
    return decompose(S,same),decompose(M,mixed)


def basis_tensors(cache,sigmas,q,order=(0,1,2,3)):
    weights,same,mixed=basis_polynomials(q)
    terms=crossed.tensor_terms(cache,order);hs=[sigmas[i] for i in order]
    out=[F()]*(len(same)+len(mixed))
    if len(set(hs))==1:
        ps=-2*sum((a*power(s,q-2) for s,a in terms),F())
        e3sq=F()
        for i,(_,a) in enumerate(terms):
            t,u=[terms[j][0] for j in range(3) if j!=i]
            e3sq+=F(Q(-2,3))*a*power(t,2)*power(u,2)
        s,t,u=[a for a,_ in terms];e2=s*t+t*u+u*s
        if q==4:out[0]=ps/2
        elif q==6:out[0]=(3*e3sq-ps)/2;out[1]=e3sq
        else:out[0]=ps/2+4*e2*e3sq;out[1]=e2*e3sq
    elif hs.count(1)==2:
        for i,(a,b,c,d) in enumerate(crossed.PAIRINGS):
            if hs[a]!=hs[b] or hs[c]!=hs[d]:continue
            s,v=terms[i];t,u=[terms[j][0] for j in range(3) if j!=i]
            for j in range(len(mixed)):out[len(same)+j]=2*v*power(s,q-2-2*j)*power(t*u,j)
            break
    return out


def scalar_projection(p):return sum((a*Q((-1)**j,j+1) for j,a in enumerate(p)),Q())


def validate_contract(c):
    assert c['schema']=='marici.scattering.photon-counterterm-running.v1'
    assert c['scope']=='parity_even_on_shell_log_supported_all_same_and_two_plus_two_minus_sectors'
    assert c['degrees']==[4,6,8] and c['basis_dimensions']=={'4':3,'6':5,'8':6}
    assert c['local_normalization']=='B_local=(r^2/pi)*sum_i a_i(nu)*O_i'
    assert c['running']=='d a_i/d log(nu)=-h_i;nu_is_squared_mass_reference;leading_r_held_fixed'
    for key in ('local_on_shell_basis_constructed','Ward_Bose_crossing_representatives_constructed',
                'log_scale_dependence_cancelled','independent_finite_matching_data_retained',
                'leading_r_not_identified_with_new_counterterms','independent_dimensionful_couplings_retained'):
        assert c[key] is True,key
    for key in ('complete_off_shell_EFT_operator_basis_constructed','three_plus_one_contact_terms_excluded',
                'mass_scale_and_squared_mass_scale_betas_identical','finite_matching_selected_by_running',
                'running_of_g2_or_g3_derived','all_order_g2_power4_mixed_coefficients_constructed',
                'full_EFT_renormalization_completed','source_scale_derived','UV_completion_constructed',
                'exact_scattering_operator_constructed','native_source_licensed','physical_rates_or_branching_derived',
                'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=logs.build();assert parent==json.loads(logs.RESULT.read_text(encoding='utf-8')),'stale crossed IR logs'
    expected_same={2:[Q(-5,24)],3:[Q(1,16),Q(-3,32)],4:[Q(-7,40),Q(7,10)]}
    expected_mixed={2:[Q(21,160),Q(-7,240)],3:[Q(111,2240),Q(-293,6720),Q(5,336)],
                    4:[Q(341,3360),Q(-509,10080),Q(989,20160),Q(-5,672)]}
    data={};scalar_checks=0
    for k in (2,3,4):
        q=2*k;weights,S,M=basis_polynomials(q);hs,hm=running_vectors(k)
        assert hs==expected_same[k] and hm==expected_mixed[k]
        assert len(S)+len(M)==c['basis_dimensions'][str(q)]
        assert len({len(p) for p in S})==len(S) and len({len(p) for p in M})==len(M)
        for j,p in enumerate(M):assert scalar_projection(p)==Q(factorial(j)**2,factorial(2*j+1))
        ms=sum((h*scalar_projection(p) for h,p in zip(hm,M)),Q())
        ss=sum((h*scalar_projection(p) for h,p in zip(hs,S)),Q())
        assert ms-ss==logs.scalar_logs(k)['minus']['real_log'];scalar_checks+=1
        assert ms+ss==logs.scalar_logs(k)['plus']['real_log'];scalar_checks+=1
        data[str(q)]={'all_same_weights':[list(w) for w in weights],'all_same_h':[str(a) for a in hs],
            'mixed_h':[str(a) for a in hm],'normalized_beta_all_same':[str(-a) for a in hs],
            'normalized_beta_mixed':[str(-a) for a in hm],'operator_dimension':4+2*q}
    cancellations=0;permuted=0;ward=0;lorentz=0;matching_witnesses=0;physical=0
    labels=((1,1),(-1,-1),(1,-1),(-1,1));packet=crossed.packet
    L=packet.boost(packet.velocity([F(Q(1,8)),F(Q(1,6)),F()]))
    configs=((Q(3,5),Q(4,5),Q(1,2)),(Q(),Q(1),Q(1,3)),(Q(1),Q(),Q(1,2)))
    for index,(cosine,sine,E) in enumerate(configs):
        ks=crossed.kinematics(cosine,sine,E)
        for inc in labels:
            for out in labels:
                h=inc+out;sigmas=(h[0],h[1],-h[2],-h[3]);es=crossed.polarizations(h,cosine,sine)
                cache=crossed.tensor_cache(ks,es)
                for k in (2,3,4):
                    q=2*k;hs,hm=running_vectors(k);coeffs=hs+hm;O=basis_tensors(cache,sigmas,q)
                    if h in ((1,1,1,1),(1,1,-1,-1)):
                        _,S,M=basis_polynomials(q);s=F(4*E*E);x=F(-(1-cosine)/2)
                        if h==(1,1,1,1):expected=[F()]*len(S)+[power(s,q)*logs.evaluate(p,x) for p in M]
                        else:expected=[power(s,q)*logs.evaluate(p,x) for p in S]+[F()]*len(M)
                        assert O==expected;physical+=1
                    H=sum(logs.log_coefficients(cache,sigmas,k).values(),F())
                    assert sum((a*b for a,b in zip(coeffs,O)),F())==H
                    for ell in (Q(-2),Q(1,3),Q(3,2)):
                        shift=sum((-ell*a*b for a,b in zip(coeffs,O)),F())
                        assert ell*H+shift==F();cancellations+=1
                    if index==0:
                        for order in permutations(range(4)):
                            assert basis_tensors(cache,sigmas,q,order)==O;permuted+=1
                    if index==0 and h in ((1,1,1,1),(1,1,-1,-1)):
                        assert any(a!=F() for a in O);matching_witnesses+=1
                        for leg in range(4):
                            changed=es.copy();changed[leg]=ks[leg]
                            assert basis_tensors(crossed.tensor_cache(ks,changed),sigmas,q)==[F()]*len(O);ward+=1
                        boosted=crossed.tensor_cache([packet.act(L,p) for p in ks],[packet.act(L,e) for e in es])
                        assert basis_tensors(boosted,sigmas,q)==O;lorentz+=1
    refused=[]
    for name in ('complete_off_shell_EFT_operator_basis_constructed','three_plus_one_contact_terms_excluded',
                 'mass_scale_and_squared_mass_scale_betas_identical','finite_matching_selected_by_running',
                 'running_of_g2_or_g3_derived','all_order_g2_power4_mixed_coefficients_constructed',
                 'source_scale_derived','exact_scattering_operator_constructed'):
        try:
            bad=copy.deepcopy(c);bad[name]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported counterterm promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((logs.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_photon_counterterm_running.py'))
    return {'schema':'marici.scattering.photon-counterterm-running-receipt.v1','status':'pass',
        'scope_verdict':'on_shell_log_sector_counterterms_and_reference_scale_cancellation_not_finite_matching_or_full_EFT',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'counterterm_data_by_degree':data,'scalar_running_projection_checks':scalar_checks,
        'finite_scale_tensor_cancellation_checks':cancellations,'basis_permutation_checks':permuted,
        'Ward_counterterm_checks':ward,'Lorentz_counterterm_checks':lorentz,'physical_basis_normalization_checks':physical,
        'independent_finite_matching_tensor_witnesses':matching_witnesses,
        'general_basis_completeness_argument_machine_formalized':False,
        **{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale photon counterterm running'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','finite_scale_tensor_cancellation_checks','basis_permutation_checks',
        'finite_matching_selected_by_running','exact_scattering_operator_constructed','hostile_controls_refused')}))


if __name__=='__main__':main()
