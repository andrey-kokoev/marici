"""Jacobian factorization for square monomial Gram maps.

For each oriented nine-link support with exactly nine phase-free Gram
coordinates (six diagonals plus three monomial off-diagonal magnitudes),
compute the exact 9x9 Jacobian. Test whether its only interior rank-drop
factor is the alternating product binomial of the unique graph cycle.
"""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
SLOTS = [(i, j) for i in range(3) for j in range(3)]


def slots(mask):
    return [s for k, s in enumerate(SLOTS) if mask & (1 << k)]


def cycle_order(mu, md):
    edges = []
    adj = {n: [] for n in range(9)}
    for sec, mask, offset in (("u", mu, 3), ("d", md, 6)):
        for i, j in slots(mask):
            idx = len(edges)
            edges.append((sec, i, j, i, offset+j))
            adj[i].append(idx)
            adj[offset+j].append(idx)
    alive = set(range(9))
    deg = {n: len(adj[n]) for n in adj}
    queue = [n for n in adj if deg[n] == 1]
    while queue:
        n = queue.pop()
        inc = [e for e in adj[n] if e in alive]
        if not inc:
            continue
        e = inc[0]
        alive.remove(e)
        a, b = edges[e][3:]
        m = b if n == a else a
        deg[m] -= 1
        if deg[m] == 1:
            queue.append(m)
    start = min(alive)
    order, edge, node = [], start, edges[start][3]
    while True:
        order.append(edge)
        a, b = edges[edge][3:]
        nxt_node = b if node == a else a
        nxt = [e for e in adj[nxt_node] if e in alive and e != edge][0]
        if nxt == start:
            break
        node, edge = nxt_node, nxt
    return order, edges


def gram_coordinates(mu, md, variables, edges):
    by_key = {(sec, i, j): variables[k]
              for k, (sec, i, j, _, _) in enumerate(edges)}
    coords = []
    for sec, mask in (("u", mu), ("d", md)):
        ss = slots(mask)
        for i in range(3):
            coords.append(sum(by_key[(sec, i, j)] for ii, j in ss if ii == i))
        for i in range(3):
            for j in range(i+1, 3):
                shared = [c for c in range(3)
                          if (i, c) in ss and (j, c) in ss]
                if len(shared) == 1:
                    c = shared[0]
                    coords.append(by_key[(sec, i, c)]*by_key[(sec, j, c)])
                elif len(shared) > 1:
                    raise ValueError("phase-sensitive support")
    return coords


inventory = json.loads(
    (RESULTS / "wp10_oriented_gram_map_inventory.json").read_text())
records = []
for row in inventory["rows"]:
    if row["requires_phase_in_gram_map"]:
        continue
    nonzero_pairs = (
        sum(c > 0 for c in row["up"]["row_pair_shared_column_counts"]) +
        sum(c > 0 for c in row["down"]["row_pair_shared_column_counts"])
    )
    if 6+nonzero_pairs != 9:
        continue
    mu, md = row["mask_u"], row["mask_d"]
    order, edges = cycle_order(mu, md)
    variables = sp.symbols("x0:9", positive=True)
    coords = gram_coordinates(mu, md, variables, edges)
    assert len(coords) == 9
    determinant = sp.factor(sp.Matrix(coords).jacobian(variables).det())
    even = sp.prod(variables[e] for e in order[::2])
    odd = sp.prod(variables[e] for e in order[1::2])
    balance = sp.expand(even-odd)
    quotient, remainder = sp.div(determinant, balance, *variables)
    quotient = sp.factor(quotient)
    divisible = sp.factor(remainder) == 0
    quotient_poly = quotient.as_poly(variables)
    quotient_is_monomial = bool(
        quotient_poly is not None and len(quotient_poly.monoms()) == 1)
    records.append({
        "orientation": row["orientation"], "orbit": row["orbit"],
        "signature_id": row["signature_id"],
        "masks": {"u": mu, "d": md},
        "cycle_length": len(order),
        "jacobian_determinant": str(determinant),
        "cycle_balance_binomial": str(balance),
        "coordinate_face_factor": str(quotient),
        "balance_divides_jacobian": divisible,
        "quotient_is_coordinate_monomial": quotient_is_monomial,
        "division_remainder": str(sp.factor(remainder)),
    })

overdetermined_records = []
for row in inventory["rows"]:
    if row["requires_phase_in_gram_map"]:
        continue
    nonzero_pairs = (
        sum(c > 0 for c in row["up"]["row_pair_shared_column_counts"]) +
        sum(c > 0 for c in row["down"]["row_pair_shared_column_counts"])
    )
    if 6+nonzero_pairs != 10:
        continue
    mu, md = row["mask_u"], row["mask_d"]
    order, edges = cycle_order(mu, md)
    variables = sp.symbols("x0:9", positive=True)
    coords = gram_coordinates(mu, md, variables, edges)
    jacobian = sp.Matrix(coords).jacobian(variables)
    minors = []
    for omitted_row in range(10):
        # Select all nine variable columns and all coordinate rows except
        # omitted_row.
        minor = sp.factor(jacobian.extract(
            [i for i in range(10) if i != omitted_row], range(9)).det())
        minors.append(minor)
    monomial_minor_indices = []
    for i, minor in enumerate(minors):
        poly = minor.as_poly(variables)
        if minor != 0 and poly is not None and len(poly.monoms()) == 1:
            monomial_minor_indices.append(i)
    overdetermined_records.append({
        "orientation": row["orientation"], "orbit": row["orbit"],
        "signature_id": row["signature_id"],
        "masks": {"u": mu, "d": md},
        "nonzero_maximal_minor_count": sum(m != 0 for m in minors),
        "coordinate_monomial_minor_indices": monomial_minor_indices,
        "positive_interior_full_rank_certified": bool(monomial_minor_indices),
        "maximal_minors": [str(m) for m in minors],
    })

out = {
    "schema": "marici.flavor.square_monomial_gram_jacobians.v1",
    "status": "complete_symbolic_factorization_census",
    "tested_class_count": len(records),
    "cycle_balance_factor_count":
        sum(r["balance_divides_jacobian"] for r in records),
    "pure_cycle_balance_wall_count":
        sum(r["balance_divides_jacobian"] and
            r["quotient_is_coordinate_monomial"] for r in records),
    "all_factor_as_coordinate_monomial_times_cycle_balance":
        all(r["balance_divides_jacobian"] and
            r["quotient_is_coordinate_monomial"] for r in records),
    "candidate_interior_rank_drop":
        "product(even cycle edge squares) = product(odd cycle edge squares), only where certified per record",
    "typing_scope":
        "oriented classes whose phase-free structural Gram coordinate map is square 9-to-9",
    "records": records,
    "overdetermined_phase_free_class_count": len(overdetermined_records),
    "overdetermined_positive_interior_full_rank_count":
        sum(r["positive_interior_full_rank_certified"]
            for r in overdetermined_records),
    "overdetermined_records": overdetermined_records,
}
(RESULTS / "wp10_square_monomial_gram_jacobians.json").write_text(
    json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps({k: v for k, v in out.items() if k != "records"}, indent=2))
