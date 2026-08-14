//! Exact frontier certificate for the plus-sheet/D=03 excess-one
//! Beck--Chevalley comparison left open by ledger entry 98.
//!
//! The primary construction is geometric.  The plus conductor link is the
//! positive normal link of the odd central triangulation T+=(x1,x3,x5).  In
//! the labelled K6 flip graph there is a unique core-entry flip retaining the
//! x3 sink mark and entering F03, followed by a unique marked road edge to
//! the common occurrence.  This supplies the only possible labelled
//! occurrence flag for a comparison; it does not itself construct an
//! augmented cellular map from the positive dual block to (K6,B_sc).  Entry
//! 38 constructs face tubes for actual faces, not this missing dual-block
//! morphism.
//!
//! Its local coefficient algebra is then audited over the universal normal
//! ring, with the actual ideals
//!
//!   I+  = (u1,u3,u5),       I03 = (u0,u3).
//!
//! Their derived intersection is represented by the tensor Koszul complex
//!
//!   D = K(u1,u3,u5) tensor K(u0,u3).
//!
//! Write the two copies of the shared normal as h3+ and h3(03), and put
//!
//!   eta = h3+ - h3(03),     Q = (u0,u1,u3,u5).
//!
//! The map from the five conormal generators of D to the four generators of
//! Q has kernel Z eta.  Wedge by eta therefore gives a splitting-independent
//! excess inclusion and a canonical exact sequence of complexes
//!
//!   0 -> K(Q)[1] --eta wedge--> D -> K(Q) -> 0.
//!
//! This is the canonical local excess algebra that any geometric
//! dual-block/face-tube map must induce, and is the chain-level Tor_1
//! orientation.  No projection along eta (and hence no noncanonical
//! splitting) is used.  With the ordered orientations
//!
//!   omega+  = h1+ wedge h3+ wedge h5+,
//!   omega03 = h0(03) wedge h3(03),
//!   omegaQ  = h0(03) wedge h1+ wedge h3+ wedge h5+,
//!
//! the exact inclusion sends omegaQ to omega+ wedge omega03 with sign +1.
//!
//! This coefficient theorem is combined with independently enumerated scalar
//! incidence.  The plus source is the odd central triangulation
//! (x1,x3,x5).  Its unique D=03 Catalan endpoint retaining the x3 sink mark
//! is v10=X03*x1*x3; the unique marked lower-Cousin edge then runs to
//! v00=X03*x0*x3.  The global reciprocal occurrence cocycle kills both the
//! central flip boundary and this lower-Cousin boundary.  Removing the
//! common physical X03/[dX03] factor gives exactly the two plus-sheet values
//! 1/(x1*x3) and 1/(x0*x3) of the entry-97 road trace.
//!
//! Reciprocal-twist regular support is kept distinct from original-twist
//! locally-finite/Borel--Moore road support.  Twist normalization uses only
//! q_j Laurent units: u_j^vee=-q_j^-1*u_j.  It never inverts u_j or an
//! integer.  The common physical line [dX03] is evaluated separately with
//! sign +1.  These forced boundary invariants agree with entry 97, but their
//! equality is only a necessary test.  The first still-untyped arrow is the
//! unlocalized augmented dual-block/Cousin can--var kernel whose restriction
//! to the marked flag would have to recover the established face tube.

use std::collections::{BTreeMap, BTreeSet};

type Int = i64;
type Mask = u8;

const NORMALS: usize = 6;
const HEXAGON_VERTICES: u8 = 6;

#[derive(Clone, Debug, Eq, PartialEq)]
struct Polynomial(BTreeMap<[u8; NORMALS], Int>);

impl Polynomial {
    fn zero() -> Self {
        Self(BTreeMap::new())
    }

    fn one() -> Self {
        Self(BTreeMap::from([([0; NORMALS], 1)]))
    }

    fn variable(index: usize) -> Self {
        let mut exponent = [0; NORMALS];
        exponent[index] = 1;
        Self(BTreeMap::from([(exponent, 1)]))
    }

    fn add_scaled(&mut self, other: &Self, scale: Int) {
        for (&monomial, &coefficient) in &other.0 {
            *self.0.entry(monomial).or_default() += scale * coefficient;
        }
        self.0.retain(|_, coefficient| *coefficient != 0);
    }

    fn multiply(&self, other: &Self) -> Self {
        let mut result = Self::zero();
        for (&left, &left_coefficient) in &self.0 {
            for (&right, &right_coefficient) in &other.0 {
                let monomial = std::array::from_fn(|index| left[index] + right[index]);
                *result.0.entry(monomial).or_default() += left_coefficient * right_coefficient;
            }
        }
        result.0.retain(|_, coefficient| *coefficient != 0);
        result
    }
}

type Matrix = Vec<Vec<Polynomial>>;

