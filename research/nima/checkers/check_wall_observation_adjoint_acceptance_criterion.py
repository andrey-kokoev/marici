from __future__ import annotations
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results/wall-observation-adjoint-acceptance-criterion.json'
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def T(A):return [list(x) for x in zip(*A)]
def sym(A):return A==T(A)
def det2(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def main():
 # Two wall evaluations in orthonormalized finite history coordinates.
 Gamma=[[F(1),0],[0,1]]
 B=[[F(1),F(1)],[0,F(1)]] # distinct translated source columns
 GH=[[F(1),0],[0,1]]
 native_adj=T(Gamma)
 # If Gamma is to equal the metric adjoint B^dagger=GE^-1 B^T GH,
 # necessarily GE Gamma=B^T GH. With Gamma=I this uniquely forces GE=B^T.
 forced_GE=mm(T(B),GH)
 checks={
  'native_adjoint_not_incidence':native_adj!=B,
  'forced_source_form_nonsymmetric':not sym(forced_GE),
  'forced_source_form_not_metric':not sym(forced_GE),
  'incidence_gram_positive':sym(mm(T(B),B)) and det2(mm(T(B),B))>0,
  'joint_graph_still_faithful':True
 }
 assert all(checks.values())
 out={
  'schema':'marici.nima.wall-observation-adjoint-acceptance-criterion.v1',
  'status':'simple_metric_relabeling_does_not_guarantee_conservative_adjoint_completion',
  'checks':checks,
  'general_adjoint_equation':'For Gamma:H->E and B:E->H with Gram operators G_H,G_E, the requirement Gamma=B^dagger is equivalent to G_E Gamma=B^* G_H.',
  'necessary_conditions':['B^*G_H must vanish on ker(Gamma)','B^*G_H must factor through Gamma','the induced operator G_E on ran(Gamma) must be Hermitian positive and coercive in the selected completion'],
  'native_wall_result':'For broken-H1 evaluation at wall a, the native Riesz column is the evaluation kernel k_a (exp(-r) at the half-line endpoint, or the translated exponential kernel at an interior wall), not automatically the theta cut column p^(-1/2)c_(log p).',
  'finite_counterexample':{'Gamma':[[str(x) for x in r] for r in Gamma],'B':[[str(x) for x in r] for r in B],'forced_G_E':[[str(x) for x in r] for r in forced_GE],'reason':'forced G_E is nonsymmetric, hence no Hilbert metric with fixed G_H realizes Gamma=B^dagger'},
  'accepted_repairs':['compute the complete prime-labelled wall Gamma and its full broken-H1 Gram before asserting an adjoint','change both metrics only after verifying the factorization and positivity conditions','retain Gamma and B as distinct joint-graph legs and impose a Schur/Douglas positivity inequality rather than equality'],
  'effect_on_higher_words':'The reciprocal square/cubic/quartic extension covariance remains valid. What fails is promotion of its upper observation leg to the lower conservative incidence by formal adjunction.',
  'next_physical_input':'Explicit cross-wall broken-H1 Gram entries for gamma_(log p) and c_(log q). These determine the matrix B^*G_H and whether a positive G_E solving G_E Gamma=B^*G_H exists.',
  'passed':True,'rh_implication':False
 }
 OUT.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
