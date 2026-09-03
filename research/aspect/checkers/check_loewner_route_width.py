"""Exact Loewner certificates for torsor omitted-route widths."""
from fractions import Fraction as F
from pathlib import Path
import json

def outer(r):return [[r[i]*r[j] for j in range(2)] for i in range(2)]
def sub(a,b):return [[a[i][j]-b[i][j] for j in range(2)] for i in range(2)]
def psd2(a):return a[0][0]>=0 and a[1][1]>=0 and a[0][0]*a[1][1]-a[0][1]*a[1][0]>=0
I=[[F(1),0],[0,F(1)]]
strict_r=[F(1,2),F(1,2)]; strict_g2=F(1,2); strict_slack=sub([[strict_g2,0],[0,strict_g2]],outer(strict_r))
term_r=[F(3,5),F(4,5)]; term_g2=F(1); term_slack=sub(I,outer(term_r))
column_max=max(x*x for x in term_r)
checks={"strict_loewner_slack_psd":psd2(strict_slack),"strict_width_squared_exact":sum(x*x for x in strict_r)==strict_g2,"terminal_loewner_slack_psd":psd2(term_slack),"columnwise_bounds_miss_unit_mixed_route":column_max<1 and sum(x*x for x in term_r)==1}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"strict_gamma_squared":str(strict_g2),"terminal_gamma_squared":str(term_g2),"terminal_column_max_squared":str(column_max),"conclusion":"R*R <= gamma^2 H is a basis-free width certificate; separate column bounds can miss the unit mixed direction"}
out=Path("research/aspect/results/loewner_route_width.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