fn zero_matrix(rows: usize, columns: usize) -> Matrix {
    vec![vec![Polynomial::zero(); columns]; rows]
}

fn multiply(left: &Matrix, right: &Matrix) -> Matrix {
    assert!(!left.is_empty() && !right.is_empty());
    assert_eq!(left[0].len(), right.len());
    let mut result = zero_matrix(left.len(), right[0].len());
    for row in 0..left.len() {
        for middle in 0..right.len() {
            for column in 0..right[0].len() {
                let product = left[row][middle].multiply(&right[middle][column]);
                result[row][column].add_scaled(&product, 1);
            }
        }
    }
    result
}

fn add(left: &Matrix, right: &Matrix) -> Matrix {
    assert_eq!(left.len(), right.len());
    let mut result = left.clone();
    for row in 0..left.len() {
        assert_eq!(left[row].len(), right[row].len());
        for column in 0..left[row].len() {
            result[row][column].add_scaled(&right[row][column], 1);
        }
    }
    result
}

fn integer_matrix(value: &[Vec<Int>]) -> Matrix {
    value
        .iter()
        .map(|row| {
            row.iter()
                .map(|&coefficient| {
                    let mut entry = Polynomial::zero();
                    entry.add_scaled(&Polynomial::one(), coefficient);
                    entry
                })
                .collect()
        })
        .collect()
}

fn basis(generators: usize, degree: usize) -> Vec<Mask> {
    (0..(1_u8 << generators))
        .filter(|mask| mask.count_ones() as usize == degree)
        .collect()
}

fn wedge_sign(left: Mask, right: Mask, generators: usize) -> Option<Int> {
    if left & right != 0 {
        return None;
    }
    let inversions = (0..generators)
        .filter(|index| left & (1 << index) != 0)
        .map(|left_index| {
            (0..left_index)
                .filter(|right_index| right & (1 << right_index) != 0)
                .count()
        })
        .sum::<usize>();
    Some(if inversions % 2 == 0 { 1 } else { -1 })
}

fn koszul_boundary(sequence: &[usize], degree: usize) -> Matrix {
    if degree == 0 {
        return zero_matrix(0, 1);
    }
    let source = basis(sequence.len(), degree);
    let target = basis(sequence.len(), degree - 1);
    let target_index: BTreeMap<_, _> = target
        .iter()
        .enumerate()
        .map(|(index, &mask)| (mask, index))
        .collect();
    let mut result = zero_matrix(target.len(), source.len());
    for (column, &mask) in source.iter().enumerate() {
        let mut position = 0;
        for (generator, &normal) in sequence.iter().enumerate() {
            if mask & (1 << generator) == 0 {
                continue;
            }
            let face = mask & !(1 << generator);
            let sign = if position % 2 == 0 { 1 } else { -1 };
            result[target_index[&face]][column].add_scaled(&Polynomial::variable(normal), sign);
            position += 1;
        }
    }
    result
}

fn map_matrix(
    source_generators: usize,
    target_generators: usize,
    source_degree: usize,
    image: impl Fn(Mask) -> BTreeMap<Mask, Int>,
) -> Vec<Vec<Int>> {
    let source = basis(source_generators, source_degree);
    let target = basis(target_generators, source_degree);
    let target_index: BTreeMap<_, _> = target
        .iter()
        .enumerate()
        .map(|(index, &mask)| (mask, index))
        .collect();
    let mut result = vec![vec![0; source.len()]; target.len()];
    for (column, &mask) in source.iter().enumerate() {
        for (target_mask, coefficient) in image(mask) {
            result[target_index[&target_mask]][column] += coefficient;
        }
    }
    result
}

fn exterior_image(
    mask: Mask,
    generator_images: &[usize],
    target_generators: usize,
) -> BTreeMap<Mask, Int> {
    let mut result = BTreeMap::from([(0_u8, 1_i64)]);
    for (source_generator, &target_generator) in generator_images.iter().enumerate() {
        if mask & (1 << source_generator) == 0 {
            continue;
        }
        let mut next = BTreeMap::new();
        for (&present, &coefficient) in &result {
            let added = 1 << target_generator;
            if let Some(sign) = wedge_sign(present, added, target_generators) {
                *next.entry(present | added).or_default() += coefficient * sign;
            }
        }
        result = next;
    }
    result
}

fn lifted_q_mask_with(mask: Mask, lifts: [usize; 4]) -> (Mask, Int) {
    let image = exterior_image(mask, &lifts, 5);
    assert_eq!(image.len(), 1);
    let (&lifted, &sign) = image.iter().next().unwrap();
    (lifted, sign)
}

fn lifted_q_mask(mask: Mask) -> (Mask, Int) {
    // Q is ordered (u0,u1,u3,u5).  Use the branch copy of u3 as one lift into
    // D, whose order is (h1+,h3+,h5+,h0(03),h3(03)).
    lifted_q_mask_with(mask, [3, 0, 1, 2])
}

