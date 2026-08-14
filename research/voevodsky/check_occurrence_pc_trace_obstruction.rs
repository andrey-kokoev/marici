//! Exact obstruction audit for lifting the conductor normal-link fold to
//! occurrence-loaded Pochhammer/Cousin coefficients at D=03.
//!
//! The audit keeps two coefficient layers separate:
//!
//! * `u_j = q_j - 1` is the normal-local-system differential of entry 38;
//! * `x_a x_b` is an occurrence mark in the D=03 road square of entry 86.
//!
//! First, consider the strongest strict interpretation of a paired fold.  A
//! source edge with normal complex K(u_j)=[R -> R] and unit endpoint value
//! `+/-1` is mapped to a single tagged rank-one normal complex K(v_i).  The
//! chain equation says that v_i divides u_j.  Since K_alt pairs independent
//! variables u_j and u_{j+3}, v_i must divide their gcd, hence v_i is a unit.
//! A unit differential has no boundary support.  Thus the associated-grade
//! K_alt fold cannot be lifted as a strict unit map to one common rank-one
//! tagged local system over the identity universal monodromy base.
//!
//! This does not rule out the desired noninvertible Gysin correspondence.  It
//! shows exactly what it must add: a span with specified pullbacks of the two
//! source characters, rather than an unidentified common target character.
//!
//! Second, entry 86 fixes only the occurrence endpoint of that correspondence.
//! On the normalized weighted road square the plus support is v00+v10 and the
//! minus support is v00+v01.  Their difference has two Cousin primitives,
//! through v00 and through v11.  Those primitives differ by the top-cell
//! boundary.  Endpoint values therefore determine a derived null class but do
//! not select the lower-Cousin/top-coherence datum required to realize Delta.

type Z = i64;
type Vector<const N: usize> = [Z; N];
type Matrix<const ROWS: usize, const COLUMNS: usize> = [[Z; COLUMNS]; ROWS];

const K_ALT: Matrix<3, 6> = [
    [0, 0, -1, 0, 0, 1],
    [-1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, -1, 0],
];

fn mat_vec<const ROWS: usize, const COLUMNS: usize>(
    matrix: Matrix<ROWS, COLUMNS>,
    vector: Vector<COLUMNS>,
) -> Vector<ROWS> {
    std::array::from_fn(|row| {
        (0..COLUMNS)
            .map(|column| matrix[row][column] * vector[column])
            .sum()
    })
}

fn column<const ROWS: usize, const COLUMNS: usize>(
    matrix: Matrix<ROWS, COLUMNS>,
    index: usize,
) -> Vector<ROWS> {
    std::array::from_fn(|row| matrix[row][index])
}

fn standard_monomial(variable: usize) -> Vector<6> {
    let mut result = [0; 6];
    result[variable] = 1;
    result
}

fn common_monomial_divisor(left: Vector<6>, right: Vector<6>) -> Vector<6> {
    std::array::from_fn(|index| left[index].min(right[index]))
}

fn is_unit_monomial(value: Vector<6>) -> bool {
    value == [0; 6]
}

fn subtract<const N: usize>(left: Vector<N>, right: Vector<N>) -> Vector<N> {
    std::array::from_fn(|index| left[index] - right[index])
}

