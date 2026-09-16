"""Fail-closed audit for the authoritative theta-history Green input."""
import json
from pathlib import Path
ROOT=Path(__file__).parents[2]
contract=json.loads((ROOT/'aspect'/'contracts'/'polarized-prime-cell-open-theorem.v1.json').read_text())
fixture=ROOT/'nima'/'contracts'/'g4-linking-fourier-poisson-candidate.v1.json'
required=['joint_sesquilinear_coefficients','common_form_domain','radical_quotient','F_covariance','P_covariance','even_wall_diagonal']
declared={k:False for k in required}
# The contract explicitly declares the linear data but not the authoritative quadratic form.
checks={'contract_status_open':contract['status']=='parameter_free_local_identity_open','Q_fixed':contract['fixed_source_data']['Q_p_lin']=='uniquely_determined','no_free_alpha':contract['fixed_source_data']['free_alpha_p'] is False,'four_identities_unconstructed':contract['open_theorem']['identity_count']==4 and contract['open_theorem']['constructed'] is False,'fixture_rejected_as_authority':contract['non_authoritative_fixture']['status']=='test_fixture_only','authoritative_theta_green_complete':all(declared.values())}
out={'schema':'marici.prime-cell-theta-green-input-audit.v1','required_authoritative_fields':required,'declared_authoritative_fields':declared,'checks':checks,'executable_matrix_unit_test':checks['authoritative_theta_green_complete'],'blocked_reason':'The fixed linear map is present, but no independently sourced theta-history Green form/domain/quotient and covariance package is declared. Substituting the test fixture or pullback metric would be circular.','next_source_artifact':'an authoritative contract declaring G_theta, its common form domain and radical quotient, F/P covariance, and the even-wall diagonal','passed':all(v for k,v in checks.items() if k!='authoritative_theta_green_complete') and not checks['authoritative_theta_green_complete']}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'prime-cell-theta-green-input-audit.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
