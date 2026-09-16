"""Exact rational acceptance test for the global common-subfeature Douglas gate."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
def add(a,b):return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def sub(a,b):return [[x-y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def scale(c,a):return [[c*x for x in r] for r in a]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def det(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def psd(a):return a[0][0]>=0 and a[1][1]>=0 and det(a)>=0
def enc(a):return [[str(x) for x in r] for r in a]
I=[[F(1),F(0)],[F(0),F(1)]]
# Rational hostile: projections onto e1 and the rational unit vector (3/5,4/5).
Gt=[[F(1),F(0)],[F(0),F(0)]];G0=[[F(9,25),F(12,25)],[F(12,25),F(16,25)]];D=sub(Gt,G0)
# D is traceless and D^2=(4/5)^2 I, hence |D|=(4/5)I exactly.
absD=scale(F(4,5),I);Dp=scale(F(1,2),add(absD,D));Dm=scale(F(1,2),sub(absD,D));C=sub(Gt,Dp)
# Common coercive repair preserves D and makes the forced common edge positive.
Gt1=add(I,Gt);G01=add(I,G0);C1=sub(Gt1,Dp)
checks={'input_grams_positive':psd(Gt) and psd(G0),'exact_alignment':sub(Gt,G0)==D,'absolute_value_identity':mm(D,D)==scale(F(16,25),I),'jordan_parts_positive':psd(Dp) and psd(Dm),'hostile_douglas_gate_fails':not psd(C),'two_orientations_same_remainder':sub(Gt,Dp)==sub(G0,Dm),'coercive_repair_passes':psd(C1),'repair_preserves_alignment':sub(Gt1,G01)==D}
out={'schema':'marici.voevodsky.global-common-subfeature-douglas-gate.v1','hostile':{'G_T':enc(Gt),'G_0':enc(G0),'D':enc(D),'D_plus':enc(Dp),'D_minus':enc(Dm),'forced_common_remainder':enc(C)},'coercive_repair':{'G_T':enc(Gt1),'G_0':enc(G01),'forced_common_remainder':enc(C1)},'checks':checks,'passed':all(checks.values()),'acceptance_rule':'Given globally aligned Grams, compute D=G_T-G_0 and C=G_T-D_+. A packet-independent physical common subfeature exists exactly when C is positive as a source form; then Douglas factorization constructs it.','next_source_estimate':'Prove C_alpha >= 0 in the phase-energy graph norm for the transported eight-leg physical Grams, or prove an asymptotic lower bound C_alpha >= -epsilon_alpha B_alpha with epsilon_alpha -> 0.'}
if __name__=='__main__':
 p=ROOT/'results'/'global-common-subfeature-douglas-gate.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
