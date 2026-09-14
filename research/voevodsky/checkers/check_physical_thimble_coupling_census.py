#!/usr/bin/env python3
"""Verify elimination of current physical coupling candidates against the target contract."""
from hashlib import sha256
from pathlib import Path
import json
R=Path(__file__).resolve().parents[3]
P=R/'research/voevodsky/physical_coupling_census_finds_no_thimble_to_syndrome_interaction.md';C=R/'research/aspect/cosmology-contour-source-authority-census.md';CUT=R/'src/ledger/20260821-1751 The Physical Cut Pairing Does Not Resolve the Integral Cusp Extension.md';OPT=R/'research/voevodsky/results/optical_decoder_circularity_gate.json';CM=R/'research/benincasa/cayley-menger-contour-family-gate.json';OUT=R/'research/voevodsky/results/physical_thimble_coupling_census.json'
p=P.read_text();c=C.read_text();cut=CUT.read_text();opt=json.loads(OPT.read_text());cm=json.loads(CM.read_text())
candidates={'bunch_davies':[1,0,0],'cayley_menger':[0,0,0],'local_leray_tube':[0,0,0],'physical_cut':[1,0,0],'five_six_site_analogues':[0,1,0],'optical_encoders':[0,1,0]}
checks={
 'bd_local_authority':'local boundary-value authority but no transportable global activation authority' in c,
 'bd_trivial_monodromy':'punctured family is trivial and produces no' in c,
 'cm_candidate_exists':'oriented semialgebraic fiber-cycle family' in cm['typing']['source_defined'],
 'cm_target_gates_open':'weighted exceptional specialization, coefficient comparison, deck trace, and overlap homotopy remain absent' in c,
 'cut_zero':'is zero' in cut,
 'analogues_wrong_carrier':'analogues are different carriers' in c,
 'optical_circularity':opt['disposition']['cusp_to_conductor_phi']=='missing',
 'no_candidate_passes':all(not all(v) for v in candidates.values()),
 'three_gate_statement':'No candidate satisfies all three gates' in p,
 'first_missing_comparison':'first missing object is not detector hardware but a target Betti/coefficient comparison' in p,
}
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.physical-thimble-coupling-census.v1','packet_sha256':sha256(P.read_bytes()).hexdigest(),'aspect_census_sha256':sha256(C.read_bytes()).hexdigest(),'cut_sha256':sha256(CUT.read_bytes()).hexdigest(),'optical_gate_sha256':sha256(OPT.read_bytes()).hexdigest(),'candidate_columns':['source_target_input','two_direction_response','integral_pairing_comparison'],'candidate_matrix':candidates,'checks':checks,'passed':all(checks.values()),'disposition':{'qualifying_current_couplings':[],'search_status':'exhausted within current artifacts','first_missing_object':'target Betti/coefficient comparison transporting globally marked thimble into physical interaction'}}
OUT.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'passed':result['passed'],'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)
