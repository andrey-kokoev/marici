"""Exact checker for nine-link flavor textures (marici.Figueiredo).

Source: arXiv:2607.27315v1 (Arkani-Hamed, Figueiredo, Hall, Manzari).
Conventions: research/flavor/flavor-nine-link-conventions.md.

All arithmetic is exact (sympy symbolic or exact rationals). No floating
point is used anywhere in the checks.

Layers:
  A. Graph audit: V, E, components, cyclomatic number b1 = E - V + c,
     unique-cycle extraction, for all four source textures (Eqs. S38, S43,
     S48, S53) plus exceptional/disconnected synthetic cases.
  B. Perfect matchings: enumerate bipartite perfect matchings per sector,
     verify their signed sum equals the determinant exactly; locate the
     phase edge relative to every matching.
  C. Rephasing invariance: prove the loop monomial is invariant under the
     full diagonal torus action (symbolic node factors), i.e. chart-level
     rephasing invariance.
  D. Weak-basis invariants: char polys of Hu = Yu Yu^dag, Hd = Yd Yd^dagger,
     mixed traces, commutator determinant; verify EXACT invariance under an
     exact rational U(3)_Q rotation while the zero pattern is destroyed and
     the loop monomial phase changes (arg M = pi/2 -> arg M' != pi/2).
  E. Leading-order mass spectrum of Example I checked against Eq. S41.

Outputs: research/flavor/results/nine_link_exact_checks.json
"""
import json
import itertools
import sympy as sp
from sympy.combinatorics import Permutation

I = sp.I
eps = sp.symbols("epsilon", positive=True, real=True)

# ---------------------------------------------------------------- textures
def sym(name):
    return sp.symbols(name, positive=True, real=True)

def build_textures():
    u12, u21, u22, u33 = sym("u12"), sym("u21"), sym("u22"), sym("u33")
    d12, d21, d22, d23, d33 = sym("d12"), sym("d21"), sym("d22"), sym("d23"), sym("d33")
    u11, u13, u23 = sym("u11"), sym("u13"), sym("u23")
    d11, d13, d31, d32 = sym("d11"), sym("d13"), sym("d31"), sym("d32")
    phi2 = -sp.pi / 8       # Example II placed phase (S43)
    phi3 = 5 * sp.pi / 8    # Example III placed phase (S48)
    Z = sp.Matrix.zeros(3)

    Yu1 = Z[:, :]; Yd1 = Z[:, :]
    Yu1[0, 1] = I * u12 * eps**4; Yu1[1, 0] = u21 * eps**5
    Yu1[1, 1] = u22 * eps**3;     Yu1[2, 2] = u33
    Yd1[0, 1] = d12 * eps**5;     Yd1[1, 0] = d21 * eps**5
    Yd1[1, 1] = d22 * eps**4;     Yd1[1, 2] = d23 * eps**3
    Yd1[2, 2] = d33 * eps**2

    Yu2 = Z[:, :]; Yd2 = Z[:, :]
    Yu2[0, 0] = u11 * eps**5; Yu2[0, 2] = u13 * eps**2
    Yu2[1, 1] = u22 * eps**2; Yu2[2, 2] = u33
    Yd2[0, 0] = d11 * eps**5; Yd2[0, 2] = d13 * eps**4
    Yd2[1, 2] = d23 * eps**3; Yd2[2, 1] = d32 * eps**2
    Yd2[2, 2] = sp.exp(I * phi2) * d33 * eps**2

    Yu3 = Z[:, :]; Yd3 = Z[:, :]
    Yu3[0, 0] = u11 * eps**5; Yu3[1, 1] = u22 * eps**2
    Yu3[1, 2] = u23 * eps;    Yu3[2, 2] = u33
    Yd3[0, 1] = sp.exp(I * phi3) * d12 * eps**4; Yd3[0, 2] = d13 * eps**4
    Yd3[1, 1] = d22 * eps**3
    Yd3[2, 0] = d31 * eps**3; Yd3[2, 2] = d33 * eps**2

    Yu4 = Z[:, :]; Yd4 = Z[:, :]
    Yu4[0, 0] = u11 * eps**6; Yu4[1, 1] = u22 * eps**3
    Yu4[1, 2] = u23 * eps**2; Yu4[2, 2] = u33
    Yd4[0, 2] = d13 * eps**5; Yd4[1, 0] = d21 * eps**5
    Yd4[1, 1] = sp.exp(I * sp.pi / 4) * d22 * eps**4
    Yd4[2, 1] = d32 * eps**2; Yd4[2, 2] = d33 * eps**2

    return {
        "example_I_S38": {"Yu": Yu1, "Yd": Yd1, "placed_phase": sp.pi / 2,
                          "phase_edge": ("u", 1, 2)},
        "example_II_S43": {"Yu": Yu2, "Yd": Yd2, "placed_phase": phi2,
                           "phase_edge": ("d", 3, 3)},
        "example_III_S48": {"Yu": Yu3, "Yd": Yd3, "placed_phase": phi3,
                            "phase_edge": ("d", 1, 2)},
        "pi_over_4_S53": {"Yu": Yu4, "Yd": Yd4, "placed_phase": sp.pi / 4,
                          "phase_edge": ("d", 2, 2)},
    }

