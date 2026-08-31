#!/usr/bin/env python3
"""Freeze the weakest next-cutoff prediction from the observed syzygy-image ranks."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];src=ROOT/'research/nima/results/cosmology_p_normal_rank26_syzygy_bockstein_summary.json';out=ROOT/'research/aspect/results/rank26_syzygy_rank_growth_prediction.json'
d=json.loads(src.read_text());r={int(k):v for k,v in d['resolved_syzygy_image_rank_by_degree'].items()};assert r=={8:7,10:7,12:11,14:15};assert d['normal_image_equals_tangent_image'] and d['p_normal_image_mod_tangent_rank']==0
prediction={'schema':'marici.aspect.rank26-syzygy-rank-growth-prediction.v1','gamma_mode':'integer','observed':r,'weakest_tail_rule':'rank(d+2)=rank(d)+4 for d>=10','predicted_degree16_rank':19,'prediction_status':'finite-pattern extrapolation, not theorem','decisive_falsifiers':['degree-16 resolved image rank is not 19','normal image differs from tangent image at either prime'],'tau_p_map_constructed':False,'passed':True};out.write_text(json.dumps(prediction,indent=2)+'\n');print(json.dumps({'status':'passed','predicted_degree16_rank':19}))
