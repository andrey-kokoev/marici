#!/usr/bin/env python3
"""Exact characteristic reconstruction from two endpoint boundaries and bulk curvature."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
rows=[]
for m in range(2,11):
 events=[(i,j) for i in range(1,m+1) for j in range(i,m+1)];pos={e:k for k,e in enumerate(events)};top=[(1,j) for j in range(1,m+1)];right=[(i,m) for i in range(2,m+1)];plaquettes=[(i,j) for i in range(2,m+1) for j in range(i,m)];observables=top+right+plaquettes;T=s.zeros(len(observables),len(events))
 for r,e in enumerate(top+right):T[r,pos[e]]=1
 for r,(i,j) in enumerate(plaquettes,start=len(top)+len(right)):
  for e,c in (((i,j),1),((i-1,j),-1),((i,j+1),-1),((i-1,j+1),1)):T[r,pos[e]]=c
 determinant=s.factor(T.det());rows.append({'m':m,'field_dimension':len(events),'lower_endpoint_boundary':len(top),'upper_endpoint_boundary_exclusive':len(right),'bulk_curvatures':len(plaquettes),'data_count':len(observables),'transform_determinant':str(determinant),'unimodular_reconstruction':abs(determinant)==1})
checks={'data_count_matches_field_dimension':all(x['data_count']==x['field_dimension'] for x in rows),'boundary_dimension_two_m_minus_one':all(x['lower_endpoint_boundary']+x['upper_endpoint_boundary_exclusive']==2*x['m']-1 for x in rows),'bulk_dimension_complements_boundary':all(x['bulk_curvatures']==x['field_dimension']-(2*x['m']-1) for x in rows),'characteristic_transform_unimodular':all(x['unimodular_reconstruction'] for x in rows),'tested_m2_through_m10':len(rows)==9}
out={'schema':'marici.nima.nnmhv-characteristic-boundary-reconstruction.v1','decomposition':'field f <-> (trace on i=1, trace on j=m excluding overlap, interior Delta_u Delta_v f)','recurrence':'f(i,j)=g(i,j)+f(i-1,j)+f(i,j+1)-f(i-1,j+1)','rows':rows,'checks':checks,'passed':all(checks.values()),'meaning':'Every history field is reconstructed integrally and uniquely from two characteristic endpoint channels plus bulk wave curvature. The transform has determinant plus/minus one, so no information or lattice volume is lost.','bridges':['Goursat characteristic boundary problem','left/right null boundary data','bulk-plus-boundary Hodge decomposition','unimodular integer transform','exact two-channel completion of sourced fields']};p=ROOT/'research/nima/results/nnmhv-characteristic-boundary-reconstruction.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'decomposition':out['decomposition'],'recurrence':out['recurrence'],'checks':checks,'meaning':out['meaning'],'bridges':out['bridges'],'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