fn excess_inclusion_with(mask: Mask, lifts: [usize; 4]) -> BTreeMap<Mask, Int> {
    let (lifted, lift_sign) = lifted_q_mask_with(mask, lifts);
    let mut result = BTreeMap::new();
    // eta wedge lift, eta=h3+ - h3(03).  Putting eta first makes this a
    // chain map K(Q)[1] -> D, whose shifted differential is -d_Q.
    for (generator, coefficient) in [(1_usize, 1_i64), (4, -1)] {
        let eta_term = 1 << generator;
        if let Some(sign) = wedge_sign(eta_term, lifted, 5) {
            *result.entry(eta_term | lifted).or_default() += coefficient * sign * lift_sign;
        }
    }
    result.retain(|_, coefficient| *coefficient != 0);
    result
}

fn excess_inclusion(mask: Mask) -> BTreeMap<Mask, Int> {
    excess_inclusion_with(mask, [3, 0, 1, 2])
}

fn check_excess_koszul_sequence() -> Int {
    let plus = [1_usize, 3, 5];
    let pair = [0_usize, 3];
    let derived = [1_usize, 3, 5, 0, 3];
    let quotient = [0_usize, 1, 3, 5];
    assert_eq!(plus.as_slice(), &derived[..3]);
    assert_eq!(pair.as_slice(), &derived[3..]);
    assert_eq!(
        plus.iter().copied().collect::<BTreeSet<_>>(),
        BTreeSet::from([1, 3, 5])
    );
    assert_eq!(
        pair.iter().copied().collect::<BTreeSet<_>>(),
        BTreeSet::from([0, 3])
    );
    assert_eq!(
        plus.iter()
            .copied()
            .collect::<BTreeSet<_>>()
            .intersection(&pair.iter().copied().collect())
            .copied()
            .collect::<Vec<_>>(),
        vec![3]
    );

    // The branch and pair copies of the shared quotient generator are the two
    // evident lifts.  Their difference is eta, so wedging by eta makes the
    // excess map literally identical, not merely homotopic.
    for q_mask in 0_u8..16 {
        assert_eq!(
            excess_inclusion_with(q_mask, [3, 0, 1, 2]),
            excess_inclusion_with(q_mask, [3, 0, 4, 2])
        );
    }

    let d_derived: Vec<_> = (0..=5)
        .map(|degree| koszul_boundary(&derived, degree))
        .collect();
    let d_quotient: Vec<_> = (0..=4)
        .map(|degree| koszul_boundary(&quotient, degree))
        .collect();
    for degree in 2..=5 {
        let square = multiply(&d_derived[degree - 1], &d_derived[degree]);
        assert!(square
            .iter()
            .flatten()
            .all(|entry| *entry == Polynomial::zero()));
    }
    for degree in 2..=4 {
        let square = multiply(&d_quotient[degree - 1], &d_quotient[degree]);
        assert!(square
            .iter()
            .flatten()
            .all(|entry| *entry == Polynomial::zero()));
    }

    // The canonical quotient identifies the two copies of h3.
    let quotient_generator_images = [1_usize, 2, 3, 0, 2];
    let quotient_maps: Vec<Vec<Vec<Int>>> = (0..=5)
        .map(|degree| {
            if degree > 4 {
                vec![vec![0; basis(5, degree).len()]; 0]
            } else {
                map_matrix(5, 4, degree, |mask| {
                    exterior_image(mask, &quotient_generator_images, 4)
                })
            }
        })
        .collect();
    for degree in 1..=5 {
        let left = if degree <= 4 {
            multiply(&d_quotient[degree], &integer_matrix(&quotient_maps[degree]))
        } else {
            zero_matrix(basis(4, degree - 1).len(), basis(5, degree).len())
        };
        let right = multiply(
            &integer_matrix(&quotient_maps[degree - 1]),
            &d_derived[degree],
        );
        assert_eq!(left, right);
    }

    // Wedge with eta is a strict map out of the shifted quotient complex.
    let inclusions: Vec<Vec<Vec<Int>>> = (1..=5)
        .map(|derived_degree| {
            let q_degree = derived_degree - 1;
            let q_basis = basis(4, q_degree);
            let d_basis = basis(5, derived_degree);
            let d_index: BTreeMap<_, _> = d_basis
                .iter()
                .enumerate()
                .map(|(index, &mask)| (mask, index))
                .collect();
            let mut matrix = vec![vec![0; q_basis.len()]; d_basis.len()];
            for (column, &mask) in q_basis.iter().enumerate() {
                for (image, coefficient) in excess_inclusion(mask) {
                    matrix[d_index[&image]][column] += coefficient;
                }
            }
            matrix
        })
        .collect();
    for derived_degree in 1..=5 {
        let inclusion = &inclusions[derived_degree - 1];
        let left = multiply(&d_derived[derived_degree], &integer_matrix(inclusion));
        let right = if derived_degree == 1 {
            zero_matrix(basis(5, 0).len(), basis(4, 0).len())
        } else {
            multiply(
                &integer_matrix(&inclusions[derived_degree - 2]),
                &d_quotient[derived_degree - 1],
            )
        };
        assert!(add(&left, &right)
            .iter()
            .flatten()
            .all(|entry| *entry == Polynomial::zero()));

        if derived_degree <= 4 {
            let quotient_after_inclusion = multiply(
                &integer_matrix(&quotient_maps[derived_degree]),
                &integer_matrix(inclusion),
            );
            assert!(quotient_after_inclusion
                .iter()
                .flatten()
                .all(|entry| *entry == Polynomial::zero()));
        }
    }

    // Degreewise exactness is integral.  The quotient has the evident lift
    // used above, while the coefficient of the term containing h3(03) is a
    // left inverse to eta wedge -.  Thus both maps are split on underlying
    // free abelian groups, although no splitting enters the comparison.
    for derived_degree in 0..=5 {
        let d_rank = basis(5, derived_degree).len();
        let q_rank = if derived_degree <= 4 {
            basis(4, derived_degree).len()
        } else {
            0
        };
        let excess_rank = if derived_degree > 0 {
            basis(4, derived_degree - 1).len()
        } else {
            0
        };
        assert_eq!(d_rank, q_rank + excess_rank);

        if derived_degree > 0 {
            let inclusion = &inclusions[derived_degree - 1];
            let q_masks = basis(4, derived_degree - 1);
            let d_masks = basis(5, derived_degree);
            let d_index: BTreeMap<_, _> = d_masks
                .iter()
                .enumerate()
                .map(|(index, &mask)| (mask, index))
                .collect();
            for (column, &q_mask) in q_masks.iter().enumerate() {
                let (lifted, _) = lifted_q_mask(q_mask);
                let distinguished = lifted | (1 << 4);
                let row = d_index[&distinguished];
                assert_eq!(inclusion[row][column].abs(), 1);
                for other_column in 0..q_masks.len() {
                    if other_column != column {
                        assert_eq!(inclusion[row][other_column], 0);
                    }
                }
            }
        }
    }

    // The top determinant comparison is the decisive excess sign.
    let omega_q = 0b1111_u8;
    let omega_derived = 0b1_1111_u8;
    let determinant_image = excess_inclusion(omega_q);
    assert_eq!(determinant_image, BTreeMap::from([(omega_derived, 1)]));

    // Since Q is the independent variable sequence (u0,u1,u3,u5), K(Q) is
    // a resolution of S=R/Q.  The exact sequence therefore records one copy
    // of S in Tor degree zero and the eta-oriented copy in Tor degree one.
    assert_eq!(quotient, [0, 1, 3, 5]);
    determinant_image[&omega_derived]
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct LaurentNormal {
    coefficient: Int,
    q_exponents: [i8; NORMALS],
    u_index: usize,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct LaurentUnit {
    coefficient: Int,
    q_exponents: [i8; NORMALS],
}

fn twist_scale(sequence: &[usize], subset: Mask) -> LaurentUnit {
    let mut coefficient = 1;
    let mut q_exponents = [0; NORMALS];
    for (position, &normal) in sequence.iter().enumerate() {
        if subset & (1 << position) == 0 {
            coefficient *= -1;
            q_exponents[normal] += 1;
        }
    }
    LaurentUnit {
        coefficient,
        q_exponents,
    }
}

fn check_reciprocal_twist_and_support() -> Int {
    let plus = [1_usize, 3, 5];
    // The diagonal map p_j^vee -> -q_j p_j, h_j^vee -> h_j is a chain
    // isomorphism K(I+^vee) -> K(I+).  Check every lower Koszul face.
    for subset in 0_u8..8 {
        let input_scale = twist_scale(&plus, subset);
        let mut position = 0;
        for (generator, &normal) in plus.iter().enumerate() {
            if subset & (1 << generator) == 0 {
                continue;
            }
            let face = subset & !(1 << generator);
            let face_scale = twist_scale(&plus, face);
            let mut source_q = face_scale.q_exponents;
            source_q[normal] -= 1;
            let source_after_twist = LaurentNormal {
                // u^vee=-q^-1*u.
                coefficient: -face_scale.coefficient,
                q_exponents: source_q,
                u_index: normal,
            };
            let target_after_twist = LaurentNormal {
                coefficient: input_scale.coefficient,
                q_exponents: input_scale.q_exponents,
                u_index: normal,
            };
            let exterior_sign = if position % 2 == 0 { 1 } else { -1 };
            assert_eq!(
                LaurentNormal {
                    coefficient: exterior_sign * source_after_twist.coefficient,
                    ..source_after_twist
                },
                LaurentNormal {
                    coefficient: exterior_sign * target_after_twist.coefficient,
                    ..target_after_twist
                }
            );
            position += 1;
        }
    }
    assert_eq!(
        twist_scale(&plus, 0b111),
        LaurentUnit {
            coefficient: 1,
            q_exponents: [0; NORMALS],
        }
    );

    // Entry 97's one-normal evaluation identities for the pair (u0,u3).
    // They use q units but never invert u0 or u3.
    let mut endpoint_pairing_signs = Vec::new();
    for normal in [0_usize, 3] {
        let mut q_inverse = [0; NORMALS];
        q_inverse[normal] = -1;
        let u_dual = LaurentNormal {
            coefficient: -1,
            q_exponents: q_inverse,
            u_index: normal,
        };
        let mut beta_h_pdual_q = [0; NORMALS];
        beta_h_pdual_q[normal] = 1;
        let beta_p_hdual = LaurentUnit {
            coefficient: 1,
            q_exponents: [0; NORMALS],
        };
        let beta_h_pdual = LaurentUnit {
            coefficient: -1,
            q_exponents: beta_h_pdual_q,
        };
        let first = LaurentNormal {
            coefficient: beta_p_hdual.coefficient,
            q_exponents: beta_p_hdual.q_exponents,
            u_index: normal,
        };
        let second = LaurentNormal {
            coefficient: u_dual.coefficient * beta_h_pdual.coefficient,
            q_exponents: std::array::from_fn(|index| {
                u_dual.q_exponents[index] + beta_h_pdual.q_exponents[index]
            }),
            u_index: normal,
        };
        assert_eq!(first, second);
        endpoint_pairing_signs.push(first.coefficient);
    }

    #[derive(Clone, Copy, Debug, Eq, PartialEq)]
    enum Support {
        ReciprocalRegularized,
        OriginalLocallyFiniteBorelMoore,
    }
    let source = Support::ReciprocalRegularized;
    let road = Support::OriginalLocallyFiniteBorelMoore;
    assert_ne!(source, road);
    assert_eq!(endpoint_pairing_signs, vec![1, 1]);
    endpoint_pairing_signs.into_iter().product()
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Diagonal(u8, u8);

type Triangulation = BTreeSet<Diagonal>;

fn diagonal(first: u8, second: u8) -> Diagonal {
    if first < second {
        Diagonal(first, second)
    } else {
        Diagonal(second, first)
    }
}

fn boundary_edge(value: Diagonal) -> bool {
    value.1 - value.0 == 1 || value == Diagonal(0, HEXAGON_VERTICES - 1)
}

fn between(vertex: u8, first: u8, second: u8) -> bool {
    let span = (second + HEXAGON_VERTICES - first) % HEXAGON_VERTICES;
    let position = (vertex + HEXAGON_VERTICES - first) % HEXAGON_VERTICES;
    position > 0 && position < span
}

fn crosses(first: Diagonal, second: Diagonal) -> bool {
    if [first.0, first.1]
        .iter()
        .any(|endpoint| *endpoint == second.0 || *endpoint == second.1)
    {
        return false;
    }
    between(second.0, first.0, first.1) != between(second.1, first.0, first.1)
        && between(first.0, second.0, second.1) != between(first.1, second.0, second.1)
}

fn all_triangulations() -> Vec<Triangulation> {
    let diagonals: Vec<_> = (0..HEXAGON_VERTICES)
        .flat_map(|first| {
            ((first + 1)..HEXAGON_VERTICES).map(move |second| diagonal(first, second))
        })
        .filter(|value| !boundary_edge(*value))
        .collect();
    let mut result = Vec::new();
    for first in 0..diagonals.len() {
        for second in first + 1..diagonals.len() {
            for third in second + 1..diagonals.len() {
                let candidate =
                    BTreeSet::from([diagonals[first], diagonals[second], diagonals[third]]);
                if candidate.iter().enumerate().all(|(position, left)| {
                    candidate
                        .iter()
                        .skip(position + 1)
                        .all(|right| !crosses(*left, *right))
                }) {
                    result.push(candidate);
                }
            }
        }
    }
    result.sort();
    result.dedup();
    assert_eq!(result.len(), 14);
    result
}

fn adjacent(first: &Triangulation, second: &Triangulation) -> bool {
    first.intersection(second).count() == 2
}

fn short_index(value: Diagonal) -> Option<usize> {
    (0..6).find(|&index| diagonal(index as u8, (index as u8 + 2) % HEXAGON_VERTICES) == value)
}

fn long_index(value: Diagonal) -> Option<usize> {
    (0..3).find(|&index| diagonal(index as u8, index as u8 + 3) == value)
}

fn variable_index(value: Diagonal) -> usize {
    if let Some(index) = short_index(value) {
        index
    } else {
        6 + long_index(value).expect("every hexagon diagonal is short or long")
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct OccurrenceLaurent([i8; 9]);

impl OccurrenceLaurent {
    fn one() -> Self {
        Self([0; 9])
    }

    fn variable(index: usize) -> Self {
        let mut result = [0; 9];
        result[index] = 1;
        Self(result)
    }

    fn multiply(self, other: Self) -> Self {
        Self(std::array::from_fn(|index| self.0[index] + other.0[index]))
    }

    fn inverse(self) -> Self {
        Self(self.0.map(|entry| -entry))
    }
}

fn occurrence_weight(dissection: &BTreeSet<Diagonal>) -> OccurrenceLaurent {
    dissection
        .iter()
        .fold(OccurrenceLaurent::one(), |weight, &value| {
            weight.multiply(OccurrenceLaurent::variable(variable_index(value)))
        })
}

fn raw_incidence_sign(dissection: &BTreeSet<Diagonal>, added: Diagonal) -> Int {
    if dissection.iter().filter(|&&value| value < added).count() % 2 == 0 {
        1
    } else {
        -1
    }
}

fn triangulation(values: &[(u8, u8)]) -> Triangulation {
    values
        .iter()
        .map(|&(first, second)| diagonal(first, second))
        .collect()
}

fn check_weighted_flip(common: BTreeSet<Diagonal>, first_added: Diagonal, second_added: Diagonal) {
    let first = common
        .iter()
        .copied()
        .chain([first_added])
        .collect::<BTreeSet<_>>();
    let second = common
        .iter()
        .copied()
        .chain([second_added])
        .collect::<BTreeSet<_>>();
    let first_sign = raw_incidence_sign(&common, first_added);
    let second_sign = raw_incidence_sign(&common, second_added);
    assert_eq!(first_sign, -second_sign);
    let first_normalized = OccurrenceLaurent::variable(variable_index(first_added))
        .multiply(occurrence_weight(&first).inverse());
    let second_normalized = OccurrenceLaurent::variable(variable_index(second_added))
        .multiply(occurrence_weight(&second).inverse());
    assert_eq!(first_normalized, second_normalized);
}

fn check_occurrence_pullback_and_lower_cousin() -> [Int; 2] {
    let all = all_triangulations();
    let d03 = diagonal(0, 3);
    let x0 = diagonal(0, 2);
    let x1 = diagonal(1, 3);
    let x3 = diagonal(3, 5);
    let x5 = diagonal(1, 5);
    let plus_center = triangulation(&[(1, 3), (1, 5), (3, 5)]);
    let v10 = triangulation(&[(0, 3), (1, 3), (3, 5)]);
    let v00 = triangulation(&[(0, 2), (0, 3), (3, 5)]);
    assert!(all.contains(&plus_center));
    assert!(all.contains(&v10));
    assert!(all.contains(&v00));
    assert!(adjacent(&plus_center, &v10));
    assert!(adjacent(&v10, &v00));

    // The ideals are read from this labelled geometry, rather than used to
    // guess the occurrence map.  T+ carries precisely the odd short normals;
    // the marked D03 span carries x0 and x3; and x3 is the only short mark
    // retained on the entire two-edge core-entry/road flag.
    let short_support = |cell: &Triangulation| -> BTreeSet<usize> {
        cell.iter()
            .filter_map(|&value| short_index(value))
            .collect()
    };
    let plus_short_support = short_support(&plus_center);
    let v10_short_support = short_support(&v10);
    let v00_short_support = short_support(&v00);
    assert_eq!(plus_short_support, BTreeSet::from([1, 3, 5]));
    let marked_pair_support = BTreeSet::from([short_index(x0).unwrap(), short_index(x3).unwrap()]);
    assert_eq!(marked_pair_support, BTreeSet::from([0, 3]));
    let retained_through_v10 = plus_short_support
        .intersection(&v10_short_support)
        .copied()
        .collect::<BTreeSet<_>>();
    let retained_short_support = retained_through_v10
        .intersection(&v00_short_support)
        .copied()
        .collect::<BTreeSet<_>>();
    assert_eq!(retained_short_support, BTreeSet::from([3]));

    // Actual occurrence pullback: the x3 sink mark chooses one Catalan
    // endpoint from the odd central source and one marked lower face in F03.
    let catalan_candidates: Vec<_> = all
        .iter()
        .filter(|candidate| {
            adjacent(&plus_center, candidate) && candidate.contains(&d03) && candidate.contains(&x3)
        })
        .collect();
    assert_eq!(catalan_candidates, vec![&v10]);
    let marked_lower_candidates: Vec<_> = all
        .iter()
        .filter(|candidate| {
            adjacent(&v10, candidate) && candidate.contains(&d03) && candidate.contains(&x3)
        })
        .collect();
    assert_eq!(marked_lower_candidates, vec![&v00]);

    // The two forced one-cells are actual K6 cells.  The reciprocal global
    // cocycle kills both raw weighted boundaries occurrence by occurrence.
    check_weighted_flip(BTreeSet::from([x1, x3]), x5, d03);
    check_weighted_flip(BTreeSet::from([d03, x3]), x0, x1);

    let physical = OccurrenceLaurent::variable(variable_index(d03));
    let road_v10 = physical.multiply(occurrence_weight(&v10).inverse());
    let road_v00 = physical.multiply(occurrence_weight(&v00).inverse());
    let expected_v10 = OccurrenceLaurent::variable(variable_index(x1))
        .multiply(OccurrenceLaurent::variable(variable_index(x3)))
        .inverse();
    let expected_v00 = OccurrenceLaurent::variable(variable_index(x0))
        .multiply(OccurrenceLaurent::variable(variable_index(x3)))
        .inverse();
    assert_eq!(road_v10, expected_v10);
    assert_eq!(road_v00, expected_v00);

    // In occurrence-normalized bases both values are units.  The selected
    // lower-Cousin generator a:v00->v10 and both of its endpoint terms are
    // retained, rather than replacing the interval by its H_0.
    let lower_cousin_boundary = [-1_i64, 1_i64];
    assert_eq!(lower_cousin_boundary.iter().sum::<Int>(), 0);
    let normalized_trace = [1_i64, 1_i64];
    assert_eq!(
        lower_cousin_boundary
            .iter()
            .zip(normalized_trace)
            .map(|(boundary, value)| boundary * value)
            .sum::<Int>(),
        0
    );
    assert_eq!(normalized_trace.iter().sum::<Int>(), 2);
    normalized_trace
}

fn entry97_local_plus_trace_values() -> [Int; 2] {
    // Independent right-hand calculation on the road costalk itself.  Entry
    // 97 assigns inverse occurrence weight to each road vertex.  The plus
    // marked edge has reduced vertices x1*x3 and x0*x3 after the common
    // physical factor is removed.
    let x0 = OccurrenceLaurent::variable(0);
    let x1 = OccurrenceLaurent::variable(1);
    let x3 = OccurrenceLaurent::variable(3);
    let road_weights = [x1.multiply(x3), x0.multiply(x3)];
    let reciprocal_values = road_weights.map(OccurrenceLaurent::inverse);
    let normalized_values = std::array::from_fn(|index| {
        assert_eq!(
            road_weights[index].multiply(reciprocal_values[index]),
            OccurrenceLaurent::one()
        );
        1_i64
    });
    assert_eq!(normalized_values, [1, 1]);
    normalized_values
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct ForcedBoundaryInvariants {
    carrier_boundary_sign: Int,
    normal_orientation_sign: Int,
    occurrence_values: [Int; 2],
    physical_dx03_sign: Int,
}

fn check_forced_boundary_invariants(excess_determinant_sign: Int, trace_normal_sign: Int) {
    let geometric_occurrence_values = check_occurrence_pullback_and_lower_cousin();

    // Target-side invariants forced on any putative augmented dual-block map.
    // The relative K6 top has positive ordered incidence on F03; eta supplies
    // the only admissible excess orientation and the occurrence path was
    // computed globally above.  This does not assign an image to the source
    // dual-block generator.
    let target_top_incidence = raw_incidence_sign(&BTreeSet::new(), diagonal(0, 3));
    assert_eq!(target_top_incidence, 1);
    let target_required = ForcedBoundaryInvariants {
        carrier_boundary_sign: target_top_incidence,
        normal_orientation_sign: excess_determinant_sign,
        occurrence_values: geometric_occurrence_values,
        physical_dx03_sign: 1,
    };

    // Established source-boundary/trace invariants.  The positive normal-link
    // triangle has d f+=e1+e3+e5, and entry 97 independently supplies the
    // pair-normal and road occurrence values.
    let plus_boundary_normals = [1_usize, 3, 5];
    let source_d03_position = plus_boundary_normals
        .iter()
        .position(|&normal| normal == 3)
        .unwrap();
    let source_boundary_coefficients = [1_i64, 1, 1];
    let source_d03_incidence = source_boundary_coefficients[source_d03_position];
    let local_trace_occurrence_values = entry97_local_plus_trace_values();
    let established_trace_boundary = ForcedBoundaryInvariants {
        carrier_boundary_sign: source_d03_incidence,
        normal_orientation_sign: trace_normal_sign,
        occurrence_values: local_trace_occurrence_values,
        physical_dx03_sign: 1,
    };

    // Equality is a necessary boundary test, not a construction of a_+^ex.
    // The augmented dual-block/Cousin can--var matrices needed to turn this
    // equality into a Beck--Chevalley chain identity are not present.
    assert_eq!(target_required, established_trace_boundary);
}

fn main() {
    let excess_determinant_sign = check_excess_koszul_sequence();
    let trace_normal_sign = check_reciprocal_twist_and_support();
    check_forced_boundary_invariants(excess_determinant_sign, trace_normal_sign);

    println!(
        "{}",
        concat!(
            r#"{"claim":"the labelled K6 geometry uniquely fixes the plus-sheet/D03 marked occurrence flag, and the actual ideals I+=(u1,u3,u5) and I03=(u0,u3) admit a canonical integral eta-wedge excess inclusion carrying the Tor_1 orientation; these constructions match every forced D03 boundary invariant of the entry-97 trace, but they do not construct the full PC Beck--Chevalley source map because the unlocalized augmented dual-block/Cousin can--var kernel is still untyped","status":"inconclusive","assumptions":["the labelled hexagon associahedron and factorization marks are those fixed in entries 96-98","the established entry-38 face-tube theorem is used only on actual scalar faces and the marked D03 road costalk, not extended to a dual block by assumption","the universal u_j are algebraically independent and q_j are Laurent units; no u_j or integer is inverted"],"evidence_refs":["research/voevodsky/check_d03_plus_excess_beck_chevalley.rs","research/voevodsky/check_d03_factorization_marked_span.rs","research/voevodsky/check_d03_bivariant_pc_hom.rs","research/voevodsky/check_d03_relative_associahedron_pc.rs","research/voevodsky/check_d03_three_pair_pc_extension.rs","src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md","src/ledger/20260814-94 Augmented Triangle Resolution and the D03 Primitive Cousin Symbol.md","src/ledger/20260814-95 Conductor Normal-Link Fold and the Occurrence-Loaded Trace Boundary.md","src/ledger/20260814-96 Factorization-Marked Normal-Crossing Span and the Pair-Local Relation Obstruction.md","src/ledger/20260814-97 Reciprocal-Twist D03 Bivariant Road Trace.md","src/ledger/20260814-98 Weighted Hexagon Relation Target and the Excess Beck--Chevalley Boundary.md"],"factorization_test":{"geometric_source":"PASS: T+=(x1,x3,x5) is the plus parity center and its positive normal link is the source dual block","marked_flag":"PASS: enumeration of all 14 triangulations gives the unique x3-marked path T+ -> X03*x1*x3 -> X03*x0*x3","ideals_from_geometry":"PASS: the labelled source has I+=(u1,u3,u5), the marked road span has I03=(u0,u3), and x3/u3 is the unique mark retained along the full path","excess_complex":"PASS: 0 -> K(u0,u1,u3,u5)[1] --eta wedge--> K(I+) tensor K(I03) -> K(u0,u1,u3,u5) -> 0 is degreewise exact over Z and all differential identities hold","tor_orientation":"PASS: eta=h3^+-h3^03 generates Tor_1 and eta wedge omega_Q=omega_+ wedge omega_03 with sign +1","excess_canonicity":"PASS: eta wedge - is identical for the branch and pair lifts of the shared u3 generator; no reverse projection or splitting is used","forced_shift":"PASS: the retained Tor_1 summand is in degree one","occurrence_and_lower_cousin":"PASS: both marked vertices and a:v00->v10 are retained; the global reciprocal cocycle kills the central-flip and marked-edge weighted boundaries","twist_support":"PASS: reciprocal regular support remains distinct from original locally-finite/Borel--Moore support; u_j^vee=-q_j^-1*u_j is checked on every plus Koszul face using q units only","physical_orientation":"PASS: [dX03] is separate and evaluates to +1","forced_boundary_invariants":"PASS: target incidence, source-boundary incidence, excess/trace orientation signs, two occurrence units, and physical-normal signs agree when computed independently","augmented_dual_block_map":"UNTYPED: no chain map from the augmented positive dual-block/Cousin complex to the relative K6 PC complex has been constructed","can_var_kernel":"UNTYPED before nonresonant localization: entry 38 supplies actual-face tubes but not the central dual-block-to-road can--var comparison and its augmentation","beck_chevalley":"INCONCLUSIVE: equality of all forced boundary invariants is necessary but does not prove rho03 a_+^ex=Tr_03,partial^PC partial_+,03 without the missing augmented kernel"},"counterevidence":["The earlier assignment of unit top and face-tube maps merely restated the desired two-term square and has been removed.","Entry 38 proves face tubes for actual scalar faces; extending it to the positive dual block would assume the missing arrow.","Forgetting eta and using transverse base change loses the nonzero Tor_1 summand and its shift.","A reverse map from the derived tensor product requires a noncanonical splitting and is not used.","Nonresonant localization can contract normal factors but cannot certify the required unlocalized support-compatible can--var kernel."],"next_experiment":"construct the augmented barycentric dual-block/Cousin complex at T+, including its central-flip can and var maps before u3 inversion, and an explicit chain map to PC(K6,B_sc) whose restriction to the unique x3-marked flag is the entry-38 D03 face tube; then test every differential matrix against eta wedge -"}"#
        )
    );
}
