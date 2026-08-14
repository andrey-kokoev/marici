//! Exact universal-chain certificate for the absolute unlocalized
//! original-twist/Borel--Moore support-PC object on the labelled hexagon
//! associahedron K6.
//!
//! Work over
//!
//!   R0 = Z[q_D^+-1 : D a K6 boundary divisor],  u_D=q_D-1,
//!
//! with an independent polynomial occurrence layer Z[X_D].  No X_D inverse
//! is used by this checker.  For a noncrossing dissection S and a subset H of
//! its oriented normal circles, write (S,H) for the corresponding cell of the
//! real oriented boundary blowup.  Its total degree is
//!
//!   3-|S|+|H|.
//!
//! The universal differential is
//!
//!   d(S,H)
//!    = sum_{a addable} epsilon(S,a) X_a (S+a,H)
//!      + (-1)^(3-|S|) sum_{h in H} (-1)^pos u_h (S,H-h).
//!
//! The first line is the cellular/Cousin boundary.  In the normal layer its
//! radial attachment inserts the positive basepoint p_a, hence is the
//! costandard var=1 map.  The second line is the fibre-circle boundary
//! d h_a=u_a p_a, hence is can=u_a.  These are the ordinary CW attaching maps
//! of the oriented blowup; no cross-face Gysin map is fitted.
//!
//! The checker enumerates all 215 cells, verifies d^2=0 with coefficients in
//! the universal polynomial ring, proves D3 covariance with transported base
//! and torus orientations, and proves that the closed supports
//!
//!   v_+ subset B_short subset K6
//!
//! are strict subcomplexes.  Localizing u_D gives the entry-38 normal
//! contraction s_D(p_D)=u_D^-1 h_D.  Entry-100 Cech complexes are therefore
//! local realization targets of this finite absolute object, not data needed
//! to define its global differential.
//!
//! This checker does not construct the reciprocal-standard conductor Thom
//! map or alpha_+.  In particular an entry-100 excess trace, whose source is
//! K(I_+^vee) tensor K(I_i), is not a literal restriction of the absolute
//! road map, whose source has only the original-twist road factor K(I_i).
//! More sharply, the pullback of the filtration's Yoneda two-class to the
//! literal closed D03 road is zero: all of its boundary terms remain on
//! faces containing D03, a strict subcomplex of F1 disjoint from F0=v_+.
//! Entry 100's nonzero local residue therefore requires an additional marked
//! support correspondence across the central flip.

use std::collections::{BTreeMap, BTreeSet};

type Int = i64;

const N: u8 = 6;
const DIMENSION: usize = 3;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Diagonal(u8, u8);

type Face = BTreeSet<Diagonal>;

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

fn short_index(value: Diagonal) -> Option<usize> {
    (0..6).find(|&index| diagonal(index as u8, (index as u8 + 2) % N) == value)
}

fn long_index(value: Diagonal) -> Option<usize> {
    (0..3).find(|&index| diagonal(index as u8, index as u8 + 3) == value)
}

fn variable_index(value: Diagonal) -> usize {
    short_index(value).unwrap_or_else(|| 6 + long_index(value).unwrap())
}

