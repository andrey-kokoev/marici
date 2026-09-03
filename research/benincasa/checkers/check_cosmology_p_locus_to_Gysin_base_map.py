#!/usr/bin/env python3
"""DPC census for a source-derived p-locus map to Gysin variables."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
chart=json.loads((B/'rank12-radial-chart.json').read_text());origin=json.loads((R/'coordinate-origin-map-inventory.json').read_text());prior=json.loads((R/'cosmology_norm_Gysin_pole_support_compatibility.json').read_text());assert prior['passed'] and origin['status']=='pass'
assert chart['normalized_chart']['inverse']['X2/X1']=='(u+v)/2-1' and chart['normalized_chart']['inverse']['X3/X1']=='(u-v)/2'
exclude={'check_cosmology_p_locus_to_Gysin_base_map.py','cosmology_p_locus_to_Gysin_base_map.json','cosmology-p-locus-to-Gysin-base-map.md','check_cosmology_norm_Gysin_pole_support_compatibility.py','cosmology_norm_Gysin_pole_support_compatibility.json','cosmology-norm-Gysin-pole-support-compatibility.md'}
scanned=0;candidates=[]
for p in B.glob('**/*'):
 if not p.is_file() or p.name in exclude or '.tmp_sympy' in p.parts or p.suffix not in ('.json','.py','.md') or p.stat().st_size>=1_000_000:continue
 scanned+=1;t=p.read_text(errors='ignore').lower().replace(' ','')
 has_base=('p=x+y+3z' in t or 'v=2u' in t);has_all=all(x in t for x in ('s1','s2','s3'));has_assignment=any(x in t for x in ('s1=','"s1":',"'s1':"))
 if has_base and has_all and has_assignment:candidates.append(str(p.relative_to(ROOT)))
assert candidates==[]
out={'schema':'marici.benincasa.cosmology-p-locus-to-Gysin-base-map.v1','conjecture':'active artifacts assign s1,s2,s3 as rational functions of the p-locus coordinate u','p_locus_data':{'ambient_ratios':{'X2/X1':'(u+v)/2-1','X3/X1':'(u-v)/2'},'divisor':'v=2u','specialized_ratios':{'X2/X1':'3u/2-1','X3/X1':'-u/2'}},'required_map':'Q[s1,s2,s3] -> Q(u)','files_scanned':scanned,'artifacts_with_p_base_and_all_three_s_assignments':candidates,'coordinate_origin_inventory_passes_typing_gate':False,'conjecture_disposition':'falsified under the active source envelope','reason':'the p chart assigns X-ratios but no source artifact identifies the three Gysin variables with rational functions on that chart','Gysin_denominator_pullback_defined':False,'next_conjecture':'the naive identification (s1,s2,s3)=(X1,X2,X3), after X1=1, has pole support compatible with the norm residual','next_falsifier':'pull back s1*s2*s3*Lambda_P along the naive assignment and compare irreducible factors with u*(u-1)*(u-2)*D','passed':True};(R/'cosmology_p_locus_to_Gysin_base_map.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
