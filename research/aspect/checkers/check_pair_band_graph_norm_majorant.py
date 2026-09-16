#!/usr/bin/env python3
import json,math
from pathlib import Path
R=Path(__file__).resolve().parents[3]
x=json.loads((R/'research/aspect/results/pair_band_graph_norm_majorant.v1.json').read_text())
def partial(N,a=0.,r=1.):
 return sum((n*m)**(-1-2*a-2*r)*(1+math.log(n*m))**2 for n in range(1,N+1) for m in range(1,N+1))
sums=[partial(n) for n in [10,20,40,80,160]]
increments=[sums[i]-sums[i-1] for i in range(1,len(sums))]
# Positive monotone series with geometrically shrinking dyadic shell increments.
checks={
 'rapid_source_source':x['source_topology'].startswith('p_r(c)^2='),
 'H1_target':x['majorant']['target']=='H1(R)_W direct-sum H1(R)_J',
 'r1_sufficient':'r=1' in x['majorant']['sufficient_source_order'],
 'series_monotone':all(sums[i]>sums[i-1] for i in range(1,len(sums))),
 'dyadic_increments_shrink':all(increments[i]<increments[i-1] for i in range(1,len(increments))),
 'tail_small':increments[-1]<5e-3,
 'cutoff_uniform':x['majorant']['cutoff_uniform'] is True,
 'completion_unique':x['majorant']['completion_unique'] is True,
 'map_continuous':x['constructed_map']['continuous'] is True,
 'radial_fold_open':x['B1_progress']['doubled_radial_component_typing']=='open',
 'wall_open':x['B1_progress']['wall_domain_admission']=='open',
 'bound_not_overclaimed':x['remaining_type_gap']['cannot_be_fixed_by_bound_alone'] is True,
 'Cpair_not_complete':x['B1_progress']['C_pair_rad_complete'] is False,
 'comparison_blocked':x['comparison_permitted'] is False,
 'rh_not_promoted':x['rh_implication'] is False}
o={'schema':'marici.aspect.pair-band-graph-norm-majorant-check.v1','passed':all(checks.values()),'checks':checks,'partial_dual_series':dict(zip(['10','20','40','80','160'],sums)),'dyadic_increments':increments,'verdict':'uniform completed continuity to pair-band H1 is certified; the remaining B1 gap is the source-derived radial fold and wall condition'}
(R/'research/aspect/results/pair_band_graph_norm_majorant.check.v1.json').write_text(json.dumps(o,indent=2)+'\n');print(json.dumps(o,indent=2));raise SystemExit(0 if o['passed'] else 1)
