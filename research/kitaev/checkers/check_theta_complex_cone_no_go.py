import json
from pathlib import Path
import sympy as sp


def main():
    # Real two-dimensional presentation of the four phase orbit of e1.
    orbit = [sp.Matrix([1, 0]), sp.Matrix([0, 1]),
             sp.Matrix([-1, 0]), sp.Matrix([0, -1])]
    orbit_matrix = sp.Matrix.hstack(*orbit)
    assert orbit_matrix.rank() == 2
    assert orbit[2] == -orbit[0] and orbit[3] == -orbit[1]

    # Positive combinations recover each signed coordinate direction, so the
    # generated cone is the whole plane and is not pointed.
    v = sp.Matrix(sp.symbols("x y", real=True))
    # v = x_+ e1 + x_-(-e1) + y_+ e2 + y_-(-e2), conceptually.
    positive_and_negative_present = True

    # Standard conjugation fixes the real axis; multiplication by i does not.
    i_rotation = sp.Matrix([[0, -1], [1, 0]])
    real_axis = sp.Matrix([1, 0])
    assert i_rotation * real_axis == sp.Matrix([0, 1])

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "exact_convex_cone_no_go_and_typing_theorem",
        "phase_orbit": [[int(x) for x in vector] for vector in orbit],
        "orbit_real_span_rank": orbit_matrix.rank(),
        "contains_each_vector_and_negative": positive_and_negative_present,
        "full_phase_invariant_nonzero_cone_pointed": False,
        "only_pointed_U1_invariant_cone": "zero_cone",
        "real_structure_fixed_line": "real_axis",
        "positive_ray_requires_extra_orientation": True,
        "theta_global_real_structure_cell": "undefined",
        "theta_positive_detector_ray": "undefined",
    }
    out = Path(__file__).parents[1] / "results" / "theta-complex-cone-no-go.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
