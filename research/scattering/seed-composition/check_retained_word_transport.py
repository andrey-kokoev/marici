"""Source-backed retained concatenation and its scoped multiplicative mode test.

Uses the existing retained-path ledger, not a fitted continuation operator.
The plane obstruction is proved by exact polynomial identities, not sampling.
"""
from contextlib import redirect_stdout
from fractions import Fraction as F
from io import StringIO
from pathlib import Path
import argparse
import hashlib
import json
import sys

from check_incidence_audit import audit as incidence_audit, apply, encode

ROOT = Path(__file__).resolve().parents[3]
BASE = Path(__file__).resolve().parent
DEST = BASE / 'results/retained-word-transport.v1.json'
sys.path.insert(0, str(ROOT / 'research/nima/checkers'))
# The imported source contains small, read-only path enumeration checks.
with redirect_stdout(StringIO()):
    from retained_path_successor import RetainedSuccessorLedger


def poly(value=0, variable=None):
    if variable is not None:
        return {tuple(int(i == variable) for i in range(3)): F(1)}
    return {(0, 0, 0): F(value)} if value else {}


def add(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, F(0)) + value
    return {k: v for k, v in out.items() if v}


def scale(a, scalar):
    return {k: v*scalar for k, v in a.items() if v*scalar}


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            key = tuple(u+v for u, v in zip(i, j))
            out[key] = out.get(key, F(0)) + x*y
    return {k: v for k, v in out.items() if v}


def evaluate(p, values):
    total = F(0)
    for powers, coefficient in p.items():
        term = coefficient
        for value, exponent in zip(values, powers):
            term *= value**exponent
        total += term
    return total