# ---------------------------------------------------------------- graph
def graph_of(Yu, Yd):
    """Undirected link graph: nodes q1..q3, uc1..3, dc1..3."""
    edges = []  # (node_a, node_b, sector, i, j) 1-based i,j
    for sec, Y in (("u", Yu), ("d", Yd)):
        for i in range(3):
            for j in range(3):
                if Y[i, j] != 0:
                    a = ("q", i + 1)
                    b = (("uc" if sec == "u" else "dc"), j + 1)
                    edges.append((a, b, sec, i + 1, j + 1))
    nodes = set()
    for a, b, *_ in edges:
        nodes.add(a); nodes.add(b)
    return nodes, edges

def components(nodes, edges):
    adj = {n: set() for n in nodes}
    for a, b, *_ in edges:
        adj[a].add(b); adj[b].add(a)
    seen, comps = set(), []
    for n in nodes:
        if n in seen:
            continue
        stack, comp = [n], []
        while stack:
            x = stack.pop()
            if x in seen:
                continue
            seen.add(x); comp.append(x)
            stack.extend(adj[x] - seen)
        comps.append(comp)
    return comps

def find_cycle(nodes, edges):
    """Return one independent cycle as a list of edge indices, or None."""
    adj = {n: [] for n in nodes}
    for k, (a, b, *_rest) in enumerate(edges):
        adj[a].append((b, k)); adj[b].append((a, k))
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {n: WHITE for n in nodes}
    parent = {}
    cyc = []
    def dfs(u, pe):
        color[u] = GRAY
        for v, k in adj[u]:
            if k == pe:
                continue
            if color[v] == GRAY:
                path = [k]; x = u
                while x != v:
                    pk = parent[x]
                    path.append(pk[1]); x = pk[0]
                cyc.extend(path)
                return True
            if color[v] == WHITE:
                parent[v] = (u, k)
                if dfs(v, k):
                    return True
        color[u] = BLACK
        return False
    for n in nodes:
        if color[n] == WHITE and dfs(n, None):
            return cyc
    return None

def loop_monomial(cycle_edges, Yu, Yd):
    """Monomial per App. V.a: traverse the cycle; an entry is conjugated if
    traversed towards its q node. Returns (sympy expr, ordered entries)."""
    # reconstruct the cyclic node order
    adj = {}
    for a, b, sec, i, j in cycle_edges:
        adj.setdefault(a, []).append((b, (a, b, sec, i, j)))
        adj.setdefault(b, []).append((a, (a, b, sec, i, j)))
    start = cycle_edges[0][0]
    seq, prev, cur = [], None, start
    while True:
        nxt = [(w, e) for w, e in adj[cur] if w != prev]
        if not nxt:
            break
        w, e = nxt[0]
        seq.append((cur, w, e))
        prev, cur = cur, w
        if cur == start:
            break
    M = 1
    entries = []
    for frm, to, (a, b, sec, i, j) in seq:
        Y = Yu if sec == "u" else Yd
        entry = Y[i - 1, j - 1]
        conj = (to[0] == "q")   # arrow points towards a q node
        M = M * (sp.conjugate(entry) if conj else entry)
        entries.append({"sector": sec, "i": i, "j": j, "conjugated": conj})
    return sp.simplify(sp.expand(M)), entries

