from fractions import Fraction as F
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'research/nima/results/retained-graph-joint-parametrix-lyapunov.json'

def tr(A): return [list(x) for x in zip(*A)]
def mm(A,B): return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))] for i in range(len(A))]
def add(*As): return [[sum((A[i][j] for A in As),F(0)) for j in range(len(As[0][0]))] for i in range(len(As[0]))]
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def inv(A):
 n=len(A); M=[row[:]+e[:] for row,e in zip(A,eye(n))]
 for c in range(n):
  p=next(i for i in range(c,n) if M[i][c]); M[c],M[p]=M[p],M[c]
  q=M[c][c]; M[c]=[x/q for x in M[c]]
  for i in range(n):
   if i!=c:
    q=M[i][c]; M[i]=[x-q*y for x,y in zip(M[i],M[c])]
 return [r[n:] for r in M]
def scale(q,A): return [[q*x for x in r] for r in A]
def eq(A,B): return A==B
def block_rows(*As): return [row[:] for A in As for row in A]
def enc(A): return [[str(x) for x in r] for r in A]

def main():
 # Exact noncommuting rational fixture on a three-dimensional retained source.
 B=[[F(1),F(2),F(0)],[F(0),F(1),F(1)]]
 M=[[F(2),F(0),F(1)],[F(1),F(-1),F(0)]]
 I=eye(3); R=block_rows(I,B,M)
 L=add(I,mm(tr(B),B),mm(tr(M),M))
 Li=inv(L); H=mm(Li,tr(R)); G=scale(F(1,2),Li)
 P=mm(R,H)
 checks={
  'normal_operator_is_R_star_R':eq(mm(tr(R),R),L),
  'canonical_left_parametrix':eq(mm(H,R),I),
  'range_projection_idempotent':eq(mm(P,P),P),
  'range_projection_self_adjoint':eq(tr(P),P),
  'lyapunov_equation':eq(add(mm(L,G),mm(G,L)),I),
  'same_inverse_generates_both':eq(scale(F(2),G),Li)
 }
 assert all(checks.values()),checks
 out={
  'schema':'marici.nima.retained-graph-joint-parametrix-lyapunov.v1',
  'classification':'finite_retained_graph_normal_operator_canonically_generates_both_parametrix_and_lyapunov_covariance',
  'fixture':{'B':enc(B),'M':enc(M),'L':enc(L),'H':enc(H),'G':enc(G)},
  'checks':checks,
  'theorem':'For R=(I,B,M), L=R*R=I+B*B+M*M is strictly positive. H=L^(-1)R* satisfies HR=I and RH is the orthogonal range projection. G=(1/2)L^(-1) uniquely solves LG+GL=I.',
  'scope':'Exact finite-dimensional Hilbert theorem and graph-core blueprint.',
  'remaining':['prove the closed-operator version on the common source graph domain','show L^(-1) maps the completed boundary dual into the source test grade','prove Adams and reciprocal covariance','prove cutoff compatibility and compact-sector equicontinuity'],
  'passed':True
 }
 OUT.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
if __name__=='__main__': main()
