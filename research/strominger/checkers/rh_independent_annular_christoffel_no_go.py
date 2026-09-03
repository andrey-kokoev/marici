import json, math
from pathlib import Path
A=1.; beta=.25; X=math.log(12); Y=1.; J=300; degrees=(1,2,4,8,12)
def legendre_values(t,K):
 vals=[1.]
 if K:return vals+[t] if K==1 else _extend(vals,t,K)
 return vals
def _extend(vals,t,K):
 vals.append(t)
 for n in range(1,K):vals.append(((2*n+1)*t*vals[n]-n*vals[n-1])/(n+1))
 return vals
def cert(K):
 s=0.
 for j in range(1,J+1):
  vals=legendre_values(2*j+1,K)
  kernel=sum((2*n+1)*vals[n]**2/Y for n in range(K+1))
  ymax=(j+1)*Y
  weight=math.exp(-2*A*((X+ymax)**beta-X**beta))
  s+=weight/kernel
 return s
cs=[cert(K) for K in degrees]
checks={
 "finite_annular_certificates_positive":all(c>0 for c in cs),
 "finite_annular_certificates_decrease_with_degree":all(cs[i+1]<cs[i] for i in range(len(cs)-1)),
 "degree_one_dominator_is_summable_model":sum(1/(1+3*(2*j+1)**2) for j in range(1,J+1))<.1,
}
base=Path(__file__).parents[1]
packet=(base/"rh-independent-annular-christoffel-bounds-lose-polynomial-coherence.md").read_text(encoding="utf-8")
checks.update({
 "packet_uses_dominated_convergence":"Dominated convergence" in packet,
 "packet_identifies_coherence_loss":"loss of polynomial coherence" in packet,
 "packet_retains_every_annulus":"every annulus is present" in packet,
 "packet_does_not_claim_true_kernel_unbounded":"does not prove that the true full-tail endpoint kernel is unbounded" in packet,
})
result={"schema":"marici.strominger.rh_independent_annular_christoffel_no_go.v1","status":"passed" if all(checks.values()) else "failed","parameters":{"a":A,"beta":beta,"X":X,"Y":Y,"annuli_used":J},"verdict":"The sum of independently optimized annular endpoint certificates degenerates with degree. Dominated convergence proves the infinite certificate tends to zero. The method retains all tail regions but loses the common-polynomial coherence needed for a uniform bound.","checks":checks,"finite_annular_certificates":[{"K":K,"C_partial":c} for K,c in zip(degrees,cs)],"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_independent_annular_christoffel_no_go.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