# ---------------------------------------------------------------- matchings
def perfect_matchings(Y):
    """All perfect matchings of the bipartite graph of Y with their terms."""
    out = []
    for sigma in itertools.permutations(range(3)):
        if all(Y[i, sigma[i]] != 0 for i in range(3)):
            term = Permutation(sigma).signature() * sp.prod(Y[i, sigma[i]] for i in range(3))
            out.append({"permutation": [s + 1 for s in sigma], "term": sp.simplify(term)})
    return out

def phase_ratio(M):
    """Return M/conj(M) simplified: e^{2 i arg M} for nonzero M."""
    return sp.simplify(sp.expand(M) / sp.conjugate(sp.expand(M)))

# ---------------------------------------------------------------- checks

def check_graph(name, Yu, Yd, placed_phase=None):
    nodes, edges = graph_of(Yu, Yd)
    comps = components(nodes, edges)
    b1 = len(edges) - len(nodes) + len(comps)
    cyc_idx = find_cycle(nodes, edges)
    info = {"V": len(nodes), "E": len(edges), "n_components": len(comps),
            "cycle_rank_b1": b1}
    if cyc_idx:
        cyc = [edges[k] for k in cyc_idx]
        M, entries = loop_monomial(cyc, Yu, Yd)
        info["unique_cycle_len"] = len(cyc)
        info["loop_entries"] = entries
        info["loop_monomial"] = str(M)
        r = phase_ratio(M)
        info["loop_monomial_over_conjugate"] = str(r)
        if placed_phase is not None:
            # exact assertion: arg M == placed phase, up to the loop-orientation
            # conjugation ambiguity acknowledged by the source
            rr = sp.expand_complex(r.rewrite(sp.exp))
            t_plus = sp.expand_complex(sp.exp(2 * I * placed_phase))
            t_minus = sp.expand_complex(sp.exp(-2 * I * placed_phase))
            info["loop_phase_matches_placed_up_to_conjugation"] = bool(
                sp.simplify(rr - t_plus) == 0 or sp.simplify(rr - t_minus) == 0)
        info["loop_sectors"] = sorted({e[2] for e in cyc})
    return info

def check_matchings(name, Yu, Yd, phase_edge):
    out = {}
    for sec, Y in (("u", Yu), ("d", Yd)):
        ms = perfect_matchings(Y)
        s = sp.simplify(sum(m["term"] for m in ms) - Y.det())
        out[sec] = {"n_matchings": len(ms),
                    "matchings": [[m["permutation"], str(m["term"])] for m in ms],
                    "signed_sum_minus_det": str(s),
                    "matching_sum_equals_det": s == 0}
    pe = phase_edge
    out["phase_edge"] = list(pe)
    in_matching = []
    for sec, Y in (("u", Yu), ("d", Yd)):
        for m in perfect_matchings(Y):
            for i in range(3):
                if (sec, i + 1, m["permutation"][i]) == pe:
                    in_matching.append((sec, m["permutation"]))
    out["phase_edge_in_any_matching"] = bool(in_matching)
    detu, detd = sp.simplify(Yu.det()), sp.simplify(Yd.det())
    out["det_Yu"] = str(detu)
    out["det_Yd"] = str(detd)
    r = sp.simplify(sp.expand(detu * detd) / sp.conjugate(sp.expand(detu * detd)))
    out["detYuYd_over_conjugate"] = str(r)  # e^{2 i arg det}
    return out

