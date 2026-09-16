"""Exact weighted-row fixture for positive-regulator alignment and common-edge removal."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
def add(a,b):return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def sub(a,b):return [[x-y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def scale(c,a):return [[c*x for x in row] for row in a]
def outer(v):return [[x*y for y in v] for x in v]
def gram(rows):
 out=[[F(0),F(0)],[F(0),F(0)]]
 for weight,v in rows:out=add(out,scale(weight,outer(v)))
 return out
def det(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def psd2(a):return a[0][0]>=0 and a[1][1]>=0 and det(a)>=0
# Shared two-copy bulk rows. Their Gram K does not commute with the signed D.
bulk=[(F(2),[F(1),F(0)]),(F(1),[F(0),F(1)])]
plus=[(F(1,2),[F(1),F(1)])]
minus=[(F(1,2),[F(1),F(-1)])]
K=gram(bulk);Dp=gram(plus);Dm=gram(minus);Gt=gram(bulk+plus);G0=gram(bulk+minus);D=sub(Dp,Dm);absD=add(Dp,Dm)
# A placement error changes one bulk-row weight only on the reference side.
bad_bulk=[(F(2),[F(1),F(0)]),(F(2),[F(0),F(1)])];G0bad=gram(bad_bulk+minus)
checks={'tate_gram_positive':psd2(Gt),'reference_gram_positive':psd2(G0),'exact_alignment':sub(Gt,G0)==D,'bulk_cancels':sub(gram(bulk+plus),gram(bulk+minus))==sub(Dp,Dm),'bulk_noncommutes_with_signed_part':mm(K,D)!=mm(D,K),'mismatched_placement_fails':sub(Gt,G0bad)!=D,'common_edge_removal_returns_abs_D':add(sub(Gt,K),sub(G0,K))==absD,'jordan_parts_orthogonal':[[sum(Dp[i][k]*Dm[k][j] for k in range(2)) for j in range(2)] for i in range(2)]==[[F(0),F(0)],[F(0),F(0)]]}
out={'schema':'marici.voevodsky.positive-regulator-alignment-fixture.v1','weighted_rows':{'common_bulk':[[str(w),[str(x) for x in v]] for w,v in bulk],'tate_residual':[[str(w),[str(x) for x in v]] for w,v in plus],'reference_residual':[[str(w),[str(x) for x in v]] for w,v in minus]},'matrices':{'common_bulk_gram':[[str(x) for x in r] for r in K],'tate_gram':[[str(x) for x in r] for r in Gt],'reference_gram':[[str(x) for x in r] for r in G0],'centered_difference':[[str(x) for x in r] for r in D],'absolute_difference':[[str(x) for x in r] for r in absD]},'checks':checks,'passed':all(checks.values()),'analytic_gate':'Identify the physical Tate and reference features with one common weighted-row regulator so their two-copy bulk rows agree before taking any limit.'}
if __name__=='__main__':
 p=ROOT/'results'/'positive-regulator-alignment-fixture.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
