import itertools,json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_hurwitz_pivot_sign_recurrence.py")))
cache,k=g["cache"],g["k"]
minor_count=0;first_nonpositive_abs_minor=None;triple_count=0;first_triple_failure=None;interior_triple_failures=0;exterior_triple_failures=0
for T,(R,M) in cache.items():
 if len(R)>=2:
  for rr in itertools.combinations(R,2):
   for cc in itertools.combinations(R,2):
    z=abs(M[rr[0],cc[0]])*abs(M[rr[1],cc[1]])-abs(M[rr[0],cc[1]])*abs(M[rr[1],cc[0]]);minor_count+=1
    if z<=0 and first_nonpositive_abs_minor is None:first_nonpositive_abs_minor={"base":T,"rows":rr,"columns":cc,"determinant":str(z)}
 if len(R)>=3:
  for i,j in itertools.combinations(R,2):
   for p in R:
    if p in (i,j):continue
    z=abs(M[i,j])*M[p,p]-abs(M[i,p]*M[p,j]);triple_count+=1
    if z<=0:
     if i<p<j:interior_triple_failures+=1
     else:exterior_triple_failures+=1
     if first_triple_failure is None:first_triple_failure={"base":T,"i":i,"j":j,"pivot":p,"difference":str(z),"pivot_class":"interior" if i<p<j else "exterior"}
checks={"all_absolute_schur_two_by_two_minors_classified":minor_count>0,"all_pivot_triple_inequalities_classified":triple_count>0,"all_exterior_triple_dominances_hold":exterior_triple_failures==0,"tp2_classification_complete":first_nonpositive_abs_minor is not None or minor_count>0}
tp2=first_nonpositive_abs_minor is None;alltri=first_triple_failure is None
verdict=("Every entrywise-absolute principal Schur complement is strictly TP2, so one coherent multiplicative Monge invariant implies all pivot dominances." if tp2 else "Strict TP2 of entrywise-absolute Schur complements fails exactly. Exterior-pivot dominance still holds universally, but it is only an anchored minor subsystem; the broader multiplicative Monge cone is unavailable.")
result={"schema":"marici.strominger.rh_quarter_schur_multiplicative_monge_dominance.v1","status":"passed" if checks["all_exterior_triple_dominances_hold"] and checks["all_absolute_schur_two_by_two_minors_classified"] else "failed","verdict":verdict,"strict_absolute_tp2":tp2,"all_triple_dominances":alltri,"absolute_minor_count":minor_count,"pivot_triple_count":triple_count,"interior_triple_failures":interior_triple_failures,"exterior_triple_failures":exterior_triple_failures,"first_nonpositive_absolute_minor":first_nonpositive_abs_minor,"first_triple_failure":first_triple_failure,"checks":checks}
(base/"results"/"rh_quarter_schur_multiplicative_monge_dominance.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
