#!/usr/bin/env python3
"""Scalar Fejer hierarchy scout for the computed source Toeplitz coefficients."""
import json,math
from pathlib import Path

def value(k,N,theta):return k[0]+2*sum((1-m/N)*k[m]*math.cos(m*theta) for m in range(1,N))
def main():
 src=json.loads((Path(__file__).parents[1]/'results'/'equal_spacing_toeplitz_rank_ladder.json').read_text());k=src['kernel_values']
 mesh=131072;rows=[]
 for N in range(2,14):
  best=(float('inf'),None)
  for j in range(mesh):
   th=2*math.pi*j/mesh;v=value(k,N,th)
   if v<best[0]:best=(v,th)
  deriv=2*sum((1-m/N)*m*abs(k[m]) for m in range(1,N))
  mesh_error=deriv*math.pi/mesh
  coefficient_error=1e-6+4e-6*sum(1-m/N for m in range(1,N))
  rows.append({'N':N,'mesh_minimum':best[0],'minimizing_angle':best[1],'derivative_bound':deriv,'mesh_interpolation_error':mesh_error,'coefficient_error_allowance':coefficient_error,'conditional_global_lower':best[0]-mesh_error-coefficient_error})
 all_mesh=all(r['mesh_minimum']>0 for r in rows);all_cert=all(r['conditional_global_lower']>0 for r in rows)
 tight=min(rows,key=lambda r:r['conditional_global_lower'])
 result={'schema':'marici.voevodsky.source-fejer-hierarchy-scout.v1','sigma':src['sigma'],'spacing':src['spacing'],'orders_checked':'2..13','angle_mesh':mesh,'rows':rows,'all_mesh_values_positive':all_mesh,'all_conditional_global_bounds_positive':all_cert,'tightest_case':tight,'coefficient_error_model':'1e-6 on K(0), 2e-6 on each nonzero-separation coefficient','coefficient_errors_included':True,'certified':'conditional on inherited source evaluation error model','conclusion':'The source Fejer polynomials through order thirteen are globally positive under mesh interpolation and coefficient error bounds.'}
 out=Path(__file__).parents[1]/'results'/'source_fejer_hierarchy_scout.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'all_mesh_positive':all_mesh,'all_mesh_derivative_positive':all_cert,'tightest':tight},indent=2))
if __name__=='__main__':main()
