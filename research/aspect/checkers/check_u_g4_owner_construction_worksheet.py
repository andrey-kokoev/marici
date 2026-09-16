#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
p=R/'research/aspect/contracts/u-g4-owner-construction-worksheet.v1.json'
x=json.loads(p.read_text())
owner=x['owner_fill_only']; fw=x['construction_firewall']; gate=x['promotion_gate']
forbidden=set(fw['forbidden_inputs'])
checks={
 'awaiting_owner':x['status']=='awaiting_independent_g4_owner_input',
 'thirteen_owner_fields':len(owner)==13,
 'no_prefill_disguised_as_owner_data':all(v is None for v in owner.values()),
 'comparison_map_firewalled':'T_pair_to_border' in forbidden,
 'comparison_locator_firewalled':'research/aspect/contracts/polarized-pair-to-bordered-radial-crossing.v1.json' in forbidden,
 'transfer_record_firewalled':'research/voevodsky/r-zeta-u-g4-transfer-record-v3.json' in forbidden,
 'comparison_postconstruction':set(fw['allowed_only_after_construction'])=={'typing comparison','forward defect','Xi-ideal divisibility','Evans jet evaluation'},
 'owner_equation_provenance_required':'owner-side G4 source equation' in fw['derivation_rule'],
 'all_gates_closed':all(v is False for v in gate.values()),
 'packet_schema_exists':(R/x['output_packet_schema']).exists(),
 'comparison_context_read_only':x['read_only_context']['comparison_map_name']=='T_pair_to_border',
 'rh_not_promoted':x['rh_implication'] is False}
out={'schema':'marici.aspect.u-g4-owner-construction-worksheet-check.v1','passed':all(checks.values()),'checks':checks,'owner_fields':list(owner),'promotion_state':'blocked_pending_owner_input','verdict':'worksheet is noncircular by construction: comparison artifacts are context-only and explicitly forbidden to the derivation'}
q=R/'research/aspect/results/u_g4_owner_construction_worksheet.check.v1.json';q.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
