import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1]
with contextlib.redirect_stdout(io.StringIO()):
 g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_transfer_p_matrix_vs_total_positivity.py')))
A,B,k=g['A'],g['B'],g['k']
def inverse(M):
 X=[M[i][:]+[F(i==j) for j in range(k)] for i in range(k)]
 for c in range(k):
  p=next(i for i in range(c,k) if X[i][c]);X[c],X[p]=X[p],X[c];q=X[c][c];X[c]=[z/q for z in X[c]]
  for i in range(k):
   if i!=c:
    q=X[i][c];X[i]=[X[i][j]-q*X[c][j] for j in range(2*k)]
 return [r[k:] for r in X]
def mm(X,Y):return [[sum(X[i][t]*Y[t][j] for t in range(k)) for j in range(k)] for i in range(k)]
T=mm(inverse(A),B);rs=[None]*k;cs=[None]*k;rs[0]=1;changed=True
while changed:
 changed=False
 for i in range(k):
  for j in range(k):
   if not T[i][j]:continue
   s=1 if T[i][j]>0 else -1
   if rs[i] is not None and cs[j] is None:cs[j]=rs[i]*s;changed=True
   elif cs[j] is not None and rs[i] is None:rs[i]=cs[j]*s;changed=True
for i in range(k):
 if rs[i] is None:rs[i]=1
for j in range(k):
 if cs[j] is None:cs[j]=1
bad=next(({'row':i,'column':j,'entry':str(T[i][j]),'required_sign':1 if T[i][j]>0 else -1,'assigned_product':rs[i]*cs[j]} for i in range(k) for j in range(k) if T[i][j] and rs[i]*cs[j]!=(1 if T[i][j]>0 else -1)),None)
checks={'exact_coupling':mm(A,T)==B,'sign_gauge_obstructed':bad is not None,'permutations_do_not_change_signability':'row and column permutations only relabel the bipartite sign graph'}
r={'schema':'marici.strominger.rh_quarter_endpoint_sign_gauge_obstruction.v1','status':'passed' if checks['exact_coupling'] and checks['sign_gauge_obstructed'] else 'failed','verdict':'No independent diagonal row/column sign gauge, even with row/column permutations, makes the direct coupling entrywise nonnegative.','matrix_size':k,'first_sign_cycle_inconsistency':bad,'checks':checks};(base/'results'/'rh_quarter_endpoint_sign_gauge_obstruction.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print(json.dumps(r,indent=2))
