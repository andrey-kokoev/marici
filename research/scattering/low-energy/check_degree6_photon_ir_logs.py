"""Complete homogeneous degree-six photon IR logs for R=c0*s^2+c1*s^3+r4*s^4+... ."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
from itertools import permutations
import json
from math import comb
from pathlib import Path
import check_mixed_photon_ir_logs as mixed

ct=mixed.ct;logs=mixed.logs;cut=mixed.cut;crossed=mixed.crossed;F=mixed.F;power=mixed.power
ROOT=mixed.ROOT;HOME=mixed.HOME
CONTRACT=HOME/'contracts/degree6-photon-ir-logs.v1.json';PROOF=HOME/'DEGREE6-PHOTON-IR-LOGS.md'
RESULT=HOME/'results/degree6-photon-ir-logs.v1.json'
SECTORS=('c1_squared','c0_r4')


def sector_polynomials(sector):
    assert sector in SECTORS
    if sector=='c1_squared':
        D,o,M,d0=logs.cut_polynomials(3)
        return ct.trim(D),o,ct.trim(M),d0
    a=cut.monomial_waves(2);b=cut.monomial_waves(4)
    minus=a['J0_minus']*b['J0_minus']/4;plus=a['J0_plus']*b['J0_plus']/4
    d0=(minus+plus)/2;o=(plus-minus)/2;D=[d0]+[Q()]*4;M=[Q()]*5
    for J in range(2,5):
        h=cut.mixed_cross_moment(2,J)*cut.mixed_cross_moment(4,J)
        for j,p in enumerate(logs.jacobi04(J-2)):M[j+2]+=Q(2*J+1,8)*h*p
        if J%2==0:
            e=cut.equal_cross_moment(2,J)*cut.equal_cross_moment(4,J)
            for j,p in enumerate(logs.legendre(J)):D[j]+=Q(2*J+1,4)*e*p
    return ct.trim(D),o,ct.trim(M),d0


def scalar_logs(sector):
    _,o,M,d0=sector_polynomials(sector);q=6
    L=2*sum((a/Q(q-j+1) for j,a in enumerate(M)),Q())
    K=-2*sum((a/Q((q-j+1)**2) for j,a in enumerate(M)),Q())
    out={}
    for name,sign in (('minus',-1),('plus',1)):
        right=d0+sign*o;left=L+sign*2*o/Q(q+1)
        out[name]={'right_cut':right,'crossed_log':left,'real_log':right+left,
                   'angular_constant':K-sign*2*o/Q((q+1)**2)}
    return out


def running_vector(sector):
    D,o,M,_=sector_polynomials(sector);q=6
    same=ct.scale(o,ct.add(ct.add([Q(1)],ct.poly_power([Q(),Q(1)],q)),ct.poly_power([Q(-1),Q(-1)],q)))
    poly=[Q()]*(q+1)
    for j,d in enumerate(D):
        for m in range(j+1):poly[m]+=d*comb(j,m)*2**m
    for j,a in enumerate(M):
        poly[q-j]+=a*(-1)**j
        for m in range(q-j+1):poly[m]+=a*comb(q-j,m)
    _,S,M=ct.basis_polynomials(q)
    return ct.decompose(same,S)+ct.decompose(ct.trim(poly),M)


def log_coefficients(cache,sigmas,sector,order=(0,1,2,3)):
    D,o,M,_=sector_polynomials(sector);q=6
    terms=crossed.tensor_terms(cache,order);hs=[sigmas[i] for i in order];out={}
    def add(s,a):
        key=tuple(s.encoded());out[key]=out.get(key,F())+a
    if len(set(hs))==1:
        for s,a in terms:add(s,-2*o*a*power(s,q-2))
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


def all_waves(k):
    out=cut.monomial_waves(k)
    out.update({'J3_mixed':cut.mixed_cross_moment(k,3),'J4_minus':cut.equal_cross_moment(k,4),
                'J4_plus':-cut.equal_cross_moment(k,4),'J4_mixed':cut.mixed_cross_moment(k,4)})
    return out


def coefficient6_from_square(c0,c1,r4):
    waves=[all_waves(k) for k in (2,3,4)];amplitudes={};coeffs={}
    for name in waves[0]:
        p=[Q(),Q(),c0*waves[0][name],c1*waves[1][name],r4*waves[2][name]]
        amplitudes[name]=p;coeffs[name]=ct.multiply(p,p)[6] if len(ct.multiply(p,p))>6 else Q()
        coeffs[name]/=8
    d0=(coeffs['J0_minus']+coeffs['J0_plus'])/2;o=(coeffs['J0_plus']-coeffs['J0_minus'])/2
    D=[d0]+[Q()]*4;M=[Q()]*5
    for J in range(2,5):
        for j,p in enumerate(logs.jacobi04(J-2)):M[j+2]+=Q(2*J+1,2)*coeffs['J'+str(J)+'_mixed']*p
        if J%2==0:
            for j,p in enumerate(logs.legendre(J)):D[j]+=(2*J+1)*coeffs['J'+str(J)+'_minus']*p
    return (ct.trim(D),o,ct.trim(M),d0),coeffs,amplitudes


def cancellation_data():
    a=scalar_logs('c1_squared');b=scalar_logs('c0_r4')
    am,ap=a['minus']['real_log'],a['plus']['real_log'];bm,bp=b['minus']['real_log'],b['plus']['real_log']
    return -am/bm,-ap/bp,am*bp-bm*ap


def invariant_covectors():
    a=running_vector('c1_squared');b=running_vector('c0_r4');det=a[0]*b[4]-b[0]*a[4]
    out=[]
    for i in (1,2,3):
        alpha=(a[i]*b[4]-b[i]*a[4])/det;beta=(a[0]*b[i]-b[0]*a[i])/det
        p=[Q()]*5;p[i]=Q(1);p[0]=-alpha;p[4]=-beta;out.append(p)
    return out


def validate_contract(c):
    assert c['schema']=='marici.scattering.degree6-photon-ir-logs.v1'
    assert c['scope']=='pure_g2_power4;homogeneous_degree_6;R=c0*s^2+c1*s^3+r4*s^4+...;no_added_massless_poles'
    assert c['sectors']==list(SECTORS)
    assert c['normalization']=='ImB6=s^6*(c1^2*A3_dagger*A3+c0*r4*(A2_dagger*A4+A4_dagger*A2))/8'
    assert c['running']=='d C_i/d log(nu)=-(c1^2*h33_i+c0*r4*h24_i)/pi;nu_is_squared_mass_reference'
    assert c['r4']=='independent_symbolic_input;1/(6*pi)_only_in_prior_spectral_control'
    for key in ('degree6_photon_cut_complete_for_declared_kernel','full_Bose_helicity_carrier_retained',
                'Ward_Bose_log_and_counterterm_tensors_retained','complete_three_term_square_positivity_retained',
                'scalar_cancellation_loci_classified','running_rank_two_and_three_invariants_constructed',
                'independent_finite_matching_data_retained','independent_dimensionful_couplings_retained'):
        assert c[key] is True,key
    for key in ('degree6_coefficient_must_be_positive','both_scalar_degree6_logs_cancel_for_nonzero_X_Y',
                'r4_spectral_control_source_licensed','finite_matching_selected_by_running','RG_invariant_values_source_selected',
                'three_plus_one_full_quartic_amplitude_excluded','full_order_g2_power4_cut_spectrum_constructed',
                'full_EFT_anomalous_dimension_matrix_constructed','running_of_g2_or_g3_derived','UV_completion_constructed',
                'exact_scattering_operator_constructed','native_source_licensed','physical_rates_or_branching_derived',
                'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=mixed.build();assert parent==json.loads(mixed.RESULT.read_text(encoding='utf-8')),'stale mixed photon logs'
    D,o,M,d0=sector_polynomials('c0_r4')
    assert (D,o,M,d0)==([Q(29,140),Q(),Q(1,280)],Q(-23,120),[Q(),Q(),Q(1,56)],Q(5,24))
    a=running_vector('c1_squared');b=running_vector('c0_r4')
    assert a==sum(ct.running_vectors(3),[]) and b==[Q(23,60),Q(-23,40),Q(8,35),Q(-3,35),Q(1,28)]
    rank_minor=a[0]*b[4]-a[4]*b[0];assert rank_minor==Q(-1,288)
    invariant=invariant_covectors()
    for p in invariant:
        assert sum((x*y for x,y in zip(p,a)),Q())==sum((x*y for x,y in zip(p,b)),Q())==0
    assert [[p[i] for i in (1,2,3)] for p in invariant]==[[1,0,0],[0,1,0],[0,0,1]]
    minus_zero,plus_zero,det=cancellation_data()
    assert (minus_zero,plus_zero,det)==(Q(-1115,6208),Q(35,416),Q(-473,125440))
    assert scalar_logs('c0_r4')['minus']['real_log']==Q(97,210)
    assert scalar_logs('c0_r4')['plus']['real_log']==Q(-13,420)
    assert scalar_logs('c1_squared')==logs.scalar_logs(3)
    _,S,B=ct.basis_polynomials(6);moments=[ct.scalar_projection(p) for p in S+B]
    projections=0
    for sector in SECTORS:
        h=running_vector(sector);D,o,M,d0=sector_polynomials(sector)
        for name,sign in (('minus',-1),('plus',1)):
            avg=sum((x*y for x,y in zip(h[2:],moments[2:])),Q())+sign*sum((x*y for x,y in zip(h[:2],moments[:2])),Q())
            assert avg==scalar_logs(sector)[name]['real_log'];projections+=1
        for J in range(2,5):
            p=logs.jacobi04(J-2)
            ordered=sum((x*y/Q(i+j+3) for i,x in enumerate(M) for j,y in enumerate(p)),Q())
            expected=cut.mixed_cross_moment(3,J)**2/8 if sector=='c1_squared' else cut.mixed_cross_moment(2,J)*cut.mixed_cross_moment(4,J)/4
            assert 2*ordered==expected;projections+=1
    coefficient_checks=0;positivity=0;angular_checks=0
    parameters=((Q(1),Q(1),Q(1)),(Q(1),Q(-2),Q(-1)),(Q(),Q(1),Q()),(Q(1),Q(),Q(1)),
                (minus_zero,Q(1),Q(1)),(plus_zero,Q(1),Q(1)),(Q(),Q(),Q(1)))
    for c0,c1,r4 in parameters:
        X,Y=c1*c1,c0*r4;polys,waves,amps=coefficient6_from_square(c0,c1,r4)
        p33=sector_polynomials('c1_squared');p24=sector_polynomials('c0_r4')
        expected=(ct.add(ct.scale(X,p33[0]),ct.scale(Y,p24[0])),X*p33[1]+Y*p24[1],
                  ct.add(ct.scale(X,p33[2]),ct.scale(Y,p24[2])),X*p33[3]+Y*p24[3])
        assert polys==expected;angular_checks+=1
        w2,w3,w4=[all_waves(k) for k in (2,3,4)]
        for name,value in waves.items():
            assert value==X*w3[name]**2/8+Y*w2[name]*w4[name]/4;coefficient_checks+=1
            for s in (Q(1,4),Q(1,2),Q(1)):
                full=logs.evaluate(ct.multiply(amps[name],amps[name]),s)/8
                assert full==logs.evaluate(amps[name],s)**2/8 and full>=0;positivity+=1
    # The degree-six coefficient itself can be negative even at a real-log cancellation locus.
    assert scalar_logs('c1_squared')['minus']['right_cut']+minus_zero*scalar_logs('c0_r4')['minus']['right_cut']==Q(-19,12416)
    assert scalar_logs('c1_squared')['plus']['right_cut']+plus_zero*scalar_logs('c0_r4')['plus']['right_cut']==Q(23,2496)
    physical=0;permuted=0;ward=0;lorentz=0;cancellations=0
    labels=((1,1),(-1,-1),(1,-1),(-1,1));packet=crossed.packet
    L=packet.boost(packet.velocity([F(Q(1,8)),F(Q(1,6)),F()]))
    for index,(cosine,sine,E) in enumerate(((Q(3,5),Q(4,5),Q(1,2)),(Q(),Q(1),Q(1,3)),(Q(1),Q(),Q(1,2)))):
        ks=crossed.kinematics(cosine,sine,E);s=F(4*E*E);x=F((1+cosine)/2);key=tuple(s.encoded())
        for inc in labels:
            for out in labels:
                helicities=inc+out;sigmas=(inc[0],inc[1],-out[0],-out[1]);es=crossed.polarizations(helicities,cosine,sine)
                cache=crossed.tensor_cache(ks,es);O=ct.basis_tensors(cache,sigmas,6);Hs=[]
                for sector in SECTORS:
                    D,o,M,_=sector_polynomials(sector);coeffs=log_coefficients(cache,sigmas,sector)
                    if sector=='c1_squared':assert coeffs==logs.log_coefficients(cache,sigmas,3)
                    d=logs.evaluate(D,F(cosine));mx=logs.evaluate(M,x);mr=logs.evaluate(M,1-x)
                    matrix=[[d,F(o),F(),F()],[F(o),d,F(),F()],[F(),F(),mx,mr],[F(),F(),mr,mx]]
                    assert coeffs.get(key,F())==power(s,6)*matrix[labels.index(out)][labels.index(inc)];physical+=1
                    H=sum(coeffs.values(),F());h=running_vector(sector)
                    assert H==sum((u*v for u,v in zip(h,O)),F());Hs.append(H)
                    if index==0:
                        for order in permutations(range(4)):
                            assert log_coefficients(cache,sigmas,sector,order)==coeffs and ct.basis_tensors(cache,sigmas,6,order)==O;permuted+=1
                    if index==0 and helicities in ((1,1,1,1),(1,1,-1,-1)):
                        for leg in range(4):
                            changed=es.copy();changed[leg]=ks[leg];altered=crossed.tensor_cache(ks,changed)
                            assert log_coefficients(altered,sigmas,sector)=={} and ct.basis_tensors(altered,sigmas,6)==[F()]*5;ward+=1
                        boosted=crossed.tensor_cache([packet.act(L,p) for p in ks],[packet.act(L,e) for e in es])
                        assert log_coefficients(boosted,sigmas,sector)==coeffs and ct.basis_tensors(boosted,sigmas,6)==O;lorentz+=1
                for X,Y in ((Q(),Q(1)),(Q(1),Q(-1)),(Q(1),minus_zero),(Q(1),plus_zero)):
                    h=[X*u+Y*v for u,v in zip(a,b)];H=X*Hs[0]+Y*Hs[1]
                    for ell in (Q(-2),Q(1,3),Q(3,2)):
                        assert ell*H+sum((-ell*u*v for u,v in zip(h,O)),F())==F();cancellations+=1
    refused=[]
    for name in ('degree6_coefficient_must_be_positive','both_scalar_degree6_logs_cancel_for_nonzero_X_Y',
                 'r4_spectral_control_source_licensed','finite_matching_selected_by_running','RG_invariant_values_source_selected',
                 'three_plus_one_full_quartic_amplitude_excluded','full_EFT_anomalous_dimension_matrix_constructed','exact_scattering_operator_constructed'):
        try:
            bad=copy.deepcopy(c);bad[name]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported degree-six promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((mixed.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_degree6_photon_ir_logs.py'))
    return {'schema':'marici.scattering.degree6-photon-ir-logs-receipt.v1','status':'pass',
        'scope_verdict':'complete_degree_6_photon_logs_for_declared_R_not_full_quartic_spectrum_or_source_matching',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'sector_data':{sector:{'D':[str(a) for a in sector_polynomials(sector)[0]],'O':str(sector_polynomials(sector)[1]),
            'M':[str(a) for a in sector_polynomials(sector)[2]],'h':[str(a) for a in running_vector(sector)],
            'scalar_logs':{n:{key:str(v) for key,v in row.items()} for n,row in scalar_logs(sector).items()}} for sector in SECTORS},
        'scalar_zero_Y_over_X':{'minus':str(minus_zero),'plus':str(plus_zero)},'scalar_log_matrix_determinant':str(det),
        'running_rank':2,'running_rank_minor':str(rank_minor),'RG_invariant_covectors':[[str(x) for x in p] for p in invariant],
        'local_basis_dimension':5,'operator_dimension':16,'scalar_and_mixed_projection_checks':projections,
        'formal_wave_coefficient_extraction_checks':coefficient_checks,'angular_coefficient_extraction_checks':angular_checks,
        'complete_wave_square_positivity_checks':positivity,'physical_right_cut_coefficient_checks':physical,
        'log_and_counterterm_permutation_checks':permuted,'Ward_tensor_checks':ward,'Lorentz_tensor_checks':lorentz,
        'combined_finite_scale_cancellation_checks':cancellations,'general_tensor_and_log_arguments_machine_formalized':False,
        **{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale degree-six photon logs'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','physical_right_cut_coefficient_checks','running_rank',
        'both_scalar_degree6_logs_cancel_for_nonzero_X_Y','finite_matching_selected_by_running','hostile_controls_refused')}))


if __name__=='__main__':main()
