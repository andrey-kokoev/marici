from __future__ import annotations
import itertools,json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[3];RESULT=ROOT/"research/nima/results/mbar06-scattering-equation-boundary-naturality.json"
LEGS=tuple(range(1,7));eps,z0=sp.symbols("epsilon z_node");x={i:sp.Symbol(f"x{i}") for i in LEGS};y={i:sp.Symbol(f"y{i}") for i in LEGS};s={(i,j):sp.Symbol(f"s{i}{j}") for i in LEGS for j in LEGS if i<j}
def sij(i,j):return s[tuple(sorted((i,j)))]
def stable_splits():
 out=[]
 for r in (2,3):
  for subset in itertools.combinations(LEGS,r):
   if r==2 or 1 in subset:out.append(frozenset(subset))
 return out
def main():
 rows=[]
 for S in stable_splits():
  coords={j:(z0+eps*x[j] if j in S else y[j]) for j in LEGS}
  for i in LEGS:
   equation=sum(sij(i,j)/(coords[i]-coords[j]) for j in LEGS if j!=i)
   if i in S:
    actual=sp.cancel(sp.limit(eps*equation,eps,0));expected=sum(sij(i,j)/(x[i]-x[j]) for j in S if j!=i);sector="cluster"
   else:
    actual=sp.cancel(sp.limit(equation,eps,0));expected=sum(sij(i,j)/(y[i]-y[j]) for j in LEGS if j not in S and j!=i)+sum(sij(i,j) for j in S)/(y[i]-z0);sector="complement_with_node"
   rows.append({"split":sorted(S),"leg":i,"sector":sector,"matches_lower_point_scattering_equation":sp.cancel(actual-expected)==0})
 checks={"all_25_stable_divisors":len(stable_splits())==25,"all_150_leg_divisor_pairs":len(rows)==150,"cluster_equations_factorize":all(r["matches_lower_point_scattering_equation"] for r in rows if r["sector"]=="cluster"),"complement_equations_factorize_with_nodal_momentum":all(r["matches_lower_point_scattering_equation"] for r in rows if r["sector"]=="complement_with_node")}
 out={"schema":"marici.nima.mbar06_scattering_equation_boundary_naturality.result.v1","status":"passed" if all(checks.values()) else "failed","checks":checks,"rows":rows,"claim_boundary":"Exact Laurent-leading factorization of every six-point scattering equation on all 25 stable divisors. Cluster equations become lower-point equations after multiplication by the plumbing parameter; complement equations acquire the aggregate nodal momentum. Combined with Parke-Taylor residue factorization, this proves stability of scattering-equation-generated BCJ exactness under all stable residues."}
 RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
 if out["status"]!="passed":raise SystemExit(1)
if __name__=="__main__":main()
