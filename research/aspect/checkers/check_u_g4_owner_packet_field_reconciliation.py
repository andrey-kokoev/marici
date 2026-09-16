#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
s=json.loads((R/'research/aspect/contracts/u-g4-owner-construction-packet.schema.v1.json').read_text())
x=json.loads((R/'research/aspect/results/u_g4_owner_packet_field_reconciliation.v1.json').read_text())
statuses=[f['status'] for f in x['fields']]
missing=sum(v=='missing' for v in statuses)
partial=sum(v in {'partial','partial_surrogate','schema_only'} for v in statuses)
sub=sum(v=='substantially_available' for v in statuses)
avail=sum(v=='available' for v in statuses)
paths=[f['source'] for f in x['fields'] if 'source' in f]
checks={
 'schema_draft':s['$schema'].endswith('2020-12/schema'),
 'packet_required_complete':set(s['required'])=={'schema','owner','authority','source_carrier','target_carrier','pairings','forward_map','placement','provenance','independence','completion','claim_boundary'},
 'forbids_extra':s['additionalProperties'] is False,
 'requires_U_G4':s['properties']['forward_map']['properties']['name']['const']=='U_G4',
 'comparison_postconstruction':s['properties']['independence']['properties']['comparison_is_postconstruction']['const'] is True,
 'forbids_TPB_dependency':s['properties']['independence']['properties']['forbidden_dependencies']['contains']['const']=='T_pair_to_border',
 'field_count':len(statuses)==x['counts']['total']==14,
 'counts':(missing,partial,sub,avail)==(x['counts']['missing'],x['counts']['partial_or_schema'],x['counts']['substantially_available'],x['counts']['available']),
 'all_sources_exist':all((R/p).exists() for p in paths),
 'packet_absent':x['complete_packet_exists'] is False,
 'first_math_block':x['first_mathematical_blocking_field']=='target_carrier',
 'first_map_block':x['first_map_blocking_field']=='forward_map.formula',
 'rh_not_promoted':x['rh_implication'] is False}
out={'schema':'marici.aspect.u-g4-owner-packet-field-reconciliation-check.v1','passed':all(checks.values()),'checks':checks,'counts':{'missing':missing,'partial_or_schema':partial,'substantially_available':sub,'available':avail},'verdict':'owner packet schema fixed; seven fields missing; target carrier is first mathematical blocker'}
(R/'research/aspect/results/u_g4_owner_packet_field_reconciliation.check.v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