def audit():
    prior = incidence_audit()  # Fresh exact previous-stage checks; no old receipt trust.
    primitive = prior['primitive_order']
    endpoints = [tuple(p['edge']) for p in primitive]
    packets = [(p['owner']+':'+''.join(p['edge']), *p['edge']) for p in primitive]
    words = [tuple(endpoints.index(edge) for edge in zip(d['path'], d['path'][1:])) for d in prior['displayed_order']]
    ledger = RetainedSuccessorLedger(packets)

    def payloads(x):
        leaves = [ledger.retain_path_payload((((a, b, label),),), (F(value),))
                  for (label, a, b), value in zip(packets, x)]
        out = []
        for word in words:
            payload = leaves[word[0]]
            for index in word[1:]:
                previous = payload
                payload = ledger.compose_payloads(previous, leaves[index])
                parents, slots = ledger.deconstruct_payload(payload)
                assert parents == (previous, leaves[index]) and slots == ((0, 0),)
            assert len(payload.paths) == 1 and len(payload.values) == 1
            expected = F(1)
            for index in word:
                expected *= x[index]
            assert payload.values == (expected,)
            out.append(payload)
        return leaves, out

    def product_map(x):
        a,b,c,d,e,f,g,h,i,j = x
        return [a,b,i*j,c*d,e,a*b,f*g,h,i*j,i,j,a*b]

    x = list(map(F, [2,3,5,7,11,13,17,19,23,29]))
    leaves, out = payloads(x)
    assert [p.values[0] for p in out] == product_map(x)
    # Parent recovery is provenance recovery, not an inverse of multiplication.
    x2 = list(x); x2[2] = 1; x2[3] = 35
    _, out2 = payloads(x2)
    assert product_map(x) == product_map(x2) and x != x2
    assert ledger.assembly_history(out[3]) != ledger.assembly_history(out2[3])
    zero = list(x); zero[2] = 0
    zero_leaves, zero_out = payloads(zero)
    parents, _ = ledger.deconstruct_payload(zero_out[3])
    assert zero_out[3].values == (0,) and parents == (zero_leaves[2], zero_leaves[3])
    assert parents[1].values == (7,)
    # The existing API refuses to hide the mixed primitive-length grading.
    try:
        ledger.retain_path_payload((out[0].paths[0], out[2].paths[0]), (F(1), F(1)))
    except ValueError:
        mixed_length_rejected = True
    else:
        raise AssertionError('mixed-length family silently accepted')

    def expand(path):
        return tuple(index for edge in path for index in words[edge])

    def valid(path):
        if not path or any(not 0 <= i < 12 for i in path):
            return False
        if len({i//6 for i in path}) != 1:
            return False
        return all(prior['displayed_order'][a]['edge'][1] == prior['displayed_order'][b]['edge'][0]
                   for a, b in zip(path, path[1:]))

    # Exact counterexamples to forgetting pair, parse, or primitive word length.
    assert expand((5,)) == expand((0, 1)) == (0, 1)
    assert valid((5,)) and valid((0, 1))
    assert expand((2,)) == expand((8,)) == (8, 9)  # pair identity also lost
    assert len(expand((2, 0))) == 3 and len(expand((2, 5))) == 4
    assert valid((2, 0)) and valid((2, 5))
    paths = [(i,) for i in range(12)]
    counts = []
    for depth in range(1, 5):
        assert all(valid(p) for p in paths)
        records = [(p[0]//6, tuple(len(words[i]) for i in p), expand(p)) for p in paths]
        # With pair + segmentation, expansion is injective at these tested grades.
        assert len(set(records)) == len(paths)
        for path in paths:
            flat = expand(path)
            assert all(endpoints[a][1] == endpoints[b][0] for a, b in zip(flat, flat[1:]))
            for cut in range(1, len(path)):
                assert flat == expand(path[:cut])+expand(path[cut:])
        counts.append({'macro_length': depth, 'segmented_records': len(paths),
                       'primitive_lengths': sorted({len(expand(p)) for p in paths})})
        paths = [p+(i,) for p in paths for i in range(12) if valid(p+(i,))]

    # Polynomial membership equations for the two reference mode planes:
    # u=s, s(s+t-2)=0, s(s+v+2)=0. Free c,d and f,g can realize
    # the required products; a representative is constructed below.
    s,t,v = (poly(variable=i) for i in range(3))
    one,two = poly(1),poly(2)
    rminus = mul(s, sub(add(s,t),two))
    rplus = mul(s, add(add(s,v),two))
    delta = sub(v,t)  # twice the discrepancy of the two CA coordinates after T
    sprime = scale(sub(t,s), F(1,2))
    tprime = scale(sub(scale(s,-3),t), F(1,2))
    rstep = mul(sprime, sub(add(sprime,tprime),two))
    assert rstep == mul(sub(s,t),add(s,one))
    # If the output and its first continuation step both belong to the image,
    # all four residuals vanish. These identities force s=t=v=0 over Q or C.
    assert sub(sub(rplus,rminus),mul(s,delta)) == scale(s,4)
    assert sub(mul(s,sub(add(s,one),t)),rstep) == t
    assert add(t,delta) == v

    V = prior['matrices']['displayed_mode_frame_V']
    # Symbolic sufficiency, not just rational samples: choose c=f=1 and solve
    # all other primitive values. Its only mismatches are the two residuals.
    bpoly=scale(add(s,t),F(1,2)); hpoly=scale(add(s,v),F(1,2))
    qpoly=[scale(s,-1),bpoly,scale(mul(s,hpoly),-1),s,scale(bpoly,-1),scale(mul(s,bpoly),-1),
           scale(s,-1),hpoly,scale(mul(s,hpoly),-1),s,scale(hpoly,-1),scale(mul(s,bpoly),-1)]
    parameters=[s,t,s,v]
    target=[]
    for row in V:
        entry={}
        for coefficient,parameter in zip(row,parameters):
            entry=add(entry,scale(parameter,coefficient))
        target.append(entry)
    expected=[{} for _ in range(12)]
    for i in [2,8]:expected[i]=scale(rplus,-F(1,2))
    for i in [5,11]:expected[i]=scale(rminus,-F(1,2))
    assert [sub(q,y) for q,y in zip(qpoly,target)] == expected
    T = prior['matrices']['reference_mode_step_T']
    samples = [(F(a),F(b),F(b)) for a in [0] for b in [-2,-1,0,1,2]]
    samples += [(F(a),F(2-a),F(-2-a)) for a in [-2,-1,1,2]]
    for sv,tv,vv in samples:
        assert evaluate(rminus,(sv,tv,vv)) == evaluate(rplus,(sv,tv,vv)) == 0
        # This representative proves sufficiency of the membership equations.
        representative = [-sv,(sv+tv)/2,F(1),sv,-(sv+tv)/2,F(1),-sv,(sv+vv)/2,sv,-(sv+vv)/2]
        assert product_map(representative) == apply(V,[sv,tv,sv,vv])
        _, records = payloads(representative)
        assert [p.values[0] for p in records] == product_map(representative)
        if (sv,tv,vv) != (0,0,0):
            assert evaluate(delta,(sv,tv,vv)) or evaluate(rstep,(sv,tv,vv))
    # A nonzero input can have zero displayed output; no claim that inputs vanish.
    assert product_map([0,0,1,0,0,1,0,0,0,0]) == [0]*12
    example = [F(1),F(1),F(1),F(-3)]
    advanced = apply(T,example[:2])+apply(T,example[2:])
    assert advanced == [0,-2,-2,0]

    dependencies = list(prior['source_sha256']) + [
        'research/scattering/seed-composition/check_retained_word_transport.py',
        'research/nima/retained-path-family-composition-synthesis.md',
        'research/nima/indexed-path-structural-synthesis.md',
        'research/nima/checkers/retained_path_successor.py',
        'research/nima/checkers/check_indexed_path_synthesis.py',
        'research/nima/checkers/check_natural_tower_return.py']
    return {
        'schema': 'marici.scattering.retained-word-transport.v1',
        'status': 'retained_concatenation_verified_multiplicative_mode_shortcut_obstructed',
        'source_sha256': {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'source_operation': 'RetainedSuccessorLedger.compose_payloads: endpoint concatenation, coefficient multiplication, registered parent retention',
        'input_boundary': 'same supplied primitive coefficient used at every occurrence; this diagonal bilinear construction is not a physical linear state evolution',
        'primitive_words_by_displayed_edge': words,
        'word_checks': {'grades_tested': counts, 'pair_and_segmentation_retained': True,
                        'composition_commutes_with_word_expansion': True,
                        'macro_AC_equals_expanded_AB_then_BC': True,
                        'shared_CA_erases_pair_identity_if_flattened': True,
                        'one_macro_step_has_different_primitive_lengths': [3,4],
                        'mixed_length_payload_rejected_by_source_api': mixed_length_rejected},
        'weighted_checks': {'actual_ledger_reused': True, 'parent_slots_and_zero_payload_retained': True,
                            'product_values_do_not_recover_factors': True,
                            'pair_1': ['a','b','i*j','c*d','e','a*b'],
                            'pair_2': ['f*g','h','i*j','i','j','a*b']},
        'mode_obstruction': {
            'scope': 'multiplicative displayed readout of repeated primitive coefficients; fixed reference planes and continuation',
            'membership': ['u=s','rminus=s*(s+t-2)=0','rplus=s*(s+v+2)=0'],
            'necessary_after_one_step': ['delta=v-t=0','rstep=(s-t)*(s+1)=0'],
            'exact_certificates': ['rplus-rminus-s*delta=4*s', 's*(s+1-t)-rstep=t', 't+delta=v'],
            'only_output_with_itself_and_next_step_in_image': 'zero',
            'nonzero_example_parameters': example, 'continued_parameters': advanced,
            'zero_output_does_not_imply_zero_input': True},
        'boundary': {'source_authorized_physical_encoder': False, 'same_tick_continuation_intertwiner': False,
                     'independent_outputs_constructed': False, 'metric_or_faces_transported': False,
                     'all_encoders_rejected': False, 'physical_annihilation_derived': False,
                     'ratio_372_derived': False, 'formal_outcome_admitted': False},
        'next_gate': 'Supply an actual boundary/segmentation-aware continuation operation or independently prepared correlated path payload; derive its coupling from the seed rather than fitting target mode values.'
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    report = audit()
    text = json.dumps(report, indent=2, default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8') != text:
            raise SystemExit('FAIL: missing or stale retained-word receipt')
    else:
        DEST.parent.mkdir(parents=True, exist_ok=True)
        DEST.write_text(text, encoding='utf-8')
    print('PASS: source retained ledger composes the candidate words with exact coefficients and provenance.')
    print('PASS: forgetting segmentation loses continuation timing; multiplicative plane transport has only zero one-step-stable output.')
    print('Boundary: these two scoped shortcuts fail, not all retained-state constructions.')


if __name__ == '__main__':
    main()
