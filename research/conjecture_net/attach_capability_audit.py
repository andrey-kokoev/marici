"""Attach bounded capability gates and alternative synthesis forks, not proof outcomes."""
import json
from pathlib import Path

HOME = Path(__file__).resolve().parent


if __name__ == '__main__':
    hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v7.json').read_text())
    hierarchy.update(schema='marici.conjecture-net.programme-hierarchy.v8',
                     id='marici.relational-carrier-physics-programme.v8',
                     phase='audited_finite_capabilities_and_synthesis_forks',
                     predecessor='research/conjecture_net/contracts/programme-hierarchy.v7.json')
    hierarchy['capability_audits'] = [{
        'id': 'native-bool-action-observation-stability-audit.v1',
        'contract': 'research/conjecture_net/contracts/pilot-capability-audit.v1.json',
        'receipt': 'research/conjecture_net/results/pilot-capability-audit.json',
        'source_instance': 'native-bool-square-pilot',
        'target_obligations': ['carrier-and-geometric-dynamics', 'cross-sector-compatibility'],
        'status': 'exact_finite_ranks_and_hostiles_audited',
        'native_domain': 'four labels are reachable and mathematically separated',
        'expanded_domain': 'full unitary control absent; seven Hermitian directions invisible to current propagated readouts',
        'completion_boundary': 'positive finite bound only on visible coordinates; zero bound on full Hermitian domain',
        'proof_bearing': False, 'discharges_parent_obligation': False
    }]
    hierarchy['candidate_synthesis_forks'] = [
        {'id': 'retain-native-domain', 'proposal': 'Keep the finite witness as a process primitive without full-state quantum capability claims.',
         'required': ['An explicit narrow recovery target and physical bridge if physical interpretation is sought.'], 'status': 'candidate', 'outcome': None},
        {'id': 'authorize-richer-observers', 'proposal': 'Seek independently source-authorized probes sensitive to the missing Pauli directions.',
         'required': ['Preparation and complete instrument records', 'Calibration and source derivation, not kernel-targeted projector insertion'], 'status': 'candidate', 'outcome': None},
        {'id': 'authorize-richer-dynamics', 'proposal': 'Seek independent additional source/control structure beyond two commuting local flows.',
         'required': ['New source contract and provenance', 'Recheck locality, retained transport and control rank'], 'status': 'candidate', 'outcome': None},
        {'id': 'construct-richer-common-source', 'proposal': 'Construct a larger relational source generating the needed actions and observers.',
         'required': ['Typed embedding of the successful finite witness', 'Explicit geometry/readout transport', 'Completion estimates if dimensions grow'], 'status': 'candidate', 'outcome': None}
    ]
    content = json.dumps(hierarchy, indent=2, sort_keys=True) + '\n'
    destination = HOME / 'contracts/programme-hierarchy.v8.json'
    if destination.exists() and destination.read_text() != content:
        raise ValueError('Refusing implicit capability hierarchy correction')
    if not destination.exists():
        destination.write_text(content, encoding='utf-8')
    print('Recorded v8 capability boundaries and four candidate synthesis forks; no programme outcomes promoted.')
