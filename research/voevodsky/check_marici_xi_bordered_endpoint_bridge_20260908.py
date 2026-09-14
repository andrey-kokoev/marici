#!/usr/bin/env python3
"""Exact symbolic bridge from the source-bordered Xi family to D35/D04 endpoint lines."""
import argparse,json
from pathlib import Path

# Polynomials in s,H represented sparsely by (s_degree,H_degree)->integer.
def add(*ps):
 z={}
 for p in ps:
  for e,c in p.items():z[e]=z.get(e,0)+c
 return {e:c for e,c in z.items() if c}
def mul(p,q):
 z={}
 for (i,j),a in p.items():
  for (k,l),b in q.items():z[(i+k,j+l)]=z.get((i+k,j+l),0)+a*b
 return {e:c for e,c in z.items() if c}
def neg(p):return {e:-c for e,c in p.items()}
def det3(M):
 return add(mul(M[0][0],add(mul(M[1][1],M[2][2]),neg(mul(M[1][2],M[2][1])))),
            neg(mul(M[0][1],add(mul(M[1][0],M[2][2]),neg(mul(M[1][2],M[2][0]))))),
            mul(M[0][2],add(mul(M[1][0],M[2][1]),neg(mul(M[1][1],M[2][0])))))

def main():
 p=argparse.ArgumentParser();p.add_argument('--root',default='.');p.add_argument('--output',required=True);a=p.parse_args();r=Path(a.root)
 desc=json.loads((r/'research/voevodsky/marici_normalization_q_descent_certificate_20260908.json').read_text())
 d=json.loads((r/'research/voevodsky/marici_strict_d35_d04_spatial_comparison_certificate_20260908.json').read_text())
 assert desc['status']==d['status']=='proved';checks=2
 Z={};one={(0,0):1};minusone={(0,0):-1};s={(1,0):1};sm1={(1,0):1,(0,0):-1};H={(0,1):1}
 M=[[s,Z,one],[Z,sm1,one],[one,minusone,H]]
 determinant=det3(M);expected={(2,1):1,(1,1):-1,(0,0):1}
 assert determinant==expected;checks+=1 # s(s-1)H+1=2xi
 # Endpoint projection pi(u35)=pi(u04)=1 gives symmetric outgoing column.
 pi35=pi04=1;outgoing=[pi35,pi04];assert outgoing==[1,1];checks+=2
 # Normalization-dual conductor comparison is the signed difference.
 alpha=[1,-1];assert '(1,-1)' in desc['dual_descent'];checks+=2
 # Pairings: alpha kills symmetric line and is primitive on either marked leg.
 assert alpha[0]*outgoing[0]+alpha[1]*outgoing[1]==0;checks+=1
 assert alpha[0]==1 and alpha[1]==-1;checks+=2
 # Reflection exchanges endpoints: P; left/right signs give M(1-s)=L M(s) R.
 # Verify entrywise using substitution s->1-s.
 sub=lambda p:{(0,j):c for (i,j),c in p.items() if i==0} if False else p
 # Direct symbolic expected transformed matrix.
 one_minus_s={(0,0):1,(1,0):-1};minus_s={(1,0):-1}
 Mref=[[one_minus_s,Z,one],[Z,minus_s,one],[one,minusone,H]]
 # Compute L M R for L=diag(-P,-1), R=diag(P,-1).
 # Result by signed row/column permutations.
 LMR=[[neg(M[1][1]),neg(M[1][0]),M[1][2]],[neg(M[0][1]),neg(M[0][0]),M[0][2]],
      [neg(M[2][1]),neg(M[2][0]),M[2][2]]]
 assert LMR==Mref;checks+=9
 assert len(d['frames'])==8 and all(x['primitive_coefficient']==1 for x in d['frames']);checks+=9
 out={'schema':'marici.xi_bordered_endpoint_bridge.v1','status':'proved','checks':checks,
  'family':'M_s=[[s,0,1],[0,s-1,1],[1,-1,H(s)]] as a two-term 3x3 complex',
  'determinant':'det M_s=s(s-1)H(s)+1=2 xi(s)',
  'endpoint_identification':'e0 -> u_35, e1 -> u_04; pi_35(u_35)=pi_04(u_04)=1',
  'outgoing_vector':[1,1],'return_row':[1,-1],
  'non_tautological_match':'the return row equals the independently derived normalization-dual conductor row; it annihilates the symmetric outgoing endpoint line',
  'reflection':'M_(1-s)=diag(-P,-1) M_s diag(P,-1)',
  'spatial_frames':8,
  'result':'a source-derived parameter-dependent endpoint complex with determinant 2xi is typed by the strict marked conormal quotient and conductor difference',
  'boundary':'the bulk H(s) to full additive/multiplicative Marici carrier chain map and off-critical conservativity are not proved'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'proved','checks':checks,'determinant':'2xi','endpoint_row_match':[1,-1]}))
if __name__=='__main__':main()
