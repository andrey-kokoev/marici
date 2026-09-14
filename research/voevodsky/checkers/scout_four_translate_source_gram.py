#!/usr/bin/env python3
"""Rank-four equally spaced source Gram scout using Cholesky pivots."""
import json,math
from pathlib import Path

def cholesky(A):
 n=len(A);L=[[0.0]*n for _ in range(n)];piv=[]
 for i in range(n):
  for j in range(i+1):
   s=sum(L[i][k]*L[j][k] for k in range(j))
   if i==j:
    q=A[i][i]-s;piv.append(q)
    if q<=0:return L,piv,False
    L[i][j]=math.sqrt(q)
   else:L[i][j]=(A[i][j]-s)/L[j][j]
 return L,piv,True
def determinant(A):
 _,p,ok=cholesky(A);return math.prod(p) if ok else float('nan')
def main():
 sigma=.005;step=.25
 deficits=json.loads((Path(__file__).parents[1]/'results'/'two_translate_weil_deficit_scout.json').read_text())
 diag=json.loads((Path(__file__).parents[1]/'results'/'two_translate_symmetric_eigenvalue_scout.json').read_text())
 k0=diag['K0'];ks=[k0]
 for m in (1,2,3):
  D=next(r['K0_minus_Kd'] for r in deficits['rows'] if r['sigma']==sigma and r['d']==m*step);ks.append(k0-D)
 G=[[ks[abs(i-j)] for j in range(4)] for i in range(4)]
 L,piv,ok=cholesky(G);assert ok
 det=math.prod(piv)
 result={'schema':'marici.voevodsky.four-translate-source-gram-scout.v1','sigma':sigma,'translate_centers':[-.375,-.125,.125,.375],'kernel_by_step':ks,'gram_matrix':G,'cholesky_pivots':piv,'determinant':det,'positive_definite_numerically':ok,'smallest_cholesky_pivot':min(piv),'certified':False,'conclusion':'The equally spaced rank-four source packet passes Sylvester positivity numerically without zero-location input.'}
 out=Path(__file__).parents[1]/'results'/'four_translate_source_gram_scout.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
