"""Exact finite-packet operator-valued quantile gate for hard bulk projection."""
import json,sys
from pathlib import Path
try:
 import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
half=s.Rational(1,2)
# Three ordered near-one edge bins; 1-exp(-x)=1/2 in this exact algebraic fixture.
# Factorized law: every bin is a scalar multiple of one observer Gram G.
G=s.Matrix([[2,1],[1,2]]);factor_weights=[G,2*G,G]
soft_factor=sum((half*M for M in factor_weights),s.zeros(2))
tails_factor=[sum(factor_weights[j:],s.zeros(2)) for j in range(1,4)]
# Tail after the middle bin has weight G, while soft mass is 2G: choose profile [G,2G,G]
# gives no equality; calibrated profile below [G,G] gives equality and demonstrates sufficiency.
cal_weights=[G,G];soft_cal=sum((half*M for M in cal_weights),s.zeros(2));tail_cal=cal_weights[1]
# Nonfactorized two-observer law with incompatible unique cuts.
weights=[s.diag(1,0),s.diag(1,1),s.diag(0,1)]
soft=sum((half*M for M in weights),s.zeros(2))
tails=[sum(weights[j:],s.zeros(2)) for j in range(1,4)]
residuals=[s.simplify(T-soft) for T in tails]
checks={'factorized_calibrated_quantile':tail_cal==soft_cal,'calibrated_gram_positive':G.is_positive_definite,'nonfactorized_soft_mass_identity':soft==s.eye(2),'first_observer_prefers_cut_one':residuals[0][0,0]==0 and residuals[1][0,0]!=0,'second_observer_prefers_cut_two':residuals[1][1,1]==0 and residuals[0][1,1]!=0,'no_common_hard_threshold':all(R!=s.zeros(2) for R in residuals)}
out={'schema':'marici.voevodsky.operator-valued-hard-bulk-quantile.v1','calibrated_factorized_soft':[[str(x) for x in row] for row in soft_cal.tolist()],'calibrated_factorized_tail':[[str(x) for x in row] for row in tail_cal.tolist()],'nonfactorized_soft':[[str(x) for x in row] for row in soft.tolist()],'nonfactorized_tail_residuals':[[[int(x) for x in row] for row in R.tolist()] for R in residuals],'checks':{k:bool(v) for k,v in checks.items()},'all_exact':all(bool(v) for v in checks.values()),'conclusion':'A factorized edge law admits one calibrated hard retraction, while incompatible observer profiles prohibit a universal hard bulk projection.','program_effect':'Retain the strictly coherent soft dyadic tower as the canonical physical positive object until the semilocal operator-valued edge law passes the quantile gate.'}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'operator-valued-hard-bulk-quantile.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
