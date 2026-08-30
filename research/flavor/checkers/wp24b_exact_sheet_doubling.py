"""WP24b: exact form of the generation-exchange sheet doubling.

Theorem under test (diagonal class, permutation u-support):

  For any full-rank nine-link texture with permutation u-support and any
  physical point p with distinct nonzero singular values, a chart point
  theta_1 over p determines a second chart point theta_2 over the same p:

    Yu_2 = P01 Yu_1 P01            (exact)
    Yd_2 = P01 Yd_1 W,  W unitary  (exact; W closes the zero pattern)

  physical16(theta_2) = physical16(theta_1) exactly by construction.
  The sheet-2 loop phase is the arg of the loop monomial of Yd_2 -- chart
  data through W, not physical data.

Run: ../.venv/Scripts/python checkers/wp24b_exact_sheet_doubling.py
"""
import json, math, sys
from collections import Counter, defaultdict

import numpy as np

sys.path.insert(0, 'checkers')
import wp7_ensemble as wp7

P = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=complex)

def build(rec):
    mu, md = rec['member']; s, i, j = rec['phase_edge']
    return wp7.build_texture(mu, md, s, (i, j),
                             np.array(rec['log_mags'] + [rec['phi_raw']]))

def canonical_V(Yu, Yd):
    _, Uu = np.linalg.eigh(Yu @ Yu.conj().T)
    _, Ud = np.linalg.eigh(Yd @ Yd.conj().T)
    def gauge(U):
        for c in range(3):
            col = U[:, c]
            k = int(np.argmax(np.abs(col)))
            U[:, c] = col * np.exp(-1j * np.angle(col[k]))
        return U
    return gauge(Uu).conj().T @ gauge(Ud)

def edges_from_masks(mu, md):
    edges = []
    for sec, mask in (('u', mu), ('d', md)):
        for (i, j) in wp7.mask_slots(mask):
            a = ('q', i + 1)
            b = (('uc' if sec == 'u' else 'dc'), j + 1)
            edges.append((a, b, sec, i + 1, j + 1))
    nodes = set()
    for a, b, *_ in edges:
        nodes.add(a); nodes.add(b)
    return nodes, edges

def find_cycle(nodes, edges):
    adj = {n: [] for n in nodes}
    for k, (a, b, *_r) in enumerate(edges):
        adj[a].append((b, k)); adj[b].append((a, k))
    color = {n: 0 for n in nodes}
    parent = {}
    cyc = []
    def dfs(u, pe):
        color[u] = 1
        for v, k in adj[u]:
            if k == pe:
                continue
            if color[v] == 1:
                path = [k]; x = u
                while x != v:
                    px, pk = parent[x]
                    path.append(pk); x = px
                cyc.extend(path)
                return True
            if color[v] == 0:
                parent[v] = (u, k)
                if dfs(v, k):
                    return True
        color[u] = 2
        return False
    for n in nodes:
        if color[n] == 0 and dfs(n, None):
            return cyc
    return None

def loop_phase_numeric(mu, md, Yu, Yd):
    nodes, edges = edges_from_masks(mu, md)
    cyc = find_cycle(nodes, edges)
    if cyc is None:
        return None
    cedges = [edges[k] for k in cyc]
    adj = {}
    for e in cedges:
        a, b = e[0], e[1]
        adj.setdefault(a, []).append((b, e))
        adj.setdefault(b, []).append((a, e))
    start = cedges[0][0]
    M = 1 + 0j
    prev, cur = None, start
    while True:
        nxt = [(w, e) for w, e in adj[cur] if w != prev]
        if not nxt:
            break
        w, e = nxt[0]
        _, _, sec, i, j = e
        Y = Yu if sec == 'u' else Yd
        entry = Y[i - 1, j - 1]
        M *= np.conjugate(entry) if w[0] == 'q' else entry
        prev, cur = cur, w
        if cur == start:
            break
    return math.degrees(wp7.fold_phi(np.angle(M)))

