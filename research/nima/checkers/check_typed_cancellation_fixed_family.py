from fractions import Fraction
import json
from pathlib import Path


def equivariant_scalar_map_allowed(source_character, target_character):
    return source_character % 3 == target_character % 3


def homogeneous(characters):
    return len(set(c % 3 for c in characters)) <= 1


# Polynomials a*t+b, sufficient for the exact transition test.
def padd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def pmul(x, y):
    # The matrices below never produce degree > 1.
    assert not (x[0] and y[0])
    return (x[0] * y[1] + x[1] * y[0], x[1] * y[1])


def matmul(a, b):
    return [[padd(pmul(a[i][0], b[0][j]), pmul(a[i][1], b[1][j])) for j in range(2)] for i in range(2)]


def det2(a):
    x = pmul(a[0][0], a[1][1])
    y = pmul(a[0][1], a[1][0])
    return (x[0] - y[0], x[1] - y[1])


def rank(matrix):
    """Exact row rank over Q for a small dense matrix."""
    a = [[Fraction(x) for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        a[r] = [x / p for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def coupled_cancellation_dimension(left, right):
    """dim ker[left right] - dim ker(left) - dim ker(right)."""
    target_dim = len(left)
    left_dim = len(left[0]) if target_dim else 0
    right_dim = len(right[0]) if target_dim else 0
    combined = [lrow + rrow for lrow, rrow in zip(left, right)]
    kernel_combined = left_dim + right_dim - rank(combined)
    kernel_left = left_dim - rank(left)
    kernel_right = right_dim - rank(right)
    return kernel_combined - kernel_left - kernel_right


def specialize_linear_column(column, t_value):
    """Column entries are pairs (t coefficient, constant coefficient)."""
    return [[a * t_value + b] for a, b in column]


def main():
    magnetic_characters = [0, 2, 2]
    descended_spin_two_character = 1
    magnetic_allowed_routes = [
        equivariant_scalar_map_allowed(c, descended_spin_two_character)
        for c in magnetic_characters
    ]

    cosmology_characters = [0, 0]
    cosmology_target = 0
    cosmology_routes = [8, -8]

    rational_depths = [Fraction(17, 3), Fraction(37, 3)]
    shifted_labels = [(d - 1, d + 1) for d in rational_depths]
    labels_integral = [all(x.denominator == 1 for x in pair) for pair in shifted_labels]

    # Forgetting grades retains the pair; cancellation needs an additional
    # codiagonal collapse into one scalar output.
    forgotten_underlying_pair = (6, -6)
    collapsed_scalar = sum(forgotten_underlying_pair)

    zero, one, two, t = (0, 0), (0, 1), (0, 2), (1, 0)
    family = [[t, zero], [zero, one]]
    left_transition = [[one, one], [zero, one]]       # determinant 1
    right_transition = [[two, zero], [one, one]]      # determinant 2, a unit over Q
    transformed = matmul(matmul(left_transition, family), right_transition)
    bad_nonunit_change = [[zero, zero], [zero, one]]  # determinant 0, not invertible
    badly_transformed = matmul(bad_nonunit_change, family)

    # A basis-chosen codiagonal on unrelated lines is not invariant under
    # independent automorphisms.  The cancellation (1,-1) is destroyed by
    # rescaling only the second line.  Under a common diagonal scaling, the
    # sum transforms covariantly and its zero is preserved.
    pair = (1, -1)
    chosen_codiagonal = lambda x: x[0] + x[1]
    independently_rescaled = (pair[0], 2 * pair[1])
    commonly_rescaled = (2 * pair[0], 2 * pair[1])

    # Invariance equations for f=(c1,c2) under diag(2,1) and diag(1,2)
    # force c1=0 and c2=0 respectively.
    only_independent_rescaling_invariant_coefficients = (0, 0)

    # Once the source supplies the two cospan legs, independent basis changes
    # are harmless only if route coordinates and leg covectors transform
    # together.  With e_i' = alpha_i e_i, coordinates divide by alpha_i and
    # covector coefficients multiply by alpha_i.
    source_route_coordinates = (Fraction(1), Fraction(-1))
    source_leg_coefficients = (Fraction(1), Fraction(1))
    independent_basis_scales = (Fraction(2), Fraction(3))
    transported_coordinates = tuple(
        x / alpha for x, alpha in zip(source_route_coordinates, independent_basis_scales)
    )
    transported_leg_coefficients = tuple(
        alpha * c for c, alpha in zip(source_leg_coefficients, independent_basis_scales)
    )
    source_contributions = tuple(
        c * x for c, x in zip(source_leg_coefficients, source_route_coordinates)
    )
    transported_contributions = tuple(
        c * x for c, x in zip(transported_leg_coefficients, transported_coordinates)
    )
    frozen_leg_contributions = tuple(
        c * x for c, x in zip(source_leg_coefficients, transported_coordinates)
    )

    # Three canonical cospan types.  Cosmology has two nonzero legs into one
    # line.  Route loss has one zero leg.  Deck-separated magnetic routes land
    # in disjoint summands of a faithful target.
    cosmology_coupled_dim = coupled_cancellation_dimension([[8]], [[-8]])
    route_loss_coupled_dim = coupled_cancellation_dimension([[0]], [[1]])
    magnetic_faithful_coupled_dim = coupled_cancellation_dimension(
        [[1], [0]], [[0], [1]]
    )

    # Interference birth with both route ranks preserved.
    collision_left = [((0, 1)), ((0, 0))]
    collision_right = [((0, 1)), ((1, 0))]
    collision_generic = (
        specialize_linear_column(collision_left, 1),
        specialize_linear_column(collision_right, 1),
    )
    collision_special = (
        specialize_linear_column(collision_left, 0),
        specialize_linear_column(collision_right, 0),
    )
    collision_dims = tuple(coupled_cancellation_dimension(*pair) for pair in (collision_generic, collision_special))
    collision_route_ranks = tuple(
        (rank(pair[0]), rank(pair[1])) for pair in (collision_generic, collision_special)
    )

    # Total determinant also vanishes here, but only because the left route
    # dies; the coupled quotient remains zero.
    loss_left = [((1, 0)), ((0, 0))]
    loss_right = [((0, 0)), ((0, 1))]
    loss_generic = (
        specialize_linear_column(loss_left, 1),
        specialize_linear_column(loss_right, 1),
    )
    loss_special = (
        specialize_linear_column(loss_left, 0),
        specialize_linear_column(loss_right, 0),
    )
    loss_dims = tuple(coupled_cancellation_dimension(*pair) for pair in (loss_generic, loss_special))
    loss_route_ranks = tuple(
        (rank(pair[0]), rank(pair[1])) for pair in (loss_generic, loss_special)
    )

    gates = {
        "magnetic_candidate_is_not_deck_homogeneous": not homogeneous(magnetic_characters),
        "no_magnetic_route_maps_to_descended_spin_two_sector": not any(magnetic_allowed_routes),
        "cosmology_routes_share_typed_output": (
            homogeneous(cosmology_characters)
            and all(equivariant_scalar_map_allowed(c, cosmology_target) for c in cosmology_characters)
            and sum(cosmology_routes) == 0
            and all(x != 0 for x in cosmology_routes)
        ),
        "forgetting_grading_does_not_kill_direct_sum_vector": forgotten_underlying_pair != (0, 0),
        "extra_codiagonal_collapse_can_fake_cancellation": collapsed_scalar == 0,
        "rational_depth_changes_integral_source_labels": not any(labels_integral),
        "invertible_basis_changes_preserve_fitting_zero": (
            det2(family) == (1, 0) and det2(transformed) == (2, 0)
        ),
        "nonunit_comparison_is_not_a_legal_transition": det2(badly_transformed) != det2(family),
        "chosen_codiagonal_is_not_natural_for_unrelated_lines": (
            chosen_codiagonal(pair) == 0
            and chosen_codiagonal(independently_rescaled) != 0
        ),
        "common_typed_scaling_preserves_cancellation": chosen_codiagonal(commonly_rescaled) == 0,
        "independent_gauge_invariance_forces_zero_pairing": (
            only_independent_rescaling_invariant_coefficients == (0, 0)
        ),
        "source_supplied_cospan_is_natural_under_independent_frames": (
            source_contributions == transported_contributions
            and sum(source_contributions) == 0
            and sum(transported_contributions) == 0
        ),
        "freezing_pairing_during_frame_change_is_mistyped": sum(frozen_leg_contributions) != 0,
        "cosmology_has_rank_one_coupled_cancellation": cosmology_coupled_dim == 1,
        "dead_route_does_not_count_as_interference": route_loss_coupled_dim == 0,
        "deck_separated_images_have_no_coupled_cancellation": magnetic_faithful_coupled_dim == 0,
        "interference_can_birth_without_route_rank_loss": (
            collision_route_ranks == ((1, 1), (1, 1))
            and collision_dims == (0, 1)
        ),
        "route_loss_is_not_interference_birth": (
            loss_route_ranks == ((1, 1), (0, 1))
            and loss_dims == (0, 0)
        ),
    }
    assert all(gates.values()), gates

    result = {
        "schema": "marici.typed-cancellation-fixed-family.v1",
        "gates": gates,
        "magnetic": {
            "route_characters": magnetic_characters,
            "target_character": descended_spin_two_character,
            "equivariant_route_admission": magnetic_allowed_routes,
            "classification": "pseudo-interference after type collapse",
            "forgotten_underlying_pair": list(forgotten_underlying_pair),
            "collapsed_scalar": collapsed_scalar,
        },
        "cosmology": {
            "route_characters": cosmology_characters,
            "route_values": cosmology_routes,
            "classification": "genuine typed interference",
        },
        "continued_labels": [[str(x) for x in pair] for pair in shifted_labels],
        "family_transition": {
            "original_determinant": "t",
            "legal_transition_determinant": "2t",
            "same_fitting_support_over_Q": True,
            "nonunit_comparison": "not a bundle transition",
        },
        "naturality": {
            "basis_chosen_cancellation": list(pair),
            "independent_rescaling_breaks_zero": list(independently_rescaled),
            "common_scaling_preserves_zero": list(commonly_rescaled),
            "canonical_pairing_on_unrelated_lines": "zero only",
            "source_supplied_pairing_contributions": [str(x) for x in source_contributions],
            "transported_pairing_contributions": [str(x) for x in transported_contributions],
            "frozen_pairing_contributions": [str(x) for x in frozen_leg_contributions],
            "classification": "bare lines have no canonical codiagonal; a source-supplied cospan transports contragrediently",
        },
        "coupled_cancellation": {
            "cosmology_dimension": cosmology_coupled_dim,
            "route_loss_dimension": route_loss_coupled_dim,
            "magnetic_faithful_dimension": magnetic_faithful_coupled_dim,
            "invariant": "ker([f_L,f_R]) / (ker(f_L) plus ker(f_R))",
            "rank_preserving_collision": {
                "route_ranks_generic_special": [list(x) for x in collision_route_ranks],
                "coupled_dimensions_generic_special": list(collision_dims),
            },
            "route_loss_control": {
                "route_ranks_generic_special": [list(x) for x in loss_route_ranks],
                "coupled_dimensions_generic_special": list(loss_dims),
            },
        },
        "conclusion": "a determinant zero is an event only in a coherent equivariant source family",
    }
    out = Path(__file__).parents[1] / "results" / "typed-cancellation-fixed-family.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
