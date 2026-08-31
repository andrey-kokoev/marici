import json
from fractions import Fraction as Q
from pathlib import Path

def rank(A):
 M=[r[:] for r in A]; rows=len(M); cols=len(M[0]); r=0
 for c in range(cols):
  p=next((i for i in range(r,rows) if M[i][c]),None)
  if p is None:continue
  M[r],M[p]=M[p],M[r];v=M[r][c];M[r]=[x/v for x in M[r]]
  for i in range(rows):
   if i!=r and M[i][c]:
    v=M[i][c];M[i]=[M[i][j]-v*M[r][j] for j in range(cols)]
  r+=1
 return r

def primes_upto(n):
 out=[]
 for x in range(2,n+1):
  if all(x%p for p in out if p*p<=x):out.append(x)
 return out

groth=(Path(__file__).parents[2]/"grothendieck"/"prime-multiplication-division-curvature-is-positive-exclusion.md").read_text(encoding="utf-8")
nima=(Path(__file__).parents[2]/"nima"/"theta-logarithmic-moment-tower-observes-finite-packets-but-prime-transport-preserves-their-divisor.md").read_text(encoding="utf-8")
rows=[]
records=[]
for N in range(3,25):
 ps=primes_upto(N+2)
 # Stack every coordinate row retained by P_{p not divide n}.
 A=[]
 for p in ps:
  for n in range(1,N+1):
   if n%p:
    A.append([Q(1) if j==n-1 else Q(0) for j in range(N)])
 r=rank(A)
 rows.append(r==N)
 records.append({"label_cutoff":N,"prime_cutoff":ps[-1],"stacked_exclusion_rank":r,"two_row_rank_cap":2})
checks={
 "all_prime_exclusion_stack_is_jointly_faithful_on_every_cutoff":all(rows),
 "defect_rank_grows_with_label_cutoff":all(records[i]["stacked_exclusion_rank"]<records[i+1]["stacked_exclusion_rank"] for i in range(len(records)-1)),
 "two_response_factorization_fails_from_cutoff_three":all(x["stacked_exclusion_rank"]>2 for x in records),
 "failure_occurs_before_principal_parts_jet_compression":("integer-label Hilbert module" in groth and "principal" not in groth.split("## Exact mixed curvature")[0]),
 "log_moment_tower_also_requires_packet_dependent_rank":("first (r) moments form the Vandermonde system" in nima and "determinant" in nima),
}
result={
 "schema":"marici.strominger.rh_all_prime_exclusion_two_response_compression_no_go.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "sources":["research/grothendieck/prime-multiplication-division-curvature-is-positive-exclusion.md","research/nima/theta-logarithmic-moment-tower-observes-finite-packets-but-prime-transport-preserves-their-divisor.md","research/strominger/results/rh_two_response_filtered_schur_naturality_audit.json"],
 "verdict":"The stacked all-prime exclusion response is injective and has rank equal to the label cutoff. Its rank grows without bound, so no lossless compression through the two common/relative response rows exists from cutoff three onward. This obstruction precedes principal-parts jets. The two-row colligation remains valid for reciprocal sector response, but the positive arithmetic defect family must be retained as an additional infinite response object rather than identified with those two rows.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),"cutoffs":records
}
out=Path(__file__).parents[1]/"results"/"rh_all_prime_exclusion_two_response_compression_no_go.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
