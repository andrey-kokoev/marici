"""Record scoped overlap obstruction/package without physical unification."""
import json
from pathlib import Path

HOME = Path(__file__).resolve().parent


if __name__ == '__main__':
    hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v11.json').read_text())
    hierarchy.update(schema='marici.conjecture-net.programme-hierarchy.v12',
                     id='marici.relational-carrier-physics-programme.v12',
                     phase='restricted_overlap_screen_and_indexed_package',
                     predecessor='research/conjecture_net/contracts/programme-hierarchy.v11.json')
    hierarchy['cross_source_overlap_screens'] = [{
        'id': 'bool-exchange-fixed-port-overlap-and-indexed-package.v1',
        'contract': 'research/conjecture_net/contracts/source-overlap-screen.v1.json',
        'implementation': 'research/conjecture_net/source_overlap_screen.py',
        'receipt': 'research/conjecture_net/results/source-overlap-screen-audit.json',
        'status': 'all_36_global_single_port_bindings_nonfaithful',
        'obstruction_scope': 'Global fixed-fibre single-port assignments only; not word-valued or endpoint-dependent bindings.',
        'bounded_typed_loop_screen': {'maximum_word_length': 12, 'closed_nonempty_word_count': 840,
                                    'faithful_fixed_fibre_native_flip_candidates': 0},
        'indexed_package_dimension': 26,
        'package_role': 'faithful_isometric_source_indexed_alternatives',
        'cross_source_identification': 'not_constructed',
        'one_common_physical_witness': 'not_proved',
        'cross_component_arrows': 'not_supplied',
        'admission_status': 'not_admitted_as_new_programme_proof_link',
        'proof_bearing': False, 'discharges_parent_obligation': False
    }]
    hierarchy['next_overlap_gates'] = [
        'Source an observable/attachment overlap beyond uncalibrated scalar budget conservation.',
        'Specify word-valued or endpoint-dependent maps and prove attachment, composition, retained-record and coherencer laws.',
        'Derive a cross-component coupling or common preparation/instrument model; arbitrary matrices on C26 are not authorized.'
    ]
    content = json.dumps(hierarchy, indent=2, sort_keys=True) + '\n'
    destination = HOME / 'contracts/programme-hierarchy.v12.json'
    if destination.exists() and destination.read_text() != content:
        raise ValueError('Refusing implicit overlap hierarchy correction')
    if not destination.exists():
        destination.write_text(content, encoding='utf-8')
    print('Recorded v12: restricted overlap obstruction and faithful source-indexed package; physical unification open.')
