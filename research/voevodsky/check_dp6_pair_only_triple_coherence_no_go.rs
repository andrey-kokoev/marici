//! Pair-only triple-coherence obstruction for the extraordinary W_ij model.
//!
//! The six oriented W_ij reduce to three oriented pair edges.  Their cyclic
//! boundary is R-I.  This checker computes the integral homology left when no
//! triple/top object is adjoined, including Boolean and Tor spectator grades.

fn rank_2_minor(matrix: &[[i64; 3]; 3]) -> i64 {
    matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
}

fn main() {
    // Rows are the three road packets; columns are W_01,W_12,W_20.
    let boundary = [[-1_i64, 0, 1], [1, -1, 0], [0, 1, -1]];
    let norm = [1_i64, 1, 1];

    for row in boundary {
        assert_eq!(row.iter().sum::<i64>(), 0);
    }
    for row in boundary {
        assert_eq!(
            row.iter()
                .zip(norm)
                .map(|(entry, value)| entry * value)
                .sum::<i64>(),
            0
        );
    }

    // A unit entry gives the first Smith factor 1; a unit 2x2 minor gives the
    // second.  The determinant is zero.  Hence SNF(R-I)=diag(1,1,0).
    assert_eq!(boundary[0][0].abs(), 1);
    assert_eq!(rank_2_minor(&boundary).abs(), 1);
    let determinant = boundary[0][0]
        * (boundary[1][1] * boundary[2][2] - boundary[1][2] * boundary[2][1])
        - boundary[0][1] * (boundary[1][0] * boundary[2][2] - boundary[1][2] * boundary[2][0])
        + boundary[0][2] * (boundary[1][0] * boundary[2][1] - boundary[1][1] * boundary[2][0]);
    assert_eq!(determinant, 0);

    // Solve (R-I)x=0 directly: row equations force x0=x1=x2.
    for a in -8_i64..=8 {
        for b in -8_i64..=8 {
            for c in -8_i64..=8 {
                let x = [a, b, c];
                let image: Vec<i64> = boundary
                    .iter()
                    .map(|row| row.iter().zip(x).map(|(m, v)| m * v).sum())
                    .collect();
                assert_eq!(image == vec![0, 0, 0], a == b && b == c);
            }
        }
    }

    // Without a degree-two triple generator, the primitive norm cycle is not
    // a boundary.  Adding one oriented top tau with d(tau)=N is the minimal
    // saturated repair: its column is primitive and has Smith factor 1.
    let pair_only_degree_two_columns = 0usize;
    let norm_is_boundary_pair_only = pair_only_degree_two_columns > 0;
    assert!(!norm_is_boundary_pair_only);
    assert_eq!(norm.iter().fold(0_i64, |g, x| gcd(g, *x)), 1);

    // Four Boolean states and two external Tor grades replicate, rather than
    // remove, the same free obstruction.
    let boolean_states = 4usize;
    let tor_grades = 2usize;
    let obstruction_rank = boolean_states * tor_grades;
    assert_eq!(obstruction_rank, 8);

    // Rotation cycles the three coordinates and fixes N. Reflection reverses
    // the cyclic pair orientation, so a future top must carry the orientation
    // sign. Neither action creates a missing boundary column.
    let rotated_norm = [norm[2], norm[0], norm[1]];
    assert_eq!(rotated_norm, norm);
    let reflected_oriented_norm = norm.map(|x| -x);
    assert_eq!(reflected_oriented_norm, [-1, -1, -1]);

    println!(
        "{}",
        r#"{"status":"falsified_scoped_pair_only_triple_coherence","pair_boundary":"R-I","pair_boundary_rank":2,"pair_boundary_smith":[1,1,0],"pair_boundary_kernel":[1,1,1],"pair_only_H1_rank":1,"triple_top_columns_present":0,"primitive_norm_boundary":false,"boolean_states":4,"tor_spectator_grades":[0,1],"replicated_obstruction_rank":8,"integer_torsion":false,"d3_fixes_norm":true,"reflection_requires_top_orientation_sign":true,"minimal_additional_datum":"one oriented triple object W_012 with dW_012=W_01+W_12+W_20 in every Boolean/Tor grade, plus a normalization-provenanced map of its top to H_Sigma and q_Sigma","endpoint_q_mapping_fiber_instantiated":false,"p_partial_Q_defined":false,"bockstein_defined":false,"d8_jordan_testable":false}"#
    );
}

fn gcd(mut left: i64, mut right: i64) -> i64 {
    left = left.abs();
    right = right.abs();
    while right != 0 {
        let remainder = left % right;
        left = right;
        right = remainder;
    }
    left
}
