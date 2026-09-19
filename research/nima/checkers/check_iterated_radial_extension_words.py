from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/nima/results/iterated-radial-extension-words.json"
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mpow(A,k):
 R=[[F(int(i==j)) for j in range(len(A))] for i in range(len(A))]
 for _ in range(k):R=mm(R,A)
 return R
def T(A):return [list(x) for x in zip(*A)]
def main():
 lam=F(3,5)
 # q plus three boundary jets; nilpotent shift a0<-a1<-a2.
 A=[[lam,-1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]]
 records={}
 for k in range(1,5):
  Ak=mpow(A,k)
  # Formula top-right: -sum_(j=0)^(k-1) lam^(k-1-j) pi0 S^j.
  expected_top=[lam**k]
  for col in range(1,4):
   j=col-1
   expected_top.append(-(lam**(k-1-j)) if j<k else F(0))
  records[str(k)]={
   "matrix":[[str(x) for x in row] for row in Ak],
   "Euler_multiplier":str(Ak[0][0]),
   "top_extension_row":[str(x) for x in Ak[0][1:]],
   "formula_matches":Ak[0]==expected_top,
   "transpose_power_matches":T(Ak)==mpow(T(A),k)
  }
 checks={
  "primitive_extension_formula":records["1"]["formula_matches"],
  "square_extension_formula":records["2"]["formula_matches"],
  "cubic_extension_formula":records["3"]["formula_matches"],
  "quartic_extension_formula":records["4"]["formula_matches"],
  "all_dual_words_correct":all(r["transpose_power_matches"] for r in records.values()),
  "Euler_subobject_carries_lambda_powers":all(records[str(k)]["Euler_multiplier"]==str(lam**k) for k in range(1,5))
 }
 assert all(checks.values())
 out={
  "schema":"marici.nima.iterated-radial-extension-words.v1",
  "status":"square_cubic_quartic_bidirectional_extension_words_constructed_exactly",
  "checks":checks,
  "general_formula":"If A=[[lambda,-pi0],[0,S]], then A^k=[[lambda^k,-sum_(j=0)^(k-1) lambda^(k-1-j) pi0 S^j],[0,S^k]].",
  "cocycle":"c_k=sum_(j=0)^(k-1)lambda^(k-1-j)pi0 S^j satisfies c_(k+l)=lambda^k c_l+c_k S^l.",
  "dual_formula":"(A^k)^top=(A^top)^k; the extension arrows reverse order automatically, giving the contragredient return word without a primal inverse.",
  "records":records,
  "interpretation":{
   "k=1":"primitive augmented return",
   "k=2":"square carries lambda^2 on Euler line and endpoint cocycle lambda pi0+pi0 S",
   "k=3":"cubic carries lambda^3 and three transported endpoint insertions",
   "k=4":"quartic carries lambda^4 and four transported endpoint insertions"
  },
  "consequence":"Higher convolutions are individually bidirectional as extension words: each has an explicit forward triangular iterate and a reversed dual iterate. They are not scalar powers on the full carrier and do not require inverse comparison maps.",
  "physical_next_gate":"Check that the old conservative extension class and quotient shift equal (-pi0,S) in the adopted response basis. Equality only on the Euler subobject is insufficient; the cocycle rows c_2,c_3,c_4 provide the first finite tests.",
  "passed":True,
  "rh_implication":False
 }
 OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps(out,indent=2))
if __name__=="__main__":main()
