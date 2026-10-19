"""Positive coherent forward photon cut moments; IR subtraction is not positive."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from math import comb,factorial
from pathlib import Path
import check_windowed_photon_dispersion as win

ir=win.ir;ct=ir.ct;ROOT=ir.ROOT;HOME=ir.HOME
CONTRACT=HOME/'contracts/forward-photon-moments.v1.json';PROOF=HOME/'FORWARD-PHOTON-MOMENTS.md'
RESULT=HOME/'results/forward-photon-moments.v1.json'
NAMES=('minus','plus','mixed')


def pair_eigenvalues(k,l):
    assert isinstance(k,int) and isinstance(l,int) and k>=2 and l>=2
    q=k+l;beta=Q(factorial(k)*factorial(l),factorial(q+1))
    plus=Q((-1)**q,16)*(Q(1,q+1)+beta)
    minus=plus+(1+Q((-1)**k,k+1)+Q((-1)**l,l+1))/8
    return minus,plus,Q((-1)**q,16*(q+1))


def eigen_polynomials(r):
    assert r and all(isinstance(k,int) and k>=2 for k in r)
    out=[{} for _ in NAMES]
    for k,a in r.items():
        for l,b in r.items():
            for p,c in zip(out,pair_eigenvalues(k,l)):p[k+l]=p.get(k+l,Q())+a*b*c
    return [{q:a for q,a in p.items() if a} for p in out]


def evaluate(p,s):return sum((a*s**q for q,a in p.items()),Q())


def moment(p,n,tau,remove_through=None):
    assert isinstance(n,int) and n>=0 and 0<tau<1
    selected={q:a for q,a in p.items() if remove_through is None or q>remove_through}
    assert all(q>n for q in selected),'IR divergent moment; declare any density subtraction explicitly'
    return sum((a*tau**(q-n)/Q(q-n) for q,a in selected.items()),Q())


def integrate(p):return sum((a/Q(j+1) for j,a in enumerate(p)),Q())


def angular_gram(r,s):
    """Independent integral of squared ordered Born blocks, including azimuth twirl."""
    rs=sum((a*s**k for k,a in r.items()),Q());rt=[Q()]*(max(r)+1);ru=rt.copy()
    for k,a in r.items():
        rt[k]+=a*s**k*(-1)**k
        for j in range(k+1):ru[j]+=a*s**k*(-1)**(k+j)*comb(k,j)
    v=ct.scale(Q(1,2),ct.add(rt,ru))
    plus=integrate(ct.multiply(v,v))/8
    u=ct.add(v,[rs]);minus=integrate(ct.multiply(u,u))/8
    mixed=integrate(ct.add(ct.multiply(rt,rt),ct.multiply(ru,ru)))/32
    untwirled_off=integrate(ct.multiply(rt,ru))/16
    return (minus,plus,mixed),untwirled_off


def matrix(eigen):
    minus,plus,mixed=eigen;D=(minus+plus)/2;O=(plus-minus)/2
    return [[D,O,Q(),Q()],[O,D,Q(),Q()],[Q(),Q(),mixed,Q()],[Q(),Q(),Q(),mixed]]


def twirl(a):
    m=(0,0,2,-2)
    return [[v if m[i]==m[j] else Q() for j,v in enumerate(row)] for i,row in enumerate(a)]


def coherent(eigen,z):
    """Normalized expectation, complex amplitudes encoded as rational (real,imag)."""
    assert len(z)==4
    norm=sum((a*a+b*b for a,b in z),Q());assert norm>0
    a=matrix(eigen)
    value=sum((a[i][j]*(z[i][0]*z[j][0]+z[i][1]*z[j][1]) for i in range(4) for j in range(4)),Q())/norm
    minus,plus,mixed=eigen
    square=lambda sign:sum((z[0][j]+sign*z[1][j])**2 for j in (0,1))
    diagonal=(minus*square(-1)/2+plus*square(1)/2+mixed*sum((x*x+y*y for x,y in z[2:]),Q()))/norm
    assert value==diagonal
    return value


def spectral_coefficients(K):
    assert isinstance(K,int) and K>=4
    return {k:ir.response.coefficient(k-4) for k in range(4,K+1)}  # pi*r_k


def spectral_moment_error(K,n,tau):
    """Operator-norm error for pi^2 moments, c0=c1=0; also after a shared leading subtraction."""
    tau=Q(tau);assert isinstance(K,int) and K>=4 and isinstance(n,int) and 0<=n<K+5 and 0<tau<1
    return ir.response.coefficient(K-3)*tau**(K+5-n)/(6*(1-tau/4)**2*(K+5-n))


def rational_box(center,error,den=10**20):
    lo=center-error;hi=center+error
    return [str(Q((lo*den).__floor__(),den)),str(Q((hi*den).__ceil__(),den))]


def validate_contract(c):
    assert c['schema']=='marici.scattering.forward-photon-moments.v1'
    assert c['scope']=='pure_g2_power4;physical_forward_photon_cut;conditional_response'
    assert c['helicity_order']==['++','--','+-','-+']
    assert c['moment']=='M_n(tau)=integral_0^tau F(s)*s^(-n-1) ds;F=Im B(s,forward)'
    assert c['IR_condition']=='n<2*k0;k0=first_nonzero_response_degree'
    for key in ('coherent_forward_moment_matrix_constructed','positive_unsubtracted_moments_established',
                'azimuth_twirl_retained','PSD_preserving_response_truncation_constructed',
                'spectral_comparison_operator_error_certified','IR_subtracted_indefinite_counterexample_constructed',
                'independent_dimensionful_couplings_retained'):
        assert c[key] is True,key
    for key in ('polarization_coherence_may_be_discarded','IR_subtracted_moments_automatically_positive',
                'amplitude_remainder_square_equals_cut_difference','moments_are_prescribed_window_Taylor_coefficients',
                'global_dispersion_growth_assumptions_source_licensed','finite_matching_fixed_or_bounded',
                'UV_fixed_order_spectral_positivity_derived',
                'positive_right_cut_is_full_crossed_dispersion_positivity','spectral_control_source_licensed',
                'physical_preparation_selected','physical_rates_or_branching_derived','UV_completion_constructed',
                'exact_scattering_operator_constructed','live_proposition_inventory_changed','C12_protocol_renewed',
                'high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=win.build();assert parent==json.loads(win.RESULT.read_text(encoding='utf-8')),'stale window representative'
    pairs=0;grams=0;polarizations=0;tau=Q(1,2)
    for k in range(2,9):
        for l in range(2,9):
            D,o,M,_=ir.pair_polynomials(k,l)
            assert pair_eigenvalues(k,l)==(sum(D)-o,sum(D)+o,sum(M));pairs+=1
    assert pair_eigenvalues(2,2)==(Q(107,480),Q(7,480),Q(1,80))
    assert pair_eigenvalues(3,3)==(Q(23,320),Q(3,320),Q(1,112))
    vectors=(((1,0),(1,0),(0,0),(0,0)),((1,0),(-1,0),(0,0),(0,0)),
             ((1,0),(0,1),(0,0),(0,0)),((Q(1,3),Q(2,5)),(Q(-1,2),Q(1,7)),(1,0),(0,1)))
    controls=({2:Q(1)},{2:Q(1),3:Q(1)},{2:Q(-2),3:Q(3),4:Q(-1)},spectral_coefficients(8))
    for r in controls:
        polys=eigen_polynomials(r)
        for s in (Q(1,8),Q(1,3),tau):
            values=tuple(evaluate(p,s) for p in polys);direct,off=angular_gram(r,s)
            assert values==direct and min(values)>0;grams+=1
            raw=matrix(values);raw[2][3]=raw[3][2]=off
            assert twirl(raw)==matrix(values)
            for z in vectors:
                value=coherent(values,z);assert min(values)<=value<=max(values);polarizations+=1
        for n in (2,3):assert all(moment(p,n,tau)>0 for p in polys)
    assert angular_gram({2:Q(1)},Q(1))[1]!=0  # omitting the twirl gives a wrong mixed forward entry
    leading={}
    for k in (2,3,4):
        eig=pair_eigenvalues(k,k);assert min(eig)>0
        p={2*k:Q(1)};assert moment(p,2*k-1,tau)==tau
        try:moment(p,2*k,tau)
        except AssertionError:pass
        else:raise AssertionError('IR divergent moment admitted')
        leading[str(k)]={'largest_finite_integer_n':2*k-1,'leading_eigenvalues':list(map(str,eig))}
    # Exact finite two-monomial control: subtraction destroys positivity.
    polys=eigen_polynomials({2:Q(1),3:Q(1)})
    sub=tuple(moment(p,4,tau,remove_through=4) for p in polys)
    assert sub[0]>0 and sub[1:]==(Q(-79,7680),Q(-25,2688))
    # Same failure in the infinite conditional spectral family, not just the polynomial control.
    K=16;polys=eigen_polynomials(spectral_coefficients(K));boxes={}
    for n in (2,3,8):
        error=spectral_moment_error(K,n,tau)
        values=[moment(p,n,tau,remove_through=8 if n==8 else None) for p in polys]
        boxes[str(n)]={name:rational_box(v,error) for name,v in zip(NAMES,values)}
        if n in (2,3):assert all(Q(box[0])>0 for box in boxes[str(n)].values()) and error<Q(3,10**18)
        else:assert Q(boxes['8']['plus'][1])<0 and Q(boxes['8']['mixed'][1])<0
    bell=pair_eigenvalues(2,2);mixture=(bell[0]+bell[1])/2
    assert coherent(bell,vectors[0])==bell[1] and coherent(bell,vectors[1])==bell[0]
    assert bell[1]<mixture<bell[0] and coherent(bell,vectors[2])==mixture
    refused=[]
    for name in ('polarization_coherence_may_be_discarded','IR_subtracted_moments_automatically_positive',
                 'amplitude_remainder_square_equals_cut_difference','moments_are_prescribed_window_Taylor_coefficients',
                 'global_dispersion_growth_assumptions_source_licensed','finite_matching_fixed_or_bounded',
                 'positive_right_cut_is_full_crossed_dispersion_positivity','UV_fixed_order_spectral_positivity_derived'):
        try:
            bad=copy.deepcopy(c);bad[name]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported forward positivity promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((win.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_forward_photon_moments.py'))
    return {'schema':'marici.scattering.forward-photon-moments-receipt.v1','status':'pass',
        'scope_verdict':'positive_coherent_forward_cut_moments_not_UV_matching_bounds',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'closed_forward_pair_checks':pairs,'independent_angular_Gram_and_twirl_checks':grams,
        'complex_coherent_polarization_checks':polarizations,'IR_threshold_controls':leading,
        'two_monomial_IR_subtracted_eigenvalues':list(map(str,sub)),
        'spectral_comparison':{'c0':'0','c1':'0','tau':'1/2','response_degree_K':K,'normalization':'pi^2 times cut moment',
            'eigenvalue_boxes':boxes,'n8_subtraction':'remove exactly the leading degree-eight cut density',
            'operator_error_bounds':{str(n):str(spectral_moment_error(K,n,tau)) for n in (2,3,8)}},
        'general_Gram_positivity_and_operator_error_argument_machine_formalized':False,
        **{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale forward photon moments'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','closed_forward_pair_checks','independent_angular_Gram_and_twirl_checks',
        'IR_subtracted_indefinite_counterexample_constructed','finite_matching_fixed_or_bounded','hostile_controls_refused')}))


if __name__=='__main__':main()
