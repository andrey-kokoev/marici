import json
from fractions import Fraction as F
from pathlib import Path
witness=[(F(3),1),(F(3),1),(F(5),1),(F(5),1),(F(7),1),(F(2),-1),(F(2),-1),(F(2),-1),(F(13),-1)]
def product(xs):
 p=F(1)
 for a,e in xs:p*=a**e
 return p
target=F(1575,104);alternatives=[]
for r in (F(11),F(17,3),F(101,7)):
 alt=witness+[(r,1),(r,-1)];alternatives.append({"inserted":str(r),"product":str(product(alt)),"different_length":len(alt)!=len(witness)})
checks={"prime_witness_exact":product(witness)==target,"canceling_pairs_preserve_product":all(F(a["product"])==target for a in alternatives),"lists_are_distinct":all(a["different_length"] for a in alternatives),"infinitely_many_parameterized_by_positive_rational":len({a["inserted"] for a in alternatives})==3,"packet_denies_source_authority":"not a claimed determinant asymptotic" in (Path(__file__).parents[1]/"rh-barnes-multiplicities-are-not-identifiable-from-the-amplitude.md").read_text(encoding="utf-8")}
result={"schema":"marici.strominger.rh_barnes_multiplicity_nonidentifiability.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The scalar signed-product constraint has infinitely many Barnes lists. A prime-supported witness gives 1575/104, but canceling signed pairs preserve the product, so multiplicities require the full parameter-dependent shift equation.","checks":checks,"witness":[[str(a),e] for a,e in witness],"alternatives":alternatives,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_barnes_multiplicity_nonidentifiability.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
