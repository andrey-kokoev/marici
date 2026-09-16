"""Numerical hostile search for Hermite--Biehler positivity of the standard Xi kernel.

Requires mpmath and numpy. Exploratory only: no interval certification.
"""
import json
import mpmath as mp
import numpy as np

mp.mp.dps = 30
PI = mp.pi


def phi(u):
    eu = mp.exp(2 * u)
    total = mp.mpf("0")
    # At u>=0 the n-series is extremely rapidly convergent.
    for n in range(1, 30):
        term = (4 * PI**2 * n**4 * mp.exp(9*u/2) - 6 * PI * n**2 * mp.exp(5*u/2)) * mp.exp(-PI*n*n*eu)
        total += term
        if n > 3 and abs(term) < mp.mpf("1e-35"):
            break
    return total


def m(z):
    return mp.quad(lambda u: phi(u) * mp.exp(-z*u), [0, 1, 2, 4, 7])


def main():
    # First scan diagonal positivity; then selected 2x2 Gram packets.
    points = [mp.mpc(a, t) for a in (mp.mpf("0.1"), mp.mpf("0.3"), mp.mpf("0.7"), mp.mpf("1.2")) for t in (0, 7, 14, 20)]
    values = {str(z): m(z) for z in points}
    reflected = {str(z): m(-z) for z in points}

    def kernel(w, z):
        return (reflected[str(z)] * mp.conj(reflected[str(w)]) - values[str(z)] * mp.conj(values[str(w)])) / (z + mp.conj(w))

    diag = [(z, mp.re(kernel(z, z))) for z in points]
    pairs = []
    minimum = (mp.inf, None)
    for i, z in enumerate(points):
        for w in points[i+1:]:
            G = np.array([[complex(kernel(z,z)), complex(kernel(w,z))], [complex(kernel(z,w)), complex(kernel(w,w))]], dtype=complex)
            eig = np.linalg.eigvalsh((G + G.conj().T)/2)
            pairs.append((z,w,float(eig[0])))
            if eig[0] < minimum[0]: minimum=(float(eig[0]),(z,w))
    out = {
        "minimum_diagonal": str(min(v for _,v in diag)),
        "minimum_2x2_eigenvalue": minimum[0],
        "minimum_pair": [str(minimum[1][0]),str(minimum[1][1])],
        "negative_diagonal_points": [[str(z),str(v)] for z,v in diag if v < 0],
        "negative_pair_count": sum(v < -1e-12 for _,_,v in pairs),
        "point_count": len(points),
        "pair_count": len(pairs)
    }
    print(json.dumps(out, indent=2))

if __name__ == "__main__": main()
