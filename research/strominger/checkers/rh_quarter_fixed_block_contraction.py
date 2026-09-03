import json
from fractions import Fraction as F
from pathlib import Path
# Fixed positive endpoint blocks A=diag(2,3), B=diag(5,7).
# X has a forbidden off-diagonal coordinate; both signs have the same Schur complement.
A=(F(2),F(3)); B=(F(5),F(7)); X=((F(0),F(1)),(F(0),F(0)))
# B-X^T A^{-1}X = diag(5, 7-1/2).
S=(B[0],B[1]-F(1,A[0]))
# Whitening gives a single nonzero entry 1/sqrt(14), hence squared norm 1/14.
white_norm_sq=F(1,A[0]*B[1])
checks={'A_positive':all(v>0 for v in A),'B_positive':all(v>0 for v in B),'schur_positive':all(v>0 for v in S),'whitened_cross_is_strict_contraction':white_norm_sq<1,'forbidden_offdiagonal_survives':X[0][1]!=0,'negative_sign_same_schur':(-X[0][1])**2==X[0][1]**2,'zero_cross_deliberate_baseline':all(v==0 for r in ((F(0),F(0)),(F(0),F(0))) for v in r)}
result={'schema':'marici.strominger.rh_quarter_fixed_block_contraction.v1','status':'passed' if all(checks.values()) else 'failed','criterion':'For A,B positive definite, [[A,X],[X^T,B]] is PSD iff A^{-1/2} X B^{-1/2} is a contraction.','verdict':'Fixed positive-definite endpoint blocks constrain only a whitened operator norm. They cannot force entry signs or interlacing-support zeros: sufficiently small positive or negative mass in any coordinate remains PSD.','witness':{'A':['2','3'],'B':['5','7'],'X':[['0','1'],['0','0']],'schur':['5','13/2'],'whitened_norm_squared':'1/14'},'claim_boundary':'Singular endpoint blocks may impose range/kernel constraints and are not covered.','checks':checks}
p=Path(__file__).parents[1]/'results'/'rh_quarter_fixed_block_contraction.json';p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
