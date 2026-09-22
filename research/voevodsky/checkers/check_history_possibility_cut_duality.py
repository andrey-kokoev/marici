"""Exact finite-language test of cut transport and logical reversal.

Words are admitted complete source developments. Every cut relation is
computed from that SAME language. Equality provides strict coherence;
no nontrivial homotopy or physical time interpretation is asserted.
"""
from itertools import product
from pathlib import Path
import json


def relation(language, k):
    return {(w[:k], w[k:]) for w in language}


def reverse(language):
    return {w[::-1] for w in language}


def move(pair, count):
    h, f = pair
    assert 0 <= count <= len(f)
    return h + f[:count], f[count:]


def flip(pair):
    h, f = pair
    return f[::-1], h[::-1]


def check(language):
    n = len(next(iter(language)))
    assert language and all(len(w) == n for w in language)
    opposite = reverse(language)
    assert reverse(opposite) == language
    checks = 0
    for k in range(n + 1):
        r = relation(language, k)
        assert {h + f for h, f in r} == language
        assert {flip(pair) for pair in r} == relation(opposite, n - k)
        assert all(flip(flip(pair)) == pair for pair in r)
        for j in range(k, n + 1):
            assert {move(pair, j - k) for pair in r} == relation(language, j)
            for pair in r:
                # Opposite orientation reverses the direction of cut movement.
                assert move(flip(move(pair, j - k)), j - k) == flip(pair)
                for ell in range(j, n + 1):
                    assert move(move(pair, j - k), ell - j) == move(pair, ell - k)
                    checks += 1
        for h in {h for h, _ in r}:
            tails = {f for hh, f in r if hh == h}
            for e in {f[:1] for f in tails if f}:
                sector = {f[1:] for f in tails if f.startswith(e)}
                after = {f for hh, f in relation(language, k + 1) if hh == h + e}
                assert sector == after
    return checks

# Exhaust all nonempty length-three binary languages, including asymmetric ones.
words = [''.join(w) for w in product('01', repeat=3)]
count = 0
for mask in range(1, 1 << len(words)):
    language = {w for i, w in enumerate(words) if mask & (1 << i)}
    count += check(language)

# Explicit adversary: marginals lose correlation at the same cut.
language = {'000', '011', '101'}
r = relation(language, 1)
cartesian = {(h, f) for h, _ in r for _, f in r}
assert len(r) == 3 and len(cartesian) == 6
assert ('1', '11') in cartesian - r
assert '111' not in language
# Logical reversal has a perfectly valid opposite language, but does not
# automatically give a word-reversal symmetry of the original language.
assert reverse(language) != language
assert '110' in reverse(language) - language
# Forgetting history destroys the inverse to cut transport: all complete
# developments have the same empty remaining tail at the terminal cut.
assert len({f for _, f in relation(language, 3)}) == 1
assert len(relation(language, 3)) == 3
report = {
    'passed': True,
    'nonempty_languages_exhausted': 255,
    'composition_instances_checked': count,
    'checks': {
        'cut_factorizations_reconstruct_same_source_language': True,
        'cut_transport_bijective_on_joint_pairs': True,
        'cut_transport_composition_strict': True,
        'reversal_involutive_between_language_and_opposite': True,
        'reversal_reverses_cut_transport': True,
        'extension_sector_equals_remaining_continuation_fiber': True,
        'cartesian_marginals_fabricate_source_developments': True,
        'same_language_word_reversal_symmetry_not_automatic': True,
        'forgetting_history_loses_invertibility': True,
    },
    'adversary': {'language': sorted(language), 'opposite': sorted(reverse(language)),
                  'joint_pairs': len(r), 'cartesian_pairs': len(cartesian)},
    'scope': 'Finite fixed-length binary source languages; strict equalities only. No actual assembled-observer integration, physical reversibility, or minimum tact claim.'
}
path = Path(__file__).resolve().parents[1] / 'results/history-possibility-cut-duality.json'
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
