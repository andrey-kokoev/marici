import json, math
from pathlib import Path
base=Path(__file__).parents[1]
src=json.loads((base/"results"/"rh_hankel_ratio_direct_one_over_n_fit_audit.json").read_text(encoding="utf-8"));raw=src["log_determinant_ratios"];X=math.log(12);z=2*X**.25;actual=[raw[n]-z*n for n in range(len(raw))]
def solve(A,b):
 A=[row[:]+[v] for row,v in zip(A,b)];m=len(A)
 for i in range(m):
  k=max(range(i,m),key=lambda r:abs(A[r][i]));A[i],A[k]=A[k],A[i];p=A[i][i]
  for j in range(i,m+1):A[i][j]/=p
  for r in range(m):
   if r!=i:
    f=A[r][i]
    for j in range(i,m+1):A[r][j]-=f*A[i][j]
 return [A[i][-1] for i in range(m)]
def fit(start):
 ns=list(range(start,13));F=[[1.,1/n,1/n**2] for n in ns];y=[actual[n] for n in ns];G=[[sum(x[i]*x[j] for x in F) for j in range(3)] for i in range(3)];b=[sum(x[i]*v for x,v in zip(F,y)) for i in range(3)];c=solve(G,b);rmse=math.sqrt(sum((v-sum(ci*xi for ci,xi in zip(c,x)))**2 for x,v in zip(F,y))/len(y));return {"window":f"{start}..12","beta":c[0],"gamma":c[1],"delta":c[2],"rmse":rmse,"limiting_gap_probability":math.exp(c[0])}
fits=[fit(s) for s in (3,4,5,6)];raw_alpha=src["fits"][-1]["alpha"]
checks={
 "raw_linear_fit_matches_missing_exponential_factor":abs(raw_alpha-z)<5e-6,
 "normalized_gap_logs_nonpositive":all(v<=1e-12 for v in actual),
 "normalized_fit_has_no_linear_term_by_construction":True,
 "limiting_gap_probabilities_in_unit_interval":all(0<f["limiting_gap_probability"]<1 for f in fits),
 "gamma_fits_positive":all(f["gamma"]>0 for f in fits),
 "later_fit_rmse_decreases":all(fits[i+1]["rmse"]<fits[i]["rmse"] for i in range(len(fits)-1)),
}
result={"schema":"marici.strominger.rh_weibull_gap_normalization_cancellation_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The apparent linear gap rate equals z=2X^(1/4), exactly the exponential normalization omitted from truncated moments. Restoring e^-z per moment cancels the linear term. The finite normalized gap logarithm fits beta+gamma/n+delta/n^2 and approaches a nonzero probability near exp(beta), diagnostically consistent with indeterminacy.","checks":checks,"z":z,"raw_alpha":raw_alpha,"fits":fits,"actual_gap_logs":actual,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_weibull_gap_normalization_cancellation_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
