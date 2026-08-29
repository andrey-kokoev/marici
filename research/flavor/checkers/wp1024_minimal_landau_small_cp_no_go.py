import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).parents[1]
wp1023=json.loads((ROOT/"results"/"wp1023_maximal_cp_selector_no_go.json").read_text())
ensemble=json.loads((ROOT/"results"/"wp20_valley_audit.json").read_text())
assert wp1023["status"]=="PASS"

x=sp.symbols("x",real=True)
# Primitive coefficient-free CP-even Landau family V=alpha*x+beta*x^2 on
# normalized invariant x=108*J^2 in [0,1].
rows=[]
for alpha in [-1,0,1]:
    beta=1
    V=alpha*x+beta*x**2
    stationary=sp.solve(sp.diff(V,x),x)
    admitted=[r for r in stationary if r.is_real and 0<=r<=1]
    candidates={sp.Integer(0),sp.Integer(1),*admitted}
    values={c:sp.simplify(V.subs(x,c)) for c in candidates}
    minimum=min(values,key=lambda c:values[c])
    rows.append({"alpha":alpha,"beta":beta,
                 "stationary":[str(r) for r in admitted],
                 "global_minimum":str(minimum)})
assert [r["global_minimum"] for r in rows]==["1/2","0","0"]

# Primitive linear actions add only the endpoints.
linear_minima={"alpha=-1":"1","alpha=1":"0"}
selected={sp.Integer(0),sp.Rational(1,2),sp.Integer(1)}

Js=[abs(sp.Rational(str(row["J"]))) for row in ensemble["records"]]
xs=[sp.factor(108*j*j) for j in Js]
assert len(xs)==1210
assert all(0<v<sp.Rational(27,250000) for v in xs)
assert all(v not in selected for v in xs)

# General quartic Landau stationary point x*=-alpha/(2 beta). Matching any
# fitted x requires the coefficient ratio alpha/beta=-2*x_fit.
ratio_bound=sp.Rational(27,125000)
assert all(abs(-2*v)<ratio_bound for v in xs)

result={
 "schema":"marici.flavor.wp1024.v1","status":"PASS",
 "admissible_domain":"normalized invariant x=108*J^2 in [0,1] on the nondegenerate physical mixing quotient",
 "candidate_family":"V(x)=alpha*x+beta*x^2 with primitive coefficient-free alpha in {-1,0,1}, beta=1, plus primitive linear endpoints",
 "candidate_rows":rows,"linear_minima":linear_minima,
 "coefficient_free_selected_values":["0","1/2","1"],
 "contextual_partition":"CP-conserving, half-maximal, and maximal primitive Landau loci versus the small nonzero fitted band",
 "classification":"descending mathematical selector family with existing readout; no viable small nonzero selector and no declared source-local realization",
 "ensemble_sheets_tested":len(xs),"ensemble_sheets_surviving":0,
 "fitted_normalized_upper_bound":"27/250000",
 "smallest_exact_falsifier":"every fitted 0<x<27/250000, disjoint from {0,1/2,1}",
 "coefficient_ratio_gate":"fitting an interior sheet requires alpha/beta=-2*x_fit, whose magnitude is below 27/125000 and therefore imports a small scale",
 "deliberate_failure_nonzero_obstruction":"the primitive broken minimum x=1/2 is exact and nonzero but phenomenologically false",
 "instrument":"CKM/Jarlskog readout resolves x; no source action or preparation instrument is established",
 "claim_boundary":"closes only the minimal quadratic Landau action in x and primitive coefficient choices, not higher-degree or source-derived nonpolynomial actions",
 "remaining_gate":"derive a small dimensionless ratio from independent source structure before inserting it into an invariant action",
}
out=ROOT/"results"/"wp1024_minimal_landau_small_cp_no_go.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print("WP1024 PASS: primitive minima {0,1/2,1}; survivors 0")
