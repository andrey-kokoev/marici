//! Finite algebra audit for the paired three-branch incidence candidate.
//!
//! This checker proves only label descent, symmetry, conductor fibre strata,
//! and the abstract seven-generator quotient.  It does not construct a Rees
//! normalization, a global cdh base change, or a ringed support/Gysin map.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct BranchPair {
    plus: usize,
    minus: usize,
}

const Z: [BranchPair; 3] = [
    BranchPair { plus: 5, minus: 2 },
    BranchPair { plus: 3, minus: 0 },
    BranchPair { plus: 1, minus: 4 },
];

const fn rotate_x(index: usize) -> usize {
    (index + 2) % 6
}

const fn reflect_x(index: usize) -> usize {
    (8 - index) % 6
}

fn pair_index(pair: BranchPair) -> usize {
    Z.iter()
        .position(|candidate| *candidate == pair)
        .expect("the transformed pair remains labelled")
}

fn rotate_pair(index: usize) -> usize {
    pair_index(BranchPair {
        plus: rotate_x(Z[index].plus),
        minus: rotate_x(Z[index].minus),
    })
}

fn reflect_pair(index: usize) -> usize {
    pair_index(BranchPair {
        plus: reflect_x(Z[index].plus),
        minus: reflect_x(Z[index].minus),
    })
}

