from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/nima/results/exceptional-euler-square-reconstruction-obstruction.json"
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mpow(A,k):
 n=len(A);R=[[F(int(i==j)) for j in range(n)] for i in range(n)]
 for _ in range(k):R=mm(R,A)
 return R
def add(A,B):return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def main():
 S=[[0,1,0],[0,0,1],[0,0,0]]
 pi=[[F(1),0,0]];delta=[[0,0,F(7)]];pi2=add(pi,delta)
 records={}
 for k in (2,3,4):
  c1=mm(pi,mpow(S,k-1));c2=mm(pi2,mpow(S,k-1))
  records[str(k)]={"pi_word":[str(x) for x in c1[0]],"pi_plus_delta_word":[str(x) for x in c2[0]],"equal":c1==c2}
 checks={
  "primitive_extensions_distinct":pi!=pi2,
  "delta_annihilates_shift":mm(delta,S)==[[0,0,0]],
  "square_indistinguishable":records["2"]["equal"],
  "cubic_indistinguishable":records["3"]["equal"],
  "quartic_indistinguishable":records["4"]["equal"],
  "all_higher_words_indistinguishable":True
 }
 assert all(checks.values())
 out={
  "schema":"marici.nima.exceptional-euler-square-reconstruction-obstruction.v1",
  "status":"higher_bidirectional_words_do_not_recover_primitive_extension_at_lambda_zero",
  "checks":checks,
  "exceptional_locus":"lambda=1-p^(-2s)=0",
  "word_formula_at_locus":"c_k=pi_0 S^(k-1) for k>=2",
  "kernel_ambiguity":"Any delta with delta S=0 may be added to pi_0 without changing c_2,c_3,c_4 or any higher c_k.",
  "finite_witness":"On the three-jet nilpotent shift, pi=(1,0,0) and pi'=(1,0,7) are distinct but produce identical words at every k>=2.",
  "records":records,
  "consequence":"Square-first reconstruction is only a generic-chart theorem. Even complete bidirectionality of square, cubic, quartic, and all higher convolutions cannot replace primitive extension data at the Euler exceptional locus.",
  "required_global_architecture":"Retain the primitive extension class pi_0 in the short exact sequence, and use square/cubic/quartic words as coherence checks. Alternatively glue generic reconstructions with explicit transition data regular at lambda=0; do not divide by lambda globally.",
  "relation_to_objective":"Primitive equality remains a logically independent obligation at the exceptional chart even when every higher cyclic word is bidirectionally coherent.",
  "next_gate":"Construct the two-chart relative extension retaining pi_0 across lambda=0 and reciprocal reflection, then verify that generic square reconstruction agrees with the retained primitive class on overlap.",
  "passed":True,
  "rh_implication":False
 }
 OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps(out,indent=2))
if __name__=="__main__":main()
