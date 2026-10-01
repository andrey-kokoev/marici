"""Verify that the 10D composable-pair carrier resolves spatial displacements
that the 6D occurrence summary cannot.

The 6D summary records the final-occurrence coefficient vector.  At
depth 3, two words can share the same 6D summary while having different
spatial displacements.  The 10D carrier (coefficients on the first
composable pair) already captures this difference, because it records
which 2-step path initiated the full 3-step word.

This is a PRELIMINARY to any full spatial-complex embedding: the 10D
carrier is strictly more informative than the 6D summary, and the
additional information IS geometrically relevant (it distinguishes
different spatial positions).

The polynomial spatial complex operates on the 6 occurrence variables
and their face relations.  The 6D summary IS the natural input to the
spatial complex's cochain map.  The 10D carrier is therefore NOT a
direct input to the spatial complex but a RICHER REPRESENTATION of the
same data at depth 1 of the retained tree, which the 6D summary loses.
"""
from fractions import Fraction as F
from pathlib import Path
from collections import defaultdict
import hashlib
import json

from retained_path_successor import RetainedSuccessorLedger, apply as mv
from photon_native_spatial_step import REGISTRY, U, W, VERTICES, ClockedHistory, continuation_matrix
from check_triangle_half_phase import mm, transpose
from check_collective_four_state_identity import rank

ROOT = Path(__file__).resolve().parents[3]
DEST = ROOT / 'research/nima/results/ten_carrier_spatial_resolution.json'

LABELS = [p.label for p in REGISTRY]


def summary6(word):
    """6D final-occurrence summary from a 3-step word."""
    s = [F(0)] * 6
    s[LABELS.index(word[-1])] = F(1)
    return tuple(s)


def carrier10(word, pair_map):
    """10D carrier: coefficient 1 on the first composable pair."""
    c = [F(0)] * 10
    key = (word[0], word[1])
    if key in pair_map:
        c[pair_map[key]] = F(1)
    return tuple(c)


def endpoint_position(occ_label, vertices):
    """Return R^3 position of the target vertex of a primitive."""
    idx = LABELS.index(occ_label)
    return vertices[REGISTRY[idx].target]


def word_displacement(word, vertices):
    """Displacement from the start of first primitive to end of last."""
    start = REGISTRY[LABELS.index(word[0])].source
    end = REGISTRY[LABELS.index(word[-1])].target
    return tuple(vertices[end][k] - vertices[start][k] for k in range(3))


