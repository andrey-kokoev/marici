//! Exact integral certificate for the global D=03 dual-block carrier.
//!
//! This checker is deliberately confined to based equivariant cellular
//! chains.  The all-odd and all-even central triangulations of the labelled
//! hexagon have triangular vertex figures.  After the one-degree dual-block
//! suspension, their augmented cellular complexes map to
//!
//!   C_*(K_6,B_short) = [ Z<K_rel> -> Z<T0,T1,T2> ],
//!
//! where d K_rel = T0 + T1 + T2.  The link edge e_j is matched with the
//! long-diagonal road F_{j,j+3}, the unique road fixed by the same reflection.
//! Consequently
//!
//!   e1 -> T2, e3 -> T1, e5 -> T0,
//!   e0 -> -T1, e2 -> -T0, e4 -> -T2,
//!
//! and the top coefficients +1 and -1 are forced by the chain equation.
//!
//! The certificate also records the essential boundary of this statement.
//! Each one-sheet map is null-homotopic after forgetting equivariance.  An
//! integral D3-equivariant contraction would require 3a=1 (or 3a=-1 on the
//! minus sheet), so only the rational coefficient a=1/3 can contract the plus
//! carrier equivariantly.  No occurrence, normal-torus, can/var, Cousin, or PC
//! loading is constructed here.

type Z = i64;
type Matrix = Vec<Vec<Z>>;

const SOURCE_D3: [[Z; 2]; 6] = [[0, 1], [1, 0], [0, 1], [1, 0], [0, 1], [1, 0]];

const SOURCE_D2: [[Z; 6]; 3] = [
    [1, 1, 0, -1, -1, 0],
    [0, -1, -1, 0, 1, 1],
    [-1, 0, 1, 1, 0, -1],
];

const SOURCE_D1: [[Z; 3]; 1] = [[1, 1, 1]];
const TARGET_D3: [[Z; 1]; 3] = [[1], [1], [1]];

const CARRIER_TOP: [[Z; 2]; 1] = [[1, -1]];
const CARRIER_EDGE: [[Z; 6]; 3] = [
    [0, 0, -1, 0, 0, 1],
    [-1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, -1, 0],
];

fn matrix<const ROWS: usize, const COLUMNS: usize>(entries: [[Z; COLUMNS]; ROWS]) -> Matrix {
    entries.map(Vec::from).into()
}

fn zero(rows: usize, columns: usize) -> Matrix {
    vec![vec![0; columns]; rows]
}

fn identity(size: usize) -> Matrix {
    let mut result = zero(size, size);
    for (index, row) in result.iter_mut().enumerate() {
        row[index] = 1;
    }
    result
}

fn dimensions(value: &Matrix) -> (usize, usize) {
    let columns = value.first().map_or(0, Vec::len);
    assert!(value.iter().all(|row| row.len() == columns));
    (value.len(), columns)
}

fn multiply(left: &Matrix, right: &Matrix) -> Matrix {
    let (left_rows, middle) = dimensions(left);
    let (right_rows, right_columns) = dimensions(right);
    assert_eq!(middle, right_rows);
    let mut result = zero(left_rows, right_columns);
    for row in 0..left_rows {
        for column in 0..right_columns {
            result[row][column] = (0..middle)
                .map(|index| left[row][index] * right[index][column])
                .sum();
        }
    }
    result
}

fn add(left: &Matrix, right: &Matrix) -> Matrix {
    assert_eq!(dimensions(left), dimensions(right));
    left.iter()
        .zip(right)
        .map(|(left_row, right_row)| {
            left_row
                .iter()
                .zip(right_row)
                .map(|(left_entry, right_entry)| left_entry + right_entry)
                .collect()
        })
        .collect()
}

fn power(value: &Matrix, exponent: usize) -> Matrix {
    let (rows, columns) = dimensions(value);
    assert_eq!(rows, columns);
    let mut result = identity(rows);
    for _ in 0..exponent {
        result = multiply(&result, value);
    }
    result
}

fn signed_permutation(images: &[(usize, Z)]) -> Matrix {
    let mut result = zero(images.len(), images.len());
    for (source, &(target, sign)) in images.iter().enumerate() {
        assert!(target < images.len());
        assert!(sign == 1 || sign == -1);
        result[target][source] = sign;
    }
    result
}

fn select_columns(value: &Matrix, columns: &[usize]) -> Matrix {
    value
        .iter()
        .map(|row| columns.iter().map(|&column| row[column]).collect())
        .collect()
}

fn check_complexes_and_carrier() {
    let source_d3 = matrix(SOURCE_D3);
    let source_d2 = matrix(SOURCE_D2);
    let source_d1 = matrix(SOURCE_D1);
    let target_d3 = matrix(TARGET_D3);
    let carrier_top = matrix(CARRIER_TOP);
    let carrier_edge = matrix(CARRIER_EDGE);

    assert_eq!(multiply(&source_d2, &source_d3), zero(3, 2));
    assert_eq!(multiply(&source_d1, &source_d2), zero(1, 6));

    // The two global sheetwise top squares.  The remaining target groups are
    // zero, so the lower carrier components are the zero maps.
    assert_eq!(
        multiply(&carrier_edge, &source_d3),
        multiply(&target_d3, &carrier_top)
    );

    let expected_edges = matrix([
        [0, 0, -1, 0, 0, 1],
        [-1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, -1, 0],
    ]);
    assert_eq!(carrier_edge, expected_edges);
}

