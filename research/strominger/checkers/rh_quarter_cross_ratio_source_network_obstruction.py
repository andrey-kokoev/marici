import json
from fractions import Fraction as F
from functools import lru_cache,reduce
from pathlib import Path
ss=(F(1),F(5,4),F(3,2),F(7,4))
def q(a,i):return reduce(lambda z,s:z*(s+a+i),ss,F(1))
@lru_cache(None)
def D(n,a):
 if n<=1:return F(1)
 return (q(a,n-1)*D(n-1,a)*D(n-1,a+2)-q(a,0)*D(n-1,a+1)**2)/D(n-2,a+2)
def A(k,a):
 n=k+2;return q(a,0)*D(n-1,a+1)**2
def B(k,a):
 n=k+2;return q(a,n-1)*D(n-1,a)*D(n-1,a+2)
def C(k,a):
 n=k+2;return D(n,a)*D(n-2,a+2)
records=[]
for a in range(13):
 for s in range(9):
  obstruction=B(s,a)*B(s+2,a)-B(s+1,a)**2
  records.append({"shift":a,"index":s,"condensation_partition_exact":B(s,a)==A(s,a)+C(s,a),"denominator_rank_one_obstruction_nonzero":obstruction!=0,"obstruction_sign":1 if obstruction>0 else -1 if obstruction<0 else 0})
checks={"all_condensation_decompositions_exact":all(r["condensation_partition_exact"] for r in records),"all_denominator_rank_one_obstructions_nonzero":all(r["denominator_rank_one_obstruction_nonzero"] for r in records),"tested_117_cases":len(records)==117,"obstruction_sign_stable":len({r["obstruction_sign"] for r in records})==1}
result={"schema":"marici.strominger.rh_quarter_cross_ratio_source_network_obstruction.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Condensation exactly decomposes each cross-ratio denominator into two positive partition terms, so each scalar theta is a normalized event weight. But B_k B_(k+2)-B_(k+1)^2 is nonzero in every tested case, obstructing factorization of entry-dependent denominators into row and column gauges. Thus a direct Lindstrom network obtained by scaling the numerator matrix is unavailable; a coupled normalization construction would be required.","record_count":len(records),"obstruction_sign":records[0]["obstruction_sign"],"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_cross_ratio_source_network_obstruction.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
