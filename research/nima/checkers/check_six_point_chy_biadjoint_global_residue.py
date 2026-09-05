from __future__ import annotations

import itertools,json
from pathlib import Path
import sympy as sp
from check_six_point_chy_localization_algebra import G,LABELS,sij,u,x3,x4,x5

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/nima/results/six-point-chy-biadjoint-global-residue.json"

def channel(diagonal):
    a,b=diagonal; subset=tuple(range(a,b))
    if len(subset)>3: subset=tuple(i for i in LABELS if i not in subset)
    return sp.expand(sum(sij(i,j) for i,j in itertools.combinations(subset,2)))
def crosses(d1,d2):
    a,b=d1;c,d=d2
    return (a<c<b<d) or (c<a<d<b)
def eval_poly(expr,C):
    poly=sp.Poly(expr,x5,domain=sp.QQ)
    return sum((coefficient*C**power for (power,),coefficient in poly.terms()),sp.zeros(6))

def main():
    triangular={}
    for variable in (x3,x4):
        candidates=[p.as_expr() for p in G.polys if sp.degree(p.as_expr(),variable)==1 and p.as_expr().free_symbols <= {variable,x5}]
        triangular[variable]=sp.solve(candidates[0],variable)[0]
    univariate=[p.as_expr() for p in G.polys if p.as_expr().free_symbols <= {x5}]
    modulus=sp.Poly(univariate[-1],x5,domain=sp.QQ).monic()
    coefficients=modulus.all_coeffs()[1:]
    C=sp.zeros(6)
    for i in range(5): C[i+1,i]=1
    for i,coefficient in enumerate(reversed(coefficients)): C[i,5]=-coefficient
    I=sp.eye(6)
    Z={1:sp.zeros(6),2:I,3:eval_poly(triangular[x3],C),4:eval_poly(triangular[x4],C),5:C,6:-I}
    def invdiff(i,j): return (Z[i]-Z[j]).inv()
    PT=I
    for i in range(6): PT=PT*invdiff(LABELS[i],LABELS[(i+1)%6])
    phi={}
    for i in LABELS:
        for j in LABELS:
            if i!=j: phi[i,j]=sij(i,j)*(invdiff(i,j)**2)
        phi[i,i]=-sum((phi[i,j] for j in LABELS if j!=i),sp.zeros(6))
    a,b,c=3,4,5
    minor=phi[a,a]*(phi[b,b]*phi[c,c]-phi[b,c]*phi[c,b])-phi[a,b]*(phi[b,a]*phi[c,c]-phi[b,c]*phi[c,a])+phi[a,c]*(phi[b,a]*phi[c,b]-phi[b,b]*phi[c,a])
    gauge=(Z[1]-Z[2])*(Z[2]-Z[6])*(Z[6]-Z[1])
    detprime=minor*(gauge**-2)
    global_residue=sp.cancel(sp.trace(PT*PT*detprime.inv()))
    diagonals=[(a,b) for a in range(1,7) for b in range(a+2,7) if not (a==1 and b==6)]
    triangulations=[combo for combo in itertools.combinations(diagonals,3) if all(not crosses(x,y) for x,y in itertools.combinations(combo,2))]
    cubic_sum=sp.cancel(sum(sp.prod(1/channel(d) for d in tri) for tri in triangulations))
    oriented_cubic_sum=(-1)**(6-3)*cubic_sum
    checks={"quotient_basis_dimension_6":C.rows==6,"hexagon_has_14_triangulations":len(triangulations)==14,"chy_global_residue_equals_oriented_planar_cubic_sum":sp.cancel(global_residue-oriented_cubic_sum)==0,"unoriented_comparison_exhibits_predicted_odd_degree_sign":sp.cancel(global_residue+cubic_sum)==0,"common_value_nonzero":global_residue!=0}
    out={"schema":"marici.nima.six_point_chy_biadjoint_global_residue.result.v1","status":"passed" if all(checks.values()) else "failed","checks":checks,"global_residue":str(global_residue),"unoriented_planar_cubic_sum":str(cubic_sum),"residue_orientation_factor":"(-1)^(n-3) = -1","claim_boundary":"Exact companion-matrix evaluation of the six-point diagonal biadjoint CHY pairing. The multivariate-residue orientation differs from the unsigned propagator sum by the predicted odd-dimensional factor (-1)^(n-3). This validates localization, Jacobian, Parke-Taylor, and residue conventions before insertion of the Yang-Mills reduced Pfaffian."}
    RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    if out["status"]!="passed":raise SystemExit(1)
if __name__=="__main__":main()
