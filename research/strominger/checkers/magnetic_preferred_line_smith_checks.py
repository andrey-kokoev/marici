"""Smith invariant of the ray-saturated preferred magnetic observation line."""
import json, math
from pathlib import Path

records=[]
for g in range(2,402,2):
 a,b=2*g+7,3*g+7
 d=math.gcd(a,b)
 records.append({"g":g,"smith_nonzero_invariant":d,
                 "equals_gcd_g_7":d==math.gcd(g,7),
                 "saturation_quotient":"Z/7" if d==7 else "0",
                 "primitive_image_generator":[a//d,b//d]})
passed=all(x["equals_gcd_g_7"] and x["smith_nonzero_invariant"] in (1,7)
           and (x["smith_nonzero_invariant"]==7)==(x["g"]%14==0)
           for x in records)
result={"schema":"marici.checker_results.v1",
 "checker":"magnetic_preferred_line_smith_checks.py","passed":passed,
 "constructor":"independently saturate the two nonzero source-column rays before restricting to preferred rows (R0,R1)",
 "normalized_boundary_matrix":"[[2g+7,2g+7],[3g+7,3g+7]] up to column signs",
 "smith_form":"diag(gcd(g,7),0)",
 "image_saturation_quotient":"Z/gcd(g,7)",
 "interpretation":"A Z/7 presentation residue occurs exactly when 14 divides even g; rational rank remains one.",
 "authority_caution":"This classifies the ray-saturated boundary presentation only, not the unsaturated full operator or a physical state.",
 "hostile_scaling_fixture":{"maps":"[v,v] versus [7v,14v]","same_saturated_rays":True,
   "different_integral_image_index":True,
   "verdict":"ray saturation forgets source multiplicity and requires an explicit constructor"},
 "bounded_replay":"even g=2..400","records":records}
Path(__file__).resolve().parents[1].joinpath("results/magnetic_preferred_line_smith.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({k:v for k,v in result.items() if k!="records"},indent=2))
raise SystemExit(0 if passed else 1)
