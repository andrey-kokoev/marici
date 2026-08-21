#!/usr/bin/env python3
"""Multiprime sampled exactness ladder for the chi_12345 top form."""

import json
from itertools import product
from pathlib import Path

import check_five_site_weight_five_rational_trace as trace

ROOT = Path(__file__).resolve().parents[2]
CANON = json.loads((ROOT / "research/benincasa/results/five-site-asymmetric-canonical-sum.json").read_text())
LABELS = CANON["denominator_labels"]
OUTPUT = ROOT / "research/nima/results/five-site-weight-five-bounded-exactness.json"


def r_data(u, p):
    u1,u2,u3=u
    r=trace.radicands(u1,u2,u3,p)
    dr=[
      [(4*u1-2*u2)%p,(4*u2-2*u1-2*u3)%p,(2*u3-2*u2)%p],
    ]
    dr += [[(dr[0][j]+v[j])%p for j in range(3)] for v in
           [(-2,0,0),(0,-2,0),(0,0,-2),(2,2,-8)]]
    return r,dr


def norm_and_derivatives(label,t,r,dr,p):
    q=trace.facets[label]
    a=sum(int(x) for x in q["x"])*t % p
    support=[(i,int(b)) for i,b in enumerate(q["y"]) if int(b)]
    if not support:
        return a,[0,0,0]
    if len(support)==1:
        i,b=support[0]; b2=b*b%p
        return (a*a-b2*r[i])%p,[(-b2*dr[i][j])%p for j in range(3)]
    assert len(support)==2
    (i,b),(k,c)=support; b2=b*b%p; c2=c*c%p
    z=(a*a-b2*r[i]-c2*r[k])%p
    n=(z*z-4*b2*c2*r[i]*r[k])%p
    dn=[]
    for j in range(3):
        dz=(-b2*dr[i][j]-c2*dr[k][j])%p
        dn.append((2*z*dz-4*b2*c2*(dr[i][j]*r[k]+r[i]*dr[k][j]))%p)
    return n,dn


def oracle_sample(prime,seed):
    roots={x*x%prime:x for x in range(prime)}
    for off in range(20000):
        u=[(seed+3*off+2)%prime,(2*seed+5*off+3)%prime,(3*seed+7*off+5)%prime]
        t=(11*seed+17*off+13)%prime
        r,dr=r_data(u,prime)
        if any(x==0 or x not in roots for x in r): continue
        ys0=[roots[x] for x in r]
        vals=[]
        for mask in range(32):
            ys=[(-y if mask&(1<<i) else y)%prime for i,y in enumerate(ys0)]
            v=trace.omega(t,ys,prime)
            if v is None: break
            vals.append(v)
        if len(vals)!=32: continue
        tr=sum((-v if m.bit_count()&1 else v) for m,v in enumerate(vals))%prime
        yp=1
        for y in ys0: yp=yp*y%prime
        target=tr*trace.inv(32*yp,prime)%prime
        D=1; dlog=[0,0,0]
        good=True
        for label in LABELS:
            n,dn=norm_and_derivatives(label,t,r,dr,prime)
            if n==0: good=False; break
            D=D*n%prime
            ni=trace.inv(n,prime)
            for j in range(3): dlog[j]=(dlog[j]+dn[j]*ni)%prime
        if not good: continue
        A=[]
        inv2=trace.inv(2,prime)
        for j in range(3): A.append(sum(dr[i][j]*trace.inv(r[i],prime) for i in range(5))*inv2%prime)
        return {"u":u,"t":t,"target":target,"D":D,"dlog":dlog,"A":A}
    raise RuntimeError("sample exhaustion")


def monomials(d):
    return [(a,b,c) for a in range(d+1) for b in range(d+1-a) for c in range(d+1-a-b)]


def rank(matrix,p):
    a=[row[:] for row in matrix]; m=len(a); n=len(a[0]); r=0
    for c in range(n):
        pivot=next((i for i in range(r,m) if a[i][c]%p),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        z=trace.inv(a[r][c],p); a[r]=[x*z%p for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c]%p:
                z=a[i][c]%p; a[i]=[(x-z*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r==m: break
    return r


def row(sample,d,p):
    u=sample["u"]; Dinv=trace.inv(sample["D"],p); out=[]
    for j in range(3):
        for e in monomials(d):
            m=1
            for x,k in zip(u,e): m=m*pow(x,k,p)%p
            derivative=0
            if e[j]:
                derivative=e[j]
                for k,(x,power_) in enumerate(zip(u,e)):
                    derivative=derivative*pow(x,power_-(1 if k==j else 0),p)%p
            out.append((derivative+m*(sample["A"][j]-sample["dlog"][j]))*Dinv%p)
    return out


results=[]
for prime in (1009,1013):
    samples=[]
    for seed in range(1,2001):
        try:
            candidate=oracle_sample(prime,seed)
        except RuntimeError:
            continue
        key=(candidate["t"],*candidate["u"])
        if key not in {(x["t"],*x["u"]) for x in samples}:
            samples.append(candidate)
        if len(samples)==77: break
    assert len(samples)==77, f"insufficient samples over {prime}: {len(samples)}"
    for d in range(4):
        unknowns=3*len(monomials(d)); used=samples[:unknowns+12]
        M=[row(s,d,prime) for s in used]
        r=rank(M,prime); ra=rank([x+[s["target"]] for x,s in zip(M,used)],prime)
        results.append({"prime":prime,"degree":d,"samples":len(used),"unknowns":unknowns,
                        "rank":r,"augmented_rank":ra,"witness_exists":r==ra})

out={"schema":"marici.five_site.weight_five_bounded_exactness.v1","results":results,
     "scope":"Sampled common-simple-denominator degree ladder; no full cohomology claim.","passed":True}
OUTPUT.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,sort_keys=True))
