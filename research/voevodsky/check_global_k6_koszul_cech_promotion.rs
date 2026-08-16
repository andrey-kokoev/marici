//! Global target-side Koszul--Cech promotion of the absolute K6 support packet.
//!
//! For a noncrossing dissection S and H subset S, use the 215 generators
//! (S,H) of the real oriented boundary blowup.  Put
//!
//!   lambda(S,H) = product_{a in S minus H} u_a^{-1}.
//!
//! The finite original-twist/BM differential has radial coefficient X_a and
//! normal coefficient u_h.  Its extended Cech realization is therefore forced
//! to have radial coefficient X_a/u_a and normal coefficient 1:
//!
//!   d_Cech Lambda = Lambda d_finite.
//!
//! Denominators occur only in the indicated target Cech summands.  The
//! occurrence layer stays polynomial, and the whole source is never globally
//! localized.  This certificate constructs only the target-side promotion;
//! it does not construct the reciprocal normalization-sheet packet or the
//! endpoint-pointed butterfly required for G_03^Cousin.

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

#[derive(Clone, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Generator {
    face: Face,
    circles: Face,
}

impl Generator {
    fn degree(&self) -> usize {
        DIMENSION - self.face.len() + self.circles.len()
    }
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

fn generators(by_size: &[Vec<Face>]) -> Vec<Generator> {
    by_size
        .iter()
        .flatten()
        .flat_map(|face| {
            subsets(face).into_iter().map(|circles| Generator {
                face: face.clone(),
                circles,
            })
        })
        .collect()
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct LaurentMonomial {
    occurrence: [i8; 9],
    normal: [i8; 9],
}

impl LaurentMonomial {
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

    fn inverse_normal(index: usize) -> Self {
        let mut result = Self::one();
        result.normal[index] = -1;
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

type Combination = BTreeMap<(Generator, LaurentMonomial), Int>;

fn add_term(
    value: &mut Combination,
    generator: Generator,
    monomial: LaurentMonomial,
    coefficient: Int,
) {
    *value.entry((generator, monomial)).or_default() += coefficient;
    value.retain(|_, entry| *entry != 0);
}

fn localization_monomial(generator: &Generator) -> LaurentMonomial {
    let mut result = LaurentMonomial::one();
    for value in generator.face.difference(&generator.circles) {
        result.normal[variable_index(*value)] = -1;
    }
    result
}

fn denominator_allowed(generator: &Generator, monomial: LaurentMonomial) -> bool {
    if monomial.occurrence.iter().any(|power| *power < 0) {
        return false;
    }
    for value in all_diagonals() {
        let exponent = monomial.normal[variable_index(value)];
        if exponent < 0 && (!generator.face.contains(&value) || generator.circles.contains(&value))
        {
            return false;
        }
    }
    true
}

fn boundary(generator: &Generator, cech: bool) -> Combination {
    assert!(generator.circles.is_subset(&generator.face));
    let mut result = Combination::new();

    for added in all_diagonals()
        .into_iter()
        .filter(|&value| addable(&generator.face, value))
    {
        let mut target_face = generator.face.clone();
        target_face.insert(added);
        let target = Generator {
            face: target_face,
            circles: generator.circles.clone(),
        };
        let index = variable_index(added);
        let monomial = if cech {
            LaurentMonomial::occurrence(index).multiply(LaurentMonomial::inverse_normal(index))
        } else {
            LaurentMonomial::occurrence(index)
        };
        assert!(!cech || denominator_allowed(&target, monomial));
        add_term(
            &mut result,
            target,
            monomial,
            incidence_sign(&generator.face, added),
        );
    }

    let base_dimension = DIMENSION - generator.face.len();
    for (position, removed) in generator.circles.iter().copied().enumerate() {
        let mut target_circles = generator.circles.clone();
        target_circles.remove(&removed);
        let sign = if (base_dimension + position) % 2 == 0 {
            1
        } else {
            -1
        };
        add_term(
            &mut result,
            Generator {
                face: generator.face.clone(),
                circles: target_circles,
            },
            if cech {
                LaurentMonomial::one()
            } else {
                LaurentMonomial::normal(variable_index(removed))
            },
            sign,
        );
    }

    result
}

fn boundary_of_combination(value: &Combination, cech: bool) -> Combination {
    let mut result = Combination::new();
    for ((generator, monomial), coefficient) in value {
        for ((target, boundary_monomial), boundary_coefficient) in boundary(generator, cech) {
            add_term(
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

fn action(
    generator: &Generator,
    signs: &[BTreeMap<Face, Int>],
    permutation: fn(u8) -> u8,
) -> (Generator, Int) {
    (
        Generator {
            face: permute_face(&generator.face, permutation),
            circles: permute_face(&generator.circles, permutation),
        },
        signs[generator.face.len()][&generator.face]
            * fibre_permutation_sign(&generator.face, &generator.circles, permutation),
    )
}

fn action_combination(
    value: &Combination,
    signs: &[BTreeMap<Face, Int>],
    permutation: fn(u8) -> u8,
) -> Combination {
    let mut result = Combination::new();
    for ((generator, monomial), coefficient) in value {
        let (image, sign) = action(generator, signs, permutation);
        add_term(
            &mut result,
            image,
            monomial.permute(permutation),
            coefficient * sign,
        );
    }
    result
}

fn compose_action(
    generator: &Generator,
    actions: &[(&[BTreeMap<Face, Int>], fn(u8) -> u8)],
) -> (Generator, Int) {
    actions.iter().fold(
        (generator.clone(), 1),
        |(present, coefficient), (signs, permutation)| {
            let (next, sign) = action(&present, signs, *permutation);
            (next, coefficient * sign)
        },
    )
}

fn check_kappa(generator: &Generator) {
    let source_localization = localization_monomial(generator);
    assert!(denominator_allowed(generator, source_localization));

    let mut left = Combination::new();
    for ((target, coefficient), sign) in boundary(generator, true) {
        add_term(
            &mut left,
            target,
            source_localization.multiply(coefficient),
            sign,
        );
    }

    let mut right = Combination::new();
    for ((target, finite_coefficient), sign) in boundary(generator, false) {
        add_term(
            &mut right,
            target.clone(),
            finite_coefficient.multiply(localization_monomial(&target)),
            sign,
        );
    }
    assert_eq!(left, right);
}

fn plus_vertex() -> Face {
    [1_usize, 3, 5]
        .into_iter()
        .map(|index| diagonal(index as u8, (index as u8 + 2) % N))
        .collect()
}

fn minus_vertex() -> Face {
    [0_usize, 2, 4]
        .into_iter()
        .map(|index| diagonal(index as u8, (index as u8 + 2) % N))
        .collect()
}

fn in_endpoint_support(face: &Face) -> bool {
    face == &plus_vertex() || face == &minus_vertex()
}

fn in_b(face: &Face) -> bool {
    face.iter().any(|value| short_index(*value).is_some())
}

fn degree_ranks(generators: &[Generator], predicate: &dyn Fn(&Face) -> bool) -> [usize; 4] {
    std::array::from_fn(|degree| {
        generators
            .iter()
            .filter(|generator| generator.degree() == degree && predicate(&generator.face))
            .count()
    })
}

fn subtract(left: [usize; 4], right: [usize; 4]) -> [usize; 4] {
    std::array::from_fn(|index| left[index] - right[index])
}

fn check_support_filtration(generators: &[Generator]) {
    let full = degree_ranks(generators, &|_| true);
    let boundary_support = degree_ranks(generators, &in_b);
    let endpoints = degree_ranks(generators, &in_endpoint_support);
    assert_eq!(full, [14, 63, 93, 45]);
    assert_eq!(boundary_support, [14, 63, 90, 41]);
    assert_eq!(endpoints, [2, 6, 6, 2]);
    assert_eq!(subtract(full, endpoints), [12, 57, 87, 43]);
    assert_eq!(subtract(boundary_support, endpoints), [12, 57, 84, 39]);
    assert_eq!(subtract(full, boundary_support), [0, 0, 3, 4]);

    for generator in generators {
        for ((target, _), _) in boundary(generator, true) {
            if in_endpoint_support(&generator.face) {
                assert!(in_endpoint_support(&target.face));
            }
            if in_b(&generator.face) {
                assert!(in_b(&target.face));
            }
        }
    }

    let q_generators: Vec<_> = generators
        .iter()
        .filter(|generator| !in_b(&generator.face))
        .collect();
    assert_eq!(q_generators.len(), 7);
    let top = q_generators
        .iter()
        .find(|generator| generator.face.is_empty())
        .expect("the generic chamber survives in Q");
    let surviving_top_terms: Vec<_> = boundary(top, true)
        .into_iter()
        .filter(|((target, _), _)| !in_b(&target.face))
        .collect();
    assert_eq!(surviving_top_terms.len(), 3);
    assert!(surviving_top_terms
        .iter()
        .all(|((target, monomial), sign)| {
            target.face.len() == 1
                && target.face.iter().all(|value| long_index(*value).is_some())
                && monomial.occurrence.iter().sum::<i8>() == 1
                && monomial.normal.iter().sum::<i8>() == -1
                && sign.abs() == 1
        }));
}

fn check_d3(by_size: &[Vec<Face>], generators: &[Generator]) {
    let rotation_signs = action_signs(by_size, rotate_vertex, 1);
    let reflection_signs = action_signs(by_size, reflect_vertex, -1);

    for generator in generators {
        let rotations = [(rotation_signs.as_slice(), rotate_vertex as fn(u8) -> u8); 3];
        let reflections = [(reflection_signs.as_slice(), reflect_vertex as fn(u8) -> u8); 2];
        assert_eq!(
            compose_action(generator, &rotations),
            (generator.clone(), 1)
        );
        assert_eq!(
            compose_action(generator, &reflections),
            (generator.clone(), 1)
        );

        for (signs, permutation) in [
            (rotation_signs.as_slice(), rotate_vertex as fn(u8) -> u8),
            (reflection_signs.as_slice(), reflect_vertex),
        ] {
            let transformed = action_combination(&boundary(generator, true), signs, permutation);
            let (image, sign) = action(generator, signs, permutation);
            let mut after_action = boundary(&image, true);
            for coefficient in after_action.values_mut() {
                *coefficient *= sign;
            }
            assert_eq!(transformed, after_action);
            assert_eq!(
                localization_monomial(&image),
                localization_monomial(generator).permute(permutation)
            );
        }
    }
}

fn main() {
    let by_size = faces_by_size();
    let loaded = generators(&by_size);
    assert_eq!(loaded.len(), 215);

    let mut radial_terms = 0_usize;
    let mut normal_terms = 0_usize;
    for generator in &loaded {
        let finite_boundary = boundary(generator, false);
        let cech_boundary = boundary(generator, true);
        assert!(boundary_of_combination(&finite_boundary, false).is_empty());
        assert!(boundary_of_combination(&cech_boundary, true).is_empty());
        check_kappa(generator);

        for ((target, monomial), coefficient) in cech_boundary {
            assert_eq!(target.degree() + 1, generator.degree());
            assert!(coefficient.abs() == 1);
            assert!(denominator_allowed(&target, monomial));
            if monomial.occurrence.iter().sum::<i8>() == 1 {
                radial_terms += 1;
                assert_eq!(monomial.normal.iter().sum::<i8>(), -1);
            } else {
                normal_terms += 1;
                assert_eq!(monomial, LaurentMonomial::one());
            }
        }
    }
    assert!(radial_terms > 0);
    assert!(normal_terms > 0);

    check_support_filtration(&loaded);
    check_d3(&by_size, &loaded);

    println!(
        "{}",
        concat!(
            r#"{"claim":"The 215-generator absolute original-twist/Borel--Moore K6 support packet admits a canonical target-side extended Koszul--Cech promotion. On (S,H), kappa is multiplication by lambda(S,H)=prod_{a in S\\H}u_a^-1; the promoted radial differential is epsilon X_a/u_a and the promoted normal differential is the signed unit localization. Thus d_Cech kappa=kappa d_finite termwise and d_Cech^2=0. The two-endpoint filtration V={v_plus,v_minus} subset B_short subset K6 and its Q quotient remain strict and D3-covariant.","status":"proved","scope":"target-side original-twist/BM extended Cech diagram only; no reciprocal normalization-sheet packet, marked conductor-to-road kernel, endpoint-pointed butterfly, or G_03^Cousin","checks":{"absolute_generators":"PASS: 215","degree_ranks":"PASS: (14,63,93,45)","kappa_formula":"PASS on every generator","finite_d_squared":"PASS on every generator","cech_d_squared":"PASS on every generator","minimal_denominators":"PASS: each u_a^-1 occurs only in a target summand where a belongs to S minus H","occurrence_layer":"PASS: polynomial X_a only; no occurrence inverse","D3_covariance":"PASS for rotation, reflection, fibre orientation, and coefficient permutation","endpoint_Q_filtration":"PASS: V degrees (2,6,6,2), B/V (12,57,84,39), E=K/V (12,57,87,43), Q (0,0,3,4)","generic_Q_leg":"PASS: the generic chamber has three surviving long-facet arrows X_D/u_D in Q"},"boundary":"This theorem constructs the target Cech realization of the endpoint/Q packet, but it does not supply the source normalization-Cech sheet arrow or the two endpoint connector cells. Those remain the first data needed to form d_sp,sc and G_03^Cousin without choosing the unresolved Z/2 butterfly point."}"#
        )
    );
}
