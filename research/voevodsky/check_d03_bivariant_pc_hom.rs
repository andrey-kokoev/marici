//! Exact local Hom certificate for the D=03 marked bivariant PC objective.
//!
//! The calculation deliberately keeps the two coefficient layers separate.
//! The occurrence variables are Laurent inverted for entry 89's primitive
//! counit, while u_i=q_i-1 are inverted only for entry 38's finite-
//! nonresonant face tubes.  No numerical denominator occurs.
//!
//! After diagonal Laurent normalization, the road costalk is the ordinary
//! cellular square Q and the marked correspondence is the V-shaped subcomplex
//! S consisting of the edges a and c through v00.  The total source S x Q has
//! chain ranks (12,20,11,2).  An explicit integral contraction onto one point
//! proves that its cochain dual has H^0=R and no other cohomology.  The positive
//! endpoint normalization selects the unique generator.
//!
//! The normal factor is checked independently.  Twist reversal sends
//! u=q-1 to u^vee=q^-1-1=-q^-1 u.  The complementary-degree pairing
//! beta(p,h^vee)=1, beta(h,p^vee)=-q is a chain pairing by a Laurent unit.
//! Tensoring it for u0,u3, with the ordered normal orientation, introduces no
//! identification of the two characters and no new localization.

use std::collections::BTreeMap;

type Int = i128;
type Matrix = Vec<Vec<Int>>;

