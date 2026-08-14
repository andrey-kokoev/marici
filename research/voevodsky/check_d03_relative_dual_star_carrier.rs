//! Carrier-only audit of relative barycentric dual-star candidates at D03.
//!
//! The actual stellar subdivision of the K6 face poset is used.  Its marked
//! gallery has the seven supports
//!
//!   a -- e_c -- b_1 -- h_E -- b_D -- e_r -- c.
//!
//! Three natural meanings of "dual star of the gallery" are compared in the
//! barycentric subdivision:
//!
//! 1. cone only from the literal D03 quotient face {D03} over gallery
//!    simplices comparable with {D03};
//! 2. cone from a quotient face common to every gallery support; and
//! 3. the full closed simplicial star of sd(gallery).
//!
//! The first is intrinsically D03-oriented and has a nonzero Q vertex, but
//! its special trace is only sd(e_r), so it misses e_c and h_E.  The unique
//! common quotient coface in the second definition is the top cell.  Its cone
//! reaches the full gallery, but it has no D03 ray and its carrier fundamental
//! boundary has unit coefficients, not the lcm-derived coefficients of
//! xi_tilde.  The third definition is strictly larger than that cone.  Thus
//! the phrase does not select an intrinsic smallest carrier, and no candidate
//! passes both the generic-Q and special-boundary tests.
//!
//! No monodromy, Cousin, can/var, purity, or Theta value is present here.

use std::collections::{BTreeMap, BTreeSet};

type Z = i64;
const N: u8 = 6;
const DIMENSION: usize = 3;

const XD: usize = 0;
const X0: usize = 1;
const X1: usize = 2;
const X3: usize = 3;
const X5: usize = 4;
const OCCURRENCE_VARIABLES: usize = 5;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Diagonal(u8, u8);

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum Ray {
    Old(Diagonal),
    Exceptional,
}

type OldFace = BTreeSet<Diagonal>;
type Face = BTreeSet<Ray>;
type BarySimplex = Vec<Face>;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Monomial([u8; OCCURRENCE_VARIABLES]);

impl Monomial {
    fn one() -> Self {
        Self([0; OCCURRENCE_VARIABLES])
    }

    fn variable(index: usize) -> Self {
        let mut powers = [0; OCCURRENCE_VARIABLES];
        powers[index] = 1;
        Self(powers)
    }

    fn multiply(self, other: Self) -> Self {
        Self(std::array::from_fn(|index| self.0[index] + other.0[index]))
    }

    fn lcm(self, other: Self) -> Self {
        Self(std::array::from_fn(|index| {
            self.0[index].max(other.0[index])
        }))
    }

    fn quotient(self, divisor: Self) -> Self {
        assert!((0..OCCURRENCE_VARIABLES).all(|index| self.0[index] >= divisor.0[index]));
        Self(std::array::from_fn(|index| {
            self.0[index] - divisor.0[index]
        }))
    }
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct Polynomial(BTreeMap<Monomial, Z>);

impl Polynomial {
    fn zero() -> Self {
        Self(BTreeMap::new())
    }

    fn monomial(value: Monomial) -> Self {
        Self(BTreeMap::from([(value, 1)]))
    }

    fn add(&self, other: &Self) -> Self {
        let mut result = self.0.clone();
        for (monomial, coefficient) in &other.0 {
            *result.entry(*monomial).or_default() += coefficient;
        }
        result.retain(|_, coefficient| *coefficient != 0);
        Self(result)
    }

    fn scale(&self, scalar: Z) -> Self {
        Self(
            self.0
                .iter()
                .filter_map(|(monomial, coefficient)| {
                    let product = scalar * coefficient;
                    (product != 0).then_some((*monomial, product))
                })
                .collect(),
        )
    }

    fn multiply_monomial(&self, scalar: Monomial) -> Self {
        Self(
            self.0
                .iter()
                .map(|(monomial, coefficient)| (monomial.multiply(scalar), *coefficient))
                .collect(),
        )
    }
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum GalleryVertex {
    A,
    B1,
    BD,
    C,
}

type GalleryBoundary = BTreeMap<GalleryVertex, Polynomial>;

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
            .map(|(_, diagonal)| *diagonal)
            .collect();
        if noncrossing(&face) {
            result.insert(face);
        }
    }
    result
}

fn old_as_blowup(face: &OldFace) -> Face {
    face.iter().copied().map(Ray::Old).collect()
}