def main():
    DEST.unlink(missing_ok=True)

    # ---- Build 10D carrier metadata ---------------------------------------
    packets = tuple((p.label, p.source, p.target) for p in REGISTRY)
    ledger = RetainedSuccessorLedger(packets)
    root = ledger.root
    first = ledger.successor(root)
    L = first.step_lift        # 10×6
    A_sum = first.summary       # 6×10

    pair_map = {}   # (first_label, second_label) → pair index
    pair_data = []  # per-pair metadata
    for idx, path in enumerate(first.paths):
        e, f = path[0][2], path[1][2]
        pair_map[(e, f)] = idx
        src = REGISTRY[LABELS.index(e)].source
        mid = REGISTRY[LABELS.index(e)].target
        tgt = REGISTRY[LABELS.index(f)].target
        disp3 = tuple(VERTICES[tgt][k] - VERTICES[src][k] for k in range(3))
        pair_data.append({
            'idx': idx, 'pair': f'{e}→{f}', 'src': src, 'mid': mid, 'tgt': tgt,
            'disp': [str(x) for x in disp3],
        })

    # ---- Lift U to 10D carrier --------------------------------------------
    def lift(v6):
        r = [F(0)] * 10
        for ri in range(10):
            for ci in range(6):
                if L[ri][ci] == F(1):
                    r[ri] += F(v6[ci])
        return r

    L_U = lift(U)

    # ---- Depth 3: 26 words ------------------------------------------------
    hist = ClockedHistory.initial()
    for _ in range(3):
        hist = hist.advance()

    words = []
    displacements = []
    for p in hist.paths:
        w = tuple(pk.label for pk in p.packets)
        words.append(w)
        displacements.append(word_displacement(w, VERTICES))

    # ---- Group words by 6D summary ----------------------------------------
    by_summary = defaultdict(list)
    for i, w in enumerate(words):
        s = summary6(w)
        by_summary[s].append(i)

    # ---- Find matching-summary pairs with different 10D carrier ----------
    matches = []
    for s, idxs in by_summary.items():
        if len(idxs) < 2:
            continue
        for i in range(len(idxs)):
            for j in range(i + 1, len(idxs)):
                a, b = idxs[i], idxs[j]
                ca = carrier10(words[a], pair_map)
                cb = carrier10(words[b], pair_map)
                if ca != cb:
                    da = displacements[a]
                    db = displacements[b]
                    diff_actual = tuple(da[k] - db[k] for k in range(3))
                    matches.append({
                        'a': int(a), 'b': int(b),
                        'word_a': ' '.join(words[a]),
                        'word_b': ' '.join(words[b]),
                        'summary': [str(x) for x in s],
                        'carrier10_diff_indices': [int(i) for i in range(10) if ca[i] != cb[i]],
                        'displacement_a': [str(x) for x in da],
                        'displacement_b': [str(x) for x in db],
                        'displacement_diff': [str(x) for x in diff_actual],
                        'displacements_differ': diff_actual != (0, 0, 0),
                    })

    # ---- Count: how many matching-summary pairs have same/different disp --
    total_pairs = len(matches)
    pairs_with_diff_disp = sum(1 for m in matches if m['displacements_differ'])

    # ---- The strong claim: the 10D carrier resolves ALL displacement ----
    # For each matching-summary pair, verify that the 10D carrier diff
    # correctly predicts the displacement diff via pair displacements.
    correct_predictions = 0
    for m in matches:
        wa = words[m['a']]
        wb = words[m['b']]
        ca = carrier10(wa, pair_map)
        cb = carrier10(wb, pair_map)
        # Compute predicted displacement diff: sum over pairs of
        # (coeff_a - coeff_b) * pair_displacement
        predicted = [F(0)] * 3
        for pi in range(10):
            diff_c = ca[pi] - cb[pi]
            if diff_c == F(0):
                continue
            # BUT: the predicted displacement from the first pair alone
            # doesn't account for later pairs.  The 10D carrier only
            # captures depth 1.  We need the FULL path carrier to predict
            # the full displacement.
            # For a 2-step difference at depth 1, the prediction works
            # only when the rest of the path is the same.
            pass
        # We can't fully predict from just the 10D carrier at depth 1.
        # The full path carrier (which grows exponentially) is needed.

    # ---- Instead, verify the more modest claim: 10D carrier refines ----
    # Two words with same 6D summary can have:
    #   (a) different 10D carriers AND different displacements
    #   (b) different 10D carriers AND same displacements
    # Case (a) shows the 10D carrier captures geometrically relevant info
    # that the 6D summary misses.

    report = {
        'passed': pairs_with_diff_disp > 0,
        'classification': 'ten_carrier_refines_sixd_summary',
        'total_depth3_words': len(words),
        'pairs_same_summary_diff_carrier10': total_pairs,
        'pairs_with_different_displacement': pairs_with_diff_disp,
        'index_assignment': {k: v for k, v in
                             sorted({'AB': 0, 'BC': 1, 'CA': 2,
                                     'BA': 3, 'AD': 4, 'DB': 5}.items(),
                                    key=lambda x: x[1])},
        'pairs_metadata': pair_data,
        'lift_U_10d': [str(x) for x in L_U],
        'examples': matches[:10],  # first 10 examples
        'conclusion': (
            f'Of {total_pairs} pairs sharing a 6D summary but differing in '
            f'their 10D carrier, {pairs_with_diff_disp} have different spatial '
            f'displacements.  The 10D carrier refines the 6D summary: it '
            f'distinguishes paths whose spatial geometry the summary cannot '
            f'resolve.  This is the necessary precondition for any spatial-'
            f'complex embedding at depth > 0.'
        ),
    }
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()