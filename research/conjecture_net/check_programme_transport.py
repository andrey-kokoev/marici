"""Check the v4 attachment of audited finite transport, without admitting it."""
import hashlib
import json
from pathlib import Path
from check_programme_pilots import documents, validate as validate_pilots
from check_structural_pilot_transport import validate_contract, check_export, POINTER, algebra_audit

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[1]


def validate(hierarchy, audit):
    def require(condition, message):
        if not condition:
            raise ValueError(message)
    previous = documents()
    validate_pilots(*previous)
    old = previous[0]
    require(hierarchy['phase'] == 'defined_finite_structural_pilot_transport', 'wrong transport phase')
    for key in ('root', 'obligations', 'structural_edges', 'existing_net_links', 'promotion_policy', 'target_links'):
        require(hierarchy[key] == old[key], 'programme obligations/outcomes changed: ' + key)
    links = hierarchy['structural_pilot_transports']
    require(len(links) == 1, 'unexpected transport count')
    link = links[0]
    require(link['proof_bearing'] is False and link['admission_status'] == 'not_admitted_as_programme_proof_link',
            'transport prematurely admitted')
    require(link['relation'] == 'defined_same_witness_transport', 'wrong transport relation')
    path = (ROOT / link['contract']).resolve()
    require(path.is_relative_to(ROOT) and not Path(link['contract']).is_absolute(), 'contract escapes repository')
    require(hashlib.sha256(path.read_bytes()).hexdigest() == link['contract_sha256'], 'transport contract drift')
    contract = json.loads(path.read_text(encoding='utf-8'))
    validate_contract(contract)
    require(link['id'] == contract['id'] and link['targets'] == contract['targets'] and
            link['source_instance'] == contract['source_instance'], 'transport attachment mismatch')
    require(audit['status'] == 'pass' and audit['validation_only'] is True and audit['claim'] == link['id'], 'invalid transport audit')
    require(audit['outcome'] is None and audit['root_outcome'] is None and
            audit['target_outcomes_promoted'] is False and audit['new_transport_kernel_proved'] is False and
            audit['physical_recovery_verified'] is False and audit['universal_carrier_embedding_proved'] is False,
            'audit verification/outcome overclaim')
    for relative, expected in audit['source_sha256'].items():
        source = (ROOT / relative).resolve()
        require(source.is_relative_to(ROOT) and not Path(relative).is_absolute(), 'audit source escapes repository')
        require(hashlib.sha256(source.read_bytes()).hexdigest() == expected, 'stale transport audit source: ' + relative)
    require(audit['exact_coordinate_controls'] == algebra_audit(), 'coordinate audit mismatch')
    current_import = check_export(json.loads((ROOT / POINTER).read_text(encoding='utf-8')))
    require(audit['imported_operational_evidence'] == current_import, 'operational import changed')
    return {'status': 'pass', 'validation_only': True, 'defined_finite_transports': 1,
            'programme_proof_links_admitted': 0, 'root_outcome': None,
            'boundary': 'Live mathematical transport audit attachment, not kernel transport or physical verification.'}


if __name__ == '__main__':
    hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v4.json').read_text(encoding='utf-8'))
    audit = json.loads((HOME / 'results/structural-pilot-transport-audit.json').read_text(encoding='utf-8'))
    print(json.dumps(validate(hierarchy, audit), indent=2))