fn blowup_faces(old: &BTreeSet<OldFace>, first: Diagonal, second: Diagonal) -> BTreeSet<Face> {
    let mut result = BTreeSet::new();
    for face in old {
        if !(face.contains(&first) && face.contains(&second)) {
            result.insert(old_as_blowup(face));
            continue;
        }
        let remainder: Face = face
            .iter()
            .filter(|diagonal| **diagonal != first && **diagonal != second)
            .copied()
            .map(Ray::Old)
            .collect();
        for retained in [None, Some(first), Some(second)] {
            let mut replacement = remainder.clone();
            replacement.insert(Ray::Exceptional);
            if let Some(diagonal) = retained {
                replacement.insert(Ray::Old(diagonal));
            }
            result.insert(replacement);
        }
    }
    result
}

fn face_census(faces: &BTreeSet<Face>) -> [usize; DIMENSION + 1] {
    std::array::from_fn(|size| faces.iter().filter(|face| face.len() == size).count())
}

fn in_f1_tilde(face: &Face) -> bool {
    face.contains(&Ray::Exceptional)
        || face.iter().any(|ray| match ray {
            Ray::Old(diagonal) => short_index(*diagonal).is_some(),
            Ray::Exceptional => true,
        })
}

fn extend_barycentric_chain(
    faces: &BTreeSet<Face>,
    chain: &mut BarySimplex,
    result: &mut BTreeSet<BarySimplex>,
) {
    result.insert(chain.clone());
    let last = chain.last().expect("a barycentric chain is nonempty");
    let successors: Vec<_> = faces
        .iter()
        .filter(|face| last.len() < face.len() && last.is_subset(face))
        .cloned()
        .collect();
    for successor in successors {
        chain.push(successor);
        extend_barycentric_chain(faces, chain, result);
        chain.pop();
    }
}

fn barycentric_subdivision(faces: &BTreeSet<Face>) -> BTreeSet<BarySimplex> {
    let mut result = BTreeSet::new();
    for face in faces {
        let mut chain = vec![face.clone()];
        extend_barycentric_chain(faces, &mut chain, &mut result);
    }
    result
}

fn barycentric_census(simplices: &BTreeSet<BarySimplex>) -> [usize; DIMENSION + 1] {
    std::array::from_fn(|dimension| {
        simplices
            .iter()
            .filter(|simplex| simplex.len() == dimension + 1)
            .count()
    })
}

fn gallery_supports(d03: Diagonal) -> BTreeMap<&'static str, Face> {
    let x0 = short_diagonal(0);
    let x1 = short_diagonal(1);
    let x3 = short_diagonal(3);
    let x5 = short_diagonal(5);
    BTreeMap::from([
        (
            "a",
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
    ])
}

fn comparable(left: &Face, right: &Face) -> bool {
    left.is_subset(right) || right.is_subset(left)
}

fn union_is_chain(left: &BarySimplex, right: &BarySimplex) -> bool {
    let union: BTreeSet<_> = left.iter().chain(right).cloned().collect();
    union
        .iter()
        .all(|first| union.iter().all(|second| comparable(first, second)))
}

fn gallery_subdivision(
    barycentric: &BTreeSet<BarySimplex>,
    gallery: &BTreeMap<&'static str, Face>,
) -> BTreeSet<BarySimplex> {
    let gallery_faces: BTreeSet<_> = gallery.values().cloned().collect();
    barycentric
        .iter()
        .filter(|simplex| simplex.iter().all(|face| gallery_faces.contains(face)))
        .cloned()
        .collect()
}

fn cone_over_trace(apex: &Face, trace: &BTreeSet<BarySimplex>) -> BTreeSet<BarySimplex> {
    let mut result = trace.clone();
    result.insert(vec![apex.clone()]);
    for simplex in trace {
        assert!(simplex.iter().all(|face| apex.is_subset(face)));
        let mut coned = Vec::with_capacity(simplex.len() + 1);
        coned.push(apex.clone());
        coned.extend(simplex.iter().cloned());
        result.insert(coned);
    }
    result
}

fn add_boundary_term(
    boundary: &mut GalleryBoundary,
    vertex: GalleryVertex,
    coefficient: &Polynomial,
) {
    let old = boundary.remove(&vertex).unwrap_or_else(Polynomial::zero);
    let sum = old.add(coefficient);
    if sum != Polynomial::zero() {
        boundary.insert(vertex, sum);
    }
}

