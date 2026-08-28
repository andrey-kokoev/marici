#!/usr/bin/env python3
"""Independently derive G31 rank-five map and test G12->G31 naturality."""
from __future__ import annotations
import contextlib, io, json, os, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
CHECKERS=ROOT/"research"/"benincasa"/"checkers"
sys.path.insert(0,str(CHECKERS))
P=int(os.environ.get("MARICI_FIELD_PRIME","32009"))
os.environ["MARICI_FIELD_PRIME"]=str(P)
with contextlib.redirect_stdout(io.StringIO()):
    import check_rank26_anti_invariant_infinity_map as source
charts=source.src.charts
base=source.src.base

add,mul,power,deriv,shift,clean=source.add,source.mul,source.power,source.deriv,source.shift,source.clean
inv2=pow(2,P-2,P)
SOURCE_POINT=(2,3,4)
TARGET_POINT=(2,4,3)
TARGET_NAMES=("g1","g3","g2","g23","g12")
x,y,z=SOURCE_POINT
k,all_q=charts.g31_fiber_data(*TARGET_POINT)
q_polys=[all_q[name] for name in TARGET_NAMES]
t={1:1}; u={0:1,1:1}

# Independently compactify the target polynomial by homogeneous fiber degree.
F={}
G={}
for (i,j),c in k.items():
    degree=i+j
    if degree==4:
        F[i]=(F.get(i,0)+c)%P
    elif degree==2:
        G[i]=(G.get(i,0)+c)%P
F=clean(F); G=clean(G); Fp=deriv(F)

# Independently compactify all five labelled target denominators.
factors=[]
for q in q_polys:
    linear={}
    constant=0
    for (i,j),c in q.items():
        if i+j==1:
            if i==1: linear=add(linear,{1:c})
            elif j==1: linear=add(linear,{0:c})
        elif i+j==0:
            constant=(constant+c)%P
    factors.append((linear,constant))
D=[{0:1},{},{}]
for linear,constant in factors:
    nxt=[{},{},{}]
    for n in range(3):
        nxt[n]=add(nxt[n],mul(D[n],linear))
        if n: nxt[n]=add(nxt[n],D[n-1],constant)
    D=nxt
D0,D1,D2=D
Q_T,Q_U,Q_F=6,4,1

def ratvec(num,a=0,b=0,f=0):
    out=shift(num,Q_T-a)
    out=mul(out,power(u,Q_U-b))
    out=mul(out,power(F,Q_F-f))
    return clean(out)

def term_vec(coefficient,tp,b,f,extra):
    a=max(0,-tp)
    num=shift(extra,max(0,tp))
    return {k:coefficient*v%P for k,v in ratvec(num,a,b,f).items()}

def reduce_vec(row,pivots):
    row=dict(row)
    while True:
        reducible=[k for k in row if k in pivots]
        if not reducible:return row
        pivot=max(reducible)
        row=add(row,pivots[pivot],-row[pivot])

def add_pivot(row,pivots):
    row=reduce_vec(row,pivots)
    if not row:return False
    pivot=max(row); iv=pow(row[pivot],P-2,P)
    pivots[pivot]={k:v*iv%P for k,v in row.items()}
    return True

def exact_dSW(n,b,f):
    out={}
    if n:out=add(out,term_vec(n,n-1,b,f,F))
    if b:out=add(out,term_vec(-b,n,b+1,f,F))
    coeff=(inv2-f)%P
    if coeff:out=add(out,term_vec(coeff,n,b,f,Fp))
    return clean(out)

exact={}
for f in range(2):
    for b in range(4):
        for n in range(-5,13):
            add_pivot(exact_dSW(n,b,f),exact)

