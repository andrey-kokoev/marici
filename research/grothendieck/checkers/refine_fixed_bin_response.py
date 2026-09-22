"""Sharpen fixed-hat bulk pairings by larger auxiliary exponential projections.

The deployed filters are read, never regenerated or replaced. All approximation
coefficients belong to a proof-only Hilbert projection, not an acquisition.
"""
from pathlib import Path
import json
from flint import arb,acb,acb_series,arb_mat,ctx

HERE=Path(__file__).resolve().parent
OUT=HERE.parent/'results'

def upper(x):return arb(x.upper())
def symmetric(x):return (-upper(x)).union(upper(x))
def rat(p):return arb(p[0])/arb(p[1])
def exp_integrals(rate,a,b):
    d=b-a;z=rate*d;e=(-z).exp();left=(-rate*a).exp()
    return left*(1-e)/rate,left*(1-(1+z)*e)/(d*rate*rate)

def refine(bulk_squared_upper,subdivisions=8,bits=3072):
    ctx.prec=bits;ctx.cap=2
    manifest=json.loads((OUT/'time-bin-cubic-observer.json').read_text(encoding='utf-8'))
    filters=manifest['filters'];times=[rat(p) for p in filters['nodes']]
    assert times[0]==0 and times[-1]==64 and all(b>a for a,b in zip(times,times[1:]))
    # Distinct positive rates give a positive-definite Cauchy Gram matrix.
    # Exclude rate 2 to avoid a removable divided-difference singularity.
    rates=[arb(2)**(arb(j)/subdivisions) for j in range(-5*subdivisions,12*subdivisions+1) if j!=subdivisions]
    s=arb(7)/2;beta=arb(3)/2
    def L(q):
        z=acb_series([acb(q),1],2).zeta()
        return (1/q+1/(q-1)-arb.pi().log()/2+(acb(q)/2).digamma()/2+z[1]/z[0]).real
    ls=L(s);lvalues=[L(beta+r) for r in rates]
    gram=arb_mat([[1/(a+b) for b in rates] for a in rates])
    responses=[];diagnostics=[]
    for side in (0,1):
        moments=[]
        for rate,lq in zip(rates,lvalues):
            q=beta+rate
            value=(-(ls+lq)/(s+q-1)+1/(s*(q-1))+1/((s-1)*q)) if side==0 else ((lq-ls)/(q-s)+1/((s-1)*(q-1))+1/(s*q))
            moments.append(-value)
        f=filters['bulk'][side];normalizer=rat(f['normalizer'])
        assert normalizer>0
        values=[arb(n)/filters['nodal_denominator']/normalizer for n in f['nodal_numerators']]
        assert len(values)==len(times) and values[-1]==0
        norm=arb(0);hat_moments=[arb(0) for _ in rates]
        for k,(lo,hi) in enumerate(zip(times,times[1:])):
            p,q=values[k:k+2]
            norm+=(hi-lo)*(p*p+p*q+q*q)/3
            for j,r in enumerate(rates):
                i0,i1=exp_integrals(r,lo,hi)
                hat_moments[j]+=p*i0+(q-p)*i1
        assert 0<norm<1
        rhs=arb_mat([[m,h] for m,h in zip(moments,hat_moments)])
        solved=gram.solve(rhs)
        g_square=sum(m*solved[j,0] for j,m in enumerate(moments))
        b_square=sum(h*solved[j,1] for j,h in enumerate(hat_moments))
        center=sum(m*solved[j,1] for j,m in enumerate(moments))
        g_residual=upper(bulk_squared_upper[side]-g_square)
        b_residual=norm-b_square
        assert center.is_finite() and b_residual>0 and g_residual>0
        radius=(g_residual*upper(b_residual)).sqrt()
        response=center+symmetric(radius)
        responses.append(response)
        diagnostics.append({'projection_dimension':len(rates),'bulk_residual_squared_upper':g_residual.str(24),
                            'fixed_hat_residual_norm':b_residual.sqrt().str(24),
                            'pairing_center':center.str(24),'pairing_error_upper':upper(radius).str(24),
                            'response':response.str(24)})
    f=filters['weak'];normalizer=rat(f['normalizer'])
    assert normalizer>0
    values=[arb(n)/filters['nodal_denominator']/normalizer for n in f['nodal_numerators']]
    assert len(values)==len(times) and values[-1]==0
    h=arb(0)
    for k,(lo,hi) in enumerate(zip(times,times[1:])):
        i0,i1=exp_integrals(arb(4),lo,hi)
        h+=values[k]*i0+(values[k+1]-values[k])*i1
    direction=[rat(p) for p in filters['endpoint_direction']]
    endpoint_normalizer=rat(filters['endpoint_normalizer'])
    assert len(direction)==2 and endpoint_normalizer>0
    assert sum(x*x for x in direction)/endpoint_normalizer**2<1
    endpoint=(arb(2)/5*direction[0]+arb(2)/7*direction[1])/endpoint_normalizer
    C=sum(responses)+endpoint+h
    assert C>0 and h>0
    return C,h,diagnostics
