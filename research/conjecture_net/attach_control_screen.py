"""Attach conditional control choices without selecting a physical source."""
import json
from pathlib import Path

HOME = Path(__file__).resolve().parent


if __name__ == '__main__':
    hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v9.json').read_text())
    hierarchy.update(schema='marici.conjecture-net.programme-hierarchy.v10',
                     id='marici.relational-carrier-physics-programme.v10',
                     phase='screened_conditional_control_source_extensions',
                     predecessor='research/conjecture_net/contracts/programme-hierarchy.v9.json')
    hierarchy['conditional_control_screens'] = [{
        'id': 'conditional-finite-control-source-enrichment-screen.v1',
        'contract': 'research/conjecture_net/contracts/pilot-control-screen.v1.json',
        'implementation': 'research/conjecture_net/pilot_controls.py',
        'receipt': 'research/conjecture_net/results/pilot-control-screen.json',
        'source_instance': 'native-bool-square-pilot',
        'status': 'exact_lie_closures_audited_under_explicit_extra_premises',
        'successful_conditional_family': 'local-phase-plus-exchange',
        'physical_source_selection': 'not_supplied',
        'phase_framing': 'assumed_not_physically_supplied',
        'proof_bearing': False, 'discharges_parent_obligation': False
    }]
    for fork in hierarchy['candidate_synthesis_forks']:
        if fork['id'] == 'authorize-richer-dynamics':
            fork['conditional_mathematical_subbranch'] = 'Local marked-phase controls plus an exchange interaction have u(4) Lie closure; permutation-only projector controls fix the uniform vector and cannot exceed u(3).'
            fork['source_authorization_gate'] = 'Additional operations, independent coefficients and relative phase standard need a new justified source/control contract.'
    hierarchy['next_source_bridge_candidates'] = [{
        'id': 'retained-noncommuting-exchange-source-adapter',
        'review_source': 'research/nima/exchange-contact-gate-comparison.md',
        'status': 'candidate_not_constructed',
        'required': ['Typed source/target state and record domains', 'Actual assignment of noncommuting port operations',
                     'Composition/coherencer and source attachment laws', 'Phase framing and source/control authority'],
        'boundary': 'The existing exchange source is not identified with this C4 pilot; its mismatch response must not be erased by a commuting target adapter.',
        'outcome': None
    }]
    content = json.dumps(hierarchy, indent=2, sort_keys=True) + '\n'
    destination = HOME / 'contracts/programme-hierarchy.v10.json'
    if destination.exists() and destination.read_text() != content:
        raise ValueError('Refusing implicit control hierarchy correction')
    if not destination.exists():
        destination.write_text(content, encoding='utf-8')
    print('Recorded v10 conditional control ranks and source-authorization gates; no physical actuation inferred.')
