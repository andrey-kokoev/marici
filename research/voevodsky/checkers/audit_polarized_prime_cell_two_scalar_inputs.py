#!/usr/bin/env python3
"""Fail-closed audit separating analytic candidates from authoritative inputs."""
import json, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
contract_path=ROOT/'research/voevodsky/contracts/polarized-prime-cell-two-scalar-closure.v1.json'
template_path=ROOT/'research/aspect/contracts/polarized-prime-cell-authoritative-input.template.v1.json'
c=json.loads(contract_path.read_text());t=json.loads(template_path.read_text());r=c['required_source_inputs'];e=c['candidate_evidence']
evidence_exists={k:(ROOT/v).is_file() for k,v in e.items() if k.endswith('dossier') or k.endswith('contract')}
checks={
 'fixed_Q_matches_template_basis':t['basis_theta']==['even_wall','odd_quarter_turn'],
 'authoritative_template_unfilled':t['status']=='unfilled_authoritative_input_template',
 'candidate_evidence_files_exist':all(evidence_exists.values()),
 'GSt_candidate_present_but_unauthorized':bool(e['candidate_G_St']) and r['G_St_authority'] is None,
 'Gtheta_diagonal_candidate_present':bool(e['candidate_G_theta_diagonal']),
 'Gtheta_mixed_operator_candidate_present':(ROOT/e['candidate_G_theta_mixed_operator']).is_file() and r['L_p_green_mate'] is not None,
 'Gtheta_analytic_candidate_complete_but_unauthorized':r['G_theta_complete']=='candidate_only' and r['G_theta_authority'] is None,
 'candidate_common_domain_present_but_unauthorized':bool(e['candidate_common_domain']) and r['common_form_domain_authority'] is None,
 'F_intertwiners_absent':r['F_intertwiner_St'] is None and r['F_intertwiner_theta'] is None,
 'antiunitary_intertwiners_absent':r['antiunitary_P_intertwiner_St'] is None and r['antiunitary_P_intertwiner_theta'] is None,
 'two_scalar_equalities_absent':r['even_wall_equality'] is None and r['oriented_linking_equality'] is None,
}
blocking=[k for k,v in r.items() if v is None]
out={'schema':'marici.voevodsky.polarized-prime-cell-two-scalar-input-audit.v2','contract_sha256':hashlib.sha256(contract_path.read_bytes()).hexdigest(),'template_sha256':hashlib.sha256(template_path.read_bytes()).hexdigest(),'candidate_evidence':e,'candidate_evidence_files_exist':evidence_exists,'checks':checks,'blocking_authoritative_fields':blocking,'comparison_executable':False,'passed':all(checks.values()),'correction':'G_St, the common plane, and a complete analytic theta candidate including the bounded mixed linking operator are present; independent quadratic identification and authority remain absent.','first_non_circular_executable_step':'freeze the independently constructed complete G_St and H_theta matrices on E_p,12 with the fixed Q_p^lin, then evaluate the parameter-free residual coordinates a_p and b_p','rh_proved':False};p=ROOT/'research/voevodsky/results/polarized_prime_cell_two_scalar_input_audit.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
