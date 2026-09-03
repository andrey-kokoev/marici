import json
from fractions import Fraction as F
from pathlib import Path
def invariants(xs):
 degree=sum(e for _,e in xs);slope=F(1)
 for lam,e in xs:slope*=F(lam)**e
 return degree,slope,1/slope
witness_two_twos=[(F(2),1),(F(2),1)]
witness_four_one=[(F(4),1),(F(1),1)]
alternatives=[]
for r in (F(3),F(5,2),F(11)):
 xs=witness_two_twos+[(r,1),(r,-1)];d,p,A=invariants(xs);alternatives.append({"inserted_slope":str(r),"degree":d,"slope_product":str(p),"amplitude":str(A)})
checks={"two_twos_give_inverse_square_quarter":invariants(witness_two_twos)==(2,F(4),F(1,4)),"four_and_one_same_invariants":invariants(witness_four_one)==(2,F(4),F(1,4)),"witnesses_inequivalent":witness_two_twos!=witness_four_one,"canceling_slope_pairs_preserve_invariants":all(a["degree"]==2 and a["slope_product"]=="4" and a["amplitude"]=="1/4" for a in alternatives),"four_column_count_does_not_select_slope_list":len(alternatives)>1}
result={"schema":"marici.strominger.rh_quarter_barnes_slope_product_condition.v1","status":"passed" if all(checks.values()) else "failed","verdict":"For C(t)=prod(lambda_r t+a_r)^(-epsilon_r), the observed tail requires sum epsilon_r=2 and prod lambda_r^epsilon_r=4. These aggregate constraints yield numerator 1/4 but do not identify a four-column Barnes divisor.","checks":checks,"witnesses":{"two_twos":[[str(x),e] for x,e in witness_two_twos],"four_and_one":[[str(x),e] for x,e in witness_four_one]},"alternatives":alternatives,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_barnes_slope_product_condition.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
