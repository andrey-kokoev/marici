#!/usr/bin/env python3
"""Four-node complete-continuum residual margins across [.649,.65]."""
import json
from pathlib import Path
root=Path(__file__).parents[1]/'results';pairs=[(.649,'physical_regularized_residual_gram_L0649_refined_scout.json'),(.6491464466094067,'physical_regularized_residual_gram_L0649146_refined_scout.json'),(.6495,'physical_regularized_residual_gram_L06495_refined_scout.json'),(.6498535533905933,'physical_regularized_residual_gram_L0649854_refined_scout.json'),(.65,'physical_regularized_residual_gram_L065_refined_scout.json')];rows=[]
for L,n in pairs:
 d=json.loads((root/n).read_text());rows.append({'L':L,'complete_residual_norm':d['complete_residual_norm'],'lower_margin':d['a_posteriori_lower_form_min']})
out={'schema':'marici.voevodsky.complete-residual-margin-across-L0649-L065.v1','rows':rows,'minimum_sampled_margin':min(x['lower_margin'] for x in rows),'maximum_sampled_residual_norm':max(x['complete_residual_norm'] for x in rows),'all_positive':all(x['lower_margin']>0 for x in rows),'status':'floating five-node slab scout; directed interval interpolation open','passed':all(x['lower_margin']>0 for x in rows),'rh_proved':False};p=root/'complete_residual_margin_across_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
