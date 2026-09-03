import contextlib,io,itertools,json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1]
with contextlib.redirect_stdout(io.StringIO()):
 g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_transfer_p_matrix_vs_total_positivity.py')))
A,B,det,k=g['A'],g['B'],g['det'],g['k']
def inverse(M):
 X=[M[i][:]+[F(i==j) for j in range(k)] for i in range(k)]
 for c in range(k):
  p=next(i for i in range(c,k) if X[i][c])
  X[c],X[p]=X[p],X[c];q=X[c][c];X[c]=[z/q for z in X[c]]
  for i in range(k):
   if i!=c:
    q=X[i][c];X[i]=[X[i][j]-q*X[c][j] for j in range(2*k)]
 return [r[k:] for r in X]
def mm(X,Y):return [[sum(X[i][t]*Y[t][j] for t in range(k)) for j in range(k)] for i in range(k)]
def first_negative(M):
 count=0
 for r in range(1,k+1):
  for R in itertools.combinations(range(k),r):
   for C in itertools.combinations(range(k),r):
    z=det([[M[i][j] for j in C] for i in R]);count+=1
    if z<0:return count,{'size':r,'rows':R,'columns':C,'determinant':str(z)}
 return count,None
T=mm(inverse(A),B);checked,first=first_negative(T);control=first_negative([[F(i==j) for j in range(k)] for i in range(k)])[1]
checks={'exact_coupling_identity':mm(A,T)==B,'direct_coupling_obstructed':first is not None,'identity_control_nonnegative':control is None}
result={'schema':'marici.strominger.rh_quarter_endpoint_direct_coupling_obstruction.v1','status':'passed' if all(checks.values()) else 'failed','verdict':'The direct exact endpoint coupling A^{-1}B is not totally nonnegative, so independent positive endpoint factorizations do not compose through this fixed-order coupling.','matrix_size':k,'minors_checked_through_first_negative':checked,'first_negative_minor':first,'checks':checks}
(base/'results'/'rh_quarter_endpoint_direct_coupling_obstruction.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
