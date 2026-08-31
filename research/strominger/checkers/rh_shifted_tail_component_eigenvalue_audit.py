import json, math, runpy
from pathlib import Path
base=Path(__file__).parent
ns=runpy.run_path(str(base/"rh_quadrature_error_generalized_eigenvalue_audit.py"))
chol,inv_lower,mm,tr,jacobi=ns["chol"],ns["inv_lower"],ns["mm"],ns["tr"],ns["jacobi"]
A=1.; B=.25; C=2.5

def moments(q,maxr=12):
 x0=math.log(q); u0=x0**B
 def simp(r,kind):
  lo,hi=u0,5.; steps=12000; h=(hi-lo)/steps
  def f(u):return 4*u**(4*r+3)*math.exp((-u**4 if kind=="suppressed" else 0)-2*u)
  s=f(lo)+f(hi)
  for k in range(1,steps):s+=(4 if k%2 else 2)*f(lo+k*h)
  return s*h/3
 Q=[]; V=[]
 for r in range(maxr+1):
  full=4*math.gamma(4*r+4)/2**(4*r+4)
  lo,hi=0.,u0; steps=3000; h=(hi-lo)/steps
  def f(u):return 4*u**(4*r+3)*math.exp(-2*u)
  s=f(lo)+f(hi)
  for k in range(1,steps):s+=(4 if k%2 else 2)*f(lo+k*h)
  Q.append(full-s*h/3); V.append(simp(r,"suppressed"))
 return x0,Q,V
def ge_max(M,Q):
 n=len(Q); d=[math.sqrt(Q[i][i]) for i in range(n)]
 Qn=[[Q[i][j]/d[i]/d[j] for j in range(n)] for i in range(n)]; Mn=[[M[i][j]/d[i]/d[j] for j in range(n)] for i in range(n)]
 Li=inv_lower(chol(Qn)); return max(jacobi(mm(mm(Li,Mn),tr(Li))))
rows=[]
tail_starts=(3,4,6,12,24,48)
for q in tail_starts:
 x0,QM,VM=moments(q)
 degrees=[]
 for K in range(7):
  n=K+1; Qm=[[QM[i+j] for j in range(n)] for i in range(n)]
  End=[[(x0**(i+j))*math.exp(-2*x0**B)/q for j in range(n)] for i in range(n)]
  Val=[[C*VM[i+j] for j in range(n)] for i in range(n)]
  Der=[[(i*j*VM[i+j-2]) if i and j else 0. for j in range(n)] for i in range(n)]
  Total=[[End[i][j]+Val[i][j]+Der[i][j] for j in range(n)] for i in range(n)]
  degrees.append({"K":K,"total_eta":ge_max(Total,Qm),"endpoint_eta":ge_max(End,Qm),"value_eta":ge_max(Val,Qm),"derivative_eta":ge_max(Der,Qm)})
 rows.append({"q":q,"analytic_value_bound":C/q,"degrees":degrees})
q3_prior=json.loads((base.parent/"results"/"rh_quadrature_error_generalized_eigenvalue_audit.json").read_text(encoding="utf-8"))["rows"]
checks={
 "q3_reproduces_prior_total_grid":all(abs(rows[0]["degrees"][k]["total_eta"]-q3_prior[k]["eta_max"])<2e-9 for k in range(7)),
 "all_component_ratios_are_nonnegative":all(v>=-1e-9 for row in rows for d in row["degrees"] for v in (d["endpoint_eta"],d["value_eta"],d["derivative_eta"])),
 "all_tested_total_ratios_are_below_one":all(d["total_eta"]<1 for row in rows for d in row["degrees"]),
 "analytic_value_bounds_decrease_with_q":all(rows[i+1]["analytic_value_bound"]<rows[i]["analytic_value_bound"] for i in range(len(rows)-1)),
 "fixed_degree_total_ratios_decrease_across_tail_starts":all(rows[i+1]["degrees"][k]["total_eta"]<rows[i]["degrees"][k]["total_eta"] for i in range(len(rows)-1) for k in range(7)),
}
result={"schema":"marici.strominger.rh_shifted_tail_component_eigenvalue_audit.v1","status":"passed" if all(checks.values()) else "failed","parameters":{"a":A,"beta":B,"tail_starts":list(tail_starts),"degrees":"0..6"},"verdict":"Shifted continuous-tail generalized eigenvalues remain below one on the tested grid. The computation separates endpoint, suppressed-value, and derivative forms for each tail start and verifies q=3 against the prior audit. Finite ratios do not select a tail or prove a uniform-degree bound; they only test whether later positive-prefix splits introduce an immediate coercivity falsifier.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base.parent/"results"/"rh_shifted_tail_component_eigenvalue_audit.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps({"schema":result["schema"],"status":result["status"],"checks":checks,"degree_six":[{"q":r["q"],**r["degrees"][-1]} for r in rows]},indent=2))