def check_rephasing():
    """Symbolic proof: the loop monomial is invariant under the full
    diagonal rephasing torus U(1)^9. Method: each node carries a formal
    Laurent factor; an un-conjugated Yu_ij contributes a_i b_j^-1, a
    conjugated one a_i^-1 b_j (since conj(x)=x^-1 for phases); the total
    rephasing factor of the loop monomial is the product, and invariance is
    the vanishing of every exponent vector."""
    a = sp.symbols("a1:4")   # q node factors
    b = sp.symbols("b1:4")   # uc node factors
    c = sp.symbols("c1:4")   # dc node factors
    syms = list(a) + list(b) + list(c)

    # Example I loop (from the JSON): Yu12, conj(Yu22), Yd22, conj(Yd12)
    loop = [("u", 1, 2, False), ("u", 2, 2, True),
            ("d", 2, 2, False), ("d", 1, 2, True)]
    F = 1
    for sec, i, j, conj in loop:
        row_f, col_f = a[i - 1], (b if sec == "u" else c)[j - 1]
        F *= (row_f**-1 * col_f) if conj else (row_f * col_f**-1)
    F = sp.expand(F)
    exps = F.as_powers_dict()  # single Laurent monomial -> {symbol: exponent}
    invariant = all(exps.get(s, 0) == 0 for s in syms)

    # Same audit for every texture's auto-detected loop.
    per_texture = {}
    for name, T in build_textures().items():
        nodes, edges = graph_of(T["Yu"], T["Yd"])
        cyc = [edges[k] for k in find_cycle(nodes, edges)]
        F = 1
        # reuse loop_monomial's orientation logic on factors:
        adj = {}
        for e0 in cyc:
            a0, b0, sec, i, j = e0
            adj.setdefault(a0, []).append((b0, e0))
            adj.setdefault(b0, []).append((a0, e0))
        start = cyc[0][0]
        seq, prev, cur = [], None, start
        while True:
            nxt = [(w, e0) for w, e0 in adj[cur] if w != prev]
            if not nxt:
                break
            w, e0 = nxt[0]
            seq.append((cur, w, e0))
            prev, cur = cur, w
            if cur == start:
                break
        for frm, to, (a0, b0, sec, i, j) in seq:
            conj = (to[0] == "q")
            row_f, col_f = a[i - 1], (b if sec == "u" else c)[j - 1]
            F *= (row_f**-1 * col_f) if conj else (row_f * col_f**-1)
        exps = sp.expand(F).as_powers_dict()
        per_texture[name] = all(exps.get(s, 0) == 0 for s in syms)
    return {"method": "Laurent exponent-vector audit of the loop rephasing factor",
            "example_I_loop_invariant": invariant,
            "all_textures_loop_invariant": per_texture}

def check_rotation():
    """Exact rational U(3)_Q rotation: invariants unchanged, chart destroyed."""
    T = build_textures()["example_I_S38"]
    Yu, Yd = T["Yu"], T["Yd"]
    c, s = sp.Rational(3, 5), sp.Rational(4, 5)
    R = sp.Matrix([[c, s, 0], [-s, c, 0], [0, 0, 1]])
    assert sp.simplify(R * R.T - sp.eye(3)) == sp.zeros(3)
    YuR, YdR = R * Yu, R * Yd

    def nz(Y):
        return sum(1 for i in range(3) for j in range(3) if Y[i, j] != 0)

    Hu, Hd = Yu * Yu.H, Yd * Yd.H
    HuR, HdR = YuR * YuR.H, YdR * YdR.H
    inv_pairs = {
        "tr_Hu": (sp.trace(Hu), sp.trace(HuR)),
        "tr_Hu2": (sp.trace(Hu**2), sp.trace(HuR**2)),
        "det_Hu": (Hu.det(), HuR.det()),
        "tr_Hd": (sp.trace(Hd), sp.trace(HdR)),
        "tr_Hd2": (sp.trace(Hd**2), sp.trace(HdR**2)),
        "det_Hd": (Hd.det(), HdR.det()),
    }
    sym_inv_ok = {}
    for k, (x, y) in inv_pairs.items():
        sym_inv_ok[k] = sp.simplify(sp.expand(x) - sp.expand(y)) == 0

    # concrete exact-rational evaluation for the heavier invariants
    sub = {eps: sp.Rational(1, 10)}
    for s_ in Yu.free_symbols | Yd.free_symbols:
        if s_ != eps:
            sub[s_] = sp.Rational(1)
    sub[sym("u21")] = sp.Rational(2)
    sub[sym("d22")] = sp.Rational(2)
    HuC = sp.Matrix(Hu.subs(sub)); HdC = sp.Matrix(Hd.subs(sub))
    HuRC = sp.Matrix(HuR.subs(sub)); HdRC = sp.Matrix(HdR.subs(sub))
    def mixed(Hu, Hd):
        com = Hu * Hd - Hd * Hu
        return {
            "tr_HuHd": sp.trace(Hu * Hd),
            "tr_Hu2Hd": sp.trace(Hu**2 * Hd),
            "tr_HuHd2": sp.trace(Hu * Hd**2),
            "tr_Hu2Hd2": sp.trace(Hu**2 * Hd**2),
            "det_commutator": sp.simplify(com.det()),
        }
    m0, m1 = mixed(HuC, HdC), mixed(HuRC, HdRC)
    concrete_ok = {k: sp.simplify(m0[k] - m1[k]) == 0 for k in m0}

    # loop monomial before/after (same edge set)
    def M(Yu, Yd):
        return sp.expand(Yu[0, 1] * sp.conjugate(Yu[1, 1])
                         * Yd[1, 1] * sp.conjugate(Yd[0, 1]))
    M0 = M(Yu, Yd)
    M1 = M(YuR, YdR)
    re1, im1 = sp.expand(M1).as_real_imag()
    re0, im0 = sp.expand(M0).as_real_imag()
    return {
        "rotation": "U(3)_Q rotation in q1-q2 plane, cos=3/5, sin=4/5 (exact rational, unitary)",
        "nonzeros_before": {"u": nz(Yu), "d": nz(Yd)},
        "nonzeros_after": {"u": nz(YuR), "d": nz(YdR)},
        "zero_pattern_destroyed": nz(YuR) + nz(YdR) > nz(Yu) + nz(Yd),
        "symbolic_invariants_equal": sym_inv_ok,
        "concrete_invariants_equal": concrete_ok,
        "det_commutator_concrete_before": str(m0["det_commutator"]),
        "monomial_before": str(M0),
        "monomial_before_arg_is_pi_over_2": sp.simplify(re0) == 0 and sp.simplify(im0) != 0,
        "monomial_after": str(M1),
        "monomial_after_real_part": str(re1),
        "monomial_after_real_part_zero": sp.simplify(re1) == 0,
        "phase_changed_under_rotation": sp.simplify(re1) != 0,
    }

