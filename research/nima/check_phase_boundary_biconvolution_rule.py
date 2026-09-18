#!/usr/bin/env python3
"""Test separate contra-insertion and co-reflow accounting across phase boundaries."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];src=json.loads((ROOT/'research/nima/results/nnmhv-seven-transition-flux.json').read_text());rows=[]
for name,data in sorted(src['transitions'].items(),key=lambda kv:kv[1]['delta']):
 s=data['samples'][-1];contra=s['insertion_fraction'];co=s['reflow_fraction'];rows.append({'transition':name,'delta':data['delta'],'contravariant_insertion':contra,'covariant_reflow':co,'orientation':co-contra,'reconstructs_scalar':abs(contra+co-1)<1e-12})
orient=[r['orientation'] for r in rows];checks={'all_scalar_fluxes_reconstructed_from_two_channels':all(r['reconstructs_scalar'] for r in rows),'orientation_strictly_orders_delta':all(a<b for a,b in zip(orient,orient[1:])),'negative_sector_contravariant':all(r['contravariant_insertion']>r['covariant_reflow'] for r in rows if r['delta']<0),'positive_sector_covariant':all(r['covariant_reflow']>r['contravariant_insertion'] for r in rows if r['delta']>0),'zero_sector_retains_both_channels':all(min(r['contravariant_insertion'],r['covariant_reflow'])>0.25 for r in rows if r['delta']==0)}
out={'schema':'marici.nima.phase-boundary-biconvolution-rule.v1','signature':'net flux = contravariant insertion + covariant reflow','orientation':'(reflow-insertion)/net','transitions':rows,'checks':checks,'passed':all(checks.values()),'rule':'A phase-boundary equivalence must match the two-channel signature before scalar augmentation.'};p=ROOT/'research/nima/results/phase-boundary-biconvolution-rule.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
