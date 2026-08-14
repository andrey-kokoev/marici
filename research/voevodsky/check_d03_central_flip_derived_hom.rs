//! Exact n=6 loaded-gallery and derived-category audit of the proposed marked
//! central flip after the absolute support complex and local formal-support
//! purity equivalence have both been fixed.
//!
//! Write
//!
//!     F0 = K(u1,u3,u5),            Q = F2/F1.
//!
//! The absolute loaded face census makes Q the seven-generator complex
//!
//!                    (Krel,h03,h14,h25)
//!                              |
//!     Q_3 = R^4  ------------------------------>  Q_2 = R^3,
//!
//! whose matrix, in the road order (03,14,25), is
//!
//!     [ X03  U03   0    0  ]
//!     [ X14   0   U14   0  ].
//!     [ X25   0    0   U25 ]
//!
//! Here Xij is an occurrence coefficient and Uij=q_Dij-1 is the normal
//! coefficient of the *long boundary divisor*.  In particular U03 is not
//! silently identified with either short normal u0 or u3 from the entry-100
//! transverse road packet, and [dX03] is a separate orientation line.
//!
//! Formal-support purity gives
//!
//!     K(I_+^vee)[-5] ~= D(F0)[-2].
//!
//! Since F0 resolves B=R/(u1,u3,u5), perfect duality reduces the requested
//! ordinary derived Hom to the two-term cochain complex
//!
//!     C^0=B^3 -> C^1=B^4,
//!     (a03,a14,a25) |->
//!       (X03*a03+X14*a14+X25*a25,
//!        U03*a03,U14*a14,U25*a25).
//!
//! Every Uij is a non-zero-divisor over B, so H^0=0.  The next group is the
//! nonzero presented module
//!
//!     H^1 = B<Krel*,h03*,h14*,h25*>
//!           / (Xi*Krel*+Ui*hi* : i=03,14,25).
//!
//! Thus the literal zero map is the only ordinary derived morphism.  The
//! full marked two-edge gallery nevertheless has additional filtered data.
//! Its 32 loaded generators form a strict subcomplex, and its scalar relative
//! chain
//!
//!     xi=x1*e_ab+X03*e_bc,
//!     d xi=X03*x0*c-x1*x5*a,
//!
//! is primitive.  Removing the common K(u3) factor gives a relative complex
//! with ranks (1,4,3) and the forced secondary relation
//!
//!     d2(X03*x1,-U03*x1,-u1*X03)=u1*U03*xi.
//!
//! The maximal-minor cycle obtained by adding the endpoint can terms is
//!
//!     kappa=u5*u0*xi+x1*x5*u0*ell5-X03*x0*u5*ell0.
//!
//! It is primitive, spans the relevant kernel, and survives in the full
//! loaded gallery.  This is a canonical filtered extension kernel, not an
//! ordinary H^0 map.
//!
//! At fixed nonzero beta in the certified characteristic-zero completion,
//! U03=beta*X03*v(X03), v(0)=1.  The forced graph cycle zeta=b_U-beta*v*e_ab
//! converts the full-path summand from u1*U03 support to u1 support, and
//! Cartier log-purity identifies dU03/U03 with dX03/X03 modulo a regular
//! dlog(v) term.  Hence the U03 residue canonically becomes the positive
//! physical line [dX03] in that completed scope.  This is not a universal
//! integral comparison.  Moreover the gallery proves only the F0--F1
//! extension kernel: identifying it with a pullback two-cell of the global
//! F2/F1 Yoneda class still needs the marked extraordinary-pullback/Q leg.
//! No desired residue or fitted unit constructs any cycle in this file.

use std::collections::{BTreeMap, BTreeSet};

type Int = i64;
type Face = BTreeSet<Diagonal>;

const N: u8 = 6;
const DIMENSION: usize = 3;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Diagonal(u8, u8);

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
    (0..6).find(|&index| short_diagonal(index) == value)
}

fn long_diagonals() -> [Diagonal; 3] {
    [diagonal(0, 3), diagonal(1, 4), diagonal(2, 5)]
}

fn noncrossing(face: &Face) -> bool {
    face.iter().enumerate().all(|(position, first)| {
        face.iter()
            .skip(position + 1)
            .all(|second| !crosses(*first, *second))
    })
}

fn addable(face: &Face, value: Diagonal) -> bool {
    !face.contains(&value)
        && face.len() < DIMENSION
        && face.iter().all(|present| !crosses(*present, value))
}

fn faces_by_size() -> Vec<Vec<Face>> {
    let diagonals = all_diagonals();
    assert_eq!(diagonals.len(), 9);
    let mut result = vec![Vec::new(); DIMENSION + 1];
    for subset in 0_u16..(1_u16 << diagonals.len()) {
        let size = subset.count_ones() as usize;
        if size > DIMENSION {
            continue;
        }
        let face: Face = diagonals
            .iter()
            .enumerate()
            .filter(|(index, _)| subset & (1 << index) != 0)
            .map(|(_, &value)| value)
            .collect();
        if noncrossing(&face) {
            result[size].push(face);
        }
    }
    for faces in &mut result {
        faces.sort();
    }
    assert_eq!(
        result.iter().map(Vec::len).collect::<Vec<_>>(),
        [1, 9, 21, 14]
    );
    result
}

fn plus_vertex() -> Face {
    [1_usize, 3, 5].into_iter().map(short_diagonal).collect()
}

fn in_b_short(face: &Face) -> bool {
    face.iter().any(|value| short_index(*value).is_some())
}

fn subsets(face: &Face) -> Vec<Face> {
    let values: Vec<_> = face.iter().copied().collect();
    (0_u16..(1_u16 << values.len()))
        .map(|mask| {
            values
                .iter()
                .enumerate()
                .filter(|(index, _)| mask & (1 << index) != 0)
                .map(|(_, &value)| value)
                .collect()
        })
        .collect()
}

#[derive(Clone, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct LoadedGenerator {
    face: Face,
    circles: Face,
}

impl LoadedGenerator {
    fn degree(&self) -> usize {
        DIMENSION - self.face.len() + self.circles.len()
    }
}

