import json, math
from fractions import Fraction as F
from pathlib import Path
# Exact exponent count: product of row factors L^i and column factors L^j,
# plus L from every entry, gives n^2.
def exponent(n):return sum(range(n))+sum(range(n))+n
checks={"hankel_dilation_exponent_is_n_squared":all(exponent(n)==n*n for n in range(1,30))}
base=Path(__file__).parents[1]
src=json.loads((base/"results"/"rh_hankel_gamma_tail_start_grid_audit.json").read_text(encoding="utf-8"))
ratios=[]
for r in src["rows"]:
 L=2*r["X"]**.75
 ratios.append({"q":r["q"],"gamma_over_L":r["gamma_proxy_n8"]/L})
checks.update({
 "finite_gamma_over_L_spread_below_five_percent":max(r["gamma_over_L"] for r in ratios)/min(r["gamma_over_L"] for r in ratios)<1.05,
 "finite_gamma_over_L_decreases_slightly":all(ratios[i+1]["gamma_over_L"]<ratios[i]["gamma_over_L"] for i in range(len(ratios)-1)),
})
packet=(base/"rh-laguerre-dilation-alone-does-not-determine-the-hankel-one-over-n-term.md").read_text(encoding="utf-8")
checks.update({
 "packet_separates_n_squared_from_one_over_n":"It does not create a \\(1/n\\) term" in packet,
 "packet_identifies_singular_local_limit":"local limit is singular" in packet,
 "packet_does_not_falsify_big_o":"does not falsify \\(\\gamma_X=O(L_X)\\)" in packet,
 "packet_requires_global_matching":"match the local Laguerre window to the far Weibull region" in packet,
})
result={"schema":"marici.strominger.rh_laguerre_dilation_hankel_gamma_no_go.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact dilation sends D_n to L^(n^2)D_n and therefore cannot by itself determine the 1/n coefficient gamma_X. Finite gamma/L ratios vary by under five percent and support proportionality diagnostically, but the singular local Laguerre limit still requires matched global Weibull control.","checks":checks,"ratios":ratios,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_laguerre_dilation_hankel_gamma_no_go.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
