#!/usr/bin/env python3
"""Exact q_G12 nine-master connection at the total-energy/Gram/soft corner.

The frozen local normals are u=ell4=E_T and v=ell3, with
X2=(u+v)/2-X1 and X3=(u-v)/2. The corner u=v=0 is X3=0,
X2=-X1. Modes test u=0, v=0, and a radial approach without adding carrier data.
"""
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

la, a, b, c = sp.symbols("lambda a b c")
mode = sys.argv[1] if len(sys.argv) > 1 else "corner"
if mode == "total":
    u, v = la, sp.Integer(1)
elif mode == "gram":
    u, v = sp.Integer(1), la
elif mode == "corner":
    u, v = la, 2*la
else:
    raise ValueError("mode must be total, gram, or corner")
x = sp.Integer(2) if mode == "gram" else sp.Integer(1)
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
Kl = sp.diff(K, la)
K1l = sp.diff(K1, la)
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

def derivative_common(num, pole):
    # d_lambda(num*K^(-pole/2)), represented over K^(5/2)
    power = (5-pole)//2
    return sp.expand(sp.diff(num,la)*K**power
                     - sp.Rational(pole,2)*num*Kl*K**(power-1))

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
    free=set().union(*(v.free_symbols for v in tup))-({la}|set(unknowns))
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

rows=[]
certificates=[]
for idx,(name,num,parity,pole) in enumerate(basis):
    target=derivative_common(num,pole)
    solved=None
    used_degree=None
    for degree in (3,5,7,9,11):
        solved=solve_block(target,parity,degree)
        if solved is not None:
            used_degree=degree
            break
    if solved is None:
        raise RuntimeError(f"no exact reduction found for {name} through degree 11")
    row,U,V,neq,nunk=solved
    # Independent cleared identity verification.
    lhs=sp.expand(target-sum(row[j]*Bcommon[j] for j in range(9)))
    rhs=sp.expand(K*sp.diff(U,a)-sp.Rational(3,2)*U*Ka
                  -K*sp.diff(V,b)+sp.Rational(3,2)*V*Kb)
    assert sp.factor(lhs-rhs)==0
    rows.append(row)
    certificates.append({"basis":name,"degree":used_degree,"equations":neq,"unknowns":nunk})

Q=sp.factor(-16*x*x*y*y-8*x*y*E*E+8*(x+y)*E**3-5*E**4)
Qpoly=sp.Poly(Q,la)
Qsqfree=sp.gcd(Qpoly,sp.diff(Qpoly,la)).degree()==0
q_poles=[]
for i,row in enumerate(rows):
    for j,val in enumerate(row):
        num,den=map(sp.factor,sp.cancel(val).as_numer_denom())
        g=sp.gcd(sp.Poly(den,la),Qpoly)
        if g.degree()>0:
            q_poles.append({"row":i+1,"column":j+1,"gcd":str(sp.factor(g.as_expr())),
                            "coefficient":str(val)})

# Source-fixed infinity-Gysin map on final block and kernel vector.
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
final_idx=[5,6,7,8]
A4=sp.Matrix([[rows[i][j] for j in final_idx] for i in final_idx])
# Connection convention: d e_i = sum_j A_ij e_j.  A row-subspace is closed
# only if rows 6..9 have no columns 1..5; report rather than assume.
outside_final=[
 {"row":i+1,"column":j+1,"coefficient":str(rows[i][j])}
 for i in final_idx for j in range(5) if rows[i][j]!=0
]

# The source-defined algebraic Gysin plane.  Differentiate the moving kernel
# vector itself; a flat subbundle requires v' + v*A4 to remain in
# span(e6,v).  Its quotient by e6 is the canonical rank-one factor selected
# by the last-three cyclic module.
vrow=valg.T
cov_v=sp.Matrix([[sp.factor(sp.diff(vrow[0,j],la)) for j in range(4)]])+vrow*A4
alpha_candidates=[
    sp.factor(cov_v[0,j]/vrow[0,j]) for j in range(1,4)
]
assert all(sp.factor(q-alpha_candidates[0])==0 for q in alpha_candidates[1:])
alpha_alg=sp.factor(alpha_candidates[0])
beta_alg=sp.factor(cov_v[0,0])
assert sp.simplify(cov_v-sp.Matrix([[beta_alg,0,0,0]])-alpha_alg*vrow)==sp.zeros(1,4)
alg_plane=sp.Matrix([
    [A4[0,0],sp.Integer(0)],
    [beta_alg,alpha_alg],
])
predicted_sign_connection=sp.factor(sp.diff(Q,la)/(2*Q))
sign_defect=sp.factor(alpha_alg-predicted_sign_connection)
alpha_num,alpha_den=map(sp.factor,sp.cancel(alpha_alg).as_numer_denom())
alpha_q_gcd=sp.factor(sp.gcd(sp.Poly(alpha_den,la),Qpoly).as_expr())

# Horizontal infinity-Gysin audit.  With C=R_infinity^T, horizontality is
# C' + C*B = A4*C.  Solve B from two independent rows and verify all four.
C=Gysin.T
rhs_gysin=A4*C-C.applyfunc(lambda q:sp.diff(q,la))
minor_rows=[1,2]  # e7 and e8
Cminor=C.extract(minor_rows,[0,1])
assert sp.factor(Cminor.det())!=0
Bboundary=sp.simplify(Cminor.inv()*rhs_gysin.extract(minor_rows,[0,1]))
assert (C.applyfunc(lambda q:sp.diff(q,la))+C*Bboundary-A4*C).applyfunc(sp.factor)==sp.zeros(4,2)

