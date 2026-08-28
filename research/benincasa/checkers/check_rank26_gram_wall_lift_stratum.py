#!/usr/bin/env python3
"""Certify the rank-26 relation-lift pattern on the existing Gram wall h=0."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; rows=[]
for p,s in ((32009,""),(32003,"-p32003")):
 for axis in ("x","y"):
  path=ROOT/"research"/"benincasa"/"results"/f"rank26-bidual-quotient-horizontality{s}-{axis}-at-3-4-5.json"
  j=json.loads(path.read_text());rows.append({"prime":p,"axis":axis,"base":j["base_relation_dimension"],"lifted":j["lifted_relation_dimension"],"obstructed":j["obstructed_relation_dimension"],"beta":j["bockstein_rank"],"total":j["bockstein_plus_mixed_rank"]})
checks={"point_is_on_existing_gram_wall":3*3+4*4-5*5==0,"all_four_patterns_match":all((r["base"],r["lifted"],r["obstructed"],r["beta"],r["total"])==(3,1,2,0,1) for r in rows)}
payload={"schema":"marici.rank26-gram-wall-lift-stratum.v1","point":[3,4,5],"gram_normal":0,"rows":rows,"checks":checks,"passed":all(checks.values()),"conclusion":"On the existing Gram wall h=x^2+y^2-z^2=0, the relation module jumps to rank three; one relation lifts, two are obstructed, the fiber Bockstein vanishes, and one mixed direction survives."}
out=ROOT/"research"/"benincasa"/"results"/"rank26-gram-wall-lift-stratum.json";out.write_text(json.dumps(payload,indent=2)+"\n");print(json.dumps(payload,indent=2));raise SystemExit(0 if payload["passed"] else 1)
