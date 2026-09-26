"""Exact uniform-domain bounds and a candidate-record degeneracy hostile."""
from fractions import Fraction as F
from pathlib import Path
import json
import hashlib

def inverse(a):
    rows=[list(map(F,r))+[F(i==j) for j in range(3)] for i,r in enumerate(a)]
    for k in range(3):
        pivot=next((i for i in range(k,3) if rows[i][k]),None)
        if pivot is None:raise ValueError('singular apparatus')
        rows[k],rows[pivot]=rows[pivot],rows[k]
        d=rows[k][k];rows[k]=[x/d for x in rows[k]]
        for i in range(3):
            if i!=k:
                d=rows[i][k];rows[i]=[x-d*y for x,y in zip(rows[i],rows[k])]
    return tuple(tuple(r[3:]) for r in rows)
def norm(a):return max(sum(abs(x) for x in r) for r in a)
def design(v):return tuple((F(x*x),F(2*x*y),F(y*y)) for x,y in v)
def apply(a,v):return tuple(sum(x*y for x,y in zip(r,v)) for r in a)
def minus(a,b):return tuple(tuple(x-y for x,y in zip(r,s)) for r,s in zip(a,b))
def reading(L,R,epsilon,h):
    w=tuple((R[2][d]**2-2*R[1][d]**2+R[0][d]**2)/epsilon**2 for d in range(3))
    return tuple(-x/(2*h*h) for x in apply(inverse(L),w))

K=F(1);e0=F(1,64);h0=F(1,8);M=F(1);r0=F(1,128)
def admitted(L,R,e,h):
    try:k=norm(inverse(L))
    except ValueError:return False
    return k<=K and e>=e0 and h>=h0 and all(r0<=x<=M for row in R for x in row)
def bound(L,R,e,h,L2,R2,e2,h2):
    dr=max(abs(x-y) for row,row2 in zip(R,R2) for x,y in zip(row,row2))
    dl=norm(minus(L,L2))
    return (4*K*M*dr+2*K*K*M*M*dl)/(e0*e0*h0*h0)+4*K*M*M*abs(e-e2)/(e0**3*h0*h0)+4*K*M*M*abs(h-h2)/(e0*e0*h0**3)

checks={};L=design(((3,0),(0,4),(3,4)));e=F(1,32);h=F(1,4)
R=tuple(tuple(e*F(x) for x in (3,4,5)) for _ in range(3))
checks['frozen_protocol_inverse_norm']=norm(inverse(L))==F(1,8)
checks['frozen_protocol_admitted']=admitted(L,R,e,h)
checks['static_reading_zero']=reading(L,R,e,h)==(0,0,0)
for n in (2,4,8,16):
    shift=F(1,256*n)
    L2=design(((F(3)+shift,F(0)),(F(0),F(4)),(F(3),F(4))))
    R2=tuple(tuple(x+shift*(j+1)*(d+1) for d,x in enumerate(row)) for j,row in enumerate(R))
    e2=e+shift;h2=h+shift
    checks[str(n)+'_perturbed_domain']=admitted(L2,R2,e2,h2)
    y=reading(L2,R2,e2,h2)
    checks[str(n)+'_joint_lipschitz_bound']=max(abs(x) for x in y)<=bound(L,R,e,h,L2,R2,e2,h2)
# q controls correspond to positive causal distances epsilon*sqrt(q).
# Only the baseline q is asserted physically flat; perturbations are synthetic.
hostiles=[]
for n in (2,4,8,16,32,64):
    delta=F(1,n);Ld=design(((1,0),(0,1),(F(1),delta)))
    inv=inverse(Ld);q=(F(1),F(1),1+delta*delta)
    noisy=(q[0],q[1],q[2]+delta/2)
    g=apply(inv,q);gn=apply(inv,noisy)
    checks[str(n)+'_hostile_base_shape']=g==(1,0,1)
    checks[str(n)+'_hostile_fixed_fit_gap']=gn[1]-g[1]==F(1,4)
    checks[str(n)+'_hostile_exact_inverse_norm']=norm(inv)==F(n)+F(1,2*n)
    # Perturb only central time: Y gap=(G_noisy-G_base)/h^2.
    gap=(gn[1]-g[1])/(h*h)
    checks[str(n)+'_hostile_fixed_processed_gap']=gap==4
    hostiles.append(dict(n=n,inverse_norm=str(norm(inv)),squared_record_error=str(delta/2),distance_error_upper=str(e*delta/4),processed_offdiagonal_gap=str(gap)))
checks['hostile_distance_errors_vanish_in_samples']=all(F(b['distance_error_upper'])<F(a['distance_error_upper']) for a,b in zip(hostiles,hostiles[1:]))
checks['hostile_rejected_by_uniform_K']=all(F(x['inverse_norm'])>K for x in hostiles)
checks['zero_resolution_margin_rejected']=not admitted(L,R,F(0),h)
checks['zero_clock_margin_rejected']=not admitted(L,R,e,F(0))
checks['singular_limit_rejected']=not admitted(design(((1,0),(0,1),(1,0))),R,e,h)
# Reuse physically realized rounded packets with their explicit source boundaries.
physical_path=Path(__file__).with_name('physical-radar-protocol.json')
physical=json.loads(physical_path.read_text())
for name,source in physical['sources'].items():
    slots={(r['time'],r['direction']):(F(r['rounded_reception'])-F(r['emission']))/2 for r in source['clocks']}
    data=tuple(tuple(slots[t,d] for d in ('x3','y4','xy5')) for t in (-1,0,1))
    checks[name+'_certificate_admitted']=admitted(L,data,e,h)
out=dict(passed=all(checks.values()),checks=checks,certificate=dict(K=str(K),epsilon_min=str(e0),proper_time_step_min=str(h0),distance_min=str(r0),distance_max=str(M)),hostiles=hostiles,
    physical_receipt_sha256=hashlib.sha256(physical_path.read_bytes()).hexdigest(),
    scope='Uniform record-domain theorem plus synthetic degeneracy hostile. No new vacuum realization of perturbed records or noise model inferred.')
Path(__file__).with_name('radar-apparatus-certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
raise SystemExit(0 if out['passed'] else 1)