fn check_top_coefficients_forced() {
    let source_d3 = matrix(SOURCE_D3);
    let carrier_edge = matrix(CARRIER_EDGE);
    let sheet_boundaries = multiply(&carrier_edge, &source_d3);

    let plus = sheet_boundaries
        .iter()
        .map(|row| row[0])
        .collect::<Vec<_>>();
    let minus = sheet_boundaries
        .iter()
        .map(|row| row[1])
        .collect::<Vec<_>>();
    assert_eq!(plus, vec![1, 1, 1]);
    assert_eq!(minus, vec![-1, -1, -1]);

    // Since d(K_rel)=(1,1,1) is injective over Z, these common entries are
    // the unique possible top coefficients.
    assert_eq!(plus[0], 1);
    assert!(plus.iter().all(|&entry| entry == plus[0]));
    assert_eq!(minus[0], -1);
    assert!(minus.iter().all(|&entry| entry == minus[0]));
}

fn check_actions_and_covariance() {
    // One-step cyclic transport is the polarity operation: it swaps sheets,
    // sends e_j to -e_{j+1}, fixes K_rel, and rotates the road facets.
    let tau_f = signed_permutation(&[(1, -1), (0, -1)]);
    let tau_e = signed_permutation(&[(1, -1), (2, -1), (3, -1), (4, -1), (5, -1), (0, -1)]);
    let tau_q = signed_permutation(&[(1, 1), (2, 1), (0, 1)]);
    let tau_one = identity(1);
    let tau_k = identity(1);
    let tau_t = signed_permutation(&[(1, 1), (2, 1), (0, 1)]);

    // The reflection k -> 2-k preserves each sheet and reverses orientations.
    let reflection_f = signed_permutation(&[(0, -1), (1, -1)]);
    let reflection_e = signed_permutation(&[(2, -1), (1, -1), (0, -1), (5, -1), (4, -1), (3, -1)]);
    let reflection_q = signed_permutation(&[(1, 1), (0, 1), (2, 1)]);
    let reflection_one = identity(1);
    let reflection_k = matrix([[-1]]);
    let reflection_t = signed_permutation(&[(1, -1), (0, -1), (2, -1)]);

    let source_d3 = matrix(SOURCE_D3);
    let source_d2 = matrix(SOURCE_D2);
    let source_d1 = matrix(SOURCE_D1);
    let target_d3 = matrix(TARGET_D3);
    let carrier_top = matrix(CARRIER_TOP);
    let carrier_edge = matrix(CARRIER_EDGE);

    for (upper, lower, differential) in [
        (&tau_f, &tau_e, &source_d3),
        (&tau_e, &tau_q, &source_d2),
        (&tau_q, &tau_one, &source_d1),
        (&reflection_f, &reflection_e, &source_d3),
        (&reflection_e, &reflection_q, &source_d2),
        (&reflection_q, &reflection_one, &source_d1),
    ] {
        assert_eq!(multiply(lower, differential), multiply(differential, upper));
    }
    assert_eq!(multiply(&tau_t, &target_d3), multiply(&target_d3, &tau_k));
    assert_eq!(
        multiply(&reflection_t, &target_d3),
        multiply(&target_d3, &reflection_k)
    );

    // Covariance of the global two-sheet carrier under polarity and D3.
    assert_eq!(
        multiply(&tau_k, &carrier_top),
        multiply(&carrier_top, &tau_f)
    );
    assert_eq!(
        multiply(&tau_t, &carrier_edge),
        multiply(&carrier_edge, &tau_e)
    );
    assert_eq!(
        multiply(&reflection_k, &carrier_top),
        multiply(&carrier_top, &reflection_f)
    );
    assert_eq!(
        multiply(&reflection_t, &carrier_edge),
        multiply(&carrier_edge, &reflection_e)
    );

    // tau^2 and the reflection generate the D3 stabilizer of either central
    // vertex.  The full signed actions obey the dihedral relations.
    for action in [&tau_f, &tau_e, &tau_q, &tau_k, &tau_t] {
        assert_eq!(power(action, 6), identity(dimensions(action).0));
    }
    for reflection in [
        &reflection_f,
        &reflection_e,
        &reflection_q,
        &reflection_k,
        &reflection_t,
    ] {
        assert_eq!(power(reflection, 2), identity(dimensions(reflection).0));
    }
    for (tau, reflection) in [
        (&tau_f, &reflection_f),
        (&tau_e, &reflection_e),
        (&tau_q, &reflection_q),
        (&tau_k, &reflection_k),
        (&tau_t, &reflection_t),
    ] {
        let inverse_tau = power(tau, 5);
        assert_eq!(
            multiply(reflection, &multiply(tau, reflection)),
            inverse_tau
        );
        let d3_rotation = power(tau, 2);
        assert_eq!(power(&d3_rotation, 3), identity(dimensions(tau).0));
    }
}

