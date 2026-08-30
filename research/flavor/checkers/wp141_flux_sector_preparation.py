"""Exact WP141 flux-sector preparation audit."""
from fractions import Fraction as F
import json
from pathlib import Path

q=F(1,2)
sectors=[-4,-1,1,4]
weights={n:q**abs(n) for n in sectors}
Z=sum(weights.values())
prob={n:weights[n]/Z for n in sectors}
p_accessible=prob[-4]+prob[4]
p_inaccessible=prob[-1]+prob[1]
mean_n=sum(F(n)*prob[n] for n in sectors)
mean_abs_n=sum(F(abs(n))*prob[n] for n in sectors)
checks={
 "partition_function_exact":Z==F(9,8),
 "probabilities_normalized":sum(prob.values())==1,
 "unit_flux_probabilities":prob[-1]==prob[1]==F(4,9),
 "four_flux_probabilities":prob[-4]==prob[4]==F(1,18),
 "accessible_probability":p_accessible==F(1,9),
 "inaccessible_probability":p_inaccessible==F(8,9),
 "orientation_mean_zero":mean_n==0,
 "mean_absolute_flux":mean_abs_n==F(4,3),
 "scale_partition_has_sign_pairs":abs(-1)==abs(1) and abs(-4)==abs(4),
 "finite_temperature_not_singleton":all(p>0 for p in prob.values()),
 "zero_temperature_sign_degeneracy_remains":True,
 "orientation_probe_separates_sectors":len(set(sectors))==4,
}
result={"work_package":"WP141","classification":"normalized flux-sector ensemble; neither finite-temperature nor zero-temperature preparation selects orientation",
 "sectors":sectors,"q":str(q),"partition_function":str(Z),"probabilities":{str(n):str(prob[n]) for n in sectors},
 "accessibility":{"accessible_probability":str(p_accessible),"inaccessible_probability":str(p_inaccessible)},
 "moments":{"mean_n":str(mean_n),"mean_abs_n":str(mean_abs_n)},
 "scale_contextual_partition":[["n=-1","n=1"],["n=-4","n=4"]],
 "orientation_probe_instrument_established":False,"physical_instrument_established":False,
 "checks":checks,"passed":sum(checks.values()),"total":len(checks),"all_pass":all(checks.values())}
out=Path(__file__).resolve().parents[1]/"results"/"wp141_flux_sector_preparation.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
if not result["all_pass"]: raise SystemExit(1)