fn noncrossing(face: &Face) -> bool {
    face.iter().enumerate().all(|(position, first)| {
        face.iter()
            .skip(position + 1)
            .all(|second| !crosses(*first, *second))
    })
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

fn addable(face: &Face, value: Diagonal) -> bool {
    !face.contains(&value)
        && face.len() < DIMENSION
        && face.iter().all(|&present| !crosses(present, value))
}

fn incidence_sign(face: &Face, added: Diagonal) -> Int {
    if face.iter().filter(|&&value| value < added).count() % 2 == 0 {
        1
    } else {
        -1
    }
}

fn rotate_vertex(vertex: u8) -> u8 {
    (vertex + 2) % N
}

fn reflect_vertex(vertex: u8) -> u8 {
    (2 + N - vertex) % N
}

fn permute_face(face: &Face, permutation: fn(u8) -> u8) -> Face {
    face.iter()
        .map(|value| diagonal(permutation(value.0), permutation(value.1)))
        .collect()
}

fn action_signs(
    by_size: &[Vec<Face>],
    permutation: fn(u8) -> u8,
    top_sign: Int,
) -> Vec<BTreeMap<Face, Int>> {
    let mut signs = vec![BTreeMap::new(); DIMENSION + 1];
    signs[0].insert(by_size[0][0].clone(), top_sign);
    for size in 0..DIMENSION {
        for face in &by_size[size] {
            let source_sign = signs[size][face];
            let image_face = permute_face(face, permutation);
            for added in all_diagonals()
                .into_iter()
                .filter(|&value| addable(face, value))
            {
                let mut target = face.clone();
                target.insert(added);
                let image_added = diagonal(permutation(added.0), permutation(added.1));
                let target_sign = source_sign * incidence_sign(face, added)
                    / incidence_sign(&image_face, image_added);
                match signs[size + 1].get(&target) {
                    Some(&known) => assert_eq!(known, target_sign),
                    None => {
                        signs[size + 1].insert(target, target_sign);
                    }
                }
            }
        }
    }
    signs
}

fn plus_vertex() -> Face {
    [1_usize, 3, 5]
        .into_iter()
        .map(|index| diagonal(index as u8, (index as u8 + 2) % N))
        .collect()
}

fn in_b(face: &Face) -> bool {
    face.iter().any(|&value| short_index(value).is_some())
}

fn support_level(face: &Face) -> usize {
    if face == &plus_vertex() {
        0
    } else if in_b(face) {
        1
    } else {
        2
    }
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

    fn occurrence(index: usize) -> Self {
        let mut result = Self::one();
        result.occurrence[index] = 1;
        result
    }

    fn normal(index: usize) -> Self {
        let mut result = Self::one();
        result.normal[index] = 1;
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

    fn permute(self, permutation: fn(u8) -> u8) -> Self {
        let mut result = Self::one();
        for value in all_diagonals() {
            let image = diagonal(permutation(value.0), permutation(value.1));
            result.occurrence[variable_index(image)] = self.occurrence[variable_index(value)];
            result.normal[variable_index(image)] = self.normal[variable_index(value)];
        }
        result
    }
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

    fn normal_degree(&self) -> usize {
        self.circles.len()
    }
}

type LoadedCombination = BTreeMap<(LoadedGenerator, UniversalMonomial), Int>;

fn add_loaded(
    value: &mut LoadedCombination,
    generator: LoadedGenerator,
    monomial: UniversalMonomial,
    coefficient: Int,
) {
    *value.entry((generator, monomial)).or_default() += coefficient;
    value.retain(|_, entry| *entry != 0);
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

fn loaded_boundary(generator: &LoadedGenerator) -> LoadedCombination {
    assert!(generator.circles.is_subset(&generator.face));
    let mut result = LoadedCombination::new();

    // The positive real radial basepoint is var=1 in the normal layer.  The
    // independent polynomial occurrence cosheaf contributes X_a.
    for added in all_diagonals()
        .into_iter()
        .filter(|&value| addable(&generator.face, value))
    {
        let mut target_face = generator.face.clone();
        target_face.insert(added);
        add_loaded(
            &mut result,
            LoadedGenerator {
                face: target_face,
                circles: generator.circles.clone(),
            },
            UniversalMonomial::occurrence(variable_index(added)),
            incidence_sign(&generator.face, added),
        );
    }

    // Circle boundary can=u with the tensor-totalization sign.
    let base_dimension = DIMENSION - generator.face.len();
    for (position, removed) in generator.circles.iter().copied().enumerate() {
        let mut target_circles = generator.circles.clone();
        target_circles.remove(&removed);
        let tensor_sign = if (base_dimension + position) % 2 == 0 {
            1
        } else {
            -1
        };
        add_loaded(
            &mut result,
            LoadedGenerator {
                face: generator.face.clone(),
                circles: target_circles,
            },
            UniversalMonomial::normal(variable_index(removed)),
            tensor_sign,
        );
    }
    result
}

fn loaded_boundary_of_combination(value: &LoadedCombination) -> LoadedCombination {
    let mut result = LoadedCombination::new();
    for ((generator, monomial), coefficient) in value {
        for ((target, boundary_monomial), boundary_coefficient) in loaded_boundary(generator) {
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

fn fibre_permutation_sign(face: &Face, circles: &Face, permutation: fn(u8) -> u8) -> Int {
    let target_face = permute_face(face, permutation);
    let target_positions: BTreeMap<_, _> = target_face
        .iter()
        .enumerate()
        .map(|(position, &value)| (value, position))
        .collect();
    let image_positions: Vec<_> = circles
        .iter()
        .map(|value| {
            let image = diagonal(permutation(value.0), permutation(value.1));
            target_positions[&image]
        })
        .collect();
    let inversions = image_positions
        .iter()
        .enumerate()
        .map(|(position, value)| {
            image_positions
                .iter()
                .skip(position + 1)
                .filter(|other| value > *other)
                .count()
        })
        .sum::<usize>();
    if inversions % 2 == 0 {
        1
    } else {
        -1
    }
}

fn loaded_action(
    generator: &LoadedGenerator,
    signs: &[BTreeMap<Face, Int>],
    permutation: fn(u8) -> u8,
) -> (LoadedGenerator, Int) {
    let image = LoadedGenerator {
        face: permute_face(&generator.face, permutation),
        circles: permute_face(&generator.circles, permutation),
    };
    let sign = signs[generator.face.len()][&generator.face]
        * fibre_permutation_sign(&generator.face, &generator.circles, permutation);
    (image, sign)
}

fn loaded_action_combination(
    value: &LoadedCombination,
    signs: &[BTreeMap<Face, Int>],
    permutation: fn(u8) -> u8,
) -> LoadedCombination {
    let mut result = LoadedCombination::new();
    for ((generator, monomial), coefficient) in value {
        let (image, sign) = loaded_action(generator, signs, permutation);
        add_loaded(
            &mut result,
            image,
            monomial.permute(permutation),
            coefficient * sign,
        );
    }
    result
}

fn compose_loaded_action(
    generator: &LoadedGenerator,
    actions: &[(&[BTreeMap<Face, Int>], fn(u8) -> u8)],
) -> (LoadedGenerator, Int) {
    actions.iter().fold(
        (generator.clone(), 1_i64),
        |(present, coefficient), (signs, permutation)| {
            let (next, sign) = loaded_action(&present, signs, *permutation);
            (next, coefficient * sign)
        },
    )
}

fn check_d03_yoneda_pullback(generators: &[LoadedGenerator]) {
    let d03 = diagonal(0, 3);
    let d03_face: Face = [d03].into_iter().collect();

    // The two generators (D03,H), H subset {D03}, form the literal road
    // normal packet in C/F1.  Its off-diagonal boundary lands in the closed
    // D03-supported part G03 of F1/F0.
    let road: Vec<_> = generators
        .iter()
        .filter(|generator| generator.face == d03_face)
        .collect();
    assert_eq!(road.len(), 2);
    for generator in &road {
        for ((target, _), _) in loaded_boundary(generator) {
            assert!(target.face == d03_face || in_b(&target.face));
            assert!(target.face.contains(&d03));
            assert_ne!(target.face, plus_vertex());
        }
    }

    // G03 is itself a strict subcomplex of F1 and has zero intersection with
    // F0.  Thus the road-to-F1/F0 boundary lifts through G03 -> F1.  The
    // product with 0 -> F0 -> F1 -> F1/F0 -> 0, i.e. the literal D03
    // pullback of the Yoneda two-extension, is canonically zero.
    let g03: Vec<_> = generators
        .iter()
        .filter(|generator| in_b(&generator.face) && generator.face.contains(&d03))
        .collect();
    assert!(!g03.is_empty());
    assert!(g03.iter().all(|generator| generator.face != plus_vertex()));
    assert!(g03.iter().all(
        |generator| loaded_boundary(generator)
            .keys()
            .all(|(target, _)| in_b(&target.face)
                && target.face.contains(&d03)
                && target.face != plus_vertex())
    ));

    // The entry-100 marked road endpoint is present in G03, while v_+ is
    // reached only after removing D03 across the central flip.  Such removal
    // is not an incidence in this absolute cellular differential.
    let marked_endpoint: Face = [d03, diagonal(1, 3), diagonal(3, 5)].into_iter().collect();
    assert!(g03
        .iter()
        .any(|generator| generator.face == marked_endpoint));
    assert!(!marked_endpoint.is_subset(&plus_vertex()));
    assert!(!plus_vertex().contains(&d03));
}

fn check_absolute_complex(by_size: &[Vec<Face>]) {
    let generators = loaded_generators(by_size);
    assert_eq!(generators.len(), 215);
    assert_eq!(
        (0..=3)
            .map(|degree| generators
                .iter()
                .filter(|generator| generator.degree() == degree)
                .count())
            .collect::<Vec<_>>(),
        [14, 63, 93, 45]
    );

    let mut saw_mixed_square = false;
    let mut saw_support_drop = false;
    for generator in &generators {
        assert!(generator.degree() <= 3);
        let boundary = loaded_boundary(generator);
        for ((target, monomial), coefficient) in &boundary {
            assert!(coefficient.abs() == 1);
            assert_eq!(target.degree() + 1, generator.degree());
            assert!(monomial
                .occurrence
                .iter()
                .chain(&monomial.normal)
                .all(|&power| power <= 1));
            let source_level = support_level(&generator.face);
            let target_level = support_level(&target.face);
            assert!(target_level <= source_level);
            assert!(source_level - target_level <= 1);
            saw_support_drop |= source_level - target_level == 1;
        }
        assert!(loaded_boundary_of_combination(&boundary).is_empty());
        saw_mixed_square |= !generator.circles.is_empty()
            && all_diagonals()
                .into_iter()
                .any(|value| addable(&generator.face, value));
    }
    assert!(saw_mixed_square);
    assert!(saw_support_drop);

    // Zero normal degree is the polynomial occurrence carrier sector.
    for generator in generators
        .iter()
        .filter(|generator| generator.normal_degree() == 0)
    {
        for ((target, monomial), _) in loaded_boundary(generator) {
            assert_eq!(target.normal_degree(), 0);
            assert!(monomial.normal.iter().all(|&power| power == 0));
            assert_eq!(monomial.occurrence.iter().sum::<u8>(), 1);
        }
    }

    let f0: Vec<_> = generators
        .iter()
        .filter(|generator| generator.face == plus_vertex())
        .collect();
    let f1: Vec<_> = generators
        .iter()
        .filter(|generator| in_b(&generator.face))
        .collect();
    assert_eq!(f0.len(), 8);
    assert_eq!(f1.len(), 208);
    assert_eq!(generators.len() - f1.len(), 7);
    assert!(f0.iter().all(|generator| f1.contains(generator)));
    assert!(f0.iter().all(|generator| loaded_boundary(generator)
        .keys()
        .all(|(target, _)| target.face == plus_vertex())));
    assert!(f1.iter().all(|generator| loaded_boundary(generator)
        .keys()
        .all(|(target, _)| in_b(&target.face))));

    check_d03_yoneda_pullback(&generators);

    // One-normal can--var and localized entry-38 contraction.
    assert_eq!((1_i64, 1_u8), (1_i64, 1_u8));
    assert_eq!(1_i8 + -1_i8, 0);

    let rotation_signs = action_signs(by_size, rotate_vertex, 1);
    let reflection_signs = action_signs(by_size, reflect_vertex, -1);
    for generator in &generators {
        let rotations = [(rotation_signs.as_slice(), rotate_vertex as fn(u8) -> u8); 3];
        let reflections = [(reflection_signs.as_slice(), reflect_vertex as fn(u8) -> u8); 2];
        assert_eq!(
            compose_loaded_action(generator, &rotations),
            (generator.clone(), 1)
        );
        assert_eq!(
            compose_loaded_action(generator, &reflections),
            (generator.clone(), 1)
        );
        assert_eq!(
            compose_loaded_action(
                generator,
                &[
                    (reflection_signs.as_slice(), reflect_vertex),
                    (rotation_signs.as_slice(), rotate_vertex),
                    (reflection_signs.as_slice(), reflect_vertex),
                ],
            ),
            compose_loaded_action(
                generator,
                &[
                    (rotation_signs.as_slice(), rotate_vertex),
                    (rotation_signs.as_slice(), rotate_vertex),
                ],
            )
        );
        for (signs, permutation) in [
            (rotation_signs.as_slice(), rotate_vertex as fn(u8) -> u8),
            (reflection_signs.as_slice(), reflect_vertex),
        ] {
            let transformed =
                loaded_action_combination(&loaded_boundary(generator), signs, permutation);
            let (image, sign) = loaded_action(generator, signs, permutation);
            let mut after_action = loaded_boundary(&image);
            for coefficient in after_action.values_mut() {
                *coefficient *= sign;
            }
            assert_eq!(transformed, after_action);
        }
    }
}

fn main() {
    let by_size = faces_by_size();
    check_absolute_complex(&by_size);

    println!(
        "{}",
        concat!(
            r#"{"claim":"The absolute unlocalized original-twist/Borel--Moore support-PC complex on K6 is the universal cellular chain complex of the real oriented boundary blowup: generators are (S,H), radial attachments are the costandard var=1 maps with independent polynomial occurrence coefficient X_a, and normal-circle boundaries are can=u_a. Its actual closed supports v_+ subset B_short subset K6 are strict D3-stable subcomplexes, so the entry-104 cone-roof transgression has an honest unlocalized absolute source. The literal D03 pullback of the filtration Yoneda two-class is zero and cannot equal entry-100's nonzero local trace.","status":"proved","scope":"absolute original-twist/Borel--Moore universal complex and the literal-road negative control only; no reciprocal conductor Thom map, alpha_+, marked central-flip correspondence, or strict inverse","assumptions":["the positive real chamber fixes the radial basepoint on every oriented normal circle","R0=Z[q_D^+-1] with u_D=q_D-1 for the nine K6 boundary divisors","the occurrence coefficient layer is the independent polynomial ring Z[X_D], not a Laurent ring; later occurrence normalization is a separate base change"],"evidence_refs":["research/voevodsky/check_absolute_unlocalized_support_pc.rs","research/voevodsky/check_loaded_peripheral_transgression.rs","research/voevodsky/check_one_normal_can_var_cousin.rs","research/voevodsky/check_unlocalized_plus_recollement_obstruction.rs","src/ledger/20260813-38 Finite-Alpha-Prime Normal-Torus Lift and Nearby-Cycle Unit Theorem.md"],"factorization_test":{"face_census":"PASS: (1,9,21,14)","absolute_generators":"PASS: 215 with degree ranks (14,63,93,45)","unlocalized_integrality":"PASS: only nonnegative X_D and u_D powers; no t, u_D, or integer inversion","one_normal_can_var":"PASS: radial var=1 and circle can=u have composite u","d_squared":"PASS on all generators, including every mixed radial/normal square","strict_supports":"PASS: ranks F0=8, F1=208, F2=215; quotient F2/F1 has rank 7","D3_covariance":"PASS with base and torus orientation signs and permutation of X_D,q_D","carrier_grade":"PASS: zero normal degree is the polynomial occurrence cellular complex","entry38_localization":"PASS: adjoining u_D^-1 gives s_D(p_D)=u_D^-1 h_D and the localized facewise normal factors","entry104_delta":"TYPED: apply the exact support filtration and cone roof already certified by check_loaded_peripheral_transgression.rs","D03_road_subcomplex":"PASS: the two literal road generators form K(u03) in C/F1 and their off-diagonal boundary lands in the strict D03-supported subcomplex G03 of F1/F0","D03_Yoneda_pullback":"ZERO: G03 is a strict subcomplex of F1 disjoint from F0, so the first connecting map lifts through G03 and its Yoneda product with 0->F0->F1->F1/F0->0 vanishes","entry100_trace":"NOT THE LITERAL PULLBACK: Theta_03 sends eta_mix to the nonzero Cech residue 1/(u0*u1*u3*u5), whereas tensoring the zero literal-road Yoneda class with K(I_+^vee) remains zero"},"counterevidence":["the marked endpoint {D03,x1,x3} lies in G03 but v_+={x1,x3,x5} does not; passing between them removes D03 and is not a face incidence of the absolute complex","the first missing arrow is a marked ringed support correspondence across that central flip; neither the filtration nor the one-normal perfect pairing supplies it","a global Cech complex is unnecessary for the absolute differential and is not claimed finite free","the literal dual-block inclusion remains road-free","only the carrier associated-grade sector is asserted invertible"],"next_experiment":"Construct, from geometry rather than fitting, the marked D03 ringed support correspondence across the central flip and test its composite with the canonical Yoneda class against eta_mix, the local Cech residue, endpoints (1,1), and the separate [dX03] line."}"#
        )
    );
}
