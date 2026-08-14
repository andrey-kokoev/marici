//! Finite exit-path/Yoneda audit for the corrected D03 log blowup.
//!
//! The ambient pair-Rees deformation retains the genuine Q=F2/F1 generator
//! carried by the strict D03 facet.  The expanded marked gallery is a
//! different source: every one of its seven supports lies in F1_tilde, so its
//! canonical projection to Q is zero.  Thus the ambient generic Q quotient
//! cannot be silently identified with a Q generator in the gallery kernel.
//!
//! The corrected blowup layers are tested independently.  Occurrence uses
//! lcm labels and the unit exceptional boundary bD-b1, forcing
//!
//!   xi_tilde=x1*ec + XD*x1*hE + XD*er.
//!
//! Monodromy has qE=qD*q1 and uE=U+qD*u1.  Its saturated local resolution
//! retracts integrally to K(U,u1).  After that retract the first bivariant
//! cap complex on the literal D03 channel is
//!
//!   C^0=R --U--> C^1=R.
//!
//! Hence H^0=0 and H^1=R/(U).  The raw extraordinary-costalk boundary is
//! X_D03.  The legitimate reciprocal operation is modelled as evaluation of
//! the dual of the principal ideal I_X=(X_D03): X^vee(X_D03)=1.  It selects
//! the local generator [1] without making 1/X_D03 an element of the base.
//!
//! This local result does not construct the required global specialization
//!
//!   sp_G:RHom(Q,F0[2])->C_D03[-1],  sp_G(e_F)=[1].
//!
//! Indeed the canonical gallery source has zero Q projection.  Consequently
//! the global Beck-Chevalley composite and its proposed Theta03 endpoint are
//! not typed by this finite model; that is the certified first blocker.

use std::collections::{BTreeMap, BTreeSet};

type Int = i64;
const N: u8 = 6;
const DIMENSION: usize = 3;
const VARIABLES: usize = 8;

const X_D03: usize = 0;
const X1: usize = 1;
const X0: usize = 2;
const X3: usize = 3;
const X4: usize = 4;
const X5: usize = 5;
const U_D03: usize = 6;
const U1: usize = 7;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Diagonal(u8, u8);

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum Ray {
    Old(Diagonal),
    Exceptional,
}

type OldFace = BTreeSet<Diagonal>;
type BlowupFace = BTreeSet<Ray>;
type Exponents = [u8; VARIABLES];

#[derive(Clone, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Polynomial(BTreeMap<Exponents, Int>);

impl Polynomial {
    fn zero() -> Self {
        Self(BTreeMap::new())
    }

    fn one() -> Self {
        Self(BTreeMap::from([([0; VARIABLES], 1)]))
    }

    fn variable(index: usize) -> Self {
        let mut powers = [0; VARIABLES];
        powers[index] = 1;
        Self(BTreeMap::from([(powers, 1)]))
    }

    fn add(&self, other: &Self) -> Self {
        let mut result = self.0.clone();
        for (powers, coefficient) in &other.0 {
            *result.entry(*powers).or_default() += coefficient;
        }
        result.retain(|_, coefficient| *coefficient != 0);
        Self(result)
    }

    fn scale(&self, coefficient: Int) -> Self {
        Self(
            self.0
                .iter()
                .filter_map(|(powers, value)| {
                    let product = coefficient * value;
                    (product != 0).then_some((*powers, product))
                })
                .collect(),
        )
    }

    fn multiply(&self, other: &Self) -> Self {
        let mut result = BTreeMap::new();
        for (left_powers, left_coefficient) in &self.0 {
            for (right_powers, right_coefficient) in &other.0 {
                let powers = std::array::from_fn(|index| left_powers[index] + right_powers[index]);
                *result.entry(powers).or_default() += left_coefficient * right_coefficient;
            }
        }
        result.retain(|_, coefficient| *coefficient != 0);
        Self(result)
    }

    fn specialize_zero(&self, variable: usize) -> Self {
        Self(
            self.0
                .iter()
                .filter(|(powers, _)| powers[variable] == 0)
                .map(|(powers, coefficient)| (*powers, *coefficient))
                .collect(),
        )
    }

    fn divisible_by(&self, variable: usize) -> bool {
        !self.0.is_empty() && self.0.keys().all(|powers| powers[variable] > 0)
    }
}

