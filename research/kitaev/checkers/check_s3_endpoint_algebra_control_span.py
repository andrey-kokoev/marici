"""Exact image of the D(S3) endpoint algebra on all eight simple modules."""

import itertools
import json
import sympy as sp


def compose(p, q): return tuple(p[q[i]] for i in range(3))
def inverse(p):
    out = [0, 0, 0]
    for i, image in enumerate(p): out[image] = i
    return tuple(out)
def conjugate(g, h): return compose(compose(g, h), inverse(g))
def parity(p): return -1 if sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3)) % 2 else 1
def cycle_type(p):
    fixed = sum(p[i] == i for i in range(3))
    return "e" if fixed == 3 else ("t" if fixed == 1 else "c")


def main():
    group = list(itertools.permutations(range(3)))
    e, t, c = (0, 1, 2), (1, 0, 2), (1, 2, 0)
    reps = {"e": e, "t": t, "c": c}
    classes = {name: [g for g in group if cycle_type(g) == name] for name in reps}
    transporters = {
        name: {target: next(q for q in group if conjugate(q, rep) == target) for target in classes[name]}
        for name, rep in reps.items()
    }
    sqrt3 = sp.sqrt(3)
    omega = -sp.Rational(1, 2) + sp.I * sqrt3 / 2
    rmat = sp.Matrix([[-sp.Rational(1, 2), -sqrt3 / 2], [sqrt3 / 2, -sp.Rational(1, 2)]])
    smat = sp.diag(1, -1)
    r, s = (1, 2, 0), (1, 0, 2)
    standard = {}
    for k in range(3):
        pr, mr = e, sp.eye(2)
        for _ in range(k): pr, mr = compose(r, pr), rmat * mr
        for epsilon in range(2): standard[compose(pr, s if epsilon else e)] = sp.simplify(mr * (smat if epsilon else sp.eye(2)))

    labels = [
        ("A", "e", "triv", 1), ("B", "e", "sign", 1), ("C", "e", "std", 2),
        ("D", "t", "plus", 3), ("E", "t", "minus", 3),
        ("F", "c", "triv", 2), ("G", "c", "omega", 2), ("H", "c", "omega2", 2),
    ]

    def internal_matrix(label, z):
        _, sector, irrep, _ = label
        if sector == "e":
            if irrep == "triv": return sp.Matrix([[1]])
            if irrep == "sign": return sp.Matrix([[parity(z)]])
            return standard[z]
        if sector == "t": return sp.Matrix([[1 if irrep == "plus" or z == e else -1]])
        power = {e: 0, c: 1, compose(c, c): 2}[z]
        exponent = power * {"triv": 0, "omega": 1, "omega2": 2}[irrep] % 3
        return sp.Matrix([[sp.simplify(omega ** exponent)]])

    def representation(label, g, x):
        _, sector, _, dimension = label
        fluxes = classes[sector]
        internal_dim = dimension // len(fluxes)
        matrix = sp.zeros(dimension)
        for i, flux_in in enumerate(fluxes):
            flux_out = conjugate(x, flux_in)
            j = fluxes.index(flux_out)
            if g != flux_out: continue
            qi, qj = transporters[sector][flux_in], transporters[sector][flux_out]
            z = compose(compose(inverse(qj), x), qi)
            matrix[j * internal_dim:(j + 1) * internal_dim, i * internal_dim:(i + 1) * internal_dim] = internal_matrix(label, z)
        return sp.simplify(matrix)

    basis = [(g, x) for g in group for x in group]
    per_sector_ranks = {}
    for label in labels:
        columns = [sp.Matrix(representation(label, g, x)).reshape(label[3] ** 2, 1) for g, x in basis]
        per_sector_ranks[label[0]] = sp.Matrix.hstack(*columns).rank()
        assert per_sector_ranks[label[0]] == label[3] ** 2

    global_columns = []
    for g, x in basis:
        block = sp.diag(*(representation(label, g, x) for label in labels))
        global_columns.append(sp.Matrix(block).reshape(16 ** 2, 1))
    global_rank = sp.Matrix.hstack(*global_columns).rank()
    assert global_rank == 36 == sum(label[3] ** 2 for label in labels)

    # Gauge-only controls sum over flux projectors and retain only C[S3].
    gauge_columns = []
    for x in group:
        block = sp.diag(*(sum((representation(label, g, x) for g in group), sp.zeros(label[3])) for label in labels))
        gauge_columns.append(sp.Matrix(block).reshape(16 ** 2, 1))
    gauge_rank = sp.Matrix.hstack(*gauge_columns).rank()
    assert gauge_rank == 6 < global_rank

    result = {
        "schema": "marici.s3-endpoint-algebra-control-span.v1",
        "endpoint_basis_dimension": len(basis),
        "simple_block_dimensions": {label[0]: label[3] for label in labels},
        "per_sector_image_ranks": per_sector_ranks,
        "global_block_diagonal_image_rank": global_rank,
        "full_block_diagonal_algebra_dimension": sum(label[3] ** 2 for label in labels),
        "gauge_only_image_rank": gauge_rank,
        "deliberate_failure": {
            "claim": "gauge_actions_alone_span_all_block_selective_controls",
            "actual_rank": gauge_rank,
            "required_rank": global_rank,
            "rank_deficit": global_rank - gauge_rank,
        },
        "aggregate_gates": {
            "all_eight_simple_representations_have_full_matrix_image": True,
            "joint_endpoint_algebra_image_is_full_block_diagonal_algebra": True,
            "sector_projectors_and_internal_matrix_units_are_in_the_algebraic_span": True,
            "gauge_only_controls_are_insufficient": True,
            "algebraic_span_does_not_imply_executable_unitary_control": True,
            "source_control_typing_remains_open": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__": main()
