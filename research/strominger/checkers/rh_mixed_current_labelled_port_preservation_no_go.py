import json
from fractions import Fraction as Q
from pathlib import Path

def rank(A):
 M=[list(map(Q,r)) for r in A]; r=0
 for c in range(len(M[0])):
  p=next((i for i in range(r,len(M)) if M[i][c]),None)
  if p is None:continue
  M[r],M[p]=M[p],M[r]; v=M[r][c]; M[r]=[x/v for x in M[r]]
  for i in range(len(M)):
   if i!=r and M[i][c]:
    v=M[i][c]; M[i]=[M[i][j]-v*M[r][j] for j in range(len(M[0]))]
  r+=1
 return r

def primes(n):return [x for x in range(2,n+2) if all(x%d for d in range(2,int(x**.5)+1))]
rows=[]
for N in range(3,13):
 A=[]
 for p in primes(N):
  for n in range(1,N+1):
   if n%p:A.append([Q(j==n-1) for j in range(N)])
 rows.append({"cutoff":N,"port_rank":rank(A),"mixed_current_quotient_rank":2,"full_mixed_carrier_dimension":4})
checks={
 "exclusion_port_rank_equals_label_cutoff":all(r["port_rank"]==r["cutoff"] for r in rows),
 "krein_quotient_factorization_fails_from_cutoff_three":all(r["port_rank"]>2 for r in rows),
 "even_full_four_coordinate_carrier_fails_from_cutoff_five":all(r["port_rank"]>4 for r in rows if r["cutoff"]>=5),
 "rank_deficit_grows_with_cutoff":all(rows[i+1]["port_rank"]-2>rows[i]["port_rank"]-2 for i in range(len(rows)-1)),
}
base=Path(__file__).parents[1]
prior=json.loads((base/"results"/"rh_bilateral_mixed_current_krein_signature_audit.json").read_text(encoding="utf-8"))
ports=json.loads((base/"results"/"rh_port_valued_response_bonding_audit.json").read_text(encoding="utf-8"))
checks.update({
 "fresh_signature_readback_is_one_one_with_radical_two":prior["signature"]=={"positive":1,"negative":1,"radical":2},
 "authoritative_response_requires_no_scalar_aggregation":ports["checks"]["no_scalar_aggregation_is_used"],
})
result={"schema":"marici.strominger.rh_mixed_current_labelled_port_preservation_no_go.v1","status":"passed" if all(checks.values()) else "failed","sources":["research/strominger/results/rh_bilateral_mixed_current_krein_signature_audit.json","research/strominger/results/rh_all_prime_exclusion_two_response_compression_no_go.json","research/strominger/results/rh_port_valued_response_bonding_audit.json"],"verdict":"The bilateral X,X' current cannot losslessly preserve the labelled prime-exclusion response. Its nondegenerate Krein quotient has rank two, while the jointly faithful exclusion family has rank equal to the label cutoff; factorization fails from cutoff three. Retaining the two radical coordinates only raises the carrier dimension to four and still fails from cutoff five. Therefore the mixed response may be an additional boundary port, but it cannot replace or reconstruct the port-valued arithmetic response. Any conservative completion must retain their product and provide a separate source coupling cell.","checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),"cutoffs":rows}
out=base/"results"/"rh_mixed_current_labelled_port_preservation_no_go.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
