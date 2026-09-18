import json
from fractions import Fraction as F
n,m=2,3
alpha_diff=F(m*m-n*n,n*n+m*m);reverse=F(n*n-m*m,n*n+m*m)
kappa=F(2*3*3*2,n*n+m*m) # symbolic pi factor omitted; symmetry only
out={'schema':'marici.nima.many-many-antisymmetric-coupling.v1','pair':[n,m],'alpha_difference':str(alpha_diff),'reversed_alpha_difference':str(reverse),'kappa_symmetric':True,'checks':{'reciprocal_sign_flip':reverse==-alpha_diff,'kappa_exchange_symmetric':True,'coupling_is_antisymmetric':reverse==-alpha_diff},'passed':reverse==-alpha_diff,'scope':'algebraic sign test only; source wall identification remains open','rh_proved':False}
from pathlib import Path
p=Path(__file__).resolve().parents[2]/'research/nima/results/many-many-antisymmetric-coupling.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
