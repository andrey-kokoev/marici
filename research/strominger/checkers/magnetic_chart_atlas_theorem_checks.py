"""Exact arithmetic gates for the unbounded two-chart magnetic atlas theorem."""
import json, math
from pathlib import Path

records=[]
for g in range(2,402,2):
 d=math.gcd(2*g+7,3*g+7)
 primitive=((2*g+7)//d,-(3*g+7)//d)
 transverse_num=-8*(2*g+3)*(g*g-g-26)*math.factorial(2*g+1)
 transverse_den=3*(g+5)*(g+6)*(g+7)*math.factorial(g-1)
 records.append({"g":g,"content":d,"content_formula":d==math.gcd(g,7),
                 "primitive":primitive,"primitive_gcd":math.gcd(*map(abs,primitive)),
                 "transverse_nonzero":transverse_num!=0,
                 "transverse_integral_or_rational":[transverse_num,transverse_den]})
passed=all(x["content_formula"] and x["primitive_gcd"]==1 and x["transverse_nonzero"] for x in records)
result={"schema":"marici.checker_results.v1","checker":"magnetic_chart_atlas_theorem_checks.py","passed":passed,
 "theorem":{"locus":"even g>=2, q=2g+8, k=g/2+4","preferred_chart_rank":"n-1",
 "primitive_row_cocircuit":"((2g+7),-(3g+7))/gcd(g,7)","alternate_chart_rank":"n",
 "logic":"alternate full rank makes the n-1 shared rows independent; preferred replacement is proportional to shared row 0"},
 "hostile_arithmetic_fixture":{"g":14,"raw_content":7,"primitive":records[6]["primitive"]},
 "bounded_arithmetic_replay":"even g=2..400"}
Path(__file__).resolve().parents[1].joinpath("results/magnetic_chart_atlas_theorem.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if passed else 1)
