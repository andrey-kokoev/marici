import json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_transfer_p_matrix_vs_total_positivity.py')));A,B,k=g['A'],g['B'],g['k']
def eye():return [[F(i==j) for j in range(k)] for i in range(k)]
def mm(X,Y):return [[sum(X[i][t]*Y[t][j] for t in range(k)) for j in range(k)] for i in range(k)]
def nev(X):
 M=[r[:] for r in X];fs=[];fail=None
 for j in range(k):
  for i in range(k-1,j,-1):
   if not M[i][j]:continue
   if not M[i-1][j]:return M,fs,{'row':i,'column':j,'reason':'zero pivot'}
   q=M[i][j]/M[i-1][j]
   if q<0:return M,fs,{'row':i,'column':j,'reason':'negative multiplier'}
   L=eye();L[i][i-1]=q;fs.append(L);M[i]=[M[i][c]-q*M[i-1][c] for c in range(k)]
 P=eye()
 for L in fs:P=mm(P,L)
 if mm(P,M)!=X:fail={'reason':'reconstruction'}
 return M,fs,fail
def rep(X):
 U,fs,f=nev(X);return {'factor_count':len(fs),'failure':f,'upper_remainder_nonnegative':all(z>=0 for r in U for z in r)}
ra,rb=rep(A),rep(B);checks={'A_exact':ra['failure'] is None and ra['upper_remainder_nonnegative'],'B_exact':rb['failure'] is None and rb['upper_remainder_nonnegative']}
r={'schema':'marici.strominger.rh_quarter_endpoint_hurwitz_neville_factorization.v2','status':'passed' if all(checks.values()) else 'failed','verdict':'Bounded positive Neville factorization backend regenerated under one Hall programme DPC boundary.','A':ra,'B':rb,'checks':checks};(base/'results'/'rh_quarter_endpoint_hurwitz_neville_factorization.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
