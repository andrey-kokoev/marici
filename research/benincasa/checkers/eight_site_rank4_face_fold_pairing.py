"""Exact source-face test for the C8 rank-four fold pairing.

The seven selected source facets cut out an eight-simplex face of the C8
cosmological polytope.  Its canonical form is reconstructed directly from
the certified source vertices.  For one source-labelled representative of
each reduced fold pattern, this checker restricts that form to the wall
solution and differentiates it along the exact corank-one kernel of the
companion map.  A nonzero odd derivative is the local source datum needed
for pairing with the rank-one A1 fold coefficient; no regulator chamber or
residue weight is selected.
"""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
CONTOUR = ROOT / "results" / "eight-site-canonical-contour-packet.json"
SOURCE = ROOT / "results" / "eight-site-rank4-labelled-expansion.json"
UNIVERSAL = ROOT / "results" / "eight-site-rank4-universal-jacobian.json"
REDUCED = ROOT / "results" / "eight-site-rank4-base-reduced-walls.json"
MODELS = ROOT / "results" / "eight-site-base-reduced-companion-models.json"
FOLDS = ROOT / "results" / "eight-site-companion-symbolic-fold.json"
TARGET = ROOT / "results" / "eight-site-rank4-face-fold-pairing.json"


def parse(expression: str, symbols: dict[str, sp.Symbol]) -> sp.Expr:
    return sp.expand(sp.sympify(expression, locals=symbols))


def first_independent_rows(matrix: sp.Matrix, target_rank: int) -> list[int]:
    rows: list[int] = []
    rank = 0
    for index in range(matrix.rows):
        trial = matrix[rows + [index], :]
        trial_rank = trial.rank()
        if trial_rank > rank:
            rows.append(index)
            rank = trial_rank
        if rank == target_rank:
            return rows
    raise AssertionError("matrix does not have requested row rank")


def primitive_kernel(vector: sp.Matrix) -> sp.Matrix:
    """Normalize a one-dimensional algebraic kernel by its first entry."""
    first = next(value for value in vector if value != 0)
    return sp.simplify(vector / first)


def model_pattern(name: str) -> str:
    if "family_A" in name:
        return "free:2,4,6,8;zero:3,5,7;survive:1"
    surviving = int(name.split("surviving_edge_")[1].split("_")[0])
    zeros = sorted(set((2, 4, 6, 8)) - {surviving})
    return f"free:1,3,5,7;zero:{','.join(map(str, zeros))};survive:{surviving}"


def fold_point(name: str, symbols: dict[str, sp.Symbol]) -> dict[sp.Symbol, sp.Expr]:
    a, b, c, d, z, k, ell = (symbols[key] for key in ("a", "b", "c", "d", "z", "k", "l"))
    if "family_A" in name:
        return {a: 1, b: 1, c: 1, d: 1, z: sp.sqrt(sp.Rational(32, 5)), k: 1, ell: 0}
    if "surviving_edge_4" in name:
        return {a: 1, b: 1, c: 1, d: 1, z: sp.sqrt(sp.Rational(19, 6)), k: 1, ell: 0}
    return {a: 1, b: sp.sqrt(sp.Rational(-9, 10)), c: 1, d: 1, z: 1, k: 1, ell: 0}


def solve_external(
    base: list[sp.Expr], beta: tuple[sp.Symbol, ...], survive_equation: sp.Expr, z: sp.Symbol,
    x: tuple[sp.Symbol, ...], face_coordinates: list[sp.Expr], fold_subs: dict[sp.Symbol, sp.Expr],
) -> tuple[dict[sp.Symbol, sp.Expr], dict[sp.Symbol, int]]:
    """Choose a source-independent affine chart with a nonboundary sample."""
    constants_packets = (
        (2, 3, 5, 7), (2, 4, 7, 11), (3, 5, 11, 13),
        (-2, 3, 5, 7), (2, -3, 5, 11),
    )
    solution_set = sp.linsolve([*[value - beta[index] for index, value in enumerate(base)], survive_equation - z], x)
    assert solution_set is not sp.EmptySet and len(solution_set) == 1
    solution_tuple = next(iter(solution_set))
    parameters = sorted(set().union(*(value.free_symbols for value in solution_tuple)) & set(x), key=str)
    assert len(parameters) == 4
    for constants in constants_packets:
            parameter_values = dict(zip(parameters, constants))
            solution = dict(zip(x, [sp.expand(value.subs(parameter_values)) for value in solution_tuple]))
            sample = [sp.simplify(value.subs(solution).subs(fold_subs).subs(dict(zip(beta, (2, 3, 5))))) for value in face_coordinates]
            if all(value != 0 for value in sample):
                return solution, parameter_values
    raise AssertionError("no nonboundary affine source chart found")


