"""Gram selection principle: N-path interference from filler overlaps.
For N alternatives with Gram G_ij = <f_j|f_i>, the interference pattern is
I(theta) = sum_{i,j} G_ij exp(i(theta_j - theta_i)). No superposition postulate.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import cmath

OWNER = Path(__file__).resolve().parents[1]

def code(pt):
    return (1 if pt[0] else 0) * 2 + (1 if pt[1] else 0)

CODES = [(False, False), (False, True), (True, False), (True, True)]
def image_vec(f):
    return [code(f(pt)) for pt in CODES]
def dot(u, v):
    return sum(a*b for a,b in zip(u, v))
def norm2(v):
    return dot(v, v)

def identity(pt):  return pt
def swap(pt):      return (pt[1], pt[0])
def twist(pt):
    if pt[0]: return (pt[0], not pt[1])
    return pt
def flip_fst(pt):  return (not pt[0], pt[1])
def flip_both(pt): return (not pt[0], not pt[1])

FILLERS = {'id': identity, 'swap': swap, 'twist': twist,
           'flip_fst': flip_fst, 'flip_both': flip_both}

def N_slit_intensity(G, phases):
    """I(theta) = sum_{i,j} G_ij * exp(i*(theta_j - theta_i))"""
    N = len(G)
    total = 0j
    for i in range(N):
        for j in range(N):
            total += G[i][j] * cmath.exp(1j * (phases[j] - phases[i]))
    return total.real

def main():
    out = OWNER / 'results/gram-selection-principle.json'
    out.unlink(missing_ok=True)

    names = list(FILLERS.keys()); n = len(names)
    vecs = [image_vec(FILLERS[name]) for name in names]
    
    # Gram: G_ij = normalized overlap <f_j | f_i>
    n2s = [norm2(v) for v in vecs]
    G_raw = [[dot(vecs[i], vecs[j]) for j in range(n)] for i in range(n)]
    G = [[G_raw[i][j] / (n2s[i]**0.5 * n2s[j]**0.5) for j in range(n)] for i in range(n)]
    
    # Check Gram is positive semidefinite (all eigenvalues >= 0)
    import numpy as np
    eigenvals = np.linalg.eigvalsh(np.array(G))
    PSD = all(ev >= -1e-12 for ev in eigenvals)

    # For each pair (N=2), verify the standard double-slit formula.
    pairs = {}
    for i in range(n):
        for j in range(i+1, n):
            gamma = G[i][j]
            V = abs(gamma)
            D = (1 - V**2)**0.5
            # Test N=2 interference formula.
            test_phases = [(0.0, 0.0), (0.0, 3.14159), (0.0, 1.5708)]
            expected = [1+gamma.real, 1-gamma.real, 1+gamma.imag]
            results = []
            for (p1, p2), exp in zip(test_phases, expected):
                I = N_slit_intensity([[G[i][i], G[i][j]], [G[j][i], G[j][j]]], [p1, p2])
                results.append({'phases': [p1, p2], 'I': round(I, 10), 'expected': round(exp, 10)})
            pairs[f"{names[i]}_{names[j]}"] = {
                'gamma': (round(gamma.real, 6), round(gamma.imag, 6)),
                'V': round(V, 6), 'D': round(D, 6),
                'V2_D2': round(V*V + D*D, 10),
                'tests': results,
            }

    # For each triple (N=3), compute the 3-slit Gram and intensity pattern.
    triples = {}
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                G3 = [[G[p][q] for q in (i,j,k)] for p in (i,j,k)]
                I0 = N_slit_intensity(G3, [0.0, 0.0, 0.0])
                I12 = N_slit_intensity(G3, [0.0, 1.0, 0.0])
                triples[f"{names[i]}_{names[j]}_{names[k]}"] = {
                    'G': [[round(x, 4) for x in row] for row in G3],
                    'I_uniform': round(I0, 6),
                    'I_phase12': round(I12, 6),
                }

    result = {
        'schema': 'marici.nima.gram-selection-principle.v1',
        'classification': 'n_path_interference_from_gram_overlaps_without_superposition',
        'n_fillers': n,
        'gram_psd': PSD,
        'eigenvalues': [round(float(ev), 6) for ev in eigenvals],
        'two_slit_pairs': pairs,
        'three_slit_triples': triples,
        'principle': ('The N-slit interference formula I(theta) = sum G_ij exp(i*(theta_j - theta_i)) '
                      'follows from the Gram matrix of record state overlaps. '
                      'No superposition, no Born rule, no probability. '
                      'The Gram is determined by the source-admitted positive pairing.'),
        'missing': ('N-slit diffraction envelope from continuous aperture. '
                    'Summing infinitely many alternatives requires a limit of the Gram. '
                    'The path integral is that limit.'),
        'input_sha256': {str(Path(__file__).relative_to(OWNER)):
                        hashlib.sha256(open(__file__, 'rb').read()).hexdigest()},
    }
    out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()