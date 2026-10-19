"""Validate the finite implemented fragment attachment and its live audit."""
import hashlib
import json
from pathlib import Path
from check_programme_admission import validate as validate_admission
from check_pilot_carrier_interface import validate_contract, validate_dossier, record_audit
from admit_structural_overlap import check as check_overlap

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(hierarchy, audit):
    previous = json.loads((HOME / 'contracts/programme-hierarchy.v6.json').read_text())
    validate_admission(previous)
    require(hierarchy['phase'] == 'implemented_finite_source_fragment', 'wrong fragment phase')
    for key in ('root', 'obligations', 'admitted_prerequisite_links', 'existing_net_links', 'promotion_policy'):
        require(hierarchy[key] == previous[key], 'programme scope/outcomes changed: ' + key)
    fragments = hierarchy['implemented_source_fragments']
    require(len(fragments) == 1, 'unexpected fragment count')
    fragment = fragments[0]
    require(fragment['source_instance'] == 'native-bool-square-pilot' and fragment['proof_bearing'] is False and
            fragment['discharges_parent_obligation'] is False and
            fragment['admission_status'] == 'not_admitted_as_new_programme_proof_link', 'finite adapter promoted beyond scope')
    contract_path = (ROOT / fragment['contract']).resolve()
    require(contract_path.is_relative_to(ROOT) and not Path(fragment['contract']).is_absolute(), 'contract escapes repository')
    require(hashlib.sha256(contract_path.read_bytes()).hexdigest() == fragment['contract_sha256'], 'adapter contract drift')
    contract = json.loads(contract_path.read_text())
    validate_contract(contract)
    validate_dossier(json.loads((HOME / 'contracts/pilot-source-records.v1.json').read_text()))
    require(audit['status'] == 'pass' and audit['validation_only'] is True and audit['claim'] == fragment['id'], 'invalid fragment audit')
    require(audit['outcome'] is None and audit['root_outcome'] is None, 'fragment outcome promotion')
    require(all(audit[key] is False for key in ('new_adapter_kernel_proved', 'full_native_agda_tick_executed_in_python',
                'universal_carrier_embedding_proved', 'physical_readout_authorized', 'programme_target_outcomes_promoted')),
            'fragment verification upgrade')
    for path, expected in audit['source_sha256'].items():
        resolved = (ROOT / path).resolve()
        require(resolved.is_relative_to(ROOT) and not Path(path).is_absolute(), 'source escapes repository')
        require(hashlib.sha256(resolved.read_bytes()).hexdigest() == expected, 'stale fragment source: ' + path)
    require(audit['controls'] == record_audit(), 'record controls changed')
    require(audit['imported_finite_overlap'] == check_overlap(), 'accepted finite prerequisite changed')
    return {'status': 'pass', 'validation_only': True, 'implemented_finite_fragments': 1,
            'accepted_scoped_prerequisites': 1, 'new_adapter_admitted': False,
            'universal_carrier_embedding_proved': False, 'physical_authorization': False, 'root_outcome': None}


if __name__ == '__main__':
    hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v7.json').read_text())
    audit = json.loads((HOME / 'results/pilot-carrier-interface-audit.json').read_text())
    print(json.dumps(validate(hierarchy, audit), indent=2))
