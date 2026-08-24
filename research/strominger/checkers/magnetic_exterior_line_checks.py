"""Exact exterior-power invariant and Plucker-atlas checker."""
from itertools import combinations
import json
import os
import sympy as sp

prefix_path = os.path.join(os.path.dirname(__file__), "magnetic_memory_one_checks.py")
with open(prefix_path, encoding="utf-8") as source_handle:
    exec(source_handle.read().split("checks = []")[0])


def full_matrix(columns):
    rows = sorted(set().union(*(item.keys() for item in columns)))
    return rows, sp.Matrix([[item.get(row, 0) for item in columns] for row in rows])


def plucker_norm_squared(matrix):
    width = matrix.cols
    coordinates = []
    for selected in combinations(range(matrix.rows), width):
        coordinates.append(int(matrix[list(selected), :].det()))
    return sum(value * value for value in coordinates), coordinates


checks = []
def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


onsets = [(g, 2 * g + 8, g // 2 + 4) for g in range(2, 16, 2)]
onset_data = []
for g, q, k in onsets:
    columns = component(g, k, q)
    all_rows, matrix = full_matrix(columns)
    primary_rows = hall_rows(columns)
    alternate_rows = [3 if row == 1 else row for row in primary_rows]
    primary = int(sp.Matrix([[item.get(row, 0) for item in columns]
                             for row in primary_rows]).det())
    alternate = int(sp.Matrix([[item.get(row, 0) for item in columns]
                               for row in alternate_rows]).det())
    gram, norm, nonzero_coordinates, rank = None, None, None, None
    onset_data.append({"g": g, "q": q, "k": k, "rows": len(all_rows),
                       "rank": rank, "columns": matrix.cols,
                       "primary": primary, "alternate": alternate,
                       "nonzero_coordinates": nonzero_coordinates,
                       "norm": norm, "gram": gram})

# Verify the coordinate-free identity on a small regular component.  The
# identity itself is Cauchy-Binet; larger fibers use a single exact nonzero
# coordinate as the economical witness that the exterior section survives.
sample_rows, sample_matrix = full_matrix(component(3, 0, 2))
sample_norm, sample_coordinates = plucker_norm_squared(sample_matrix)
sample_gram = int((sample_matrix.T * sample_matrix).det())
record("WEDGE.cauchy_binet",
       "the Gram determinant equals the sum of squared Plucker coordinates",
       sample_gram == sample_norm and sample_gram > 0,
       f"rows={sample_rows}; coordinates={sample_coordinates}; norm={sample_norm}")
record("WEDGE.nonzero",
       "the exterior-power section is nonzero at every primary-chart boundary",
       all(item["alternate"] != 0 for item in onset_data),
       [(item["g"], item["q"], item["alternate"] != 0)
        for item in onset_data])
record("CHART.boundary",
       "the preferred coordinate vanishes while the adjacent coordinate survives",
       all(item["primary"] == 0 and item["alternate"] != 0
           for item in onset_data),
       f"confirmed={len(onset_data)}")
record("CHART.atlas",
       "one uniform adjacent chart witnesses the invariant section",
       all(item["alternate"] != 0 for item in onset_data),
       "row exchange 1->3 at all seven onsets")

# At the two genuine exceptional births the top column exterior power vanishes.
def defect_data(g, q, k):
    columns = component(g, k, q)
    _, matrix = full_matrix(columns)
    gram = int((matrix.T * matrix).det())
    return {"g": g, "q": q, "k": k, "rank": matrix.rank(),
            "columns": matrix.cols, "gram": gram,
            "nullity": matrix.cols - matrix.rank()}


defects = [defect_data(2, 1, 0), defect_data(2, 7, 3)]
record("WEDGE.defects",
       "the top exterior-power section vanishes at both genuine births",
       all(item["gram"] == 0 and item["nullity"] == 1 for item in defects),
       defects)

# Nearby regular fibers distinguish genuine zeros from an identically zero family.
neighbors = [defect_data(3, 1, 0), defect_data(3, 7, 3),
             defect_data(2, 6, 3), defect_data(2, 8, 3)]
record("WEDGE.transverse",
       "nearby grade or component fibers restore a nonzero exterior section",
       all(item["gram"] > 0 and item["nullity"] == 0 for item in neighbors),
       [(item["g"], item["q"], item["gram"] != 0) for item in neighbors])

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_exterior_line_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "exact finite exterior-power and chart-boundary theorem",
              "chart_onsets": onsets,
              "defect_fibers": [[2, 1, 0], [2, 7, 3]]},
    "checks": checks, "n_pass": len(checks) - len(failed), "n_fail": len(failed),
    "onset_data": onset_data, "defects": defects, "neighbors": neighbors,
    "verdict": "The invariant squared norm of the top exterior section is det(M^T M), equal by Cauchy-Binet to the sum of squares of all maximal minors. It remains strictly positive at every tested even primary-chart boundary although the preferred coordinate is zero. It vanishes with nullity one at the two genuine grade-two births. Thus chart failure and transport failure are exactly separated in the tested fibers."
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_exterior_line.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