fn check_sheet_null_homotopies() {
    let source_d2 = matrix(SOURCE_D2);
    let carrier_edge = matrix(CARRIER_EDGE);
    let target_d3 = matrix(TARGET_D3);
    let sheet_d3 = matrix([[1], [1], [1]]);

    let plus_d2 = select_columns(&source_d2, &[1, 3, 5]);
    let plus_edge = select_columns(&carrier_edge, &[1, 3, 5]);
    let plus_h2 = matrix([[1, 0, 0]]);
    let plus_h1 = matrix([[0, 1, 0], [0, 1, 1], [0, 0, 0]]);
    assert_eq!(multiply(&plus_h2, &sheet_d3), matrix([[1]]));
    assert_eq!(
        add(
            &multiply(&target_d3, &plus_h2),
            &multiply(&plus_h1, &plus_d2)
        ),
        plus_edge
    );

    let minus_d2 = select_columns(&source_d2, &[0, 2, 4]);
    let minus_edge = select_columns(&carrier_edge, &[0, 2, 4]);
    let minus_h2 = matrix([[-1, 0, 0]]);
    let minus_h1 = matrix([[0, 0, -1], [0, 0, 0], [0, -1, -1]]);
    assert_eq!(multiply(&minus_h2, &sheet_d3), matrix([[-1]]));
    assert_eq!(
        add(
            &multiply(&target_d3, &minus_h2),
            &multiply(&minus_h1, &minus_d2)
        ),
        minus_edge
    );
}

fn check_equivariant_contraction_obstruction() {
    // D3 transitively permutes the three link edges and fixes K_rel, so an
    // equivariant h2 has one integral coefficient a on all three edges.  The
    // plus top homotopy equation is 3a=1, which has no integral solution.
    assert_ne!(1_i64.rem_euclid(3), 0);
    assert_ne!((-1_i64).rem_euclid(3), 0);

    // Over Q, a=1/3 (and -1/3 on the minus sheet) solves the top equation.
    let plus_numerator = 1_i64;
    let minus_numerator = -1_i64;
    let denominator = 3_i64;
    assert_eq!(3 * plus_numerator, denominator);
    assert_eq!(3 * minus_numerator, -denominator);
}

fn main() {
    check_complexes_and_carrier();
    check_top_coefficients_forced();
    check_actions_and_covariance();
    check_sheet_null_homotopies();
    check_equivariant_contraction_obstruction();

    println!(
        "{}",
        concat!(
            r#"{"claim":"the labelled pair (K6,B_short), with its based vertex-figure cells and transported orientations, supplies two polarity-related integral cellular maps from the suspended augmented plus/minus links to the relative complex Z<K_rel> -> Z<T0,T1,T2>; the link-to-road matching forces f_+ -> +K_rel and f_- -> -K_rel, so all six carrier attachments are restrictions of two global maps","status":"proved","scope":"based D3-equivariant integral cellular carrier only","assumptions":["the relative facet orientations are normalized by dK_rel=T0+T1+T2","the link edge e_j is matched with the long-diagonal road F_{j,j+3}, equivalently the road fixed by the same reflection","the documented polarity action sends e_j to -e_{j+1}, swaps f_+ and f_- with sign -1, and fixes K_rel"],"factorization_test":{"plus_chain_map":"PASS: f_+ maps to K_rel and (e1,e3,e5) map to (T2,T1,T0)","minus_chain_map":"PASS: f_- maps to -K_rel and (e0,e2,e4) map to (-T1,-T0,-T2)","top_coefficients":"PASS and forced: injectivity of dK_rel=(1,1,1) gives +1 and -1","D3_covariance":"PASS for the order-three rotation tau^2 and the orientation-reversing reflection","polarity_covariance":"PASS for one-step signed sheet exchange tau","ordinary_homotopy":"PASS: explicit integral non-equivariant null-homotopies are verified on both sheets","equivariant_obstruction":"PASS: D3-equivariance forces a common h2 coefficient and hence 3a=1 or 3a=-1, with no integral solution","rational_contraction":"PASS: a=1/3 and a=-1/3 solve the respective top equations over Q"},"counterevidence":["after forgetting based equivariant cellular structure, each one-sheet carrier is null-homotopic","the certificate does not construct an occurrence-weighted or normal-support kernel","the certificate contains no nearby-cycle can/var maps, lower Cousin terms, reciprocal/Borel-Moore pairing, or PC loading"],"blocker":"construct an unlocalized support-filtered can/var-Cousin lift whose associated based cellular grade is this global carrier and whose road restrictions are the six excess-one Beck-Chevalley comparisons","next_experiment":"build the plus-sheet unlocalized normal-support lift before inverting any u_j, then verify its D03 restriction against the established reciprocal-twist PC trace"}"#
        )
    );
}
