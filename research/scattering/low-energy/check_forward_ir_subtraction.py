"""Crossing-paired forward IR subtraction and analytic window transport."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from pathlib import Path
import check_forward_crossing_positivity as cross

mom=cross.mom;ir=mom.ir;win=mom.win;ROOT=ir.ROOT;HOME=ir.HOME
CONTRACT=HOME/'contracts/forward-ir-subtraction.v1.json';PROOF=HOME/'FORWARD-IR-SUBTRACTION.md'
RESULT=HOME/'results/forward-ir-subtraction.v1.json'


def zero():return [[Q() for _ in range(4)] for _ in range(4)]
def clean(form):return {key:A for key,A in form.items() if key!=Q(1) and A!=zero()}
def add_form(a,b):
    out=a.copy()
    for key,A in b.items():out[key]=cross.add(out.get(key,zero()),A)
    return clean(out)
def scale_form(c,a):return clean({key:cross.scale(c,A) for key,A in a.items()})
def log_form(A,b,a):return add_form({Q(b):A},{Q(a):cross.scale(-1,A)})


def coefficients(r):
    polys=mom.eigen_polynomials(r)
    return {q:mom.matrix([p.get(q,Q()) for p in polys]) for q in sorted(set().union(*polys))}


def shell(coeff,n,a,b,paired=True):
    """Unnormalized shell S=pi*W; None means constant, positive rational keys mean log(key)."""
    assert isinstance(n,int) and n>=2 and 0<a<1 and 0<b<1
    out={}
    for q,A in coeff.items():
        C=cross.crossed_sum(A,n) if paired else A
        if q==n:out=add_form(out,log_form(C,b,a))
        else:out=add_form(out,{None:cross.scale((b**(q-n)-a**(q-n))/Q(q-n),C)})
    return out


def analytic_coefficient(coeff,n,tau,nu):
    """Coefficient of z^n in pi*(D_tau-B_log,nu); finite also at logarithmic degrees."""
    assert isinstance(n,int) and n>=2 and 0<tau<1 and nu>0
    out={}
    for q,A in coeff.items():
        C=cross.crossed_sum(A,n)
        if q==n:out=add_form(out,log_form(C,tau,nu))
        else:out=add_form(out,{None:cross.scale(tau**(q-n)/Q(q-n),C)})
    return out


def expanded_remainder(coeff,N,tau,nu):
    """Independent expansion of the division polynomial and two analytic logarithms."""
    out={n:{} for n in range(2,N+1)}
    for q,A in coeff.items():
        for n in range(2,min(q,N+1)):
            C=cross.crossed_sum(A,n)
            out[n]=add_form(out[n],{None:cross.scale(tau**(q-n)/Q(q-n),C)})
        if q<=N:out[q]=add_form(out[q],log_form(cross.crossed_sum(A,q),tau,nu))
        for m in range(1,N-q+1):
            n=q+m;C=cross.crossed_sum(A,n)
            out[n]=add_form(out[n],{None:cross.scale(-1/(Q(m)*tau**m),C)})
    return out


def polynomial_part(coeff,z,tau):
    out=zero()
    for q,A in coeff.items():
        for n in range(2,q):out=cross.add(out,cross.scale(tau**(q-n)*z**n/Q(q-n),cross.crossed_sum(A,n)))
    return out


def residue_from_Cauchy(coeff,z,tau):
    # I_tau(-z) is on the LOWER rim when z is on the upper rim.
    right=win.rim_window_log(z,tau)[2];left=-win.rim_window_log(-z,tau)[2];out=zero()
    for q,A in coeff.items():
        out=cross.add(out,cross.scale(z**q*right,A))
        out=cross.add(out,cross.scale((-z)**q*left,cross.gamma(A)))
    return out


def form_box(form,z):
    norm=cross.rational(sum((a.conjugate()*a for a in z),Q()));assert norm>0
    lo=hi=Q()
    for key,A in form.items():
        c=cross.rational(cross.expectation(A,z))/norm
        a,b=(Q(1),Q(1)) if key is None else win.positive_log_box(key,64)
        x,y=c*a,c*b;lo+=min(x,y);hi+=max(x,y)
    return lo,hi


def rounded_box(lo,hi,error=Q(),den=10**20):
    return [str(Q(((lo-error)*den).__floor__(),den)),str(Q(((hi+error)*den).__ceil__(),den))]


def remainder_tail(Qmax,tau,a,c0=Q(),c1=Q()):
    """Operator-norm bound for generated analytic E, nu=tau; not unknown matching."""
    return 2*win.analytic_tail(Qmax,tau,a,c0,c1)


def improved_dispersion_gate(n,N,assumptions):
    # No n<2*k0 condition: the WHOLE retained IR cut, not a density power, was removed.
    assert isinstance(n,int) and isinstance(N,int) and N>=0 and n>=max(2,N)
    for key in ('entire_retained_IR_cut_subtracted','regular_matching_and_exhaustive_IR_inventory',
                'poles_and_forward_limit_accounted','large_arc_zero_at_n',
                'global_cut_positive_at_same_scope','jet_and_cut_same_scope',
                'forward_crossing_and_Hermitian_analyticity'):
        assert assumptions.get(key) is True,key
    return True


def validate_contract(c):
    assert c['schema']=='marici.scattering.forward-ir-subtraction.v1'
    assert c['scope']=='pure_g2_power4;forward_IR_control;conditional_improved_matching'
    assert c['kernel']=='D_tau(z)=z^2/pi*integral_0^tau [F(x)/(x-z)+Gamma(F(x))/(x+z)]/x^2 dx'
    assert c['transport']=='C_hat_n(tau2)-C_hat_n(tau1)=-integral_tau1^tau2 [F(x)+(-1)^n*Gamma(F(x))]/(pi*x^(n+1)) dx'
    for key in ('entire_retained_forward_IR_cut_representative_constructed','crossing_and_rim_signs_retained',
                'generated_log_subtraction_remainder_analytic','analytic_coefficient_tail_certified',
                'all_degree_window_shell_transport_constructed','window_cocycle_and_reference_compatibility_retained',
                'positive_right_shell_moments_certified','preparation_dependent_even_window_order_retained',
                'conditional_improved_dispersion_gate_constructed','independent_dimensionful_couplings_retained'):
        assert c[key] is True,key
    for key in ('physical_IR_improved_amplitude_constructed','analyticity_of_arbitrary_matching_series_derived',
                'off_forward_IR_improved_tensor_constructed','matrix_Loewner_window_monotonicity_derived',
                'signed_density_subtraction_is_positive','window_or_reference_source_selected',
                'window_endpoint_is_physical_threshold','global_dispersion_growth_assumptions_source_licensed',
                'UV_fixed_order_spectral_positivity_derived','finite_matching_fixed_or_bounded',
                'native_source_licensed','physical_preparation_selected','physical_rates_or_branching_derived',
                'UV_completion_constructed','exact_scattering_operator_constructed','live_proposition_inventory_changed',
                'C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=cross.build();assert parent==json.loads(cross.RESULT.read_text(encoding='utf-8')),'stale crossing positivity'
    a,b,d=Q(1,4),Q(1,2),Q(3,4);norms=0;division=0;rims=0;expansions=0;cocycles=0;references=0;flows=0
    for k,l in product(range(2,9),repeat=2):
        fm,fp,M=mom.pair_eigenvalues(k,l);D=(fm+fp)/2;O=(fp-fm)/2;N=ir.coefficient_norm(k,l)
        assert max(abs(fm),abs(fp),abs(M),abs(M+O),abs(M-O),abs(D))<=N;norms+=1
    for q in range(4,13):
        A=mom.matrix(mom.pair_eigenvalues(2,q-2))
        for z in (Q(1,8),Q(-1,6)):
            p={(q-2,0):Q(1)};J=win.divided_integral(p,z,Q(),b);Jm=win.divided_integral(p,-z,Q(),b)
            explicit=cross.add(cross.scale(z*z*J,A),cross.scale(z*z*Jm,cross.gamma(A)))
            assert polynomial_part({q:A},z,b)==explicit
            assert polynomial_part({q:A},-z,b)==cross.gamma(explicit);division+=1
    for r in ({2:Q(1)},{2:Q(1),3:Q(1)},mom.spectral_coefficients(6)):
        coeff=coefficients(r);expanded=expanded_remainder(coeff,12,b,Q(1,3))
        for n in range(2,13):
            E=analytic_coefficient(coeff,n,b,Q(1,3));assert E==expanded[n];expansions+=1
            assert {key:cross.gamma(A) for key,A in E.items()}==scale_form((-1)**n,E)
            w13=shell(coeff,n,a,d);w12=shell(coeff,n,a,b);w23=shell(coeff,n,b,d)
            assert w13==add_form(w12,w23);cocycles+=1
            for nu in (Q(1),Q(1,3)):
                delta=add_form(analytic_coefficient(coeff,n,b,nu),scale_form(-1,analytic_coefficient(coeff,n,a,nu)))
                assert delta==w12
                # Derivative of the closed coefficient expression vs the endpoint kernel.
                derivative=zero();point=zero()
                for q,A in coeff.items():
                    derivative=cross.add(derivative,cross.scale(b**(q-n),cross.crossed_sum(A,n)))
                    point=cross.add(point,cross.scale(b**q,A))
                assert derivative==cross.scale(b**(-n),cross.crossed_sum(point,n));flows+=1
            rect=add_form(add_form(analytic_coefficient(coeff,n,b,Q(1,3)),scale_form(-1,analytic_coefficient(coeff,n,a,Q(1,3)))),
                          scale_form(-1,add_form(analytic_coefficient(coeff,n,b,Q(1)),scale_form(-1,analytic_coefficient(coeff,n,a,Q(1))))))
            assert rect=={};references+=1
        for z in (b/3,-b/3,3*b/2,-3*b/2):
            actual=residue_from_Cauchy(coeff,z,b);expected=zero()
            if abs(z)<b:
                for q,A in coeff.items():expected=cross.add(expected,cross.scale(abs(z)**q,A))
                if z<0:expected=cross.scale(-1,cross.gamma(expected))
            assert actual==expected;rims+=1
    coeff=coefficients({2:Q(1)});plus=[Q(1),Q(1),Q(),Q()];product_plus=[Q(1),Q(),Q(),Q()]
    w2=shell(coeff,2,a,b);assert form_box(w2,plus)==(Q(-37,5120),Q(-37,5120))
    assert form_box(w2,product_plus)==(Q(63,5120),Q(63,5120))
    # At the first logarithmic degree transport is finite even though the bare moment is not.
    assert shell(coeff,4,a,b)==log_form(cross.crossed_sum(coeff[4],4),b,a)
    K=16;coeff=coefficients(mom.spectral_coefficients(K));error=mom.spectral_moment_error(K,8,b)
    right=shell(coeff,8,a,b,paired=False);paired=shell(coeff,8,a,b)
    vectors={'minus':[Q(1),Q(-1),Q(),Q()],'plus':plus,'mixed':[Q(),Q(),Q(1),Q()]}
    right_boxes={name:rounded_box(*form_box(right,z),error) for name,z in vectors.items()}
    assert all(Q(box[0])>0 for box in right_boxes.values())
    bell_box=rounded_box(*form_box(paired,plus),3*error);product_box=rounded_box(*form_box(paired,product_plus),2*error)
    assert Q(bell_box[1])<0<Q(product_box[0])
    assert remainder_tail(40,b,a)<Q(1,10**8) and remainder_tail(48,b,a)<Q(1,10**10)
    assumptions={key:True for key in ('entire_retained_IR_cut_subtracted','regular_matching_and_exhaustive_IR_inventory',
        'poles_and_forward_limit_accounted','large_arc_zero_at_n','global_cut_positive_at_same_scope',
        'jet_and_cut_same_scope','forward_crossing_and_Hermitian_analyticity')}
    assert improved_dispersion_gate(8,2,assumptions)
    refused_gates=0
    for key in assumptions:
        try:improved_dispersion_gate(8,2,{**assumptions,key:False})
        except AssertionError:refused_gates+=1
        else:raise AssertionError('missing improved dispersion hypothesis admitted')
    try:improved_dispersion_gate(2,4,assumptions)
    except AssertionError:refused_gates+=1
    else:raise AssertionError('free subtraction coefficient fixed')
    refused=[]
    for name in ('physical_IR_improved_amplitude_constructed','analyticity_of_arbitrary_matching_series_derived',
                 'off_forward_IR_improved_tensor_constructed','matrix_Loewner_window_monotonicity_derived',
                 'signed_density_subtraction_is_positive','window_endpoint_is_physical_threshold',
                 'UV_fixed_order_spectral_positivity_derived','finite_matching_fixed_or_bounded'):
        try:
            bad=copy.deepcopy(c);bad[name]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported IR improvement promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((cross.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_forward_ir_subtraction.py'))
    return {'schema':'marici.scattering.forward-ir-subtraction-receipt.v1','status':'pass',
        'scope_verdict':'forward_whole_IR_cut_subtraction_and_window_transport_not_physical_matching_selection',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'forward_and_crossed_coefficient_norm_checks':norms,'paired_Cauchy_division_checks':division,
        'analytic_remainder_coefficient_checks':expansions,'window_cocycle_checks':cocycles,
        'reference_window_compatibility_checks':references,'endpoint_window_flow_checks':flows,'rim_residue_checks':rims,
        'c0_only_unnormalized_n2_shell':{'Bell_plus':'-37/5120','product_plus':'63/5120'},
        'spectral_comparison':{'c0':'0','c1':'0','tau1':'1/4','tau2':'1/2','n':8,'K':K,
            'normalization':'pi^2 times shell integrals; physical coefficient transport divides by another pi',
            'positive_right_shell_eigenvalue_boxes':right_boxes,'paired_Bell_plus_box':bell_box,'paired_product_plus_box':product_box},
        'analytic_remainder_comparison':{'tau':'1/2','a':'1/4','nu':'tau','c0':'0','c1':'0',
            'operator_tail_bounds':{str(N):str(remainder_tail(N,b,a)) for N in (40,48)}},
        'missing_improved_contour_controls_refused':refused_gates,'general_analytic_and_transport_arguments_machine_formalized':False,
        **{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale forward IR subtraction'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','window_cocycle_checks','rim_residue_checks',
        'physical_IR_improved_amplitude_constructed','finite_matching_fixed_or_bounded','hostile_controls_refused')}))


if __name__=='__main__':main()
