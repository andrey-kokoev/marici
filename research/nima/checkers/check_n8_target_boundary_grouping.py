#!/usr/bin/env python3
"""Group transition-refined rank-seven n=8 source facets by certified target label."""
from pathlib import Path
import json,collections
ROOT=Path(__file__).resolve().parents[3];src=json.loads((ROOT/'research/nima/results/n8-external-boundary-pushforward-rank.json').read_text());groups=collections.defaultdict(list)
for r in src['rank7_details']:
 labels=r['target_boundary_brackets']
 if labels:label=('bracket',tuple(labels[0]));kind='standard_bracket' if r['standard_boundary_brackets'] else 'nonstandard_bracket'
 elif r['history_index']==13 and r['seed']=='G' and r['alpha']==4:label=('quartic_history13_G_alpha4',);kind='verified_quartic'
 else:label=('unimplicitized',r['history_index'],r['seed'],r['alpha']);kind='unimplicitized_nonlinear'
 groups[label].append({'history_index':r['history_index'],'seed':r['seed'],'alpha':r['alpha'],'source_coefficient':r['source_coefficient'],'source_grassmannian_rank':r['source_grassmannian_rank'],'kind':kind})
items=[]
for label,branches in sorted(groups.items(),key=lambda z:str(z[0])):
 kinds={x['kind'] for x in branches};assert len(kinds)==1
 items.append({'target_label':str(label),'kind':next(iter(kinds)),'multiplicity':len(branches),'source_coefficient_sum':sum(x['source_coefficient'] for x in branches),'branches':branches})
summary=collections.Counter(x['kind'] for x in items);branch_summary=collections.Counter()
for x in items:branch_summary[x['kind']]+=x['multiplicity']
checks={'all_61_rank7_grouped':sum(x['multiplicity'] for x in items)==61,'one_label_per_branch':sum(x['multiplicity'] for x in items)==len(src['rank7_details']),'one_verified_quartic':summary['verified_quartic']==1,'no_unimplicitized_nonlinear_branches':branch_summary['unimplicitized_nonlinear']==0,'no_unproved_merging_of_unlabelled_images':all(x['multiplicity']==1 for x in items if x['kind']=='unimplicitized_nonlinear')}
out={'schema':'marici.nima.n8-target-boundary-grouping.v2','target_groups':len(items),'groups_by_kind':dict(summary),'branches_by_kind':dict(branch_summary),'groups_with_zero_naive_source_coefficient_sum':sum(x['source_coefficient_sum']==0 for x in items),'groups':items,'checks':checks,'passed':all(checks.values()),'claim_boundary':'Bracket equality certifies a common containing hypersurface, not equality of pushed-forward residues. Unimplicitized images are not merged. Source coefficient sums omit transition Jacobians, map degrees, and field traces.'};p=ROOT/'research/nima/results/n8-target-boundary-grouping.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='groups'},indent=2));raise SystemExit(0 if out['passed'] else 1)
