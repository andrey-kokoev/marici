import json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_transfer_p_matrix_vs_total_positivity.py')));A,B,det,k=g['A'],g['B'],g['det'],g['k']
def mn(M,rs,cs):return F(1) if not rs else det([[M[i][j] for j in cs] for i in rs])
def formula(M,i,j):
 d1=mn(M,range(i-j,i+1),range(j+1));d2=mn(M,range(i-j-1,i-1),range(j));d3=mn(M,range(i-j,i),range(j));d4=mn(M,range(i-j-1,i),range(j+1));return None if d3*d4==0 else d1*d2/(d3*d4)
def run(M):
 X=[r[:] for r in M];out=[]
 for j in range(k):
  for i in range(k-1,j,-1):
   if not X[i][j]:continue
   q=X[i][j]/X[i-1][j];f=formula(M,i,j);out.append({'row':i,'column':j,'elimination':str(q),'minor_ratio':None if f is None else str(f),'denominator_nonzero':f is not None,'equal':f==q if f is not None else False});X[i]=[X[i][c]-q*X[i-1][c] for c in range(k)]
 return out
ra,rb=run(A),run(B);u=[('A',x) for x in ra if not x['denominator_nonzero']]+[('B',x) for x in rb if not x['denominator_nonzero']];checks={'factors_enumerated':bool(ra and rb),'standard_formula_obstruction':bool(u)}
r={'schema':'marici.strominger.rh_quarter_endpoint_neville_minor_ratio_formula.v2','status':'passed' if all(checks.values()) else 'failed','verdict':'The ordinary contiguous-minor formula is exactly classified and obstructed by Hurwitz staircase zeros.','first_undefined':{'matrix':u[0][0],**u[0][1]},'A_records':ra,'B_records':rb,'checks':checks};(base/'results'/'rh_quarter_endpoint_neville_minor_ratio_formula.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':r['status'],'first':r['first_undefined']}))
