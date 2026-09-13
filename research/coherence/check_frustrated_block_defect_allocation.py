#!/usr/bin/env python3
"""Exact audit of local consistency-defect allocation between two orientations."""
import json
from fractions import Fraction
from pathlib import Path
import check_two_sided_block_observer_model as block

def moments(w,rho):
 n=len(w);return sum(rho**(n-1-i)*x for i,x in enumerate(w)),sum(rho**i*x for i,x in enumerate(w))
def main():
 n=9;rho=Fraction(3,5);omega=[Fraction(0)]*n;omega[4]=Fraction(2)
 rows=[]
 for theta in (Fraction(0),Fraction(1,2),Fraction(1)):
  past_events=[theta*w for w in omega];future_events=[-(1-theta)*w for w in omega]
  P,_=block.tails(past_events,rho);_,F=block.tails(future_events,rho)
  mismatch=[P[i]-(rho*P[i-1] if i else 0)-(F[i]-(rho*F[i+1] if i+1<n else 0)) for i in range(n)]
  assert mismatch==omega
  rows.append({'theta':str(theta),'right_past_boundary':str(P[-1]),'left_future_boundary':str(F[0]),'same_local_defect':True})
 assert len({(r['right_past_boundary'],r['left_future_boundary']) for r in rows})==3
 # A three-site two-moment-kernel defect has no boundary leakage for any split.
 sites=(2,4,7);A=[[rho**(n-1-i) for i in sites],[rho**i for i in sites]]
 v=[A[0][1]*A[1][2]-A[0][2]*A[1][1],A[0][2]*A[1][0]-A[0][0]*A[1][2],A[0][0]*A[1][1]-A[0][1]*A[1][0]];hidden=[Fraction(0)]*n
 for i,x in zip(sites,v):hidden[i]=x
 assert moments(hidden,rho)==(0,0)
 result={'schema':'marici.coherence.frustrated-block-defect-allocation.v1','rho':str(rho),'single_defect_site':4,'allocation_rows':rows,'defect_does_not_determine_boundary_leakage':True,'kernel_defect_sites':sites,'kernel_defect_invisible_for_every_allocation':True,'conclusion':'a frustration cocycle needs an allocation/gauge rule before propagation is defined; two-moment-kernel frustrations remain localized under every allocation'}
 Path(__file__).with_name('frustrated-block-defect-allocation.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
