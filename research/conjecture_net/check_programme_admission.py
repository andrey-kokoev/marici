"""Validate the accepted prerequisite attachment, not physical programme closure."""
import json
from pathlib import Path
from admit_structural_overlap import check, NET, CLAIM, POINTER
from outcome_reference import require

HOME = Path(__file__).resolve().parent


def validate(hierarchy):
    previous = json.loads((HOME / 'contracts/programme-hierarchy.v5.json').read_text(encoding='utf-8'))
    require(hierarchy['phase'] == 'accepted_finite_structural_prerequisite', 'wrong admission phase')
    for key in ('root', 'obligations', 'promotion_policy', 'existing_net_links', 'target_links'):
        require(hierarchy[key] == previous[key], 'programme outcome/scope changed: ' + key)
    links = hierarchy['admitted_prerequisite_links']
    require(len(links) == 1, 'unexpected admitted prerequisite count')
    link = links[0]
    require(link['source_net'] == NET and link['source_claim'] == CLAIM and link['outcome_pointer'] == POINTER,
            'wrong scoped prerequisite')
    require(link['target_obligation'] == 'cross-sector-compatibility' and link['relation'] == 'supplies_scoped_prerequisite'
            and link['status'] == 'admitted' and link['proof_bearing'] is True, 'wrong admitted link type')
    require(link['discharges_parent_obligation'] is False and link['scope_transport'] and link['witness_transport'],
            'prerequisite promoted to parent closure')
    resolved = check()
    require(link['verification_boundary'] == resolved['verification'], 'admission verification level changed')
    current = hierarchy['current_finite_overlap_admission']
    require(current['outcome'] == '++' and current['source_claim'] == CLAIM and current['outcome_pointer'] == POINTER,
            'wrong admitted finite outcome')
    require(current['physical_overlap'] == 'not_defined' and current['universal_carrier_embedding'] == 'not_proved',
            'physical/universal promotion')
    return {'status': 'pass', 'validation_only': True, 'accepted_finite_prerequisite_outcome': '++',
            'admitted_prerequisite_links': 1, 'root_outcome': None,
            'parent_obligation_discharged': False, 'programme_pilot_outcomes_promoted': False,
            'physical_verification': False}


if __name__ == '__main__':
    hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v6.json').read_text(encoding='utf-8'))
    print(json.dumps(validate(hierarchy), indent=2))
