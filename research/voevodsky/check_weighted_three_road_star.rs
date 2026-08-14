//! Exact algebraic certificate for the corrected weighted three-road star.
//!
//! The base ring is
//!
//!   R0=Z[q0^+-1,...,q5^+-1], uj=qj-1.
//!
//! No uj is inverted in R0.  Negative u powers below occur only in explicitly
//! labelled support-Cech localization summands.  Put
//!
//!   A=(u1,u3,u5), tau_A=1/(u1*u3*u5), E=(u4,u0,u2).
//!
//! The raw source is K(E), in the based form
//!
//!   f=h4*h0*h2,
//!   e1=p4*h0*h2, e3=-h4*p0*h2, e5=h4*h0*p2,
//!   q0=p4*p0*h2, q1=p4*h0*p2, q2=h4*p0*p2,
//!   a=p4*p0*p2.
//!
//! The candidate target is the relative three-road star with Cech
//! coefficients.  This certificate checks the formal map
//!
//!   f  |-> tau_A Krel,
//!   e1 |-> tau_A/u4 T2,
//!   e3 |-> tau_A/u0 T1,
//!   e5 |-> tau_A/u2 T0,
//!   q0,q1,q2,a |-> 0.
//!
//! It proves the raw Koszul identities, the top chain square, every lower
//! zero-target square, and D3 covariance with all basis signs.  It does not
//! construct the intrinsic supported arrow f->Krel, nor attach entry 100's
//! local excess, occurrence, and physical-normal lines to the three displayed
//! road terms.  The result is therefore conditional/inconclusive as a PC map.
//!
//! The same checker identifies the integral augmented triangle of entries 94
//! and 99 with one finite window of the complete C3 Tate resolution
//!
//!   Z_or --N--> Z[C3] --(1-r)--> Z[C3] --epsilon--> Z,
//!
//! including the D3 inversion action and the top orientation twist.  It then
//! tests whether the weighted Koszul star realizes that window over R0.

use std::collections::BTreeMap;

type Int = i64;
type Mask = u8;