def main():
    w20 = json.load(open('results/wp20_valley_audit.json'))['records']
    w21 = json.load(open('results/wp21e_universal_factorization.json'))['census']
    tex = defaultdict(list)
    for r in w20:
        key = f"{r['member'][0]}_{r['member'][1]}_{r['phase_edge'][0]}{r['phase_edge'][1]}{r['phase_edge'][2]}"
        tex[key].append(r)

    pairs = sorted(k for k in tex
                   if w21[k]['factorization_type'] == 'diagonal' and len(tex[k]) == 2)
    rows = []
    for k in pairs:
        r1, r2 = sorted(tex[k], key=lambda r: r['phi_folded_deg'])
        Yu1, Yd1 = build(r1); Yu2, Yd2 = build(r2)
        u_def = float(np.abs(Yu2 - P @ Yu1 @ P).max())
        Hd1 = Yd1 @ Yd1.conj().T; Hd2 = Yd2 @ Yd2.conj().T
        Hc = P @ Hd1 @ P
        mag_def = float(np.abs(np.abs(Hd2) - np.abs(Hc)).max())
        def tri_phase(H):
            return float(np.angle(H[0, 1] * H[1, 2] * H[2, 0]))
        tri_def = float(abs(np.angle(np.exp(1j * (tri_phase(Hd2) - tri_phase(Hc))))))
        # D' via spanning tree over structurally nonzero off-diagonal entries:
        # need d_i * conj(d_j) = Hd2_ij / Hc_ij on each nonzero entry; the
        # triangle-phase match certifies cycle closure.
        rel = 1e-9 * max(1.0, float(np.abs(Hc).max()))
        d = np.ones(3, dtype=complex)
        fixed = {0}
        for _ in range(3):
            for (i, j) in ((0, 1), (0, 2), (1, 2)):
                if abs(Hc[i, j]) < rel:
                    continue
                r = Hd2[i, j] / Hc[i, j]
                if i in fixed and j not in fixed:
                    d[j] = np.conj(r) * d[i] * np.exp(1j * np.angle(d[j] / (np.conj(r) * d[i])) * 0)
                    d[j] = d[i] / r
                    fixed.add(j)
                elif j in fixed and i not in fixed:
                    d[i] = r * d[j]
                    fixed.add(i)
        # normalize to unit modulus (should already be)
        d = d / np.abs(d)
        Dp = np.diag(d)
        dp_resid = float(np.abs(Hd2 - Dp @ Hc @ Dp.conj().T).max())
        # W with Yd2 = D' P01 Yd1 W
        W = np.linalg.solve(Dp @ P @ Yd1, Yd2)
        w_def = float(np.abs(W @ W.conj().T - np.eye(3)).max())
        v_def = mag_def  # magnitude channel; complex V certified in WP24c
        yd_min = float(np.sqrt(np.linalg.eigvalsh(Hd1)[0]))
        mu, md = r1['member']
        lp1 = loop_phase_numeric(mu, md, Yu1, Yd1)
        lp2 = loop_phase_numeric(mu, md, Yu2, Yd2)
        rows.append(dict(
            texture=k, u_defect=u_def,
            hd_mag_defect=mag_def, hd_triangle_phase_defect=tri_def,
            dprime_residual=dp_resid,
            w_unitarity_defect=w_def, w_def_scaled=w_def * yd_min**2,
            yd_min=yd_min,
            phi1_stored=r1['phi_folded_deg'], phi2_stored=r2['phi_folded_deg'],
            phi1_loop=lp1, phi2_loop=lp2,
            dphi=abs(r2['phi_folded_deg'] - r1['phi_folded_deg']),
            phase_edge=f"{r1['phase_edge'][0]}{r1['phase_edge'][1]}{r1['phase_edge'][2]}"))

    diag_all = sorted(k for k in tex if w21[k]['factorization_type'] == 'diagonal')
    obstr = Counter()
    for k in diag_all:
        md = int(k.split('_')[1])
        slots = set(wp7.mask_slots(md))
        zeros = [(i, j) for i in range(3) for j in range(3) if (i, j) not in slots]
        row_zero = any(all((i, j) not in slots for j in range(3)) for i in range(3))
        col_zero = any(all((i, j) not in slots for i in range(3)) for j in range(3))
        colcounts = Counter(j for (_, j) in zeros)
        ctype = tuple(sorted(colcounts.values(), reverse=True))
        obstr[(row_zero, col_zero, str(ctype))] += 1

    dphi_c = Counter(round(r['dphi'], 3) for r in rows)
    def fold_diff(a, b):
        return min(abs(a - b), abs(a + b - 90), abs(a - (90 - b)), abs(a - b - 90), abs(a + b))
    loop_check = max(fold_diff(r['phi1_loop'], r['phi1_stored']) for r in rows)
    loop_check2 = max(fold_diff(r['phi2_loop'], r['phi2_stored']) for r in rows)
    out = dict(
        purpose='WP24b exact sheet doubling certificates (35 stored diagonal pairs)',
        A_u_side_exact=dict(max_defect=max(r['u_defect'] for r in rows)),
        B_hd_magnitudes=dict(
            max_magnitude_defect=max(r['hd_mag_defect'] for r in rows),
            max_triangle_phase_defect_rad=max(r['hd_triangle_phase_defect'] for r in rows),
            max_dprime_residual=max(r['dprime_residual'] for r in rows),
            note='Hd2 = Dp P01 Hd1 P01 Dp^dag with Dp diagonal unitary; magnitudes conjugated exactly'),
        C_w_unitarity=dict(
            max_defect_all35=max(r['w_unitarity_defect'] for r in rows),
            note='W = (Dp P01 Yd1)^-1 Yd2; given Hd2 = Dp P01 Hd1 P01 Dp^dag, WW^dag = I is an algebraic identity, so the residual measures the Dp-solve precision amplified by 1/yd^2'),
        C2_dprime_solve=dict(max_residual=max(r['dprime_residual'] for r in rows)),
        D_loop_phase=dict(
            max_loop_vs_stored_deg=[loop_check, loop_check2],
            dphi_census={str(k): v for k, v in dphi_c.items()}),
        E_obstruction_census={str(k): v for k, v in obstr.items()},
        rows=rows)
    with open('results/wp24b_exact_sheet_doubling.json', 'w') as f:
        json.dump(out, f, indent=1)
    summ = {k: v for k, v in out.items() if k != 'rows'}
    print(json.dumps(summ, indent=1))

if __name__ == '__main__':
    main()
