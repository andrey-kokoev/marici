"""Exact finite spectral-stage composition and interchange fixture."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def eq(a,b):return a==b
def diag(xs):return [[xs[i] if i==j else F(0) for j in range(len(xs))] for i in range(len(xs))]
def proj(vals,eta):return diag([F(1) if x>=eta else F(0) for x in vals])
vals=[F(0),F(1,8),F(1,2),F(2)]
R=diag(vals);Z=proj([F(1) if x==0 else F(0) for x in vals],F(1)) # diag indicator of zero
# Two commuting spectral maps (multipliers) provide horizontal and vertical arrows.
H=diag([F(3),F(2),F(1),F(4)]);T=diag([F(5),F(1),F(2),F(3)]);C=mm(T,H)
thresholds=[F(2),F(1,2),F(1,8)]
checks={'H_intertwines_R':eq(mm(H,R),mm(R,H)),'T_intertwines_R':eq(mm(T,R),mm(R,T)),'composite_intertwines_R':eq(mm(C,R),mm(R,C)),'radical_preserved_H':eq(mm(H,Z),mm(Z,H)),'radical_preserved_T':eq(mm(T,Z),mm(Z,T)),'spectral_stages_preserved_H':all(eq(mm(H,proj(vals,e)),mm(proj(vals,e),H)) for e in thresholds),'spectral_stages_preserved_T':all(eq(mm(T,proj(vals,e)),mm(proj(vals,e),T)) for e in thresholds),'interchange':eq(mm(T,H),mm(H,T)),'composition_associative':eq(mm(T,mm(H,Z)),mm(mm(T,H),Z))}
# Hostile off-diagonal map mixes the radical and 1/8 spectral stage.
B=[[F(1),F(1),F(0),F(0)],[F(0),F(1),F(0),F(0)],[F(0),F(0),F(1),F(0)],[F(0),F(0),F(0),F(1)]]
hostile={'intertwines_R':eq(mm(B,R),mm(R,B)),'preserves_radical':eq(mm(B,Z),mm(Z,B)),'preserves_all_stages':all(eq(mm(B,proj(vals,e)),mm(proj(vals,e),B)) for e in thresholds)}
out={'schema':'marici.voevodsky.gapless-spectral-completion-composition.v1','spectrum':[str(x) for x in vals],'thresholds':[str(x) for x in thresholds],'checks':checks,'exact_fixture_passed':all(checks.values()),'hostile_mixing_map':hostile,'hostile_refused':not all(hostile.values()),'meaning':'Exact spectral morphisms compose stagewise, preserve the radical, and satisfy interchange; a map mixing zero and positive spectral levels is refused.','next_gate':'Instantiate these certificate laws for conductor and successor maps of the phase-energy tower.'}
if __name__=='__main__':
 p=ROOT/'results'/'gapless-spectral-completion-composition.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
