"""Validate v8 finite capability boundaries and synthesis forks, not their solutions."""
import hashlib
import json
from pathlib import Path
from check_pilot_capabilities import audit as exact_audit, validate_contract
from check_programme_carrier import validate as validate_carrier

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(hierarchy, receipt):
    old = json.loads((HOME / 'contracts/programme-hierarchy.v7.json').read_text())
    carrier = validate_carrier(old, json.loads((HOME / 'results/pilot-carrier-interface-audit.json').read_text()))
    require(hierarchy['phase'] == 'audited_finite_capabilities_and_synthesis_forks', 'wrong capability phase')
    for key in ('root', 'obligations', 'admitted_prerequisite_links', 'implemented_source_fragments', 'promotion_policy'):
        require(hierarchy[key] == old[key], 'programme outcome/scope changed: ' + key)
    audits = hierarchy['capability_audits']
    require(len(audits) == 1 and audits[0]['proof_bearing'] is False and audits[0]['discharges_parent_obligation'] is False,
            'capability audit promoted to programme closure')
    contract = json.loads((HOME / 'contracts/pilot-capability-audit.v1.json').read_text())
    validate_contract(contract)
    require(receipt['status'] == 'pass' and receipt['validation_only'] is True and receipt['outcome'] is None
            and receipt['root_outcome'] is None and receipt['new_kernel_proof'] is False
            and receipt['physical_capabilities_authorized'] is False and receipt['programme_target_outcomes_promoted'] is False,
            'capability receipt verification upgrade')
    for path, expected in receipt['source_sha256'].items():
        source = (ROOT / path).resolve()
        require(source.is_relative_to(ROOT) and not Path(path).is_absolute(), 'source escapes repository')
        require(hashlib.sha256(source.read_bytes()).hexdigest() == expected, 'stale capability source: ' + path)
    require(receipt['gates'] == exact_audit(), 'capability controls changed')
    require(receipt['live_finite_fragment_validation'] == carrier, 'finite fragment validation changed')
    forks = hierarchy['candidate_synthesis_forks']
    require(len(forks) == 4 and len({fork['id'] for fork in forks}) == 4, 'synthesis fork coverage changed')
    require(all(fork['status'] == 'candidate' and fork['outcome'] is None and fork['required'] for fork in forks),
            'synthesis fork prematurely solved')
    return {'status': 'pass', 'validation_only': True, 'candidate_forks': 4,
            'continuous_control_dimension': 2, 'propagated_hermitian_observation_rank': 9,
            'invisible_directions': 7, 'root_outcome': None, 'physical_capabilities_authorized': False,
            'boundary': 'Correct audit of restricted capabilities; not success of full control/observation or physical synthesis.'}


if __name__ == '__main__':
    hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v8.json').read_text())
    receipt = json.loads((HOME / 'results/pilot-capability-audit.json').read_text())
    print(json.dumps(validate(hierarchy, receipt), indent=2))
