import json
from fractions import Fraction as F
k0=F(493,231);ka=-F(289,462)
det=k0*k0-ka*ka
out={'schema':'marici.nima.qRB-rank-two-toeplitz-witness.v1','K0':str(k0),'Kdelta':str(ka),'determinant':str(det),'checks':{'diagonal_positive':k0>0,'rank_two_psd':det>=0,'nonzero_character_is_signed':ka<0},'passed':det>=0,'scope':'one existing smoothed witness only; no all-character positivity','rh_proved':False}
from pathlib import Path
p=Path(__file__).resolve().parents[2]/'research/nima/results/qRB-rank-two-toeplitz-witness.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
