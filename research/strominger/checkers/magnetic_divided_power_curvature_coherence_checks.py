"""Curvature obstruction to ambient integral divided-power coherence."""
import json
from fractions import Fraction
from pathlib import Path

records=[]
for g in range(2,202):
    residual=Fraction(2*(g+2),g+1)
    records.append({"g":g,"spin_t":g+2,"residual":str(residual),
                    "ambient_integral":residual.denominator==1})
passed=all(not x["ambient_integral"] for x in records)
result={"schema":"marici.checker_results.v1",
 "checker":"magnetic_divided_power_curvature_coherence_checks.py","passed":passed,
 "source_commutator":"B_(t+1)E_t-E_(t-1)B_t=2tI",
 "divided_step":"delta_g=E_(g+2)/(g+1)",
 "comparison_residual":"2(g+2)/(g+1) I",
 "classification":{"over_Q":"typed central curvature 2-cell","ambient_over_Z":"not defined for g>=2",
 "reachable_integral_submodule":"open; requires a divisibility-and-stability theorem"},
 "decisive_falsifier":"assuming strict commutation or an ambient integral coherence cell",
 "replay":"g=2..201"}
Path(__file__).resolve().parents[1].joinpath("results/magnetic_divided_power_curvature_coherence.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if passed else 1)
