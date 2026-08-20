#!/usr/bin/env python3
"""Exact bivariate final-block Gauss-Manin connection at the soft SNC corner."""
import json, sys, traceback
from pathlib import Path
import sympy as sp

HERE=Path(__file__).resolve().parent
OUT=HERE/"soft_corner_bivariate_final_block.json"
ERR=HERE/"soft_corner_bivariate_final_block.error.txt"

def uncaught(tp,exc,tb):
    ERR.write_text("".join(traceback.format_exception(tp,exc,tb)),encoding="utf-8")
    sys.__excepthook__(tp,exc,tb)
sys.excepthook=uncaught

u,v,a,b,c=sp.symbols("u v a b c")
x=sp.Integer(1)
y=(u+v)/2-x
z=(u-v)/2
E=u
h=x*x+y*y-z*z
F4=x*x*a**4-h*a*a*b*b+y*y*b**4
Ga=(x*x-c*c)*(x*x-y*y-z*z)-2*c*c*z*z
Gb=(y*y-c*c)*(y*y-x*x-z*z)-2*c*c*z*z
H=z*z*((c*c-y*y)*(c*c-x*x)+c*c*z*z)
Kc=sp.expand(F4+Ga*a*a+Gb*b*b+H)
K=sp.factor(Kc.subs(c,-E))
K1=sp.factor(sp.diff(Kc,c).subs(c,-E))
Ka,Kb=sp.diff(K,a),sp.diff(K,b)

basis=[
 ("e6",-sp.Rational(1,2)*K1,3),
 ("e7",sp.Integer(1),1),
 ("e8",a*a,1),
 ("e9",b*b,1),
]
Bcommon=[sp.expand(num*K**((5-pole)//2)) for _,num,pole in basis]

def mons(deg,par):
    return [a**i*b**j for i in range(deg+1) for j in range(deg+1-i)
            if i%2==par[0] and j%2==par[1]]

def solve(target,deg):
    um=mons(deg,(1,0)); vm=mons(deg,(0,1))
    us=sp.symbols(f"U0:{len(um)}"); vs=sp.symbols(f"V0:{len(vm)}")
    cs=sp.symbols("C0:4")
    U=sum((q*m for q,m in zip(us,um)),sp.Integer(0))
    V=sum((q*m for q,m in zip(vs,vm)),sp.Integer(0))
    exact=sp.expand(K*sp.diff(U,a)-sp.Rational(3,2)*U*Ka
                    -K*sp.diff(V,b)+sp.Rational(3,2)*V*Kb)
    expr=sp.expand(target-sum(q*w for q,w in zip(cs,Bcommon))-exact)
    equations=[coef for _,coef in sp.Poly(expr,a,b).terms()]
    unknowns=list(cs)+list(us)+list(vs)
    A,rhs=sp.linear_eq_to_matrix(equations,unknowns)
    ss=sp.linsolve((A,rhs),unknowns)
    if ss is sp.EmptySet or ss==sp.EmptySet: return None
    tup=list(next(iter(ss)))
    unk=set(unknowns)
    if any(tup[k].free_symbols & unk for k in range(4)):
        raise RuntimeError("nonunique cohomology coefficients")
    free=set().union(*(q.free_symbols for q in tup)) & unk
    tup=[sp.factor(q.subs({f:0 for f in free})) for q in tup]
    sub=dict(zip(unknowns,tup))
    if sp.factor(expr.subs(sub))!=0: return None
    return [sp.factor(sub[q]) for q in cs],sp.factor(U.subs(sub)),sp.factor(V.subs(sub)),len(equations),len(unknowns)

def derivative(num,pole,d):
    power=(5-pole)//2
    return sp.expand(sp.diff(num,d)*K**power-sp.Rational(pole,2)*num*sp.diff(K,d)*K**(power-1))

connections={}
certs={}
for d in (u,v):
    rows=[]; dc=[]
    for name,num,pole in basis:
        found=None
        for degree in (3,5,7,9):
            found=solve(derivative(num,pole,d),degree)
            if found:
                row,U,V,neq,nunk=found
                lhs=sp.expand(derivative(num,pole,d)-sum(row[j]*Bcommon[j] for j in range(4)))
                rhs=sp.expand(K*sp.diff(U,a)-sp.Rational(3,2)*U*Ka-K*sp.diff(V,b)+sp.Rational(3,2)*V*Kb)
                assert sp.factor(lhs-rhs)==0
                rows.append(row)
                dc.append({"basis":name,"degree":degree,"equations":neq,"unknowns":nunk})
                break
        if not found: raise RuntimeError(f"no reduction for {name} d{d}")
    connections[str(d)]=rows
    certs[str(d)]=dc

G=sp.Matrix([
 [0,1,(E*E+y*y)/2,(E*E+x*x)/2],
 [0,0,-(E*E+x*x)/2,-x*x*(E*E+y*y)/(2*y*y)]
])
valg=sp.Matrix([
 0,
 (x*x-y*y)*(x*x*y*y-E**4),
 2*x*x*(E*E+y*y),
 -2*y*y*(E*E+x*x)
])
assert sp.simplify(G*valg)==sp.zeros(2,1)

def plane_and_boundary(rows,d):
    A4=sp.Matrix(rows)
    vr=valg.T
    cov=vr.applyfunc(lambda q:sp.diff(q,d))+vr*A4
    alphas=[sp.factor(cov[0,j]/vr[0,j]) for j in (1,2,3)]
    assert all(sp.factor(q-alphas[0])==0 for q in alphas[1:])
    alpha=alphas[0]; beta=sp.factor(cov[0,0])
    assert (cov-sp.Matrix([[beta,0,0,0]])-alpha*vr).applyfunc(sp.factor)==sp.zeros(1,4)
    plane=sp.Matrix([[A4[0,0],0],[beta,alpha]])
    C=G.T
    rhs=A4*C-C.applyfunc(lambda q:sp.diff(q,d))
    cm=C.extract([1,2],[0,1])
    B=sp.simplify(cm.inv()*rhs.extract([1,2],[0,1]))
    assert (C.applyfunc(lambda q:sp.diff(q,d))+C*B-A4*C).applyfunc(sp.factor)==sp.zeros(4,2)
    return plane,B

derived={}
for d in (u,v):
    P,B=plane_and_boundary(connections[str(d)],d)
    derived[str(d)]={"algebraic_plane":P,"boundary":B}

def smat(M):
    return [[str(sp.factor(M[i,j])) for j in range(M.cols)] for i in range(M.rows)]
result={
 "schema":"marici.benincasa.soft_corner_bivariate_final_block.v1",
 "variables":{"x":"1","y":str(y),"z":str(z),"E":"u","B":"u*v"},
 "basis":[q[0] for q in basis],
 "K":str(K),"K1":str(K1),
 "connections":{d:[[str(sp.factor(q)) for q in row] for row in rows] for d,rows in connections.items()},
 "certificates":certs,
 "gysin":smat(G),
 "v_alg":[str(sp.factor(q)) for q in valg],
 "algebraic_planes":{d:smat(derived[d]["algebraic_plane"]) for d in ("u","v")},
 "boundary_connections":{d:smat(derived[d]["boundary"]) for d in ("u","v")},
 "verification":{"all_cleared_identities":True,"gysin_horizontal_both_directions":True}
}
OUT.write_text(json.dumps(result,indent=2,sort_keys=True),encoding="utf-8")
print(json.dumps({"status":"ok","output":str(OUT),"certificates":certs},indent=2))
