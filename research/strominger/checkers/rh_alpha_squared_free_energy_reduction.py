import json,math
from pathlib import Path
def d2(f,n):return f(n+1)+f(n-1)-2*f(n)
rows=[]
for n in (20,50,100,500,1000):
 v=d2(math.log,n);rows.append({"n":n,"d2_log_n":v,"n2_d2":n*n*v,"error_from_minus_one":n*n*v+1})
checks={"centered_log_has_minus_inverse_square":abs(rows[-1]["n2_d2"]+1)<1e-6,"error_decays":all(abs(rows[i+1]["error_from_minus_one"])<abs(rows[i]["error_from_minus_one"]) for i in range(len(rows)-1)),"constant_and_linear_terms_annihilated":all(abs(d2(lambda x:2.3*x+7,n))<1e-9 for n in (20,100,1000))}
base=Path(__file__).parents[1];packet=(base/"rh-minus-alpha-squared-is-the-centered-image-of-a-hard-edge-log-free-energy.md").read_text(encoding="utf-8")
checks.update({"packet_maps_positive_log_to_negative_square":"hard-edge term in relative Hankel free energy" in packet and "Centered differencing then gives" in packet,"packet_requires_centered_remainder":"\\Delta^2 E_n^{(\\alpha)}=o(n^{-2})" in packet,"packet_does_not_claim_derivation":"does not derive that term" in packet})
result={"schema":"marici.strominger.rh_alpha_squared_free_energy_reduction.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Centered differencing maps +alpha^2 log n in relative Hankel free energy to -alpha^2/n^2 in the relative recurrence logarithm. Proving the free-energy coefficient and centered remainder remains open.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_alpha_squared_free_energy_reduction.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
