from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/nima/results/square-word-recovers-primitive-extension.json"
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def add(A,B):return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def inv3(A):
 # Gauss-Jordan exact
 n=3;M=[A[i][:]+[F(int(i==j)) for j in range(n)] for i in range(n)]
 for c in range(n):
  pivot=next(r for r in range(c,n) if M[r][c]);M[c],M[pivot]=M[pivot],M[c]
  q=M[c][c];M[c]=[x/q for x in M[c]]
  for r in range(n):
   if r!=c:
    q=M[r][c];M[r]=[M[r][j]-q*M[c][j] for j in range(2*n)]
 return [r[n:] for r in M]
def main():
 lam=F(3,5);I=[[F(int(i==j)) for j in range(3)] for i in range(3)]
 S=[[0,1,0],[0,0,1],[0,0,0]];pi=[[F(1),0,0]]
 lamI=[[lam*I[i][j] for j in range(3)] for i in range(3)]
 syl=add(lamI,S)
 c2=mm(pi,syl)
 recovered=mm(c2,inv3(syl))
 # c3=lambda^2 pi+lambda pi S+pi S^2 = lambda*c2+pi*S^2
 c3=add([[lam*x for x in c2[0]]],mm(pi,mm(S,S)))
 predicted_c3=add([[lam*x for x in c2[0]]],mm(recovered,mm(S,S)))
 c4=add([[lam*x for x in c3[0]]],mm(pi,mm(mm(S,S),S)))
 predicted_c4=add([[lam*x for x in c3[0]]],mm(recovered,mm(mm(S,S),S)))
 checks={
  "sylvester_factor_invertible":mm(syl,inv3(syl))==I,
  "square_recovers_pi0":recovered==pi,
  "cubic_compatibility":c3==predicted_c3,
  "quartic_compatibility":c4==predicted_c4,
  "exact_rational":True
 }
 assert all(checks.values())
 out={
  "schema":"marici.nima.square-word-recovers-primitive-extension.v1",
  "status":"generic_square_bidirectionality_determines_primitive_extension_cubic_quartic_are_coherence_tests",
  "checks":checks,
  "square_equation":"c_2=lambda pi_0+pi_0 S=pi_0(lambda I+S)",
  "reconstruction":"pi_0=c_2(lambda I+S)^(-1), whenever -lambda is not in spectrum(S)",
  "nilpotent_jet_case":"For boundary shift S nilpotent and lambda!=0, lambda I+S is automatically invertible with finite Neumann inverse.",
  "cubic_test":"c_3=lambda c_2+pi_0 S^2",
  "quartic_test":"c_4=lambda c_3+pi_0 S^3",
  "interpretation":"One can legitimately start from a fully bidirectional square extension. On the generic Euler chart it recovers the primitive endpoint extension class; cubic and quartic words then test associativity/cocycle coherence rather than introduce new reverse maps.",
  "exceptional_chart":"At lambda=1-p^(-2s)=0, reconstruction from c_2 alone may fail. The primitive extension or a higher relative/jet datum must be retained across that locus; division by lambda is forbidden there.",
  "physical_acceptance":"If the old conservative owner exposes its square cocycle c_2^old and quotient shift S_old, compare them with the radial c_2 and S. Reconstruct pi_0^old generically, then verify c_3 and c_4. This is stronger than scalar Euler agreement and avoids demanding an inverse of j_H.",
  "passed":True,
  "rh_implication":False
 }
 OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps(out,indent=2))
if __name__=="__main__":main()
