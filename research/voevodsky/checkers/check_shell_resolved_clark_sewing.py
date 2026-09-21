"""Exact Clark coefficients and piecewise-smooth two-shell Green regression.

Fixture: Phi(x)=exp(-x) on [0,2], split at 1. This tests shell bookkeeping,
not completed-theta positivity or an arithmetic source adapter.
"""
from pathlib import Path
import json
import sympy as sp
import mpmath as mp

ROOT = Path(__file__).resolve().parents[3]


def main():
    S = sp.I * sp.Matrix([[-1, 1, 1, 1], [-1, 1, -1, -1]]) / 2
    D = sp.diag(sp.I, -sp.I, sp.I, -sp.I)
    C = sp.simplify(D.conjugate().T * S.conjugate().T * sp.diag(1, -1) * S * D)
    expected = sp.Matrix([[0, 0, -1, 1], [0, 0, -1, 1], [-1, -1, 0, 0], [1, 1, 0, 0]]) / 2
    assert C == expected and C.eigenvals() == {-1: 1, 1: 1, 0: 2}
    assert C[0, :] + C[1, :] == sp.Matrix([[0, 0, -1, 1]])
    assert C[2, :] + C[3, :] == sp.zeros(1, 4)
    s, t = sp.symbols('s t')
    assert sp.cancel((1/s+1/(s-1)+1/t+1/(t-1))/(s+t-1)-1/(s*(t-1))-1/((s-1)*t)) == 0
    mp.mp.dps = 35
    intervals = [(mp.mpf(0), mp.mpf(1)), (mp.mpf(1), mp.mpf(2))]
    signs, moments = (1, -1, 1, -1), (0, 0, 1, 1)
    z, w = mp.mpc('.4', '.2'), mp.mpc('-.3', '.1')
    tolerance = mp.mpf('1e-27')

    def tail(shell, channel, spectral, x):
        left, right = intervals[shell]
        if x >= right:
            return mp.mpc(0)
        lower = max(x, left)
        frequency = signs[channel] * 1j * spectral
        a = frequency - 1
        if moments[channel] == 0:
            primitive = lambda q: mp.exp(a*q)/a
        else:
            primitive = lambda q: mp.exp(a*q)*(q/a-1/a**2)
        return mp.exp(-frequency*x)*(primitive(right)-primitive(lower))

    def forcing(shell, moment, x):
        left, right = intervals[shell]
        return x**moment * mp.exp(-x) if left < x < right else mp.mpf(0)

    def integral(f):
        return mp.quad(f, [0, 1, 2])

    def correlation(i, j, distance):
        lower = max(intervals[i][0], intervals[j][0]-distance)
        upper = min(intervals[i][1], intervals[j][1]-distance)
        if upper <= lower:
            return mp.mpf(0)
        primitive = lambda x: -mp.exp(-2*x)*(x/2+mp.mpf(1)/4+distance/2)
        return mp.exp(-distance)*(primitive(upper)-primitive(lower))

    records, endpoint_rows = [], {}
    for i in range(2):
        for j in range(2):
            N, bulk, full_forcing = mp.mpc(0), mp.mpc(0), mp.mpc(0)
            max_local_error = mp.mpf(0)
            for a in range(4):
                for b in range(4):
                    if C[a, b] == 0:
                        continue
                    coefficient = mp.mpf(int(C[a, b].p))/int(C[a, b].q)
                    endpoint = mp.conj(tail(i, a, w, 0))*tail(j, b, z, 0)
                    gram = integral(lambda x: mp.conj(tail(i, a, w, x))*tail(j, b, z, x))
                    source = integral(lambda x: forcing(i, moments[a], x)*tail(j, b, z, x)
                                      +mp.conj(tail(i, a, w, x))*forcing(j, moments[b], x))
                    factor = 1j*(signs[b]*z-signs[a]*mp.conj(w))
                    max_local_error = max(max_local_error, abs(endpoint-factor*gram-source))
                    N += coefficient*endpoint
                    bulk += coefficient*factor*gram
                    full_forcing += coefficient*source
            reduced = integral(lambda x: forcing(i, 0, x)*(tail(j, 3, z, x)-tail(j, 2, z, x))
                               +mp.conj(tail(i, 3, w, x)-tail(i, 2, w, x))*forcing(j, 0, x))
            corr = 2j*integral(lambda d: correlation(j, i, d)*mp.sin(mp.conj(w)*d)
                              -correlation(i, j, d)*mp.sin(z*d))
            assert max_local_error < tolerance
            assert abs(full_forcing-reduced) < tolerance
            assert abs(reduced-corr) < tolerance
            assert abs(N-bulk-reduced) < tolerance
            endpoint_rows[i, j] = N
            records.append({'shell_pair': [i, j], 'max_local_error': mp.nstr(max_local_error, 8),
                            'sewn_error': mp.nstr(abs(N-bulk-reduced), 8),
                            'correlation_error': mp.nstr(abs(reduced-corr), 8)})
    assert correlation(1, 0, mp.mpf('.5')) == 0
    assert correlation(0, 1, mp.mpf('.5')) > 0
    cross = endpoint_rows[0, 1] + endpoint_rows[1, 0]
    assert abs(cross) > mp.mpf('1e-5')
    # Off-diagonal shell numerators need not vanish at z=conj(w).
    real_z = mp.mpf('.4')
    residue = sum(mp.mpf(int(C[a, b].p))/int(C[a, b].q)
                  *mp.conj(tail(0, a, real_z, 0))*tail(1, b, real_z, 0)
                  for a in range(4) for b in range(4) if C[a, b])
    reverse_residue = sum(mp.mpf(int(C[a, b].p))/int(C[a, b].q)
                          *mp.conj(tail(1, a, real_z, 0))*tail(0, b, real_z, 0)
                          for a in range(4) for b in range(4) if C[a, b])
    assert abs(residue) > mp.mpf('1e-5')
    assert abs(residue+reverse_residue) < tolerance
    result = {
        'schema': 'marici.voevodsky.shell-resolved-clark-sewing.v1', 'passed': True,
        'exact_checks': ['Clark matrix and inertia', 'first-moment forcing cancellation', 'endpoint swap identity'],
        'fixture': 'exp(-x) on [0,2], split into [0,1] and [1,2]',
        'precision_digits': 35, 'tolerance': str(tolerance), 'shell_pair_checks': records,
        'cross_shell_numerator': mp.nstr(cross, 20),
        'off_diagonal_diagonal_residue': mp.nstr(residue, 20),
        'opposite_shell_residues_cancel': True,
        'scope': 'Numerical regression of proved first-order Green identities on compact L2 shell sources; not interval certification, completed-theta positivity, or route-event access.',
    }
    out = ROOT / 'research/voevodsky/results/shell-resolved-clark-sewing.json'
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