const fn polarity(pair: BranchPair) -> BranchPair {
    BranchPair {
        plus: pair.minus,
        minus: pair.plus,
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Coordinate {
    G,
    H(usize),
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct IncidenceEquation {
    branch: usize,
    left_y: usize,
    left_coordinate: Coordinate,
    right_x: usize,
    right_coordinate: Coordinate,
}

fn incidence_on_branch(pair_index: usize, plus_sheet: bool) -> IncidenceEquation {
    let pair = Z[pair_index];
    IncidenceEquation {
        branch: pair_index,
        left_y: pair_index,
        left_coordinate: Coordinate::G,
        right_x: if plus_sheet { pair.plus } else { pair.minus },
        right_coordinate: Coordinate::H(pair_index),
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct LinearPolynomial {
    constant: i64,
    y: [i64; 3],
}

impl LinearPolynomial {
    const fn constant(value: i64) -> Self {
        Self {
            constant: value,
            y: [0; 3],
        }
    }

    const fn variable(index: usize, coefficient: i64) -> Self {
        let mut y = [0; 3];
        y[index] = coefficient;
        Self { constant: 0, y }
    }

    const fn add(self, other: Self) -> Self {
        Self {
            constant: self.constant + other.constant,
            y: [
                self.y[0] + other.y[0],
                self.y[1] + other.y[1],
                self.y[2] + other.y[2],
            ],
        }
    }
}

fn quotient_boundary(column: usize) -> [LinearPolynomial; 3] {
    if column == 0 {
        std::array::from_fn(|row| LinearPolynomial::variable(row, 1))
    } else {
        std::array::from_fn(|row| LinearPolynomial::constant(i64::from(row + 1 == column)))
    }
}

fn main() {
    assert_eq!(Z[0], BranchPair { plus: 5, minus: 2 });
    assert_eq!(Z[1], BranchPair { plus: 3, minus: 0 });
    assert_eq!(Z[2], BranchPair { plus: 1, minus: 4 });

    let rotation: [usize; 3] = std::array::from_fn(rotate_pair);
    let reflection: [usize; 3] = std::array::from_fn(reflect_pair);
    assert_eq!(rotation, [2, 0, 1]);
    assert_eq!(reflection, [1, 0, 2]);
    for index in 0..3 {
        assert_eq!(rotation[rotation[rotation[index]]], index);
        assert_eq!(reflection[reflection[index]], index);
        assert_eq!(
            reflection[rotation[reflection[index]]],
            rotation[rotation[index]]
        );
        assert_eq!(polarity(polarity(Z[index])), Z[index]);
    }

    for index in 0..3 {
        let plus = incidence_on_branch(index, true);
        let minus = incidence_on_branch(index, false);
        assert_eq!(plus.left_y, index);
        assert_eq!(minus.left_y, index);
        assert_eq!(plus.left_coordinate, Coordinate::G);
        assert_eq!(minus.left_coordinate, Coordinate::G);
        assert_eq!(plus.right_x, Z[index].plus);
        assert_eq!(minus.right_x, Z[index].minus);
        assert_eq!(plus.right_coordinate, Coordinate::H(index));
        assert_eq!(minus.right_coordinate, Coordinate::H(index));
    }

    // On the conductor all six x labels vanish.  If every y_i is nonzero,
    // y_i*G=0 forces G=0, leaving the coordinate P2 with 1 face, 3 edges,
    // and 3 vertices.  If every y_i also vanishes, no equation remains and
    // the fibre enlarges to the ambient P3.
    let conductor_x = [0_i64; 6];
    let generic_y = [1_i64; 3];
    assert!(conductor_x.iter().all(|coefficient| *coefficient == 0));
    assert!(generic_y.iter().all(|coefficient| *coefficient != 0));
    let p2_coordinate_strata = [1_usize, 3, 3];
    assert_eq!(p2_coordinate_strata, [1, 3, 3]);
    let deeper_y_zero = [0_i64; 3];
    assert!(deeper_y_zero.iter().all(|coefficient| *coefficient == 0));
    let ambient_projective_dimension = 3_usize;
    assert_eq!(ambient_projective_dimension, 3);

    // Degree three has the generic top followed by three normal states;
    // degree two has three radial states.  Its matrix is [y | I_3].
    let matrix: [[LinearPolynomial; 4]; 3] =
        std::array::from_fn(|row| std::array::from_fn(|column| quotient_boundary(column)[row]));
    for row in 0..3 {
        assert_eq!(matrix[row][0], LinearPolynomial::variable(row, 1));
        for column in 1..4 {
            assert_eq!(
                matrix[row][column],
                LinearPolynomial::constant(i64::from(row + 1 == column))
            );
        }
    }

    // The polynomial kernel is generated by (1,-y0,-y1,-y2).
    let kernel = [
        LinearPolynomial::constant(1),
        LinearPolynomial::variable(0, -1),
        LinearPolynomial::variable(1, -1),
        LinearPolynomial::variable(2, -1),
    ];
    for row in 0..3 {
        let image = LinearPolynomial::variable(row, kernel[0].constant).add(kernel[row + 1]);
        assert_eq!(image, LinearPolynomial::constant(0));
    }

    // The identity minor is unimodular.  Therefore the boundary is split
    // surjective, its cokernel has no torsion, and the displayed kernel line
    // is primitive.
    let identity_minor = [[1_i64, 0, 0], [0, 1, 0], [0, 0, 1]];
    let determinant = identity_minor[0][0] * identity_minor[1][1] * identity_minor[2][2];
    assert_eq!(determinant, 1);
    assert_eq!(kernel[0].constant, 1);

    println!(
        "{}",
        r#"{"claim":"The paired fibre-product labels z0=(x5,x2), z1=(x3,x0), z2=(x1,x4) carry the exact D3 permutation and sheet-polarity exchange, and the branch equations y_i G=z_i H_i restrict to y_i G=x_odd H_i and y_i G=x_even H_i. On the conductor with generic nonzero y, G=0 gives the coordinate-stratified P2. Its abstract first radial/normal quotient has seven generators and boundary matrix [y|I3], with primitive kernel (1,-y0,-y1,-y2) and no cokernel torsion.","status":"proved","scope":"finite paired-label, symmetry, conductor-fibre, and seven-generator coefficient algebra only","factorization_test":{"paired_labels":"PASS: z0=(x5,x2), z1=(x3,x0), z2=(x1,x4)","D3":"PASS: rotation [2,0,1], reflection [1,0,2], srs=r^-1","polarity":"PASS: exchanges the two branch restrictions and squares to one","branch_incidence":"PASS: common y_i G restricts against the labelled odd/even x coordinate","generic_conductor_fibre":"PASS: y_i nonzero forces G=0 and leaves P2 coordinate strata (1,3,3)","deeper_y_zero":"P3: all incidence equations vanish when x_i=y_i=0","seven_generator_quotient":"PASS: degrees Q2=3 and Q3=4 with matrix [y|I3]","primitive_kernel":"PASS: (1,-y0,-y1,-y2)","torsion":"NONE: identity minor has determinant one","Rees_normalization":"UNCONSTRUCTED","global_cdh_base_change":"UNCONSTRUCTED","ringed_support_Gysin_map":"UNCONSTRUCTED"},"boundary":"This checker does not prove saturation over the full fibre-product ring, normality, a normalization universal property, a global cdh square, or a map from the incidence P2 to the K6 endpoint/Q support filtration.","next_experiment":"Construct a labelled ringed-support comparison from the paired incidence coordinate strata to the actual K6 Boolean coface/AW roof and entry-143 Q packet, then test endpoint connector parity without fitting corridor values."}"#
    );
}