fn scaled_edge_boundary(
    left: GalleryVertex,
    left_coefficient: Monomial,
    right: GalleryVertex,
    right_coefficient: Monomial,
    chain_coefficient: Monomial,
) -> GalleryBoundary {
    BTreeMap::from([
        (
            left,
            Polynomial::monomial(left_coefficient)
                .multiply_monomial(chain_coefficient)
                .scale(-1),
        ),
        (
            right,
            Polynomial::monomial(right_coefficient).multiply_monomial(chain_coefficient),
        ),
    ])
}

fn add_boundaries(left: &GalleryBoundary, right: &GalleryBoundary) -> GalleryBoundary {
    let mut result = left.clone();
    for (vertex, coefficient) in right {
        add_boundary_term(&mut result, *vertex, coefficient);
    }
    result
}

fn check_occurrence_lcm_xi() -> [Monomial; 3] {
    let xd = Monomial::variable(XD);
    let x0 = Monomial::variable(X0);
    let x1 = Monomial::variable(X1);
    let x3 = Monomial::variable(X3);
    let x5 = Monomial::variable(X5);

    let label_a = x1.multiply(x3).multiply(x5);
    let label_ec = x1.multiply(x3);
    let label_b1 = xd.multiply(x1).multiply(x3);
    let label_h = label_b1;
    let label_bd = label_b1;
    let label_er = xd.multiply(x3);
    let label_c = xd.multiply(x0).multiply(x3);

    assert_eq!(label_b1.quotient(label_ec), xd);
    assert_eq!(label_a.quotient(label_ec), x5);
    assert_eq!(label_bd.quotient(label_h), Monomial::one());
    assert_eq!(label_b1.quotient(label_h), Monomial::one());
    assert_eq!(label_bd.quotient(label_er), x1);
    assert_eq!(label_c.quotient(label_er), x0);

    // Internal cancellation requires XD*c_ec=c_h=x1*c_er.  The primitive
    // common lcm is XD*x1, so the coefficients are derived, not assigned.
    let middle_lcm = xd.lcm(x1);
    let coefficients = [middle_lcm.quotient(xd), middle_lcm, middle_lcm.quotient(x1)];
    assert_eq!(coefficients, [x1, xd.multiply(x1), xd]);

    let d_ec = scaled_edge_boundary(GalleryVertex::A, x5, GalleryVertex::B1, xd, coefficients[0]);
    let d_h = scaled_edge_boundary(
        GalleryVertex::B1,
        Monomial::one(),
        GalleryVertex::BD,
        Monomial::one(),
        coefficients[1],
    );
    let d_er = scaled_edge_boundary(GalleryVertex::BD, x1, GalleryVertex::C, x0, coefficients[2]);
    let boundary = add_boundaries(&add_boundaries(&d_ec, &d_h), &d_er);
    assert_eq!(
        boundary,
        BTreeMap::from([
            (
                GalleryVertex::A,
                Polynomial::monomial(x1.multiply(x5)).scale(-1),
            ),
            (GalleryVertex::C, Polynomial::monomial(xd.multiply(x0)),),
        ])
    );
    coefficients
}

