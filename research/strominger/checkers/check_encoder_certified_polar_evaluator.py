"""Rational polynomial polar evaluator with a proved geometric tail bound.

Default executes a 1/10 full-encoder tolerance. --epsilon accepts any positive
rational. Runtime/resource efficiency at small epsilon is not asserted.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
from check_witnessed_interface_compiler import ROOT, BASE, rat, mm, tr, inverse, eye, minus, plus, scale, rank, enc


def positive_pivots(A):
    assert A==tr(A)
    a=[row[:] for row in A]
    pivots=[]
    for k in range(len(a)):
        q=a[k][k]
        if q<=0:return None
        pivots.append(q)
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                a[i][j]-=a[i][k]*a[k][j]/q
    return pivots


def main(epsilon, output_name='encoder-certified-polar-evaluator.json'):
    assert epsilon>0
    assert Path(output_name).name==output_name and output_name.endswith('.json')
    files={key:BASE/'results'/name for key,name in {
        'source':'neutron-seam-control-transport.json',
        'memory':'neutron-comparison-memory.json'}.items()}
    raw={key:p.read_bytes() for key,p in files.items()}
    data={key:json.loads(value) for key,value in raw.items()}
    M=rat(data['source']['metric'])
    B=rat(data['memory']['residual_incidence'])
    Gamma=rat(data['memory']['memory_metric'])
    sharp=mm(mm(inverse(M),tr(B)),Gamma)
    S=mm(sharp,B)
    S6=[row[:6] for row in S[:6]]
    M6=[row[:6] for row in M[:6]]
    assert rank(S6)==5 and rank(B)==15
    for i in range(24):
        for j in range(24):
            expected=S6[i%6][j%6] if i<18 and j<18 and i//6==j//6 else F(0)
            assert S[i][j]==expected
    # Exact support projector: all six native amplitudes equal is the kernel.
    ones=[[F(1)] for _ in range(6)]
    norm=mm(mm(tr(ones),M6),ones)[0][0]
    N6=scale(1/norm,mm(mm(ones,tr(ones)),M6))
    Q6=minus(eye(6),N6)
    assert mm(Q6,Q6)==Q6 and mm(S6,Q6)==S6 and mm(S6,N6)==[[F(0)]*6 for _ in range(6)]
    independent=[]
    for column in tr(S6):
        if rank(independent+[column])>len(independent):independent.append(column)
    V=tr(independent)
    g=mm(mm(tr(V),M6),V)
    energy=mm(mm(mm(tr(V),M6),S6),V)
    a,b=F(1,6),F(25,9)
    lower=positive_pivots(minus(energy,scale(a,g)))
    upper=positive_pivots(minus(scale(b,g),energy))
    assert lower is not None and upper is not None
    # Deliberately false enclosing intervals must be rejected exactly.
    assert positive_pivots(minus(energy,scale(F(1,5),g))) is None
    assert positive_pivots(minus(scale(F(2),g),energy)) is None
    rho=1-a/b
    # On the support: f_N(S)=(3/5) sum c_k (I-S/b)^k,
    # c_0=1, c_(k+1)=c_k*(2k+1)/(2k+2). Since c_k<=1,
    # ||W_N-W|| <= rho^(N+1)/(1-rho). Same for off-diagonal U error.
    N=0
    bound=rho/(1-rho)
    while bound>=epsilon:
        N+=1
        bound*=rho
    X=minus(eye(6),scale(1/b,S6))
    power=Q6
    coeff=F(1)
    total=Q6
    for k in range(1,N+1):
        power=mm(X,power)
        coeff*=F(2*k-1,2*k)
        assert 0<coeff<=1
        total=plus(total,scale(coeff,power))
    f6=scale(F(3,5),total)
    assert mm(tr(f6),M6)==mm(M6,f6)
    assert mm(f6,N6)==[[F(0)]*6 for _ in range(6)]
    f=[[F(0)]*24 for _ in range(24)]
    Q=[[F(0)]*24 for _ in range(24)]
    for sector in range(3):
        for i in range(6):
            for j in range(6):
                f[6*sector+i][6*sector+j]=f6[i][j]
                Q[6*sector+i][6*sector+j]=Q6[i][j]
    W=mm(B,f)
    assert mm(W,Q)==W
    # Exact occurrence-memory support via an independent column basis of B.
    cols=[]
    for column in tr(B):
        if rank(cols+[column])>len(cols):cols.append(column)
    Fmem=tr(cols)
    Qmem=mm(mm(mm(Fmem,inverse(mm(mm(tr(Fmem),Gamma),Fmem))),tr(Fmem)),Gamma)
    assert rank(Qmem)==15 and mm(Qmem,Qmem)==Qmem and mm(Qmem,B)==B
    assert mm(Qmem,W)==W
    hashes={p.relative_to(ROOT).as_posix():hashlib.sha256(raw[k]).hexdigest() for k,p in files.items()}
    own=Path(__file__).resolve()
    hashes[own.relative_to(ROOT).as_posix()]=hashlib.sha256(own.read_bytes()).hexdigest()
    for p,h in hashes.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    result={'status':'pass','requested_epsilon':str(epsilon),'polynomial_degree':N,
        'positive_spectral_lower_bound':str(a),'positive_spectral_upper_bound':str(b),
        'exact_contraction_bound':str(rho),'exact_full_encoder_error_upper_bound':str(bound),
        'error_bound_decimal_display':float(bound),
        'lower_positive_pivots':list(map(str,lower)),'upper_positive_pivots':list(map(str,upper)),
        'false_spectral_bounds_rejected':{'lower_1_over_5':True,'upper_2':True},
        'memory_polar_approximation':enc(W),'native_support_projector':enc(Q),
        'memory_support_projector':enc(Qmem),
        'encoder_assembly':'U_N=[[I-Q,W_N^sharp],[W_N,I-Qmem]], sharp uses the stored M and Gamma.',
        'unitarity_scope':'U_N is a certified approximation, not an exact unitary gate. Compiler words must separately be exact isometries.',
        'source_hashes':hashes,
        'scope':'Exact arithmetic and written spectral tail proof; no binary64 target or zero-eigenvalue threshold. Not a compiler, efficiency theorem, WG composition, or physical control admission.'}
    (BASE/'results'/output_name).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','requested_epsilon','polynomial_degree','error_bound_decimal_display']}))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--epsilon',default='1/10')
    parser.add_argument('--output',default='encoder-certified-polar-evaluator.json')
    args=parser.parse_args()
    main(F(args.epsilon),args.output)
