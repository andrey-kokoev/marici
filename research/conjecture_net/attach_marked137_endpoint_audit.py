"""Attach source-table endpoint audit without selecting intended T9."""
import json
from pathlib import Path

HOME = Path(__file__).resolve().parent


if __name__ == '__main__':
    hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v12.json').read_text())
    hierarchy.update(schema='marici.conjecture-net.programme-hierarchy.v13',
                     id='marici.relational-carrier-physics-programme.v13',
                     phase='marked137_endpoint_roles_and_partial_readout',
                     predecessor='research/conjecture_net/contracts/programme-hierarchy.v12.json')
    hierarchy['source_endpoint_audits'] = [{
        'id': 'marked137-endpoint-role-audit-v1',
        'contract': 'research/conjecture_net/contracts/marked137-endpoint-audit.v1.json',
        'implementation': 'research/conjecture_net/marked137_endpoint_audit.py',
        'receipt': 'research/conjecture_net/results/marked137-endpoint-audit.json',
        'source_stratum': 'supplied137-row shared-leg rational comparison fixture',
        'status': 'assembly_and_carrier_index_roles_separated_partial_observer_constructed',
        'carrier_target_keys': 32, 'assembly_target_keys': 1,
        'parent153_marked137_overlap': 130, 'partial_endpoint_readouts': 145,
        'full_response_descent': False, 'readout_is_invertible_connector': False,
        'intended_T9_selected': False, 'physical_readout_authorized': False,
        'admission_status': 'not_admitted_as_new_programme_proof_link',
        'proof_bearing': False, 'discharges_parent_obligation': False
    }]
    hierarchy['endpoint_role_binding_gate'] = {
        'first_missing_object': 'Intended rung-table endpoint-role map, distinct from a fixture grouping convention.',
        'acceptance_test': 'Name each column role, preserve original row/path attachment and specify the admitted composition domain.',
        'response_level_readout_gate': 'Supply an operation/readout law; endpoint-index lookup cannot substitute for full response transport.',
        'authority_only_branch_actionable': False
    }
    content = json.dumps(hierarchy, indent=2, sort_keys=True) + '\n'
    destination = HOME / 'contracts/programme-hierarchy.v13.json'
    if destination.exists() and destination.read_text() != content:
        raise ValueError('Refusing implicit endpoint-role hierarchy correction')
    if not destination.exists():
        destination.write_text(content, encoding='utf-8')
    print('Recorded v13: distinct endpoint roles and a partial retained observer; no intended-T9 or physical promotion.')
