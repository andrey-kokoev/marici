#!/usr/bin/env python3
"""Exact audit: mesh-charge positivity is Weil positivity on the zero-sum subspace only."""
import json
from fractions import Fraction
from pathlib import Path

def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):return [list(x) for x in zip(*A)]
def q(A,x):return sum(x[i]*A[i][j]*x[j] for i in range(len(x)) for j in range(len(x)))
def main():
 r=Fraction(-2,5);n=4;G=[[Fraction(1) if i==j else r for j in range(n)] for i in range(n)]
 D=[[Fraction(-1) if j==i else Fraction(1) if j==i+1 else Fraction(0) for j in range(n)] for i in range(n-1)]
 C=mm(mm(D,G),tr(D))
 # Here every increment charge matrix is positive: C=(1-r) times path Laplacian Gram.
 probes=[[1,0,0],[1,-1,2],[3,2,1]];assert all(q(C,x)>0 for x in probes)
 allones=[1]*n;bad=q(G,allones);assert bad<0
 # Any increment combination D^T b has coefficient sum zero.
 b=[1,-2,3];zero= [sum(D[i][j]*b[i] for i in range(n-1)) for j in range(n)];assert sum(zero)==0 and q(G,zero)==q(C,b)
 result={'schema':'marici.voevodsky.mesh-charge-zero-sum-scope.v1','identity':'C=D G D* with C_ij=2K(i-j)-K(i-j+1)-K(i-j-1)','increment_image':'im(D*) = coefficient-zero-sum subspace','fixture':{'rank':n,'K0':'1','off_diagonal':str(r),'mesh_charge_matrix':[[str(x) for x in row] for row in C],'all_ones_Weil_value':str(bad)},'mesh_charge_positive':True,'full_Gram_positive':False,'conclusion':'Positive primitive-increment/mesh-charge observations control every zero-sum composite but can miss a negative total-mass mode. A coupled endpoint/archimedean balancing identity is required to recover full Weil positivity.'}
 out=Path(__file__).parents[1]/'results'/'mesh_charge_zero_sum_scope.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
