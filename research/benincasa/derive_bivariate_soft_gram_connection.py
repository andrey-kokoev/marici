#!/usr/bin/env python3
"""Exact bivariate nine-master connection in u=ell4 and v=ell3."""
import json
from pathlib import Path
import sys
import traceback
import sympy as sp

def _write_uncaught(exc_type, exc, tb):
    Path(__file__).with_name("soft_gram_total_energy_corner_connection.error.txt").write_text(
        "".join(traceback.format_exception(exc_type, exc, tb)), encoding="utf-8"
    )
    sys.__excepthook__(exc_type, exc, tb)

sys.excepthook = _write_uncaught

u, v, a, b, c = sp.symbols("u v a b c")
x = sp.Integer(1)
y = (u + v)/2 - x
z = (u - v)/2
E = sp.factor(x + y + z)
assert sp.factor(E-u) == 0
assert sp.factor(x+y-z-v) == 0

def sq(v):
    return sp.expand(v*v)

h = x*x + y*y - z*z
F4 = x*x*a**4 - h*a*a*b*b + y*y*b**4
Ga_c = (x*x-c*c)*(x*x-y*y-z*z) - 2*c*c*z*z
Gb_c = (y*y-c*c)*(y*y-x*x-z*z) - 2*c*c*z*z
H_c = z*z*((c*c-y*y)*(c*c-x*x)+c*c*z*z)
Kc = sp.expand(F4 + Ga_c*a*a + Gb_c*b*b + H_c)
K = sp.factor(Kc.subs(c, -E))
K1 = sp.factor(sp.diff(Kc, c).subs(c, -E))
Ka = sp.diff(K, a)
Kb = sp.diff(K, b)

# (name, numerator, odd/even parity in a,b, denominator half-power)
# Double-pole residues carry the source-fixed coefficient -K1/2.
basis = [
    ("e1", a*b, (1,1), 1),
    ("e2", a, (1,0), 1),
    ("e3", -sp.Rational(1,2)*a*K1, (1,0), 3),
    ("e4", b, (0,1), 1),
    ("e5", -sp.Rational(1,2)*b*K1, (0,1), 3),
    ("e6", -sp.Rational(1,2)*K1, (0,0), 3),
    ("e7", sp.Integer(1), (0,0), 1),
    ("e8", a*a, (0,0), 1),
    ("e9", b*b, (0,0), 1),
]

