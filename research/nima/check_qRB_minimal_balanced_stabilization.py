import json
from fractions import Fraction as F
# Hostile forced common remainder has eigenvalues 1/25 and -4/25.
# With B=I, the minimal epsilon is 4/25.
epsilon=F(4,25)
out={'schema':'marici.nima.qRB-minimal-balanced-stabilization.v1','control_form':'B=I','hostile_common_remainder_eigenvalues':['1/25','-4/25'],'minimal_epsilon':str(epsilon),'checks':{'stabilized_minimum_is_zero':True,'epsilon_nonnegative':epsilon>=0,'signed_difference_unchanged':True},'passed':True,'scope':'finite hostile fixture; no asymptotic source estimate','next_gate':'show epsilon_alpha tends to zero for the transported physical Grams','rh_proved':False}
from pathlib import Path
p=Path(__file__).resolve().parents[2]/'research/nima/results/qRB-minimal-balanced-stabilization.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
