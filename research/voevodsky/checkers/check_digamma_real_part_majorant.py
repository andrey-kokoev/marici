#!/usr/bin/env python3
"""Numerical stress audit accompanying the convergent-series digamma majorant proof."""
import json,math
from pathlib import Path
EULER_GAMMA=0.5772156649015329
def repsi_series(u,N=200000):
 a=.25;b=u/2;s=-EULER_GAMMA
 for k in range(N):s+=1/(k+1)-(k+a)/((k+a)**2+b*b)
 # Tail is O(1/N); this evaluator is diagnostic only.
 return s
def main():
 points=[0,.01,.1,.5,1,2,5,10,20,50,100];rows=[]
 for u in points:
  v=repsi_series(u);bound=21+2*u;assert abs(v)<bound
  rows.append({'u':u,'series_partial':v,'majorant':bound,'slack':bound-abs(v)})
 result={'schema':'marici.voevodsky.digamma-real-part-majorant.v1','points_checked':len(points),'rows':rows,'proved_majorant':'|Re psi(1/4+iu/2)| <= 21+2u for u>=0','proof_components':{'difference_series_bound':'less than 17/4','imaginary_correction_bound':'less than 11/2+2u','euler_constant_bound':'less than 1'},'numerical_role':'stress audit only','conclusion':'The majorant used in the gamma-tail and midpoint Lipschitz estimates follows from an absolutely convergent decomposition.'}
 out=Path(__file__).parents[1]/'results'/'digamma_real_part_majorant.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'points_checked':len(points),'minimum_slack':min(r['slack'] for r in rows)},indent=2))
if __name__=='__main__':main()
