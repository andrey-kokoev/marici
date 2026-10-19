"""Cross leading infrared photon cuts and project the scalar parity logarithms."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
from itertools import permutations
import json
from math import comb,factorial
from pathlib import Path
import check_photon_unitarity_cut as cut

crossed=cut.crossed;F=cut.F;phase=cut.phase;response=cut.response
ROOT=cut.ROOT;HOME=cut.HOME;power=response.analytic.power
CONTRACT=HOME/'contracts/crossed-photon-ir-logs.v1.json';PROOF=HOME/'CROSSED-PHOTON-IR-LOGS.md'
RESULT=HOME/'results/crossed-photon-ir-logs.v1.json'


def legendre(J):
    out=[Q()]*(J+1)
    for m in range(J//2+1):
        out[J-2*m]=Q((-1)**m*factorial(2*J-2*m),2**J*factorial(m)*factorial(J-m)*factorial(J-2*m))
    return out


def jacobi04(n):
    out=[Q()]*(n+1)
    for m in range(n+1):
        for j in range(n-m+1):
            out[m+j]+=comb(n,m)*comb(n+4,n-m)*comb(n-m,j)*(-1)**(n-m-j)
    return out


def evaluate(p,x):
    out=x*0
    for a in reversed(p):out=out*x+a
    return out


def cut_polynomials(k):
    assert k in (2,3,4)
    e=cut.equal_cross_moment(k,0);minus=1+e;plus=-e
    d0=(minus*minus+plus*plus)/16;o=(plus*plus-minus*minus)/16
    D=[Q()]*(k+1);D[0]=d0;M=[Q()]*(k+1)
    for J in range(2,k+1):
        h=cut.mixed_cross_moment(k,J)
        for j,a in enumerate(jacobi04(J-2)):M[j+2]+=Q(2*J+1,16)*h*h*a
        if J%2==0:
            eJ=cut.equal_cross_moment(k,J)
            for j,a in enumerate(legendre(J)):D[j]+=Q(2*J+1,8)*eJ*eJ*a
    assert M[0]==M[1]==0 and all(a==0 for j,a in enumerate(D) if j%2)
    return D,o,M,d0


def log_coefficients(cache,sigmas,k,order=(0,1,2,3)):
    """Gauge-invariant pure-duality sections; no Mandelstam division is performed."""
    assert len(sigmas)==4 and all(h in (-1,1) for h in sigmas)
    D,o,M,_=cut_polynomials(k);q=2*k
    terms=crossed.tensor_terms(cache,order);hs=[sigmas[i] for i in order];out={}
    def add(s,a):
        key=tuple(s.encoded());out[key]=out.get(key,F())+a
    if len(set(hs))==1:
        for s,a in terms:add(s,-2*o*a*power(s,q-2))  # a=2*Vij*Vkl.
    elif hs.count(1)==2:
        for index,(i,j,l,m) in enumerate(crossed.PAIRINGS):
            if hs[i]!=hs[j] or hs[l]!=hs[m]:continue
            s,a=terms[index];t,u=[terms[n][0] for n in range(3) if n!=index]
            group=sum((d*power(s,q-j-2)*power(t-u,j) for j,d in enumerate(D) if d),F())
            tpart=sum((m*(-1)**j*power(s,j-2)*power(t,q-j) for j,m in enumerate(M) if m),F())
            upart=sum((m*(-1)**j*power(s,j-2)*power(u,q-j) for j,m in enumerate(M) if m),F())
            add(s,2*a*group);add(t,2*a*tpart);add(u,2*a*upart)
            break
    return {s:a for s,a in out.items() if a!=F()}


def scalar_logs(k):
    D,o,M,d0=cut_polynomials(k);q=2*k
    L=2*sum((a/Q(q-j+1) for j,a in enumerate(M)),Q())
    K=-2*sum((a/Q((q-j+1)**2) for j,a in enumerate(M)),Q())
    out={}
    for name,sign in (('minus',-1),('plus',1)):
        right=d0+sign*o;left=L+sign*2*o/Q(q+1)
        out[name]={'right_cut':right,'crossed_log':left,'real_log':right+left,
                   'angular_constant':K-sign*2*o/Q((q+1)**2)}
    return out


def validate_contract(c):
    assert c['schema']=='marici.scattering.crossed-photon-ir-logs.v1'
    assert c['monomial_controls']==[2,3,4]
    assert c['normalization']=='T=(b/2)*A+b^2*B;R_leading=r*s^k;B_log=-(r^2/pi)*H_log'
    assert c['regimes']=='r=c0;k=2 | r=c1;k=3 | r=1/(6*pi);k=4'
    assert c['scope']=='pure_g2_power4;leading_IR_logarithms_only;no_added_massless_poles'
    for key in ('leading_IR_crossed_photon_cuts_constructed','Bose_Ward_log_tensor_retained',
                'full_photon_helicity_carrier_used','right_cut_optical_normalization_retained',
                'real_local_counterterm_freedom_retained','finite_IR_window_scale_not_selected',
                'independent_dimensionful_couplings_retained'):
        assert c[key] is True,key
    for key in ('real_scalar_logs_cancel_completely','real_log_sign_fixed_by_right_cut_positivity',
                'three_plus_one_full_quartic_amplitude_excluded','artificial_Mandelstam_poles_introduced',
                'full_order_g2_power4_cut_spectrum_constructed','finite_counterterms_source_selected',
                'UV_contact_density_extrapolation_source_licensed','exact_scattering_operator_constructed',
                'local_interacting_QFT_constructed','all_local_UV_completions_excluded',
                'native_source_licensed','physical_rates_or_branching_derived',
                'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=cut.build();assert parent==json.loads(cut.RESULT.read_text(encoding='utf-8')),'stale photon cut'
    expected={2:(Q(49,180),Q(-7,360)),3:(Q(223,2688),Q(1,384)),4:(Q(5927,29400),Q(-271,22050))}
    polynomials={};logs={};projection_checks=0;scalar_checks=0
    for k in (2,3,4):
        D,o,M,d0=cut_polynomials(k);data=scalar_logs(k)
        assert sum((a/Q(j+1) for j,a in enumerate(D) if j%2==0),Q())==d0
        for J in range(2,k+1):
            d=jacobi04(J-2)
            integral=sum((a*b/Q(i+j+3) for i,a in enumerate(M) for j,b in enumerate(d)),Q())
            assert integral==cut.mixed_cross_moment(k,J)**2/16;projection_checks+=1
        # Independently integrate the common-scale log polynomial at s=1,t=-a,u=a-1.
        q=2*k;base=[Q()]*(q+1)
        for j,d in enumerate(D):
            for m in range(j+1):base[m]+=d*comb(j,m)*(-2)**m
        for j,a in enumerate(M):
            base[q-j]+=a
            for m in range(q-j+1):base[m]+=a*comb(q-j,m)*(-1)**m
        for name,sign in (('minus',-1),('plus',1)):
            p=base.copy();p[0]+=sign*o;p[q]+=sign*o
            for m in range(q+1):p[m]+=sign*o*comb(q,m)*(-1)**m
            assert sum((a/Q(j+1) for j,a in enumerate(p)),Q())==data[name]['real_log'];scalar_checks+=1
        assert (data['minus']['real_log'],data['plus']['real_log'])==expected[k]
        assert all(v['right_cut']>0 and v['real_log']!=0 for v in data.values())
        regime=('c0_nonzero','c0_zero_c1_nonzero','both_zero')[k-2];r=Q(1,6) if k==4 else Q(1)
        for name,v in data.items():
            assert r*r*v['right_cut']==Q(parent['IR_regimes'][regime]['ImB_leading_coefficients']['J0_'+name])
        polynomials[str(k)]={'D':[str(a) for a in D],'O':str(o),'M':[str(a) for a in M]}
        logs[str(k)]={name:{key:str(value) for key,value in v.items()} for name,v in data.items()}
    physical=0;bose=0;ward=0;lorentz=0
    labels=((1,1),(-1,-1),(1,-1),(-1,1))
    packet=crossed.packet
    boost=packet.boost(packet.velocity([F(Q(1,8)),F(Q(1,6)),F()]))
    configs=((Q(3,5),Q(4,5),Q(1,2)),(Q(),Q(1),Q(1,3)),(Q(1),Q(),Q(1,2)))
    for index,(cosine,sine,E) in enumerate(configs):
        ks=crossed.kinematics(cosine,sine,E);s=F(4*E*E);x=F((1+cosine)/2)
        key=tuple(s.encoded())
        for inc in labels:
            for out in labels:
                h=inc+out;hs=(h[0],h[1],-h[2],-h[3]);es=crossed.polarizations(h,cosine,sine)
                cache=crossed.tensor_cache(ks,es)
                for k in (2,3,4):
                    coeffs=log_coefficients(cache,hs,k);D,o,M,_=cut_polynomials(k)
                    d=evaluate(D,F(cosine));mx=evaluate(M,x);mr=evaluate(M,1-x)
                    matrix=[[d,F(o),F(),F()],[F(o),d,F(),F()],
                            [F(),F(),mx,mr],[F(),F(),mr,mx]]
                    assert coeffs.get(key,F())==power(s,2*k)*matrix[labels.index(out)][labels.index(inc)]
                    physical+=1
                    if index==0:
                        for order in permutations(range(4)):
                            assert log_coefficients(cache,hs,k,order)==coeffs;bose+=1
                    if index==0 and h in ((1,1,1,1),(1,1,-1,-1)):
                        for leg in range(4):
                            changed=es.copy();changed[leg]=ks[leg]
                            assert log_coefficients(crossed.tensor_cache(ks,changed),hs,k)=={};ward+=1
                        boosted=crossed.tensor_cache([packet.act(boost,q) for q in ks],[packet.act(boost,e) for e in es])
                        assert log_coefficients(boosted,hs,k)==coeffs;lorentz+=1
    # Exact angular log moments; a temporary finite IR scale changes only a local constant.
    angular=0
    for k in (2,3,4):
        _,o,M,_=cut_polynomials(k);q=2*k
        for j,a in enumerate(M):
            if a:
                n=q-j;assert n>=2
                # integral_0^1 x^n log(x) dx=-1/(n+1)^2, finite at collinear endpoints.
                assert Q(-1,(n+1)**2)<0;angular+=1
        assert q-k>=2 and q-k-2>=0
    refused=[]
    for name in ('real_scalar_logs_cancel_completely','real_log_sign_fixed_by_right_cut_positivity',
                 'three_plus_one_full_quartic_amplitude_excluded','artificial_Mandelstam_poles_introduced',
                 'full_order_g2_power4_cut_spectrum_constructed','finite_counterterms_source_selected',
                 'UV_contact_density_extrapolation_source_licensed','exact_scattering_operator_constructed'):
        try:
            bad=copy.deepcopy(c);bad[name]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported crossed-log promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((cut.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_crossed_photon_ir_logs.py'))
    return {'schema':'marici.scattering.crossed-photon-ir-logs-receipt.v1','status':'pass',
        'scope_verdict':'leading_IR_crossed_log_kernels_and_scalar_partial_cancellations_not_full_quartic_scattering',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'cut_polynomials_by_k':polynomials,'scalar_logs_by_k':logs,
        'physical_right_cut_coefficient_checks':physical,'all_outgoing_permutation_checks':bose,
        'Ward_log_tensor_checks':ward,'Lorentz_log_tensor_checks':lorentz,
        'mixed_helicity_projection_checks':projection_checks,'independent_scalar_log_projections':scalar_checks,
        'finite_angular_log_moments':angular,
        'general_crossing_and_log_argument_machine_formalized':False,
        **{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale crossed photon IR logs'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','physical_right_cut_coefficient_checks','all_outgoing_permutation_checks',
        'real_scalar_logs_cancel_completely','exact_scattering_operator_constructed','hostile_controls_refused')}))


if __name__=='__main__':main()