# Target roots are independently read from F: t'=0 gives x, t'=-1 gives z,
# and the leading coefficient gives y.
assert F.get(0)==x*x%P
assert sum(c*(-1)**e for e,c in F.items())%P==z*z%P
assert F.get(4)==y*y%P
coh_raw=[
    ratvec({0:1}),ratvec({2:1}),
    ratvec({0:x},a=1),
    ratvec({0:z},b=1),
    ratvec({1:y}),
]
coh_pivots={}
for j,raw in enumerate(coh_raw):
    row=reduce_vec(raw,exact); expr={j:1}
    while True:
        rs=[k for k in row if k in coh_pivots]
        if not rs:break
        pivot=max(rs); prow,pexpr=coh_pivots[pivot]; c=row[pivot]
        row=add(row,prow,-c); expr=add(expr,pexpr,-c)
    if not row:raise RuntimeError(("collapsed",j))
    pivot=max(row); iv=pow(row[pivot],P-2,P)
    coh_pivots[pivot]=(
        {k:v*iv%P for k,v in row.items()},
        {k:v*iv%P for k,v in expr.items()},
    )

def target_form(i,degree):
    if degree<5:return {}
    if degree==5:return ratvec({i:1},a=2,b=1)
    if degree==6:return ratvec({k:-v%P for k,v in shift(D1,i).items()},a=4,b=2)
    first=add(mul(D1,D1),mul(D0,D2),-1)
    return add(
        ratvec(shift(first,i),a=6,b=3),
        ratvec({k:-inv2*v%P for k,v in shift(G,i).items()},a=2,b=1,f=1),
    )

def coords(row):
    row=reduce_vec(row,exact); out={}
    while row:
        rs=[k for k in row if k in coh_pivots]
        if not rs:return None,row
        pivot=max(rs); prow,expr=coh_pivots[pivot]; c=row[pivot]
        row=add(row,prow,-c); out=add(out,expr,c)
    return [out.get(i,0) for i in range(5)],{}

target_coordinates={}
remainders={}
for e in source.low_exponents:
    i,j=e
    c,r=coords(target_form(i,i+j))
    target_coordinates[e]=c
    if r:remainders[e]=r

# Signed target transport from independently derived t'=1/t matrix.
inv_x2=pow(x*x%P,P-2,P)
signed_U=[
    [1,0,0,z,0],
    [0,y*y*inv_x2%P,0,0,0],
    [0,0,0,0,1],
    [0,0,0,-1,0],
    [0,0,1,0,0],
]
def matvec(M,v):
    return [sum(a*b for a,b in zip(row,v))%P for row in M]

failures=[]
for e in source.low_exponents:
    mapped=(e[1],e[0])
    expected=matvec(signed_U,source.coordinates[e])
    actual=target_coordinates[mapped]
    if actual!=expected:
        failures.append({"source":list(e),"target":list(mapped),"expected":expected,"actual":actual})

checks={
    "target_F_derived_from_target_K": bool(F) and len(F)==3,
    "target_D_derived_from_five_labelled_denominators": len(factors)==5,
    "target_exact_span_rank_25": len(exact)==25,
    "target_anti_cohomology_rank_5": len(coh_pivots)==5,
    "target_all_forms_reduce": not remainders,
    "all_36_raw_monomials_satisfy_naturality": not failures,
}
packet={
 "schema":"marici.rank5-g12-g31-naturality.v1",
 "prime":P,
 "source_point":list(SOURCE_POINT),
 "target_point":list(TARGET_POINT),
 "target_marks":list(TARGET_NAMES),
 "target_F":{str(k):v for k,v in sorted(F.items())},
 "target_G":{str(k):v for k,v in sorted(G.items())},
 "signed_target_transport":signed_U,
 "failure_count":len(failures),
 "failures":failures[:10],
 "checks":checks,
 "passed":all(checks.values()),
 "conclusion":(
   "The independently derived G31 rank-five map agrees with the G12 map "
   "through the signed occurrence-inversion transport on all 36 low monomials."
 ),
}
out=ROOT/"research"/"benincasa"/"results"/f"rank5-g12-g31-naturality-p{P}.json"
out.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8")
print(json.dumps(packet,indent=2))
if not packet["passed"]:raise SystemExit(1)
