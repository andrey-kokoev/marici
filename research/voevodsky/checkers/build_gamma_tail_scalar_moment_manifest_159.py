#!/usr/bin/env python3
"""Enumerate scalar moments sufficient for every j_m*j_n gamma tail, m,n<80."""
import json
from pathlib import Path
data=json.loads((Path(__file__).parents[1]/'results'/'spherical_bessel_inverse_power_expansions_159.json').read_text());S=data['S'];C=data['C'];powers=set();families=set()
for m in range(160):
 for n in range(m,160):
  for A,B,fams in ((S[m],S[n],('plain','cos2')), (C[m],C[n],('plain','cos2')), (S[m],C[n],('sin2',)),(C[m],S[n],('sin2',))):
   for i,a in enumerate(A):
    if not a:continue
    for j,b in enumerate(B):
     if b:
      powers.add(i+j)
      for f in fams:families.add((f,i+j))
assert min(powers)==2 and max(powers)==320
out={'schema':'marici.voevodsky.gamma-tail-scalar-moment-manifest.v1','basis_orders':'0..159','inverse_power_range':[min(powers),max(powers)],'moment_families':{'plain':[k for f,k in sorted(families) if f=='plain'],'cos_2Lu':[k for f,k in sorted(families) if f=='cos2'],'sin_2Lu':[k for f,k in sorted(families) if f=='sin2']},'total_distinct_scalar_moments':len(families),'identity':'sin^2=(1-cos 2x)/2, cos^2=(1+cos 2x)/2, sin*cos=sin 2x/2','passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'gamma_tail_scalar_moment_manifest_159.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'inverse_power_range':out['inverse_power_range'],'total_distinct_scalar_moments':len(families),'passed':True},indent=2))
