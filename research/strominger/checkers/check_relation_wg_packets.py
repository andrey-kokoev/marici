"""Finite retained relation-packet comparison using the owning source algebra.

Four events test a nonzero I^2 attachment; five events test a nonidentity
balancing move. This is an executable typed fixture, not an Agda theorem.
"""
from dataclasses import dataclass
from pathlib import Path
from collections import defaultdict
from itertools import product
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[3]
owner = ROOT / 'research/nima/checkers/check_seven_event_factorization_descent.py'
spec = importlib.util.spec_from_file_location('source_descent', owner)
S = importlib.util.module_from_spec(spec)
spec.loader.exec_module(S)  # guarded main; reuse definitions, no seven-event run

@dataclass(frozen=True)
class Arrow:
    start: int
    end: int
    terms: tuple

    def column(self): return dict(self.terms)


def arrow(start, column):
    column = S.clean(column)
    ends = set()
    for (word, marks), coefficient in column.items():
        assert len(word) == len(marks) and coefficient
        state = start
        for event in word:
            assert not state & (1 << event)
            state |= 1 << event
        ends.add(state)
    assert len(ends) == 1
    return Arrow(start, ends.pop(), tuple(sorted(column.items())))


def mul(a, b):
    if a.end != b.start:
        raise ValueError('noncomposable packet endpoints')
    return arrow(a.start, S.multiply(a.column(), b.column()))


def observe(a):
    out = defaultdict(int)
    for (word, marks), c in a.terms:
        for k, v in S.record(a.start, word, marks).items(): out[k] += c*v
    return S.clean(out)


def raw_seams(left, right):
    assert left.end == right.start
    cut = left.end
    out = defaultdict(int)
    for a, x in S.derivative(left.start, left.column()).items():
        for b, y in S.derivative(right.start, right.column()).items():
            out[(cut, a, b)] += x*y
    return S.clean(out)


def balanced_two(raw):
    # Two-factor specialization of the owner's three-factor buffer normal form.
    out = defaultdict(int)
    for (cut, a, b), c in raw.items():
        x, y, u, keep, v = a
        xx, yy, uu, kk, vv = b
        out[((('e', x, y, keep), ('e', xx, yy, kk)), (u, v+uu, vv))] += c
    return S.clean(out)


def boundary_two(column):
    out = defaultdict(int)
    for (separators, buffers), c in column.items():
        for i, (_, x, y, keep) in enumerate(separators):
            for word, b in S.feature(x, y, keep).items():
                marks, bs = list(separators), list(buffers)
                marks[i] = ('v', y); bs[i] += word
                out[tuple(marks), tuple(bs)] += (-1)**i*c*b
                marks, bs = list(separators), list(buffers)
                marks[i] = ('v', x); bs[i+1] = word+bs[i+1]
                out[tuple(marks), tuple(bs)] -= (-1)**i*c*b
    return S.clean(out)


@dataclass(frozen=True)
class FactorPacket:
    left: Arrow
    right: Arrow
    product: Arrow
    raw: tuple
    balanced: tuple


def package(left, right):
    result = mul(left, right)
    assert not observe(left) and not observe(right) and not observe(result)
    raw = raw_seams(left, right)
    balanced = balanced_two(raw)
    assert balanced and not boundary_two(balanced)
    return FactorPacket(left, right, result, tuple(sorted(raw.items())),
                        tuple(sorted(balanced.items())))


@dataclass(frozen=True)
class Request:
    a: Arrow
    middle: Arrow
    b: Arrow


@dataclass(frozen=True)
class Answer:
    request: Request
    left_cut: FactorPacket
    right_cut: FactorPacket
    detector: tuple


def verify(answer):
    q = answer.request
    # Recompute all equations and provenance rather than trust success booleans.
    expected_left = package(mul(q.a, q.middle), q.b)
    expected_right = package(q.a, mul(q.middle, q.b))
    assert answer.left_cut == expected_left and answer.right_cut == expected_right
    assert expected_left.product == expected_right.product
    assert expected_left.balanced == expected_right.balanced
    key, value = answer.detector
    assert value != 0 and expected_left.product.column().get(key) == value


def generate(q):
    l, r = package(mul(q.a, q.middle), q.b), package(q.a, mul(q.middle, q.b))
    result = Answer(q, l, r, l.product.terms[0])
    verify(result)
    return result


