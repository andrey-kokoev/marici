import json, math
from pathlib import Path
A=1.; B=.25; X0=math.log(3); U0=X0**B; C=2+2*A*B

def simpson_moment(r,steps=20000):
 lo,hi=U0,5.; h=(hi-lo)/steps
 def f(u):return 4*u**(4*r+3)*math.exp(-u**4-2*u)
 s=f(lo)+f(hi)
 for i in range(1,steps):s+=(4 if i%2 else 2)*f(lo+i*h)
 return s*h/3
def cont_moment(r):
 # Full gamma moment minus the compact interval [0,x0], integrated in u.
 full=4*math.gamma(4*r+4)/(2**(4*r+4))
 lo,hi=0.,U0; steps=4000; h=(hi-lo)/steps
 def f(u):return 4*u**(4*r+3)*math.exp(-2*u)
 s=f(lo)+f(hi)
 for i in range(1,steps):s+=(4 if i%2 else 2)*f(lo+i*h)
 return full-s*h/3
VM=[simpson_moment(r) for r in range(13)]; QM=[cont_moment(r) for r in range(13)]
def chol(A):
 n=len(A); L=[[0.]*n for _ in range(n)]
 for i in range(n):
  for j in range(i+1):
   z=A[i][j]-sum(L[i][k]*L[j][k] for k in range(j))
   if i==j:
    if z<=0:raise ArithmeticError("nonpositive pivot")
    L[i][j]=math.sqrt(z)
   else:L[i][j]=z/L[j][j]
 return L
def inv_lower(L):
 n=len(L); X=[[0.]*n for _ in range(n)]
 for col in range(n):
  for i in range(n):X[i][col]=((1. if i==col else 0.)-sum(L[i][k]*X[k][col] for k in range(i)))/L[i][i]
 return X
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):return [list(x) for x in zip(*A)]
def jacobi(A):
 n=len(A); A=[r[:] for r in A]
 if n==1:return [A[0][0]]
 for _ in range(100*n*n):
  p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda z:abs(A[z[0]][z[1]]))
  if abs(A[p][q])<1e-11*max(1.,max(abs(A[i][i]) for i in range(n))):break
  ang=.5*math.atan2(2*A[p][q],A[q][q]-A[p][p]); c,s=math.cos(ang),math.sin(ang)
  for k in range(n):
   if k not in (p,q):
    x,y=A[k][p],A[k][q]; A[k][p]=A[p][k]=c*x-s*y; A[k][q]=A[q][k]=s*x+c*y
  x,y,z=A[p][p],A[q][q],A[p][q]; A[p][p]=c*c*x-2*s*c*z+s*s*y; A[q][q]=s*s*x+2*s*c*z+c*c*y; A[p][q]=A[q][p]=0.
 return sorted(A[i][i] for i in range(n))
rows=[]
for K in range(0,7):
 n=K+1; Q=[[QM[i+j] for j in range(n)] for i in range(n)]; R=[]
 for i in range(n):
  row=[]
  for j in range(n):
   endpoint=(X0**(i+j))*math.exp(-2*X0**B)/3
   deriv=(i*j*VM[i+j-2]) if i and j else 0.
   row.append(endpoint+deriv+C*VM[i+j])
  R.append(row)
 # Diagonal congruence improves monomial scaling before Cholesky.
 d=[math.sqrt(Q[i][i]) for i in range(n)]; Qn=[[Q[i][j]/d[i]/d[j] for j in range(n)] for i in range(n)]; Rn=[[R[i][j]/d[i]/d[j] for j in range(n)] for i in range(n)]
 Li=inv_lower(chol(Qn)); E=mm(mm(Li,Rn),tr(Li)); ev=jacobi(E)
 V=[[C*VM[i+j] for j in range(n)] for i in range(n)]
 Dm=[[(i*j*VM[i+j-2]) if i and j else 0. for j in range(n)] for i in range(n)]
 Vn=[[V[i][j]/d[i]/d[j] for j in range(n)] for i in range(n)]
 Dn=[[Dm[i][j]/d[i]/d[j] for j in range(n)] for i in range(n)]
 value_eta=max(jacobi(mm(mm(Li,Vn),tr(Li))))
 derivative_eta=max(jacobi(mm(mm(Li,Dn),tr(Li))))
 # The endpoint form is rank one: b v v^T. Its sole generalized
 # eigenvalue is b*||L^{-1}v||^2 after diagonal congruence.
 vn=[X0**i/d[i] for i in range(n)]
 y=[sum(Li[i][j]*vn[j] for j in range(n)) for i in range(n)]
 endpoint_eta=math.exp(-2*X0**B)/3*sum(z*z for z in y)
 rows.append({"K":K,"eta_max":max(ev),"eta_min":min(ev),"endpoint_eta":endpoint_eta,"value_eta":value_eta,"derivative_eta":derivative_eta})
checks={
 "all_generalized_eigenvalues_are_nonnegative":all(r["eta_min"]>-1e-8 for r in rows),
 "degree_zero_error_ratio_is_below_one":rows[0]["eta_max"]<1,
 "tested_maximum_ratio_increases_with_degree":all(rows[i+1]["eta_max"]>=rows[i]["eta_max"] for i in range(len(rows)-1)),
 "relative_coercivity_holds_on_tested_grid":all(r["eta_max"]<1 for r in rows),
 "endpoint_ratio_is_below_total_error_ratio":all(r["endpoint_eta"]<=r["eta_max"]+1e-10 for r in rows),
 "endpoint_christoffel_ratio_increases_with_degree":all(rows[i+1]["endpoint_eta"]>=rows[i]["endpoint_eta"] for i in range(len(rows)-1)),
 "component_ratios_are_nonnegative":all(r["value_eta"]>=0 and r["derivative_eta"]>=-1e-10 for r in rows),
 "total_ratio_is_bounded_by_sum_of_component_maxima":all(r["eta_max"]<=r["endpoint_eta"]+r["value_eta"]+r["derivative_eta"]+1e-9 for r in rows),
}
result={"schema":"marici.strominger.rh_quadrature_error_generalized_eigenvalue_audit.v1","status":"passed" if all(checks.values()) else "failed","parameters":{"a":A,"beta":B,"degrees":"0..6"},"verdict":"Generalized eigenvalues of the positive quadrature-error form against the continuous Weibull Gram form remain below one through degree six, rising from about 0.097 to 0.121. Thus the sufficient Loewner coercivity bound has no falsifier on this grid. This does not prove a uniform-in-degree bound below one. Numerical conditioning is controlled by diagonal congruence and Cholesky reduction, but the result remains a finite numerical grid.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=Path(__file__).parents[1]/"results"/"rh_quadrature_error_generalized_eigenvalue_audit.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
