#!/usr/bin/env python3
"""Exact finite Fourier regression in cyclotomic number rings.

Run: uv run --with sympy python research/nima/checkers/check_finite_fourier_segal_exact.py
The general theorem is in the accompanying proof note.
"""
import itertools
import json
import math
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
x = s.Symbol('x')
rows = []
for moduli in [(1,), (2,), (3,), (4,), (5,), (2, 2), (2, 3), (2, 2, 2)]:
    E = list(itertools.product(*(range(n) for n in moduli)))
    order = len(E)
    period = math.lcm(*moduli)
    phi = s.Poly(s.cyclotomic_poly(period, x), x, domain=s.QQ)

    def reduce(value):
        return s.rem(s.Poly(value, x, domain=s.QQ), phi).as_expr()

    powers = [reduce(x**j) for j in range(period)]

    def phase(k, g, sign=1):
        exponent = sum(a*b*(period//n) for a, b, n in zip(k, g, moduli))
        return powers[(sign*exponent) % period]

    def add(a, b):
        return tuple((u+v) % n for u, v, n in zip(a, b, moduli))

    def convolution(f, h):
        out = dict.fromkeys(E, s.Integer(0))
        for a in E:
            for b in E:
                out[add(a, b)] += f[a]*h[b]
        return out

    def transform(f, sign=-1):
        return {k: reduce(sum(f[g]*phase(k, g, sign) for g in E)) for k in E}

    f = {g: s.Integer(1+sum((i+1)*a for i, a in enumerate(g))) for g in E}
    h = {g: s.Integer(2-sum((i+2)*a for i, a in enumerate(g))) for g in E}
    Ff, Fh = transform(f), transform(h)
    Fconv = transform(convolution(f, h))
    inverse = transform(Ff, sign=1)
    conjugate_Fh = transform(h, sign=1)  # h has real integer coefficients.

    # Exact orthogonality of the full Fourier matrix, not just a test vector.
    orthogonal = all(
        reduce(sum(phase(k, a, -1)*phase(k, b, 1) for k in E))
        == (order if a == b else 0)
        for a in E for b in E
    )
    # Exact multiplicativity on every pair of delta-function basis vectors.
    basis_multiplicative = all(
        reduce(phase(k, add(a, b), -1)-phase(k, a, -1)*phase(k, b, -1)) == 0
        for k in E for a in E for b in E
    )
    checks = {
        'segal_associativity': all(add(add(a, b), c) == add(a, add(b, c))
                                  for a in E for b in E for c in E),
        'full_fourier_matrix_orthogonality': orthogonal,
        'all_basis_gluings_multiplicative': basis_multiplicative,
        'convolution': all(reduce(Fconv[k]-Ff[k]*Fh[k]) == 0 for k in E),
        'inversion': all(reduce(inverse[g]-order*f[g]) == 0 for g in E),
        'polarized_plancherel': reduce(
            sum(Ff[k]*conjugate_Fh[k] for k in E)
            -order*sum(f[g]*h[g] for g in E)) == 0,
        'reversal': all(phase(k, tuple((-a) % n for a, n in zip(g, moduli)))
                        == phase(k, g, -1) for k in E for g in E),
    }
    rows.append({'moduli': moduli, 'order': order,
                 'coefficient_ring': f'Q[x]/({phi.as_expr()})', 'checks': checks})

out = {'schema': 'marici.nima.finite-fourier-segal-exact.v1',
       'models': rows,
       'passed': all(all(row['checks'].values()) for row in rows),
       'scope': 'Exact cyclotomic arithmetic; finite regression of the written theorem, not analytic verification.'}
path = ROOT/'research/nima/results/finite-fourier-segal-exact.json'
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
raise SystemExit(0 if out['passed'] else 1)
