//! Endpoint-relative D03 Morse-sector triads in the blown-up K6 face poset.
//!
//! A sector over a gallery edge is the two-triangle barycentric cone from a
//! relative-Q coface of that edge.  Three sectors are glued in gallery order;
//! when adjacent apices differ, the unique barycentric transition triangle at
//! their common gallery vertex is inserted.  The generic side is retained
//! relative to the gallery endpoints a and c.
//!
//! Exact enumeration gives only two minimal apex triples:
//!
//!   (top,top,top),  (top,top,D03).
//!
//! Both have a rank-one generic-side class before inclusion into the ambient
//! pair and all three special gallery edges.  For the mixed triple, however,
//! the oriented sum T of its seven triangles satisfies
//!
//!   dT=G-J,
//!
//! where G is the subdivided gallery and J is the endpoint-relative generic
//! side.  Since G lies in F1_tilde, J=-dT in the ambient relative complex.
//! Thus the purported ambient derived Q class is zero.  The presence and sign
//! of [top<D03] is only a stipulated marked-edge predicate here; no ordered
//! normal comparison is available to promote it to geometric coorientation.
//!
//! Conditional on the asserted occurrence junction matrix, its equations are
//!
//!   XD*c_ec=c_h,  c_h=x1*c_er.
//!
//! Their primitive lcm solution is uniquely
//!
//!   (c_ec,c_h,c_er)=(x1,XD*x1,XD).
//!
//! The lcm solution is checked algebraically, but the matrix has not been
//! derived as the actual P_abs pullback and its weighted d^2 is not certified.
//! Uniqueness holds only inside the cone-per-edge ansatz.  This is a secondary
//! cobordism/no-go theorem, not a Yoneda specialization or downstream result.

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
type IntegralChain = BTreeMap<BarySimplex, Z>;

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
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum GalleryEdge {
    Ec,
    HExceptional,
    Er,
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum ApexKind {
    Top,
    D03,
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum BoundaryComponent {
    SpecialEc,
    SpecialH,
    SpecialEr,
    EndpointA,
    EndpointC,
    RadialTopB1,
    RadialTopBD,
    RadialD03BD,
    GenericTopD03,
}

type SectorBoundary = BTreeMap<BoundaryComponent, Polynomial>;

#[derive(Clone, Debug, Eq, PartialEq)]
struct Triad {
    apices: [ApexKind; 3],
    carrier: BTreeSet<BarySimplex>,
    generic_side: Vec<(Face, Face, Z)>,
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

fn edge_data<'a>(
    edge: GalleryEdge,
    gallery: &'a BTreeMap<&'static str, Face>,
) -> (&'a Face, &'a Face, &'a Face) {
    match edge {
        GalleryEdge::Ec => (&gallery["e_c"], &gallery["a"], &gallery["b_1"]),
        GalleryEdge::HExceptional => (&gallery["h_E"], &gallery["b_1"], &gallery["b_D"]),
        GalleryEdge::Er => (&gallery["e_r"], &gallery["b_D"], &gallery["c"]),
    }
}

fn q_cofaces(edge: &Face, faces: &BTreeSet<Face>) -> Vec<Face> {
    faces
        .iter()
        .filter(|candidate| candidate.is_subset(edge) && !in_f1_tilde(candidate))
        .cloned()
        .collect()
}

fn insert_with_faces(carrier: &mut BTreeSet<BarySimplex>, simplex: &BarySimplex) {
    for mask in 1_usize..(1_usize << simplex.len()) {
        carrier.insert(
            simplex
                .iter()
                .enumerate()
                .filter(|(index, _)| mask & (1 << index) != 0)
                .map(|(_, face)| face.clone())
                .collect(),
        );
    }
}

fn apex_face(kind: ApexKind, d03: Diagonal) -> Face {
    match kind {
        ApexKind::Top => Face::new(),
        ApexKind::D03 => [Ray::Old(d03)].into_iter().collect(),
    }
}

fn classify_apex(face: &Face, d03: Diagonal) -> ApexKind {
    if face.is_empty() {
        ApexKind::Top
    } else {
        assert_eq!(*face, apex_face(ApexKind::D03, d03));
        ApexKind::D03
    }
}

fn oriented_side_boundary(side: &[(Face, Face, Z)]) -> BTreeMap<Face, Z> {
    let mut boundary = BTreeMap::new();
    for (lower, upper, sign) in side {
        assert!(lower.is_subset(upper));
        *boundary.entry(lower.clone()).or_default() -= sign;
        *boundary.entry(upper.clone()).or_default() += sign;
    }
    boundary.retain(|_, coefficient| *coefficient != 0);
    boundary
}

fn add_integral_term(chain: &mut IntegralChain, simplex: BarySimplex, coefficient: Z) {
    *chain.entry(simplex.clone()).or_default() += coefficient;
    if chain[&simplex] == 0 {
        chain.remove(&simplex);
    }
}

fn integral_boundary(chain: &IntegralChain) -> IntegralChain {
    let mut boundary = IntegralChain::new();
    for (simplex, coefficient) in chain {
        assert!(simplex.len() >= 2);
        for removed in 0..simplex.len() {
            let mut face = simplex.clone();
            face.remove(removed);
            let sign = if removed % 2 == 0 { 1 } else { -1 };
            add_integral_term(&mut boundary, face, sign * coefficient);
        }
    }
    boundary
}

fn add_integral_chains(
    left: &IntegralChain,
    right: &IntegralChain,
    right_sign: Z,
) -> IntegralChain {
    let mut result = left.clone();
    for (simplex, coefficient) in right {
        add_integral_term(&mut result, simplex.clone(), right_sign * coefficient);
    }
    result
}

fn special_gallery_chain(gallery: &BTreeMap<&'static str, Face>) -> IntegralChain {
    let mut chain = IntegralChain::new();
    for edge in [GalleryEdge::Ec, GalleryEdge::HExceptional, GalleryEdge::Er] {
        let (edge_face, left, right) = edge_data(edge, gallery);
        add_integral_term(&mut chain, vec![edge_face.clone(), right.clone()], 1);
        add_integral_term(&mut chain, vec![edge_face.clone(), left.clone()], -1);
    }
    chain
}

fn generic_side_chain(triad: &Triad) -> IntegralChain {
    triad
        .generic_side
        .iter()
        .map(|(lower, upper, sign)| (vec![lower.clone(), upper.clone()], *sign))
        .collect()
}

fn sector_two_chain(
    apices: [ApexKind; 3],
    gallery: &BTreeMap<&'static str, Face>,
    d03: Diagonal,
    include_transitions: bool,
) -> IntegralChain {
    let mut chain = IntegralChain::new();
    for (position, edge) in [GalleryEdge::Ec, GalleryEdge::HExceptional, GalleryEdge::Er]
        .into_iter()
        .enumerate()
    {
        let (edge_face, left, right) = edge_data(edge, gallery);
        let apex = apex_face(apices[position], d03);
        add_integral_term(
            &mut chain,
            vec![apex.clone(), edge_face.clone(), right.clone()],
            1,
        );
        add_integral_term(&mut chain, vec![apex, edge_face.clone(), left.clone()], -1);
    }
    if include_transitions {
        let junctions = [&gallery["b_1"], &gallery["b_D"]];
        for position in 0..2 {
            if apices[position] == apices[position + 1] {
                continue;
            }
            let left_apex = apex_face(apices[position], d03);
            let right_apex = apex_face(apices[position + 1], d03);
            // Negative orientation is the unique coefficient that cancels
            // both radial edges of the adjacent sectors.
            add_integral_term(
                &mut chain,
                vec![left_apex, right_apex, junctions[position].clone()],
                -1,
            );
        }
    }
    chain
}

fn modulo_f1(chain: &IntegralChain) -> IntegralChain {
    chain
        .iter()
        .filter(|(simplex, _)| !simplex.iter().all(in_f1_tilde))
        .map(|(simplex, coefficient)| (simplex.clone(), *coefficient))
        .collect()
}

fn check_secondary_cobordism(triad: &Triad, gallery: &BTreeMap<&'static str, Face>, d03: Diagonal) {
    let special = special_gallery_chain(gallery);
    let generic = generic_side_chain(triad);
    let sectors_without_transition = sector_two_chain(triad.apices, gallery, d03, false);
    let incomplete_boundary = integral_boundary(&sectors_without_transition);

    if triad.apices[1] != triad.apices[2] {
        let top_bd = vec![apex_face(ApexKind::Top, d03), gallery["b_D"].clone()];
        let d03_bd = vec![apex_face(ApexKind::D03, d03), gallery["b_D"].clone()];
        assert_eq!(incomplete_boundary[&top_bd], -1);
        assert_eq!(incomplete_boundary[&d03_bd], 1);
        let transition = vec![
            apex_face(ApexKind::Top, d03),
            apex_face(ApexKind::D03, d03),
            gallery["b_D"].clone(),
        ];
        let transition_boundary = integral_boundary(&BTreeMap::from([(transition, 1)]));
        // If k is the transition coefficient, both cancellation equations
        // are -1-k=0 and 1+k=0, hence uniquely k=-1.
        assert_eq!(transition_boundary[&top_bd], -1);
        assert_eq!(transition_boundary[&d03_bd], 1);
        let forced_transition_coefficient = -1_i64;
        assert_eq!(forced_transition_coefficient, -1);
    }

    let thimble = sector_two_chain(triad.apices, gallery, d03, true);
    let expected_triangle_count = if triad.apices[1] == triad.apices[2] {
        6
    } else {
        7
    };
    assert_eq!(thimble.len(), expected_triangle_count);
    let expected_boundary = add_integral_chains(&special, &generic, -1);
    assert_eq!(integral_boundary(&thimble), expected_boundary);
    assert_eq!(
        integral_boundary(&integral_boundary(&thimble)),
        IntegralChain::new()
    );

    // Every special simplex lies in F1_tilde, whereas every generic-side edge
    // survives the relative quotient.  Hence dT=-J mod F1 and J is ambiently
    // exact, despite generating H1 of the isolated endpoint-relative side.
    assert_eq!(modulo_f1(&special), IntegralChain::new());
    assert_eq!(modulo_f1(&generic), generic);
    assert_eq!(
        modulo_f1(&integral_boundary(&thimble)),
        add_integral_chains(&IntegralChain::new(), &generic, -1)
    );
}

fn build_triad(
    apices: [ApexKind; 3],
    gallery: &BTreeMap<&'static str, Face>,
    barycentric: &BTreeSet<BarySimplex>,
    d03: Diagonal,
) -> Triad {
    let edges = [GalleryEdge::Ec, GalleryEdge::HExceptional, GalleryEdge::Er];
    let mut carrier = BTreeSet::new();
    for (position, edge) in edges.into_iter().enumerate() {
        let (edge_face, left, right) = edge_data(edge, gallery);
        let apex = apex_face(apices[position], d03);
        assert!(apex.is_subset(edge_face));
        for endpoint in [left, right] {
            let simplex = vec![apex.clone(), edge_face.clone(), endpoint.clone()];
            assert!(barycentric.contains(&simplex));
            insert_with_faces(&mut carrier, &simplex);
        }
    }

    let junctions = [gallery["b_1"].clone(), gallery["b_D"].clone()];
    for position in 0..2 {
        if apices[position] == apices[position + 1] {
            continue;
        }
        let left_apex = apex_face(apices[position], d03);
        let right_apex = apex_face(apices[position + 1], d03);
        assert!(left_apex.is_subset(&right_apex));
        assert!(right_apex.is_subset(&junctions[position]));
        let transition = vec![left_apex, right_apex, junctions[position].clone()];
        assert!(barycentric.contains(&transition));
        insert_with_faces(&mut carrier, &transition);
    }

    // The generic side is the oriented path from a to c through the distinct
    // quotient apices.  Canonical barycentric orientation orders each edge by
    // face inclusion, so a->top is represented with sign -1.
    let a = gallery["a"].clone();
    let c = gallery["c"].clone();
    let mut apex_path = vec![apex_face(apices[0], d03)];
    for kind in apices.iter().skip(1) {
        let face = apex_face(*kind, d03);
        if apex_path.last() != Some(&face) {
            apex_path.push(face);
        }
    }
    let mut generic_side = Vec::new();
    generic_side.push((apex_path[0].clone(), a.clone(), -1));
    for pair in apex_path.windows(2) {
        assert!(pair[0].is_subset(&pair[1]));
        generic_side.push((pair[0].clone(), pair[1].clone(), 1));
    }
    generic_side.push((
        apex_path.last().expect("an apex path exists").clone(),
        c.clone(),
        1,
    ));
    assert!(generic_side
        .iter()
        .all(|(lower, upper, _)| barycentric.contains(&vec![lower.clone(), upper.clone()])));
    let side_boundary = oriented_side_boundary(&generic_side);
    assert_eq!(side_boundary, BTreeMap::from([(a, -1), (c, 1)]));

    Triad {
        apices,
        carrier,
        generic_side,
    }
}

fn add_sector_term(
    boundary: &mut SectorBoundary,
    component: BoundaryComponent,
    coefficient: Monomial,
    sign: Z,
) {
    let old = boundary.remove(&component).unwrap_or_else(Polynomial::zero);
    let sum = old.add(&Polynomial::monomial(coefficient).scale(sign));
    if sum != Polynomial::zero() {
        boundary.insert(component, sum);
    }
}

fn conditional_lcm_coefficients() -> [Monomial; 4] {
    let xd = Monomial::variable(XD);
    let x0 = Monomial::variable(X0);
    let x1 = Monomial::variable(X1);
    let x3 = Monomial::variable(X3);
    let x5 = Monomial::variable(X5);
    let label_ec = x1.multiply(x3);
    let label_a = label_ec.multiply(x5);
    let label_b1 = xd.multiply(label_ec);
    let label_h = label_b1;
    let label_bd = label_b1;
    let label_er = xd.multiply(x3);
    let label_c = label_er.multiply(x0);
    assert_eq!(label_a.quotient(label_ec), x5);
    assert_eq!(label_b1.quotient(label_ec), xd);
    assert_eq!(label_b1.quotient(label_h), Monomial::one());
    assert_eq!(label_bd.quotient(label_h), Monomial::one());
    assert_eq!(label_bd.quotient(label_er), x1);
    assert_eq!(label_c.quotient(label_er), x0);
    let junction_lcm = xd.lcm(x1);
    let coefficients = [
        junction_lcm.quotient(xd),
        junction_lcm,
        junction_lcm.quotient(x1),
        junction_lcm,
    ];
    assert_eq!(coefficients, [x1, xd.multiply(x1), xd, xd.multiply(x1)]);

    // Among monomials with exponents at most two, XD*x1 is the unique
    // coordinatewise-minimal common multiple.  This finite lcm check encodes
    // the primitive occurrence solution rather than inserting its entries.
    let common_multiples: Vec<_> = (0_u8..=2)
        .flat_map(|xd_power| {
            (0_u8..=2).map(move |x1_power| {
                let mut powers = [0; OCCURRENCE_VARIABLES];
                powers[XD] = xd_power;
                powers[X1] = x1_power;
                Monomial(powers)
            })
        })
        .filter(|candidate| candidate.0[XD] >= 1 && candidate.0[X1] >= 1)
        .collect();
    let minima: Vec<_> = common_multiples
        .iter()
        .filter(|candidate| {
            common_multiples.iter().all(|other| {
                !(other != *candidate
                    && (0..OCCURRENCE_VARIABLES).all(|index| other.0[index] <= candidate.0[index]))
            })
        })
        .copied()
        .collect();
    assert_eq!(minima, vec![junction_lcm]);
    coefficients
}

fn conditional_occurrence_sector_boundary(
    apices: [ApexKind; 3],
    coefficients: [Monomial; 4],
) -> SectorBoundary {
    let xd = Monomial::variable(XD);
    let x0 = Monomial::variable(X0);
    let x1 = Monomial::variable(X1);
    let x3 = Monomial::variable(X3);
    let x5 = Monomial::variable(X5);
    let [c_ec, c_h, c_er, transition] = coefficients;
    let mut boundary = SectorBoundary::new();

    add_sector_term(&mut boundary, BoundaryComponent::SpecialEc, c_ec, 1);
    add_sector_term(
        &mut boundary,
        BoundaryComponent::EndpointA,
        x5.multiply(c_ec),
        1,
    );
    add_sector_term(
        &mut boundary,
        BoundaryComponent::RadialTopB1,
        xd.multiply(c_ec),
        -1,
    );

    add_sector_term(&mut boundary, BoundaryComponent::SpecialH, c_h, 1);
    add_sector_term(&mut boundary, BoundaryComponent::RadialTopB1, c_h, 1);
    add_sector_term(&mut boundary, BoundaryComponent::RadialTopBD, c_h, -1);

    add_sector_term(&mut boundary, BoundaryComponent::SpecialEr, c_er, 1);
    let er_left_component = match apices[2] {
        ApexKind::Top => BoundaryComponent::RadialTopBD,
        ApexKind::D03 => BoundaryComponent::RadialD03BD,
    };
    add_sector_term(&mut boundary, er_left_component, x1.multiply(c_er), 1);
    add_sector_term(
        &mut boundary,
        BoundaryComponent::EndpointC,
        x0.multiply(c_er),
        -1,
    );

    if apices[1] != apices[2] {
        // The negatively oriented transition triangle has boundary
        // top-b_D - D03-b_D - (top-D03).  The two b_D radial incidences have
        // the transition label and hence unit coefficients.  The generic
        // edge has label XD, so its lcm quotient is x1*x3.
        add_sector_term(&mut boundary, BoundaryComponent::RadialTopBD, transition, 1);
        add_sector_term(
            &mut boundary,
            BoundaryComponent::RadialD03BD,
            transition,
            -1,
        );
        add_sector_term(
            &mut boundary,
            BoundaryComponent::GenericTopD03,
            transition.multiply(x1).multiply(x3),
            -1,
        );
    }
    boundary
}

fn check_conditional_occurrence_boundary(apices: [ApexKind; 3], coefficients: [Monomial; 4]) {
    let xd = Monomial::variable(XD);
    let x0 = Monomial::variable(X0);
    let x1 = Monomial::variable(X1);
    let x3 = Monomial::variable(X3);
    let x5 = Monomial::variable(X5);
    let boundary = conditional_occurrence_sector_boundary(apices, coefficients);

    assert_eq!(
        boundary[&BoundaryComponent::SpecialEc],
        Polynomial::monomial(x1)
    );
    assert_eq!(
        boundary[&BoundaryComponent::SpecialH],
        Polynomial::monomial(xd.multiply(x1))
    );
    assert_eq!(
        boundary[&BoundaryComponent::SpecialEr],
        Polynomial::monomial(xd)
    );
    assert_eq!(
        boundary[&BoundaryComponent::EndpointA],
        Polynomial::monomial(x1.multiply(x5))
    );
    assert_eq!(
        boundary[&BoundaryComponent::EndpointC],
        Polynomial::monomial(xd.multiply(x0)).scale(-1)
    );
    assert!(!boundary.contains_key(&BoundaryComponent::RadialTopB1));
    assert!(!boundary.contains_key(&BoundaryComponent::RadialTopBD));
    assert!(!boundary.contains_key(&BoundaryComponent::RadialD03BD));
    if apices[2] == ApexKind::D03 {
        assert_eq!(
            boundary[&BoundaryComponent::GenericTopD03],
            Polynomial::monomial(xd.multiply(x1).multiply(x1).multiply(x3)).scale(-1)
        );
    } else {
        assert!(!boundary.contains_key(&BoundaryComponent::GenericTopD03));
    }
}

fn relative_side_h1_rank(triad: &Triad, gallery: &BTreeMap<&'static str, Face>) -> usize {
    // The generic side is an interval.  Relative to {a,c}, C1 has one basis
    // element per edge and C0 one per interior vertex; its incidence matrix
    // has full row rank, hence H1 has rank edges-(vertices-2)=1.
    let vertices: BTreeSet<_> = triad
        .generic_side
        .iter()
        .flat_map(|(left, right, _)| [left.clone(), right.clone()])
        .collect();
    let endpoint_set = BTreeSet::from([gallery["a"].clone(), gallery["c"].clone()]);
    assert!(endpoint_set.is_subset(&vertices));
    assert!(endpoint_set.iter().all(in_f1_tilde));
    assert!(triad
        .generic_side
        .iter()
        .all(|(left, right, _)| { !in_f1_tilde(left) || !in_f1_tilde(right) }));
    let relative_vertices = vertices.len() - endpoint_set.len();
    assert_eq!(triad.generic_side.len(), relative_vertices + 1);
    1
}

fn main() {
    let d03 = diagonal(0, 3);
    let center_x1 = short_diagonal(1);
    let old = old_faces();
    let blown_up = blowup_faces(&old, d03, center_x1);
    assert_eq!(face_census(&blown_up), [1, 10, 24, 16]);
    let barycentric = barycentric_subdivision(&blown_up);
    assert_eq!(barycentric_census(&barycentric), [51, 194, 240, 96]);
    let gallery = gallery_supports(d03);
    assert!(gallery
        .values()
        .all(|support| blown_up.contains(support) && in_f1_tilde(support)));

    let relative_cofaces: BTreeMap<_, _> =
        [GalleryEdge::Ec, GalleryEdge::HExceptional, GalleryEdge::Er]
            .into_iter()
            .map(|edge| {
                let (support, _, _) = edge_data(edge, &gallery);
                (edge, q_cofaces(support, &blown_up))
            })
            .collect();
    let top = Face::new();
    let q_d03 = apex_face(ApexKind::D03, d03);
    assert_eq!(relative_cofaces[&GalleryEdge::Ec], vec![top.clone()]);
    assert_eq!(
        relative_cofaces[&GalleryEdge::HExceptional],
        vec![top.clone()]
    );
    assert_eq!(
        relative_cofaces[&GalleryEdge::Er],
        vec![top.clone(), q_d03.clone()]
    );

    let mut apex_triples = Vec::new();
    for ec_apex in &relative_cofaces[&GalleryEdge::Ec] {
        for h_apex in &relative_cofaces[&GalleryEdge::HExceptional] {
            for er_apex in &relative_cofaces[&GalleryEdge::Er] {
                apex_triples.push([
                    classify_apex(ec_apex, d03),
                    classify_apex(h_apex, d03),
                    classify_apex(er_apex, d03),
                ]);
            }
        }
    }
    assert_eq!(
        apex_triples,
        vec![
            [ApexKind::Top, ApexKind::Top, ApexKind::Top],
            [ApexKind::Top, ApexKind::Top, ApexKind::D03],
        ]
    );
    let triads: Vec<_> = apex_triples
        .into_iter()
        .map(|apices| build_triad(apices, &gallery, &barycentric, d03))
        .collect();
    assert_eq!(triads.len(), 2);
    assert_eq!(
        triads[0]
            .carrier
            .iter()
            .filter(|simplex| simplex.len() == 3)
            .count(),
        6
    );
    assert_eq!(
        triads[1]
            .carrier
            .iter()
            .filter(|simplex| simplex.len() == 3)
            .count(),
        7
    );
    assert_eq!(relative_side_h1_rank(&triads[0], &gallery), 1);
    assert_eq!(relative_side_h1_rank(&triads[1], &gallery), 1);
    check_secondary_cobordism(&triads[0], &gallery, d03);
    check_secondary_cobordism(&triads[1], &gallery, d03);
    for triad in &triads {
        for edge in [GalleryEdge::Ec, GalleryEdge::HExceptional, GalleryEdge::Er] {
            let (edge_face, left, right) = edge_data(edge, &gallery);
            assert!(triad
                .carrier
                .contains(&vec![edge_face.clone(), left.clone()]));
            assert!(triad
                .carrier
                .contains(&vec![edge_face.clone(), right.clone()]));
        }
        for simplex in &triad.carrier {
            for removed in 0..simplex.len() {
                if simplex.len() == 1 {
                    continue;
                }
                let mut face = simplex.clone();
                face.remove(removed);
                assert!(triad.carrier.contains(&face));
            }
        }
    }
    assert_eq!(triads[0].apices, [ApexKind::Top; 3]);
    assert_eq!(
        triads[1].apices,
        [ApexKind::Top, ApexKind::Top, ApexKind::D03]
    );

    // This is only a marked-edge predicate.  The face poset has no ordered
    // normal line with which to compare its sign.
    let marked_d03_edge = vec![top.clone(), q_d03.clone()];
    assert!(!triads[0].carrier.contains(&marked_d03_edge));
    assert!(triads[1].carrier.contains(&marked_d03_edge));
    let d03_marked: Vec<_> = triads
        .iter()
        .filter(|triad| triad.carrier.contains(&marked_d03_edge))
        .collect();
    assert_eq!(d03_marked.len(), 1);
    let ordered_normal_comparison_performed = false;
    assert!(!ordered_normal_comparison_performed);

    // This is a conditional algebra test of the displayed junction matrix.
    // The checker does not derive that matrix from P_abs or verify its full
    // weighted differential squares to zero.
    let coefficients = conditional_lcm_coefficients();
    check_conditional_occurrence_boundary(triads[0].apices, coefficients);
    check_conditional_occurrence_boundary(triads[1].apices, coefficients);
    let actual_p_abs_pullback_verified = false;
    let weighted_d_squared_verified = false;
    assert!(!actual_p_abs_pullback_verified);
    assert!(!weighted_d_squared_verified);

    let monodromy_value_assigned = false;
    let cousin_value_assigned = false;
    let theta_value_assigned = false;
    assert!(!monodromy_value_assigned);
    assert!(!cousin_value_assigned);
    assert!(!theta_value_assigned);

    println!(
        "{}",
        concat!(
            r#"{"claim":"Within the explicitly defined cone-per-gallery-edge ansatz, the actual blown-up K6 barycentric poset has exactly two minimal apex triples, (top,top,top) and (top,top,D03). For the mixed triple, the six sector triangles leave two radial residuals at b_D; imposing radial cancellation and a cobordism from the special gallery G to the generic side J uniquely forces coefficient -1 on the transition triangle [top<D03<b_D]. The resulting oriented seven-triangle chain T satisfies dT=G-J and d^2T=0 integrally. Since G is contained in F1_tilde, J=-dT modulo F1_tilde, so its ambient relative-Q class is zero. The edge [top<D03] is only a stipulated D03 mark, not a certified geometric coorientation. Conditional on the displayed junction matrix, its primitive lcm kernel is (x1,XD*x1,XD,XD*x1); the checker does not derive that matrix from P_abs or certify its weighted d^2.","status":"proved","status_meaning":"The scoped integral secondary-cobordism theorem and its ambient-Q no-go are proved; sp_G and the desired derived Q-leg remain unconstructed.","scope":"cone-per-edge endpoint-relative ansatz in the actual blown-up K6 barycentric carrier, with a conditional occurrence-junction calculation","result":{"ambient":{"blowup_face_census":[1,10,24,16],"barycentric_census":[51,194,240,96]},"ansatz":{"definition":"choose one relative-Q coface apex for each of e_c,h_E,e_r; use its two barycentric cone triangles; if adjacent apices differ, optionally add the unique comparable transition triangle at their junction","edge_Q_cofaces":{"e_c":["top"],"h_E":["top"],"e_r":["top","D03"]},"enumeration_complete_inside_ansatz":true,"global_minimality_outside_ansatz":"NOT CLAIMED"},"minimal_sector_triads":[{"apices":["top","top","top"],"sector_triangle_count":6,"generic_side":"a-top-c","isolated_endpoint_relative_H1_rank":1,"ambient_relative_Q_class":"ZERO: the side is the boundary of its six-triangle cone modulo F1_tilde","D03_marked_edge_present":false},{"apices":["top","top","D03"],"sector_triangle_count":6,"transition_triangle_count":1,"total_triangle_count":7,"generic_side":"J=a-top-D03-c","isolated_endpoint_relative_H1_rank":1,"ambient_relative_Q_class":"ZERO","D03_marked_edge_present":true,"geometric_D03_coorientation":"NOT CERTIFIED"}],"integral_secondary_cobordism":{"special_chain":"G=sd(xi_unweighted), the six oriented barycentric gallery edges","generic_chain":"J=-[top,a]+[top,D03]+[D03,c]","thimble":"T is the oriented sum of six sector triangles minus [top,D03,b_D]","chain_identity":"dT=G-J","relative_identity":"dT=-J mod F1_tilde","d_squared":"d^2T=0","ambient_Q_conclusion":"[J]=0"},"transition":{"status":"FORCED ONLY UNDER RADIAL-CANCELLATION/COBORDISM CONDITION","residual_without_transition":"-[top,b_D]+[D03,b_D]","transition_boundary":"[D03,b_D]-[top,b_D]+[top,D03]","forced_integral_coefficient":-1,"universal_transition_forcing":"NOT CLAIMED"},"marked_edge_typing":{"predicate":"the carrier contains the canonically ordered barycentric edge [top<D03]","predicate_uniqueness_inside_ansatz":"(top,top,D03) is the sole marked triple","ordered_normal_comparison":"NOT PERFORMED","D03_coorientation_claim":"STIPULATED MARK ONLY"},"conditional_occurrence_kernel":{"status":"CONDITIONAL","asserted_junction_matrix":"[[-XD,1,0,0],[0,-1,0,1],[0,0,x1,-1]] on (c_ec,c_h,c_er,t)","primitive_lcm":"lcm(XD,x1)=XD*x1","primitive_kernel_generator":["x1","XD*x1","XD","XD*x1"],"conditional_special_chain":"xi_tilde=x1*e_c+XD*x1*h_E+XD*e_r","actual_P_abs_pullback":"NOT VERIFIED","weighted_d_squared":"NOT VERIFIED","assigned_from_target":false},"uniqueness":{"carrier_uniqueness":"ONLY INSIDE THE CONE-PER-EDGE ANSATZ","marked_support_torsor_inside_ansatz":"singleton","geometric_orientation_torsor":"NOT COMPUTED"},"requirements_audit":{"genuine_nonzero_ambient_derived_Q_class":"FAIL: J is exact modulo F1_tilde","endpoint_relative_boundary_across_three_gallery_edges":"PASS at the integral carrier level","D03_coorientation":"NOT CERTIFIED; marked-edge predicate only","lcm_coefficient_cosheaf":"CONDITIONAL on the asserted junction matrix and pending P_abs/d^2"}},"checks":{"actual_blowup_poset":"PASS","actual_barycentric_subdivision":"PASS","cone_per_edge_enumeration":"PASS: exactly two","oriented_seven_triangle_chain":"PASS","radial_transition_coefficient":"PASS: -1 under the named cobordism condition","integral_chain_identity":"PASS: dT=G-J","carrier_d_squared":"PASS: d^2T=0","ambient_relative_reduction":"PASS: dT=-J mod F1_tilde","ambient_derived_Q_class":"ZERO","ordered_normal_comparison":"NOT PERFORMED","actual_P_abs_occurrence_pullback":"NOT VERIFIED","weighted_occurrence_d_squared":"NOT VERIFIED","global_sp_G":"NOT CONSTRUCTED","monodromy_values_assigned":false,"Cousin_values_assigned":false,"can_var_values_assigned":false,"Theta_values_assigned":false,"base_variables_inverted":false},"blocker":"A successful source must not merely add an endpoint-relative side interval whose ambient image bounds the same sector thimble. It must construct a separately typed derived/nearby-cycle Q-leg and derive the occurrence junction matrix from the actual P_abs pullback with weighted d^2=0.","next_experiment":"Compute the actual P_abs restriction to the mixed seven-triangle carrier and its derived quotient map; reject it unless a Q class survives after the explicit null-cobordism is taken into account."}"#
        )
    );
}
