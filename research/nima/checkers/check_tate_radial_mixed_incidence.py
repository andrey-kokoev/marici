"""Exact finite Tate residue/radial incidence audit (standard library only).

V_N is the additive cyclic model Z/(p^(2N)); radial shells are unit orbits.
Averages use the uniform counting inner product. The radial indicator basis
has metric diag(shell sizes), so its matrices need not look symmetric.
No identification with the arithmetic Green/primitive-square packet is assumed.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def mul(a, b):
    return [[sum((x*y for x, y in zip(row, col)), F(0))
             for col in zip(*b)] for row in a]


def sub(a, b):
    return [[x-y for x, y in zip(r, s)] for r, s in zip(a, b)]


def scale(c, a):
    return [[c*x for x in row] for row in a]


def rank(a):
    a = [row[:] for row in a]
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        c = a[r][j]
        a[r] = [x/c for x in a[r]]
        for i in range(r+1, len(a)):
            c = a[i][j]
            if c:
                a[i] = [x-c*y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def shell(j, p, exponent):
    if not j:
        return exponent
    v = 0
    while j % p == 0:
        j //= p
        v += 1
    return v


def radial_matrix(p, N, k):
    exponent = 2*N
    size = p**exponent
    labels = [shell(j, p, exponent) for j in range(size)]
    sizes = [labels.count(i) for i in range(exponent+1)]
    counts = [[0]*(exponent+1) for _ in sizes]
    for j in range(size):
        counts[labels[(j+p**k) % size]][labels[j]] += 1
    return [[F(c, sizes[i]) for c in row] for i, row in enumerate(counts)], sizes


def main():
    cases = []
    for p in (2, 3, 5, 7):
        for N in (1, 2, 3):
            for k in range(2*N):
                A, sizes = radial_matrix(p, N, k)
                I = identity(len(A))
                assert all(sizes[i]*A[i][j] == sizes[j]*A[j][i]
                           for i in range(len(A)) for j in range(len(A)))
                # Self-adjoint A has eigenvalues 1,-1/(p-1),0.
                third_factor = sub(scale(p-1, A), scale(-1, I))
                polynomial = mul(mul(sub(A, I), A), third_factor)
                assert not any(x for row in polynomial for x in row)
                assert len(A)-rank(sub(A, I)) == k+1
                assert len(A)-rank(third_factor) == 1
                assert len(A)-rank(A) == 2*N-k-1
                # C C* restricted to radial functions equals I-A^2.
                gram = sub(I, mul(A, A))
                expected_rank = 2*N-k-1 if p == 2 else 2*N-k
                assert rank(gram) == expected_rank
                cases.append({'p': p, 'N': N, 'v_p_h': k-N,
                              'active_rank': expected_rank,
                              'active_singular_values_squared':
                              ([str(F(1)-F(1, (p-1)**2))] if p > 2 else [])
                              + (['1'] if 2*N-k-1 else [])})

    # Independent full four-state construction of R T (I-R).
    labels = [shell(j, 2, 2) for j in range(4)]
    R = [[F(labels[i] == labels[j], labels.count(labels[i]))
          for j in range(4)] for i in range(4)]
    T = [[F(i == (j+1) % 4) for j in range(4)] for i in range(4)]
    C = mul(mul(R, T), sub(identity(4), R))
    expected = scale(F(1, 2), [[0,-1,0,1], [0,0,0,0],
                              [0,1,0,-1], [0,0,0,0]])
    assert C == expected
    assert mul(R, C) == C
    assert not any(x for row in mul(C, R) for x in row)
    assert not any(x for row in mul(C, C) for x in row)
    adjoint = list(map(list, zip(*C)))
    for gram in (mul(C, adjoint), mul(adjoint, C)):
        assert mul(gram, gram) == gram and rank(gram) == 1

    report = {
        'status': 'passed', 'exact_radial_cases': len(cases),
        'full_p2_N1_fixture': 'passed',
        'scope': 'Finite radial compression, multiplicities, and mixed-incidence active singular values. Fourier/dilation identities follow separately from the group action; no arithmetic packet identification or completion bound is certified here.',
        'cases': cases,
    }
    out = Path(__file__).resolve().parent.parent/'results'/'tate-radial-mixed-incidence.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(f'PASS: {len(cases)} exact radial cases; full p=2,N=1 mixed-incidence fixture.')
    print('All nonzero singular values squared are 1 or 1-1/(p-1)^2.')
    print('Active rank may be zero (p=2, v_p(h)=N-1).')


if __name__ == '__main__':
    main()
