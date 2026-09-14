#!/usr/bin/env python3
"""Exact finite model of a least-rung positive-constructor obstruction."""
import json
from fractions import Fraction
from pathlib import Path

def det2(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def q(A,v):return sum(v[i]*A[i][j]*v[j] for i in range(len(v)) for j in range(len(v)))
def main():
 # Equicorrelation r=-3/5: every proper 1/2 packet is positive, rank three fails.
 r=Fraction(-3,5);G=[[Fraction(1) if i==j else r for j in range(3)] for i in range(3)]
 assert all(G[i][i]>0 for i in range(3))
 proper=[]
 for i in range(3):
  ids=[j for j in range(3) if j!=i];A=[[G[a][b] for b in ids] for a in ids]
  assert det2(A)>0;proper.append(str(det2(A)))
 witness=[1,1,1];negative=q(G,witness);assert negative<0
 # Positive feature fixture: Gram restrictions are automatically coherent under inclusions.
 features=[(1,0),(1,1),(0,1)]
 P=[[sum(features[i][k]*features[j][k] for k in range(2)) for j in range(3)] for i in range(3)]
 assert q(P,[1,-1,1])>=0
 result={'schema':'marici.voevodsky.positive-rung-constructor-obstruction.v1','minimal_failure_fixture':{'rank':3,'matrix':[[str(x) for x in row] for row in G],'proper_rank_two_determinants':proper,'negative_vector':witness,'negative_value':str(negative)},'positive_feature_fixture_coherent':True,'theorem':'For a fixed Hermitian kernel, coherent positive constructors on every finite packet exist iff every finite Gram matrix is PSD. If a negative packet exists, a least failing cardinality exists and all smaller packets succeed while that next rung has no positive constructor.','rh_bridge':'Schwartz density of Gaussian translates turns failure of Weil positivity into a negative finite Gaussian packet; the standard Weil criterion then identifies all-rung existence with RH.','warning':'Constructor existence is an equivalent positivity target unless a source-derived feature map is supplied independently.'}
 out=Path(__file__).parents[1]/'results'/'positive_rung_constructor_obstruction.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
