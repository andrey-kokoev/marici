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
def mm(X,Y):return [[sum(X[i][t]*Y[t][j] for t in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]
T=mm(inverse(A),B);negative=next(({'row':i,'column':j,'entry':str(T[i][j])} for i in range(k) for j in range(k) if T[i][j]<0),None)
U=[[F(1),F(2)],[F(0),F(3)]];V=[[F(4),F(0)],[F(5),F(6)]];control=mm(U,V)
checks={'exact_coupling':mm(A,T)==B,'negative_entry_present':negative is not None,'nonnegative_product_control':all(z>=0 for r in control for z in r)}
r={'schema':'marici.strominger.rh_quarter_endpoint_rectangular_positive_lift_obstruction.v1','status':'passed' if all(checks.values()) else 'failed','verdict':'No factorization T=UV with entrywise nonnegative rectangular U and V exists at any inner dimension, because every such product is entrywise nonnegative while T has a negative entry.','first_negative_entry':negative,'dimension_scope':'all finite inner dimensions','checks':checks};(base/'results'/'rh_quarter_endpoint_rectangular_positive_lift_obstruction.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print(json.dumps(r,indent=2))
