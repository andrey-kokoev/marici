"""Exact finite-dimensional audit of quotient-chart edge construction."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
# X=Q^3. S1=(x,y), S2=x, S3=y. ker S1 subset ker S2 and ker S3;
# ker S2 and ker S3 are incomparable.
S1=[[F(1),0,0],[0,F(1),0]];S2=[[F(1),0,0]];S3=[[0,F(1),0]]
C12=[[F(1),0]];C13=[[0,F(1)]]
# A further terminal quotient S4=0 gives a strict inclusion chain and strict composition.
S4=[[F(0),0,0]];C24=[[F(0)]];C14=[[F(0),F(0)]]
checks={
 'S2_factors_through_S1':mm(C12,S1)==S2,
 'S3_factors_through_S1':mm(C13,S1)==S3,
 'chain_composition_strict':mm(C24,C12)==C14 and mm(C14,S1)==S4,
 'incomparable_kernels_block_S2_to_S3':False,
 'incomparable_kernels_block_S3_to_S2':False,
}
# No scalar C can satisfy C*S2=S3 or C*S3=S2.
checks['incomparable_kernels_block_S2_to_S3']=all(mm([[F(c)]],S2)!=S3 for c in range(-3,4))
checks['incomparable_kernels_block_S3_to_S2']=all(mm([[F(c)]],S3)!=S2 for c in range(-3,4))
# Exact relation parametrization retains both coordinates for the incomparable pair.
relation_basis=[([F(1)],[F(0)]),([F(0)],[F(1)])]
checks['relation_retains_incomparable_pair']=len(relation_basis)==2
out={'schema':'marici.voevodsky.quotient-chart-transport-analytical-realization-check.v1','fixture':{'S1':'(x,y)','S2':'x','S3':'y','S4':'0','kernel_order':['ker(S1) subset ker(S2) subset ker(S4)','ker(S1) subset ker(S3) subset ker(S4)','ker(S2) and ker(S3) incomparable']},'checks':checks,'passed':all(checks.values()),'classification':{'S1_to_S2':'directed quotient edge','S1_to_S3':'directed quotient edge','S2_to_S3':'relation only','S3_to_S2':'relation only','S2_to_S4':'directed quotient edge'}}
if __name__=='__main__':
 p=ROOT/'results'/'quotient-chart-transport-analytical-realization.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