def main() -> None:
    contour = json.loads(CONTOUR.read_text())
    source = json.loads(SOURCE.read_text())
    universal = json.loads(UNIVERSAL.read_text())
    reduced = json.loads(REDUCED.read_text())
    models = json.loads(MODELS.read_text())
    folds = json.loads(FOLDS.read_text())

    x = sp.symbols("X1:9")
    y = sp.symbols("y1:9")
    a, b, c, d, z, k, ell = sp.symbols("a b c d z k l")
    beta = sp.symbols("B1:4")
    t = sp.symbols("t0:8")
    all_symbols = {str(value): value for value in (*x, *y, a, b, c, d, z, k, ell, *beta, *t)}
    vertices = sp.Matrix.hstack(*(sp.Matrix(item["column"]) for item in contour["vertices"]))
    facets = {item["label"]: item for item in contour["facets"]}
    universal_by_key = {item["canonical_key"]: item for item in universal["classes"]}
    occurrence_by_key = {}
    for occurrence in source["occurrences"]:
        occurrence_by_key.setdefault(occurrence["source_orbit_key"], occurrence)
    model_by_pattern = {model_pattern(model["name"]): model for model in models["models"]}
    fold_by_model = {item["model"]: item for item in folds["models"]}
    model_geometry = {}
    for model in models["models"]:
        cover = sp.Matrix([parse(expression, all_symbols) for expression in model["cover_equations"]])
        jacobian = cover.jacobian((a, b, c, d))
        determinant_factors = sp.factor_list(jacobian.det())[1]
        fold_candidates = [
            factor for factor, _multiplicity in determinant_factors
            if len(factor.free_symbols & {a, b, c, z}) >= 2
        ]
        assert len(fold_candidates) == 1
        adjugate_column = int(fold_by_model[model["name"]]["adjugate_column"])
        cofactor_row = [
            (-1) ** (adjugate_column + column) * jacobian.minor_submatrix(adjugate_column, column).det()
            for column in range(4)
        ]
        model_geometry[model["name"]] = (
            jacobian,
            sp.factor(fold_candidates[0]),
            adjugate_column,
            cofactor_row,
        )

    audits = []
    for reduced_record in reduced["records"]:
        pattern = reduced_record["reduced_pattern"]
        model = model_by_pattern[pattern]
        key = reduced_record["canonical_key"]
        occurrence = occurrence_by_key[key]
        record = universal_by_key[key]
        labels = occurrence["labels"]

        face_vertices = sorted(set.intersection(*(set(facets[label]["zero_vertex_indices"]) for label in labels)))
        assert len(face_vertices) == 9
        face_vertex_matrix = vertices[:, face_vertices]
        assert face_vertex_matrix.rank() == 9
        coordinate_rows = first_independent_rows(face_vertex_matrix, 9)
        simplex_matrix = face_vertex_matrix[coordinate_rows, :]
        determinant = sp.Integer(simplex_matrix.det())
        assert determinant != 0

        ambient = sp.Matrix([*x, *y])
        barycentric = list(simplex_matrix.inv() * ambient[coordinate_rows, :])
        face_form = sp.factor(1 / (abs(determinant) * sp.prod(barycentric)))

        wall_solution = [parse(expression, all_symbols) for expression in record["wall_solution"]]
        free_edges = record["free_signed_energy_indices"]
        for variable, edge in zip((a, b, c, d), free_edges):
            wall_solution[edge - 1] = variable
        base = [parse(expression, all_symbols) for expression in record["base_relations"]]
        survive = int(pattern.split("survive:")[1])
        fold_subs = fold_point(model["name"], all_symbols)

        restricted_barycentric = [sp.factor(value.subs(dict(zip(y, wall_solution)))) for value in barycentric]
        external_solution, parameter_values = solve_external(
            base, beta, wall_solution[survive - 1], z, x, restricted_barycentric, fold_subs
        )
        restricted_factors = [sp.factor(value.subs(external_solution)) for value in restricted_barycentric]
        restricted_form = 1 / (abs(determinant) * sp.prod(restricted_factors))

        jacobian, fold_divisor, adjugate_column, cofactor_row = model_geometry[model["name"]]
        jacobian_at_fold = sp.simplify(jacobian.subs(fold_subs))
        assert jacobian_at_fold.rank() == 3
        kernel = primitive_kernel(jacobian_at_fold.nullspace()[0])
        directional_log_terms = []
        for factor in restricted_factors:
            directional = sum(sp.diff(factor, variable) * kernel[index] for index, variable in enumerate((a, b, c, d)))
            directional_log_terms.append(directional / factor)
        odd_log_derivative = sp.factor((-sum(directional_log_terms)).subs(fold_subs))
        form_at_fold = sp.factor(restricted_form.subs(fold_subs))
        odd_derivative = sp.factor(form_at_fold * odd_log_derivative)
        assert form_at_fold != 0

        specialized_barycentric = [sp.factor(value.subs(external_solution).subs(fold_subs)) for value in restricted_barycentric]
        zero_at_base = [index for index, value in enumerate(specialized_barycentric) if sp.simplify(value.subs(dict.fromkeys(beta, 0))) == 0]
        if odd_log_derivative != 0:
            generic_pairing_nonzero = True
            fold_remainder = "nonzero exact fold sample certifies generic nonvanishing"
        else:
            assert not zero_at_base
            base_factors = [sp.factor(factor.subs(dict.fromkeys(beta, 0))) for factor in restricted_factors]
            symbolic_log_gradient = [
                -sum(sp.diff(factor, variable) / factor for factor in base_factors)
                for variable in (a, b, c, d)
            ]
            symbolic_numerator = sp.cancel(sum(value * cofactor for value, cofactor in zip(symbolic_log_gradient, cofactor_row))).as_numer_denom()[0]
            division_variable = z if z in fold_divisor.free_symbols else b
            fold_remainder = sp.rem(symbolic_numerator, fold_divisor, division_variable)
            generic_pairing_nonzero = sp.expand(fold_remainder) != 0
        pairing_nonzero = generic_pairing_nonzero

        audits.append({
            "model": model["name"],
            "reduced_pattern": pattern,
            "source_orbit_key": key,
            "occurrence_id": occurrence["occurrence_id"],
            "ordered_labels": labels,
            "face_vertex_indices": face_vertices,
            "face_dimension": 8,
            "barycentric_coordinate_rows_zero_based": coordinate_rows,
            "simplex_determinant": str(determinant),
            "external_free_parameter_values": {str(symbol): value for symbol, value in parameter_values.items()},
            "external_solution": {str(symbol): str(value) for symbol, value in external_solution.items()},
            "fold_point": {str(symbol): str(value) for symbol, value in fold_subs.items()},
            "base_normal_coordinates": [str(value) for value in beta],
            "barycentric_factors_vanishing_at_base": zero_at_base,
            "vanishing_barycentric_linear_forms": [str(specialized_barycentric[index]) for index in zero_at_base],
            "companion_jacobian_rank": jacobian_at_fold.rank(),
            "normalized_fold_kernel": [str(value) for value in kernel],
            "face_form_at_fold": str(form_at_fold),
            "odd_log_derivative": str(odd_log_derivative),
            "odd_face_form_derivative": str(odd_derivative),
            "fold_divisor": str(fold_divisor),
            "symbolic_odd_numerator_mod_fold_is_zero": not generic_pairing_nonzero,
            "fold_remainder_certificate": str(fold_remainder),
            "local_pairing_nonzero": pairing_nonzero,
        })

    packet = {
        "schema": "marici.eight_site_rank4_face_fold_pairing.v1",
        "typing": {
            "source": "sevenfold residue of the certified complete C8 canonical form",
            "source_face": "eight-simplex cut out by the seven ordered occurrence facets",
            "fold_direction": "exact corank-one kernel of the source-derived companion map",
            "tested_pairing": "odd first derivative of the source face form along the fold kernel",
            "scope": "local nonvanishing; cyclic normalization and global OS sewing remain separate tests",
        },
        "checks": {
            "source_orbit_count": len(audits),
            "fold_family_count": len({item["model"] for item in audits}),
            "all_faces_are_eight_simplices": all(item["face_dimension"] == 8 for item in audits),
            "all_companion_ranks_three": all(item["companion_jacobian_rank"] == 3 for item in audits),
            "all_source_face_values_nonzero": all(item["face_form_at_fold"] != "0" for item in audits),
            "local_odd_pairing_nonzero_count": sum(item["local_pairing_nonzero"] for item in audits),
            "local_odd_pairing_zero_count": sum(not item["local_pairing_nonzero"] for item in audits),
        },
        "families": audits,
    }
    assert packet["checks"]["source_orbit_count"] == 36
    assert packet["checks"]["fold_family_count"] == 4
    TARGET.write_text(json.dumps(packet, indent=2) + "\n")
    print(json.dumps(packet["checks"], sort_keys=True))


if __name__ == "__main__":
    main()
