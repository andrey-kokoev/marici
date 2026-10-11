"""Input sensitivity and exact historical-manifest regression checks."""
from copy import deepcopy
import json
from pathlib import Path
from assemble_triangle_arrow_source import assemble

ROOT = Path(__file__).resolve().parents[1]


def main():
    source = json.loads((ROOT/'inputs/proton-six-arrows.json').read_text())
    report, arrows = assemble(source)
    historical = json.loads((ROOT/'results/twelve-triangle-1836-arrows.json').read_text())
    assert arrows == historical, 'Exact typed endpoints and coefficients changed'
    assert report['return_cycle_union_measure'] == 1836
    assert report['boundary_chain_zero']
    assert report['closed_cycle_weights_positive']
    assert report['closed_walk_union_covers_every_arrow']
    deletions = []
    for edge in source['arrows']:
        reduced = deepcopy(source)
        reduced['arrows'].remove(edge)
        result, _ = assemble(reduced)
        assert result['proper_rotations'] == 3
        assert not result['boundary_chain_zero']
        assert result['return_cycle_union_measure'] != 1836
        deletions.append({'removed': edge, 'measure': result['return_cycle_union_measure']})
    # No fallback to the historical cycles when the source has no triangles.
    empty = deepcopy(source)
    empty['arrows'] = []
    try:
        assemble(empty)
    except ValueError as exc:
        assert 'no complete oriented triangle' in str(exc)
    else:
        raise AssertionError('Empty input silently acquired historical arrows')
    # Coordinates are consumed, not merely read and replaced with the old tetrahedron.
    changed = deepcopy(source)
    changed['vertices']['D'][2] = 2
    try:
        assemble(changed)
    except ValueError as exc:
        assert 'geometry' in str(exc) or 'vertices' in str(exc)
    else:
        raise AssertionError('Incompatible geometry was ignored')
    print(json.dumps({'status': 'passed', 'exact_historical_manifest_match': True,
                      'single_arrow_deletions': deletions,
                      'empty_input_rejected': True, 'incompatible_geometry_rejected': True}))


if __name__ == '__main__':
    main()
