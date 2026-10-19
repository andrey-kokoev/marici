"""Mixed c0*c1 degree-five photon cuts, crossed logs and local scale mixing."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
from itertools import permutations
import json
from math import comb
from pathlib import Path
import check_photon_counterterm_running as ct

logs=ct.logs;cut=logs.cut;crossed=ct.crossed;F=ct.F;phase=ct.phase;power=ct.power
ROOT=ct.ROOT;HOME=ct.HOME
CONTRACT=HOME/'contracts/mixed-photon-ir-logs.v1.json';PROOF=HOME/'MIXED-PHOTON-IR-LOGS.md'
RESULT=HOME/'results/mixed-photon-ir-logs.v1.json'


def cut_polynomials():
    a=cut.monomial_waves(2);b=cut.monomial_waves(3)
    minus=a['J0_minus']*b['J0_minus']/4;plus=a['J0_plus']*b['J0_plus']/4
    d0=(minus+plus)/2;o=(plus-minus)/2
    D=[d0,Q(),Q()];M=[Q(),Q(),Q(),Q()]
    for J in (2,3):
        h=cut.mixed_cross_moment(2,J)*cut.mixed_cross_moment(3,J)
        for j,p in enumerate(logs.jacobi04(J-2)):M[j+2]+=Q(2*J+1,8)*h*p
        if J%2==0:
            e=cut.equal_cross_moment(2,J)*cut.equal_cross_moment(3,J)
            for j,p in enumerate(logs.legendre(J)):D[j]+=Q(2*J+1,4)*e*p
    return ct.trim(D),o,ct.trim(M),d0


def combined_cut_polynomials(c0,c1,s):
    """Independently square the two-term leading amplitude, retaining the Bose carrier."""
    c0=Q(c0)*s**2;c1=Q(c1)*s**3
    a=cut.monomial_waves(2);b=cut.monomial_waves(3)
    minus=c0*a['J0_minus']+c1*b['J0_minus'];plus=c0*a['J0_plus']+c1*b['J0_plus']
    D=[(minus*minus+plus*plus)/16,Q(),Q()];o=(plus*plus-minus*minus)/16;M=[Q()]*4
    for J in (2,3):
        h=c0*cut.mixed_cross_moment(2,J)+c1*cut.mixed_cross_moment(3,J)
        for j,p in enumerate(logs.jacobi04(J-2)):M[j+2]+=Q(2*J+1,16)*h*h*p
        if J%2==0:
            e=c0*cut.equal_cross_moment(2,J)+c1*cut.equal_cross_moment(3,J)
            for j,p in enumerate(logs.legendre(J)):D[j]+=Q(2*J+1,8)*e*e*p
    return ct.trim(D),o,ct.trim(M)


def log_coefficients(cache,sigmas,order=(0,1,2,3)):
    D,o,M,_=cut_polynomials();q=5
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


def scalar_logs():
    _,o,M,d0=cut_polynomials();q=5
    L=2*(-1)**q*sum((a/Q(q-j+1) for j,a in enumerate(M)),Q())
    K=-2*(-1)**q*sum((a/Q((q-j+1)**2) for j,a in enumerate(M)),Q())
    out={}
    for name,sign in (('minus',-1),('plus',1)):
        right=d0+sign*o;left=L+sign*2*(-1)**q*o/Q(q+1)
        out[name]={'right_cut':right,'crossed_log':left,'real_log':right+left,
                   'angular_constant':K-sign*2*(-1)**q*o/Q((q+1)**2)}
    return out


def basis_polynomials():
    e2=[Q(-1),Q(-1),Q(-1)];e3=[Q(),Q(-1),Q(-1)]
    return [ct.multiply(e2,e3)],[ [Q(1)],e3 ]


def running_vector():
    D,o,M,_=cut_polynomials();q=5
    same=ct.scale(o,ct.add(ct.add([Q(1)],ct.poly_power([Q(),Q(1)],q)),ct.poly_power([Q(-1),Q(-1)],q)))
    mixed=[Q()]*(q+1)
    for j,d in enumerate(D):
        for m in range(j+1):mixed[m]+=d*comb(j,m)*2**m
    for j,a in enumerate(M):
        mixed[q-j]+=a*(-1)**j
        for m in range(q-j+1):mixed[m]+=a*(-1)**q*comb(q-j,m)
    S,M=basis_polynomials()
    return ct.decompose(same,S)+ct.decompose(ct.trim(mixed),M)


def basis_tensors(cache,sigmas,order=(0,1,2,3)):
    terms=crossed.tensor_terms(cache,order);hs=[sigmas[i] for i in order];out=[F()]*3
    if len(set(hs))==1:
        # p5=-5*e2*e3; A5=-4*sum W_S*S^3, with cached a=2*W_S.
        out[0]=F(Q(2,5))*sum((a*power(s,3) for s,a in terms),F())
    elif hs.count(1)==2:
        for index,(i,j,l,m) in enumerate(crossed.PAIRINGS):
            if hs[i]!=hs[j] or hs[l]!=hs[m]:continue
            s,a=terms[index];t,u=[terms[n][0] for n in range(3) if n!=index]
            out[1]=2*a*power(s,3);out[2]=2*a*s*t*u
            break
    return out


def validate_contract(c):
    assert c['schema']=='marici.scattering.mixed-photon-ir-logs.v1'
    assert c['scope']=='pure_g2_power4;c0_c1_interference_only;homogeneous_degree_5;no_added_massless_poles'
    assert c['normalization']=='ImB_23=c0*c1*s^5*(A2_dagger*A3+A3_dagger*A2)/8'
    assert c['running']=='d C_i/d log(nu)=-(c0*c1/pi)*h_i;nu_is_squared_mass_reference'
    assert c['basis']==['P_all*e2*e3','P_mixed*S^5','P_mixed*S^3*T*U']
    for key in ('interference_cut_constructed','full_Bose_helicity_carrier_retained','odd_degree_crossing_sign_retained',
                'Ward_Bose_log_and_counterterm_tensors_retained','complete_two_term_square_positivity_retained',
                'finite_local_matching_independent_of_c0_c1_retained','independent_dimensionful_couplings_retained'):
        assert c[key] is True,key
    for key in ('interference_cut_coefficient_must_be_positive','mixed_real_scalar_logs_cancel_completely',
                'finite_matching_selected_by_running','three_plus_one_full_quartic_amplitude_excluded',
                'full_degree_6_cut_constructed','full_order_g2_power4_cut_spectrum_constructed',
                'full_EFT_anomalous_dimension_matrix_constructed','running_of_g2_or_g3_derived','UV_completion_constructed',
                'exact_scattering_operator_constructed','native_source_licensed','physical_rates_or_branching_derived',
                'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=ct.build();assert parent==json.loads(ct.RESULT.read_text(encoding='utf-8')),'stale counterterm running'
    D,o,M,d0=cut_polynomials();assert D==[Q(37,320),Q(),Q(-1,320)] and o==Q(-13,96) and M==[Q(),Q(),Q(-1,48)]
    scalar=scalar_logs();assert [scalar[n]['right_cut'] for n in ('minus','plus')]==[Q(1,4),Q(-1,48)]
    assert [scalar[n]['real_log'] for n in ('minus','plus')]==[Q(31,144),Q(5,144)]
    h=running_vector();assert h==[Q(65,96),Q(2,15),Q(-1,20)]
    S,B=basis_polynomials();moments=[ct.scalar_projection(p) for p in S+B]
    assert moments==[Q(-2,15),Q(1),Q(1,6)]
    for name,sign in (('minus',-1),('plus',1)):
        assert h[1]*moments[1]+h[2]*moments[2]+sign*h[0]*moments[0]==scalar[name]['real_log']
    projections=0
    for J in (2,3):
        jac=logs.jacobi04(J-2)
        ordered=sum((a*b/Q(i+j+3) for i,a in enumerate(M) for j,b in enumerate(jac)),Q())
        assert 2*ordered==cut.mixed_cross_moment(2,J)*cut.mixed_cross_moment(3,J)/4;projections+=1
    # D is a polynomial in z: integral z^j dz/2 is zero at odd j, 1/(j+1) at even j.
    avg=sum((a/Q(i+1) for i,a in enumerate(D) if i%2==0),Q());assert avg==d0
    for name,sign in (('minus',-1),('plus',1)):
        assert avg+sign*o==scalar[name]['right_cut'];projections+=1
    P2=logs.legendre(2)
    moment=sum((a*b/Q(i+j+1) for i,a in enumerate(D) for j,b in enumerate(P2) if (i+j)%2==0),Q())
    assert moment==cut.equal_cross_moment(2,2)*cut.equal_cross_moment(3,2)/4;projections+=1
    square_checks=0;positivity=0
    a=cut.monomial_waves(2);b=cut.monomial_waves(3)
    for c0,c1 in ((Q(1),Q(1)),(Q(1),Q(-2)),(Q(),Q(1)),(Q(-2),Q(-1)),(Q(),Q()),(Q(3),Q(4))):
        for s in (Q(1,3),Q(1,2),Q(1)):
            direct=combined_cut_polynomials(c0,c1,s);d2,o2,m2,_=logs.cut_polynomials(2);d3,o3,m3,_=logs.cut_polynomials(3)
            expected=(ct.add(ct.add(ct.scale(c0*c0*s**4,d2),ct.scale(c0*c1*s**5,D)),ct.scale(c1*c1*s**6,d3)),
                c0*c0*s**4*o2+c0*c1*s**5*o+c1*c1*s**6*o3,
                ct.add(ct.add(ct.scale(c0*c0*s**4,m2),ct.scale(c0*c1*s**5,M)),ct.scale(c1*c1*s**6,m3)))
            assert direct==expected;square_checks+=1
            for name in cut.WAVES:
                norm=(c0*s*s*a[name]+c1*s**3*b[name])**2/8
                expanded=c0*c0*s**4*a[name]**2/8+c0*c1*s**5*a[name]*b[name]/4+c1*c1*s**6*b[name]**2/8
                assert norm==expanded and norm>=0;positivity+=1
            h3=c1*s**3*cut.mixed_cross_moment(3,3);assert h3*h3/8>=0;positivity+=1
    assert 3*a['J0_plus']+4*b['J0_plus']==0  # coherent cancellation, not a source matching choice
    physical=0;permuted=0;ward=0;lorentz=0;cancellations=0;basis_normalizations=0
    labels=((1,1),(-1,-1),(1,-1),(-1,1));packet=crossed.packet
    L=packet.boost(packet.velocity([F(Q(1,8)),F(Q(1,6)),F()]))
    for index,(cosine,sine,E) in enumerate(((Q(3,5),Q(4,5),Q(1,2)),(Q(),Q(1),Q(1,3)),(Q(1),Q(),Q(1,2)))):
        ks=crossed.kinematics(cosine,sine,E);s=F(4*E*E);x=F((1+cosine)/2);key=tuple(s.encoded())
        for inc in labels:
            for out in labels:
                helicities=inc+out;sigmas=(inc[0],inc[1],-out[0],-out[1]);es=crossed.polarizations(helicities,cosine,sine)
                cache=crossed.tensor_cache(ks,es);coeffs=log_coefficients(cache,sigmas);O=basis_tensors(cache,sigmas)
                d=logs.evaluate(D,F(cosine));mx=logs.evaluate(M,x);mr=logs.evaluate(M,1-x)
                matrix=[[d,F(o),F(),F()],[F(o),d,F(),F()],[F(),F(),mx,mr],[F(),F(),mr,mx]]
                assert coeffs.get(key,F())==power(s,5)*matrix[labels.index(out)][labels.index(inc)];physical+=1
                H=sum(coeffs.values(),F());assert H==sum((a*b for a,b in zip(h,O)),F())
                for ell in (Q(-2),Q(1,3),Q(3,2)):
                    assert ell*H+sum((-ell*a*b for a,b in zip(h,O)),F())==F();cancellations+=1
                if helicities in ((1,1,1,1),(1,1,-1,-1)):
                    y=F(-(1-cosine)/2)
                    expected=[F()]+[power(s,5)*logs.evaluate(p,y) for p in B] if helicities==(1,1,1,1) else [power(s,5)*logs.evaluate(S[0],y),F(),F()]
                    assert O==expected;basis_normalizations+=1
                if index==0:
                    for order in permutations(range(4)):
                        assert log_coefficients(cache,sigmas,order)==coeffs and basis_tensors(cache,sigmas,order)==O;permuted+=1
                if index==0 and helicities in ((1,1,1,1),(1,1,-1,-1)):
                    for leg in range(4):
                        changed=es.copy();changed[leg]=ks[leg];altered=crossed.tensor_cache(ks,changed)
                        assert log_coefficients(altered,sigmas)=={} and basis_tensors(altered,sigmas)==[F()]*3;ward+=1
                    boosted=crossed.tensor_cache([packet.act(L,p) for p in ks],[packet.act(L,e) for e in es])
                    assert log_coefficients(boosted,sigmas)==coeffs and basis_tensors(boosted,sigmas)==O;lorentz+=1
    refused=[]
    for name in ('interference_cut_coefficient_must_be_positive','mixed_real_scalar_logs_cancel_completely',
                 'finite_matching_selected_by_running','three_plus_one_full_quartic_amplitude_excluded',
                 'full_degree_6_cut_constructed','full_order_g2_power4_cut_spectrum_constructed',
                 'full_EFT_anomalous_dimension_matrix_constructed','exact_scattering_operator_constructed'):
        try:
            bad=copy.deepcopy(c);bad[name]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported mixed-cut promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((ct.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_mixed_photon_ir_logs.py'))
    return {'schema':'marici.scattering.mixed-photon-ir-logs-receipt.v1','status':'pass',
        'scope_verdict':'degree_5_c0_c1_interference_logs_and_local_scale_mixing_not_full_quartic_spectrum',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'D':[str(a) for a in D],'O':str(o),'M':[str(a) for a in M],
        'scalar_logs':{n:{key:str(value) for key,value in row.items()} for n,row in scalar.items()},
        'counterterm_h':[str(a) for a in h],'beta_coefficient_of_c0_c1_over_pi':[str(-a) for a in h],
        'operator_dimension':14,'basis_dimension':3,'Bose_projection_checks':projections,
        'two_term_cut_polynomial_square_checks':square_checks,'Bose_wave_square_positivity_checks':positivity,
        'physical_right_cut_coefficient_checks':physical,'log_and_counterterm_permutation_checks':permuted,
        'Ward_log_and_counterterm_checks':ward,'Lorentz_log_and_counterterm_checks':lorentz,
        'physical_basis_normalization_checks':basis_normalizations,'finite_scale_tensor_cancellation_checks':cancellations,
        'general_log_and_invariant_ring_argument_machine_formalized':False,
        **{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale mixed photon IR logs'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','physical_right_cut_coefficient_checks','log_and_counterterm_permutation_checks',
        'mixed_real_scalar_logs_cancel_completely','finite_matching_selected_by_running','hostile_controls_refused')}))


if __name__=='__main__':main()
