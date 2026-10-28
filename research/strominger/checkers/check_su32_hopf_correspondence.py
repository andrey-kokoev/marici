"""Audit the Su-32 fixture and replay read-only exact source adapters.
This checks incidence/provenance and conditional reference adapters, not the missing global Hopf construction.
Run the fixture and reference checkers first; see the accompanying packet.
"""
from pathlib import Path
from hashlib import sha256
import json
import copy
import sys
from collections import Counter

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT/'research/strominger/results/su32-hopf-tests-v1'
sys.path.insert(0, str(Path(__file__).parent))
from check_retained_spinor_dual_line_trial import run as spinor_run
from check_native_dual_line_context_adapter import run as context_run


def verify_fixture(fixture):
    assert fixture['nativeHopfBinding'] is False
    assert fixture['inventory']['cells'] == 51
    assert len(fixture['interfaces']) == 104 and len(fixture['boundary']) == 72
    assert len(fixture['readings']) == 6 and fixture['uniqueStars'] == 6
    for path, digest in fixture['sourceHashes'].items():
        assert sha256((ROOT/path).read_bytes()).hexdigest() == digest, path
    for reading in fixture['readings']:
        square = reading['referenceSquare']
        edges = [frozenset(e['vertices']) for e in square['edges']]
        assert len(set(edges)) == 4
        assert Counter(v for e in edges for v in e) == Counter({v: 2 for v in square['vertices']})
        assert len(reading['cones']) == 6
        for cone in reading['cones']:
            assert len(cone['paths']) == 16 and len(cone['moves']) == 20
            assert cone['operationMap'] is None
            assert all(move['witness'] is None for move in cone['moves'])
        assert all(c['comparisonMap'] is None for c in reading['comparisons'])
        assert all(o['transition'] is None for o in reading['coneOverlaps'])
    return True


def rejects(call):
    try:
        call()
    except AssertionError:
        return True
    return False


def main():
    fixture = json.loads((OUT/'fixture.json').read_text())
    contract_path = ROOT/'research/strominger/contracts/su32-hopf-correspondence-v1.json'
    contract = json.loads(contract_path.read_text())
    verify_fixture(fixture)
    bad = copy.deepcopy(fixture)
    bad['readings'][0]['cones'][0]['operationMap'] = 'identity inserted without source'
    assert rejects(lambda: verify_fixture(bad))
    bad = copy.deepcopy(fixture)
    bad['sourceHashes'][next(iter(bad['sourceHashes']))] = 'stale'
    assert rejects(lambda: verify_fixture(bad))
    assert contract['nativeHopfBinding'] is False
    assert len({r['id'] for r in contract['rows']}) == len(contract['rows']) == 7
    join = json.loads((OUT/'circle-join.json').read_text())
    history = json.loads((OUT/'simplicial-source.json').read_text())
    assert join['status'] == history['status'] == 'pass'
    spinor, context = spinor_run(), context_run()
    assert spinor['sourceStoresUnchanged'] and context['sourceStoresUnchanged']
    assert context['NNcounterexample']['outgoingContrastNormSquared'] == '2/3'
    for name, result in [('spinor-source', spinor), ('context-adapter', context)]:
        (OUT/f'{name}.json').write_text(json.dumps(result, indent=2)+'\n')
    berry_path = ROOT/'research/strominger/results/berry-connection-domain-cut/verification.json'
    berry = json.loads(berry_path.read_text())
    assert berry['status'] == 'pass' and berry['transition_winding'] == -1
    for path, digest in berry['sha256'].items():
        assert sha256((ROOT/path).read_bytes()).hexdigest() == digest
    (OUT/'berry-reference.json').write_text(json.dumps(berry, indent=2)+'\n')
    inputs = [contract_path, Path(__file__), OUT/'fixture.json', OUT/'circle-join.json', OUT/'simplicial-source.json',
              ROOT/'research/chatgpt/20261019/check_wg_circle_torsor.py', ROOT/'research/chatgpt/20261019/check_simplicial_source.py', berry_path]
    result = {
        'schema': 'su32.hopf-correspondence-audit.v1', 'passed': True,
        'classification': 'incidence_fixture_and_conditional_reference_adapters_checked',
        'admitted_scope': '51-cell incidence; one entry C4 per reading; exact retained-electron and five-slot adapter tests',
        'nativeHopfBinding': False,
        'referenceReplay': {'circleJoinChecks': join['total_exact_checks'], 'simplicialAssertions': history['total_assertions'],
                            'spinorRoundTrips': spinor['retainedRecordRoundTrips'], 'equivarianceChecks': spinor['equivarianceChecks'],
                            'berryCharts': berry['decorated_charts_checked']},
        'hostiles': ['invented native identity map rejected', 'stale source digest rejected'],
        'residuals': [r['firstMissingObject'] for r in contract['rows'] if 'firstMissingObject' in r],
        'next_falsifier': 'Construct a global signed-record encoder or join adapter; test its six-cone restrictions without discarding context or relative phase.',
        'sourceHashes': {str(p.relative_to(ROOT)).replace('\\', '/'): sha256(p.read_bytes()).hexdigest() for p in inputs},
        'nonverification': 'Full original spinor producer, Agda/Lean proofs, native simplicial adapter, native clutching degree and global wiring were not executed or established.'
    }
    (OUT/'verification.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
