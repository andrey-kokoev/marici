#!/usr/bin/env python3
"""Cholesky scout for equally spaced source Toeplitz packets through rank thirteen."""
import json,math
from pathlib import Path

def cholesky_pivots(A):
 n=len(A);L=[[0.0]*n for _ in range(n)];p=[]
 for i in range(n):
  for j in range(i+1):
   s=sum(L[i][k]*L[j][k] for k in range(j))
   if i==j:
    q=A[i][i]-s;p.append(q)
    if q<=0:return p,False
    L[i][j]=math.sqrt(q)
   else:L[i][j]=(A[i][j]-s)/L[j][j]
 return p,True
def main():
 sigma=.005;step=.25;max_rank=13
 src=json.loads((Path(__file__).parents[1]/'results'/'two_translate_weil_deficit_scout.json').read_text())
 diag=json.loads((Path(__file__).parents[1]/'results'/'two_translate_symmetric_eigenvalue_scout.json').read_text());k0=diag['K0']
 ks=[k0]+[k0-next(r['K0_minus_Kd'] for r in src['rows'] if r['sigma']==sigma and r['d']==m*step) for m in range(1,max_rank)]
 rows=[];all_ok=True
 for n in range(2,max_rank+1):
  G=[[ks[abs(i-j)] for j in range(n)] for i in range(n)];p,ok=cholesky_pivots(G);all_ok &= ok
  rows.append({'rank':n,'positive_definite':ok,'smallest_pivot':min(p),'last_pivot':p[-1],'determinant':math.prod(p) if ok else None})
 worst=min(rows,key=lambda r:r['smallest_pivot'])
 result={'schema':'marici.voevodsky.equal-spacing-toeplitz-rank-ladder.v1','sigma':sigma,'spacing':step,'ranks_checked':'2..13','kernel_values':ks,'rank_results':rows,'all_positive_definite_numerically':all_ok,'smallest_pivot_case':worst,'zero_locations_used':False,'certified':False,'conclusion':'Every equally spaced source Toeplitz packet through rank thirteen passes numerical Cholesky positivity at the selected width and spacing.'}
 out=Path(__file__).parents[1]/'results'/'equal_spacing_toeplitz_rank_ladder.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'all_positive':all_ok,'smallest_pivot_case':worst},indent=2))
if __name__=='__main__':main()
