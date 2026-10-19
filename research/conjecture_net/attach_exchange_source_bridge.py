"""Attach a second sourced structural instance; never identify physical witnesses."""
import json
from pathlib import Path

HOME = Path(__file__).resolve().parent


if __name__ == '__main__':
    hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v10.json').read_text())
    hierarchy.update(schema='marici.conjecture-net.programme-hierarchy.v11',
                     id='marici.relational-carrier-physics-programme.v11',
                     phase='constructed_retained_exchange_metric_bridge',
                     predecessor='research/conjecture_net/contracts/programme-hierarchy.v10.json')
    hierarchy['retained_source_bridges'] = [{
        'id': 'retained-exchange-to-metric-spectral-source-bridge.v1',
        'contract': 'research/conjecture_net/contracts/exchange-source-bridge.v1.json',
        'implementation': 'research/conjecture_net/exchange_source_bridge.py',
        'receipt': 'research/conjecture_net/results/exchange-source-bridge-audit.json',
        'source_instance': 'conditional-six-port-retained-exchange',
        'target_carrier': 'C16 anchor direct_sum C6 mismatch with the transported positive source metric',
        'status': 'faithful_structural_adapter_constructed_and_exactly_audited',
        'physical_source_bridge': 'not_supplied',
        'cross_source_common_physical_witness': 'not_proved',
        'free_global_control_switching': 'not_supplied',
        'admission_status': 'not_admitted_as_new_programme_proof_link',
        'proof_bearing': False, 'discharges_parent_obligation': False
    }]
    for candidate in hierarchy['next_source_bridge_candidates']:
        if candidate['id'] == 'retained-noncommuting-exchange-source-adapter':
            candidate['status'] = 'structural_adapter_constructed_physical_bridge_open'
            candidate['constructed_target'] = 'Faithful positive-metric C16 plus C6 spectral realization, not C4 or commuting fixed gates.'
    hierarchy['shared_finite_structural_recipe'] = {
        'instances': ['native-bool-square-pilot', 'conditional-six-port-retained-exchange'],
        'signature': ['finite positive metric', 'metric-preserving involutive operation', 'explicit source/port attachment',
                      'retained execution records', 'uniform spectral-projector realization', 'metric Hamiltonian realification'],
        'status': 'two_scoped_mathematical_instances',
        'one_common_physical_witness': False,
        'cross_source_transport_maps': None
    }
    content = json.dumps(hierarchy, indent=2, sort_keys=True) + '\n'
    destination = HOME / 'contracts/programme-hierarchy.v11.json'
    if destination.exists() and destination.read_text() != content:
        raise ValueError('Refusing implicit exchange-bridge hierarchy correction')
    if not destination.exists():
        destination.write_text(content, encoding='utf-8')
    print('Recorded v11: second sourced structural realization, without physical-witness or control promotion.')
