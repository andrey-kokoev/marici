#!/usr/bin/env python3
"""Exact rank audit for movable-cutoff observation of a Green block."""
import json
from fractions import Fraction
from pathlib import Path
import check_two_boundary_block_consistency as ranks

def main():
 n=12;rho=Fraction(3,5);K=[[rho**abs(i-j) for j in range(n)] for i in range(n)];rows=[]
 for m in range(n+1):
  marks=list(range(m));A=[K[i][:] for i in marks]
  r=0 if not A else ranks.rank(A);assert r==m
  rows.append({'observer_cuts':m,'visible_dimension':m,'hidden_dimension':n-m,'first_order_cross_capacity':m*(n-m)})
 assert max(x['first_order_cross_capacity'] for x in rows)==36
 result={'schema':'marici.coherence.movable-cutoff-observability.v1','state_dimension':n,'rho':str(rho),'rows':rows,'complete_observation_rank':n,'maximum_cross_capacity':36,'maximum_at_observer_counts':[6],'conclusion':'independent movable cutoffs increase visible rank one by one; complete cutoff coverage removes the hidden block kernel, while leakage-tomography capacity peaks at half coverage'}
 Path(__file__).with_name('movable-cutoff-observability.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
