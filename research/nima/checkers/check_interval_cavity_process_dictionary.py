"""Finite source-record/process dictionary, not a physical state encoding."""
import contextlib
import io
import json
import runpy
import sys
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/nima'))
from nnmhv_coherence_paths import compile_nnmhv_histories, supports_component_23
SOURCES = ['research/nima/checkers/check_physics_geometric_candidate.py',
           'research/nima/checkers/check_indexed_path_synthesis.py',
           'research/nima/nnmhv_coherence_paths.py',
           'research/nima/interval-cavity-process-dictionary-protocol.md',
           'research/nima/checkers/check_interval_cavity_process_dictionary.py']


def require(ok, why):
    if not ok:
        raise ValueError(why)


def transpose(a):
    return [list(row) for row in zip(*a)]


def hashes():
    return {p: sha256((ROOT / p).read_bytes()).hexdigest() for p in SOURCES}


def main():
    pins = hashes()
    g = runpy.run_path(str(ROOT / SOURCES[0]))
    with contextlib.redirect_stdout(io.StringIO()):
        path_api = runpy.run_path(str(ROOT / SOURCES[1]))
    compose = path_api['compose']
    mm, eye = g['mm'], g['eye']
    ws = [g['round_map'](k) for k in range(3)]
    records = {(h.inner_pair[1]-4, h.outer_pair[1]-4): h
               for h in compile_nnmhv_histories(8) if supports_component_23(h)}
    require(len(records) == 6, 'source record count')

    def process(i, j):
        require((i, j) in records, 'process domain')
        result = eye()
        for k in range(i-1, j):
            result = mm(ws[k], result)
        return result

    def recover(matrix):
        active = []
        for k in range(3):
            value = matrix[1+3*k][1+3*k]
            require(value in (F(-3, 5), F(1)), 'invalid diagonal signature')
            if value == F(-3, 5):
                active.append(k+1)
        require(active and active == list(range(active[0], active[-1]+1)), 'noninterval signature')
        pair = (active[0], active[-1])
        require(matrix == process(*pair), 'signature matches but full process differs')
        return records[pair]

    def word(i, j):
        return tuple((k, k+1) for k in range(i, j+1))

    def pair(p):
        return p[0][0], p[-1][0]

    def step(p, tag):
        i, j = pair(p)
        if tag == 'L':
            require(i > 1, 'illegal L')
            return next(iter(compose({((i-1, i),)}, {p})))
        if tag == 'R':
            require(j < 3, 'illegal R')
            return next(iter(compose({p}, {((j+1, j+2),)})))
        require(i < j and tag in ('l', 'r'), 'illegal trim')
        return p[1:] if tag == 'l' else p[:-1]

    def trace(p, tags):
        out = [p]
        for tag in tags:
            out.append(step(out[-1], tag))
        return out

    def visible(p):
        i, j = pair(p)
        require(i < j, 'diagonal excluded from metric readout')
        return i, j

    counts = dict(records=0, edits=0, occupation_columns=0, adjacent_compositions=0, retained_squares=0)
    signature_rows = []
    for (i, j), record in records.items():
        p, V = word(i, j), process(i, j)
        require(recover(V) == record, 'full NNMHV record lost')
        require(bool(record.boundary_updates) == (i == j), 'boundary update mismatch')
        require(mm(transpose(V), V) == eye(), 'process not orthogonal')
        counts['records'] += 1
        signature_rows.append({'interval': [i, j], 'round_word': list(range(i-1, j)),
                               'signature': [str(V[1+3*k][1+3*k]) for k in range(3)]})
        for tag, legal in (('L', i > 1), ('R', j < 3), ('l', i < j), ('r', i < j)):
            if not legal:
                continue
            q = step(p, tag)
            expected = process(*pair(q))
            if tag == 'L':
                actual = mm(V, ws[i-2])
            elif tag == 'R':
                actual = mm(ws[j], V)
            elif tag == 'l':
                actual = mm(V, transpose(ws[i-1]))
            else:
                actual = mm(transpose(ws[j-1]), V)
            require(actual == expected and recover(actual) == records[pair(q)], 'edit operation square')
            correction = mm(expected, transpose(V))
            require(mm(correction, V) == expected, 'based final-state edit square')
            for n in (0, 1, 2):
                for b in g['basis'](n):
                    staged = g['lift_state'](correction, g['lift_column'](V, b))
                    require(staged == g['lift_column'](expected, b), 'lifted edit square')
                    require(g['inner'](staged, staged) == g['weight'](b), 'edit factorial norm')
                    counts['occupation_columns'] += 1
            counts['edits'] += 1
        for a, b in ((('L', 'R'), ('R', 'L')), (('l', 'R'), ('R', 'l'))):
            try:
                t1, t2 = trace(p, a), trace(p, b)
            except ValueError:
                continue
            require(t1[-1] == t2[-1] and t1 != t2, 'execution histories collapsed')
            require(process(*pair(t1[-1])) == process(*pair(t2[-1])), 'endpoint process square')
            counts['retained_squares'] += 1
    for i in range(1, 4):
        for cut in range(i, 3):
            for end in range(cut+1, 4):
                require(compose({word(i, cut)}, {word(cut+1, end)}) == {word(i, end)}, 'source concatenation')
                require(mm(process(cut+1, end), process(i, cut)) == process(i, end), 'adjacent process composition')
                counts['adjacent_compositions'] += 1

    hostiles = []
    def rejects(name, action):
        try:
            action()
        except ValueError:
            hostiles.append(name)
        else:
            raise AssertionError('corruption accepted: ' + name)
    rejects('out-of-domain-L', lambda: step(word(1, 2), 'L'))
    rejects('empty-trim', lambda: step(word(2, 2), 'l'))
    rejects('diagonal-metric-readout', lambda: visible(word(2, 2)))
    rejects('empty-signature', lambda: recover(eye()))
    rejects('noncontiguous-signature', lambda: recover(mm(ws[2], ws[0])))
    wrong = process(1, 2)
    wrong[9][8] += F(1)
    rejects('same-diagonal-corrupt-full-map', lambda: recover(wrong))
    require(mm(ws[0], ws[1]) != process(1, 2), 'wrong order did not differ')
    rejects('wrong-round-order', lambda: recover(mm(ws[0], ws[1])))
    V, S = process(1, 2), process(2, 2)
    require(mm(transpose(ws[0]), V) != S, 'bare prefix inverse escaped')
    hostiles.append('bare-left-prefix-inverse')
    vacuum = {g['VAC']: F(1)}
    require(all(g['lift_state'](process(*ij), vacuum) == vacuum for ij in records), 'vacuum control mismatch')
    hostiles.append('common-vacuum-is-not-faithful-state-encoding')
    require(hashes() == pins, 'source changed during execution')
    result = {'schema': 'marici.nima.interval-cavity-process-dictionary.v1', 'passed': True,
              'verdict': 'finite_process_dictionary_constructed_not_physical_state_encoding',
              'm': 3, 'n': 8, 'counts': counts, 'process_signatures': signature_rows,
              'hostiles': hostiles, 'inverse_controls': 'supplied mathematical capabilities',
              'physical_realization_admitted': False, 'causal_maps_derived': False,
              'history_policy': 'Retain source edit tags and intermediate records separately; process equality is not execution genealogy.',
              'source_sha256': pins}
    out = ROOT / 'research/nima/results/interval-cavity-process-dictionary.json'
    out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
