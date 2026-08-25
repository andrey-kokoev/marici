"""Exact audit of boundary-jet annihilation by the aligned plus-chain tail."""
import json
import os
import sympy as sp

prefix_path = os.path.join(os.path.dirname(__file__), "magnetic_memory_one_checks.py")
namespace = {"__file__": prefix_path, "__name__": "magnetic_plus_boundary_prefix"}
with open(prefix_path, encoding="utf-8") as source_handle:
    prefix = source_handle.read().split("checks = []")[0]
exec(compile(prefix, prefix_path, "exec"), namespace)
component = namespace["component"]


def boundary_step(g, d):
    q = g + d
    columns = component(g, (q + q % 2) // 2, q)
    plus_columns = [0] + list(range(3, len(columns), 2))
    if d % 2 == 0:
        core_columns = [0, d + 1]
        boundary_rows = [1, 0]
    else:
        core_columns = [0, d, d + 2]
        boundary_rows = [1, 2, 0]
    tail_columns = [index for index in plus_columns if index not in core_columns]
    E = sp.Matrix([[columns[index].get(row, 0) for index in core_columns]
                   for row in boundary_rows])
    if not tail_columns:
        return E, E, sp.zeros(E.rows, E.cols), 0, 0, True, set(), set()

    available = sorted(set().union(*(set(columns[index]) for index in tail_columns)) -
                       set(boundary_rows))
    full_tail = sp.Matrix([[columns[index].get(row, 0)
                            for index in tail_columns] for row in available])
    pivots = full_tail.T.rref()[1]
    if len(pivots) != len(tail_columns):
        return None
    tail_rows = [available[index] for index in pivots]
    A = sp.Matrix([[columns[index].get(row, 0) for index in tail_columns]
                   for row in tail_rows])
    B = sp.Matrix([[columns[index].get(row, 0) for index in core_columns]
                   for row in tail_rows])
    C = sp.Matrix([[columns[index].get(row, 0) for index in tail_columns]
                   for row in boundary_rows])
    reconstruction = A.inv() * B
    correction = sp.simplify(C * reconstruction)
    S = sp.simplify(E - correction)
    reconstruction_support = {
        tail_columns[index] for index in range(len(tail_columns))
        if any(reconstruction[index, column] != 0
               for column in range(reconstruction.cols))
    }
    boundary_support = {
        tail_columns[index] for index in range(len(tail_columns))
        if any(C[row, index] != 0 for row in range(C.rows))
    }
    return (E, S, correction, sum(value != 0 for value in B),
            sum(value != 0 for value in C),
            all(B[row, 0] == 0 for row in range(B.rows)),
            reconstruction_support, boundary_support)


checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


failures = []
nontrivial = 0
minus_decoupling = True
support_separation = True
depth_bounds = True
records = []
for g in range(2, 17):
    for d in range(2, 25):
        result = boundary_step(g, d)
        if result is None:
            failures.append((g, d, "tail rank"))
            continue
        (E, S, correction, b_nonzero, c_nonzero, minus_zero,
         reconstruction_support, boundary_support) = result
        if correction != sp.zeros(*correction.shape) or S != E:
            failures.append((g, d, E.tolist(), S.tolist(), correction.tolist()))
        if b_nonzero and c_nonzero:
            nontrivial += 1
        minus_decoupling = minus_decoupling and minus_zero
        support_separation = (support_separation and
                              reconstruction_support.isdisjoint(boundary_support))
        # A plus column at list index a+1 has pole-depth label a.
        reconstruction_depths = {index - 1 for index in reconstruction_support}
        boundary_depths = {index - 1 for index in boundary_support}
        left_limit = d - 2 if d % 2 == 0 else d - 3
        right_limit = d + 2 if d % 2 == 0 else d + 3
        depth_bounds = (depth_bounds and
                        all(a <= left_limit for a in reconstruction_depths) and
                        all(a >= right_limit for a in boundary_depths))
        records.append((g, d, E.rows, b_nonzero, c_nonzero))

record("TAIL.rank", "every audited aligned plus tail has full column rank off boundary rows",
       not failures, f"blocks={len(records)}; failures={failures[:1]}")
record("JET.zero", "the reconstructed tail has identically zero boundary jet C*A^-1*B",
       not failures, "even rows=(1,0); odd rows=(1,2,0)")
record("SCHUR.literal", "the boundary Schur complement equals the raw local core E",
       not failures, "S=E, not merely det(S)=det(E)")
record("FALSIFIER.trivial", "the identity is not explained by B=0 or C=0",
       nontrivial > 0, f"blocks with both B and C nonzero={nontrivial}")
record("ENDPOINT.minus", "the (0,-) core column has zero interior reconstruction data",
       minus_decoupling,
       "its support is confined to reserved rows 0,1; only plus collision columns remain")
record("SUPPORT.disjoint", "reconstruction and boundary-visible tail columns are disjoint",
       support_separation, "support(A^-1*B) intersect support(C) is empty")
record("SUPPORT.bounds", "the two supports lie on opposite sides of the collision gap",
       depth_bounds,
       "left: a<=d-2/even or d-3/odd; right: a>=d+2/even or d+3/odd")

# Retain the two important zero fibers.
even_zero = boundary_step(4, 12)
odd_zero = boundary_step(2, 5)
record("FIBER.even", "the even chart divisor survives tail elimination unchanged",
       even_zero is not None and even_zero[1].det() == 0 and even_zero[1] == even_zero[0],
       "(g,d,q)=(4,12,16)")
record("FIBER.odd", "the genuine odd exception survives tail elimination unchanged",
       odd_zero is not None and odd_zero[1].det() == 0 and odd_zero[1] == odd_zero[0],
       "(g,d,q)=(2,5,7)")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_plus_boundary_compatibility_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "exact bounded boundary-compatibility theorem",
              "audit": "2<=g<=16 and 2<=d<=24"},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "After reserving the parity boundary rows and choosing the aligned full-rank tail observation chart, the plus-chain satisfies C A^-1 B=0 in every audited block. The reason is support separation in the triangular basis: reconstruction uses depths a<=d-2 (even) or a<=d-3 (odd), whereas boundary-visible tail columns begin at a>=d+2 or a>=d+3. Thus the Schur complement is literally the raw 2x2 or 3x3 collision matrix E. The (0,-) core column separately has B-data identically zero because it is supported only on rows 0,1.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_plus_boundary_compatibility.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
