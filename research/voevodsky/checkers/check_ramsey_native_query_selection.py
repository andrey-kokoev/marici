"""Fresh native forward query realization plus independent finite task checks."""
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from research.voevodsky.checkers.check_ramsey_native_word_trace import independent_decode
BASE = 'research/voevodsky/'

def point(vertex):
    b = tuple(map(int, vertex.split(',')))
    assert len(b) == 4 and sum(b) == 1
    return [b[1]+b[2], b[1]+b[3], b[2]+b[3]]


def check_case(task, case):
    word, value = case['word'], case['selection']
    path = value['path']
    assert independent_decode(path['prefix']) == word
    current = path['prefix']['endpoint']
    for j, event in enumerate(path['events']):
        assert event['source'] == current
        assert event['ordinal'] == len(path['prefix']['events']) + j
        a, b = event['source'], event['target']
        kind = event['kind']
        delta = int(kind in ('reader-phase-advance', 'NN-phase-advance'))
        if delta:
            assert a['chart']['species'] == b['chart']['species']
            permutation = [2, 3, 0, 1, 4] if a['chart']['species'] == 'proton' else [0, 3, 4, 1, 2]
            witness = event['phaseWitness']
            assert witness['from'] == event['phaseFrames']['source'] and witness['to'] == event['phaseFrames']['target']
            assert witness['referenceContext']['physicalLawDerived'] is False
            assert witness['referenceContext']['coefficientRule'] == 'retain'
        else:
            assert kind in ('PN', 'inverse-PN')
            assert a['chart']['aliases'] == b['chart']['aliases']
            permutation = [3, 1, 2, 0, 4]
            assert event['phaseWitness'] is None
        assert event['phaseDelta'] == delta
        assert b['packet']['origin'] == a['packet']['origin'] + delta
        assert event['permutation'] == permutation
        assert b['packet']['permutation'] == [a['packet']['permutation'][i] for i in permutation]
        current = b
    assert current == path['endpoint']
    c, origin = current['chart'], current['packet']['origin']
    names, context = (('C0', 'M0', 'C1'), 'M1') if c['species'] == 'proton' else (('M0', 'C1', 'M1'), 'C2')
    occurrence = lambda n: {'role': n[0], 'index': int(n[1:])+origin, 'vertex': c['aliases'][n]}
    frame = {'id': c['id']+'@'+str(origin), 'species': c['species'], 'window': [occurrence(n) for n in names], 'context': occurrence(context)}
    assert value['marker']['frame'] == frame
    assert value['marker']['occurrence'] == frame['window'][0]
    actual = point(frame['window'][0]['vertex'])
    expected = [sum(task['pattern'][i][j] for i in word) for j in range(3)]
    assert value['marker']['latticePoint'] == actual == expected
    table = {tuple(row['point']): row['color'] for row in task['coloring']}
    assert value['color'] == table[tuple(expected)]


def main():
    run = subprocess.run(['node', BASE+'checkers/check_ramsey_native_query_selection.mjs'], cwd=ROOT, capture_output=True, text=True, check=True, timeout=90)
    raw = json.loads(run.stdout)
    task = raw['task']
    assert task['pattern'] == [[0,0,0],[1,1,0],[1,0,1]]
    assert {tuple(row['point']) for row in task['coloring']} == {p for p in product(range(-2,3), repeat=3) if sum(p)%2 == 0}
    assert {tuple(c['word']) for c in raw['cases']} == set(product(range(3), repeat=2))
    for case in raw['cases']:
        check_case(task, case)
    assert raw['primaryColors'] == [0,1] and raw['primarySuffixCounts'] == [0,2]
    assert raw['primaryNativeEndpointsDistinguished'] is True
    assert raw['constructionCases'] == 27 and raw['recoloringPathComparisons'] == 18
    assert raw['sourceValidWrongQueryControls'] == 2 and len(raw['negativeControls']) == 13
    assert raw['nativeWitnessEvents'] == 81
    for key in ('sourceSelectionUsesTargetPointOrColor', 'autonomousNativeControllerProved', 'uniformTaskPackageAdmitted', 'rootResolved'):
        assert raw[key] is False
    # The old inventory is provenance only; source paths above are freshly run.
    old = json.loads((ROOT/(BASE+'results/ramsey-native-word-trace-v1.json')).read_text(encoding='utf-8'))
    pins = dict(old['source_sha256'])
    for relative in ['contracts/ramsey-native-query-selection-attempt.v1.json', 'ramsey-native-query-selection-v1.md',
                     'ramsey-native-query-selection.mjs', 'checkers/check_ramsey_native_query_selection.mjs',
                     'checkers/check_ramsey_native_query_selection.py']:
        pins[BASE+relative] = sha256((ROOT/(BASE+relative)).read_bytes()).hexdigest()
    for relative, digest in pins.items():
        assert sha256((ROOT/relative).read_bytes()).hexdigest() == digest
    result = {
        'schema': 'marici.ramsey-native-query-selection.verification.v1', 'status': 'passed',
        'scope_id': 'fixed-task-native-marked-query-realization-v1', 'outcome': '++',
        'verification_level': 'written finite source-geometry argument, actual native packet/phase replay and independent Python checks; bounded host-compiled selection, not autonomous control or kernel proof',
        'witness': raw, 'exhaustive_length_two_words': 9, 'construction_cases': 27,
        'native_witness_events': 81, 'negative_controls': 13, 'source_valid_wrong_query_controls': 2,
        'native_forward_selected_points_realized': True, 'source_selection_depends_on_colors': False,
        'host_instruction_compiler_retained': True, 'input_color_table_observation_retained': True,
        'autonomous_native_controller_proved': False, 'uniform_task_package_admitted': False, 'root_resolved': False,
        'source_sha256': dict(sorted(pins.items())),
    }
    (ROOT/(BASE+'results/ramsey-native-query-selection-v1.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('source_sha256','witness')}))

if __name__ == '__main__':
    main()
