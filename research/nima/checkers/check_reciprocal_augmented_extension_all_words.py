from __future__ import annotations
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results/reciprocal-augmented-extension-all-words.json'
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mp(A,k):
 n=len(A);R=[[F(int(i==j)) for j in range(n)] for i in range(n)]
 for _ in range(k):R=mm(R,A)
 return R
def T(A):return [list(x) for x in zip(*A)]
def ext(lam,sign):
 # sign=+1 positive: top jet=-pi0, shift=S; sign=-1 negative: +pi0,-S
 return [[lam,F(-sign),0,0],[0,0,F(sign),0],[0,0,0,F(sign)],[0,0,0,0]]
def main():
 # lambda_+ at z and lambda_- at -z are equal; arbitrary exact value includes no division.
 lam=F(0) # deliberately test exceptional Euler locus
 Ap=ext(lam,1);Am_reflected=ext(lam,-1)
 C=[[F(-1),0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,1]]
 records={}
 for k in range(1,5):
  left=mm(C,mp(Ap,k));right=mm(mp(Am_reflected,k),C)
  # transpose reverses the intertwiner: Ap^T^k C^T = C^T Am^T^k
  dleft=mm(mp(T(Ap),k),T(C));dright=mm(T(C),mp(T(Am_reflected),k))
  records[str(k)]={'primal_chart_covariance':left==right,'dual_chart_covariance':dleft==dright}
 checks={
  'transport_involutive':mm(C,C)==[[F(int(i==j)) for j in range(4)] for i in range(4)],
  'primitive_at_lambda_zero':all(records['1'].values()),
  'square_at_lambda_zero':all(records['2'].values()),
  'cubic_at_lambda_zero':all(records['3'].values()),
  'quartic_at_lambda_zero':all(records['4'].values()),
 }
 assert all(checks.values())
 out={
  'schema':'marici.nima.reciprocal-augmented-extension-all-words.v1',
  'status':'primitive_square_cubic_quartic_reciprocal_bidirectionality_closed_including_exceptional_locus',
  'checks':checks,'records':records,
  'transport':'C_J=diag(-1,1,-1,1,...) on (q,a0,a1,a2,...); C_J^2=I',
  'positive':'A_+(z)=[[lambda_+(z),-pi0],[0,S]]',
  'negative':'A_-(z)=[[lambda_-(z),+pi0],[0,-S]]',
  'primitive_law':'C_J A_+(z)=A_-(-z) C_J because lambda_-(-z)=lambda_+(z), pi0 P_J=pi0, and P_J S=-S P_J.',
  'all_word_law':'C_J A_+(z)^k=A_-(-z)^k C_J for every k; transposition gives the contragredient law (A_+^T)^k C_J^T=C_J^T(A_-^T)^k.',
  'exceptional_locus':'The exact test uses lambda=0. No inversion or square reconstruction occurs, so the retained primitive extension removes the exceptional-chart ambiguity.',
  'consequence':'Square, cubic, and quartic augmented returns now have explicit forward and dual reciprocal transport, with primitive endpoint data retained. This completes bidirectionality internal to the radial/cyclic augmented extension, but not comparison to unexposed old conservative owner blocks.',
  'next_gate':'Transport the old conservative arithmetic/history/incidence matrices into this response basis and test equality with A_+, A_- and their transposes. Without those owner matrices no further cross-architecture equality is executable.',
  'passed':True,'rh_implication':False
 }
 OUT.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
