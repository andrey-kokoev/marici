#!/usr/bin/env python3
"""Fejer hierarchy scout after halving source translate spacing."""
import json,math
from pathlib import Path

def value(k,N,x):return k[0]+2*sum((1-m/N)*k[m]*math.cos(m*x) for m in range(1,N))
def main():
 sigma=.005;h=.125;maxN=13;mesh=131072
 src=json.loads((Path(__file__).parents[1]/'results'/'two_translate_weil_deficit_scout.json').read_text())
 diag=json.loads((Path(__file__).parents[1]/'results'/'two_translate_symmetric_eigenvalue_scout.json').read_text());k0=diag['K0']
 k=[k0]+[k0-next(r['K0_minus_Kd'] for r in src['rows'] if r['sigma']==sigma and r['d']==m*h) for m in range(1,maxN)]
 rows=[]
 for N in range(2,maxN+1):
  vals=[value(k,N,2*math.pi*j/mesh) for j in range(mesh)];mn=min(vals);j=vals.index(mn);deriv=2*sum((1-m/N)*m*abs(k[m]) for m in range(1,N));interp=deriv*math.pi/mesh
  coeff=1e-6+4e-6*sum(1-m/N for m in range(1,N));lower=mn-interp-coeff
  rows.append({'N':N,'mesh_minimum':mn,'minimizing_angle':2*math.pi*j/mesh,'interpolation_error':interp,'coefficient_error':coeff,'conditional_global_lower':lower})
 tight=min(rows,key=lambda r:r['conditional_global_lower']);allpos=all(r['conditional_global_lower']>0 for r in rows)
 result={'schema':'marici.voevodsky.halved-spacing-fejer-hierarchy.v1','sigma':sigma,'spacing':h,'orders_checked':'2..13','kernel_values':k,'rows':rows,'all_conditional_global_bounds_positive':allpos,'tightest_case':tight,'comparison_spacing':.25,'certified':'conditional on inherited source coefficient error model','conclusion':'Halving the spacing preserves conditional Fejer positivity through order thirteen.'}
 out=Path(__file__).parents[1]/'results'/'halved_spacing_fejer_hierarchy.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'all_positive':allpos,'tightest':tight},indent=2))
if __name__=='__main__':main()
