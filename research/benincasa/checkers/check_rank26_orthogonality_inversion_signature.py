#!/usr/bin/env python3
"""Check h=0 rank-signature invariance under x<->y, a<->b inversion."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];rows=[]
for point in ((3,4,5),(4,3,5)):
 for p,s in ((32009,""),(32003,"-p32003")):
  for axis in ("x","y"):
   q="-at-"+"-".join(map(str,point));path=ROOT/"research"/"benincasa"/"results"/f"rank26-bidual-quotient-horizontality{s}-{axis}{q}.json";j=json.loads(path.read_text());rows.append([list(point),p,axis,j["base_relation_dimension"],j["lifted_relation_dimension"],j["obstructed_relation_dimension"],j["bockstein_rank"],j["bockstein_plus_mixed_rank"]])
checks={"both_points_are_orthogonal":all(x*x+y*y-z*z==0 for x,y,z in ((3,4,5),(4,3,5))),"all_eight_signatures_match":all(tuple(r[3:])==(3,1,2,0,1) for r in rows)}
payload={"schema":"marici.rank26-orthogonality-inversion-signature.v1","rows":rows,"checks":checks,"passed":all(checks.values()),"conclusion":"The h=0 rank signature survives the source inversion chart x<->y, a<->b. This establishes signature covariance only, not transport naturality of the individual classes."}
out=ROOT/"research"/"benincasa"/"results"/"rank26-orthogonality-inversion-signature.json";out.write_text(json.dumps(payload,indent=2)+"\n");print(json.dumps(payload,indent=2));raise SystemExit(0 if payload["passed"] else 1)
