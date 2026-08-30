import json
from pathlib import Path

n = 5
# Basis ordering: regular r_i, logarithmic l_i for i in Z/5.
T = [[0] * (2 * n) for _ in range(2 * n)]
N = [[0] * (2 * n) for _ in range(2 * n)]
for i in range(n):
    T[(i + 1) % n][i] = 1
    T[n + (i + 1) % n][n + i] = 1
    N[i][n + i] = 1

def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def rank(a):
    a = [list(map(int, r)) for r in a]
    out = 0
    for c in range(len(a[0])):
        p = next((i for i in range(out, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[out], a[p] = a[p], a[out]
        pv = a[out][c]
        for i in range(len(a)):
            if i != out and a[i][c]:
                q = a[i][c]
                a[i] = [pv * x - q * y for x, y in zip(a[i], a[out])]
        out += 1
    return out

N2 = mm(N, N)
assert mm(T, N) == mm(N, T)
assert rank(N) == 5 and all(x == 0 for r in N2 for x in r)
chars = []
Tk = [[int(i == j) for j in range(2 * n)] for i in range(2 * n)]
for _ in range(n):
    chars.append(sum(Tk[i][i] for i in range(2 * n)))
    Tk = mm(Tk, T)

packet = {
    'schema': 'marici.five_site_g5_logarithmic_orbit.v1',
    'orbit_size': n,
    'total_extension_rank': 2 * n,
    'nilpotent_rank': rank(N),
    'nilpotent_square_zero': True,
    'cyclic_character_on_total_extension': chars,
    'cyclic_character_on_logarithmic_lines': [5, 0, 0, 0, 0],
    'cyclic_transport_commutes_with_nilpotent': True,
}
Path('research/benincasa/results/five-site-g5-logarithmic-orbit.json').write_text(
    json.dumps(packet, indent=2, sort_keys=True) + '\n', encoding='utf-8')
print(json.dumps(packet, sort_keys=True))
