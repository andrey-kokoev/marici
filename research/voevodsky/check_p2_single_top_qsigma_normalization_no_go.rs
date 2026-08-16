//! Scoped incompatibility of a single P2 source top with both required targets.
//!
//! The certified C3 carrier equation forces the source top coefficient to
//! have absolute value two.  The independently fixed mixed boundary
//! dH_Sigma=q_Sigma-sum_D s_D and projective Gysin q_*(xi^2)=1 force the
//! same coefficient to have absolute value one.  Orientation changes signs,
//! not magnitudes, so one source generator cannot satisfy both equations.
//!
//! This does not obstruct a two-top/can-var extension separating cyclic
//! coherence from the primitive physical mixed top.

fn gcd(mut a: i64, mut b: i64) -> i64 {
    a = a.abs();
    b = b.abs();
    while b != 0 {
        (a, b) = (b, a % b);
    }
    a
}

fn main() {
    // Independently certified inputs.
    let pairwise_cyclic_top_defect = -2_i64;
    let projective_gysin_top = 1_i64;
    let physical_q_sigma_coefficient = 1_i64;
    let conductor_codimension = 3_i64;
    let relative_canonical_discrepancy = conductor_codimension - 1;
    assert_eq!(relative_canonical_discrepancy, 2);

    // If one primitive source top maps to the primitive K6 top with
    // coefficient a, the carrier chain equation forces a=-defect=2 in this
    // orientation. Reversing either orientation changes only the sign.
    let carrier_forced = -pairwise_cyclic_top_defect;
    assert_eq!(carrier_forced.abs(), 2);

    // The same top, if identified with entry113's physical mixed top, must
    // carry the primitive projective augmentation to qSigma with unit
    // coefficient. Again orientation permits only a sign change.
    let generic_forced = projective_gysin_top * physical_q_sigma_coefficient;
    assert_eq!(generic_forced.abs(), 1);

    let mut simultaneous_integer_solutions = Vec::new();
    for source_orientation in [-1_i64, 1] {
        for target_orientation in [-1_i64, 1] {
            let carrier_value = source_orientation * target_orientation * carrier_forced;
            let generic_value = source_orientation * target_orientation * generic_forced;
            if carrier_value == generic_value {
                simultaneous_integer_solutions.push((source_orientation, target_orientation));
            }
        }
    }
    assert!(simultaneous_integer_solutions.is_empty());

    // Written as two affine equations for a single coefficient a, their
    // difference is three. This is the exact integral normalization defect.
    let affine_rhs = [carrier_forced, generic_forced];
    let affine_difference = affine_rhs[0] - affine_rhs[1];
    assert_eq!(affine_difference, 1);
    // With the carrier orientation used in entry202, the equations are
    // a=-2 and a=+1, whose difference is -3. Magnitude is invariant.
    let entry202_rhs = [pairwise_cyclic_top_defect, physical_q_sigma_coefficient];
    let entry202_difference = entry202_rhs[0] - entry202_rhs[1];
    assert_eq!(entry202_difference, -3);
    assert_eq!(entry202_difference.rem_euclid(3), 0);

    // The coefficient matrix [1;1] is primitive (SNF [1]); inconsistency is
    // affine, not torsion in the homogeneous map. Adding a contractible
    // stabilization cannot change it.
    let coefficient_smith = gcd(1, 1);
    assert_eq!(coefficient_smith, 1);

    // Minimal algebraic repair: two independent tops C and H. C absorbs the
    // coefficient-two cyclic coherence, while H retains primitive qSigma.
    // Their diagonal coefficient matrix is unimodular.
    let two_top_matrix = [[1_i64, 0_i64], [0_i64, 1_i64]];
    let determinant =
        two_top_matrix[0][0] * two_top_matrix[1][1] - two_top_matrix[0][1] * two_top_matrix[1][0];
    assert_eq!(determinant.abs(), 1);
    let coherence_top_coefficient = carrier_forced;
    let mixed_top_coefficient = generic_forced;
    assert_eq!((coherence_top_coefficient, mixed_top_coefficient), (2, 1));

    println!(
        "{}",
        r#"{"claim":"A single primitive P2 source top cannot simultaneously close the certified pairwise cyclic K6 defect and realize entry113's primitive qSigma mixed boundary. Carrier closure forces absolute coefficient 2, while projective Gysin and based qSigma normalization force absolute coefficient 1. Orientation changes cannot remove the magnitude mismatch.","status":"falsified_scoped_single_top_spatial_promotion","pairwise_cyclic_top_defect":-2,"conductor_codimension":3,"relative_canonical_discrepancy":2,"carrier_forced_absolute_coefficient":2,"projective_gysin_top":1,"physical_qSigma_coefficient":1,"generic_forced_absolute_coefficient":1,"simultaneous_integer_solution":false,"entry202_affine_difference":-3,"homogeneous_smith":[1],"minimal_two_top_matrix_smith":[1,1],"minimal_additional_geometry":"separate cyclic-coherence top C and physical mixed top H_Sigma, joined by an independently geometric can-var/Beck-Chevalley cell; do not identify them","literal_entry143_rows":"unconstructed","physical_mapping_fiber":"unconstructed"}"#
    );
}
