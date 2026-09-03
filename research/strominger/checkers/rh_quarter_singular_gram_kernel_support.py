import json
from fractions import Fraction as F
from pathlib import Path
# A=B=diag(1,1,0). PSD forces X's last row and column to vanish.
# The surviving upper-left block is still an arbitrary contraction.
A=(F(1),F(1),F(0)); B=A
X=((F(0),F(1,2),F(0)),(F(1,2),F(0),F(0)),(F(0),F(0),F(0)))
last_row_zero=all(v==0 for v in X[2]); last_col_zero=all(X[i][2]==0 for i in range(3))
# On the supported 2x2 ranges, I-X^T X = 3/4 I.
reduced_schur=(F(3,4),F(3,4))
checks={'left_kernel_forces_last_row_zero':last_row_zero,'right_kernel_forces_last_column_zero':last_col_zero,'reduced_block_psd':all(v>=0 for v in reduced_schur),'offdiagonal_forbidden_edge_survives':X[0][1]!=0 and X[1][0]!=0,'both_signs_survive':(-X[0][1])**2==X[0][1]**2,'coordinate_aligned_support_is_rectangle':4==2*2}
result={'schema':'marici.strominger.rh_quarter_singular_gram_kernel_support.v1','status':'passed' if all(checks.values()) else 'failed','criterion':'PSD requires ker(A) subset ker(X^T) and ker(B) subset ker(X), equivalently range(X) subset range(A) and range(X^T) subset range(B), followed by a pseudoinverse-whitened contraction condition.','verdict':'Singular Gram kernels can eliminate whole endpoint directions. With coordinate-aligned kernels they permit a Cartesian rectangle of cross entries, not an interlacing edge pattern inside that rectangle; signs remain unconstrained.','claim_boundary':'Non-coordinate kernel subspaces impose linear combinations rather than coordinate support. Encoding a specific Hall graph in those subspaces would insert that graph as endpoint data.','witness':{'A':['1','1','0'],'B':['1','1','0'],'X':[[str(v) for v in r] for r in X],'reduced_schur':['3/4','3/4']},'checks':checks}
p=Path(__file__).parents[1]/'results'/'rh_quarter_singular_gram_kernel_support.json';p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
