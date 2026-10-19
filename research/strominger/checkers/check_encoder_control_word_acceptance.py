"""Independent rational certificate for a numerically proposed exact control word.

Propagate the exact field operations with deliberate dyadic rounding, charging a
rigorous metric error at every step. The implemented word remains the EXACT
unitary word; rounded states are used only to bound its output. No floating
scout score is used for acceptance.
"""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import argparse
import hashlib
import json
import sys
from check_witnessed_interface_compiler import ROOT, BASE, rat, mm, tr, inverse, blockdiag, minus, plus, scale, eye, enc
from check_encoder_certified_polar_evaluator import positive_pivots


def main(epsilon=F(1,10), output_name='encoder-control-word-acceptance.json',
         scout_name='encoder-control-word-scout.json', evaluator_name='encoder-certified-polar-evaluator.json'):
    assert epsilon>0
    for name in (output_name,scout_name,evaluator_name):
        assert Path(name).name==name and name.endswith('.json')
    sys.set_int_max_str_digits(0)
    names={'source':'neutron-seam-control-transport.json',
           'memory':'neutron-comparison-memory.json',
           'scattering':'neutron-autonomous-rim-scattering.json',
           'orbit':'encoder-conjugated-bank-controls.json',
           'scout':scout_name,
           'evaluator':evaluator_name}
    raw={k:(BASE/'results'/name).read_bytes() for k,name in names.items()}
    data={k:json.loads(value) for k,value in raw.items()}
    for key in ('orbit','scout','evaluator'):
        for p,h in data[key]['source_hashes'].items():
            assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    M=rat(data['source']['metric']);Gamma=rat(data['memory']['memory_metric'])
    metric=blockdiag(M,Gamma);B=rat(data['memory']['residual_incidence'])
    Mi=inverse(M)
    E=rat(data['scattering']['exact_bright_basis'])
    g=mm(mm(tr(E),M),E);gi=inverse(g)
    def dot(a,b):return sum((x*y for x,y in zip(a,b) if x and y),F(0))
    def mv(A,v):return [dot(row,v) for row in A]
    def direction(P):return next(c for c in tr(P) if any(c))
    def zero(A):return all(not x for row in A for x in row)
    # Rebuild every discrete conjugating primitive from the actual source.
    operations={}
    for i,item in enumerate(data['source']['seam_controls']):
        P=rat(item['projector'])
        assert mm(P,P)==P and mm(tr(P),M)==mm(M,P)
        operations[f'seam:{i}']=direction(P)+[F(0)]*21
    for i,row in enumerate(B):
        a=[Gamma[i][i]*x for x in mv(Mi,row)]
        assert dot(row,a)==1
        operations[f'write:{i}']=a+[-F(j==i) for j in range(21)]
    reflectors={}
    for label,d in operations.items():
        dual=mv(metric,d);n=dot(d,dual)
        assert n>0
        reflectors[label]=(d,[2*x/n for x in dual])
    R=rat(data['source']['native_rotation'])
    assert mm(mm(R,R),R)==eye(24) and mm(mm(tr(R),M),R)==M
    base_item=next(x for x in data['source']['source_pulses'] if x['frame']==0)
    baseP=rat(base_item['projector'])
    assert mm(baseP,baseP)==baseP and mm(tr(baseP),M)==mm(M,baseP)
    initial=direction(baseP)+[F(0)]*21
    ds=rat(data['orbit']['directions'])
    words=data['orbit']['conjugating_words']
    duals=[]
    for d,word in zip(ds,words):
        v=initial[:]
        for label in word:
            if label=='native_rotation':v=mv(R,v[:24])+v[24:]
            else:
                normal,dual=reflectors[label];q=dot(dual,v)
                v=[x-q*y for x,y in zip(v,normal)]
        assert v==d
        dual=mv(metric,d);n=dot(d,dual)
        assert n==dot(initial,mv(metric,initial))>0
        duals.append([x/n for x in dual])
    # Retain the ideal source identities needed for the end-to-end theorem.
    S=mm(mm(mm(Mi,tr(B)),Gamma),B)
    L=mm(mm(gi,tr(E)),M);Kb=mm(mm(L,S),E)
    assert mm(S,E)==mm(E,Kb)
    assert zero(mm(scale(F(1,4),rat(data['source']['native_energy'])),E))
    contacts=[row[:2] for row in E]
    assert mm(mm(tr(contacts),M),contacts)==scale(F(3),eye(2))
    # Exact field pair (real, imaginary/sqrt(3)), with bounded dyadic rounding.
    real=E+[[F(0)]*5 for _ in range(21)]
    imag=[[F(0)]*5 for _ in range(45)]
    precision=96;den=2**precision
    def rounded(x):return F((x.numerator*den)//x.denominator,den)
    controls=data['scout']['controls']
    for control in controls:
        index=control['conjugate_direction'];d,dual=ds[index],duals[index]
        t=F(int(control['t_numerator']),int(control['t_denominator']))
        assert t.denominator & (t.denominator-1)==0
        denominator=1+3*t*t
        zr=(1-3*t*t)/denominator;zi=2*t/denominator
        assert zr*zr+3*zi*zi==1
        qr=[dot(dual,c) for c in tr(real)]
        qi=[dot(dual,c) for c in tr(imag)]
        ar=[(zr-1)*x-3*zi*y for x,y in zip(qr,qi)]
        ai=[(zr-1)*y+zi*x for x,y in zip(qr,qi)]
        real=[[rounded(x+d[i]*ar[j]) for j,x in enumerate(row)] for i,row in enumerate(real)]
        imag=[[rounded(x+d[i]*ai[j]) for j,x in enumerate(row)] for i,row in enumerate(imag)]
    # At each step, each of 225 complex entries has magnitude error <=2/den.
    # Weighted HS <= sqrt(tr(metric)*tr(gi))*ordinary Frobenius.
    # The following rational constant safely bounds 2 sqrt(225 tr(metric) tr(gi)).
    tm=sum(metric[i][i] for i in range(45));tg=sum(gi[i][i] for i in range(5))
    assert tm>0 and tg>0
    constant=2*225*(1+tm)*(1+tg)
    assert constant*constant>=4*225*tm*tg
    rounding_bound=len(controls)*constant/den
    evaluator=data['evaluator']
    W=rat(evaluator['memory_polar_approximation'])
    Q=rat(evaluator['native_support_projector'])
    # Replay the rational evaluator rather than trusting its stated error field.
    a,b=F(1,6),F(25,9)
    assert F(evaluator['positive_spectral_lower_bound'])==a
    assert F(evaluator['positive_spectral_upper_bound'])==b
    S6=[row[:6] for row in S[:6]];M6=[row[:6] for row in M[:6]]
    ones=[[F(1)] for _ in range(6)]
    n6=scale(1/mm(mm(tr(ones),M6),ones)[0][0],mm(mm(ones,tr(ones)),M6))
    q6=minus(eye(6),n6)
    # The first five columns form an independent basis of this rank-five support.
    V=[row[:5] for row in S6]
    gp=mm(mm(tr(V),M6),V);energy=mm(mm(mm(tr(V),M6),S6),V)
    assert positive_pivots(gp) is not None
    assert positive_pivots(minus(energy,scale(a,gp))) is not None
    assert positive_pivots(minus(scale(b,gp),energy)) is not None
    assert mm(S6,q6)==S6 and zero(mm(S6,n6))
    X=minus(eye(6),scale(1/b,S6));power=q6;polynomial=q6;coefficient=F(1)
    degree=evaluator['polynomial_degree'];assert degree>=0
    for k in range(1,degree+1):
        power=mm(X,power);coefficient*=F(2*k-1,2*k)
        polynomial=plus(polynomial,scale(coefficient,power))
    f6=scale(F(3,5),polynomial)
    f=[[F(0)]*24 for _ in range(24)]
    for i in range(24):
        for j in range(24):
            live=i<18 and j<18 and i//6==j//6
            assert S[i][j]==(S6[i%6][j%6] if live else 0)
            assert Q[i][j]==(q6[i%6][j%6] if live else 0)
            if live:f[i][j]=f6[i%6][j%6]
    assert mm(B,f)==W
    rho=1-a/b
    assert F(evaluator['exact_full_encoder_error_upper_bound'])==rho**(degree+1)/(1-rho)
    target=mm(minus(eye(24),Q),E)+mm(W,E)
    error=minus(real,target)
    squared=plus(mm(mm(tr(error),metric),error),scale(3,mm(mm(tr(imag),metric),imag)))
    weighted=mm(gi,squared)
    hs2=sum(weighted[i][i] for i in range(5))
    assert hs2>=0
    # Upward dyadic enclosure of sqrt(hs2), checked without floating arithmetic.
    rootden=2**40
    rootfloor=isqrt((hs2.numerator*rootden*rootden)//hs2.denominator)
    measured_lower=F(rootfloor,rootden)
    measured_bound=F(rootfloor+1,rootden)
    assert measured_lower*measured_lower<=hs2<=measured_bound*measured_bound
    evaluation_bound=F(evaluator['exact_full_encoder_error_upper_bound'])
    total=measured_bound+rounding_bound+evaluation_bound
    accepted=total<epsilon
    # A map with five input dimensions satisfies ||D||HS <= sqrt(5)||D||op.
    # Since sqrt(5)<9/4, use a rational lower bound and subtract both certified
    # approximation errors. This bounds the exact word vs the ideal target.
    lower=max(F(0),F(4,9)*measured_lower-rounding_bound-evaluation_bound)
    assert lower<=total
    refuted=lower>epsilon
    assert not (accepted and refuted)
    # Hostile: identity word fails even on the first normalized contact input.
    ready=E+[[F(0)]*5 for _ in range(21)]
    identity_error=[ready[i][0]-target[i][0] for i in range(45)]
    identity_error_squared=dot(identity_error,mv(metric,identity_error))/3
    assert identity_error_squared>(F(1,10)+evaluation_bound)**2
    # Negative controls: an impossible zero budget cannot be accepted; the
    # evaluator tail and arithmetic rounding are not silently dropped.
    assert not total<F(0)
    assert total>measured_bound and evaluation_bound>0 and rounding_bound>0
    # Uniform full-state inverse is symbolic: reverse all unitary primitives;
    # for a conjugated bank gate, negate t. No rounded state is the gate output.
    inverse_controls=[dict(c,t_numerator=str(-int(c['t_numerator']))) for c in reversed(controls)]
    primitive_length=sum(2*len(words[c['conjugate_direction']])+1 for c in controls)
    hashes={(BASE/'results'/names[k]).relative_to(ROOT).as_posix():hashlib.sha256(value).hexdigest() for k,value in raw.items()}
    own=Path(__file__).resolve();hashes[own.relative_to(ROOT).as_posix()]=hashlib.sha256(own.read_bytes()).hexdigest()
    for p,h in hashes.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    report={'status':'pass','word_accepted':accepted,'requested_encoding_tolerance':str(epsilon),
        'word_refuted_at_requested_tolerance':refuted,
        'exact_word_error_lower_bound':str(lower),'word_error_lower_decimal_display':float(lower),
        'evaluation_budget_alone_exhausts_tolerance':evaluation_bound>=epsilon,
        'word_disposition':('accepted' if accepted else 'refuted' if refuted else 'unresolved_by_bounds'),
        'conjugated_bank_gates':len(controls),'primitive_operation_count_with_R_inverse_macro':primitive_length,
        'execution_model':'Exact rational-field bank phase gates conjugated by stored discrete words; rounded arrays are certification intermediates only.',
        'evaluator_polynomial_and_spectral_bounds_replayed_exactly':True,
        'identity_word_rejected_on_normalized_contact':True,
        'rounding_bits':precision,'rounded_comparison_HS_upper_bound':str(measured_bound),
        'certification_rounding_error_bound':str(rounding_bound),
        'polar_evaluation_error_bound':str(evaluation_bound),
        'total_encoding_error_bound':str(total),'total_encoding_error_decimal_display':float(total),
        'free_storage_error_bound':str(total),'decoded_recovery_error_bound':str(2*total),
        'transported_contact_amplitude_error_bound':str(2*total),
        'inverse_controls':inverse_controls,
        'contact_recipe':'Apply the SAME exact accepted word to the two ready raw contact columns, then normalize by sqrt(3); do not substitute rounded certification states.',
        'source_hashes':hashes,
        'scope':'One accepted software word if word_accepted=true. Bounds apply to ready-memory bright inputs, fixed free storage and co-transported contacts. No all-tolerance termination implementation, optimized complexity, formal WG term, coupled-lead/noise theorem or hardware admission.'}
    (BASE/'results'/output_name).write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['status','word_disposition','requested_encoding_tolerance','word_error_lower_decimal_display','total_encoding_error_decimal_display','evaluation_budget_alone_exhausts_tolerance']}))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--epsilon',default='1/10')
    parser.add_argument('--output',default='encoder-control-word-acceptance.json')
    parser.add_argument('--scout',default='encoder-control-word-scout.json')
    parser.add_argument('--evaluator',default='encoder-certified-polar-evaluator.json')
    args=parser.parse_args()
    main(F(args.epsilon),args.output,args.scout,args.evaluator)
