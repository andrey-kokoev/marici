import json
from fractions import Fraction as F
from pathlib import Path
N=20
a=[None]+[F((n+2)**4) for n in range(N+2)]
b=[None]+[F(3*n*n+1) for n in range(1,N+1)]
def solution(u0,u1):
 u=[F(u0),F(u1)]
 for n in range(1,N):u.append((-b[n]*u[n]-a[n]*u[n-1])/a[n+1])
 return u
u=solution(1,2);v=solution(2,-1)
def W(x,y,n):return a[n+1]*(x[n]*y[n+1]-x[n+1]*y[n])
ws=[W(u,v,n) for n in range(1,N)]
model=[]
A=F(7)
for n in (10,100,1000,10000):
 f0=F(1,n);f1=F(1,n+1);g0=F(1,n*n);g1=F(1,(n+1)**2)
 w=A*(n+1)**4*(f0*g1-f1*g0);model.append({"n":n,"wronskian":float(w),"error_from_minus_A":float(w+A)})
f=[F(1,n) for n in range(1,30)];g=[F(1,n*n) for n in range(1,30)];p=[3*x+5*y for x,y in zip(f,g)]
ratios=[]
for n in range(1,28):
 def raw(x,y):return x[n-1]*y[n]-x[n]*y[n-1]
 ratios.append(raw(p,g)/raw(f,g))
checks={"jacobi_wronskian_exactly_constant":all(x==ws[0] for x in ws),"model_normalization_tends_to_minus_A":abs(model[-1]["error_from_minus_A"])<.002,"connection_ratio_recovers_three":all(x==3 for x in ratios),"basis_wronskian_nonzero":ws[0]!=0}
base=Path(__file__).parents[1];packet=(base/"rh-hard-edge-connection-coefficient-is-a-discrete-wronskian.md").read_text(encoding="utf-8")
checks.update({"packet_states_nonvanishing_gate":"\\mathcal W(P,G)\\ne0" in packet,"packet_preserves_asymptotic_existence_gate":"requires a discrete asymptotic theorem" in packet})
result={"schema":"marici.strominger.rh_discrete_wronskian_connection_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The Jacobi-weighted discrete Wronskian is exactly index-independent, its n^-1/n^-2 model normalization tends to -A0 for a_n~A0 n^4, and the Wronskian quotient recovers the p=-1 connection coefficient. Nonvanishing remains a separate minimal-solution separation problem.","checks":checks,"constant_wronskian":str(ws[0]),"model_rows":model,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_discrete_wronskian_connection_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