fn main() {
    // K_alt pairs the six conductor edges into three tags.  Every column is a
    // signed unit tag, and every tag receives exactly two opposite signs.
    let expected_tag = [1, 2, 0, 1, 2, 0];
    let expected_sign = [-1, 1, -1, 1, -1, 1];
    for edge in 0..6 {
        let image = column(K_ALT, edge);
        assert_eq!(image.iter().filter(|&&value| value != 0).count(), 1);
        assert_eq!(image[expected_tag[edge]], expected_sign[edge]);
    }

    let paired_edges = [(2, 5), (0, 3), (1, 4)];
    for (tag, &(first, second)) in paired_edges.iter().enumerate() {
        assert_eq!(expected_tag[first], tag);
        assert_eq!(expected_tag[second], tag);
        assert_eq!(expected_sign[first], -expected_sign[second]);

        // For a strict map K(u_j) -> K(v_tag) with unit endpoint coefficient,
        // the chain equation v_tag * a_j = +/- u_j requires v_tag | u_j.
        // The two source monodromies are independent universal variables, so
        // their only common monomial divisor is 1.
        let common = common_monomial_divisor(standard_monomial(first), standard_monomial(second));
        assert!(is_unit_monomial(common));
    }

    // Entry 86's occurrence marks are kept distinct from u_j.  In normalized
    // road-square coordinates the four vertices are
    //   v00=x0*x3, v10=x1*x3, v01=x0*x4, v11=x1*x4.
    // The two sheet-resolved endpoint supports agree at v00 but are not equal
    // as occurrence vectors.
    let plus_endpoint = [1, 1, 0, 0];
    let minus_endpoint = [1, 0, 1, 0];
    let endpoint_difference = subtract(plus_endpoint, minus_endpoint);
    assert_eq!(endpoint_difference, [0, 1, -1, 0]);

    // Established normalized weighted-square Cousin boundary.  Columns are:
    // bottom horizontal a, top horizontal b, left vertical c, right vertical
    // d.  The top-cell boundary is a-b-c+d.
    let road_cousin_d1: Matrix<4, 4> = [[-1, 0, -1, 0], [1, 0, 0, -1], [0, -1, 1, 0], [0, 1, 0, 1]];
    let road_cousin_d2 = [1, -1, -1, 1];
    assert_eq!(mat_vec(road_cousin_d1, road_cousin_d2), [0; 4]);

    // The route through the common occurrence v00 is a-c; the opposite route
    // through v11 is b-d.  Both have the required endpoint difference.
    let primitive_via_v00 = [1, 0, -1, 0];
    let primitive_via_v11 = [0, 1, 0, -1];
    assert_eq!(
        mat_vec(road_cousin_d1, primitive_via_v00),
        endpoint_difference
    );
    assert_eq!(
        mat_vec(road_cousin_d1, primitive_via_v11),
        endpoint_difference
    );
    assert_eq!(
        subtract(primitive_via_v00, primitive_via_v11),
        road_cousin_d2
    );

    // The primitive endpoint functional sees all four normalized occurrences
    // as one.  It kills the endpoint difference, but cannot distinguish the
    // two lower-Cousin primitives or provide the missing top coherence.
    let primitive_counit = [1, 1, 1, 1];
    let endpoint_period: Z = primitive_counit
        .into_iter()
        .zip(endpoint_difference)
        .map(|(functional, value)| functional * value)
        .sum();
    assert_eq!(endpoint_period, 0);

    // Sanity check that the two source supports have equal primitive period
    // two, as in the selected-edge part of entry 86.
    let plus_period: Z = plus_endpoint.into_iter().sum();
    let minus_period: Z = minus_endpoint.into_iter().sum();
    assert_eq!((plus_period, minus_period), (2, 2));

    // Static packet preserves the project result schema.  This is a scoped
    // obstruction, not a claim that a noninvertible Gysin lift cannot exist.
    println!(
        "{}",
        concat!(
            r#"{"claim":"the associated-grade conductor fold is not canonically liftable from the recorded data as a strict unit map of the six paired rank-one PC normal local systems; the first admissible replacement is an occurrence-loaded Gysin span with specified monodromy pullbacks and a chosen-by-geometry lower-Cousin/top-cell coherence realizing Delta","status":"inconclusive","assumptions":["the strict negative control is over the identity universal monodromy base Z[u0,...,u5] with algebraically independent normal factors","K_alt retains unit endpoint coefficients on its six columns","the D=03 normalized road-square differential is the tensor weighted-interval Cousin differential of entries 38, 86, and 89"],"evidence_refs":["research/voevodsky/check_occurrence_pc_trace_obstruction.rs","src/ledger/20260813-38 Finite-Alpha-Prime Normal-Torus Lift and Nearby-Cycle Unit Theorem.md","src/ledger/20260814-86 Occurrence-Conjugated Core-Entry Counit and the Vanishing Residue Scalar.md","src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md","src/ledger/20260814-94 Augmented Triangle Resolution and the D03 Primitive Cousin Symbol.md","research/voevodsky/check_conductor_normal_link_fold.rs"],"factorization_test":{"channel":"D=03","strict_common_rank_one_target":"FAIL: the common divisor of each paired independent monodromy pair is the unit, so a supported target normal differential cannot satisfy both unit chain equations","occurrence_endpoint":"PASS: plus and minus selected-edge periods are both 2 and their difference has primitive period 0","lower_cousin":"UNDERDETERMINED: two exact primitives of the endpoint difference differ by the road-square top-cell boundary","delta_relation":"UNTYPED: no recorded Gysin span selects the pullback characters, lower-Cousin primitive, and compatible top coherence"},"counterevidence":["Nonresonant localization makes every u_j invertible, so algebraic maps can be manufactured by ratios u_j/v; this erases support and does not canonically choose v or its associated grade.","Entry 86 fixes endpoint residue values but not a morphism of normal local systems or the top-cell coherence needed for the Delta relation.","The strict no-go does not falsify a noninvertible correspondence whose two legs pull one target coefficient object back to the two distinct source characters."],"next_experiment":"construct for the pair (x0,x3) the actual factorization-marked correspondence Z_0 <- W_03 -> Z_3, specify its pullback maps on the universal normal tori and occurrence cosheaves, and compute its PC trace on the two road-square Cousin primitives; require geometry to select one primitive and send their top-cell difference to the Delta relation, then rotate only after this D=03 square commutes"}"#
        )
    );
}