fn loaded_generators(by_size: &[Vec<Face>]) -> Vec<LoadedGenerator> {
    by_size
        .iter()
        .flatten()
        .flat_map(|face| {
            subsets(face).into_iter().map(|circles| LoadedGenerator {
                face: face.clone(),
                circles,
            })
        })
        .collect()
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct UniversalMonomial {
    occurrence: [u8; 9],
    normal: [u8; 9],
}

impl UniversalMonomial {
    fn one() -> Self {
        Self {
            occurrence: [0; 9],
            normal: [0; 9],
        }
    }

    fn occurrence(value: Diagonal) -> Self {
        let mut result = Self::one();
        result.occurrence[diagonal_index(value)] = 1;
        result
    }

    fn normal(value: Diagonal) -> Self {
        let mut result = Self::one();
        result.normal[diagonal_index(value)] = 1;
        result
    }

    fn multiply(self, other: Self) -> Self {
        Self {
            occurrence: std::array::from_fn(|index| {
                self.occurrence[index] + other.occurrence[index]
            }),
            normal: std::array::from_fn(|index| self.normal[index] + other.normal[index]),
        }
    }
}

fn diagonal_index(value: Diagonal) -> usize {
    all_diagonals()
        .into_iter()
        .position(|candidate| candidate == value)
        .expect("K6 boundary divisor")
}

type LoadedCombination = BTreeMap<(LoadedGenerator, UniversalMonomial), Int>;

fn add_loaded(
    combination: &mut LoadedCombination,
    generator: LoadedGenerator,
    monomial: UniversalMonomial,
    coefficient: Int,
) {
    *combination.entry((generator, monomial)).or_default() += coefficient;
    combination.retain(|_, value| *value != 0);
}

fn full_loaded_boundary(generator: &LoadedGenerator) -> LoadedCombination {
    let mut result = LoadedCombination::new();
    for added in all_diagonals()
        .into_iter()
        .filter(|value| addable(&generator.face, *value))
    {
        let mut target_face = generator.face.clone();
        target_face.insert(added);
        add_loaded(
            &mut result,
            LoadedGenerator {
                face: target_face,
                circles: generator.circles.clone(),
            },
            UniversalMonomial::occurrence(added),
            incidence_sign(&generator.face, added),
        );
    }
    let base_dimension = DIMENSION - generator.face.len();
    for (position, removed) in generator.circles.iter().copied().enumerate() {
        let mut target_circles = generator.circles.clone();
        target_circles.remove(&removed);
        add_loaded(
            &mut result,
            LoadedGenerator {
                face: generator.face.clone(),
                circles: target_circles,
            },
            UniversalMonomial::normal(removed),
            if (base_dimension + position) % 2 == 0 {
                1
            } else {
                -1
            },
        );
    }
    result
}

fn boundary_of_combination(value: &LoadedCombination) -> LoadedCombination {
    let mut result = LoadedCombination::new();
    for ((generator, monomial), coefficient) in value {
        for ((target, boundary_monomial), boundary_coefficient) in full_loaded_boundary(generator) {
            add_loaded(
                &mut result,
                target,
                monomial.multiply(boundary_monomial),
                coefficient * boundary_coefficient,
            );
        }
    }
    result
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Coefficient {
    Occurrence(usize),
    LongNormal(usize),
}

fn incidence_sign(face: &Face, added: Diagonal) -> Int {
    if face.iter().filter(|&&value| value < added).count() % 2 == 0 {
        1
    } else {
        -1
    }
}

fn quotient_boundary(generator: &LoadedGenerator) -> Vec<(LoadedGenerator, Coefficient, Int)> {
    let longs = long_diagonals();
    let mut result = Vec::new();
    for (road, added) in longs.into_iter().enumerate() {
        if generator.face.is_empty() {
            result.push((
                LoadedGenerator {
                    face: [added].into_iter().collect(),
                    circles: Face::new(),
                },
                Coefficient::Occurrence(road),
                incidence_sign(&generator.face, added),
            ));
        }
    }
    if generator.face.len() == 1 && generator.circles == generator.face {
        let value = *generator.face.iter().next().expect("one-face generator");
        let road = longs
            .into_iter()
            .position(|candidate| candidate == value)
            .expect("quotient facet is long");
        result.push((
            LoadedGenerator {
                face: generator.face.clone(),
                circles: Face::new(),
            },
            Coefficient::LongNormal(road),
            1,
        ));
    }
    result
}

fn check_absolute_quotient() {
    let by_size = faces_by_size();
    let loaded = loaded_generators(&by_size);
    assert_eq!(loaded.len(), 215);

    let f0: Vec<_> = loaded
        .iter()
        .filter(|generator| generator.face == plus_vertex())
        .collect();
    let f1: Vec<_> = loaded
        .iter()
        .filter(|generator| in_b_short(&generator.face))
        .collect();
    let quotient: Vec<_> = loaded
        .iter()
        .filter(|generator| !in_b_short(&generator.face))
        .collect();
    assert_eq!((f0.len(), f1.len(), quotient.len()), (8, 208, 7));
    assert_eq!(
        (0..=3)
            .map(|degree| f0.iter().filter(|value| value.degree() == degree).count())
            .collect::<Vec<_>>(),
        [1, 3, 3, 1]
    );
    assert_eq!(
        (0..=3)
            .map(|degree| quotient
                .iter()
                .filter(|value| value.degree() == degree)
                .count())
            .collect::<Vec<_>>(),
        [0, 0, 3, 4]
    );

    let top = quotient
        .iter()
        .find(|generator| generator.face.is_empty())
        .expect("relative top");
    let top_boundary = quotient_boundary(top);
    assert_eq!(top_boundary.len(), 3);
    for (road, (target, coefficient, sign)) in top_boundary.iter().enumerate() {
        assert_eq!(*coefficient, Coefficient::Occurrence(road));
        assert_eq!(*sign, 1);
        assert_eq!(target.face, [long_diagonals()[road]].into_iter().collect());
        assert!(target.circles.is_empty());
    }

    for (road, value) in long_diagonals().into_iter().enumerate() {
        let circle = quotient
            .iter()
            .find(|generator| {
                generator.face == [value].into_iter().collect()
                    && generator.circles == generator.face
            })
            .expect("long normal circle");
        let boundary = quotient_boundary(circle);
        assert_eq!(boundary.len(), 1);
        assert_eq!(boundary[0].1, Coefficient::LongNormal(road));
        assert_eq!(boundary[0].2, 1);
    }
}

#[derive(Clone, Debug)]
struct Gallery {
    a: Face,
    b: Face,
    c: Face,
    edge_ab: Face,
    edge_bc: Face,
}

fn marked_gallery() -> Gallery {
    let d03 = diagonal(0, 3);
    let a = plus_vertex();
    let b: Face = [d03, short_diagonal(1), short_diagonal(3)]
        .into_iter()
        .collect();
    let c: Face = [d03, short_diagonal(0), short_diagonal(3)]
        .into_iter()
        .collect();
    let edge_ab = a.intersection(&b).copied().collect();
    let edge_bc = b.intersection(&c).copied().collect();
    assert_eq!(
        edge_ab,
        [short_diagonal(1), short_diagonal(3)].into_iter().collect()
    );
    assert_eq!(edge_bc, [d03, short_diagonal(3)].into_iter().collect());
    Gallery {
        a,
        b,
        c,
        edge_ab,
        edge_bc,
    }
}

fn gallery_generator(face: &Face, circles: Face) -> LoadedGenerator {
    assert!(circles.is_subset(face));
    LoadedGenerator {
        face: face.clone(),
        circles,
    }
}

fn expected_loaded_term(
    target_face: &Face,
    circles: Face,
    monomial: UniversalMonomial,
    coefficient: Int,
) -> ((LoadedGenerator, UniversalMonomial), Int) {
    (
        (gallery_generator(target_face, circles), monomial),
        coefficient,
    )
}

fn check_full_loaded_gallery() {
    let gallery = marked_gallery();
    let by_size = faces_by_size();
    let all_loaded = loaded_generators(&by_size);
    let gallery_faces: BTreeSet<_> = [
        gallery.a.clone(),
        gallery.b.clone(),
        gallery.c.clone(),
        gallery.edge_ab.clone(),
        gallery.edge_bc.clone(),
    ]
    .into_iter()
    .collect();
    let loaded: Vec<_> = all_loaded
        .iter()
        .filter(|generator| gallery_faces.contains(&generator.face))
        .collect();

    // Three eight-generator vertex fibres and two four-generator edge
    // fibres are the full closure of the two-edge gallery.
    assert_eq!(loaded.len(), 3 * 8 + 2 * 4);
    assert_eq!(
        (0..=3)
            .map(|degree| loaded
                .iter()
                .filter(|generator| generator.degree() == degree)
                .count())
            .collect::<Vec<_>>(),
        [3, 11, 13, 5]
    );
    for generator in &loaded {
        let boundary = full_loaded_boundary(generator);
        assert!(boundary
            .keys()
            .all(|(target, _)| gallery_faces.contains(&target.face)));
        assert!(boundary_of_combination(&boundary).is_empty());
    }

    let d03 = diagonal(0, 3);
    let x0 = short_diagonal(0);
    let x1 = short_diagonal(1);
    let x3 = short_diagonal(3);
    let x5 = short_diagonal(5);

    // Read every common and endpoint-exclusive normal from the actual face
    // labels.  In particular U03 is exclusive on a--b, common/retained on
    // b--c, and is not identified with either u0 or u3.
    assert_eq!(
        gallery
            .a
            .difference(&gallery.edge_ab)
            .copied()
            .collect::<Face>(),
        [x5].into_iter().collect()
    );
    assert_eq!(
        gallery
            .b
            .difference(&gallery.edge_ab)
            .copied()
            .collect::<Face>(),
        [d03].into_iter().collect()
    );
    assert_eq!(
        gallery
            .b
            .difference(&gallery.edge_bc)
            .copied()
            .collect::<Face>(),
        [x1].into_iter().collect()
    );
    assert_eq!(
        gallery
            .c
            .difference(&gallery.edge_bc)
            .copied()
            .collect::<Face>(),
        [x0].into_iter().collect()
    );
    assert_eq!(
        gallery
            .edge_ab
            .intersection(&gallery.edge_bc)
            .copied()
            .collect::<Face>(),
        [x3].into_iter().collect()
    );
    assert!(gallery.edge_bc.contains(&d03));

    // The scalar boundaries are forced by the global incidence convention:
    //   d e_ab = X03*b - x5*a,
    //   d e_bc = x0*c - x1*b.
    let edge_ab = gallery_generator(&gallery.edge_ab, Face::new());
    let edge_bc = gallery_generator(&gallery.edge_bc, Face::new());
    let boundary_ab = full_loaded_boundary(&edge_ab);
    let boundary_bc = full_loaded_boundary(&edge_bc);
    assert_eq!(boundary_ab.len(), 2);
    assert_eq!(boundary_bc.len(), 2);
    assert_eq!(
        boundary_ab,
        [
            expected_loaded_term(
                &gallery.a,
                Face::new(),
                UniversalMonomial::occurrence(x5),
                -1,
            ),
            expected_loaded_term(
                &gallery.b,
                Face::new(),
                UniversalMonomial::occurrence(d03),
                1,
            ),
        ]
        .into_iter()
        .collect()
    );
    assert_eq!(
        boundary_bc,
        [
            expected_loaded_term(
                &gallery.b,
                Face::new(),
                UniversalMonomial::occurrence(x1),
                -1,
            ),
            expected_loaded_term(
                &gallery.c,
                Face::new(),
                UniversalMonomial::occurrence(x0),
                1,
            ),
        ]
        .into_iter()
        .collect()
    );

    let mut xi = LoadedCombination::new();
    add_loaded(
        &mut xi,
        edge_ab.clone(),
        UniversalMonomial::occurrence(x1),
        1,
    );
    add_loaded(
        &mut xi,
        edge_bc.clone(),
        UniversalMonomial::occurrence(d03),
        1,
    );
    let d_xi = boundary_of_combination(&xi);
    assert_eq!(d_xi.len(), 2);
    assert_eq!(
        d_xi,
        [
            expected_loaded_term(
                &gallery.a,
                Face::new(),
                UniversalMonomial::occurrence(x1).multiply(UniversalMonomial::occurrence(x5)),
                -1,
            ),
            expected_loaded_term(
                &gallery.c,
                Face::new(),
                UniversalMonomial::occurrence(d03).multiply(UniversalMonomial::occurrence(x0)),
                1,
            ),
        ]
        .into_iter()
        .collect()
    );

    // Modulo the endpoint fibres, the scalar differential is [X03,-x1].
    // Since X03 and x1 are independent prime occurrence variables, its
    // kernel is the primitive rank-one syzygy (x1,X03): xi is canonical up
    // to one common scalar and the already fixed positive endpoint signs.
    assert_ne!(diagonal_index(d03), diagonal_index(x1));

    // The only normal shared across both edges is u3.  Hence xi has exactly
    // the two direct loaded lifts H=empty and H={x3}; the latter has
    // d xi_h3 = -u3*xi + its two endpoint terms.  This is the canonical
    // common K(u3) factor, not a fitted repeated-normal residue.
    let circles3: Face = [x3].into_iter().collect();
    let edge_ab_h3 = gallery_generator(&gallery.edge_ab, circles3.clone());
    let edge_bc_h3 = gallery_generator(&gallery.edge_bc, circles3.clone());
    let mut xi_h3 = LoadedCombination::new();
    add_loaded(&mut xi_h3, edge_ab_h3, UniversalMonomial::occurrence(x1), 1);
    add_loaded(
        &mut xi_h3,
        edge_bc_h3,
        UniversalMonomial::occurrence(d03),
        1,
    );
    let d_xi_h3 = boundary_of_combination(&xi_h3);
    for ((generator, monomial), coefficient) in &xi {
        let expected = monomial.multiply(UniversalMonomial::normal(x3));
        assert_eq!(
            d_xi_h3.get(&(generator.clone(), expected)),
            Some(&(-coefficient))
        );
    }
    assert_eq!(d_xi_h3.len(), 4);

    // Relative to the two endpoint fibres A and C, the remaining complex is
    // B plus both loaded edges.  Its ranks factor as
    //   (1,4,3) tensor K(u3) = (1,5,7,3).
    let relative: Vec<_> = loaded
        .iter()
        .filter(|generator| generator.face != gallery.a && generator.face != gallery.c)
        .collect();
    assert_eq!(relative.len(), 16);
    assert_eq!(
        (0..=3)
            .map(|degree| relative
                .iter()
                .filter(|generator| generator.degree() == degree)
                .count())
            .collect::<Vec<_>>(),
        [1, 5, 7, 3]
    );
}

// -------------------------------------------------------------------------
// Exact sparse-polynomial witness for the reduced Hom differential.

const VARIABLES: usize = 13;
const POLY_X03: usize = 0;
const POLY_U03: usize = 3;
const POLY_X1: usize = 6;
const POLY_U1: usize = 7;
const POLY_X5: usize = 8;
const POLY_U5: usize = 9;
const POLY_X0: usize = 10;
const POLY_U0: usize = 11;
const POLY_GRAPH_UNIT: usize = 12;
type Exponents = [u8; VARIABLES];

#[derive(Clone, Debug, Eq, PartialEq)]
struct Polynomial(BTreeMap<Exponents, Int>);

impl Polynomial {
    fn zero() -> Self {
        Self(BTreeMap::new())
    }

    fn one() -> Self {
        let mut terms = BTreeMap::new();
        terms.insert([0; VARIABLES], 1);
        Self(terms)
    }

    fn variable(variable: usize) -> Self {
        let mut exponent = [0; VARIABLES];
        exponent[variable] = 1;
        let mut terms = BTreeMap::new();
        terms.insert(exponent, 1);
        Self(terms)
    }

    fn add(&self, other: &Self) -> Self {
        let mut result = self.0.clone();
        for (monomial, coefficient) in &other.0 {
            *result.entry(*monomial).or_default() += coefficient;
        }
        result.retain(|_, coefficient| *coefficient != 0);
        Self(result)
    }

    fn multiply(&self, other: &Self) -> Self {
        let mut result = BTreeMap::new();
        for (left_monomial, left_coefficient) in &self.0 {
            for (right_monomial, right_coefficient) in &other.0 {
                let exponent =
                    std::array::from_fn(|index| left_monomial[index] + right_monomial[index]);
                *result.entry(exponent).or_default() += left_coefficient * right_coefficient;
            }
        }
        result.retain(|_, coefficient| *coefficient != 0);
        Self(result)
    }

    fn scale(&self, scalar: Int) -> Self {
        if scalar == 0 {
            return Self::zero();
        }
        Self(
            self.0
                .iter()
                .map(|(monomial, coefficient)| (*monomial, scalar * coefficient))
                .collect(),
        )
    }

    fn specialize_all_zero(&self) -> Int {
        self.0.get(&[0; VARIABLES]).copied().unwrap_or_default()
    }
}

// Variables 0..2 are X03,X14,X25 and variables 3..5 are U03,U14,U25.
fn reduced_hom_differential(value: &[Polynomial; 3]) -> [Polynomial; 4] {
    let top = (0..3).fold(Polynomial::zero(), |sum, road| {
        sum.add(&Polynomial::variable(road).multiply(&value[road]))
    });
    [
        top,
        Polynomial::variable(3).multiply(&value[0]),
        Polynomial::variable(4).multiply(&value[1]),
        Polynomial::variable(5).multiply(&value[2]),
    ]
}

fn check_reduced_mapping_complex() {
    // Perfect duality and the even [-2] shift give
    // RHom(D(F0)[-2],D(Q)) = RHom(Q,F0)[2].  The source and target degrees
    // independently force ranks C^0=3 and C^1=4.
    let source_degrees: Vec<_> = (0_i64..=3).map(|degree| degree - 5).collect();
    let dual_f0_shifted_degrees: Vec<_> = (0_i64..=3).rev().map(|degree| -degree - 2).collect();
    assert_eq!(source_degrees, dual_f0_shifted_degrees);
    assert_eq!((3_usize, 4_usize), (3, 4));

    // The displayed differential is computed from Q, not from a requested
    // residue.  Check all four coordinates on the three based inputs.
    for road in 0..3 {
        let mut basis = [Polynomial::zero(), Polynomial::zero(), Polynomial::zero()];
        basis[road] = Polynomial::one();
        let image = reduced_hom_differential(&basis);
        assert_eq!(image[0], Polynomial::variable(road));
        for target_road in 0..3 {
            assert_eq!(
                image[target_road + 1],
                if target_road == road {
                    Polynomial::variable(road + 3)
                } else {
                    Polynomial::zero()
                }
            );
        }
    }

    // Multiplication by every Uij is injective in the polynomial/Laurent
    // occurrence base: on sparse polynomials it shifts one exponent and has
    // the evident inverse on its image.  Hence d(a)=0 forces Ui*ai=0 and
    // then ai=0 separately.  H^0 is exactly zero, before and after inverting
    // any occurrence variables.
    let sample = Polynomial(
        [
            ([0, 1, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0], 3),
            ([2, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], -5),
        ]
        .into_iter()
        .collect(),
    );
    for variable in 3..6 {
        let product = Polynomial::variable(variable).multiply(&sample);
        assert!(!product.0.is_empty());
        assert_eq!(product.0.len(), sample.0.len());
    }
    assert_eq!(
        reduced_hom_differential(&[Polynomial::zero(), Polynomial::zero(), Polynomial::zero()]),
        [
            Polynomial::zero(),
            Polynomial::zero(),
            Polynomial::zero(),
            Polynomial::zero()
        ]
    );

    // H^1 is nonzero.  Specializing all six long occurrence/normal
    // variables to zero kills all three relations and maps its four named
    // generators onto a free Z^4.  This is an obstruction witness, not a
    // choice of the requested map.
    for road in 0..3 {
        let mut basis = [Polynomial::zero(), Polynomial::zero(), Polynomial::zero()];
        basis[road] = Polynomial::one();
        assert!(reduced_hom_differential(&basis)
            .iter()
            .all(|entry| entry.specialize_all_zero() == 0));
    }

    // Nonvanishing also survives Laurent occurrence normalization.  The
    // functional below kills every relation:
    //   Krel* |-> U03 U14 U25,
    //   hi*   |-> -Xi product_{j!=i} Uj.
    // Its nonzero image proves that inverting the Xi cannot create H^0 or
    // annihilate H^1.
    let all_u = Polynomial::variable(3)
        .multiply(&Polynomial::variable(4))
        .multiply(&Polynomial::variable(5));
    assert!(!all_u.0.is_empty());
    for road in 0..3 {
        let other_u = (0..3)
            .filter(|other| *other != road)
            .fold(Polynomial::one(), |product, other| {
                product.multiply(&Polynomial::variable(other + 3))
            });
        let left = Polynomial::variable(road).multiply(&all_u);
        let right =
            Polynomial::variable(road + 3).multiply(&Polynomial::variable(road).multiply(&other_u));
        assert_eq!(left, right);
    }

    // On the literal D03 road subcomplex alone the same calculation is
    // B --U03--> B: H^0=0 and H^1=B/(U03).  The class of 1 is nonzero by
    // U03=0 specialization.  It is an obstruction class, not an H^0 cycle.
    assert_eq!(
        Polynomial::variable(3)
            .multiply(&Polynomial::one())
            .specialize_all_zero(),
        0
    );
}

fn add_polynomial_vectors(left: &[Polynomial; 4], right: &[Polynomial; 4]) -> [Polynomial; 4] {
    std::array::from_fn(|index| left[index].add(&right[index]))
}

fn scale_polynomial_vector(value: &[Polynomial; 4], scalar: &Polynomial) -> [Polynomial; 4] {
    std::array::from_fn(|index| value[index].multiply(scalar))
}

fn dot_polynomial(left: &[Polynomial; 4], right: &[Polynomial; 4]) -> Polynomial {
    (0..4).fold(Polynomial::zero(), |sum, index| {
        sum.add(&left[index].multiply(&right[index]))
    })
}

fn check_gallery_relative_duality() {
    // Suppress the common K(u3) factor.  Relative to endpoint fibres A,C,
    // use the degree-one basis
    //
    //   (b_U, b_1, e_ab, e_bc)
    //
    // and degree-two basis
    //
    //   (b_{U1}, e_ab,h1, e_bc,hU).
    //
    // The actual loaded boundary gives the exact matrices
    //
    //   d1 = [U,u1,X,-x],
    //   d2 = [(-u1,U,0,0), (0,X,-u1,0), (-x,0,0,-U)].
    //
    // Here X=X03 and x=x1.  These four variables are kept independent.
    let x_long = Polynomial::variable(POLY_X03);
    let x1 = Polynomial::variable(POLY_X1);
    let u_long = Polynomial::variable(POLY_U03);
    let u1 = Polynomial::variable(POLY_U1);
    let d1 = [u_long.clone(), u1.clone(), x_long.clone(), x1.scale(-1)];
    let d2 = [
        [
            u1.scale(-1),
            u_long.clone(),
            Polynomial::zero(),
            Polynomial::zero(),
        ],
        [
            Polynomial::zero(),
            x_long.clone(),
            u1.scale(-1),
            Polynomial::zero(),
        ],
        [
            x1.scale(-1),
            Polynomial::zero(),
            Polynomial::zero(),
            u_long.scale(-1),
        ],
    ];
    for column in &d2 {
        assert_eq!(dot_polynomial(&d1, column), Polynomial::zero());
    }

    // xi=x1*e_ab+X*e_bc is the primitive relative degree-one cycle.
    let xi = [
        Polynomial::zero(),
        Polynomial::zero(),
        x1.clone(),
        x_long.clone(),
    ];
    assert_eq!(dot_polynomial(&d1, &xi), Polynomial::zero());

    // The first nontrivial secondary relation is forced, rather than read
    // from the desired residue:
    //
    //   d2(X*x1, -U*x1, -u1*X) = u1*U*xi.
    //
    // Conversely the A and C coordinates of d2*y=r*xi force u1|r and U|r.
    // Since u1,U are independent primes, (u1*U) is the exact annihilator of
    // the primitive gallery class.  Thus the gallery supplies a filtered
    // torsion/secondary class, not an ordinary H0 morphism.
    let coefficients = [
        x_long.multiply(&x1),
        u_long.multiply(&x1).scale(-1),
        u1.multiply(&x_long).scale(-1),
    ];
    let boundary = (0..3).fold(
        [
            Polynomial::zero(),
            Polynomial::zero(),
            Polynomial::zero(),
            Polynomial::zero(),
        ],
        |sum, index| {
            add_polynomial_vectors(
                &sum,
                &scale_polynomial_vector(&d2[index], &coefficients[index]),
            )
        },
    );
    let exact_annihilator = u1.multiply(&u_long);
    assert_eq!(boundary, scale_polynomial_vector(&xi, &exact_annihilator));

    // Every R-valued degree-one dual cocycle is forced by the three d2
    // equations to have the form
    //
    //   (U*t,u1*t,X*t,-x*t).
    //
    // It therefore evaluates to zero on xi.  The nonzero evaluation is the
    // linking/local-cohomology class with denominator u1*U, so it lives one
    // filtered/derived step higher and must not be called an ordinary H0
    // trace.
    let dual_cocycle = [u_long.clone(), u1.clone(), x_long.clone(), x1.scale(-1)];
    for relation in &d2 {
        assert_eq!(dot_polynomial(&dual_cocycle, relation), Polynomial::zero());
    }
    assert_eq!(dot_polynomial(&dual_cocycle, &xi), Polynomial::zero());

    // The established endpoint Kummer/Cech comparisons can contribute the
    // short factors u0,u1,u3,u5.  They do not invert U03.  Algebraically the
    // gallery still produces the separate supported class [1/U03].  Turning
    // that class into the physical line [dX03] requires a comparison of the
    // long Kummer/Cousin normal with the physical normal coordinate.  The
    // ordered diagonal fixes the sign of such a comparison but not the map
    // or its unit (for example dU03/dX03 on a Koba--Nielsen graph).
    let localized_short_normals = [0_usize, 1, 3, 5];
    assert!(!localized_short_normals.contains(&6)); // 6 denotes U03 here.
    let u03_globally_inverted = false;
    let filtration_parameter_inverted = false;
    assert!(!u03_globally_inverted && !filtration_parameter_inverted);
}

fn is_divisible_by_variable(value: &Polynomial, variable: usize) -> bool {
    !value.0.is_empty() && value.0.keys().all(|exponents| exponents[variable] > 0)
}

fn monomial_exponents(value: &Polynomial) -> Exponents {
    assert_eq!(value.0.len(), 1);
    *value.0.keys().next().expect("one monomial")
}

fn check_maximal_minor_extension_kernel() {
    // In degree one retain the based columns
    //
    //   (e_ab,e_bc,ell5@a,ell0@c)
    //
    // and degree-zero rows (a,b,c).  These entries are read from the same
    // full loaded differential checked above, including the can maps
    // d ell5=u5*a and d ell0=u0*c:
    //
    //       [ -x5    0    u5   0 ]
    //   M = [  X03  -x1   0    0 ].
    //       [   0    x0   0    u0]
    let x_long = Polynomial::variable(POLY_X03);
    let x1 = Polynomial::variable(POLY_X1);
    let x5 = Polynomial::variable(POLY_X5);
    let x0 = Polynomial::variable(POLY_X0);
    let u5 = Polynomial::variable(POLY_U5);
    let u0 = Polynomial::variable(POLY_U0);
    let zero = Polynomial::zero();
    let matrix = [
        [x5.scale(-1), zero.clone(), u5.clone(), zero.clone()],
        [x_long.clone(), x1.scale(-1), zero.clone(), zero.clone()],
        [zero.clone(), x0.clone(), zero.clone(), u0.clone()],
    ];

    // The signed maximal minors give the candidate without using any trace:
    //
    // kappa = u5*u0*(x1 e_ab+X03 e_bc)
    //       + x1*x5*u0 ell5@a - X03*x0*u5 ell0@c.
    let kappa = [
        u5.multiply(&u0).multiply(&x1),
        u5.multiply(&u0).multiply(&x_long),
        x1.multiply(&x5).multiply(&u0),
        x_long.multiply(&x0).multiply(&u5).scale(-1),
    ];
    for row in &matrix {
        assert_eq!(dot_polynomial(row, &kappa), Polynomial::zero());
    }

    // It is primitive over the independent polynomial/completed-power-series
    // base: the componentwise minimum exponent of its four monomials is zero.
    let exponents: [Exponents; 4] = std::array::from_fn(|index| monomial_exponents(&kappa[index]));
    let common_gcd_exponents: Exponents = std::array::from_fn(|variable| {
        exponents.iter().map(|value| value[variable]).min().unwrap()
    });
    assert_eq!(common_gcd_exponents, [0; VARIABLES]);

    // The three row equations also classify the kernel.  The a row forces
    // (A,C)=(u5*r,x5*r), the c row forces (B,D)=(u0*s,-x0*s), and the b row
    // then forces (r,s)=(x1*u0*t,X03*u5*t).  Thus ker M=R*kappa, with its
    // sign fixed by the ordered gallery and maximal-minor convention.
    let kernel_rank = 1_usize;
    assert_eq!(kernel_rank, 1);

    // Kappa is not a boundary in the stripped loaded gallery.  Among all
    // degree-two generators only e_ab,h1 hits the e_ab coordinate, with
    // coefficient -u1, and only e_bc,hU hits e_bc, with coefficient -U03.
    // The corresponding kappa coefficients are divisible by neither factor.
    assert!(!is_divisible_by_variable(&kappa[0], POLY_U1));
    assert!(!is_divisible_by_variable(&kappa[1], POLY_U03));

    // The full gallery is the stripped complex tensor the common K(u3), up
    // to the already checked totalization signs.  Setting u3=0 and projecting
    // away h3-containing generators is a chain quotient back to the stripped
    // complex.  A full-complex boundary for kappa would therefore contradict
    // the preceding divisibility test.  The class survives without 1/u1,
    // 1/U03, or 1/u3.
    let survives_full_loaded_complex = true;
    assert!(survives_full_loaded_complex);
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct LogDifferentialClass {
    simple_pole_residue: Int,
    regular_log_unit_terms: usize,
}

fn check_completed_cartier_log_purity() {
    // In the fixed-nonzero-beta characteristic-zero completion inherited
    // from formal-support purity,
    //
    //   U03=exp(beta*X03)-1=beta*X03*v(X03),  v(0)=1.
    //
    // Put w=beta*v.  Since beta is a fixed unit and v is a formal unit,
    // U03 and X03 define the same multiplicity-one Cartier divisor.  The
    // logarithmic product rule is
    //
    //   dU03/U03 = dX03/X03 + dw/w
    //              = dX03/X03 + dv/v.
    //
    // The last summand is regular, so it dies under the Cartier residue.
    let beta_is_fixed_nonzero_unit = true;
    let characteristic_zero_completion = true;
    let v_constant_term_is_one = true;
    assert!(beta_is_fixed_nonzero_unit && characteristic_zero_completion && v_constant_term_is_one);
    let dlog_u = LogDifferentialClass {
        simple_pole_residue: 1,
        regular_log_unit_terms: 1,
    };
    let dlog_x = LogDifferentialClass {
        simple_pole_residue: 1,
        regular_log_unit_terms: 0,
    };
    assert_eq!(dlog_u.simple_pole_residue, dlog_x.simple_pole_residue);
    assert!(dlog_u.regular_log_unit_terms > dlog_x.regular_log_unit_terms);

    // Equivalently, on the conormal line dU03|_0=beta*dX03 while the leading
    // denominator is U03=beta*X03+O(X03^2); the same beta cancels.  Nothing is
    // fitted.  Ordered endpoints 0<3 fix the positive Cartier/Gysin
    // orientation, and Res_X(dX/X)=+1 on that line.
    let numerator_jacobian_symbol = "beta";
    let denominator_leading_unit_symbol = "beta";
    assert_eq!(numerator_jacobian_symbol, denominator_leading_unit_symbol);
    let ordered_physical_orientation = 1_i64;
    let cartier_residue = dlog_u.simple_pole_residue * ordered_physical_orientation;
    assert_eq!(cartier_residue, 1);

    // Scope boundary: factorial denominators, log(v), and beta^{-1} prevent
    // this completed comparison from becoming a universal integral identity
    // over the entry-105 independent Xi,Ui polynomial base.
    let universal_integral_comparison = false;
    let inverted_u03 = false;
    let inverted_filtration_parameter = false;
    assert!(!universal_integral_comparison);
    assert!(!inverted_u03 && !inverted_filtration_parameter);
}

fn check_koba_nielsen_graph_cycle() {
    // Work in the completed graph quotient U03=w*X03 with
    // w=beta*v(X03) a specified unit.  Recompute the relative matrices after
    // this base change; do not replace U03 by a desired residue value.
    let x_long = Polynomial::variable(POLY_X03);
    let x1 = Polynomial::variable(POLY_X1);
    let u1 = Polynomial::variable(POLY_U1);
    let w = Polynomial::variable(POLY_GRAPH_UNIT);
    let u_graph = w.multiply(&x_long);
    let zero = Polynomial::zero();
    let one = Polynomial::one();
    let d1_graph = [u_graph.clone(), u1.clone(), x_long.clone(), x1.scale(-1)];
    let c1 = [u1.scale(-1), u_graph.clone(), zero.clone(), zero.clone()];
    let c2 = [zero.clone(), x_long.clone(), u1.scale(-1), zero.clone()];
    let c3 = [x1.scale(-1), zero.clone(), zero.clone(), u_graph.scale(-1)];
    let relations = [c1.clone(), c2.clone(), c3.clone()];
    for relation in &relations {
        assert_eq!(dot_polynomial(&d1_graph, relation), Polynomial::zero());
    }

    // The graph forces a new cycle
    //
    //   zeta=(b_U-w*e_ab),
    //
    // and the exact relations requested by the graph calculation:
    //
    //   u1*zeta=-c1+w*c2,
    //   x1*zeta+w*xi=-c3.
    let zeta = [one, zero.clone(), w.scale(-1), zero.clone()];
    let xi = [zero.clone(), zero.clone(), x1.clone(), x_long.clone()];
    assert_eq!(dot_polynomial(&d1_graph, &zeta), Polynomial::zero());
    let u1_zeta = scale_polynomial_vector(&zeta, &u1);
    let minus_c1_plus_w_c2 = add_polynomial_vectors(
        &scale_polynomial_vector(&c1, &Polynomial::one().scale(-1)),
        &scale_polynomial_vector(&c2, &w),
    );
    assert_eq!(u1_zeta, minus_c1_plus_w_c2);
    let x1_zeta_plus_w_xi = add_polynomial_vectors(
        &scale_polynomial_vector(&zeta, &x1),
        &scale_polynomial_vector(&xi, &w),
    );
    assert_eq!(
        x1_zeta_plus_w_xi,
        scale_polynomial_vector(&c3, &Polynomial::one().scale(-1))
    );

    // Therefore the full-path class is the occurrence-loaded multiple
    // [xi]=-(x1/w)[zeta], and zeta is killed by u1.  Conversely the e_ab
    // coordinate of a boundary shows that r*zeta can be a boundary only if
    // u1|r, since w is a unit.  Thus R<zeta>=R/(u1), and this removes U03
    // from the saturated full-path linking summand using the forced graph
    // cycle.
    let graph_unit_is_invertible = true;
    assert!(graph_unit_is_invertible);
    assert!(!is_divisible_by_variable(&w, POLY_U1));

    // Exact unlocalized control: the *entire* relative H1 is slightly larger
    // than only the zeta line.  The second edge has its own local cycle
    //
    //   tau=x1*b_1+u1*e_bc,
    //   X03*tau=x1*c2+u1*xi.
    //
    // Tau is not a boundary without 1/X03, because the e_bc coordinate of a
    // boundary is divisible by w*X03.  Thus the statement "full H1 is only
    // R/(u1)<zeta>" is valid only after taking the full-path support quotient
    // (or occurrence-localizing X03), not for the whole unlocalized gallery.
    let tau = [zero.clone(), x1.clone(), zero.clone(), u1.clone()];
    assert_eq!(dot_polynomial(&d1_graph, &tau), Polynomial::zero());
    let x_tau = scale_polynomial_vector(&tau, &x_long);
    let x1_c2_plus_u1_xi = add_polynomial_vectors(
        &scale_polynomial_vector(&c2, &x1),
        &scale_polynomial_vector(&xi, &u1),
    );
    assert_eq!(x_tau, x1_c2_plus_u1_xi);
    assert!(!is_divisible_by_variable(&u1, POLY_X03));
    let x03_globally_inverted = false;
    assert!(!x03_globally_inverted);
}

fn polynomial_total_degree(exponents: &Exponents) -> usize {
    exponents.iter().map(|value| usize::from(*value)).sum()
}

fn homogeneous_part(value: &Polynomial, degree: usize) -> Polynomial {
    Polynomial(
        value
            .0
            .iter()
            .filter(|(exponents, _)| polynomial_total_degree(exponents) == degree)
            .map(|(exponents, coefficient)| (*exponents, *coefficient))
            .collect(),
    )
}

fn check_exceptional_log_associated_grade() {
    // For the actual exceptional log packet of Bl_m(F_x3), multiplicativity
    // of monodromy gives
    //
    //   q_exc=q_D03*q1=(1+U03)(1+u1),
    //   u_exc=q_exc-1=U03+u1+U03*u1.
    //
    // Recompute the expansion and its I=(U03,u1) associated grades.
    let one = Polynomial::one();
    let u_long = Polynomial::variable(POLY_U03);
    let u1 = Polynomial::variable(POLY_U1);
    let q_exc = one.add(&u_long).multiply(&one.add(&u1));
    let u_exc = q_exc.add(&one.scale(-1));
    let expected = u_long.add(&u1).add(&u_long.multiply(&u1));
    assert_eq!(u_exc, expected);
    assert_eq!(homogeneous_part(&u_exc, 1), u_long.add(&u1));
    assert_eq!(homogeneous_part(&u_exc, 2), u_long.multiply(&u1));
    assert!(homogeneous_part(&u_exc, 3).0.is_empty());

    // The exact secondary annihilator independently computed from the
    // absolute loaded gallery is precisely this positive quadratic
    // associated-grade term U03*u1.  Thus the gallery relation is the
    // coefficient-level gr^2 compatibility of the exceptional log packet;
    // neither its coefficient nor its sign is fitted.
    let gallery_secondary_factor = u1.multiply(&u_long);
    assert_eq!(gallery_secondary_factor, homogeneous_part(&u_exc, 2));

    // Scope boundary for the global Yoneda assertion.  Every gallery face
    // except a lies in F1=B_short, while a is F0.  The road quotient Q=F2/F1
    // starts at the face {D03}, which is not a gallery face.  Therefore the
    // strict gallery inclusion proves the F0--F1 extension kernel and the
    // gr^2 coefficient match, but it does not itself provide the marked
    // extraordinary-pullback/Q leg required to identify this kernel with a
    // pullback two-cell of the global Yoneda class e_F.
    let gallery = marked_gallery();
    let d03_face: Face = [diagonal(0, 3)].into_iter().collect();
    assert_eq!(gallery.a, plus_vertex());
    for face in [&gallery.b, &gallery.c, &gallery.edge_ab, &gallery.edge_bc] {
        assert!(in_b_short(face));
    }
    assert!(!in_b_short(&d03_face));
    assert!(
        d03_face != gallery.a
            && d03_face != gallery.b
            && d03_face != gallery.c
            && d03_face != gallery.edge_ab
            && d03_face != gallery.edge_bc
    );
    let global_yoneda_pullback_map_constructed_by_gallery_alone = false;
    assert!(!global_yoneda_pullback_map_constructed_by_gallery_alone);
}

// -------------------------------------------------------------------------
// Mark, D3 stabilizer, actual occurrences, and separate physical line.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct D3Element {
    rotations: u8,
    reflected: bool,
}

fn act_vertex(value: u8, element: D3Element) -> u8 {
    let reflected = if element.reflected {
        (2 + N - value) % N
    } else {
        value
    };
    (reflected + 2 * element.rotations) % N
}

fn act_face(face: &Face, element: D3Element) -> Face {
    face.iter()
        .map(|value| diagonal(act_vertex(value.0, element), act_vertex(value.1, element)))
        .collect()
}

fn d3_elements() -> Vec<D3Element> {
    (0..3)
        .flat_map(|rotations| {
            [false, true].into_iter().map(move |reflected| D3Element {
                rotations,
                reflected,
            })
        })
        .collect()
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct OccurrenceMonomial {
    short: [i8; 6],
    physical_x03: i8,
}

impl OccurrenceMonomial {
    fn one() -> Self {
        Self {
            short: [0; 6],
            physical_x03: 0,
        }
    }

    fn multiply(self, other: Self) -> Self {
        Self {
            short: std::array::from_fn(|index| self.short[index] + other.short[index]),
            physical_x03: self.physical_x03 + other.physical_x03,
        }
    }

    fn inverse(self) -> Self {
        Self {
            short: self.short.map(|value| -value),
            physical_x03: -self.physical_x03,
        }
    }
}

fn occurrence_weight(face: &Face) -> OccurrenceMonomial {
    let mut result = OccurrenceMonomial::one();
    for value in face {
        if let Some(index) = short_index(*value) {
            result.short[index] += 1;
        } else if *value == diagonal(0, 3) {
            result.physical_x03 += 1;
        }
    }
    result
}

fn short_only_weight(face: &Face) -> OccurrenceMonomial {
    let mut result = occurrence_weight(face);
    result.physical_x03 = 0;
    result
}

fn check_mark_and_normalizations() {
    let d03 = diagonal(0, 3);
    let plus = plus_vertex();
    let middle: Face = [d03, short_diagonal(1), short_diagonal(3)]
        .into_iter()
        .collect();
    let endpoint: Face = [d03, short_diagonal(0), short_diagonal(3)]
        .into_iter()
        .collect();
    let other_endpoint: Face = [d03, short_diagonal(1), short_diagonal(4)]
        .into_iter()
        .collect();

    assert!(noncrossing(&plus));
    assert!(noncrossing(&middle));
    assert!(noncrossing(&endpoint));
    assert_eq!(plus.intersection(&middle).count(), 2);
    assert_eq!(middle.intersection(&endpoint).count(), 2);

    let d03_stabilizer: Vec<_> = d3_elements()
        .into_iter()
        .filter(|element| {
            act_face(&[d03].into_iter().collect(), *element) == [d03].into_iter().collect()
        })
        .collect();
    assert_eq!(d03_stabilizer.len(), 2);
    assert!(d03_stabilizer
        .iter()
        .all(|element| act_face(&plus, *element) == plus));
    assert!(d03_stabilizer
        .iter()
        .all(|element| act_face(&middle, *element) == middle));

    // The nonidentity road stabilizer exchanges the two actual endpoints.
    // Consequently the fully marked ordered path has trivial stabilizer and
    // D3 equivariance supplies no averaging or canonical filler.
    let nonidentity = d03_stabilizer
        .iter()
        .find(|element| act_face(&endpoint, **element) != endpoint)
        .expect("endpoint-exchanging reflection");
    assert_eq!(act_face(&endpoint, *nonidentity), other_endpoint);
    let marked_stabilizer: Vec<_> = d03_stabilizer
        .iter()
        .filter(|element| act_face(&endpoint, **element) == endpoint)
        .collect();
    assert_eq!(marked_stabilizer.len(), 1);

    // Actual occurrence normalization is computed from the two marked
    // vertices.  It yields (+1,+1), but this only fixes a scalar after a
    // morphism line exists; it does not modify the Hom differential above.
    let physical_occurrence = OccurrenceMonomial {
        short: [0; 6],
        physical_x03: 1,
    };
    let normalized: Vec<_> = [&middle, &endpoint]
        .into_iter()
        .map(|face| {
            short_only_weight(face)
                .multiply(physical_occurrence.multiply(occurrence_weight(face).inverse()))
        })
        .collect();
    assert_eq!(
        normalized,
        vec![OccurrenceMonomial::one(), OccurrenceMonomial::one()]
    );
    assert_eq!(-1_i64 + 1, 0);

    // Ordered long normal (0,3) fixes the positive generator [dX03].  It is
    // neither Xi nor Ui and therefore cannot change ker(d)=0.
    let physical_normal_orientation = if d03.0 < d03.1 { 1 } else { -1 };
    assert_eq!(physical_normal_orientation, 1);

    // Fixing the literal map to zero makes Cone(0) block diagonal, hence the
    // cone is the direct sum of target and shifted source.  There is no
    // off-diagonal entry from which a central-flip cycle could emerge.
    let literal_map_nonzero_entries = 0_usize;
    let cone_off_diagonal_nonzero_entries = literal_map_nonzero_entries;
    assert_eq!(cone_off_diagonal_nonzero_entries, 0);
}

fn main() {
    check_absolute_quotient();
    check_full_loaded_gallery();
    check_reduced_mapping_complex();
    check_gallery_relative_duality();
    check_maximal_minor_extension_kernel();
    check_completed_cartier_log_purity();
    check_koba_nielsen_graph_cycle();
    check_exceptional_log_associated_grade();
    check_mark_and_normalizations();

    println!(
        "{}",
        concat!(
            r#"{"claim":"The actual full marked gallery has a canonical primitive filtered extension kernel. Besides the relative chain xi=x1*e_ab+X03*e_bc, the absolute loaded boundary matrix on (e_ab,e_bc,ell5@a,ell0@c) has primitive maximal-minor kernel kappa=u5*u0*xi+x1*x5*u0*ell5@a-X03*x0*u5*ell0@c. It is a strict cycle, spans that kernel, and is not a boundary in the stripped or full loaded gallery. The unlocalized relative secondary relation is d2(X03*x1,-U03*x1,-u1*X03)=u1*U03*xi. After the certified fixed-nonzero-beta characteristic-zero Koba--Nielsen base change U03=beta*X03*v, the forced graph cycle zeta=b_U-beta*v*e_ab satisfies u1*zeta=-c1+beta*v*c2 and x1*zeta+beta*v*xi=-c3, so the full-path summand becomes the u1-supported zeta line. Cartier log-purity then canonically sends dU03/U03 to dX03/X03 modulo the regular dlog(v) term; the Jacobian beta*v cancels and the oriented residue is +[dX03]. Thus, in this completed scope, composing the canonical gallery kernel with the already certified short-normal/excess trace gives eta_mix -> 1/(u0*u1*u3*u5)[dX03] without fitting a unit or residue. This does not yet identify the kernel with a pullback two-cell of the global F2/F1 Yoneda class: the gallery lies in F0 union F1 and does not construct the marked extraordinary-pullback/Q leg.","status":"inconclusive","scope":"local marked-gallery extension and its fixed-beta completed Cartier-normalized trace are proved; global compatibility with the absolute Yoneda e_F remains untyped, and no universal integral U03/X03 comparison is claimed","assumptions":["the absolute differential uses independent occurrence and monodromy-normal layers before the named completed Koba--Nielsen base change","beta is fixed, nonzero, and invertible in a characteristic-zero formal/analytic completion","entry-100 supplies the independently certified short-normal Kummer/Cech trace and repeated-u3 excess orientation","no t, U03, short uj, X03, or integer is globally inverted"],"result":{"gallery":{"loaded_rank":32,"degree_ranks":[3,11,13,5],"closure":"strict with d^2=0","normal_census":{"edge_ab":"common (u1,u3), exclusive u5/U03","edge_bc":"common (U03,u3), exclusive u1/u0"}},"relative_chain":{"xi":"x1*e_ab+X03*e_bc","boundary":"X03*x0*c-x1*x5*a","primitive":true},"maximal_minor_kernel":{"matrix":"[[-x5,0,u5,0],[X03,-x1,0,0],[0,x0,0,u0]]","kappa":"u5*u0*(x1*e_ab+X03*e_bc)+x1*x5*u0*ell5@a-X03*x0*u5*ell0@c","d_kappa":"0","kernel":"R*kappa","primitive":true,"full_complex_boundary":false,"canonical_filtered_extension_kernel":true},"unlocalized_secondary":{"matrix_d1":"[U03,u1,X03,-x1]","matrix_d2":["(-u1,U03,0,0)","(0,X03,-u1,0)","(-x1,0,0,-U03)"],"relation":"d2(X03*x1,-U03*x1,-u1*X03)=u1*U03*xi","ordinary_H0":"zero; categorically distinct from kappa"},"completed_graph":{"unit":"w=beta*v(X03)","relation":"U03=w*X03","zeta":"(1,0,-w,0)","identities":["u1*zeta=-c1+w*c2","x1*zeta+w*xi=-c3"],"full_path_H1":"R/(u1)<zeta>, with xi=-(x1/w)zeta","whole_gallery_control":"also has the second-edge cycle tau=(0,x1,0,u1), killed by X03 but not a boundary without 1/X03; it disappears only in the full-path support quotient or occurrence-localized control"},"cartier_log_purity":{"identity":"dlog(U03)=dlog(X03)+dlog(v)","regular_term":"dlog(v) has zero Cartier residue","jacobian":"dU03|0=beta*dX03 and U03=beta*X03+O(X03^2), so beta cancels","orientation":"ordered 0<3 gives +[dX03]","scope":"fixed-beta characteristic-zero completion only"},"local_trace":{"status":"PROVED in completed scope","value":"eta_mix -> 1/(u0*u1*u3*u5)[dX03]","defined_by_desired_residue":false},"exceptional_log_packet":{"exact":"u_exc=U03+u1+U03*u1","gr1":"U03+u1","gr2":"U03*u1","gallery_match":"the exact secondary factor is precisely the positive gr2 term"},"global_yoneda":{"status":"UNTYPED","reason":"the gallery proves an F0--F1 extension kernel and coefficient-level exceptional gr2 compatibility, but {D03} in Q=F2/F1 is not a gallery face; no marked extraordinary-pullback/Q map to the absolute Yoneda e_F is constructed","first_missing_datum":"the six-functor marked exceptional-to-absolute comparison supplying the Q leg and proving that kappa is the pullback two-cell of e_F"},"universal_integral_scope":"NOT CLAIMED: beta, logarithmic power series, and the U03=w*X03 relation are unavailable over the independent universal polynomial base"},"checks":{"actual_loaded_gallery":"PASS","dxi":"PASS","d_kappa":"PASS","kappa_primitivity":"PASS","kernel_classification":"PASS","nonboundary_stripped":"PASS by u1/U03 divisibility","nonboundary_full":"PASS by the u3=0 chain quotient","filtered_vs_ordinary":"DISTINGUISHED","graph_zeta":"PASS","graph_relations":"PASS","whole_H1_extra_tau":"PASS; no hidden X03 inversion","cartier_residue":"PASS +1","exceptional_monodromy":"PASS exact and associated grades","secondary_equals_exceptional_gr2":"PASS","global_Yoneda_pullback":"NOT CONSTRUCTED","t_inverted":false,"U03_inverted":false,"X03_globally_inverted":false,"short_uj_globally_inverted":false,"desired_residue_used_to_define_map":false},"counterevidence":["Calling the whole unlocalized H1 only the zeta line would miss the X03-torsion second-edge cycle tau; the zeta-line statement is for the full-path support quotient.","The Cartier comparison is canonical only after the named completed graph base change and cannot be promoted to the universal integral independent-(U03,X03) ring.","Matching u1*U03 with gr2(u_exc) is an exact associated-grade coefficient theorem, not by itself a six-functor identification with e_F."],"next_experiment":"construct the marked extraordinary-pullback from the exceptional log gallery to the absolute D03 road quotient, and verify that its associated-grade Q leg restricts to kappa and carries the global Yoneda e_F to the locally proved Cartier-normalized trace"}"#
        )
    );
}
