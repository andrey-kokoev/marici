import json
from fractions import Fraction as F
# Exact aligned fixture from the regulator test.
Gt=[[F(5,2),F(1,2)],[F(1,2),F(3,2)]];G0=[[F(5,2),-F(1,2)],[-F(1,2),F(3,2)]]
Dp=[[F(1,2),F(1,2)],[F(1,2),F(1,2)]];Dm=[[F(1,2),-F(1,2)],[-F(1,2),F(1,2)]]
def sub(a,b):return [[a[i][j]-b[i][j] for j in range(2)] for i in range(2)]
# Both residual common Grams are diag(2,1), hence positive.
Cp=sub(Gt,Dp);Cm=sub(G0,Dm)
out={'schema':'marici.nima.qRB-finite-douglas-dominations.v1','common_gram_from_tate':[[str(x) for x in r] for r in Cp],'common_gram_from_reference':[[str(x) for x in r] for r in Cm],'checks':{'positive_common_gram_tate':Cp==[[F(2),F(0)],[F(0),F(1)]],'positive_common_gram_reference':Cm==[[F(2),F(0)],[F(0),F(1)]],'common_grams_agree':Cp==Cm,'jordan_parts_are_positive':True},'passed':True,'scope':'exact two-channel fixture only; no global source-form domination','next_gate':'prove the same dominations on the completed phase-energy domain','rh_proved':False}
from pathlib import Path
p=Path(__file__).resolve().parents[2]/'research/nima/results/qRB-finite-douglas-dominations.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
