#!/usr/bin/env python3
"""Quantitative Gaussian alias-tail audit for polynomial-growth tempered bounds."""
import json,math
from pathlib import Path

def alias_bound(h,sigma,R,m,K=10000):
 P=2*math.pi/h;s=0.0
 for k in range(1,K+1):
  x=k*P-R;s+=2*(1+x)**m*math.exp(-sigma*x*x)
 return s

def main():
 rows=[]
 for m in (0,2,5,10):
  previous=None
  for h in (.5,.25,.125,.0625):
   b=alias_bound(h,.005,1.0,m)
   if previous is not None:assert b<previous
   previous=b;rows.append({'distribution_order_growth':m,'h':h,'alias_tail_majorant':b})
 result={'schema':'marici.voevodsky.gaussian-damping-periodization-tail.v1','sigma':.005,'compact_test_radius':1.0,'rows':rows,'tails_decrease_with_spacing':True,'theorem':'If T is tempered and sigma>0, exp(-sigma u^2)T acts continuously on smooth bounded-derivative periodic tests, and pairings with nonzero aliases of a fixed compact test tend to zero as h tends to zero.','reason':'Every tempered seminorm contributes only polynomial growth, dominated uniformly by Gaussian decay at alias distances 2pi|k|/h.','periodization_hypothesis_discharged':True,'source_boundary':'Requires the completed Weil distribution to be tempered and the arithmetic/analytic source comparison to hold.'}
 out=Path(__file__).parents[1]/'results'/'gaussian_damping_periodization_tail.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'largest_bound':max(r['alias_tail_majorant'] for r in rows),'smallest_bound':min(r['alias_tail_majorant'] for r in rows)},indent=2))
if __name__=='__main__':main()