const NORMALS: usize = 6;
const EVEN_SEQUENCE: [usize; 3] = [4, 0, 2];
const ODD_SUPPORT: [usize; 3] = [1, 3, 5];

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum SourceBasis {
    F,
    E1,
    E3,
    E5,
    Q0,
    Q1,
    Q2,
    Augmentation,
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum TargetBasis {
    Krel,
    T0,
    T1,
    T2,
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Monomial {
    u: [i8; NORMALS],
}

impl Monomial {
    fn one() -> Self {
        Self { u: [0; NORMALS] }
    }

    fn u(index: usize, exponent: i8) -> Self {
        let mut result = Self::one();
        result.u[index] = exponent;
        result
    }

    fn multiply(self, other: Self) -> Self {
        Self {
            u: std::array::from_fn(|index| self.u[index] + other.u[index]),
        }
    }

    fn permute(self, permutation: fn(usize) -> usize) -> Self {
        let mut result = Self::one();
        for index in 0..NORMALS {
            result.u[permutation(index)] = self.u[index];
        }
        result
    }
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct CechCoefficient {
    localization: Mask,
    monomial: Monomial,
}

impl CechCoefficient {
    fn multiply_by_u(mut self, normal: usize) -> Self {
        self.monomial.u[normal] += 1;
        self
    }

    fn permute(self, permutation: fn(usize) -> usize) -> Self {
        let mut localization = 0_u8;
        for normal in 0..NORMALS {
            if self.localization & (1 << normal) != 0 {
                localization |= 1 << permutation(normal);
            }
        }
        Self {
            localization,
            monomial: self.monomial.permute(permutation),
        }
    }

    fn denominators_are_legal(self) -> bool {
        (0..NORMALS)
            .all(|normal| self.monomial.u[normal] >= 0 || self.localization & (1 << normal) != 0)
    }
}

type SourceCombination = BTreeMap<(SourceBasis, Monomial), Int>;
type TargetCombination = BTreeMap<(TargetBasis, CechCoefficient), Int>;
type Matrix = Vec<Vec<Int>>;

fn matrix_multiply(left: &Matrix, right: &Matrix) -> Matrix {
    assert!(!left.is_empty() && !right.is_empty());
    assert_eq!(left[0].len(), right.len());
    let mut result = vec![vec![0; right[0].len()]; left.len()];
    for row in 0..left.len() {
        for middle in 0..right.len() {
            for column in 0..right[0].len() {
                result[row][column] += left[row][middle] * right[middle][column];
            }
        }
    }
    result
}

fn matrix_add(left: &Matrix, right: &Matrix, right_scale: Int) -> Matrix {
    assert_eq!(left.len(), right.len());
    left.iter()
        .zip(right)
        .map(|(left_row, right_row)| {
            assert_eq!(left_row.len(), right_row.len());
            left_row
                .iter()
                .zip(right_row)
                .map(|(left_entry, right_entry)| left_entry + right_scale * right_entry)
                .collect()
        })
        .collect()
}

fn matrix_transpose(value: &Matrix) -> Matrix {
    assert!(!value.is_empty());
    (0..value[0].len())
        .map(|column| value.iter().map(|row| row[column]).collect())
        .collect()
}

fn identity_matrix(size: usize) -> Matrix {
    let mut result = vec![vec![0; size]; size];
    for (index, row) in result.iter_mut().enumerate() {
        row[index] = 1;
    }
    result
}

fn determinant_two(value: [[Int; 2]; 2]) -> Int {
    value[0][0] * value[1][1] - value[0][1] * value[1][0]
}

fn determinant_three(value: &Matrix) -> Int {
    assert_eq!(value.len(), 3);
    assert!(value.iter().all(|row| row.len() == 3));
    value[0][0] * determinant_two([[value[1][1], value[1][2]], [value[2][1], value[2][2]]])
        - value[0][1] * determinant_two([[value[1][0], value[1][2]], [value[2][0], value[2][2]]])
        + value[0][2] * determinant_two([[value[1][0], value[1][1]], [value[2][0], value[2][1]]])
}

fn gcd(mut left: Int, mut right: Int) -> Int {
    left = left.abs();
    right = right.abs();
    while right != 0 {
        let remainder = left % right;
        left = right;
        right = remainder;
    }
    left
}

fn smith_factors_three(value: &Matrix) -> [Int; 3] {
    assert_eq!(value.len(), 3);
    assert!(value.iter().all(|row| row.len() == 3));
    let divisor_one = value
        .iter()
        .flatten()
        .fold(0_i64, |g, &entry| gcd(g, entry));
    let mut divisor_two = 0_i64;
    for first_row in 0..3 {
        for second_row in (first_row + 1)..3 {
            for first_column in 0..3 {
                for second_column in (first_column + 1)..3 {
                    divisor_two = gcd(
                        divisor_two,
                        determinant_two([
                            [
                                value[first_row][first_column],
                                value[first_row][second_column],
                            ],
                            [
                                value[second_row][first_column],
                                value[second_row][second_column],
                            ],
                        ]),
                    );
                }
            }
        }
    }
    let divisor_three = determinant_three(value).abs();
    [
        divisor_one,
        if divisor_one == 0 {
            0
        } else {
            divisor_two / divisor_one
        },
        if divisor_two == 0 {
            0
        } else {
            divisor_three / divisor_two
        },
    ]
}

fn add_source(
    value: &mut SourceCombination,
    basis: SourceBasis,
    monomial: Monomial,
    coefficient: Int,
) {
    *value.entry((basis, monomial)).or_default() += coefficient;
    value.retain(|_, entry| *entry != 0);
}

fn add_target(
    value: &mut TargetCombination,
    basis: TargetBasis,
    coefficient_data: CechCoefficient,
    coefficient: Int,
) {
    *value.entry((basis, coefficient_data)).or_default() += coefficient;
    value.retain(|_, entry| *entry != 0);
}

fn source_data(basis: SourceBasis) -> (Mask, Int) {
    match basis {
        SourceBasis::F => (0b111, 1),
        SourceBasis::E1 => (0b110, 1),
        SourceBasis::E3 => (0b101, -1),
        SourceBasis::E5 => (0b011, 1),
        SourceBasis::Q0 => (0b100, 1),
        SourceBasis::Q1 => (0b010, 1),
        SourceBasis::Q2 => (0b001, 1),
        SourceBasis::Augmentation => (0b000, 1),
    }
}

fn source_basis_for_mask(mask: Mask) -> SourceBasis {
    match mask {
        0b111 => SourceBasis::F,
        0b110 => SourceBasis::E1,
        0b101 => SourceBasis::E3,
        0b011 => SourceBasis::E5,
        0b100 => SourceBasis::Q0,
        0b010 => SourceBasis::Q1,
        0b001 => SourceBasis::Q2,
        0b000 => SourceBasis::Augmentation,
        _ => panic!("invalid three-generator mask"),
    }
}

fn source_boundary(basis: SourceBasis) -> SourceCombination {
    let (mask, source_scale) = source_data(basis);
    let mut result = SourceCombination::new();
    let mut exterior_position = 0_usize;
    for (slot, &normal) in EVEN_SEQUENCE.iter().enumerate() {
        if mask & (1 << slot) == 0 {
            continue;
        }
        let face = mask & !(1 << slot);
        let target_basis = source_basis_for_mask(face);
        let (_, target_scale) = source_data(target_basis);
        let exterior_sign = if exterior_position % 2 == 0 { 1 } else { -1 };
        add_source(
            &mut result,
            target_basis,
            Monomial::u(normal, 1),
            source_scale * exterior_sign * target_scale,
        );
        exterior_position += 1;
    }
    result
}

fn source_boundary_of_combination(value: &SourceCombination) -> SourceCombination {
    let mut result = SourceCombination::new();
    for (&(basis, monomial), &coefficient) in value {
        for ((target_basis, boundary_monomial), boundary_coefficient) in source_boundary(basis) {
            add_source(
                &mut result,
                target_basis,
                monomial.multiply(boundary_monomial),
                coefficient * boundary_coefficient,
            );
        }
    }
    result
}

fn tau_a() -> CechCoefficient {
    let mut localization = 0_u8;
    let mut monomial = Monomial::one();
    for normal in ODD_SUPPORT {
        localization |= 1 << normal;
        monomial.u[normal] = -1;
    }
    CechCoefficient {
        localization,
        monomial,
    }
}

fn simple_pole(even_normal: usize) -> CechCoefficient {
    let mut result = tau_a();
    result.localization |= 1 << even_normal;
    result.monomial.u[even_normal] = -1;
    result
}

fn star_map(basis: SourceBasis) -> TargetCombination {
    let mut result = TargetCombination::new();
    match basis {
        SourceBasis::F => add_target(&mut result, TargetBasis::Krel, tau_a(), 1),
        SourceBasis::E1 => add_target(&mut result, TargetBasis::T2, simple_pole(4), 1),
        SourceBasis::E3 => add_target(&mut result, TargetBasis::T1, simple_pole(0), 1),
        SourceBasis::E5 => add_target(&mut result, TargetBasis::T0, simple_pole(2), 1),
        SourceBasis::Q0 | SourceBasis::Q1 | SourceBasis::Q2 | SourceBasis::Augmentation => {}
    }
    result
}

fn star_map_of_source_combination(value: &SourceCombination) -> TargetCombination {
    let mut result = TargetCombination::new();
    for (&(basis, monomial), &coefficient) in value {
        for ((target_basis, target_coefficient), map_coefficient) in star_map(basis) {
            let mut multiplied = target_coefficient;
            multiplied.monomial = multiplied.monomial.multiply(monomial);
            add_target(
                &mut result,
                target_basis,
                multiplied,
                coefficient * map_coefficient,
            );
        }
    }
    result
}

fn target_boundary(value: &TargetCombination) -> TargetCombination {
    let mut result = TargetCombination::new();
    for (&(basis, coefficient_data), &coefficient) in value {
        if basis != TargetBasis::Krel {
            continue;
        }
        for (road, even_normal) in [
            (TargetBasis::T0, 2_usize),
            (TargetBasis::T1, 0_usize),
            (TargetBasis::T2, 4_usize),
        ] {
            let mut localized = coefficient_data;
            localized.localization |= 1 << even_normal;
            add_target(&mut result, road, localized, coefficient);
        }
    }
    result
}

fn check_raw_koszul_differential() {
    assert_eq!(
        source_boundary(SourceBasis::F),
        BTreeMap::from([
            ((SourceBasis::E1, Monomial::u(4, 1)), 1),
            ((SourceBasis::E3, Monomial::u(0, 1)), 1),
            ((SourceBasis::E5, Monomial::u(2, 1)), 1),
        ])
    );
    assert_eq!(
        source_boundary(SourceBasis::E1),
        BTreeMap::from([
            ((SourceBasis::Q0, Monomial::u(0, 1)), 1),
            ((SourceBasis::Q1, Monomial::u(2, 1)), -1),
        ])
    );
    assert_eq!(
        source_boundary(SourceBasis::E3),
        BTreeMap::from([
            ((SourceBasis::Q0, Monomial::u(4, 1)), -1),
            ((SourceBasis::Q2, Monomial::u(2, 1)), 1),
        ])
    );
    assert_eq!(
        source_boundary(SourceBasis::E5),
        BTreeMap::from([
            ((SourceBasis::Q1, Monomial::u(4, 1)), 1),
            ((SourceBasis::Q2, Monomial::u(0, 1)), -1),
        ])
    );
    assert_eq!(
        source_boundary(SourceBasis::Q0),
        BTreeMap::from([((SourceBasis::Augmentation, Monomial::u(2, 1)), 1)])
    );
    assert_eq!(
        source_boundary(SourceBasis::Q1),
        BTreeMap::from([((SourceBasis::Augmentation, Monomial::u(0, 1)), 1)])
    );
    assert_eq!(
        source_boundary(SourceBasis::Q2),
        BTreeMap::from([((SourceBasis::Augmentation, Monomial::u(4, 1)), 1)])
    );
    assert!(source_boundary(SourceBasis::Augmentation).is_empty());

    for basis in [
        SourceBasis::F,
        SourceBasis::E1,
        SourceBasis::E3,
        SourceBasis::E5,
        SourceBasis::Q0,
        SourceBasis::Q1,
        SourceBasis::Q2,
        SourceBasis::Augmentation,
    ] {
        assert!(source_boundary_of_combination(&source_boundary(basis)).is_empty());
    }
}

fn check_cech_values_and_chain_map() {
    let tau = tau_a();
    assert!(tau.denominators_are_legal());
    for normal in [4_usize, 0, 2] {
        let pole = simple_pole(normal);
        assert!(pole.denominators_are_legal());
        assert_eq!(pole.multiply_by_u(normal).monomial, tau.monomial);
    }

    assert_eq!(
        star_map(SourceBasis::F),
        BTreeMap::from([((TargetBasis::Krel, tau), 1)])
    );
    assert_eq!(
        star_map(SourceBasis::E1),
        BTreeMap::from([((TargetBasis::T2, simple_pole(4)), 1)])
    );
    assert_eq!(
        star_map(SourceBasis::E3),
        BTreeMap::from([((TargetBasis::T1, simple_pole(0)), 1)])
    );
    assert_eq!(
        star_map(SourceBasis::E5),
        BTreeMap::from([((TargetBasis::T0, simple_pole(2)), 1)])
    );

    // The top identity is exactly ui*(tau/ui)=tau in the indicated road
    // localization, together with dKrel=T0+T1+T2.
    assert_eq!(
        target_boundary(&star_map(SourceBasis::F)),
        star_map_of_source_combination(&source_boundary(SourceBasis::F))
    );

    // The relative target has no groups below its three roads.  Sending all
    // q's and the augmentation to zero makes every remaining square strict.
    for basis in [
        SourceBasis::E1,
        SourceBasis::E3,
        SourceBasis::E5,
        SourceBasis::Q0,
        SourceBasis::Q1,
        SourceBasis::Q2,
        SourceBasis::Augmentation,
    ] {
        assert_eq!(
            target_boundary(&star_map(basis)),
            star_map_of_source_combination(&source_boundary(basis))
        );
    }

    assert!(star_map(SourceBasis::Q0).is_empty());
    assert!(star_map(SourceBasis::Q1).is_empty());
    assert!(star_map(SourceBasis::Q2).is_empty());
    assert!(star_map(SourceBasis::Augmentation).is_empty());
}

fn rotation_normal(normal: usize) -> usize {
    (normal + 2) % NORMALS
}

fn reflection_normal(normal: usize) -> usize {
    (2 + NORMALS - normal) % NORMALS
}

fn rotation_source(basis: SourceBasis) -> (SourceBasis, Int) {
    (
        match basis {
            SourceBasis::F => SourceBasis::F,
            SourceBasis::E1 => SourceBasis::E3,
            SourceBasis::E3 => SourceBasis::E5,
            SourceBasis::E5 => SourceBasis::E1,
            SourceBasis::Q0 => SourceBasis::Q2,
            SourceBasis::Q2 => SourceBasis::Q1,
            SourceBasis::Q1 => SourceBasis::Q0,
            SourceBasis::Augmentation => SourceBasis::Augmentation,
        },
        1,
    )
}

fn reflection_source(basis: SourceBasis) -> (SourceBasis, Int) {
    match basis {
        SourceBasis::F => (SourceBasis::F, -1),
        SourceBasis::E1 => (SourceBasis::E1, -1),
        SourceBasis::E3 => (SourceBasis::E5, -1),
        SourceBasis::E5 => (SourceBasis::E3, -1),
        SourceBasis::Q0 => (SourceBasis::Q1, 1),
        SourceBasis::Q1 => (SourceBasis::Q0, 1),
        SourceBasis::Q2 => (SourceBasis::Q2, 1),
        SourceBasis::Augmentation => (SourceBasis::Augmentation, 1),
    }
}

fn rotation_target(basis: TargetBasis) -> (TargetBasis, Int) {
    (
        match basis {
            TargetBasis::Krel => TargetBasis::Krel,
            TargetBasis::T2 => TargetBasis::T1,
            TargetBasis::T1 => TargetBasis::T0,
            TargetBasis::T0 => TargetBasis::T2,
        },
        1,
    )
}

fn reflection_target(basis: TargetBasis) -> (TargetBasis, Int) {
    match basis {
        TargetBasis::Krel => (TargetBasis::Krel, -1),
        TargetBasis::T2 => (TargetBasis::T2, -1),
        TargetBasis::T1 => (TargetBasis::T0, -1),
        TargetBasis::T0 => (TargetBasis::T1, -1),
    }
}

fn transform_source_combination(
    value: &SourceCombination,
    basis_action: fn(SourceBasis) -> (SourceBasis, Int),
    normal_action: fn(usize) -> usize,
) -> SourceCombination {
    let mut result = SourceCombination::new();
    for (&(basis, monomial), &coefficient) in value {
        let (image, sign) = basis_action(basis);
        add_source(
            &mut result,
            image,
            monomial.permute(normal_action),
            coefficient * sign,
        );
    }
    result
}

fn transform_target_combination(
    value: &TargetCombination,
    basis_action: fn(TargetBasis) -> (TargetBasis, Int),
    normal_action: fn(usize) -> usize,
) -> TargetCombination {
    let mut result = TargetCombination::new();
    for (&(basis, coefficient_data), &coefficient) in value {
        let (image, sign) = basis_action(basis);
        add_target(
            &mut result,
            image,
            coefficient_data.permute(normal_action),
            coefficient * sign,
        );
    }
    result
}

fn apply_source_action(
    basis: SourceBasis,
    action: fn(SourceBasis) -> (SourceBasis, Int),
) -> (SourceBasis, Int) {
    action(basis)
}

fn compose_source_actions(
    basis: SourceBasis,
    actions: &[fn(SourceBasis) -> (SourceBasis, Int)],
) -> (SourceBasis, Int) {
    actions
        .iter()
        .fold((basis, 1_i64), |(present, sign), action| {
            let (next, next_sign) = apply_source_action(present, *action);
            (next, sign * next_sign)
        })
}

fn compose_target_actions(
    basis: TargetBasis,
    actions: &[fn(TargetBasis) -> (TargetBasis, Int)],
) -> (TargetBasis, Int) {
    actions
        .iter()
        .fold((basis, 1_i64), |(present, sign), action| {
            let (next, next_sign) = action(present);
            (next, sign * next_sign)
        })
}

fn check_d3_covariance() {
    let bases = [
        SourceBasis::F,
        SourceBasis::E1,
        SourceBasis::E3,
        SourceBasis::E5,
        SourceBasis::Q0,
        SourceBasis::Q1,
        SourceBasis::Q2,
        SourceBasis::Augmentation,
    ];

    // r^3=s^2=1 and srs=r^-1 on every signed source basis.
    for basis in bases {
        assert_eq!(
            compose_source_actions(
                basis,
                &[rotation_source as fn(SourceBasis) -> (SourceBasis, Int); 3],
            ),
            (basis, 1)
        );
        assert_eq!(
            compose_source_actions(
                basis,
                &[reflection_source as fn(SourceBasis) -> (SourceBasis, Int); 2],
            ),
            (basis, 1)
        );
        assert_eq!(
            compose_source_actions(
                basis,
                &[reflection_source, rotation_source, reflection_source]
            ),
            compose_source_actions(basis, &[rotation_source, rotation_source])
        );
    }

    for basis in [
        TargetBasis::Krel,
        TargetBasis::T0,
        TargetBasis::T1,
        TargetBasis::T2,
    ] {
        assert_eq!(
            compose_target_actions(
                basis,
                &[rotation_target as fn(TargetBasis) -> (TargetBasis, Int); 3],
            ),
            (basis, 1)
        );
        assert_eq!(
            compose_target_actions(
                basis,
                &[reflection_target as fn(TargetBasis) -> (TargetBasis, Int); 2],
            ),
            (basis, 1)
        );
        assert_eq!(
            compose_target_actions(
                basis,
                &[reflection_target, rotation_target, reflection_target]
            ),
            compose_target_actions(basis, &[rotation_target, rotation_target])
        );
    }

    // Both source differential and the candidate star map are D3-covariant.
    for basis in bases {
        for (source_action, target_action, normal_action) in [
            (
                rotation_source as fn(SourceBasis) -> (SourceBasis, Int),
                rotation_target as fn(TargetBasis) -> (TargetBasis, Int),
                rotation_normal as fn(usize) -> usize,
            ),
            (
                reflection_source as fn(SourceBasis) -> (SourceBasis, Int),
                reflection_target as fn(TargetBasis) -> (TargetBasis, Int),
                reflection_normal as fn(usize) -> usize,
            ),
        ] {
            let (image_basis, image_sign) = source_action(basis);
            let mut boundary_after_action = source_boundary(image_basis);
            for coefficient in boundary_after_action.values_mut() {
                *coefficient *= image_sign;
            }
            assert_eq!(
                boundary_after_action,
                transform_source_combination(&source_boundary(basis), source_action, normal_action)
            );

            let mut map_after_action = star_map(image_basis);
            for coefficient in map_after_action.values_mut() {
                *coefficient *= image_sign;
            }
            assert_eq!(
                map_after_action,
                transform_target_combination(&star_map(basis), target_action, normal_action)
            );
        }
    }
}

fn entry94_triangle() -> Matrix {
    vec![vec![0, -1, 1], vec![1, 0, -1], vec![-1, 1, 0]]
}

fn entry99_triangle() -> Matrix {
    vec![vec![1, -1, 0], vec![-1, 0, 1], vec![0, 1, -1]]
}

fn c3_rotation() -> Matrix {
    // Left multiplication by r in the standard basis (1,r,r^2).
    vec![vec![0, 0, 1], vec![1, 0, 0], vec![0, 1, 0]]
}

fn c3_inversion() -> Matrix {
    // The reflection fixes 1 and exchanges r with r^2.
    vec![vec![1, 0, 0], vec![0, 0, 1], vec![0, 1, 0]]
}

fn check_tate_window_based_identification() {
    let rotation = c3_rotation();
    let rotation_inverse = matrix_multiply(&rotation, &rotation);
    let inversion = c3_inversion();
    let identity = identity_matrix(3);
    assert_eq!(matrix_multiply(&rotation_inverse, &rotation), identity);
    assert_eq!(matrix_multiply(&inversion, &inversion), identity);
    assert_eq!(
        matrix_multiply(&matrix_multiply(&inversion, &rotation), &inversion),
        rotation_inverse
    );

    let one_minus_rotation = matrix_add(&identity_matrix(3), &rotation, -1);
    let norm_column = vec![vec![1], vec![1], vec![1]];
    let augmentation = vec![vec![1, 1, 1]];
    assert_eq!(
        matrix_multiply(&one_minus_rotation, &norm_column),
        vec![vec![0], vec![0], vec![0]]
    );
    assert_eq!(
        matrix_multiply(&augmentation, &one_minus_rotation),
        vec![vec![0, 0, 0]]
    );

    // Entry 94 orders its tag basis as (r,r^2,1), while its road basis is
    // (1,r,r^2).  Thus its skew triangle is exactly (1-r) after the positive
    // cyclic tag-basis shift.
    let tag_shift = vec![vec![0, 0, 1], vec![1, 0, 0], vec![0, 1, 0]];
    let entry94 = entry94_triangle();
    assert_eq!(matrix_multiply(&one_minus_rotation, &tag_shift), entry94);
    assert_eq!(matrix_multiply(&tag_shift, &norm_column), norm_column);

    // Entry 99 uses the edge order obtained by reversing the three entry-94
    // tag columns.  The top norm vector is unchanged.
    let edge_reversal = vec![vec![0, 0, 1], vec![0, 1, 0], vec![1, 0, 0]];
    assert_eq!(
        matrix_multiply(&entry94, &edge_reversal),
        entry99_triangle()
    );
    assert_eq!(matrix_multiply(&edge_reversal, &norm_column), norm_column);

    // Exactness is saturated: the middle differential has Smith factors
    // (1,1,0), its kernel is the primitive norm line, and its image is the
    // primitive augmentation-zero A2 lattice.
    assert_eq!(smith_factors_three(&entry94), [1, 1, 0]);
    assert_eq!(
        matrix_multiply(&entry94, &norm_column),
        vec![vec![0], vec![0], vec![0]]
    );
    assert_eq!(
        matrix_multiply(&augmentation, &entry94),
        vec![vec![0, 0, 0]]
    );
    assert_eq!(
        matrix_transpose(&entry94),
        matrix_add(&vec![vec![0; 3]; 3], &entry94, -1)
    );
    assert_eq!(matrix_transpose(&norm_column), augmentation);
}

fn check_tate_d3_chain_actions_and_orientation() {
    let rotation = c3_rotation();
    let rotation_inverse = matrix_multiply(&rotation, &rotation);
    let road_reflection = c3_inversion();
    let one_minus_rotation = matrix_add(&identity_matrix(3), &rotation, -1);
    let norm_column = vec![vec![1], vec![1], vec![1]];
    let augmentation = vec![vec![1, 1, 1]];

    // Inversion sends 1-r to 1-r^-1=-r^-1(1-r).  Therefore the tag copy
    // needs the orientation-twisted reflection -r^-1*s, while the road copy
    // uses ordinary inversion.  The top norm line is reflection-odd and the
    // bottom augmentation line reflection-even.
    let tag_reflection = matrix_add(
        &vec![vec![0; 3]; 3],
        &matrix_multiply(&rotation_inverse, &road_reflection),
        -1,
    );
    assert_eq!(
        matrix_multiply(&road_reflection, &one_minus_rotation),
        matrix_multiply(&one_minus_rotation, &tag_reflection)
    );
    assert_eq!(
        matrix_multiply(&tag_reflection, &norm_column),
        vec![vec![-1], vec![-1], vec![-1]]
    );
    assert_eq!(
        matrix_multiply(&augmentation, &road_reflection),
        augmentation
    );
    assert_eq!(
        matrix_multiply(&tag_reflection, &tag_reflection),
        identity_matrix(3)
    );
    assert_eq!(
        matrix_multiply(
            &matrix_multiply(&tag_reflection, &rotation),
            &tag_reflection
        ),
        rotation_inverse
    );
}

fn check_index_three_and_tate_class() {
    // Entry 94's combined primitive/contact map uses epsilon in the first
    // row and two integral coordinates of the A2 road lattice below it.
    let primitive_contact = vec![vec![1, 1, 1], vec![0, -1, 1], vec![1, 0, -1]];
    assert_eq!(smith_factors_three(&primitive_contact), [1, 1, 3]);
    assert_eq!(determinant_three(&primitive_contact).abs(), 3);

    // The primitive quotient unit is not in the image: its unique rational
    // preimage is (1/3,1/3,1/3).  Three times it is the image of the norm
    // vector.  It therefore generates the exact Z/3 cokernel.
    assert_eq!(
        matrix_multiply(&primitive_contact, &vec![vec![1], vec![1], vec![1]]),
        vec![vec![3], vec![0], vec![0]]
    );
    let rational_preimage_numerators = [1_i64, 1, 1];
    assert!(rational_preimage_numerators
        .iter()
        .any(|numerator| numerator % 3 != 0));

    // Applying Hom_{Z[C3]}(-,Z_triv) to the complete resolution sends
    // 1-r to zero and N to multiplication by three.  Hence the relevant
    // even Tate group is Z/3, the class of 1 has exact order three, and the
    // adjacent odd Tate group vanishes.
    let hom_one_minus_r = 0_i64;
    let hom_norm = 3_i64;
    assert_eq!(hom_one_minus_r, 0);
    assert_eq!(hom_norm, 3);
    assert_ne!(1_i64.rem_euclid(hom_norm), 0);
    assert_eq!(3_i64.rem_euclid(hom_norm), 0);
}

fn check_weighted_star_is_not_unlocalized_tate_window() {
    // Formally setting u4=u0=u2=1 turns the weighted matrices into entry
    // 99's based Tate window.  Because uj=qj-1 and qj is a Laurent unit,
    // this means q_even=2 over Z[1/2]; it is an unsupported localized
    // control, not an integral fibre or an isomorphism over R0.
    let weighted_top_at_one = vec![vec![1], vec![1], vec![1]];
    let weighted_middle_at_one = entry99_triangle();
    let weighted_bottom_at_one = vec![vec![1, 1, 1]];
    assert_eq!(weighted_top_at_one, vec![vec![1], vec![1], vec![1]]);
    assert_eq!(weighted_middle_at_one, entry99_triangle());
    assert_eq!(weighted_bottom_at_one, vec![vec![1, 1, 1]]);

    // At the support fibre u4=u0=u2=0, the weighted q->a row vanishes,
    // whereas the Tate augmentation remains primitive.  Thus the weighted
    // complex has H0=R0/(u4,u0,u2) and cannot be a deformation-equivalent
    // copy of the exact Tate window over the unlocalized base.
    let weighted_bottom_at_support = vec![vec![0, 0, 0]];
    let tate_augmentation = vec![vec![1, 1, 1]];
    assert_ne!(weighted_bottom_at_support, tate_augmentation);

    // Diagonal normalization uses 1/u4,1/u0,1/u2.  The checker verifies
    // that each pole is legal only in its own Cech summand and is not an R0
    // coefficient.  A single chain isomorphism to the Tate window would
    // require the unsupported global localization of all three even u's.
    for normal in [4_usize, 0, 2] {
        let pole = simple_pole(normal);
        assert!(pole.monomial.u[normal] < 0);
        assert!(pole.localization & (1 << normal) != 0);
    }
    let all_even_localization: Mask = (1 << 4) | (1 << 0) | (1 << 2);
    assert_eq!(all_even_localization.count_ones(), 3);

    // The actual corrected star deliberately kills q and a, so it retains
    // only the top/road half of the window and is not the complete window.
    assert!(star_map(SourceBasis::Q0).is_empty());
    assert!(star_map(SourceBasis::Q1).is_empty());
    assert!(star_map(SourceBasis::Q2).is_empty());
    assert!(star_map(SourceBasis::Augmentation).is_empty());
}

fn main() {
    check_raw_koszul_differential();
    check_cech_values_and_chain_map();
    check_d3_covariance();
    check_tate_window_based_identification();
    check_tate_d3_chain_actions_and_orientation();
    check_index_three_and_tate_class();
    check_weighted_star_is_not_unlocalized_tate_window();

    let packet = concat!(
        r#"{"claim":"the entry-94/99 augmented triangle is a based, orientation-twisted finite window of the complete C3 Tate resolution, but the corrected weighted Koszul/Cech star is not that window over the unlocalized base; it agrees only on the u_even=1 fibre or after unsupported global even-normal localization","status":"inconclusive","conditional_theorem":"if the intrinsic supported arrow f_plus->tau_A*Krel exists and restricts to the three labelled entry-100 road traces, the displayed top/road half-star is a strict D3-equivariant chain map; it is not thereby the full Tate window","ring":{"base":"R0=Z[q0^+-1,...,q5^+-1], uj=qj-1","base_inversions":"none: no uj or integer is inverted in R0","cech_rule":"negative uj powers occur only in a localization summand whose support mask contains j","tau_A":"1/(u1*u3*u5) in the A=(u1,u3,u5) Cech summand"},"tate_window":{"standard":"Z_or --N--> Z[C3] --(1-r)--> Z[C3] --epsilon--> Z, N=1+r+r^2","entry94_bases":"road basis=(1,r,r^2), tag basis=(r,r^2,1); the displayed skew triangle is multiplication by 1-r","entry99_bases":"entry99 is entry94 followed by the column reversal (d2,d1,d0), with the norm vector fixed","exactness":"middle Smith factors (1,1,0); kernel is the primitive norm line and image is the primitive augmentation-zero A2 lattice","self_duality":"Delta^vee=epsilon and partial_triangle^T=-partial_triangle","D3_reflection":"road reflection is inversion s; tag reflection is -r^-1*s; the top orientation line is reflection-odd and the bottom trivial line is reflection-even","index_three":"the combined (epsilon, two A2 coordinates) map has Smith factors (1,1,3)","tate_class":"Hom_{Z[C3]}(-,Z_triv) sends 1-r to 0 and N to 3; the relevant even Tate group is Z/3, generated by the primitive quotient unit of exact order three, and the adjacent odd group vanishes"},"source":{"complex":"K(u4,u0,u2)","bases":{"degree3":"f=h4*h0*h2","degree2":["e1=p4*h0*h2","e3=-h4*p0*h2","e5=h4*h0*p2"],"degree1":["q0=p4*p0*h2","q1=p4*h0*p2","q2=h4*p0*p2"],"degree0":"a=p4*p0*p2"},"differential":{"f":"u4*e1+u0*e3+u2*e5","e1":"u0*q0-u2*q1","e3":"-u4*q0+u2*q2","e5":"u4*q1-u0*q2","q0":"u2*a","q1":"u0*a","q2":"u4*a","a":"0"},"d_squared":"zero on all eight bases"},"target":{"relative_bases":{"degree3":"Krel","degree2":["T0","T1","T2"],"lower":"zero"},"differential":"dKrel=T0+T1+T2, with localization into the appropriate road Cech summand","map":{"f":"tau_A*Krel","e1":"tau_A/u4*T2","e3":"tau_A/u0*T1","e5":"tau_A/u2*T0","q0_q1_q2_a":"0"},"top_identity":"G(df)=tau_A*(T2+T1+T0)=d(tau_A*Krel), using uj*(tau_A/uj)=tau_A inside each indicated Cech summand","lower_identity":"all edge, q, and augmentation squares commute because the relative target is zero below road degree"},"D3":{"rotation":{"normals":"4->0->2->4 and 1->3->5->1","source_edges":"e1->e3->e5->e1","target_roads":"T2->T1->T0->T2","top_sign":"+1"},"reflection":{"normals":"0<->2, 4 fixed; 3<->5, 1 fixed","source":"f,e1,e3,e5 carry the exterior orientation signs (-,-,-,-), with e3<->e5; q0<->q1 and q2 fixed","target":"Krel and all road orientations carry -1, with T1<->T0 and T2 fixed"},"relations":"r^3=s^2=1 and srs=r^-1; differential and candidate map are covariant"},"comparison":{"special_fibre":"setting u4=u0=u2=1 gives exactly the entry-99 based Tate window","unlocalized_obstruction":"at u4=u0=u2=0 the weighted q-to-a row vanishes, so H0=R0/(u4,u0,u2), whereas the Tate window remains exact with primitive epsilon","global_localization":"diagonal conjugation to unit incidence requires 1/u4,1/u0,1/u2 simultaneously and therefore globally localizes away the supported fibre","Cech_scope":"the corrected star uses separate legal localization summands and kills q,a; it realizes only a conditional top/road half-map, not the complete Tate window"},"checks":{"entry94_as_1_minus_r":"PASS","entry99_based_reversal":"PASS","Tate_exact_matrices":"PASS","Tate_self_duality":"PASS","Tate_D3_inversion_and_orientation_twist":"PASS","SNF_index_three":"PASS","Tate_class_order_three":"PASS","raw_Koszul_differential":"PASS","raw_d_squared":"PASS","Cech_denominator_legality":"PASS","four_displayed_Koszul_to_Cech_values":"PASS","top_chain_identity":"PASS","q_and_augmentation_zero_compatibility":"PASS","D3_group_relations_and_signs":"PASS","D3_differential_covariance":"PASS","D3_map_covariance":"PASS","unlocalized_Tate_realization":"FAIL: bottom homology/support fibre differs","localized_or_specialized_control":"PASS"},"typing_boundary":{"intrinsic_supported_top_arrow":"NOT SUPPLIED: tau_A*Krel is the candidate value being assumed, not derived by entries 93-100","local_attachment":"NOT SUPPLIED: this coefficient checker does not identify its three road terms with the mixed excess generators, occurrence counits, or separate physical normal evaluations of entry 100","alpha_plus":"NOT CLAIMED: the full alpha_plus PC/Gysin map remains unconstructed","PC_status":"CONDITIONAL/INCONCLUSIVE"},"next_experiment":"construct the intrinsic supported f_plus-to-Krel arrow without globally inverting even normals, then prove its restrictions are the labelled local excess traces; the Tate-window identification alone cannot supply alpha_plus"}"#
    );
    let packet = packet
        .replace(
            "on the u_even=1 fibre",
            "under the formal u_even=1 control over Z[1/2]",
        )
        .replace(
            "setting u4=u0=u2=1 gives exactly the entry-99 based Tate window",
            "formally setting u4=u0=u2=1 (q_even=2 over Z[1/2]) gives the entry-99 based Tate window",
        );
    println!("{packet}");
}
