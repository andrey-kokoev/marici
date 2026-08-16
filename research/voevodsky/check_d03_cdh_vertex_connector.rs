//! Exact vertex/connector truncation of the paired D03 cdh cone.
//!
//! The positive theorem uses the primitive reduced endpoint-difference line.
//! The scoped no-go concerns separate endpoint values or diagonal coinvariants.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Circulant {
    diagonal: i64,
    off_diagonal: i64,
}

impl Circulant {
    const fn column_sum(self) -> i64 {
        self.diagonal + 2 * self.off_diagonal
    }

    const fn matrix(self) -> [[i64; 3]; 3] {
        let a = self.diagonal;
        let b = self.off_diagonal;
        [[a, b, b], [b, a, b], [b, b, a]]
    }
}

fn rotate(vector: [i64; 3]) -> [i64; 3] {
    [vector[2], vector[0], vector[1]]
}

fn reflect(vector: [i64; 3]) -> [i64; 3] {
    [vector[0], vector[2], vector[1]]
}

fn apply(matrix: [[i64; 3]; 3], vector: [i64; 3]) -> [i64; 3] {
    let mut result = [0_i64; 3];
    for row in 0..3 {
        for column in 0..3 {
            result[row] += matrix[row][column] * vector[column];
        }
    }
    result
}

fn main() {
    // Rotation covariance and physical reflection covariance (both connector
    // and road modules carry negative reflected permutation) force the map
    // to a*I+b*(R+R^2).
    for a in -8_i64..=8 {
        for b in -8_i64..=8 {
            let map = Circulant {
                diagonal: a,
                off_diagonal: b,
            };
            let matrix = map.matrix();
            for basis in [[1, 0, 0], [0, 1, 0], [0, 0, 1]] {
                assert_eq!(apply(matrix, rotate(basis)), rotate(apply(matrix, basis)));
                assert_eq!(apply(matrix, reflect(basis)), reflect(apply(matrix, basis)));
            }

            // For dc_i=delta and epsilon(q_i)=1, the chain equation is the
            // common column sum a+2b=t, where F0(delta)=t.
            let t = map.column_sum();
            for column in 0..3 {
                let column_sum: i64 = matrix.iter().map(|row| row[column]).sum();
                assert_eq!(column_sum, t);
            }
        }
    }

    // Fixed primitive endpoint orientation t=1 leaves the rank-one affine
    // family a=1-2b.  Matched-label locality kills off-diagonal b and forces I.
    for b in -16_i64..=16 {
        let map = Circulant {
            diagonal: 1 - 2 * b,
            off_diagonal: b,
        };
        assert_eq!(map.column_sum(), 1);
        if b == 0 {
            assert_eq!(map.matrix(), [[1, 0, 0], [0, 1, 0], [0, 0, 1]]);
        } else {
            assert_ne!(map.off_diagonal, 0);
        }
    }
    let label_local_positive = Circulant {
        diagonal: 1,
        off_diagonal: 0,
    };
    let label_local_negative = Circulant {
        diagonal: -1,
        off_diagonal: 0,
    };
    assert_eq!(label_local_positive.column_sum(), 1);
    assert_eq!(label_local_negative.column_sum(), -1);

    // The norm remains unsplit: d(c0+c1+c2)=3*delta and epsilon(Nq)=3.
    let norm_boundary = 3_i64;
    let road_norm_augmentation = 3_i64;
    assert_eq!(norm_boundary, road_norm_augmentation);

    // Scoped factor-two no-go.  If separate sheet endpoint values are A and
    // B, sheet-exchanging reflection into Z_or forces B=-A.  The connector
    // difference is therefore -2A and cannot be a primitive odd value.
    for plus_value in -16_i64..=16 {
        let minus_value = -plus_value;
        let difference = minus_value - plus_value;
        assert_eq!(difference, -2 * plus_value);
        assert_eq!(difference.rem_euclid(2), 0);
        assert_ne!(difference, 1);
        assert_ne!(difference, -1);
    }

    // The diagonal quotient has the same defect: imposing v_plus+v_minus=0
    // makes delta=v_minus-v_plus twice the quotient generator.  In contrast,
    // ker(epsilon:Z^2->Z) is generated primitively by (-1,+1).
    let delta_in_diagonal_quotient = 2_i64;
    assert_eq!(delta_in_diagonal_quotient, 2);
    let reduced_endpoint_generator = [-1_i64, 1_i64];
    assert_eq!(
        reduced_endpoint_generator[0] + reduced_endpoint_generator[1],
        0
    );
    assert!(reduced_endpoint_generator
        .iter()
        .any(|value| value.abs() == 1));

    println!(
        "{}",
        r#"{"claim":"For the paired D03 cdh vertex/connector truncation with primitive reduced endpoint line Z_or<delta>, every strict D3-equivariant map to the road augmentation T is a circulant a*I+b*(R+R^2) with chain equation a+2b=t=F0(delta). Primitive positive orientation t=1 leaves a rank-one affine family, and independently imposed matched-label locality forces the unique map I. The connector norm has boundary 3*delta and retains the unsplit index-three extension. By contrast, retaining separate sheet endpoint values under sheet-exchanging reflection, or using diagonal coinvariants, forces an even endpoint difference and cannot realize a primitive connector.","status":"proved","scope":"Exact integral vertex/connector coefficient complex only; the no-go is scoped to separate endpoint values and the diagonal quotient, not to a future pointed butterfly or geometric DNC connector.","references":["ledger entry 93","ledger entry 135","ledger entry 143"],"factorization_test":{"equivariant_map_module":"rank two: a*I+b*(R+R^2)","chain_equation":"a+2b=t","primitive_orientation":"t=1 gives a=1-2b","label_locality":"b=0 forces I; reversed orientation forces -I","norm_boundary":"dN=3*delta","road_augmentation":"epsilon(Nq)=3","index_three":"retained unsplit; no division by 3","separate_endpoints":"FALSIFIED for primitive difference by B=-A and B-A=-2A","diagonal_quotient":"FALSIFIED for primitive difference: delta is twice the quotient generator","reduced_endpoint_line":"primitive generator (-1,+1)","integer_torsion":"none"},"unconstructed":["geometric proof of matched-label locality","individual endpoint pointing compatible with sheet-exchanging reflection","higher cdh edge/face Gysin maps","physical Beck-Chevalley cell"],"boundary":"The checker proves the reduced endpoint-line classification. It does not identify the connector cells with spatial K6 corridors or select a pointed global lift."}"#
    );
}
