"""Exhaustive nine-link support census (marici.Figueiredo).

Responds to marici.Nima (ev-000000000692): enumerate the full finite
set of 3x3 up/down support pairs with nine total links, full-rank
sectors, and a connected combined graph (hence b1 = 1 on nine nodes),
modulo the S3^3 = S_Q x S_u x S_d permutation group and sector
exchange.  For each orbit representative and each placement of the
single phase on an edge of the unique cycle:

  1. assign algebraically independent magnitudes (times eps powers =
     plain independent symbols here: identical vanishing of a_2 as a
     polynomial is unaffected by exponent bookkeeping);
  2. compute a_2 EXACTLY via the verified rank-one factorization
     (a2_factorization.py) -- no determinant needed;
  3. classify: NONZERO (purity fails) or zero by mechanism:
     telescoping (stripped phase-sector Gram diagonal),
     obstruction (both Ho sandwiches identically zero), or
     cancellation (nontrivial polynomial identity);

Decisive outcomes (Nima):
- every (orbit, phase placement) has a_2 = 0  => finite classification
  theorem, support => support {1}, admission hinge survives;
- one generic counterexample                     => the support route to
  admission is falsified; purity belongs to the coefficient layer.

All arithmetic exact (sympy symbolic).

Output: research/flavor/results/orbit_census.json
"""
import itertools
import json
import sympy as sp

SLOTS = [(i, j) for i in range(3) for j in range(3)]
SLOT_INDEX = {s: k for k, s in enumerate(SLOTS)}


def has_perfect_matching(mask):
    rows = [set() for _ in range(3)]
    for k in range(9):
        if mask >> k & 1:
            i, j = SLOTS[k]
            rows[i].add(j)
    for perm in itertools.permutations(range(3)):
        if all(perm[i] in rows[i] for i in range(3)):
            return True
    return False


def connected(mu, md):
    """9-node graph: Q nodes 0-2, u^c 3-5, d^c 6-8; edges Q_i--u^c_j /
    Q_i--d^c_j.  Union-find connectivity."""
    parent = list(range(9))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        parent[find(a)] = find(b)

    for k in range(9):
        i, j = SLOTS[k]
        if mu >> k & 1:
            union(i, 3 + j)
        if md >> k & 1:
            union(i, 6 + j)
    return len({find(n) for n in range(9)}) == 1


def unique_cycle(mu, md):
    """Return the edge list of the unique cycle of the connected
    nine-node nine-edge graph, as ('u'/'d', i, j) triples."""
    edges = []
    adj = {n: [] for n in range(9)}
    for k in range(9):
        i, j = SLOTS[k]
        if mu >> k & 1:
            edges.append(("u", i, j))
            adj[i].append((3 + j, len(edges) - 1))
            adj[3 + j].append((i, len(edges) - 1))
        if md >> k & 1:
            edges.append(("d", i, j))
            adj[i].append((6 + j, len(edges) - 1))
            adj[6 + j].append((i, len(edges) - 1))
    # find the cycle by iterative leaf removal
    deg = {n: len(adj[n]) for n in range(9)}
    alive = [True] * 9
    stack = [n for n in range(9) if deg[n] == 1]
    removed_edges = set()
    while stack:
        n = stack.pop()
        if not alive[n]:
            continue
        alive[n] = False
        for m, eidx in adj[n]:
            if eidx in removed_edges or not alive[m]:
                continue
            removed_edges.add(eidx)
            deg[m] -= 1
            if deg[m] == 1:
                stack.append(m)
    return [edges[e] for e in range(len(edges)) if e not in removed_edges]


def permute(mu, md, pq, pu, pd):
    """Apply row perm pq (shared Q) and column perms pu, pd."""
    nmu = nmd = 0
    for k in range(9):
        i, j = SLOTS[k]
        if mu >> k & 1:
            nmu |= 1 << SLOT_INDEX[(pq[i], pu[j])]
        if md >> k & 1:
            nmd |= 1 << SLOT_INDEX[(pq[i], pd[j])]
    return nmu, nmd


def canonical(mu, md):
    """Orbit canonical form under S3^3 and sector exchange."""
    best = None
    for pq in itertools.permutations(range(3)):
        for pu in itertools.permutations(range(3)):
            for pd in itertools.permutations(range(3)):
                a, b = permute(mu, md, pq, pu, pd)
                for x, y in ((a, b), (b, a)):
                    if best is None or (x, y) < best:
                        best = (x, y)
    return best


