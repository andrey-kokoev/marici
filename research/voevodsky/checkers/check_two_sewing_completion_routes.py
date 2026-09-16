"""Exact finite angular models for strong and minimal-product sewing completions."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):return sum(a[i][i] for i in range(len(a)))
def tp(a):return [list(x) for x in zip(*a)]
def hs2(a):return sum(x*x for row in a for x in row)
def sub(a,b):return [[x-y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
chars=range(6);rows=[]
for n in (1,2,4,8):
 strong_error=F(0);product_error=F(0);sewing=F(0);target=F(0)
 for chi in chars:
  q=F(1,2**(chi+1));B=[[q,F(0)],[F(0),q]];C=[[q,F(0)],[F(0),-q]]
  U=[[F(1,n+1)*q,F(0)],[F(0),F(0)]];V=[[F(0),F(0)],[F(0),F(1,n+1)*q]]
  Bn=[[B[i][j]+U[i][j] for j in range(2)] for i in range(2)];Cn=[[C[i][j]+V[i][j] for j in range(2)] for i in range(2)]
  strong_error+=hs2(U)+hs2(V)
  Zn=mm(tp(Bn),Cn);Z=mm(tp(B),C);product_error+=sum(abs(x) for row in sub(Zn,Z) for x in row)
  sewing+=tr(Zn);target+=tr(Z)
 rows.append({'regulator':n,'strong_squared_error':str(strong_error),'product_trace_norm_bound':str(product_error),'sewing':str(sewing),'target_sewing':str(target)})
# Strictness fixture B_n=n, C_n=1/n.
strict=[{'n':n,'B_norm':str(F(n)),'C_norm':str(F(1,n)),'product':str(F(1))} for n in (1,2,4,8,16)]
checks={'strong_errors_decrease':all(F(rows[i+1]['strong_squared_error'])<F(rows[i]['strong_squared_error']) for i in range(len(rows)-1)),'product_errors_decrease':all(F(rows[i+1]['product_trace_norm_bound'])<F(rows[i]['product_trace_norm_bound']) for i in range(len(rows)-1)),'sewing_converges_in_fixture':all(abs(F(r['sewing'])-F(r['target_sewing']))<=F(r['product_trace_norm_bound']) for r in rows),'minimal_product_strictness':all(F(r['product'])==1 for r in strict) and F(strict[-1]['B_norm'])>F(strict[0]['B_norm'])}
out={'schema':'marici.voevodsky.two-sewing-completion-routes.v1','strong_to_product_rows':rows,'product_without_strong_fixture':strict,'checks':checks,'all_exact':all(checks.values()),'meaning':'Strong Hilbert-Schmidt leg convergence induces trace-class product convergence, while a constant product may exist with an unbounded individual leg.','analytic_gate':'Instantiate either route for the recentered semilocal prolate/Hankel legs with a summable character majorant.'}
if __name__=='__main__':
 p=ROOT/'results'/'two-sewing-completion-routes.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
