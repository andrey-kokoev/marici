#!/usr/bin/env python3
"""Finite checks for Fourier transform as character linearization of a Segal translation object."""
import cmath
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def elements(moduli):
    return list(itertools.product(*(range(n) for n in moduli)))


def add(a, b, moduli):
    return tuple((x + y) % n for x, y, n in zip(a, b, moduli))


def neg(a, moduli):
    return tuple((-x) % n for x, n in zip(a, moduli))


def conv(f, h, E, moduli):
    out = {g: 0j for g in E}
    for a in E:
        for b in E:
            out[add(a, b, moduli)] += f[a] * h[b]
    return out


def char(k, g, moduli):
    phase = sum(ki * gi / n for ki, gi, n in zip(k, g, moduli))
    return cmath.exp(2j * math.pi * phase)


def fourier(f, E, dual, moduli):
    return {k: sum(f[g] * char(k, g, moduli).conjugate() for g in E) for k in dual}


def close(a, b, tol=2e-9):
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


rows = []
for moduli in [(2,), (3,), (4,), (5,), (2, 2), (2, 3), (2, 2, 2)]:
    E = elements(moduli)
    dual = elements(moduli)
    zero = tuple(0 for _ in moduli)
    f = {g: complex(1 + sum((i + 1) * x for i, x in enumerate(g)), sum(g) % 3 - 1) for g in E}
    h = {g: complex(2 - sum(g), 1 + sum((i + 2) * x for i, x in enumerate(g))) for g in E}
    q = {g: complex((3 + sum(g)) % 5 - 2, 2 - sum(g)) for g in E}

    # Segal long-edge coherence: all parenthesizations of three translations agree.
    segal = all(
        add(add(a, b, moduli), c, moduli) == add(a, add(b, c, moduli), moduli)
        for a in E for b in E for c in E
    )
    unit = all(add(g, zero, moduli) == g == add(zero, g, moduli) for g in E)

    # Character realization preserves every binary gluing.
    character_gluing = all(
        close(char(k, add(a, b, moduli), moduli), char(k, a, moduli) * char(k, b, moduli))
        for k in dual for a in E for b in E
    )
    reversal = all(
        close(char(k, neg(g, moduli), moduli), char(k, g, moduli).conjugate())
        for k in dual for g in E
    )

    fh = conv(f, h, E, moduli)
    Ff, Fh, Ffh = fourier(f, E, dual, moduli), fourier(h, E, dual, moduli), fourier(fh, E, dual, moduli)
    convolution_theorem = all(close(Ffh[k], Ff[k] * Fh[k]) for k in dual)

    # Associativity after push-pull linearization.
    left = conv(conv(f, h, E, moduli), q, E, moduli)
    right = conv(f, conv(h, q, E, moduli), E, moduli)
    convolution_associative = all(close(left[g], right[g]) for g in E)

    # Character completeness, inversion, and Plancherel.
    orthogonality = all(
        close(sum(char(k, add(g, neg(a, moduli), moduli), moduli) for k in dual), len(E) if g == a else 0)
        for g in E for a in E
    )
    recovered = {
        g: sum(Ff[k] * char(k, g, moduli) for k in dual) / len(E)
        for g in E
    }
    inversion = all(close(recovered[g], f[g]) for g in E)
    lhs = sum(f[g] * h[g].conjugate() for g in E)
    rhs = sum(Ff[k] * Fh[k].conjugate() for k in dual) / len(E)
    plancherel = close(lhs, rhs)

    checks = {
        'segal_long_edge_coherence': segal,
        'unital_degeneracy': unit,
        'scalar_realizations_preserve_gluing': character_gluing,
        'direction_reversal_is_conjugation': reversal,
        'push_pull_convolution_associative': convolution_associative,
        'fourier_converts_convolution_to_product': convolution_theorem,
        'character_orthogonality': orthogonality,
        'fourier_inversion': inversion,
        'plancherel': plancherel,
    }
    rows.append({'group_moduli': list(moduli), 'order': len(E), 'character_count': len(dual), 'checks': checks})

checks = {
    'all_finite_models_pass': all(all(r['checks'].values()) for r in rows),
    'dual_cardinality_equals_group_cardinality': all(r['character_count'] == r['order'] for r in rows),
    'product_groups_included': any(len(r['group_moduli']) > 1 for r in rows),
}
out = {
    'schema': 'marici.nima.finite-fourier-segal-character-linearization.v1',
    'theorem': 'For finite abelian G, Fourier transform is simultaneous evaluation of the push-pull convolution algebra on all unitary scalar coherent realizations of N(BG).',
    'models': rows,
    'checks': checks,
    'passed': all(checks.values()),
    'proof_note': 'research/nima/fourier-transform-as-character-linearization-of-segal-translation-object.md',
    'scope': 'Executable finite models support the written general proof. Floating evaluation is used only for roots of unity; the proof uses exact finite-character orthogonality.',
}
path = ROOT / 'research/nima/results/finite-fourier-segal-character-linearization.json'
path.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
raise SystemExit(0 if out['passed'] else 1)