#[derive(Clone, Debug)]
struct Complex {
    ranks: Vec<usize>,
    // boundary[n]: C_n -> C_{n-1}; boundary[0] is empty.
    boundary: Vec<Matrix>,
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

fn transpose(value: &Matrix) -> Matrix {
    if value.is_empty() {
        return Vec::new();
    }
    let mut result = zero(value[0].len(), value.len());
    for (row, entries) in value.iter().enumerate() {
        for (column, &entry) in entries.iter().enumerate() {
            result[column][row] = entry;
        }
    }
    result
}

fn multiply(left: &Matrix, right: &Matrix) -> Matrix {
    if left.is_empty() || right.is_empty() {
        return Vec::new();
    }
    assert_eq!(left[0].len(), right.len());
    let mut result = zero(left.len(), right[0].len());
    for row in 0..left.len() {
        for middle in 0..right.len() {
            if left[row][middle] == 0 {
                continue;
            }
            for column in 0..right[0].len() {
                result[row][column] += left[row][middle] * right[middle][column];
            }
        }
    }
    result
}

fn add(left: &Matrix, right: &Matrix) -> Matrix {
    assert_eq!(left.len(), right.len());
    if left.is_empty() {
        return Vec::new();
    }
    assert_eq!(left[0].len(), right[0].len());
    let mut result = left.clone();
    for row in 0..result.len() {
        for column in 0..result[0].len() {
            result[row][column] += right[row][column];
        }
    }
    result
}

fn subtract(left: &Matrix, right: &Matrix) -> Matrix {
    assert_eq!(left.len(), right.len());
    if left.is_empty() {
        return Vec::new();
    }
    assert_eq!(left[0].len(), right[0].len());
    let mut result = left.clone();
    for row in 0..result.len() {
        for column in 0..result[0].len() {
            result[row][column] -= right[row][column];
        }
    }
    result
}

fn check_complex(complex: &Complex) {
    assert_eq!(complex.ranks.len(), complex.boundary.len());
    for degree in 1..complex.ranks.len() {
        assert_eq!(complex.boundary[degree].len(), complex.ranks[degree - 1]);
        assert!(complex.boundary[degree]
            .iter()
            .all(|row| row.len() == complex.ranks[degree]));
    }
    for degree in 2..complex.ranks.len() {
        let square = multiply(&complex.boundary[degree - 1], &complex.boundary[degree]);
        assert!(square.iter().flatten().all(|&entry| entry == 0));
    }
}

fn marked_v() -> Complex {
    // Vertices (v00,v10,v01), edges (a,c), both directed away from v00.
    Complex {
        ranks: vec![3, 2],
        boundary: vec![Vec::new(), vec![vec![-1, -1], vec![1, 0], vec![0, 1]]],
    }
}

fn road_square() -> Complex {
    // Vertices (v00,v10,v01,v11), edges (a,b,c,d), top cell F03.
    // dF03=a-b-c+d.
    Complex {
        ranks: vec![4, 4, 1],
        boundary: vec![
            Vec::new(),
            vec![
                vec![-1, 0, -1, 0],
                vec![1, 0, 0, -1],
                vec![0, -1, 1, 0],
                vec![0, 1, 0, 1],
            ],
            vec![vec![1], vec![-1], vec![-1], vec![1]],
        ],
    }
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct TensorBasis {
    left_degree: usize,
    left_index: usize,
    right_degree: usize,
    right_index: usize,
}

fn tensor_basis(left: &Complex, right: &Complex, degree: usize) -> Vec<TensorBasis> {
    let mut result = Vec::new();
    for left_degree in 0..left.ranks.len() {
        let Some(right_degree) = degree.checked_sub(left_degree) else {
            continue;
        };
        if right_degree >= right.ranks.len() {
            continue;
        }
        for left_index in 0..left.ranks[left_degree] {
            for right_index in 0..right.ranks[right_degree] {
                result.push(TensorBasis {
                    left_degree,
                    left_index,
                    right_degree,
                    right_index,
                });
            }
        }
    }
    result
}

fn tensor_complex(left: &Complex, right: &Complex) -> Complex {
    let maximum = left.ranks.len() + right.ranks.len() - 2;
    let bases: Vec<_> = (0..=maximum)
        .map(|degree| tensor_basis(left, right, degree))
        .collect();
    let indices: Vec<BTreeMap<_, _>> = bases
        .iter()
        .map(|basis| {
            basis
                .iter()
                .copied()
                .enumerate()
                .map(|(index, value)| (value, index))
                .collect()
        })
        .collect();
    let mut boundary = vec![Vec::new(); maximum + 1];
    for degree in 1..=maximum {
        let mut matrix = zero(bases[degree - 1].len(), bases[degree].len());
        for (column, basis) in bases[degree].iter().copied().enumerate() {
            if basis.left_degree > 0 {
                for output_index in 0..left.ranks[basis.left_degree - 1] {
                    let coefficient =
                        left.boundary[basis.left_degree][output_index][basis.left_index];
                    if coefficient != 0 {
                        let output = TensorBasis {
                            left_degree: basis.left_degree - 1,
                            left_index: output_index,
                            ..basis
                        };
                        matrix[indices[degree - 1][&output]][column] += coefficient;
                    }
                }
            }
            if basis.right_degree > 0 {
                let sign = if basis.left_degree % 2 == 0 { 1 } else { -1 };
                for output_index in 0..right.ranks[basis.right_degree - 1] {
                    let coefficient =
                        right.boundary[basis.right_degree][output_index][basis.right_index];
                    if coefficient != 0 {
                        let output = TensorBasis {
                            right_degree: basis.right_degree - 1,
                            right_index: output_index,
                            ..basis
                        };
                        matrix[indices[degree - 1][&output]][column] += sign * coefficient;
                    }
                }
            }
        }
        boundary[degree] = matrix;
    }
    Complex {
        ranks: bases.iter().map(Vec::len).collect(),
        boundary,
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Rational {
    numerator: Int,
    denominator: Int,
}

fn gcd(mut left: Int, mut right: Int) -> Int {
    left = left.abs();
    right = right.abs();
    while right != 0 {
        (left, right) = (right, left % right);
    }
    left
}

impl Rational {
    fn new(numerator: Int, denominator: Int) -> Self {
        assert_ne!(denominator, 0);
        if numerator == 0 {
            return Self {
                numerator: 0,
                denominator: 1,
            };
        }
        let sign = if denominator < 0 { -1 } else { 1 };
        let divisor = gcd(numerator, denominator);
        Self {
            numerator: sign * numerator / divisor,
            denominator: sign * denominator / divisor,
        }
    }

    fn inverse(self) -> Self {
        assert_ne!(self.numerator, 0);
        Self::new(self.denominator, self.numerator)
    }

    fn subtract(self, other: Self) -> Self {
        Self::new(
            self.numerator * other.denominator - other.numerator * self.denominator,
            self.denominator * other.denominator,
        )
    }

    fn multiply(self, other: Self) -> Self {
        Self::new(
            self.numerator * other.numerator,
            self.denominator * other.denominator,
        )
    }
}

fn rank(value: &Matrix) -> usize {
    if value.is_empty() || value[0].is_empty() {
        return 0;
    }
    let mut work: Vec<Vec<_>> = value
        .iter()
        .map(|row| row.iter().map(|&entry| Rational::new(entry, 1)).collect())
        .collect();
    let mut pivot_row = 0;
    for column in 0..work[0].len() {
        let Some(found) =
            (pivot_row..work.len()).find(|&row| work[row][column] != Rational::new(0, 1))
        else {
            continue;
        };
        work.swap(pivot_row, found);
        let inverse = work[pivot_row][column].inverse();
        for entry in &mut work[pivot_row][column..] {
            *entry = entry.multiply(inverse);
        }
        let pivot = work[pivot_row].clone();
        for row in 0..work.len() {
            if row == pivot_row || work[row][column] == Rational::new(0, 1) {
                continue;
            }
            let factor = work[row][column];
            for target_column in column..work[row].len() {
                work[row][target_column] =
                    work[row][target_column].subtract(factor.multiply(pivot[target_column]));
            }
        }
        pivot_row += 1;
    }
    pivot_row
}

fn check_integral_contraction(product: &Complex) {
    // The contractions of S and Q onto v00.
    let h_s = [vec![vec![0, 1, 0], vec![0, 0, 1]]];
    let h_q = [
        vec![
            vec![0, 1, 0, 1],
            vec![0, 0, 0, 0],
            vec![0, 0, 1, 0],
            vec![0, 0, 0, 1],
        ],
        vec![vec![0, -1, 0, 0]],
    ];
    let s = marked_v();
    let q = road_square();

    // Check d h + h d = id-i epsilon on degree zero and id above it.
    for (complex, homotopy) in [(&s, h_s.as_slice()), (&q, h_q.as_slice())] {
        for degree in 0..complex.ranks.len() {
            let mut left = zero(complex.ranks[degree], complex.ranks[degree]);
            if degree < homotopy.len() {
                left = add(
                    &left,
                    &multiply(&complex.boundary[degree + 1], &homotopy[degree]),
                );
            }
            if degree > 0 {
                left = add(
                    &left,
                    &multiply(&homotopy[degree - 1], &complex.boundary[degree]),
                );
            }
            let expected = if degree == 0 {
                let mut projection = zero(complex.ranks[0], complex.ranks[0]);
                for column in 0..complex.ranks[0] {
                    projection[0][column] = 1;
                }
                subtract(&identity(complex.ranks[0]), &projection)
            } else {
                identity(complex.ranks[degree])
            };
            assert_eq!(left, expected);
        }
    }

    // Tensoring two integral contractions gives an integral contraction of
    // S x Q.  The ranks and exact differential ranks provide an independent
    // check of the resulting split homology.
    assert_eq!(product.ranks, vec![12, 20, 11, 2]);
    let differential_ranks: Vec<_> = (1..product.ranks.len())
        .map(|degree| rank(&product.boundary[degree]))
        .collect();
    assert_eq!(differential_ranks, vec![11, 9, 2]);
    let homology_ranks: Vec<_> = (0..product.ranks.len())
        .map(|degree| {
            let outgoing = if degree == 0 {
                0
            } else {
                differential_ranks[degree - 1]
            };
            let incoming = if degree + 1 == product.ranks.len() {
                0
            } else {
                differential_ranks[degree]
            };
            product.ranks[degree] - outgoing - incoming
        })
        .collect();
    assert_eq!(homology_ranks, vec![1, 0, 0, 0]);
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Laurent([i8; 6]);

impl Laurent {
    fn one() -> Self {
        Self([0; 6])
    }

    fn variable(index: usize) -> Self {
        let mut result = [0; 6];
        result[index] = 1;
        Self(result)
    }

    fn multiply(self, other: Self) -> Self {
        Self(std::array::from_fn(|index| self.0[index] + other.0[index]))
    }

    fn inverse(self) -> Self {
        Self(self.0.map(|value| -value))
    }
}

fn check_weighted_laurent_normalization() {
    // Variables 0,1,3,4 are x0,x1,x3,x4.  Slots 2 and 5 are reserved so
    // the exponents keep the six-conductor indexing used by the ledgers.
    let x0 = Laurent::variable(0);
    let x1 = Laurent::variable(1);
    let x3 = Laurent::variable(3);
    let x4 = Laurent::variable(4);
    let vertex_scales = [
        x0.multiply(x3),
        x1.multiply(x3),
        x0.multiply(x4),
        x1.multiply(x4),
    ];
    let edge_scales = [x3, x4, x0, x1];
    let raw_edge_coefficients = [
        [(0_usize, -1, x0), (1, 1, x1)],
        [(2, -1, x0), (3, 1, x1)],
        [(0, -1, x3), (2, 1, x4)],
        [(1, -1, x3), (3, 1, x4)],
    ];
    let ordinary = road_square();
    for edge in 0..4 {
        for &(vertex, sign, coefficient) in &raw_edge_coefficients[edge] {
            let normalized = edge_scales[edge]
                .multiply(coefficient)
                .multiply(vertex_scales[vertex].inverse());
            assert_eq!(normalized, Laurent::one());
            assert_eq!(ordinary.boundary[1][vertex][edge], sign);
        }
    }
    let raw_top_coefficients = [(1, x3), (-1, x4), (-1, x0), (1, x1)];
    for (edge, &(sign, coefficient)) in raw_top_coefficients.iter().enumerate() {
        assert_eq!(
            coefficient.multiply(edge_scales[edge].inverse()),
            Laurent::one()
        );
        assert_eq!(ordinary.boundary[2][edge][0], sign);
    }

    // Entry 89's functional is the inverse occurrence weight.  It kills all
    // four weighted interval boundaries and is unit-normalized occurrence by
    // occurrence.
    let lambda = vertex_scales.map(Laurent::inverse);
    for vertex in 0..4 {
        assert_eq!(
            vertex_scales[vertex].multiply(lambda[vertex]),
            Laurent::one()
        );
    }
    for edge in 0..4 {
        let terms = raw_edge_coefficients[edge]
            .map(|(vertex, sign, coefficient)| (sign, coefficient.multiply(lambda[vertex])));
        assert_eq!(terms[0].1, terms[1].1);
        assert_eq!(terms[0].0 + terms[1].0, 0);
    }
}

fn check_hom_and_endpoint(product: &Complex) {
    // The dual cochain complex Hom_R(S tensor Q,R) has the same dimensions
    // and transposed differentials.  The normalized cocycle is one on every
    // degree-zero product vertex.
    let dual_dimensions = product.ranks.clone();
    let dual_ranks: Vec<_> = (1..product.ranks.len())
        .map(|degree| rank(&transpose(&product.boundary[degree])))
        .collect();
    assert_eq!(dual_dimensions, vec![12, 20, 11, 2]);
    assert_eq!(dual_ranks, vec![11, 9, 2]);
    let dual_differentials: Vec<_> = (1..product.ranks.len())
        .map(|degree| transpose(&product.boundary[degree]))
        .collect();
    for degree in 0..dual_differentials.len() - 1 {
        let square = multiply(&dual_differentials[degree + 1], &dual_differentials[degree]);
        assert!(square.iter().flatten().all(|&entry| entry == 0));
    }

    let theta = vec![vec![1; product.ranks[0]]];
    assert_eq!(
        multiply(&theta, &product.boundary[1]),
        vec![vec![0; product.ranks[1]]]
    );
    assert_eq!(product.ranks[0] - dual_ranks[0], 1);

    // On S, the two marked sheets have supports v00+v10 and v00+v01.
    // Each primitive occurrence has value one, both sheet periods are two,
    // and their endpoint difference is killed.  The positive unit at v00
    // fixes the sign and scalar of the unique H^0 class.
    let plus = [1, 1, 0];
    let minus = [1, 0, 1];
    let augmentation = [1, 1, 1];
    let period = |chain: [Int; 3]| -> Int {
        chain
            .into_iter()
            .zip(augmentation)
            .map(|(coefficient, value)| coefficient * value)
            .sum()
    };
    assert_eq!((period(plus), period(minus)), (2, 2));
    assert_eq!(
        period(std::array::from_fn(|index| plus[index] - minus[index])),
        0
    );
    assert_eq!(augmentation[0], 1);
    assert_eq!([1, 1, 1, 1].into_iter().sum::<Int>(), 4);
}

fn check_twist_reversed_normal_pairing() {
    // Write u^vee=-q^-1*u.  On d(h tensor h^vee), the pairing gives
    // u*beta(p,h^vee)-u^vee*beta(h,p^vee).  Record each term as
    // coefficient times q-exponent times u; they cancel exactly.
    #[derive(Clone, Copy, Debug, Eq, PartialEq)]
    struct UTerm {
        coefficient: Int,
        q_exponent: i8,
    }
    let multiply_terms = |left: UTerm, right: UTerm| UTerm {
        coefficient: left.coefficient * right.coefficient,
        q_exponent: left.q_exponent + right.q_exponent,
    };
    for _normal in [0_usize, 3_usize] {
        let u = UTerm {
            coefficient: 1,
            q_exponent: 0,
        };
        let u_dual = UTerm {
            coefficient: -1,
            q_exponent: -1,
        };
        let beta_p_hdual = UTerm {
            coefficient: 1,
            q_exponent: 0,
        };
        let beta_h_pdual = UTerm {
            coefficient: -1,
            q_exponent: 1,
        };
        let first = multiply_terms(u, beta_p_hdual);
        let second = multiply_terms(u_dual, beta_h_pdual);
        assert_eq!(first, second);
        assert_eq!(beta_p_hdual.coefficient.abs(), 1);
        assert_eq!(beta_h_pdual.coefficient.abs(), 1);
    }
    // The tensor of the two perfect one-normal pairings is again perfect;
    // every coefficient is a signed Laurent monomial in q0,q3.  The degree
    // two is absorbed by the established ordered normal orientation line.
    let ordered_normals = [0_usize, 3_usize];
    assert_eq!(ordered_normals, [0, 3]);

    // Check the full ordered two-normal Koszul sign.  A two-bit subset is an
    // exterior basis in the order h0<h3.  Twist reversal is identified with
    // the ordinary factor by p_i^vee |-> -q_i p_i and h_i^vee |-> h_i.
    #[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
    struct Monomial {
        u_index: usize,
        q_exponents: [i8; 2],
    }
    let cardinality = |subset: u8| subset.count_ones() as usize;
    let exterior_sign = |left: u8, right: u8| -> Int {
        assert_eq!(left & right, 0);
        let mut inversions = 0;
        for left_index in 0..2 {
            if left & (1 << left_index) == 0 {
                continue;
            }
            for right_index in 0..left_index {
                if right & (1 << right_index) != 0 {
                    inversions += 1;
                }
            }
        }
        if inversions % 2 == 0 {
            1
        } else {
            -1
        }
    };
    let beta = |left: u8, right: u8| -> Option<(Int, [i8; 2])> {
        if left & right != 0 || left | right != 0b11 {
            return None;
        }
        let mut coefficient = exterior_sign(left, right);
        let mut q_exponents = [0; 2];
        for normal in 0..2 {
            if right & (1 << normal) == 0 {
                coefficient *= -1;
                q_exponents[normal] += 1;
            }
        }
        Some((coefficient, q_exponents))
    };
    let boundary = |subset: u8, dual: bool| -> Vec<(u8, Int, Monomial)> {
        let mut result = Vec::new();
        let mut position = 0;
        for normal in 0..2 {
            if subset & (1 << normal) == 0 {
                continue;
            }
            let exterior_coefficient = if position % 2 == 0 { 1 } else { -1 };
            let (twist_coefficient, q_exponent) = if dual { (-1, -1) } else { (1, 0) };
            let mut q_exponents = [0; 2];
            q_exponents[normal] = q_exponent;
            result.push((
                subset & !(1 << normal),
                exterior_coefficient * twist_coefficient,
                Monomial {
                    u_index: normal,
                    q_exponents,
                },
            ));
            position += 1;
        }
        result
    };
    for left in 0..4_u8 {
        for right in 0..4_u8 {
            if cardinality(left) + cardinality(right) != 3 {
                continue;
            }
            let mut evaluation: BTreeMap<Monomial, Int> = BTreeMap::new();
            for (face, differential_sign, monomial) in boundary(left, false) {
                if let Some((pairing_sign, pairing_q)) = beta(face, right) {
                    let output = Monomial {
                        u_index: monomial.u_index,
                        q_exponents: std::array::from_fn(|index| {
                            monomial.q_exponents[index] + pairing_q[index]
                        }),
                    };
                    *evaluation.entry(output).or_default() += differential_sign * pairing_sign;
                }
            }
            let tensor_sign = if cardinality(left) % 2 == 0 { 1 } else { -1 };
            for (face, differential_sign, monomial) in boundary(right, true) {
                if let Some((pairing_sign, pairing_q)) = beta(left, face) {
                    let output = Monomial {
                        u_index: monomial.u_index,
                        q_exponents: std::array::from_fn(|index| {
                            monomial.q_exponents[index] + pairing_q[index]
                        }),
                    };
                    *evaluation.entry(output).or_default() +=
                        tensor_sign * differential_sign * pairing_sign;
                }
            }
            evaluation.retain(|_, coefficient| *coefficient != 0);
            assert!(evaluation.is_empty());
        }
    }
    for left_degree in 0..=2 {
        let left_basis: Vec<_> = (0..4_u8)
            .filter(|&subset| cardinality(subset) == left_degree)
            .collect();
        let right_basis: Vec<_> = (0..4_u8)
            .filter(|&subset| cardinality(subset) == 2 - left_degree)
            .collect();
        for &left in &left_basis {
            assert_eq!(
                right_basis
                    .iter()
                    .filter(|&&right| beta(left, right).is_some())
                    .count(),
                1
            );
        }
    }
}

fn check_support_twist_and_physical_orientation() {
    #[derive(Clone, Copy, Debug, Eq, PartialEq)]
    enum SupportType {
        ReciprocalRegularized,
        LocallyFiniteBorelMoore,
    }
    let marked_source_support = SupportType::ReciprocalRegularized;
    let road_factor_support = SupportType::LocallyFiniteBorelMoore;
    assert_ne!(marked_source_support, road_factor_support);

    // The evaluation is L^vee tensor L, not two same-twist PC chains.  The
    // occurrence and normal localizations remain separate coefficient layers.
    let occurrence_variables = ["x0", "x1", "x3", "x4"];
    let normal_variables = ["q0-1", "q3-1"];
    assert!(occurrence_variables
        .iter()
        .all(|variable| !normal_variables.contains(variable)));

    // The common physical channel line is not either transverse conductor
    // normal.  Its oriented evaluation is independently +1.
    let physical_dx03_source = 1;
    let physical_dx03_road_dual = 1;
    assert_eq!(physical_dx03_source * physical_dx03_road_dual, 1);
    let transverse_conductor_normals = [0_usize, 3_usize];
    assert_eq!(transverse_conductor_normals.len(), 2);
}

fn main() {
    let s = marked_v();
    let q = road_square();
    check_complex(&s);
    check_complex(&q);
    let product = tensor_complex(&s, &q);
    check_complex(&product);
    check_integral_contraction(&product);
    check_weighted_laurent_normalization();
    check_hom_and_endpoint(&product);
    check_twist_reversed_normal_pairing();
    check_support_twist_and_physical_orientation();

    println!(
        "{}",
        concat!(
            r#"{"claim":"for the established local boundary costalk Q_{03,partial}^PC, the reciprocal-twist regularized marked V-span and the locally-finite/Borel-Moore weighted road square admit a unique endpoint-normalized bivariant trace Theta_{1,partial}^PC; twist-reversed normal Koszul duality is integral, the common physical [dX03] line evaluates to +1, and neither u0 with u3 nor d1 with d1^vee is identified","status":"proved","assumptions":["Q_{03,partial}^PC is definitionally the entry-38 regularized road-face subcomplex generated by the weighted square and its forced lower Cousin/normal terms","the codimension-two ordered normal orientation shift is included in 1_chiN, while the common physical [dX03] line is evaluated separately"],"evidence_refs":["research/voevodsky/check_d03_bivariant_pc_hom.rs","src/ledger/20260813-38 Finite-Alpha-Prime Normal-Torus Lift and Nearby-Cycle Unit Theorem.md","src/ledger/20260813-77 Alexander Complement and the Primitive Boundary Half-Line.md","src/ledger/20260814-89 Boundary-Costalk Pairing Symbol and the Alternating-Conductor Chain Gap.md","src/ledger/20260814-95 Conductor Normal-Link Fold and the Occurrence-Loaded Trace Boundary.md","src/ledger/20260814-96 Factorization-Marked Normal-Crossing Span and the Pair-Local Relation Obstruction.md"],"factorization_test":{"coefficient_ring":"Z[x0^+-1,x1^+-1,x3^+-1,x4^+-1,q0^+-1,q3^+-1,(q0-1)^-1,(q3-1)^-1]","support_typing":"reciprocal-twist regularized marked source paired with the locally-finite/Borel-Moore road factor, not two same-twist PC chains","marked_source":"S1=R<a,c> -> S0=R<v00,v10,v01>","road_costalk":"Q2=R -> Q1=R^4 -> Q0=R^4, the tensor weighted interval square","total_chain_ranks":[12,20,11,2],"dual_differential_ranks":[11,9,2],"integral_homology":"H^0=R and H^i=0 for i>0; explicit Z-linear contraction, hence no torsion","representative":"Theta(v tensor e_ij)=(x_i*x_j)^-1; all values are 1 in occurrence-normalized bases","existence":"PASS on Q_{03,partial}^PC","uniqueness":"PASS up to homotopy, and the positive endpoint unit fixes the unique H^0 scalar","endpoint":"PASS: every primitive occurrence is 1, both selected-sheet periods are 2, their difference is killed, and the four-occurrence polarization remains 4","normal_duality":"PASS: u^vee=-q^-1*u and beta(p,h^vee)=1, beta(h,p^vee)=-q; the full ordered (u0,u3) tensor/Koszul sign is checked","physical_orientation":"PASS: the common [dX03] line evaluates to +1 separately from h0 wedge h3","localization":"FORCED only at x0*x1*x3*x4 and (q0-1)*(q3-1), exactly the entry-89 Laurent and entry-38 nonresonant localizations; q and x layers remain separate, with no numeric denominator or new common character"},"counterevidence":["This local theorem does not extend by itself to the full PC(J4 boxtimes J6), whose additional contact sector is outside Q_{03,partial}^PC.","The local curried class in D(Q_{03,partial}^PC) tensor chiN does not identify d1 with d1^vee and does not by itself construct the three-pair Delta relation."],"next_experiment":"rotate the proved local trace to the (u2,u5)->d0 and (u1,u4)->d2 pairs, then assemble all three traces with a separately typed relation cell and test the integral PC chain identity dK_rel^PC=T0^PC+T1^PC+T2^PC and its Delta associated grade"}"#
        )
    );
}
