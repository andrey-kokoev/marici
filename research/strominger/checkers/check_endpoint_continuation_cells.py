"""Exhaustive task-restriction atlas for the frozen native-query automaton.
No physical cell or endpoint language is assumed. Standard library only.
"""
from collections import Counter, deque
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/strominger'
FRAGMENT = BASE / 'contracts/native-query-source-fragment.v1.json'
SOURCE = ROOT / 'research/nima/agda/NativeSeedTransitionProbe.agda'
fragment = json.loads(FRAGMENT.read_text())
text = SOURCE.read_text()


def native(name):
    rows = dict(re.findall(r'^' + name + r' ([ABCD]) = ([ABCD])$', text, re.M))
    assert set(rows) == set('ABCD')
    return tuple('ABCD'.index(rows[v]) for v in 'ABCD')


def comp(h, g):
    return tuple(h[g[i]] for i in range(4))


left = {'L_ABC': native('abc'), 'L_ADB': native('adb')}
identity = tuple(range(4))
group = {identity}
queue = deque([identity])
while queue:
    g = queue.popleft()
    for h in left.values():
        k = comp(h, g)
        if k not in group:
            group.add(k)
            queue.append(k)
assert len(group) == 12
states = list(product(sorted(group), (0, 1)))
index = {s: i for i, s in enumerate(states)}
names = list(fragment['generators'])
assert set(names) == set(left) | {'Q_AB', 'Q_BC', 'Q_CA', 'Q_AD', 'Q_DB', 'Q_BA'}
outputs = tuple(b for g, b in states)
transitions = {}
for a in names:
    if a in left:
        successors = [(comp(left[a], g), b) for g, b in states]
    else:
        s, p = map('ABCD'.index, a[2:])
        successors = [(g, b ^ int(g[s] == p)) for g, b in states]
    transitions[a] = [index[x] for x in successors]


def canonical(signatures):
    labels = {}
    return tuple(labels.setdefault(x, len(labels)) for x in signatures)


def minimize(alphabet):
    colors = canonical(outputs)
    while True:
        refined = canonical((outputs[i], tuple(colors[transitions[a][i]] for a in alphabet))
                            for i in range(len(states)))
        if refined == colors:
            return colors
        colors = refined


def distinguish(i, j, alphabet):
    todo = deque([(i, j, [])])
    seen = {(i, j)}
    while todo:
        x, y, word = todo.popleft()
        if outputs[x] != outputs[y]:
            return word
        for a in alphabet:
            pair = (transitions[a][x], transitions[a][y])
            if pair not in seen:
                seen.add(pair)
                todo.append((*pair, word + [a]))
    return None


def execute(i, word):
    for a in word:
        i = transitions[a][i]
    return i


atlas = []
for mask in range(1 << len(names)):
    alphabet = [a for k, a in enumerate(names) if mask & (1 << k)]
    colors = minimize(alphabet)
    # Independently certify every pair by complete paired-state BFS.
    witnesses = []
    for i, j in combinations(range(len(states)), 2):
        word = distinguish(i, j, alphabet)
        assert (word is None) == (colors[i] == colors[j])
        if word is not None:
            assert outputs[execute(i, word)] != outputs[execute(j, word)]
            witnesses.append({'states': [i, j], 'word': word})
    atlas.append({'mask': mask, 'alphabet': alphabet, 'partition': colors,
                  'classes': len(set(colors)), 'separating_words': witnesses})

# More operations can split classes, never merge them.
for small in atlas:
    for big in atlas:
        if small['mask'] & big['mask'] == small['mask']:
            assert all(big['partition'][i] != big['partition'][j]
                       or small['partition'][i] == small['partition'][j]
                       for i, j in combinations(range(24), 2))

full = atlas[-1]
assert full['classes'] == 24
minimal_complete = [r for r in atlas if r['classes'] == 24 and
                    all(atlas[r['mask'] ^ (1 << k)]['classes'] < 24
                        for k in range(len(names)) if r['mask'] & (1 << k))]
# Minimal operation sets are NOT geometrical cells.
endpoint_tasks = []
for q in [a for a in names if a.startswith('Q_')]:
    for transports in ([], ['L_ABC'], ['L_ADB'], list(left)):
        alphabet = transports + [q]
        mask = sum(1 << names.index(a) for a in alphabet)
        r = atlas[mask]
        endpoint_tasks.append({'query': q, 'transports': transports,
                               'classes': r['classes'], 'partition': r['partition']})
# With both left actions, a query at input vertex s observes exactly g(s).
# Check the proposed coordinate projection for every one of 64 query subsets.
projection_checks = []
for r in atlas:
    if not all(a in r['alphabet'] for a in left):
        continue
    vertices = sorted({'ABCD'.index(a[2]) for a in r['alphabet'] if a.startswith('Q_')})
    predicted = canonical((b, tuple(g[s] for s in vertices)) for g, b in states)
    assert predicted == r['partition']
    expected_count = 2 if not vertices else 8 if len(vertices) == 1 else 24
    assert r['classes'] == expected_count
    projection_checks.append({'alphabet': r['alphabet'],
                              'input_vertices': ['ABCD'[s] for s in vertices],
                              'classes': r['classes']})
assert len(projection_checks) == 64
query_mask = sum(1 << k for k, a in enumerate(names) if a.startswith('Q_'))
queries = atlas[query_mask]
assert queries['classes'] == 20
# Find same-pointer states merged by ALL six queries but split by transport.
hidden = next((i, j) for i, j in combinations(range(24), 2)
              if queries['partition'][i] == queries['partition'][j])
hidden_word = distinguish(*hidden, names)
assert hidden_word and any(a in left for a in hidden_word)
report = {
    'status': 'pass',
    'scope': 'Exact finite automaton classification for all alphabet subsets; no physical or geometric cell identification.',
    'states': [{'g': ''.join('ABCD'[v] for v in g), 'bit': b} for g, b in states],
    'transitions': transitions,
    'alphabet_subset_count': len(atlas),
    'independent_pair_searches': len(atlas) * 276,
    'class_count_histogram': dict(sorted(Counter(r['classes'] for r in atlas).items())),
    'distinct_partitions': len({r['partition'] for r in atlas}),
    'full_word_length_histogram': dict(sorted(Counter(len(w['word']) for w in full['separating_words']).items())),
    'minimal_full_distinguishing_alphabets': [r['alphabet'] for r in minimal_complete],
    'endpoint_tasks': endpoint_tasks,
    'coordinate_projection_checks': projection_checks,
    'query_only_hidden_pair': {'states': hidden, 'separating_word': hidden_word,
                              'final_pointer_values': [outputs[execute(i, hidden_word)] for i in hidden]},
    'source_justification': 'Only the full eight-generator language is the frozen task. Alphabet subsets are explicitly hypothetical restrictions, not source-selected endpoint protocols.',
    'atlas': atlas,
    'sha256': {str(p.relative_to(ROOT)).replace('\\', '/'): hashlib.sha256(p.read_bytes()).hexdigest()
               for p in (FRAGMENT, SOURCE, Path(__file__).resolve())},
}
out = BASE / 'results/endpoint-continuation-cells/verification.json'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({k: v for k, v in report.items() if k not in
                  ('atlas', 'transitions', 'states', 'endpoint_tasks', 'coordinate_projection_checks', 'sha256')}, indent=2))
print('Endpoint tasks:', [(r['query'], r['transports'], r['classes']) for r in endpoint_tasks])