def check_example1_spectrum():
    """Leading eigenvalue structure of Example I vs Eq. S41."""
    T = build_textures()["example_I_S38"]
    Yu, Yd = T["Yu"], T["Yd"]
    Hu, Hd = Yu * Yu.H, Yd * Yd.H
    u12, u21, u22, u33 = sym("u12"), sym("u21"), sym("u22"), sym("u33")
    d22, d33 = sym("d22"), sym("d33")
    def invariants(H):
        e1 = sp.trace(H)
        e2 = sum(H.extract([i, j], [i, j]).det() for i, j in
                 [(0, 1), (0, 2), (1, 2)])
        e3 = H.det()
        return sp.expand(e1), sp.expand(e2), sp.expand(e3)
    e1u, e2u, e3u = invariants(Hu)
    e1d, e2d, e3d = invariants(Hd)
    d12, d21 = sym("d12"), sym("d21")
    # S41 leading structure:
    #   up:   e1 ~ u33^2, e2 ~ u33^2 u22^2 eps^6, e3 = u12^2 u21^2 u33^2 eps^18
    #   down: e1 ~ d33^2 eps^4, e2 ~ d22^2 d33^2 eps^12, e3 = d12^2 d21^2 d33^2 eps^24
    # (e3d: unique Yd matching {(1,2),(2,1),(3,3)} gives det Yd ~ eps^12.)
    e1u_l = sp.series(e1u, eps, 0, 1).removeO()
    e2u_l = sp.series(e2u, eps, 0, 7).removeO()
    e1d_l = sp.series(e1d, eps, 0, 5).removeO()
    e2d_l = sp.series(e2d, eps, 0, 13).removeO()
    checks = {
        "e1u_leading": str(e1u_l),
        "e2u_leading": str(e2u_l),
        "e3u_exact": str(e3u),
        "e1d_leading": str(e1d_l),
        "e2d_leading": str(e2d_l),
        "e3d_exact": str(e3d),
        "S41_up_spectrum_matches": (
            e1u_l == u33**2 and
            e2u_l == u33**2 * u22**2 * eps**6 and
            sp.simplify(e3u - u12**2 * u21**2 * u33**2 * eps**18) == 0),
        "S41_down_spectrum_matches": (
            e1d_l == d33**2 * eps**4 and
            e2d_l == d22**2 * d33**2 * eps**12 and
            sp.simplify(e3d - d12**2 * d21**2 * d33**2 * eps**24) == 0),
    }
    return checks

