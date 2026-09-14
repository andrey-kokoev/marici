#!/usr/bin/env python3
"""Cross-check the audited source candidates for the minimal Aspect generator."""
from hashlib import sha256
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/minimal_aspect_source_realization_fiber_is_empty.md';RESULT=ROOT/'research/voevodsky/results/minimal_aspect_source_realization_gate.json'
paths={
 'exceptional':ROOT/'research/benincasa/cosmology-cayley-menger-exceptional-incoming-generator-audit.md',
 'face_cone':ROOT/'research/benincasa/cosmology-existing-relative-face-cone-primitive-map-audit.md',
 'realization':ROOT/'research/benincasa/cosmology-minimal-extension-source-realization-functor.md'}
text={k:p.read_text(encoding='utf-8') for k,p in paths.items()};checks={
 'blowup_column_is_0_1':'column \\((0,1)\\)' in text['exceptional'],
 'cm_specialization_absent':'weighted-Rees specialization' in text['exceptional'] and 'does not yet supply' in text['exceptional'],
 'physical_wall_absolute_lift_absent':'no absolute lift is selected' in text['exceptional'],
 'face_cone_only_conditionally_forces_1_1':'chain-map equations would uniquely force the primitive integral column' in text['face_cone'] and 'conditional uniqueness is not a construction' in text['face_cone'],
 'incoming_generator_absent':'no incoming generator' in text['face_cone'],
 'realization_fiber_empty':'realization fiber is empty on the audited candidate subcategory' in text['realization'],
 'outside_envelope_not_excluded':'outside the audited envelope' in text['realization'],
 'scope_retained':'does not prove that no suitable geometric source exists outside that envelope' in PACKET.read_text(encoding='utf-8')}
checks={k:bool(v) for k,v in checks.items()};result={'schema':'marici.voevodsky.minimal-aspect-source-realization-gate.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'audited_inputs':{k:{'path':str(p.relative_to(ROOT)).replace('\\','/'),'sha256':sha256(p.read_bytes()).hexdigest()} for k,p in paths.items()},'checks':checks,'passed':all(checks.values()),'gate':{'status':'blocked_at_object_assignment','first_missing_constructor':'weighted exceptional specialization of sourced Cayley-Menger incidence family with comparisons to Xi_log and blow-up face','required_image':[1,1],'reopen_condition':'materialize that source object and both typed comparison legs'},'nonverification':'formal sphere map remains algebraic only'}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'gate':result['gate'],'checks':checks}));raise SystemExit(0 if result['passed'] else 1)
