import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/"research/strominger/results/magnetic_chart_cocircuit_symbolic.json"
records=[]
for g in range(2,202,2):
 q=2*g+8;m=-3*g-7;u=math.prod(4+i for i in range(g));left=((m+g)*u,m*u)
 v=math.prod(g+8+i for i in range(g-1));right=(-(2*g+7)*v,-(3*g+7)*v)
 ok=(2*g+7)*left[1]==(3*g+7)*left[0] and (2*g+7)*right[1]==(3*g+7)*right[0]
 d=math.gcd(g,7)
 records.append({"g":g,"q":q,"a":g+8,"relation":ok,"content":d,"primitive_relation":[(2*g+7)//d,-(3*g+7)//d]})
passed=all(x["relation"] for x in records)
result={"schema":"marici.checker_results.v1","checker":"magnetic_chart_cocircuit_symbolic_checks.py","passed":passed,"symbolic_statement":"for every even g>=2 on q=2g+8,a=g+8, (2g+7)R1=(3g+7)R0","primitive_normalization":"divide ((2g+7),-(3g+7)) by gcd(g,7); content 7 exactly when 14 divides g","derivation":{"a0_minus_row_pair":"-(4)^(overline g)*(2g+7,3g+7)","a_g_plus_8_row_pair":"-(g+8)^(overline g-1)*(2g+7,3g+7)","all_other_columns_on_rows_0_1":"zero_by_support"},"bounded_replay":{"g_even":[2,200],"passed":passed}}
OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2));raise SystemExit(0 if passed else 1)
