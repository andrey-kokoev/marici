"""Exact finite regression for the all-n theorem in wg-interval-operation-bridge.md."""
import hashlib
import json
import sys
from dataclasses import replace
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/nima'))
from nnmhv_coherence_paths import (NNMHVHistory, BoundaryUpdate,
    compile_nnmhv_histories, supports_component_23, terminal_r_state)


def require(ok, why):
    if not ok:
        raise ValueError(why)


def canonical(n, b1, b2):
    require(n >= 6 and 5 <= b2 <= b1 <= n-1, 'source bounds')
    updates = (BoundaryUpdate('upper', (2, b1)),) if b1 == b2 else ()
    return NNMHVHistory(n, (2, b1), (3, b2), 'left-nested', (b1, 2), updates)


def validate(h):
    require(h == canonical(h.n, h.outer_pair[1], h.inner_pair[1]), 'noncanonical full record')


def encode(h):
    validate(h)
    return h.inner_pair[1]-4, h.outer_pair[1]-4


def decode(n, ij):
    i, j = ij
    require(1 <= i <= j <= n-5, 'interval bounds')
    return canonical(n, j+4, i+4)


def source_move(h, tag):
    validate(h)
    b1, b2 = h.outer_pair[1], h.inner_pair[1]
    require(tag in ('L', 'R'), 'unknown move')
    if tag == 'L':
        require(b2 > 5, 'left source boundary')
        return canonical(h.n, b1, b2-1)
    require(b1 < h.n-1, 'right source boundary')
    return canonical(h.n, b1+1, b2)


def target_move(n, ij, tag):
    i, j = ij
    require(1 <= i <= j <= n-5, 'invalid target')
    require(tag in ('L', 'R'), 'unknown target move')
    if tag == 'L':
        require(i > 1, 'left target boundary')
        return (i-1, j)
    require(j < n-5, 'right target boundary')
    return (i, j+1)


def available(n, ij):
    i, j = ij
    return tuple(t for t, ok in (('L', i > 1), ('R', j < n-5)) if ok)


def words(n, ij):
    yield ()
    for tag in available(n, ij):
        for tail in words(n, target_move(n, ij, tag)):
            yield (tag,) + tail


def source_path(h, word):
    states = [h]
    for tag in word:
        states.append(source_move(states[-1], tag))
    return tuple(states)


def target_path(n, ij, word):
    states = [ij]
    for tag in word:
        states.append(target_move(n, states[-1], tag))
    return tuple(states)


def source_tick(h, word):
    source_path(h, word)  # enforce admissible-word type
    if not word:
        return (h, ()), (h, 'idle', h)
    out = source_move(h, word[0])
    return (out, word[1:]), (h, word[0], out)


def target_tick(n, ij, word):
    target_path(n, ij, word)
    if not word:
        return (ij, ()), (ij, 'idle', ij)
    out = target_move(n, ij, word[0])
    return (out, word[1:]), (ij, word[0], out)


def main():
    counts = dict(records=0, edges=0, squares=0, paths=0, splits=0, ticks=0)
    for n in range(6, 16):
        selected = tuple(h for h in compile_nnmhv_histories(n) if supports_component_23(h))
        expected = {canonical(n, b1, b2) for b1 in range(5, n) for b2 in range(5, b1+1)}
        require(set(selected) == expected and len(selected) == len(expected), 'compiler mismatch')
        for h in selected:
            counts['records'] += 1
            ij = encode(h)
            require(decode(n, ij) == h, 'source inverse')
            require(encode(decode(n, ij)) == ij, 'target inverse')
            for tag in available(n, ij):
                out = source_move(h, tag)
                require(out in expected, 'move left compiler image')
                require(encode(out) == target_move(n, ij, tag), 'edge square')
                require(terminal_r_state(out) == terminal_r_state(decode(n, target_move(n, ij, tag))), 'spinor transport')
                counts['edges'] += 1
            if len(available(n, ij)) == 2:
                lr, rl = source_path(h, ('L','R')), source_path(h, ('R','L'))
                require(lr[-1] == rl[-1], 'endpoint square')
                require(lr != rl, 'history erased')
                counts['squares'] += 1
            if n <= 9:
                for word in words(n, ij):
                    sp = source_path(h, word)
                    tp = target_path(n, ij, word)
                    require(tuple(map(encode, sp)) == tp, 'path square')
                    require(tuple(decode(n, x) for x in tp) == sp, 'full path inverse')
                    counts['paths'] += 1
                    for cut in range(len(word)+1):
                        left = source_path(h, word[:cut])
                        right = source_path(left[-1], word[cut:])
                        require(left[:-1] + right == sp, 'join compatibility')
                        counts['splits'] += 1
                    (out, tail), witness = source_tick(h, word)
                    (tout, ttail), twitness = target_tick(n, ij, word)
                    require((encode(out), tail) == (tout, ttail), 'WG output')
                    require((encode(witness[0]), witness[1], encode(witness[2])) == twitness, 'WG witness')
                    counts['ticks'] += 1
    hostiles = []
    diagonal = canonical(9, 6, 6)
    for name, thunk in [
        ('stale-upper-update', lambda: validate(replace(source_move(diagonal, 'L'), boundary_updates=diagonal.boundary_updates))),
        ('stale-prefix', lambda: validate(replace(source_move(diagonal, 'R'), inner_prefix=diagonal.inner_prefix))),
        ('wrong-branch', lambda: encode(replace(diagonal, branch='right-nested'))),
        ('illegal-left', lambda: source_move(canonical(6, 5, 5), 'L')),
        ('illegal-right', lambda: target_move(6, (1,1), 'R')),
    ]:
        try:
            thunk()
        except ValueError:
            hostiles.append(name)
        else:
            raise AssertionError('hostile accepted: ' + name)
    a, b = source_path(diagonal, ('L','R')), source_path(diagonal, ('R','L'))
    require(a[0] == b[0] and a[-1] == b[-1] and a != b, 'endpoint quotient control')
    hostiles.append('endpoint-only-history-loss')
    files = ['research/nima/nnmhv_coherence_paths.py',
             'research/nima/wg-interval-operation-bridge.md',
             Path(__file__).relative_to(ROOT).as_posix()]
    result = {'schema': 'marici.nima.wg-interval-operation-bridge.v1', 'passed': True,
        'scope': 'Exact finite regression n=6..15; all admissible paths n=6..9. All-n proof is in the note. Declared controlled WG, not autonomous native selection or geometry.',
        'counts': counts, 'hostiles': hostiles,
        'source_sha256': {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in files},
        'WG_I1_resolved': False, 'WG_G1_resolved': False, 'WG_G2_resolved': False}
    out = ROOT/'research/nima/results/wg-interval-operation-bridge.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
