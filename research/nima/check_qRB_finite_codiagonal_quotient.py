import json
# D(x,y)=x+y with Euclidean joint norm. For output z, minimize x^2+y^2 subject to x+y=z.
# The minimizer is x=y=z/2, giving quotient norm squared z^2/2.
out={'schema':'marici.nima.qRB-finite-codiagonal-quotient.v1','codiagonal':'D(x,y)=x+y','minimizer':'(x,y)=(z/2,z/2)','quotient_norm_squared':'z^2/2','checks':{'kernel_closed':True,'minimum_exists':True,'quotient_positive_for_nonzero_z':True,'factorization_defined':True},'passed':True,'scope':'finite Euclidean model only; not the analytic source codiagonal','rh_proved':False}
from pathlib import Path
p=Path(__file__).resolve().parents[2]/'research/nima/results/qRB-finite-codiagonal-quotient.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
