"""Exact finite diagonal fixture for phase-energy spectral successor interchange."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
def diag(x):return [[x[i] if i==j else F(0) for j in range(len(x))] for i in range(len(x))]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
a=[F(0),F(1,16),F(1,4),F(3,4),F(2)]
R=diag(a);L=diag([F(2),F(-1),F(3),F(1,2),F(4)]);PF=diag([F(1),F(1),F(1),F(0),F(0)])
thresholds=[F(1),F(1,2),F(1,8),F(1,32)]
def E(e):return diag([F(1) if x>=e else F(0) for x in a])
checks={'successor_intertwines_boundary':mm(L,R)==mm(R,L),'truncation_intertwines_boundary':mm(PF,R)==mm(R,PF),'successor_preserves_all_stages':all(mm(L,E(e))==mm(E(e),L) for e in thresholds),'truncation_preserves_all_stages':all(mm(PF,E(e))==mm(E(e),PF) for e in thresholds),'conductor_successor_interchange':mm(PF,L)==mm(L,PF),'stagewise_interchange':all(mm(PF,mm(E(e),L))==mm(L,mm(E(e),PF)) for e in thresholds)}
out={'schema':'marici.voevodsky.phase-energy-spectral-successor-interchange.v1','thresholds':[str(x) for x in thresholds],'checks':checks,'all_exact':all(checks.values()),'meaning':'Mellin multiplication successors and character truncations commute with the positive boundary multiplier and every gapless spectral stage.','scope':'Finite diagonal fixture for the exact multiplication-operator theorem; boundedness and domain certificates remain symbol-specific.'}
if __name__=='__main__':
 p=ROOT/'results'/'phase-energy-spectral-successor-interchange.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