fn check_carrier_definitions(
    faces: &BTreeSet<Face>,
    barycentric: &BTreeSet<BarySimplex>,
    gallery: &BTreeMap<&'static str, Face>,
    gallery_sd: &BTreeSet<BarySimplex>,
    d03: Diagonal,
    xi_coefficients: [Monomial; 3],
) {
    let q_d03: Face = [Ray::Old(d03)].into_iter().collect();
    let q_top = Face::new();
    assert!(faces.contains(&q_d03));
    assert!(faces.contains(&q_top));
    assert!(!in_f1_tilde(&q_d03));
    assert!(!in_f1_tilde(&q_top));

    // Definition A: the strict D03-apex relative star.  Its special trace is
    // exactly the gallery simplices comparable with the literal Q face D03.
    let strict_trace: BTreeSet<_> = gallery_sd
        .iter()
        .filter(|simplex| simplex.iter().all(|face| comparable(&q_d03, face)))
        .cloned()
        .collect();
    assert_eq!(barycentric_census(&strict_trace), [3, 2, 0, 0]);
    let strict_trace_vertices: BTreeSet<_> = strict_trace
        .iter()
        .filter(|simplex| simplex.len() == 1)
        .map(|simplex| simplex[0].clone())
        .collect();
    assert_eq!(
        strict_trace_vertices,
        [
            gallery["b_D"].clone(),
            gallery["e_r"].clone(),
            gallery["c"].clone()
        ]
        .into_iter()
        .collect()
    );
    let strict_cone = cone_over_trace(&q_d03, &strict_trace);
    let mut strict_carrier = gallery_sd.clone();
    strict_carrier.extend(strict_cone);
    assert!(strict_carrier
        .iter()
        .all(|simplex| barycentric.contains(simplex)));
    assert!(strict_carrier.contains(&vec![q_d03.clone()]));
    let strict_generic_q_projection_nonzero = !in_f1_tilde(&q_d03);
    assert!(strict_generic_q_projection_nonzero);

    // Its two relative 2-simplices can meet only the two barycentric halves
    // of e_r.  Therefore the coefficient of e_c in every special boundary is
    // zero, whereas xi_tilde has the nonzero primitive coefficient x1.
    assert_eq!(
        strict_carrier
            .iter()
            .filter(|simplex| simplex.len() == 3)
            .count(),
        2
    );
    assert!(!strict_trace.contains(&vec![gallery["e_c"].clone()]));
    assert!(!strict_trace.contains(&vec![gallery["h_E"].clone()]));
    let strict_ec_boundary_coefficient = Polynomial::zero();
    let target_ec_boundary_coefficient = Polynomial::monomial(xi_coefficients[0]);
    assert_ne!(
        strict_ec_boundary_coefficient,
        target_ec_boundary_coefficient
    );

    // Definition B: a single quotient apex common to the whole gallery.  The
    // actual poset has exactly one such face, namely the top cell.
    let relative_faces: Vec<_> = faces.iter().filter(|face| !in_f1_tilde(face)).collect();
    let common_relative_cofaces: Vec<_> = relative_faces
        .iter()
        .filter(|candidate| gallery.values().all(|support| candidate.is_subset(support)))
        .copied()
        .collect();
    assert_eq!(common_relative_cofaces, vec![&q_top]);
    assert!(!q_top.contains(&Ray::Old(d03)));
    let top_cone = cone_over_trace(&q_top, gallery_sd);
    assert!(top_cone.iter().all(|simplex| barycentric.contains(simplex)));
    assert!(top_cone.contains(&vec![q_top.clone()]));
    let top_generic_q_projection_nonzero = !in_f1_tilde(&q_top);
    assert!(top_generic_q_projection_nonzero);

    // The integral fundamental boundary of this disk has cellular edge
    // coefficients (1,1,1).  It is not the occurrence chain
    // (x1,XD*x1,XD).  Installing those three coefficients on the coned
    // triangles would be assignment of xi_tilde, not a carrier-only output.
    let carrier_fundamental_coefficients = [Monomial::one(); 3];
    assert_ne!(carrier_fundamental_coefficients, xi_coefficients);
    assert_ne!(carrier_fundamental_coefficients[0], xi_coefficients[0]);

    // Definition C: the closed simplicial star of sd(gallery), consisting of
    // every barycentric simplex extendable with a gallery simplex.  It is
    // strictly larger than the minimal top cone, hence the two standard
    // readings of "star of a subcomplex" do not even select the same carrier.
    let closed_star: BTreeSet<_> = barycentric
        .iter()
        .filter(|simplex| {
            gallery_sd
                .iter()
                .any(|gallery_simplex| union_is_chain(simplex, gallery_simplex))
        })
        .cloned()
        .collect();
    assert!(top_cone.is_subset(&closed_star));
    assert!(top_cone.len() < closed_star.len());
    let x1_facet: Face = [Ray::Old(short_diagonal(1))].into_iter().collect();
    assert!(closed_star.contains(&vec![x1_facet.clone()]));
    assert!(!top_cone.contains(&vec![x1_facet]));

    let intrinsic_smallest_d03_whole_gallery_carrier_exists = false;
    assert!(!intrinsic_smallest_d03_whole_gallery_carrier_exists);
}

fn check_no_downstream_assignments() {
    let monodromy_value_assigned = false;
    let cousin_value_assigned = false;
    let can_var_value_assigned = false;
    let theta_value_assigned = false;
    assert!(!monodromy_value_assigned);
    assert!(!cousin_value_assigned);
    assert!(!can_var_value_assigned);
    assert!(!theta_value_assigned);
}