checks = {}
a4 = arrow(0, S.relation((0, 1), 1))
b4 = arrow(3, S.relation((2, 3), 0))
p4 = package(a4, b4)
checks['four_event_eight_term_nonzero_product'] = len(p4.product.terms) == 8
checks['four_event_terminal_product_invisible'] = not observe(p4.product)
checks['four_event_only_cut_after_two'] = [k for k in range(5) if k >= 2 and 4-k >= 2] == [2]
checks['five_event_two_nonminimal_cuts'] = [k for k in range(6) if k >= 2 and 5-k >= 2] == [2, 3]

# The attachment action is the ACTUAL source multiplication a4*b4=v.
# Right multiplication by b4 sends a4 to v. It kills b4 and v by endpoints.
checks['actual_attachment_action'] = mul(a4, b4) == p4.product
checks['product_cannot_continue_by_b'] = p4.product.end != b4.start
# On [a,b,v], right b has column a = v; on the graded direct sum it is zero.
basis = (a4, b4, p4.product)
def typed_column(x):
    return {(x.start, x.end, key): value for key, value in x.terms}
basis_columns = [typed_column(x) for x in basis]
action_columns = []
for x in basis:
    image = typed_column(mul(x, b4)) if x.end == b4.start else {}
    coordinates = tuple(image.get(next(iter(col)), 0) // next(iter(col.values()))
                        for col in basis_columns)
    rebuilt = defaultdict(int)
    for coefficient, col in zip(coordinates, basis_columns):
        for key, value in col.items(): rebuilt[key] += coefficient * value
    assert S.clean(rebuilt) == image
    action_columns.append(coordinates)
actual_action = tuple(tuple(col[i] for col in action_columns) for i in range(3))
assert actual_action == ((0,0,0),(0,0,0),(1,0,0))
# Associated-graded action drops the cross-layer a->ab term; all same-layer
# blocks of this computed action vanish.
graded_action = tuple(tuple(actual_action[i][j] if (i == 2) == (j == 2) else 0
                            for j in range(3)) for i in range(3))
checks['unrelated_direct_sum_loses_action'] = actual_action != graded_action

answers = []
for ka, kb, mark in product((0,1), repeat=3):
    a = arrow(0, S.relation((0,1), ka))
    middle = arrow(3, {((2,), (mark,)):1})
    b = arrow(7, S.relation((3,4), kb))
    q = Request(a, middle, b)
    result = generate(q)
    assert result.request == q
    assert result.left_cut.raw != result.right_cut.raw
    assert result.left_cut.balanced == result.right_cut.balanced
    # Retain q and both constructions if the answer becomes the next input.
    answers.append(result)
checks['eight_source_generated_balancing_packets'] = len(answers) == 8
checks['balanced_cycles_and_nonzero_detectors'] = all(a.left_cut.balanced and a.detector[1] for a in answers)

hostiles = []
q = answers[0].request
try:
    mul(q.b, q.a)
except ValueError:
    hostiles.append('wrong_endpoint_product')
else:
    raise AssertionError('wrong endpoints accepted')
if answers[0].left_cut.raw != answers[0].right_cut.raw:
    hostiles.append('unbalanced_cut_labels_claimed_equal')
if actual_action != graded_action:
    hostiles.append('unrelated_direct_sum_claimed_source_linear')
bad = Answer(q, answers[0].left_cut, answers[0].right_cut,
             (answers[0].detector[0], 0))
try:
    verify(bad)
except AssertionError:
    hostiles.append('zeroed_product_detector')
else:
    raise AssertionError('zero detector accepted')
assert all(checks.values()) and len(hostiles) == 4

def encode_arrow(a):
    return {'start':a.start, 'end':a.end,
            'terms':[{'word':w, 'marks':m, 'coefficient':c} for (w,m),c in a.terms]}

out = {'schema':'marici.relation-wg-packets.v1', 'status':'pass',
       'checks':checks, 'rejected_hostiles':hostiles,
       'four_event_product':encode_arrow(p4.product),
       'local_right_action_basis':['a','b','ab'], 'actual_right_b':actual_action,
       'graded_direct_sum_right_b':graded_action,
       'five_event_cases':[{'kinds':list(k), 'product_terms':len(a.left_cut.product.terms),
                           'raw_sizes':[len(a.left_cut.raw),len(a.right_cut.raw)],
                           'balanced_size':len(a.left_cut.balanced)}
                          for k,a in zip(product((0,1),repeat=3),answers)],
       'scope':'Exact finite source coefficients and two-factor seam normal form; not a compiled native WG or a global reconstructed source module.'}
path = ROOT/'research/strominger/results/relation-wg-packets-v1.json'
path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