def check_permutation_transport():
    """Sparse-groupoid transport test (WP3, positive direction).

    Apply a non-trivial S3^3 element to Example I: rows (q side) cycled
    1->2->3->1, up columns swapped 1<->3, down columns swapped 2<->3.
    Verify the transported chart still has b1 = 1, its loop holonomy agrees
    with the original up to the orientation-conjugation ambiguity, and the
    determinant/matching data are preserved exactly (real sign factors only).
    """
    T = build_textures()["example_I_S38"]
    Yu, Yd = T["Yu"], T["Yd"]
    P = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])   # row cycle
    Qu = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])  # up col swap 1<->3
    Qd = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])  # down col swap 2<->3
    YuP, YdP = P * Yu * Qu, P * Yd * Qd

    g_old = check_graph("ex1", Yu, Yd, T["placed_phase"])
    g_new = check_graph("ex1_perm", YuP, YdP, T["placed_phase"])

    def M(Yu_, Yd_):
        return sp.expand(Yu_[0, 1] * sp.conjugate(Yu_[1, 1])
                         * Yd_[1, 1] * sp.conjugate(Yd_[0, 1]))
    M_old = M(Yu, Yd)

    # locate the transported loop's monomial directly from the new graph
    nodes, edges = graph_of(YuP, YdP)
    cyc = [edges[k] for k in find_cycle(nodes, edges)]
    M_new, _ = loop_monomial(cyc, YuP, YdP)
    r = sp.expand_complex(phase_ratio(M_new).rewrite(sp.exp))
    r0 = sp.expand_complex(phase_ratio(M_old).rewrite(sp.exp))

    detu, detd = Yu.det(), Yd.det()
    detuP, detdP = YuP.det(), YdP.det()
    sign_u = sp.simplify(detuP / detu)
    sign_d = sp.simplify(detdP / detd)
    return {
        "permutation": "rows cycled 1->2->3->1; up cols 1<->3; down cols 2<->3",
        "graph_after": {"V": g_new["V"], "E": g_new["E"],
                        "n_components": g_new["n_components"],
                        "cycle_rank_b1": g_new["cycle_rank_b1"],
                        "unique_cycle_len": g_new.get("unique_cycle_len")},
        "loop_holonomy_matches_up_to_conjugation":
            g_new["loop_phase_matches_placed_up_to_conjugation"],
        "holonomy_ratio_new_over_old": str(sp.simplify(r / r0)),
        "n_matchings_after": {"u": len(perfect_matchings(YuP)),
                              "d": len(perfect_matchings(YdP))},
        "det_ratio_u": str(sign_u),
        "det_ratio_d": str(sign_d),
        "det_ratios_real_signs": sign_u in (1, -1) and sign_d in (1, -1),
        "arg_det_product_preserved": sp.simplify(
            (detuP * detdP) / (detu * detd)) in (1, -1),
    }

def main():
    textures = build_textures()
    out = {"checks": {}}
    for name, T in textures.items():
        Yu, Yd = T["Yu"], T["Yd"]
        entry = {"graph": check_graph(name, Yu, Yd, T["placed_phase"]),
                 "matchings": check_matchings(name, Yu, Yd, T["phase_edge"]),
                 "placed_phase": str(T["placed_phase"])}
        out["checks"][name] = entry
    out["checks"]["rephasing_torus"] = check_rephasing()
    out["checks"]["u3q_rotation"] = check_rotation()
    out["checks"]["s3_cubed_permutation_transport"] = check_permutation_transport()
    out["checks"]["example1_spectrum_vs_S41"] = check_example1_spectrum()
    # exceptional audits: disconnected 9-node/9-edge graph and a 10-edge graph
    YuX = sp.diag(1, 1, 1); YdX = sp.diag(1, 1, 1)
    YuX[0, 1] = 1; YdX[0, 1] = 1; YdX[1, 0] = 1  # 9 edges, but is it one loop?
    nodes, edges = graph_of(YuX, YdX)
    comps = components(nodes, edges)
    out["checks"]["exceptional_diag_plus_extra"] = {
        "note": "Yu diag + Yu12; Yd diag + Yd12 + Yd21: E=9, V=9 but disconnected (c=2)",
        "V": len(nodes), "E": len(edges), "n_components": len(comps),
        "cycle_rank_b1": len(edges) - len(nodes) + len(comps),
        "comment": "b1 = E - V + c = 2, not 1: the single-holonomy slogan b1 = E - V + 1 = 1 presupposes connectedness. V and E alone do not certify the single-loop structure; the cycle audit must be run per component. Full-rank + 9 links + connected + single loop is the source definition; disconnected or multi-loop exceptional cases are audited separately, as here."}
    with open("results/nine_link_exact_checks.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=2)[:6000])

if __name__ == "__main__":
    main()
