#!/usr/bin/env python3
"""Finite matrix gate between the three-channel theta packet and six normal ports."""
import argparse,json
from fractions import Fraction
from pathlib import Path

def mm(A,B):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*B)] for r in A]
def det3(A):return A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])
def main():
 p=argparse.ArgumentParser();p.add_argument('--root',default='.');p.add_argument('--output',required=True);a=p.parse_args();r=Path(a.root)
 six=json.loads((r/'research/voevodsky/marici_six_normal_spatial_transport_certificate_20260908.json').read_text());assert six['status']=='proved';checks=1
 K=[[0,0,-1,0,0,1],[-1,0,0,1,0,0],[0,1,0,0,-1,0]]
 KT=[list(x) for x in zip(*K)];G=mm(K,KT);assert G==[[2,0,0],[0,2,0],[0,0,2]];checks+=9
 left=[[Fraction(x,2) for x in row] for row in K]
 assert mm(left,KT)==[[1,0,0],[0,1,0],[0,0,1]];checks+=9
 # Theta coordinates (C,U,V) -> (xi=C+U+V, odd=U-V, transverse=2C-U-V).
 A=[[1,1,1],[0,1,-1],[2,-1,-1]];assert det3(A)==-6;checks+=1
 # Therefore both sides are rank three, and a 3x3 adapter is the sole finite missing map.
 out={'schema':'marici.theta_six_normal_adapter_gate.v1','status':'open_exact_adapter','checks':checks,
  'theta_coordinates':['C','U','V'],'theta_comparison_matrix':A,'theta_matrix_determinant':-6,
  'normal_incidence_K_alt':K,'K_alt_Gram':G,'normal_incidence_rank':3,
  'rational_left_inverse_of_K_alt_transpose':[[str(x) for x in row] for row in left],
  'known':'the three-channel theta packet and the six-normal incidence image are both exactly rank three',
  'missing':'a source-authorized 3x3 adapter from (xi,U-V,2C-U-V) to the three rows of K_alt, with support, grading, and completion-energy compatibility',
  'warning':'dimension/rank agreement does not authorize identifying these bases',
  'consequence_if_supplied':'K_alt^T composed with the adapter gives the common-source transport to all six normal observers; its rational return is (1/2)K_alt composed with the inverse adapter'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'open_exact_adapter','checks':checks,'theta_rank':3,'normal_incidence_rank':3,'missing_matrix':'3x3'}))
if __name__=='__main__':main()
