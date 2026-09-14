#!/usr/bin/env python3
"""Audit whether the Aspect classifier supplies the required physical chain interface."""
from hashlib import sha256
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/physical_descent_test_stops_at_missing_sector_chain_map.md';RESULT=ROOT/'research/voevodsky/results/physical_descent_interface_gate.json';CONTRACT=ROOT/'research/aspect/contracts/relative-cech-de-rham-interferometer.v1.json';ASPECT_RESULT=ROOT/'research/aspect/results/relative_cech_de_rham_interferometer.json';SCOPE=ROOT/'research/aspect/the-two-term-target-complex-is-not-yet-the-specialization-mapping-cone.md'
c=json.loads(CONTRACT.read_text(encoding='utf-8'));r=json.loads(ASPECT_RESULT.read_text(encoding='utf-8'));scope=SCOPE.read_text(encoding='utf-8');checks={}
checks['candidate_result_passed']=r['status']=='passed'
checks['relative_target_closed']=r['residue_cocycle_closed'] is True
checks['hypothetical_column_algebraically_sufficient']=all(r['regimes']['sourced_exceptional_total_lift']['target_in_incoming_span'].values())
checks['contract_declares_constructor_missing']=c['source_authority_gate']['currently_constructed'] is False
checks['result_declares_simulation_only']=r['simulation_only'] is True
checks['source_derived_constructor_absent']=r['exceptional_constructor_source_derived'] is False
checks['total_lift_absent']=r['total_lift_constructed'] is False
checks['physical_readout_absent']=r['global_contour_constructed'] is False and r['physical_period_constructed'] is False
checks['mapping_cone_not_computed']='does not assemble the block differential of the mapping cone' in scope
checks['required_image_exact']=c['source_authority_gate']['required_image']==[1,1]
checks['no_substitute_boundary_retained']='not an admissible substitute' in PACKET.read_text(encoding='utf-8');checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.physical-descent-interface-gate.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'audited_inputs':{str(p.relative_to(ROOT)).replace('\\','/'):sha256(p.read_bytes()).hexdigest() for p in (CONTRACT,ASPECT_RESULT,SCOPE)},'checks':checks,'passed':all(checks.values()),'gate':{'status':'blocked','first_missing_typed_object':c['source_authority_gate']['required_constructor'],'required_image':c['source_authority_gate']['required_image'],'reopen_when':'source-derived map, complete mapping-cone differential/homology, and physical contour/readout authority are materialized'},'nonverification':'classifier adequacy does not establish a physical contraction-descent obstruction'}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'gate':result['gate'],'checks':checks}));raise SystemExit(0 if result['passed'] else 1)
