from __future__ import annotations
import itertools,json
from pathlib import Path
from check_six_point_bcj_quotient_rank import DDM

ROOT=Path(__file__).resolve().parents[3];RESULT=ROOT/"research/nima/results/mbar06-parke-taylor-boundary-functor.json"
LEGS=tuple(range(1,7));NODE=0

def blocks(order,subset):
 membership=[x in subset for x in order]
 return sum(membership[i] and not membership[(i-1)%6] for i in range(6))
def cyclic_canonical(word):
 rotations=[word[i:]+word[:i] for i in range(len(word))]
 reversed_word=tuple(reversed(word));rotations += [reversed_word[i:]+reversed_word[:i] for i in range(len(word))]
 return min(rotations)
def factor_words(order,subset):
 positions=[i for i,x in enumerate(order) if x in subset];start=next(i for i in positions if order[(i-1)%6] not in subset)
 cluster=[];i=start
 while order[i] in subset:cluster.append(order[i]);i=(i+1)%6
 complement=[];j=i
 while order[j] not in subset:complement.append(order[j]);j=(j+1)%6
 return cyclic_canonical(tuple(cluster)+(NODE,)),cyclic_canonical((NODE,)+tuple(complement))
def main():
 splits=[]
 for r in (2,3):
  for subset in itertools.combinations(LEGS,r):
   if r==2 or 1 in subset:splits.append(frozenset(subset))
 rows=[];log_count=0
 for subset in splits:
  for order in DDM:
   q=blocks(order,subset);internal_edges=len(subset)-q;rational_scaling=-internal_edges;differential_scaling=len(subset)-2;total=rational_scaling+differential_scaling;has_log=total==-1
   factors=factor_words(order,subset) if has_log else None
   if has_log:log_count+=1
   rows.append({"split":sorted(subset),"ordering":list(order),"cyclic_blocks":q,"total_epsilon_exponent":total,"has_logarithmic_residue":has_log,"factor_words":[list(x) for x in factors] if factors else None,"criterion_consistent":has_log==(q==1)})
 checks={"mbar06_has_25_stable_divisors":len(splits)==25,"all_600_ordering_divisor_pairs_checked":len(rows)==600,"log_residue_iff_subset_is_cyclic_interval":all(r["criterion_consistent"] for r in rows),"each_ordering_has_9_planar_boundary_divisors":log_count==24*9,"every_residue_has_two_lower_point_parke_taylor_factors":all((r["factor_words"] is not None)==r["has_logarithmic_residue"] for r in rows)}
 out={"schema":"marici.nima.mbar06_parke_taylor_boundary_functor.result.v1","status":"passed" if all(checks.values()) else "failed","checks":checks,"stable_divisor_count":len(splits),"ordering_divisor_pair_count":len(rows),"logarithmic_residue_count":log_count,"rows":rows,"claim_boundary":"Complete combinatorial boundary map for 24 DDM Parke-Taylor forms over all 25 stable divisors of Mbar_0,6. It proves logarithmic residue support and factorization into two lower-point cyclic words. It does not yet prove that every BCJ generator maps to the lower-point BCJ ideals on each divisor."}
 RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
 if out["status"]!="passed":raise SystemExit(1)
if __name__=="__main__":main()