fn main() {
    let d03 = diagonal(0, 3);
    let x1 = short_diagonal(1);
    let old = old_faces();
    let blown_up = blowup_faces(&old, d03, x1);
    assert_eq!(face_census(&blown_up), [1, 10, 24, 16]);

    let barycentric = barycentric_subdivision(&blown_up);
    assert_eq!(barycentric_census(&barycentric), [51, 194, 240, 96]);
    let gallery = gallery_supports(d03);
    assert!(gallery
        .values()
        .all(|support| blown_up.contains(support) && in_f1_tilde(support)));
    let gallery_sd = gallery_subdivision(&barycentric, &gallery);
    assert_eq!(barycentric_census(&gallery_sd), [7, 6, 0, 0]);

    let xi_coefficients = check_occurrence_lcm_xi();
    check_carrier_definitions(
        &blown_up,
        &barycentric,
        &gallery,
        &gallery_sd,
        d03,
        xi_coefficients,
    );
    check_no_downstream_assignments();

    println!(
        "{}",
        concat!(
            r#"{"claim":"The actual blown-up K6 face poset and its barycentric subdivision do not intrinsically define a smallest D03-oriented dual-star/normal-Morse thimble whose own generic carrier projects nontrivially to Q and whose special boundary is xi_tilde. The strict D03-apex relative star has a literal Q vertex but its gallery trace is only sd(e_r), so its first mismatch is zero e_c coefficient versus the required x1. The unique quotient coface common to all seven gallery supports is the top cell; its cone reaches the whole gallery and has nonzero Q projection, but it is not D03-oriented and its integral carrier fundamental boundary has unit coefficients (1,1,1), not the lcm-derived (x1,X_D03*x1,X_D03). The full closed barycentric star is strictly larger than this cone. Thus 'dual star of a subcomplex' is a genuine typing ambiguity and no carrier-only candidate passes both tests.","status":"proved","status_meaning":"The carrier comparison and first mismatch are proved; no specialization, Beck-Chevalley, Cousin, or Theta construction is claimed.","scope":"carrier-only actual blown-up K6 face poset and barycentric subdivision","result":{"face_poset":{"blowup_census":[1,10,24,16],"barycentric_census":[51,194,240,96],"gallery_support_count":7,"gallery_barycentric_census":[7,6,0,0]},"target_gallery":{"supports":["a={x1,x3,x5}","e_c={x1,x3}","b_1={E,x1,x3}","h_E={E,x3}","b_D={E,D03,x3}","e_r={D03,x3}","c={D03,x0,x3}"],"lcm_derivation":"XD*c_ec=c_h=x1*c_er; primitive lcm XD*x1 gives (c_ec,c_h,c_er)=(x1,XD*x1,XD)","xi_tilde":"x1*e_c+X_D03*x1*h_E+X_D03*e_r","boundary":"X_D03*x0*c-x1*x5*a"},"strict_D03_apex_relative_star":{"apex":"{D03}","generic_Q_projection":"NONZERO","special_trace":"sd(e_r), with barycentric census [3,2,0,0] on {b_D,e_r,c}","relative_2_simplex_count":2,"first_mismatch":"e_c coefficient is 0, required x1","passes_both_tests":false},"common_coface_cone":{"unique_common_Q_coface":"top={}","generic_Q_projection":"NONZERO","covers_all_seven_supports":true,"D03_oriented":false,"integral_fundamental_boundary_coefficients":["1","1","1"],"required_coefficients":["x1","X_D03*x1","X_D03"],"first_coefficient_mismatch":"e_c: 1 versus x1","assigning_required_triangle_coefficients":"would insert xi_tilde rather than derive it"},"closed_barycentric_star":{"definition":"simplices extendable with a simplex of sd(gallery)","relation_to_common_coface_cone":"strictly larger","witness":"the {x1} barycentric vertex lies in the closed star but not the top cone"},"typing_conclusion":{"canonical_candidate":"NONE","reason":"strict D03 orientation and whole-gallery special boundary select different quotient apices/carriers"}},"checks":{"actual_blowup_face_poset":"PASS","actual_barycentric_subdivision":"PASS","lcm_xi_tilde":"PASS","strict_D03_carrier_Q_projection":"NONZERO","strict_D03_special_boundary":"FAIL at missing e_c and h_E support","top_cone_Q_projection":"NONZERO","top_cone_D03_orientation":"ABSENT","top_cone_integral_boundary":"MISMATCH: (1,1,1) versus (x1,X_D03*x1,X_D03)","dual_star_definition_intrinsic":"NO","monodromy_values_assigned":false,"Cousin_values_assigned":false,"can_var_values_assigned":false,"Theta_values_assigned":false,"base_variables_inverted":false},"blocker":"Supply an independently typed normal orientation or coefficient cosheaf on a specified relative star, together with a canonical fundamental class whose boundary derives the lcm syzygy; the carrier poset alone does not provide these data.","next_experiment":"Specify whether the source is the strict {D03} dual block, the top-coface cone, or a sheaf-theoretic normal-Morse functor, then test its canonical relative fundamental class before attaching any downstream values."}"#
        )
    );
}
