#!/usr/bin/env python3
"""Census explicit normalized transverse-slice lift declarations."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/benincasa/results/cosmology_normalized_transverse_slice_census.json'
roots=[ROOT/'research/benincasa/results',ROOT/'research/nima/results',ROOT/'research/voevodsky/results']
typed_keys={'dp','dp_normalization','slice_direction','transverse_direction','normal_coordinate','normalized_lift'};hits=[];scanned=0
def walk(x,path=()):
 if isinstance(x,dict):
  for k,v in x.items():
   if k in typed_keys:hits.append((path+(k,),v))
   walk(v,path+(k,))
 elif isinstance(x,list):
  for i,v in enumerate(x):walk(v,path+(str(i),))
for root in roots:
 for p in sorted(root.glob('cosmology*.json')):
  try:d=json.loads(p.read_text())
  except Exception:continue
  scanned+=1;before=len(hits);walk(d)
  for i in range(before,len(hits)):hits[i]={'path':p.relative_to(ROOT).as_posix(),'key_path':'.'.join(hits[i][0]),'value':hits[i][1]}
unit=[h for h in hits if h['key_path'].startswith('unit_p_normals.') and h['key_path'].endswith('.dp') and h['value']==1]
assert len(unit)==4 and {h['key_path'].split('.')[1] for h in unit}=={'nx','ny','n_alt_unit','n_alt_nonunit'}
source=json.loads((ROOT/'research/nima/results/cosmology_relative_c_kernel_section_no_go.json').read_text())
values={k:v['dc_on_graph'] for k,v in source['unit_p_normals'].items() if v['dp']==1};assert set(values.values())=={-3,-1,1}
out={'schema':'marici.benincasa.cosmology-normalized-transverse-slice-census.v1','scope':{'roots':[p.relative_to(ROOT).as_posix() for p in roots],'glob':'cosmology*.json','files_scanned':scanned,'admission_keys':sorted(typed_keys)},'admitted_unit_normal_declarations':unit,'unit_normal_vectors':{k:v['vector'] for k,v in source['unit_p_normals'].items() if v['dp']==1},'dc_on_graph_by_lift':values,'exact_residual':'four explicit dp=1 transverse lifts give dc values -1,-1,+1,-3; normalization by dp does not define a slice-independent c coefficient','disposition':'slice-independence falsified for the frozen graph relation c=-E','factorization_obstruction':'E does not vanish on ker(dp), equivalently E is not proportional to p','surviving_scope':'nx and ny agree, but alternative unit normals change dc; agreement of coordinate-axis slices is not canonical descent','acceptance_test':'supply a source-derived quotient section or prove the readout covector factors through dp','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