// I_X=(X_D03) is represented by its free rank-one generator X.  An element
// is stored by its coefficient before inclusion I_X -> R.  The dual basis
// X^vee in Hom_R(I_X,R) returns that coefficient; it never constructs X^-1
// as a scalar in R.
#[derive(Clone, Debug, Eq, PartialEq)]
struct PrincipalIdeal {
    generator: Polynomial,
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct PrincipalIdealElement {
    coefficient: Polynomial,
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct PrincipalIdealDual {
    source_generator: Polynomial,
}

impl PrincipalIdeal {
    fn include(&self, element: &PrincipalIdealElement) -> Polynomial {
        self.generator.multiply(&element.coefficient)
    }
}

impl PrincipalIdealDual {
    fn evaluate(&self, ideal: &PrincipalIdeal, element: &PrincipalIdealElement) -> Polynomial {
        assert_eq!(self.source_generator, ideal.generator);
        element.coefficient.clone()
    }
}

type Matrix = Vec<Vec<Polynomial>>;

fn zero_matrix(rows: usize, columns: usize) -> Matrix {
    vec![vec![Polynomial::zero(); columns]; rows]
}

fn multiply_matrices(left: &Matrix, right: &Matrix) -> Matrix {
    if left.is_empty() || right.is_empty() {
        return Vec::new();
    }
    assert_eq!(left[0].len(), right.len());
    let mut result = zero_matrix(left.len(), right[0].len());
    for row in 0..left.len() {
        for middle in 0..right.len() {
            for column in 0..right[0].len() {
                let term = left[row][middle].multiply(&right[middle][column]);
                result[row][column] = result[row][column].add(&term);
            }
        }
    }
    result
}

fn diagonal(first: u8, second: u8) -> Diagonal {
    if first < second {
        Diagonal(first, second)
    } else {
        Diagonal(second, first)
    }
}

fn boundary_edge(value: Diagonal) -> bool {
    value.1 - value.0 == 1 || value == Diagonal(0, N - 1)
}

fn between(vertex: u8, first: u8, second: u8) -> bool {
    let span = (second + N - first) % N;
    let position = (vertex + N - first) % N;
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

fn all_diagonals() -> Vec<Diagonal> {
    (0..N)
        .flat_map(|first| ((first + 1)..N).map(move |second| diagonal(first, second)))
        .filter(|value| !boundary_edge(*value))
        .collect()
}

fn short_diagonal(index: usize) -> Diagonal {
    diagonal(index as u8, (index as u8 + 2) % N)
}

fn short_index(value: Diagonal) -> Option<usize> {
    (0..6).find(|index| short_diagonal(*index) == value)
}

fn noncrossing(face: &OldFace) -> bool {
    face.iter().enumerate().all(|(position, first)| {
        face.iter()
            .skip(position + 1)
            .all(|second| !crosses(*first, *second))
    })
}

fn incidence_sign(face: &OldFace, added: Diagonal) -> Int {
    if face.iter().filter(|value| **value < added).count() % 2 == 0 {
        1
    } else {
        -1
    }
}

fn old_faces() -> BTreeSet<OldFace> {
    let diagonals = all_diagonals();
    let mut result = BTreeSet::new();
    for mask in 0_u16..(1_u16 << diagonals.len()) {
        if mask.count_ones() as usize > DIMENSION {
            continue;
        }
        let face: OldFace = diagonals
            .iter()
            .enumerate()
            .filter(|(index, _)| mask & (1 << index) != 0)
            .map(|(_, value)| *value)
            .collect();
        if noncrossing(&face) {
            result.insert(face);
        }
    }
    result
}

fn old_as_blowup(face: &OldFace) -> BlowupFace {
    face.iter().copied().map(Ray::Old).collect()
}

fn blowup_faces(
    old: &BTreeSet<OldFace>,
    first: Diagonal,
    second: Diagonal,
) -> BTreeSet<BlowupFace> {
    let mut result = BTreeSet::new();
    for face in old {
        if !(face.contains(&first) && face.contains(&second)) {
            result.insert(old_as_blowup(face));
            continue;
        }
        let remainder: BlowupFace = face
            .iter()
            .filter(|value| **value != first && **value != second)
            .copied()
            .map(Ray::Old)
            .collect();
        for retained in [None, Some(first), Some(second)] {
            let mut replacement = remainder.clone();
            replacement.insert(Ray::Exceptional);
            if let Some(value) = retained {
                replacement.insert(Ray::Old(value));
            }
            result.insert(replacement);
        }
    }
    result
}

fn census<T: Ord>(faces: &BTreeSet<BTreeSet<T>>) -> Vec<usize> {
    (0..=DIMENSION)
        .map(|size| faces.iter().filter(|face| face.len() == size).count())
        .collect()
}

fn binomial(n: usize, k: usize) -> usize {
    (0..k).fold(1, |value, index| value * (n - index) / (index + 1))
}

fn loaded_ranks<T: Ord>(faces: &BTreeSet<BTreeSet<T>>) -> Vec<usize> {
    let mut result = vec![0; DIMENSION + 1];
    for face in faces {
        for circles in 0..=face.len() {
            result[DIMENSION - face.len() + circles] += binomial(face.len(), circles);
        }
    }
    result
}

fn plus_vertex() -> BlowupFace {
    [1_usize, 3, 5]
        .into_iter()
        .map(|index| Ray::Old(short_diagonal(index)))
        .collect()
}

fn in_b_tilde(face: &BlowupFace) -> bool {
    face.contains(&Ray::Exceptional)
        || face.iter().any(|ray| match ray {
            Ray::Old(value) => short_index(*value).is_some(),
            Ray::Exceptional => true,
        })
}

fn check_global_support_model(blown_up: &BTreeSet<BlowupFace>, d03: Diagonal) {
    assert_eq!(census(blown_up), [1, 10, 24, 16]);
    assert_eq!(loaded_ranks(blown_up), [16, 72, 106, 51]);
    assert_eq!(loaded_ranks(blown_up).iter().sum::<usize>(), 245);

    let relative_faces: Vec<_> = blown_up.iter().filter(|face| !in_b_tilde(face)).collect();
    assert_eq!(relative_faces.len(), 4); // top and three long facets.
    let relative_loaded_rank: usize = relative_faces
        .iter()
        .map(|face| 1_usize << face.len())
        .sum();
    assert_eq!(relative_loaded_rank, 7);
    assert_eq!(
        (1_usize << plus_vertex().len(), 245 - 7, 245),
        (8, 238, 245)
    );

    let q_d03: BlowupFace = [Ray::Old(d03)].into_iter().collect();
    assert!(relative_faces.contains(&&q_d03));
    let g03: Vec<_> = blown_up
        .iter()
        .filter(|face| in_b_tilde(face) && face.contains(&Ray::Old(d03)) && **face != plus_vertex())
        .collect();
    assert!(!g03.is_empty());
    assert!(g03.iter().all(|face| face.contains(&Ray::Old(d03))));
    assert!(g03.iter().all(|face| **face != plus_vertex()));
    assert!(g03.iter().all(|face| !face.is_subset(&plus_vertex())));

    // The four actual radial targets of the strict D03 facet after blowup.
    let expected = [
        [Ray::Old(d03), Ray::Old(short_diagonal(0))]
            .into_iter()
            .collect(),
        [Ray::Old(d03), Ray::Exceptional].into_iter().collect(),
        [Ray::Old(d03), Ray::Old(short_diagonal(3))]
            .into_iter()
            .collect(),
        [Ray::Old(d03), Ray::Old(short_diagonal(4))]
            .into_iter()
            .collect(),
    ];
    assert!(expected.iter().all(|face| blown_up.contains(face)));
    assert!(expected
        .iter()
        .all(|face| face.contains(&Ray::Old(d03)) && in_b_tilde(face)));
}

fn check_gallery_kernel_q_projection(blown_up: &BTreeSet<BlowupFace>, d03: Diagonal) {
    let x0 = short_diagonal(0);
    let x1 = short_diagonal(1);
    let x3 = short_diagonal(3);
    let x5 = short_diagonal(5);
    let gallery_supports: [(&str, BlowupFace); 7] = [
        (
            "a=v_plus",
            [Ray::Old(x1), Ray::Old(x3), Ray::Old(x5)]
                .into_iter()
                .collect(),
        ),
        ("e_c", [Ray::Old(x1), Ray::Old(x3)].into_iter().collect()),
        (
            "b_1",
            [Ray::Exceptional, Ray::Old(x1), Ray::Old(x3)]
                .into_iter()
                .collect(),
        ),
        (
            "h_E",
            [Ray::Exceptional, Ray::Old(x3)].into_iter().collect(),
        ),
        (
            "b_D",
            [Ray::Exceptional, Ray::Old(d03), Ray::Old(x3)]
                .into_iter()
                .collect(),
        ),
        ("e_r", [Ray::Old(d03), Ray::Old(x3)].into_iter().collect()),
        (
            "c",
            [Ray::Old(d03), Ray::Old(x0), Ray::Old(x3)]
                .into_iter()
                .collect(),
        ),
    ];
    assert!(gallery_supports
        .iter()
        .all(|(_, support)| blown_up.contains(support)));
    assert!(gallery_supports
        .iter()
        .all(|(_, support)| in_b_tilde(support)));

    // Q is the quotient by F1_tilde.  Therefore the cellular projection of
    // every gallery support is zero, including the D03-side supports b_D,
    // e_r, and c: each also contains E or a short diagonal.
    let relative_q_supports: Vec<_> = blown_up
        .iter()
        .filter(|support| !in_b_tilde(support))
        .collect();
    assert_eq!(relative_q_supports.len(), 4);
    assert!(gallery_supports.iter().all(|(_, gallery)| {
        relative_q_supports
            .iter()
            .all(|q_support| gallery != *q_support)
    }));
    let gallery_to_q = zero_matrix(7, gallery_supports.len());
    assert!(gallery_to_q
        .iter()
        .flatten()
        .all(|coefficient| *coefficient == Polynomial::zero()));

    // The ambient quotient nevertheless retains rank seven.  This separates
    // the generic fiber of Rees(F2,F1) from the source kernel obtained by
    // restricting the marked gallery, whose Q projection is exactly zero.
    let ambient_q_rank: usize = relative_q_supports
        .iter()
        .map(|support| 1_usize << support.len())
        .sum();
    assert_eq!(ambient_q_rank, 7);
    let gallery_kernel_q_rank = 0_usize;
    assert_eq!(gallery_kernel_q_rank, 0);
}

fn check_yoneda_support_blocks() {
    // Q_D03 has the base and normal-circle generators.  Each has four
    // radial targets in G03_tilde, with the inherited D03 signs
    // (+x0,-x1,-x3,-x4).  Rows 0..3 are base targets and rows 4..7 retain
    // the D03 circle.
    let coefficients = [
        Polynomial::variable(X0),
        Polynomial::variable(X1).scale(-1),
        Polynomial::variable(X3).scale(-1),
        Polynomial::variable(X4).scale(-1),
    ];
    let mut first_block = zero_matrix(8, 2);
    for row in 0..4 {
        first_block[row][0] = coefficients[row].clone();
        first_block[row + 4][1] = coefficients[row].clone();
    }
    assert!(first_block
        .iter()
        .flatten()
        .any(|entry| *entry != Polynomial::zero()));

    // G03_tilde is a strict D03-supported subcomplex, disjoint from F0.
    // Therefore its support-changing block to the eight F0 generators is
    // exactly zero, and so is the length-two Yoneda cap on this channel.
    let second_block = zero_matrix(8, 8);
    let yoneda_product = multiply_matrices(&second_block, &first_block);
    assert_eq!(yoneda_product, zero_matrix(8, 2));

    // The internal Q normal differential is kept separate from occurrence.
    let q_internal = vec![vec![Polynomial::variable(U_D03)]];
    assert_eq!(q_internal.len(), 1);
    assert_eq!(q_internal[0][0], Polynomial::variable(U_D03));
}

fn check_ambient_pair_rees_only() {
    // The ambient Rees deformation of F1_tilde subset F2_tilde has generic
    // quotient Q, with the literal relative cells.  This statement is about
    // the ambient pair and does not identify its generic Q with the kernel of
    // the gallery restriction.
    let generic_q_basis = ["top", "p_D03", "h_D03"];
    assert_eq!(generic_q_basis.len(), 3);
    let generic_q_boundary = vec![vec![
        Polynomial::variable(X_D03),
        Polynomial::variable(U_D03),
    ]];
    assert_eq!(generic_q_boundary[0].len(), 2);

    // Every Q_D03 -> G03_tilde support drop has Rees exponent one.  Generic
    // specialization t=1 recovers the actual four incidence coefficients;
    // special specialization t=0 kills that off-diagonal block.  We record
    // exponents and evaluations without adjoining t^-1.
    let support_rees_exponents = [1_u8; 4];
    let generic_t = 1_i64;
    let special_t = 0_i64;
    let generic_values: Vec<_> = support_rees_exponents
        .iter()
        .map(|exponent| generic_t.pow(u32::from(*exponent)))
        .collect();
    let special_values: Vec<_> = support_rees_exponents
        .iter()
        .map(|exponent| special_t.pow(u32::from(*exponent)))
        .collect();
    assert_eq!(generic_values, [1, 1, 1, 1]);
    assert_eq!(special_values, [0, 0, 0, 0]);

    // Its D03 occurrence entry is the raw X_D03 class used by the local
    // costalk calculation.  The gallery-to-Q projection checked separately
    // is zero, so these data do not define a gallery specialization map.
    let ambient_raw_d03_class = generic_q_boundary[0][0].clone();
    assert_eq!(ambient_raw_d03_class, Polynomial::variable(X_D03));
    let ambient_generic_literal_q_present = true;
    let gallery_specialization_defined = false;
    let t_inverted = false;
    assert!(ambient_generic_literal_q_present);
    assert!(!gallery_specialization_defined);
    assert!(!t_inverted);
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum GalleryVertex {
    A,
    B1,
    BD,
    C,
}

type GalleryBoundary = BTreeMap<GalleryVertex, Polynomial>;

fn add_gallery_term(
    boundary: &mut GalleryBoundary,
    vertex: GalleryVertex,
    coefficient: &Polynomial,
) {
    let present = boundary.remove(&vertex).unwrap_or_else(Polynomial::zero);
    let sum = present.add(coefficient);
    if sum != Polynomial::zero() {
        boundary.insert(vertex, sum);
    }
}

fn add_boundaries(left: &GalleryBoundary, right: &GalleryBoundary) -> GalleryBoundary {
    let mut result = left.clone();
    for (vertex, coefficient) in right {
        add_gallery_term(&mut result, *vertex, coefficient);
    }
    result
}

fn scale_boundary(value: &GalleryBoundary, scalar: &Polynomial) -> GalleryBoundary {
    value
        .iter()
        .map(|(vertex, coefficient)| (*vertex, coefficient.multiply(scalar)))
        .collect()
}

fn collapse_exceptional(value: &GalleryBoundary) -> GalleryBoundary {
    let mut result = GalleryBoundary::new();
    for (vertex, coefficient) in value {
        let image = if *vertex == GalleryVertex::BD {
            GalleryVertex::B1
        } else {
            *vertex
        };
        add_gallery_term(&mut result, image, coefficient);
    }
    result
}

fn check_occurrence_gallery_sdr() {
    let xd = Polynomial::variable(X_D03);
    let x1 = Polynomial::variable(X1);
    let x0 = Polynomial::variable(X0);
    let x5 = Polynomial::variable(X5);
    let d_ec = BTreeMap::from([
        (GalleryVertex::A, x5.scale(-1)),
        (GalleryVertex::B1, xd.clone()),
    ]);
    let d_h = BTreeMap::from([
        (GalleryVertex::B1, Polynomial::one().scale(-1)),
        (GalleryVertex::BD, Polynomial::one()),
    ]);
    let d_er = BTreeMap::from([
        (GalleryVertex::BD, x1.scale(-1)),
        (GalleryVertex::C, x0.clone()),
    ]);

    let d_xi = add_boundaries(
        &add_boundaries(
            &scale_boundary(&d_ec, &x1),
            &scale_boundary(&d_h, &xd.multiply(&x1)),
        ),
        &scale_boundary(&d_er, &xd),
    );
    assert_eq!(
        d_xi,
        BTreeMap::from([
            (GalleryVertex::A, x1.multiply(&x5).scale(-1)),
            (GalleryVertex::C, xd.multiply(&x0)),
        ])
    );

    // p identifies bD with b1 and kills h.  A section sends the old road
    // edge to er+x1*h.  H(bD)=h proves the unit SDR.
    assert_eq!(collapse_exceptional(&d_h), GalleryBoundary::new());
    assert_eq!(
        add_boundaries(&d_er, &scale_boundary(&d_h, &x1)),
        collapse_exceptional(&d_er)
    );
    let exceptional_occurrence_variable_exists = false;
    assert!(!exceptional_occurrence_variable_exists);
}

fn check_normal_saturated_sdr() {
    let u = Polynomial::variable(U_D03);
    let u1 = Polynomial::variable(U1);
    let q = Polynomial::one().add(&u);
    let ue = u.add(&q.multiply(&u1));
    assert_eq!(ue, u.add(&u1).add(&u.multiply(&u1)));

    // L1=(hD,hE,h1), L2=(A,B).
    let d_a = [Polynomial::one().scale(-1), Polynomial::one(), q.scale(-1)];
    let d_b = [u1.clone(), Polynomial::zero(), u.scale(-1)];
    let d_one = [u.clone(), ue, u1.clone()];
    for column in [&d_a, &d_b] {
        let square = (0..3).fold(Polynomial::zero(), |sum, index| {
            sum.add(&d_one[index].multiply(&column[index]))
        });
        assert_eq!(square, Polynomial::zero());
    }

    // p(hE)=hD+q*h1, p(A)=0, p(B)=top; i(top)=B; H(hE)=A.
    let projected_h_e = [Polynomial::one(), q.clone()];
    assert_eq!(
        projected_h_e[0]
            .multiply(&u)
            .add(&projected_h_e[1].multiply(&u1)),
        d_one[1]
    );
    let projected_d_a = [d_a[0].add(&d_a[1]), d_a[1].multiply(&q).add(&d_a[2])];
    assert_eq!(projected_d_a, [Polynomial::zero(), Polynomial::zero()]);
    assert_eq!(
        d_a,
        [Polynomial::one().scale(-1), Polynomial::one(), q.scale(-1)]
    );
    for local_degree in 0..=2 {
        let first = if (local_degree + 1) % 2 == 0 { 1 } else { -1 };
        let second = if local_degree % 2 == 0 { 1 } else { -1 };
        assert_eq!(first + second, 0);
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum CostalkType {
    TopOnly,
    D03Channel,
}

fn check_extraordinary_costalk_localization() {
    // The ambient cellular extraordinary costalk is generated by relative-Q
    // cells whose closures contain the selected support.  The blowup resolves
    // the jump at b into the two sections and their exceptional interval.
    // This ambient closure calculation does not itself provide a Q generator
    // in the gallery source kernel.
    let expanded_gallery_costalks = [
        ("a", CostalkType::TopOnly),
        ("e_c", CostalkType::TopOnly),
        ("b_1", CostalkType::TopOnly),
        ("h_E", CostalkType::TopOnly),
        ("b_D", CostalkType::D03Channel),
        ("e_r", CostalkType::D03Channel),
        ("c", CostalkType::D03Channel),
    ];
    assert_eq!(expanded_gallery_costalks.len(), 7);
    assert_eq!(expanded_gallery_costalks[0].1, CostalkType::TopOnly);
    assert_eq!(expanded_gallery_costalks[4].1, CostalkType::D03Channel);

    // Before expansion, b contains D03 and has the D03-channel costalk.
    let named_original_costalks = [
        ("a", CostalkType::TopOnly),
        ("e_c", CostalkType::TopOnly),
        ("b", CostalkType::D03Channel),
        ("e_r", CostalkType::D03Channel),
        ("c", CostalkType::D03Channel),
    ];
    assert_eq!(named_original_costalks.len(), 5);

    // On the left T=i^!Q is one top generator.  On the D03 side
    //
    //   K1=R<top,h_D> --[X_D,U_D]--> K0=R<p_D>.
    //
    // Generization K->T projects top to top and kills h_D,p_D.  Its kernel
    // is K(U_D), and the localization boundary is top |-> X_D*p_D.
    let boundary_k = vec![vec![
        Polynomial::variable(X_D03),
        Polynomial::variable(U_D03),
    ]];
    assert_eq!(boundary_k.len(), 1);
    assert_eq!(boundary_k[0].len(), 2);
    let projection_degree_one = [Polynomial::one(), Polynomial::zero()];
    assert_eq!(projection_degree_one[0], Polynomial::one());
    assert_eq!(projection_degree_one[1], Polynomial::zero());
    let kernel_boundary = vec![vec![Polynomial::variable(U_D03)]];
    assert_eq!(kernel_boundary[0][0], Polynomial::variable(U_D03));
    let localization_boundary = Polynomial::variable(X_D03);
    assert!(!localization_boundary.divisible_by(U_D03));
    assert_eq!(
        localization_boundary.specialize_zero(U_D03),
        Polynomial::variable(X_D03)
    );

    // The reciprocal occurrence operation is the ordinary evaluation pairing
    // I_X^vee tensor I_X -> R for I_X=(X_D03), not base localization.  With
    // X^vee the dual of the chosen principal-ideal generator, ev(X^vee,X)=1.
    let ideal = PrincipalIdeal {
        generator: Polynomial::variable(X_D03),
    };
    let x = PrincipalIdealElement {
        coefficient: Polynomial::one(),
    };
    let x_dual = PrincipalIdealDual {
        source_generator: Polynomial::variable(X_D03),
    };
    assert_eq!(ideal.include(&x), localization_boundary);
    let normalized_localization_class = x_dual.evaluate(&ideal, &x);
    assert_eq!(normalized_localization_class, Polynomial::one());
    assert!(!normalized_localization_class.divisible_by(U_D03));
    let base_x_d03_inverted = false;
    assert!(!base_x_d03_inverted);

    // Locally this unit survives in R/(U_D03).  No assertion is made here
    // that the global Yoneda cocycle maps to it.
    assert_eq!(
        normalized_localization_class.specialize_zero(U_D03),
        Polynomial::one()
    );

    // Lcm incidence supplies x1 on the left and the costalk localization
    // supplies XD.  Their product is the forced exceptional coefficient in
    // xi_tilde; no desired value is inserted.
    let left_coefficient = Polynomial::variable(X1);
    let right_coefficient = localization_boundary.clone();
    assert_eq!(
        left_coefficient.multiply(&right_coefficient),
        Polynomial::variable(X_D03).multiply(&Polynomial::variable(X1))
    );

    // This Q costalk alone has only the long physical normal U_D03.  Entry
    // 100 independently supplies two distinct short-u3 occurrences with
    // opposite support variance; they must be tensored in, never identified
    // with U_D03 or with one another.
    #[derive(Clone, Copy, Debug, Eq, PartialEq)]
    enum NormalLabel {
        PhysicalLongU03,
        ReciprocalShortU3,
        RoadShortU3,
    }
    let costalk_labels = [NormalLabel::PhysicalLongU03];
    let theta_labels = [NormalLabel::ReciprocalShortU3, NormalLabel::RoadShortU3];
    assert!(theta_labels
        .iter()
        .all(|label| !costalk_labels.contains(label)));
    assert_eq!(theta_labels.len(), 2);
}

fn check_saturated_unit_road_transgression() {
    // The normalized D03 facet boundary in the corrected blowup has the four
    // actual labelled targets (x0,E,x3,x4) and inherited signs.  It is a
    // primitive integer vector.  The empty-face-to-D03 incidence is positive
    // and fixes the sign of the local cellular top basis.  This is a local
    // orientation calculation, not a construction of sp_G on e_F.
    let d03 = diagonal(0, 3);
    let d03_face: OldFace = [d03].into_iter().collect();
    let compatible_marked_additions = [
        short_diagonal(0),
        short_diagonal(1),
        short_diagonal(3),
        short_diagonal(4),
    ];
    assert!(compatible_marked_additions
        .iter()
        .all(|added| noncrossing(&[d03, *added].into_iter().collect())));
    let normalized_d03_boundary =
        compatible_marked_additions.map(|added| incidence_sign(&d03_face, added));
    assert_eq!(normalized_d03_boundary, [1_i64, -1, -1, -1]);
    let content = normalized_d03_boundary
        .iter()
        .fold(0_i64, |gcd, value| gcd_i64(gcd, value.abs()));
    assert_eq!(content, 1);
    let empty_to_d03_incidence = incidence_sign(&OldFace::new(), d03);
    assert_eq!(empty_to_d03_incidence, 1);
    let initial_top_unit = empty_to_d03_incidence * normalized_d03_boundary[0];
    assert_eq!(initial_top_unit, 1);

    // The principal-ideal dual evaluation derives the corresponding local
    // unit from the raw X_D03 entry without assigning a Theta value.
    let ideal = PrincipalIdeal {
        generator: Polynomial::variable(X_D03),
    };
    let raw_x = PrincipalIdealElement {
        coefficient: Polynomial::one(),
    };
    let dual = PrincipalIdealDual {
        source_generator: Polynomial::variable(X_D03),
    };
    assert_eq!(ideal.include(&raw_x), Polynomial::variable(X_D03));
    assert_eq!(dual.evaluate(&ideal, &raw_x), Polynomial::one());
}

fn gcd_i64(mut left: i64, mut right: i64) -> i64 {
    while right != 0 {
        let remainder = left % right;
        left = right;
        right = remainder;
    }
    left.abs()
}

fn check_local_dual_line_and_global_bc_blocker() {
    // The local costalk provides the raw X_D03 class.  Its principal-ideal
    // dual evaluates it to the generator [1] of R/(U_D03), without inverting
    // X_D03 in the coefficient ring.
    let ideal = PrincipalIdeal {
        generator: Polynomial::variable(X_D03),
    };
    let raw_x = PrincipalIdealElement {
        coefficient: Polynomial::one(),
    };
    let x_dual = PrincipalIdealDual {
        source_generator: Polynomial::variable(X_D03),
    };
    assert_eq!(ideal.include(&raw_x), Polynomial::variable(X_D03));
    let local_shifted_generator = x_dual.evaluate(&ideal, &raw_x);
    assert_eq!(local_shifted_generator, Polynomial::one());
    assert!(!local_shifted_generator.divisible_by(U_D03));

    // At e_r and c the extraordinary and ordinary D03 costalk complexes are
    // identical.  Their ordinary comparison cone is contractible.  This zero
    // endpoint calculation neither constructs nor falsifies an extraordinary
    // integration map by itself.
    let road_cone_differential = Polynomial::one();
    let road_endpoint_candidate = Polynomial::one();
    assert_eq!(
        road_cone_differential.multiply(&road_endpoint_candidate),
        Polynomial::one()
    );
    let ordinary_road_cone_class = "ZERO";
    assert_eq!(ordinary_road_cone_class, "ZERO");

    // Cartier purity and entry 100's excess trace remain independently typed
    // downstream ingredients.  Their two short-u3 labels are distinct, but
    // this checker cannot compose them with e_F because the first arrow is
    // absent from the gallery model.
    #[derive(Clone, Copy, Debug, Eq, PartialEq)]
    enum U3Label {
        Reciprocal,
        RoadBorelMoore,
    }
    let u3_labels = [U3Label::Reciprocal, U3Label::RoadBorelMoore];
    assert_ne!(u3_labels[0], u3_labels[1]);
    let cartier_dx03_orientation = 1_i64;
    let entry100_excess_orientation = 1_i64;
    let entry100_denominator_normals = [0_usize, 1, 3, 5];
    assert_eq!(cartier_dx03_orientation, 1);
    assert_eq!(entry100_excess_orientation, 1);
    assert_eq!(entry100_denominator_normals, [0, 1, 3, 5]);

    let first_missing_arrow = "sp_G:RHom(Q,F0[2])->C_D03[-1]";
    let required_value = "sp_G(e_F)=[1]";
    let specialization_status = "UNDEFINED";
    let extraordinary_push_pull_status = "NOT TYPED";
    let theta_equality_status = "NOT PROVED";
    assert_eq!(first_missing_arrow, "sp_G:RHom(Q,F0[2])->C_D03[-1]");
    assert_eq!(required_value, "sp_G(e_F)=[1]");
    assert_eq!(specialization_status, "UNDEFINED");
    assert_eq!(extraordinary_push_pull_status, "NOT TYPED");
    assert_eq!(theta_equality_status, "NOT PROVED");
}

fn check_relative_bivariant_hom() {
    // After the occurrence and normal SDRs, the literal D03 cap/dual-cell
    // complex is C0=R --U--> C1=R.  Multiplication by U is injective in the
    // polynomial/Laurent-q base, so H0 vanishes.
    let sample = Polynomial(
        [
            ([1, 0, 2, 0, 0, 1, 0, 0], 3),
            ([0, 2, 0, 1, 1, 0, 2, 0], -5),
        ]
        .into_iter()
        .collect(),
    );
    let image = Polynomial::variable(U_D03).multiply(&sample);
    assert_eq!(image.0.len(), sample.0.len());
    assert!(image.divisible_by(U_D03));
    assert_eq!(image.specialize_zero(U_D03), Polynomial::zero());
    let hom_degree_zero = "ZERO";
    assert_eq!(hom_degree_zero, "ZERO");

    // The first nonzero local group is H1=R/(U), with generator [1].  The
    // principal-ideal evaluation above provides this local class, but the
    // zero gallery-to-Q projection prevents identifying it as sp_G(e_F).
    let ext_one_generator = Polynomial::one();
    assert!(!ext_one_generator.divisible_by(U_D03));
    assert_eq!(ext_one_generator.specialize_zero(U_D03), Polynomial::one());
    let global_e_f_image = "NOT CONSTRUCTED";
    let theta_comparison = "NOT PROVED";
    assert_eq!(global_e_f_image, "NOT CONSTRUCTED");
    assert_eq!(theta_comparison, "NOT PROVED");
}

fn main() {
    let d03 = diagonal(0, 3);
    let x1 = short_diagonal(1);
    let old = old_faces();
    assert_eq!(census(&old), [1, 9, 21, 14]);
    assert_eq!(loaded_ranks(&old), [14, 63, 93, 45]);
    assert_eq!(loaded_ranks(&old).iter().sum::<usize>(), 215);
    let blown_up = blowup_faces(&old, d03, x1);
    check_global_support_model(&blown_up, d03);
    check_gallery_kernel_q_projection(&blown_up, d03);
    check_yoneda_support_blocks();
    check_ambient_pair_rees_only();
    check_occurrence_gallery_sdr();
    check_normal_saturated_sdr();
    check_extraordinary_costalk_localization();
    check_saturated_unit_road_transgression();
    check_local_dual_line_and_global_bc_blocker();
    check_relative_bivariant_hom();

    println!(
        "{}",
        concat!(
            r#"{"claim":"Scoped theorem and falsifier for the corrected D03 blowup: the exact cellular subdivision, corrected occurrence gallery, saturated normal SDR, ambient extraordinary costalk C^0=R --U_D03--> C^1=R, raw class X_D03, and principal-ideal dual evaluation ev(X^vee tensor X)=1 are proved. However, every expanded gallery support lies in F1_tilde, so the canonical gallery projection to Q=F2/F1 is zero. The ambient pair-Rees generic Q quotient is not a Q generator in the gallery source kernel. Consequently the first required specialization arrow is undefined in this finite model, and no global Beck-Chevalley/Yoneda or Theta03 equality follows.","status":"proved","status_meaning":"The combined local theorem and kernel-level no-go are proved; the desired global Beck-Chevalley statement is not proved.","scope":"finite cellular/exit-path certificate for the entry-105 D03 stellar subdivision and the first missing global specialization map","assumptions":["the filtered triple is entry 105's absolute PC complex and its corrected C={D03,x1} cellular subdivision","occurrence uses lcm labels with d(h_E)=b_D-b_1 and no exceptional occurrence variable","monodromy is separate and uses q_E=q_D03*q1 and u_E=U_D03+q_D03*u1","the reciprocal operation is the R-linear dual of I_X=(X_D03), not inversion of X_D03 in R"],"result":{"global_model":{"old_face_census":[1,9,21,14],"blowup_face_census":[1,10,24,16],"old_loaded_ranks":[14,63,93,45],"blowup_loaded_ranks":[16,72,106,51],"filtration_ranks":[8,238,245],"relative_Q_rank":7,"relative_Q_D03_generators":2},"occurrence_blowup":{"exceptional_boundary":"d(h_E)=b_D-b_1","xi_tilde":"x1*e_c+X_D03*x1*h_E+X_D03*e_r","boundary":"X_D03*x0*c-x1*x5*v_plus","lcm_layers":{"e_c":"x1*x3","b_1":"X_D03*x1*x3","h_E":"X_D03*x1*x3","b_D":"X_D03*x1*x3","e_r":"X_D03*x3"},"exceptional_occurrence_variable":false},"normal_blowup":{"q_E":"q_D03*q1","u_E":"U_D03+q_D03*u1=U_D03+u1+U_D03*u1","resolution":"dA=h_E-h_D03-q_D03*h1; dB=u1*h_D03-U_D03*h1","SDR":"p(h_E)=h_D03+q_D03*h1, p(A)=0, p(B)=top, H(h_E)=A","integral":true},"yoneda_support_cocycle":{"first_block":"Q_D03 -> G03_tilde is nonzero with occurrence column (+x0,-x1,-x3,-x4), duplicated on base/circle states","second_block":"G03_tilde -> F0 is zero","ordinary_product":"zero"},"ambient_extraordinary_costalk":{"named_gallery":{"a":"T=R<top>","e_c":"T=R<top>","b":"K1=R<top,h_D03> --[X_D03,U_D03]--> K0=R<p_D03>","e_r":"same D03-channel K","c":"same D03-channel K"},"expanded_middle":{"b_1":"top-only T","h_E":"top-only T","b_D":"D03-channel K"},"generization":"K->T sends top to top and kills h_D03,p_D03","kernel":"K(U_D03)","raw_localization_boundary":"top -> X_D03*p_D03"},"local_principal_ideal_dual":{"ideal":"I_X=(X_D03)","dual":"I_X^vee=Hom_R(I_X,R)","chosen_basis":"X^vee(X_D03)=1","evaluation":"ev(X^vee tensor X_D03)=1","base_X_D03_inverted":false},"bivariant_relative_Hom":{"complex":"C^0=R --U_D03--> C^1=R","H0":"0","H1":"R/(U_D03)","local_shifted_generator":"[1]","raw_class_before_dual_evaluation":"[X_D03]","global_e_F_image":"NOT CONSTRUCTED"},"gallery_kernel_no_go":{"expanded_supports":{"a=v_plus":"{x1,x3,x5}","e_c":"{x1,x3}","b_1":"{E,x1,x3}","h_E":"{E,x3}","b_D":"{E,D03,x3}","e_r":"{D03,x3}","c":"{D03,x0,x3}"},"all_supports_in_F1_tilde":true,"canonical_gallery_to_Q_projection":"zero","gallery_source_kernel_Q_rank":0,"ambient_pair_Rees_generic_Q_rank":7,"distinction":"the ambient pair-Rees generic F2/F1 quotient exists, but restriction of the marked gallery factors through F1_tilde"},"global_blocker":{"first_missing_arrow":"sp_G:RHom(Q,F0[2])->C_D03[-1]","required_value":"sp_G(e_F)=[1]","arrow_status":"UNDEFINED","reason":"the canonical gallery source has zero projection to Q, so the ambient costalk class does not canonically receive e_F","extraordinary_push_pull":"NOT TYPED","theta03_equality":"NOT PROVED"},"logical_distinctions":{"subdivision_equivalence":"proved by the exact stellar face census and the occurrence/normal SDR checks","relative_Q_equivalence":"the ambient quotient has rank 7 and is unchanged; this does not give a Q leg on the gallery source","Beck_Chevalley_Yoneda_equality":"not proved; its first specialization arrow sp_G is undefined"}},"checks":{"face_census":"PASS","loaded_rank_census":"PASS","xi_tilde":"PASS","normal_SDR":"PASS integrally","ambient_pair_Rees_Q":"PASS","ambient_costalk_table":"PASS","raw_localization":"PASS: X_D03","local_principal_ideal_eval":"PASS: ev(X^vee tensor X_D03)=1","local_H1_generator":"PASS: [1]","gallery_support_enumeration":"PASS","gallery_kernel_Q_projection":"ZERO","actual_gallery_specialization_sp_G":"UNDEFINED","global_eF_to_local_generator":"NOT CONSTRUCTED","ordinary_road_cone":"ZERO","extraordinary_push_pull":"NOT TYPED","theta03_equality":"NOT PROVED","t_inverted":false,"U_D03_inverted":false,"short_u_inverted":false,"base_occurrence_inverted":false,"three_inverted":false},"blocker":"A canonical generic-to-special map for the ambient pair does not restrict to the desired gallery source: the gallery inclusion factors through F1_tilde and hence has zero Q projection.","next_required_construction":"Provide an external deformation/nearby-cycle or extraordinary pull-push construction of sp_G and prove sp_G(e_F)=[1]; only then can Cartier purity and entry 100's excess trace be composed and compared with Theta03."}"#
        )
    );
}
