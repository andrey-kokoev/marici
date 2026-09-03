import json,math
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];src=json.loads((base/"results"/"rh_quarter_four_staircase_cross_ratio_grid.json").read_text(encoding="utf-8"));q0=F(105,32);target=F(208,1575);rows=[]
for r in src["rows"]:
 n=r["n"];m=n-1;qm=(m+1)*(m+F(5,4))*(m+F(3,2))*(m+F(7,4));R=r["theta"]*float(qm/q0);P=2*R/((m+1)*(m+2))
 rows.append({"m":m,"renormalized_product":P,"error_from_208_1575":P-float(target)})
late=rows[-8:]
checks={"source_grid_passed":src["status"]=="passed","reference_product_exact":all(__import__('math').prod(F(j+2,j) for j in range(1,m+1))==F((m+1)*(m+2),2) for m in range(1,10)),"target_double_amplitude_exact":2*F(104,1575)==target,"partial_products_positive":all(r["renormalized_product"]>0 for r in rows),"late_errors_decrease":all(abs(late[i+1]["error_from_208_1575"])<abs(late[i]["error_from_208_1575"]) for i in range(len(late)-1))}
result={"schema":"marici.strominger.rh_quarter_renormalized_pivot_product.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Factoring the exact reference product prod(1+2/j)=(m+1)(m+2)/2 converts C=104/1575 into the convergent-product target prod rho_j=208/1575. Exact-grid partial products move toward the target but do not evaluate it.","checks":checks,"target":str(target),"late_rows":late,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_quarter_renormalized_pivot_product.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