def enumerate_orbits():
    perms = [p for p in itertools.permutations(range(3))]
    seen = {}
    masks = [m for m in range(512) if has_perfect_matching(m)]
    for mu in masks:
        for md in masks:
            if bin(mu).count("1") + bin(md).count("1") != 9:
                continue
            if not connected(mu, md):
                continue
            best = None
            for pq in perms:
                for pu in perms:
                    for pd in perms:
                        a, b = permute(mu, md, pq, pu, pd)
                        for x, y in ((a, b), (b, a)):
                            if best is None or (x, y) < best:
                                best = (x, y)
            seen.setdefault(best, (mu, md))
    return list(seen.values())


def classify(mu, md):
    """For one orbit representative: per phase placement on the unique
    cycle, exact a_2 status and mechanism."""
    cycle = unique_cycle(mu, md)
    rows = []
    for sec, p, q in cycle:
        names = {}
        Yu = sp.Matrix.zeros(3)
        Yd = sp.Matrix.zeros(3)
        for k in range(9):
            i, j = SLOTS[k]
            if mu >> k & 1:
                Yu[i, j] = sp.symbols(f"u{i}{j}", positive=True)
            if md >> k & 1:
                Yd[i, j] = sp.symbols(f"d{i}{j}", positive=True)
        src = Yu if sec == "u" else Yd
        b = src[p, q]
        Y0 = src.copy()
        Y0[p, q] = 0
        Yu0, Yd0 = (Y0, Yd) if sec == "u" else (Yu, Y0)
        Hu0, Hd0 = Yu0 * Yu0.H, Yd0 * Yd0.H
        Ho = Hd0 if sec == "u" else Hu0
        C0 = Hu0 * Hd0 - Hd0 * Hu0
        u = sp.Matrix.zeros(3, 1)
        u[p] = 1
        v = b * Y0[:, q]
        vd = v.H
        s1 = sp.expand((vd * Ho * u)[0])
        s2 = sp.expand((vd * Ho * Ho * u)[0])
        s3 = sp.expand((vd * C0 * u)[0])
        s4 = sp.expand((vd * (C0 * Ho + Ho * C0) * u)[0])
        a2 = sp.expand(s1 * s4 - s2 * s3)
        Hs = Y0 * Y0.H
        diagonal = all(sp.simplify(Hs[i, j]) == 0
                       for i in range(3) for j in range(3) if i < j)
        if a2 != 0:
            mech = "nonzero"
        elif diagonal:
            mech = "telescoping"
        elif s1 == 0 and s2 == 0:
            mech = "obstruction"
        else:
            mech = "cancellation"
        rows.append({"phase_edge": [sec, p + 1, q + 1],
                     "a2_zero": a2 == 0,
                     "mechanism": mech,
                     "n_a2_monomials": 0 if a2 == 0 else
                     len(sp.Add.make_args(a2))})
        print("   ", sec, p + 1, q + 1, rows[-1]["mechanism"], flush=True)
    return {"cycle_length": len(cycle), "placements": rows}


def main():
    orbits = enumerate_orbits()
    print("orbit count:", len(orbits), flush=True)
    out = {"purpose": "exhaustive nine-link b1=1 support census: is "
                      "a_2 = 0 forced by support alone? "
                      "(ev-000000000692)",
           "orbit_count": len(orbits), "orbits": []}
    n_bad = 0
    for idx, (mu, md) in enumerate(orbits):
        print(f"orbit {idx}: u={mu:09b} d={md:09b}", flush=True)
        rep = classify(mu, md)
        rep["orbit_index"] = idx
        rep["mask_u"] = mu
        rep["mask_d"] = md
        out["orbits"].append(rep)
        bad = [r for r in rep["placements"] if not r["a2_zero"]]
        n_bad += len(bad)
    out["placements_with_nonzero_a2"] = n_bad
    out["support_forces_purity"] = n_bad == 0
    with open("results/orbit_census.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print("nonzero placements:", n_bad,
          "| support forces purity:", n_bad == 0)


if __name__ == "__main__":
    main()