# Eliminate omega_2 from omega_0'=a0*omega_0+b0*omega_2.
a0,b0=Bboundary[0,0],Bboundary[0,1]
c0,d0=Bboundary[1,0],Bboundary[1,1]
S=sp.factor(a0+sp.diff(b0,la)/b0+d0)
T=sp.factor(sp.diff(a0,la)+b0*c0-a0*(sp.diff(b0,la)/b0+d0))
pf_p=sp.factor(-S)
pf_q=sp.factor(-T)
published_p=sp.factor(
    (5*64*la**4-6*10*la**2+1)/(64*la**5-20*la**3+la)
)
published_q=sp.factor((192*la**2-20)/(64*la**4-20*la**2+1))
pf_matches_published=sp.factor(pf_p-published_p)==0 and sp.factor(pf_q-published_q)==0

def lambda_valuation(expr):
    expr=sp.cancel(expr)
    if expr==0:
        return 0
    num,den=expr.as_numer_denom()
    def val(poly):
        poly=sp.Poly(poly,la)
        k=0
        while not poly.is_zero and poly.eval(0)==0:
            poly=sp.quo(poly,sp.Poly(la,la))
            k+=1
        return k
    return val(den)-val(num)

higher_poles=[]
residue_matrix=sp.zeros(9,9)
for i,row in enumerate(rows):
    for j,val in enumerate(row):
        order=lambda_valuation(val)
        if order>1:
            higher_poles.append({"row":i+1,"column":j+1,"order":order})
        elif order==1:
            residue_matrix[i,j]=sp.factor(sp.limit(la*val,la,0))
Ralg=sp.Matrix([[sp.factor(sp.limit(la*alg_plane[i,j],la,0)) for j in range(2)] for i in range(2)])
Rell=sp.Matrix([[sp.factor(sp.limit(la*Bboundary[i,j],la,0)) for j in range(2)] for i in range(2)])

result={
 "schema":"marici.benincasa.soft_gram_total_energy_corner_connection.v1",
 "mode":mode,
 "normals":{"u_total_energy":str(u),"v_gram":str(v),"B_equals_uv":str(sp.factor(u*v))},
 "slice":{"X1":str(x),"X2":str(y),"X3":str(z),"E":str(E)},
 "source_normalization":{"q_G12":"E+y12","gamma":"-1/2","K1":"dK/dy12 at y12=-E"},
 "basis_order":[v[0] for v in basis],
 "K0":str(K),
 "K1":str(K1),
 "Q":str(Q),
 "Q_squarefree":Qsqfree,
 "connection_rows":[[str(sp.factor(v)) for v in row] for row in rows],
 "reduction_certificates":certificates,
 "generic_Q_pole_entries":q_poles,
 "generic_Q_connection_regular":len(q_poles)==0,
 "generic_Q_residue":"zero" if len(q_poles)==0 else "nonzero_or_gauge_dependent",
 "generic_Q_monodromy":"identity" if len(q_poles)==0 else "requires_residue_analysis",
 "final_4x4":[[str(sp.factor(v)) for v in A4.row(i)] for i in range(4)],
 "final_block_outside_entries":outside_final,
 "gysin_rank":Gysin.rank(),
 "gysin_kernel_check":True,
 "algebraic_plane_connection":[
   [str(sp.factor(alg_plane[i,j])) for j in range(2)] for i in range(2)
 ],
 "algebraic_quotient_connection":str(alpha_alg),
 "predicted_Q_sign_connection":str(predicted_sign_connection),
 "Q_sign_rational_gauge_defect":str(sign_defect),
 "algebraic_quotient_denominator_Q_gcd":str(alpha_q_gcd),
 "Q_sign_line_passes":alpha_q_gcd!=1,
 "boundary_connection":[
   [str(sp.factor(Bboundary[i,j])) for j in range(2)] for i in range(2)
 ],
 "boundary_PF_p":str(pf_p),
 "boundary_PF_q":str(pf_q),
 "published_L2_match_not_applicable":pf_matches_published,
 "normal_connection":{"higher_poles":higher_poles,
   "logarithmic":len(higher_poles)==0,
   "residue_matrix":[[str(sp.factor(residue_matrix[i,j])) for j in range(9)] for i in range(9)],
   "residue_charpoly":str(sp.factor(residue_matrix.charpoly().as_expr())),
   "algebraic_plane_residue":[[str(Ralg[i,j]) for j in range(2)] for i in range(2)],
   "elliptic_boundary_residue":[[str(Rell[i,j]) for j in range(2)] for i in range(2)]},
 "interpretive_boundary":[
   "This is an exact de Rham residue-surface connection on one generic homogeneous slice.",
   "It does not by itself construct the physical Borel-Moore integration chain.",
   "Absence of Q in this connection does not exclude Q from a separately supplied moving-chain extension."
 ]
}
out=Path(__file__).with_name(f"soft_gram_total_energy_corner_{mode}.json")
out.write_text(json.dumps(result,indent=2,sort_keys=True),encoding="utf-8")
print(json.dumps({"status":"ok","output":str(out),"Q_regular":result["generic_Q_connection_regular"],
                  "certificates":certificates},indent=2))