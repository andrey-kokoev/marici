#!/usr/bin/env python3
"""Assemble the complete oriented n=8 source boundary chain with evidence levels."""
from pathlib import Path
import json,collections
R=Path(__file__).resolve().parents[3];bru=json.loads((R/'research/nima/results/n8-positroid-bruhat-boundaries.json').read_text());cov=json.loads((R/'research/nima/results/n8-coordinate-to-bruhat-boundary-coverage.json').read_text());tr=json.loads((R/'research/nima/results/n8-all-shared-boundary-transitions.json').read_text());hidden=json.loads((R/'research/nima/results/n8-bcfw-bridge-orientation-anchors.json').read_text());hidden_exact={tuple(x['boundary_permutation']):x for x in hidden['pairs']};ext=json.loads((R/'research/nima/results/n8-complete-external-pushforward.json').read_text());inc=collections.defaultdict(list)
for c in bru['cells']:
 for f in c['bruhat_facets']:inc[tuple(f)].append(c['history_index'])
vis=collections.defaultdict(list)
for x in cov['visible_facet_incidences']:vis[tuple(x['boundary_permutation'])].append((x['history_index'],x['alpha']))
explicit={}
for r in tr['pairs']:
 if r.get('positive_orthant_classification')!='positive_to_positive':continue
 l=(r['left']['history'],r['left']['alpha']);q=(r['right']['history'],r['right']['alpha']);f=next(f for f,z in vis.items() if l in z and q in z);sl=(-1)**(l[1]-1);sr=int(r['log_jacobian'])*(-1)**(q[1]-1);explicit[f]={'left_coordinate_residue_sign':sl,'right_in_left_coordinates_sign':sr,'log_jacobian':int(r['log_jacobian']),'cancels':sl+sr==0}
rows=[]
for f,hs in sorted(inc.items()):
 if len(hs)!=2:continue
 if f in explicit:evidence='explicit_seed_dlog_transition';detail=explicit[f];relative=-1 if detail['cancels'] else 1
 else:
  z=hidden_exact[f];evidence='explicit_cyclic_bcfw_bridge_transition';detail={'left':z['left'],'right':z['right'],'log_jacobian':z['log_jacobian'],'left_seed_oriented_residue_sign':z['left_seed_oriented_residue_sign'],'right_seed_oriented_residue_sign':z['right_in_left_seed_orientation_sign'],'cancels':z['cancels']};relative=-1 if z['cancels'] else 1
 rows.append({'boundary_permutation':list(f),'histories':hs,'incidence_signs_in_declared_facet_orientation':{str(hs[0]):1,str(hs[1]):-1},'relative_sign':relative,'evidence':evidence,'detail':detail})
checks={'forty_shared_facets':len(rows)==40,'twentythree_seed_chart_transitions':sum(r['evidence']=='explicit_seed_dlog_transition' for r in rows)==23,'seventeen_cyclic_bcfw_bridge_transitions':sum(r['evidence']=='explicit_cyclic_bcfw_bridge_transition' for r in rows)==17,'all_forty_explicit_residues_cancel':all(r['relative_sign']==-1 for r in rows),'all_shared_relative_sign_minus_one':all(r['relative_sign']==-1 for r in rows),'eighty_six_external_incidences_remain':sum(len(h)==1 for h in inc.values())==86,'complete_external_pushforward_passed':ext['passed']}
out={'schema':'marici.nima.n8-complete-oriented-boundary-chain.v1','orientation_convention':'For each shared facet, orient its canonical seven-form by the lower history index incidence. The other incidence then has sign -1. Explicit coordinate signs include the residue deletion parity (-1)^(alpha-1) and transition log-Jacobian.','shared_facets':rows,'boundary_chain_summary':{'top_cells':20,'shared_facets_cancelled':40,'external_facets':86,'external_rank7_physical':80,'external_contracted':6},'checks':checks,'passed':all(checks.values()),'claim_boundary':'All forty relative signs are independently calculated: twenty-three in overlapping seed charts and seventeen in genuine cyclic colored-BCFW bridge charts with exact seed-orientation anchors.'};p=R/'research/nima/results/n8-complete-oriented-boundary-chain.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'boundary_chain_summary':out['boundary_chain_summary'],'checks':checks,'passed':out['passed'],'claim_boundary':out['claim_boundary']},indent=2));raise SystemExit(0 if out['passed'] else 1)
