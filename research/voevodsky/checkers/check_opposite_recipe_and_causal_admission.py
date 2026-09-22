"""Exact pullback recipe construction and fixed-constructor causal reversal test.

Uses actual analytical recipe syntax and freshly replayable deadline artifacts.
A pullback is a coordinate construction; it does not authorize new acquisition.
"""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction as Q
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
NIMA = ROOT / 'research/nima/results'
OUT = ROOT / 'research/voevodsky/results'
union_path = NIMA / 'actual-retained-cubic-observer-union.json'
union = json.loads(union_path.read_text())
deadline_path = OUT / 'signed-certificate-deadline.json'
deadline = json.loads(deadline_path.read_text())
assert deadline['passed']
for name, digest in deadline['protected_file_hashes'].items():
    assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest


def rw(window):
    a, b = window
    assert 0 <= a < b <= 63
    return [63 - b, 63 - a]


def pair(windows):
    return [rw(w) for w in reversed(windows)]


def polynomial(terms, pullback=False):
    result = defaultdict(Q)
    for t in terms:
        windows = [rw(w) for w in t['windows']] if pullback else t['windows']
        result[tuple(sorted(map(tuple, windows)))] += Q(t['coefficient'])
    return {k: v for k, v in result.items() if v}

recipes = []
terms_checked = 0
for frame in union['frames']:
    denoms = []
    for denominator in frame['denominators']:
        reversed_denominator = [{'windows': pair(t['windows']), 'coefficient': t['coefficient']}
                                for t in denominator]
        # Wop(a,b)=W(63-b,63-a). Scalar products commute; components stay fixed.
        assert polynomial(reversed_denominator, True) == polynomial(denominator)
        assert all(Q(t['coefficient']) > 0 for t in denominator)
        denoms.append(reversed_denominator)
    for row in frame['rows']:
        for t in row['terms']:
            transformed = pair(t['windows'])
            assert pair(transformed) == t['windows']
            assert sorted(map(tuple, map(rw, transformed))) == sorted(map(tuple, t['windows']))
            terms_checked += 1
    recipes.append({'family': frame['family'], 'response': frame['response'],
                    'opposite_response_definition': 'Wop(a,b)=W(63-b,63-a)',
                    'component_policy': 'retain S[j] and component_coefficients[j]',
                    'opposite_denominators': denoms,
                    'original_denominator_recovered_exactly': True})
# Additivity is transported algebraically by endpoint cancellation.
additivity_checks = 0
for a in range(64):
    for b in range(a + 1, 64):
        for c in range(b + 1, 64):
            # Wop(a,c)=F(63-a)-F(63-c).
            lhs = {63 - a: 1, 63 - c: -1}
            rhs = defaultdict(int)
            for lo, hi in ((a, b), (b, c)):
                rhs[63 - lo] += 1
                rhs[63 - hi] -= 1
            assert {k: v for k, v in rhs.items() if v} == lhs
            additivity_checks += 1

# Keep actual event constructors: B issues, A receives then replays.
# Any reversed time coordinate t'=K-t swaps their order.
causal = []
for group in ('fast_cases', 'delayed_cases'):
    for case in deadline[group]:
        issue = case['B_issues_at']
        receive = issue + case['B_to_A_delay']
        assert issue < receive
        K = receive + issue
        assert K - receive < K - issue
        causal.append({'world': case['world'], 'schedule': group,
                       'original_issue': issue, 'original_receive': receive,
                       'reversed_receive': K - receive, 'reversed_issue': K - issue,
                       'same_issue_before_receive_constructor_preserved': False})
# Actual proof payload carries all raw rows; removing distinguishing evidence
# leaves exactly the common coarse record in the delayed contrasting worlds.
slow = deadline['delayed_cases']
assert slow[0]['traces']['A']['received_by_deadline'] == slow[1]['traces']['A']['received_by_deadline']
assert slow[0]['correct_status'] != slow[1]['correct_status']
for case in deadline['fast_cases']:
    assert case['traces']['A']['certificate'] == case['correct_status']
    frames = [m for m in case['traces']['A']['received_by_deadline']
              if m['kind'] == 'signed-pairing-task-transport-frame']
    assert len(frames) == 1 and 'positive' in frames[0]['payload']['raw']
report = {
    'passed': True,
    'analytical_status': 'exact coordinate-pullback recipes constructed',
    'actual_window_terms_checked': terms_checked,
    'endpoint_additivity_checks': additivity_checks,
    'recipes': recipes,
    'causal_status': 'time reversal with unchanged issue/receive constructors obstructed',
    'causal_witnesses': causal,
    'inputs_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in (union_path, deadline_path)},
    'admission_boundary': 'Pullback reuses original response evaluations and positive denominators. Physical reversed-window constructors are not supplied. Causal reversal requires new event constructors or an independently justified evidence supply; the existing forward protocol does not authorize it.',
    'conjecture_status': 'Coordinate analytical gate closed; fixed-constructor temporal reversal refuted; existence of a separately authorized opposite causal protocol remains open.'
}
(OUT / 'opposite-recipe-and-causal-admission.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({k: v for k, v in report.items() if k not in ('recipes', 'causal_witnesses')}, indent=2))
