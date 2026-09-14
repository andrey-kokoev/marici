#!/usr/bin/env python3
"""Audit which registered coherence-pyramid cells carry invertibility gates."""
import json
from pathlib import Path

ROOT = Path(__file__).parents[1]

def main():
    laws = json.loads((ROOT / 'coherence-pyramid-cells-and-laws.json').read_text())
    signature = json.loads((ROOT / 'coherence-pyramid-computad-signature.json').read_text())
    cells = laws['cells']
    gated = {name: spec['invertibility'] for name, spec in cells.items() if 'invertibility' in spec}
    ungated = sorted(set(cells) - set(gated))
    assert set(gated) == {'beck_chevalley', 'completion_comparison'}
    assert 'all_beck_chevalley_cells_are_invertible' in laws['nonclaims']
    assert laws['refusals']['beck_chevalley_invertibility_assumed'] == 'comparison inverse lacks certificate preservation'
    registered_two = set(signature['two_generators'])
    absent = [name for name in ('meaning_plane', 'transport_plane') if name not in registered_two and name not in cells]
    assert absent == ['meaning_plane', 'transport_plane']
    result = {
        'schema': 'marici.voevodsky.coherence-pyramid-plane-invertibility-gate.v1',
        'registered_cell_classes': sorted(cells),
        'cell_classes_with_explicit_invertibility_gates': gated,
        'cell_classes_without_explicit_invertibility_gates': ungated,
        'conversational_plane_names_absent_from_source_schema': absent,
        'uniform_plane_invertibility_established': False,
        'infinity_one_promotion_admissible': False,
        'first_missing_typed_object': 'source-derived identification of meaning and transport planes with registered cell classes',
        'acceptance_test': 'For each identified class, provide a reverse cell and verify both identity composites plus certificate preservation under composition.',
        'disposition': 'The current source supports conditional invertibility for two cell classes, not invertibility of all planes.',
    }
    out = ROOT / 'results' / 'coherence_pyramid_plane_invertibility_gate.json'
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__': main()