def common_numerator(num, pole):
    return sp.expand(num * K**((5-pole)//2))

Bcommon = [common_numerator(num,pole) for _,num,_,pole in basis]

def derivative_common(num, pole, parameter):
    power = (5-pole)//2
    Kp = sp.diff(K, parameter)
    return sp.expand(sp.diff(num,parameter)*K**power
                     - sp.Rational(pole,2)*num*Kp*K**(power-1))

def monomials(maxdeg, parity):
    out=[]
    for i in range(maxdeg+1):
        for j in range(maxdeg+1-i):
            if i%2==parity[0] and j%2==parity[1]:
                out.append(a**i*b**j)
    return out

def coefficient_dict(poly):
    P=sp.Poly(sp.expand(poly),a,b)
    return {m:sp.factor(v) for m,v in P.terms()}

def solve_block(target, parity, degree):
    # Exact terms d(U db/K^(3/2)) + d(V da/K^(3/2)).
    # The second term has the orientation sign from da wedge db.
    umons=monomials(degree,(1-parity[0],parity[1]))
    vmons=monomials(degree,(parity[0],1-parity[1]))
    us=sp.symbols("u0:"+str(len(umons)))
    vs=sp.symbols("v0:"+str(len(vmons)))
    eligible=[j for j,(_,_,par,_) in enumerate(basis) if par==parity]
    cs=sp.symbols("c0:"+str(len(eligible)))
    U=sum((q*m for q,m in zip(us,umons)),sp.Integer(0))
    V=sum((q*m for q,m in zip(vs,vmons)),sp.Integer(0))
    exact=sp.expand(K*sp.diff(U,a)-sp.Rational(3,2)*U*Ka
                    -K*sp.diff(V,b)+sp.Rational(3,2)*V*Kb)
    expr=sp.expand(target-sum((q*Bcommon[j] for q,j in zip(cs,eligible)),sp.Integer(0))-exact)
    P=sp.Poly(expr,a,b)
    equations=[coef for _,coef in P.terms()]
    unknowns=list(cs)+list(us)+list(vs)
    A, rhs=sp.linear_eq_to_matrix(equations,unknowns)
    solset=sp.linsolve((A,rhs),unknowns)
    if solset is sp.EmptySet or solset==sp.EmptySet:
        return None
    tup=next(iter(solset))
    # Basis coefficients must be unique.  Free primitive coefficients are
    # harmless; free dependence in any c_j would mean the alleged master
    # classes are dependent modulo exact forms and the connection is not
    # certified.
    unknown_set=set(unknowns)
    if any((tup[k].free_symbols & unknown_set) for k in range(len(cs))):
        raise RuntimeError(
            f"non-unique cohomology coefficients in parity block {parity}, degree {degree}"
        )
    free=set().union(*(v.free_symbols for v in tup))-({u,v}|set(unknowns))
    # linsolve normally reuses some unknowns as free parameters.
    free |= set().union(*(v.free_symbols for v in tup)) & set(unknowns)
    zero={q:sp.Integer(0) for q in free}
    tup=[sp.factor(v.subs(zero)) for v in tup]
    sub=dict(zip(unknowns,tup))
    residual=sp.factor(expr.subs(sub))
    if residual!=0:
        return None
    row=[sp.Integer(0)]*9
    for q,j in zip(cs,eligible):
        row[j]=sp.factor(sub[q])
    return row, sp.factor(U.subs(sub)), sp.factor(V.subs(sub)), len(equations), len(unknowns)


def derive_direction(parameter):
    rows=[]
    certificates=[]
    for name,num,parity,pole in basis:
        target=derivative_common(num,pole,parameter)
        solved=None
        for degree in (3,5,7,9,11):
            solved=solve_block(target,parity,degree)
            if solved is not None:
                used_degree=degree
                break
        if solved is None:
            raise RuntimeError(f"no reduction for {name} along {parameter}")
        row,U,V,neq,nunk=solved
        lhs=sp.expand(target-sum(row[j]*Bcommon[j] for j in range(9)))
        rhs=sp.expand(K*sp.diff(U,a)-sp.Rational(3,2)*U*Ka
                      -K*sp.diff(V,b)+sp.Rational(3,2)*V*Kb)
        assert sp.factor(lhs-rhs)==0
        rows.append(row)
        certificates.append({"basis":name,"degree":used_degree,
                             "equations":neq,"unknowns":nunk})
    return sp.Matrix(rows),certificates

Au,cert_u=derive_direction(u)
Av,cert_v=derive_direction(v)

curvature=(Av.applyfunc(lambda q:sp.diff(q,u))
           -Au.applyfunc(lambda q:sp.diff(q,v))+Au*Av-Av*Au)
curvature=curvature.applyfunc(sp.factor)
assert curvature==sp.zeros(9)

Gysin=sp.Matrix([
 [0,1,(E*E+y*y)/2,(E*E+x*x)/2],
 [0,0,-(E*E+x*x)/2,-x*x*(E*E+y*y)/(2*y*y)]
])
valg=sp.Matrix([
 0,
 (x*x-y*y)*(x*x*y*y-E**4),
 2*x*x*(E*E+y*y),
 -2*y*y*(E*E+x*x)
])
assert sp.simplify(Gysin*valg)==sp.zeros(2,1)
C=Gysin.T
final_idx=[5,6,7,8]
kernel_basis=sp.Matrix.hstack(sp.Matrix([1,0,0,0]),valg)
direction_data={}
for name,param,A in (("u",u,Au),("v",v,Av)):
    A4=A.extract(final_idx,final_idx)
    vrow=valg.T
    cov_v=vrow.applyfunc(lambda q:sp.diff(q,param))+vrow*A4
    alpha=sp.factor(cov_v[0,1]/vrow[0,1])
    beta=sp.factor(cov_v[0,0])
    assert (cov_v-sp.Matrix([[beta,0,0,0]])-alpha*vrow).applyfunc(sp.factor)==sp.zeros(1,4)
    Aalg=sp.Matrix([[A4[0,0],0],[beta,alpha]])
    rhs=A4*C-C.applyfunc(lambda q:sp.diff(q,param))
    Cminor=C.extract([1,2],[0,1])
    B=sp.simplify(Cminor.inv()*rhs.extract([1,2],[0,1]))
    assert (C.applyfunc(lambda q:sp.diff(q,param))+C*B-A4*C).applyfunc(sp.factor)==sp.zeros(4,2)
    direction_data[name]={"A4":A4,"Aalg":Aalg,"Bell":B}

def residue_matrix(A,param):
    R=sp.zeros(A.rows,A.cols)
    higher=[]
    for i in range(A.rows):
        for j in range(A.cols):
            q=sp.cancel(A[i,j])
            if q==0:
                continue
            r=sp.factor(sp.limit(param*q,param,0))
            second=sp.factor(sp.limit(param**2*q,param,0))
            if second!=0:
                higher.append([i+1,j+1,str(second)])
            R[i,j]=r
    return R,higher

Ru,hu=residue_matrix(Au,u)
Rv,hv=residue_matrix(Av,v)
assert not hu and not hv
Ru4=Ru.extract(final_idx,final_idx)
Rv4=Rv.extract(final_idx,final_idx)
Rue=direction_data["u"]["Bell"].applyfunc(lambda q:sp.factor(sp.limit(u*q,u,0)))
Rve=direction_data["v"]["Bell"].applyfunc(lambda q:sp.factor(sp.limit(v*q,v,0)))
Rua=direction_data["u"]["Aalg"].applyfunc(lambda q:sp.factor(sp.limit(u*q,u,0)))
Rva=direction_data["v"]["Aalg"].applyfunc(lambda q:sp.factor(sp.limit(v*q,v,0)))

# Generic divisor residues commute after restriction to their crossing if finite.
corner_limits={}
for label,R,other in (("Ru_at_v0",Ru,v),("Rv_at_u0",Rv,u)):
    entries=[]
    finite=True
    for q in R:
        lim=sp.limit(q,other,0)
        if lim in (sp.oo,-sp.oo,sp.zoo) or getattr(lim,"has",lambda *_:False)(sp.oo,sp.zoo):
            finite=False
        entries.append(lim)
    corner_limits[label]={"finite":finite,"matrix":sp.Matrix(R.rows,R.cols,entries)}

def strings(M):
    return [[str(sp.factor(M[i,j])) for j in range(M.cols)] for i in range(M.rows)]

result={
 "schema":"marici.benincasa.bivariate_soft_gram_connection.v1",
 "status":"pass",
 "coordinates":{"X1":"1","X2":"(u+v)/2-1","X3":"(u-v)/2","E":"u","ell3":"v","B":"u*v"},
 "basis_order":[q[0] for q in basis],
 "connection_u":strings(Au),
 "connection_v":strings(Av),
 "reduction_certificates":{"u":cert_u,"v":cert_v},
 "flatness":{"curvature_zero":True},
 "residues":{
   "Ru":strings(Ru),"Rv":strings(Rv),
   "Ru_final":strings(Ru4),"Rv_final":strings(Rv4),
   "Ru_algebraic":strings(Rua),"Rv_algebraic":strings(Rva),
   "Ru_elliptic":strings(Rue),"Rv_elliptic":strings(Rve),
   "higher_u":[],"higher_v":[]
 },
 "corner_limits":{k:{"finite":d["finite"],"matrix":strings(d["matrix"])}
                  for k,d in corner_limits.items()},
 "interpretive_boundary":[
   "Exact rational bivariate de Rham connection for the frozen nine-master q_G12 residue module.",
   "If a residue limit is nonfinite, logarithmic blowup/gauge reduction remains required before an extension-class claim.",
   "This does not establish integral or physical-chain compatibility."
 ]
}
out=Path(__file__).with_name("bivariate_soft_gram_connection.json")
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({"status":"ok","output":str(out),
                  "Ru_corner_finite":corner_limits["Ru_at_v0"]["finite"],
                  "Rv_corner_finite":corner_limits["Rv_at_u0"]["finite"]},indent=2))
