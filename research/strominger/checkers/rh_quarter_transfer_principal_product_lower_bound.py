import itertools,json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_hurwitz_transfer_p_matrix_vs_total_positivity.py")))
C,det,k=g["C"],g["det"],g["k"]
def inds(mask):return [i for i in range(k) if mask>>i&1]
def principal(mask):
 S=inds(mask);return F(1) if not S else det([[C[i][j] for j in S] for i in S])
p={m:principal(m) for m in range(1<<k)};diag=[p[1<<i] for i in range(k)];records=[];first_failure=None;chain_failure=None
for mask in range(1<<k):
 S=inds(mask);bound=F(1)
 for i in S:bound*=diag[i]
 relation="equal" if p[mask]==bound else "strict" if p[mask]>bound else "failed"
 rec={"mask":mask,"size":len(S),"relation_to_diagonal_product":relation};records.append(rec)
 if relation=="failed" and first_failure is None:first_failure=rec
 current=0
 for i in S:
  nxt=current|(1<<i)
  if p[current]*p[1<<i]>p[nxt] and chain_failure is None:chain_failure={"base_mask":current,"added_index":i,"difference":str(p[current]*p[1<<i]-p[nxt])}
  current=nxt
checks={"all_principal_product_lower_bounds_hold":first_failure is None,"all_size_at_least_two_bounds_strict":all(r["relation_to_diagonal_product"]=="strict" for r in records if r["size"]>=2),"empty_and_singleton_bounds_equal":all(r["relation_to_diagonal_product"]=="equal" for r in records if r["size"]<=1),"all_canonical_chain_steps_verified":chain_failure is None,"all_256_subsets_checked":len(records)==256}
result={"schema":"marici.strominger.rh_quarter_transfer_principal_product_lower_bound.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Every transfer principal minor is at least the product of its diagonal principal minors, with strict inequality at subset size two or larger. The bound follows inductively from reverse Hadamard-Fischer applied to a current subset and a new singleton. Consequently, positive diagonal plus log-supermodularity is sufficient for the P-matrix signs; no fixed orientation of individual almost-principal minors is needed.","records":records,"first_failure":first_failure,"chain_failure":chain_failure,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
(base/"results"/"rh_quarter_transfer_principal_product_lower_bound.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
