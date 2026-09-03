import json
from fractions import Fraction as F
from pathlib import Path
X=((F(1),F(2)),(F(0),F(1)))
lam=sum(abs(v) for r in X for v in r)
sumsq=sum(v*v for r in X for v in r)
# Schur complement lambda I-X^T X/lambda for the exact witness.
xtx=((F(1),F(2)),(F(2),F(5)))
S=((lam-xtx[0][0]/lam,-xtx[0][1]/lam),(-xtx[1][0]/lam,lam-xtx[1][1]/lam))
detS=S[0][0]*S[1][1]-S[0][1]*S[1][0]
# At lambda=1 the same Schur complement has negative determinant.
bad=((F(0),F(-2)),(F(-2),F(-4))); bad_det=bad[0][0]*bad[1][1]-bad[0][1]*bad[1][0]
checks={'l1_dominates_spectral_via_frobenius':lam*lam>=sumsq,'scaled_schur_first_pivot_positive':S[0][0]>0,'scaled_schur_determinant_positive':detS>0,'deliberate_small_lambda_obstruction_nonzero':bad_det<0,'lambda_exact':lam==4}
result={'schema':'marici.strominger.rh_quarter_gram_embeddability_vacuity.v1','status':'passed' if all(checks.values()) else 'failed','theorem':'For every finite real matrix X, the symmetric block matrix [[lambda I,X],[X^T,lambda I]] is positive semidefinite whenever lambda is at least the spectral norm of X. Choosing lambda=sum_ij |X_ij| always suffices.','consequence':'If endpoint Gram blocks may be scaled freely, every finite coupling and every non-Hall matrix has a PSD Gram embedding; PSD embeddability imposes no sign, margin, or support restriction.','witness':{'X':[[str(v) for v in r] for r in X],'lambda':str(lam),'schur':[[str(v) for v in r] for r in S],'schur_determinant':str(detS),'small_lambda_obstruction':str(bad_det)},'checks':checks}
p=Path(__file__).parents[1]/'results'/'rh_quarter_gram_embeddability_vacuity.json';p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
