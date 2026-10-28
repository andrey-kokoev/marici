"""Actual native packet replay plus a separate Python word-trace decoder."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[3]
ATTEMPT = 'research/voevodsky/contracts/ramsey-native-word-trace-attempt.v1.json'
PROOF = 'research/voevodsky/ramsey-native-word-history-lift-v1.md'
JS = 'research/voevodsky/checkers/check_ramsey_native_word_trace.mjs'


def independent_decode(trace):
    alphabet, events = trace['alphabet'], trace['events']
    assert alphabet and len(set(alphabet)) == len(alphabet)
    previous = trace['seed']
    for i, event in enumerate(events):
        assert type(event['ordinal']) is int and event['ordinal'] == i
        assert event['source'] == previous
        previous = event['target']
    assert previous == trace['endpoint']
    bits, cursor = [], 0
    while cursor < len(events):
        row = events[cursor]
        if row['kind'] == 'PN':
            assert cursor + 1 < len(events)
            back = events[cursor + 1]
            assert back['kind'] == 'inverse-PN'
            assert row['source'] == back['target']
            assert row['source']['chart']['species'] == 'proton'
            assert row['target']['chart']['species'] == 'neutron'
            assert row['phaseDelta'] == back['phaseDelta'] == 0
            bits.append(0)
            cursor += 2
        else:
            assert row['kind'] == 'reader-phase-advance'
            assert row['source']['chart']['species'] == row['target']['chart']['species'] == 'proton'
            assert row['phaseDelta'] == 1
            assert row['target']['packet']['origin'] == row['source']['packet']['origin'] + 1
            reference = row['phaseWitness']['referenceContext']
            assert reference['coefficientRule'] == 'retain' and reference['physicalLawDerived'] is False
            bits.append(1)
            cursor += 1
    width = max(1, (len(alphabet) - 1).bit_length())
    assert len(bits) % width == 0
    word = []
    for start in range(0, len(bits), width):
        symbol = sum(bit << (width - j - 1) for j, bit in enumerate(bits[start:start + width]))
        assert symbol < len(alphabet)
        word.append(symbol)
    return word


def main():
    done = subprocess.run(['node', str(ROOT / JS)], cwd=ROOT, capture_output=True,
                          text=True, check=True, timeout=90)
    summary = json.loads(done.stdout)
    assert summary['status'] == 'passed'
    raw_path = ROOT / 'research/voevodsky/results/ramsey-native-word-trace-replay-v1.json'
    fixture_path = ROOT / 'research/voevodsky/results/ramsey-native-word-trace-fixture-v1.json'
    raw = json.loads(raw_path.read_text(encoding='utf-8'))
    fixture = json.loads(fixture_path.read_text(encoding='utf-8'))
    attempt = json.loads((ROOT / ATTEMPT).read_text(encoding='utf-8'))
    assert len(raw['cases']) == 133 and raw['appendCases'] == 49 and raw['associativityCases'] == 3
    assert len(raw['rejectedControls']) == 19
    assert independent_decode(fixture['trace']) == fixture['expectedWord']
    assert fixture['trace']['alphabet'] == fixture['expectedAlphabet']
    assert raw['endpointCollisionVerified'] and raw['cacheStateCollisionVerified'] and raw['supportMultiplicityCollisionVerified']
    for key in ('simultaneousAssemblyAdmissionProved', 'codebookNativeSeedAdmissionProved', 'nativeForcingControlProved', 'rootResolved'):
        assert raw[key] is False
    sources = dict(raw['sourceHashes'])
    for relative in [ATTEMPT, PROOF, 'research/voevodsky/checkers/check_ramsey_native_word_trace.py']:
        sources[relative] = sha256((ROOT / relative).read_bytes()).hexdigest()
    for relative, digest in sources.items():
        path = (ROOT / relative).resolve()
        assert path.is_relative_to(ROOT) and sha256(path.read_bytes()).hexdigest() == digest
    result = {
        'schema': 'marici.ramsey-native-word-history.verification.v1', 'status': 'passed',
        'scope_id': attempt['scope_id'], 'outcome': '++',
        'verification_level': 'written bounded model-native trace argument and actual packet/phase replay with independent decoder; not native forcing or kernel verified',
        'word_cases': len(raw['cases']), 'append_cases': raw['appendCases'], 'associativity_cases': raw['associativityCases'],
        'selected_events_in_positive_word_cases': raw['selectedEventsInPositiveCases'],
        'negative_controls': len(raw['rejectedControls']), 'independent_decoder_agrees': True,
        'endpoint_projection_faithful_for_this_code': False,
        'deduplicated_support_faithful_for_this_code': False,
        'repeated_zero_loop_leaves_cached_model_unchanged': True,
        'execution_envelope': attempt['execution_envelope'],
        'codebook_native_seed_admission_proved': False,
        'simultaneous_assembly_admission_proved': False,
        'native_forcing_control_proved': False, 'general_endpoint_encoding_impossibility_proved': False,
        'root_resolved': False,
        'replay_receipt': {'path': str(raw_path.relative_to(ROOT)).replace('\\', '/'), 'sha256': sha256(raw_path.read_bytes()).hexdigest()},
        'trace_fixture': {'path': str(fixture_path.relative_to(ROOT)).replace('\\', '/'), 'sha256': sha256(fixture_path.read_bytes()).hexdigest()},
        'source_sha256': dict(sorted(sources.items())),
    }
    target = ROOT / 'research/voevodsky/results/ramsey-native-word-trace-v1.json'
    target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k not in ('source_sha256', 'replay_receipt', 'trace_fixture')}))


if __name__ == '__main__':
    main()
