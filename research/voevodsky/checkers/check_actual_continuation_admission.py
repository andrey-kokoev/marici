"""Exhaust actual square-free path admission; bind to actual action verification.

Admission is independently checked by the authoritative source recorder.
This covers typed path extension, not undeclared certificate dependencies.
"""
from pathlib import Path
from itertools import permutations, product
import importlib.util
import subprocess
import sys
import json
import hashlib

ROOT = Path(__file__).resolve().parents[3]
source_path = ROOT / 'research/voevodsky/certificates/verify_filtered_obstruction.py'
spec = importlib.util.spec_from_file_location('source_admission', source_path)
source = importlib.util.module_from_spec(spec)
spec.loader.exec_module(source)
# Freshly recheck actual source-action equivariance. The owning test derives
# both sides from raw coefficient rows, including every expected action group.
action_checker = Path(__file__).with_name('check_actual_opposite_observer_transport.py')
subprocess.run([sys.executable, str(action_checker)], check=True, capture_output=True, text=True)
action_path = ROOT / 'research/voevodsky/results/actual-opposite-observer-transport.json'
action_report = json.loads(action_path.read_text())
assert action_report['passed']

histories = 0
accepted = 0
rejected = 0
by_corner = {}
for start in range(64):
    available = tuple(e for e in range(6) if not start & (1 << e))
    for length in range(len(available) + 1):
        for word in permutations(available, length):
            end = start | sum(1 << e for e in word)
            expected = frozenset((e, m) for e in range(6) if not end & (1 << e) for m in (0, 1))
            for marks in product((0, 1), repeat=length):
                source.record(start, word, marks)
                admitted = set()
                for e in range(6):
                    for m in (0, 1):
                        try:
                            source.record(start, word + (e,), marks + (m,))
                        except ValueError as error:
                            assert str(error) == 'event repeated from initial state'
                            assert end & (1 << e)
                            rejected += 1
                        else:
                            admitted.add((e, m))
                            accepted += 1
                assert frozenset(admitted) == expected
                corner = (start, end)
                if corner in by_corner:
                    assert by_corner[corner] == expected
                else:
                    by_corner[corner] = expected
                histories += 1

# Explicit actual-observer collision: the previously exported hidden relation
# is the difference of these two admitted zero-mark paths in corner (0,11).
witness_path = ROOT / 'research/voevodsky/results/actual-observer-reversal-descent.json'
witness = json.loads(witness_path.read_text())
assert witness['status'] == 'same-observer-reversal-obstructed'
assert witness['witness']['source_generator'] == 36
assert witness['witness']['original_observer_column'] == []
assert witness['presentation_sha256'] == action_report['presentation_sha256']
assert by_corner[0, 11] == frozenset((e, m) for e in (2, 4, 5) for m in (0, 1))
report = {
    'passed': True,
    'admission_contract': 'Six square-free events; retained marks 0/1; initial and terminal masks retained as types. Source record() accepts exactly unused-event extensions.',
    'admitted_histories_checked': histories,
    'typed_corners_checked': len(by_corner),
    'accepted_one_event_extensions': accepted,
    'rejected_repeated_event_extensions': rejected,
    'actual_action_entries_verified': sum(f['action_entries_per_orientation'] for f in action_report['frames']),
    'algebraic_result': 'Typed path admission depends only on endpoint. On the declared ideal-source domain, actual action equivariance preserves observer equality under every admitted event word by induction. Applying this to two paths requires their difference to lie in that domain.',
    'explicit_collision_common_next_events': [2, 4, 5],
    'evidence_dependency_status': 'No certificate/provenance-dependent continuation admission contract is supplied by this source recorder. Such dependencies are not tested here.',
    'dpc_status': 'Typed algebraic continuation clause verified; stronger evidence-dependent continuation clause remains unspecified.',
    'input_hashes': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in (source_path, action_path, witness_path)},
}
out = ROOT / 'research/voevodsky/results/actual-continuation-admission.json'
out.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
