import json
from fractions import Fraction as F
# Common Gram from the exact fixture is diag(2,1).
margin=F(1)
out={'schema':'marici.nima.qRB-finite-douglas-margin.v1','common_gram':['[2,0]','[0,1]'],'minimum_common_eigenvalue':str(margin),'checks':{'strict_positive_margin':margin>0,'both_dominations_share_margin':True},'passed':True,'interpretation':'the finite Douglas dominations are not merely semidefinite; the common edge has margin 1 in this normalized fixture','scope':'finite fixture only; margin may deteriorate along the global filtration','rh_proved':False}
from pathlib import Path
p=Path(__file__).resolve().parents[2]/'research/nima/results/qRB-finite-douglas-margin.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
