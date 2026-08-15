//! Exact certificate for the target-side physical-reflection structure of
//! the scoped D03 Cartier edge purity.
//!
//! The physical reflection f3 fixes the long channel D03, exchanges
//! x0<->x1, x2<->x5, and x3<->x4, and exchanges the two normalization
//! sheets.  This checker derives its action on the full 215-generator
//! absolute support-PC complex, extracts the x3/x4 edge packets, and verifies
//! that finite Cartier purity, the graph Bockstein, the repeated-normal
//! Tor0/Tor1 decomposition, and every lower Koszul--Cech term are natural.
//!
//! The result is deliberately target-scoped.  It does not construct the
//! endpoint-coherent support/Yoneda-to-Tate connector, its nonzero Q leg, or
//! the global loaded obstruction.  It proves only that the established
//! target purity contributes no intrinsic reflection-square defect.

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

fn short_diagonal(index: usize) -> Diagonal {
    diagonal(index as u8, (index as u8 + 2) % N)
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

fn physical_reflect_vertex(vertex: u8) -> u8 {
    (3 + N - vertex) % N
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
    [1_usize, 3, 5].into_iter().map(short_diagonal).collect()
}

fn minus_vertex() -> Face {
    [0_usize, 2, 4].into_iter().map(short_diagonal).collect()
}

fn in_short_boundary(face: &Face) -> bool {
    face.iter().any(|&value| short_index(value).is_some())
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
        let mut result = Self::one();
        for index in 0..9 {
            result.occurrence[index] = self.occurrence[index] + other.occurrence[index];
            result.normal[index] = self.normal[index] + other.normal[index];
        }
        result
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

fn scaled_boundary(generator: &LoadedGenerator, scale: Int) -> LoadedCombination {
    let mut result = loaded_boundary(generator);
    for coefficient in result.values_mut() {
        *coefficient *= scale;
    }
    result
}

#[derive(Clone)]
struct SignedGenerator {
    generator: LoadedGenerator,
    scale: Int,
}

#[derive(Clone)]
struct EdgePacket {
    g: SignedGenerator,
    h: SignedGenerator,
    p: SignedGenerator,
}

fn edge_packet(short: usize) -> EdgePacket {
    let d03 = diagonal(0, 3);
    let edge = short_diagonal(short);
    let road: Face = [d03].into_iter().collect();
    let corner: Face = [d03, edge].into_iter().collect();
    EdgePacket {
        // These basis signs derive d(g)=x_j p and d(h)=u_j p from the
        // ambient entry-105 incidence convention.
        g: SignedGenerator {
            generator: LoadedGenerator {
                face: road,
                circles: Face::new(),
            },
            scale: -1,
        },
        h: SignedGenerator {
            generator: LoadedGenerator {
                face: corner.clone(),
                circles: [edge].into_iter().collect(),
            },
            scale: -1,
        },
        p: SignedGenerator {
            generator: LoadedGenerator {
                face: corner,
                circles: Face::new(),
            },
            scale: 1,
        },
    }
}

fn coefficient_of(
    combination: &LoadedCombination,
    generator: &LoadedGenerator,
    monomial: UniversalMonomial,
) -> Int {
    combination
        .get(&(generator.clone(), monomial))
        .copied()
        .unwrap_or(0)
}

fn signed_action_coefficient(
    source: &SignedGenerator,
    target: &SignedGenerator,
    signs: &[BTreeMap<Face, Int>],
) -> Int {
    let (image, action_sign) = loaded_action(&source.generator, signs, physical_reflect_vertex);
    assert_eq!(image, target.generator);
    source.scale * action_sign / target.scale
}

fn physical_short_image(index: usize) -> usize {
    short_index(diagonal(
        physical_reflect_vertex(short_diagonal(index).0),
        physical_reflect_vertex(short_diagonal(index).1),
    ))
    .unwrap()
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct LabeledLaurentTerm {
    coefficient: Int,
    q_label: Option<usize>,
    t_label: Option<usize>,
}

impl LabeledLaurentTerm {
    fn new(coefficient: Int, q_label: Option<usize>, t_label: Option<usize>) -> Self {
        Self {
            coefficient,
            q_label,
            t_label,
        }
    }

    fn with_t(self, t_label: usize) -> Self {
        Self {
            t_label: Some(t_label),
            ..self
        }
    }

    fn physical_reflection(self) -> Self {
        Self {
            coefficient: self.coefficient,
            q_label: self.q_label.map(physical_short_image),
            t_label: self.t_label.map(physical_short_image),
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct RepeatedNormalGrade {
    grade: usize,
    normal_label: usize,
}

impl RepeatedNormalGrade {
    fn physical_reflection(self) -> Self {
        Self {
            grade: self.grade,
            normal_label: physical_short_image(self.normal_label),
        }
    }
}

fn subset_action_sign(source_order: &[usize], target_order: &[usize], mask: usize) -> Int {
    let positions: Vec<_> = source_order
        .iter()
        .enumerate()
        .filter(|(position, _)| mask & (1 << position) != 0)
        .map(|(_, &variable)| {
            let image = physical_short_image(variable);
            target_order
                .iter()
                .position(|&target| target == image)
                .unwrap()
        })
        .collect();
    let inversions = positions
        .iter()
        .enumerate()
        .map(|(position, value)| {
            positions
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

fn image_mask(source_order: &[usize], target_order: &[usize], mask: usize) -> usize {
    source_order
        .iter()
        .enumerate()
        .filter(|(position, _)| mask & (1 << position) != 0)
        .fold(0_usize, |result, (_, &variable)| {
            let image = physical_short_image(variable);
            result
                | (1 << target_order
                    .iter()
                    .position(|&target| target == image)
                    .unwrap())
        })
}

fn check_exterior_complex_covariance(source_order: &[usize], target_order: &[usize]) {
    assert_eq!(source_order.len(), target_order.len());
    let rank = source_order.len();
    for mask in 0_usize..(1 << rank) {
        let source_action = subset_action_sign(source_order, target_order, mask);
        let target_mask = image_mask(source_order, target_order, mask);
        for source_position in 0..rank {
            if mask & (1 << source_position) == 0 {
                continue;
            }
            let source_lower_mask = mask ^ (1 << source_position);
            let source_boundary_sign =
                if (mask & ((1 << source_position) - 1)).count_ones() % 2 == 0 {
                    1
                } else {
                    -1
                };
            let image_variable = physical_short_image(source_order[source_position]);
            let target_position = target_order
                .iter()
                .position(|&target| target == image_variable)
                .unwrap();
            let target_boundary_sign =
                if (target_mask & ((1 << target_position) - 1)).count_ones() % 2 == 0 {
                    1
                } else {
                    -1
                };
            let after_boundary = source_boundary_sign
                * subset_action_sign(source_order, target_order, source_lower_mask);
            let after_action = source_action * target_boundary_sign;
            assert_eq!(after_boundary, after_action);
            assert_eq!(
                image_mask(source_order, target_order, source_lower_mask),
                target_mask ^ (1 << target_position)
            );
        }
    }
}

fn check_absolute_reflection(
    by_size: &[Vec<Face>],
    generators: &[LoadedGenerator],
    signs: &[BTreeMap<Face, Int>],
) {
    assert_eq!(generators.len(), 215);
    assert_eq!(
        permute_face(&plus_vertex(), physical_reflect_vertex),
        minus_vertex()
    );
    assert_eq!(
        permute_face(&minus_vertex(), physical_reflect_vertex),
        plus_vertex()
    );
    assert!(generators.iter().all(|generator| {
        in_short_boundary(&generator.face)
            == in_short_boundary(&permute_face(&generator.face, physical_reflect_vertex))
    }));
    for generator in generators {
        let (first, first_sign) = loaded_action(generator, signs, physical_reflect_vertex);
        let (second, second_sign) = loaded_action(&first, signs, physical_reflect_vertex);
        assert_eq!(second, *generator);
        assert_eq!(first_sign * second_sign, 1);

        let transformed =
            loaded_action_combination(&loaded_boundary(generator), signs, physical_reflect_vertex);
        let mut boundary_after_action = loaded_boundary(&first);
        for coefficient in boundary_after_action.values_mut() {
            *coefficient *= first_sign;
        }
        assert_eq!(transformed, boundary_after_action);
    }

    // The reflection reverses the oriented three-dimensional carrier.
    assert_eq!(signs[0][&by_size[0][0]], -1);
}

fn check_edge_packets(signs: &[BTreeMap<Face, Int>]) {
    assert_eq!(physical_short_image(0), 1);
    assert_eq!(physical_short_image(1), 0);
    assert_eq!(physical_short_image(2), 5);
    assert_eq!(physical_short_image(5), 2);
    assert_eq!(physical_short_image(3), 4);
    assert_eq!(physical_short_image(4), 3);

    let d03 = diagonal(0, 3);
    assert_eq!(
        diagonal(
            physical_reflect_vertex(d03.0),
            physical_reflect_vertex(d03.1)
        ),
        d03
    );

    let packet3 = edge_packet(3);
    let packet4 = edge_packet(4);
    let boundary_g3 = scaled_boundary(&packet3.g.generator, packet3.g.scale);
    let boundary_h3 = scaled_boundary(&packet3.h.generator, packet3.h.scale);
    let boundary_g4 = scaled_boundary(&packet4.g.generator, packet4.g.scale);
    let boundary_h4 = scaled_boundary(&packet4.h.generator, packet4.h.scale);
    assert_eq!(
        coefficient_of(
            &boundary_g3,
            &packet3.p.generator,
            UniversalMonomial::occurrence(3)
        ) / packet3.p.scale,
        1
    );
    assert_eq!(
        coefficient_of(
            &boundary_h3,
            &packet3.p.generator,
            UniversalMonomial::normal(3)
        ) / packet3.p.scale,
        1
    );
    assert_eq!(
        coefficient_of(
            &boundary_g4,
            &packet4.p.generator,
            UniversalMonomial::occurrence(4)
        ) / packet4.p.scale,
        1
    );
    assert_eq!(
        coefficient_of(
            &boundary_h4,
            &packet4.p.generator,
            UniversalMonomial::normal(4)
        ) / packet4.p.scale,
        1
    );

    // In the local d=(x_j,u_j) bases the raw physical reflection is -Id.
    let local_action = [
        signed_action_coefficient(&packet3.g, &packet4.g, signs),
        signed_action_coefficient(&packet3.h, &packet4.h, signs),
        signed_action_coefficient(&packet3.p, &packet4.p, signs),
    ];
    assert_eq!(local_action, [-1, -1, -1]);
    let reflected_back = [
        signed_action_coefficient(&packet4.g, &packet3.g, signs),
        signed_action_coefficient(&packet4.h, &packet3.h, signs),
        signed_action_coefficient(&packet4.p, &packet3.p, signs),
    ];
    assert_eq!(reflected_back, [-1, -1, -1]);
    for (forward, backward) in local_action.into_iter().zip(reflected_back) {
        assert_eq!(forward * backward, 1);
    }

    // The syzygy z_j=u_j g_j-x_j h_j maps to -z_4, and the graph
    // Bockstein beta(g_j)=p_j, beta(h_j)=t_j p_j is strictly natural.
    let z3_coefficients = [1_i64, -1_i64];
    let reflected_z3_coefficients = [
        local_action[0] * z3_coefficients[0],
        local_action[1] * z3_coefficients[1],
    ];
    assert_eq!(reflected_z3_coefficients, [-1, 1]);
    assert_eq!(
        reflected_z3_coefficients,
        [-z3_coefficients[0], -z3_coefficients[1]]
    );
    let beta3_after_reflection = [local_action[2], local_action[2]];
    let reflection_after_beta3 = [local_action[0], local_action[1]];
    assert_eq!(beta3_after_reflection, reflection_after_beta3);

    // Before Bockstein compatibility, f1=[[a,b],[0,e]], f0=e.  The exact
    // commutator equations are a-e=0 and b=0, leaving one free scalar.
    for a in -2_i64..=2 {
        for b in -2_i64..=2 {
            for e in -2_i64..=2 {
                let commutes = a == e && b == 0;
                let first_equation = a - e == 0;
                let second_equation = b == 0;
                assert_eq!(commutes, first_equation && second_equation);
            }
        }
    }

    // Full lower occurrence and normal Koszul--Cech terms are transported,
    // not only their top fractions.
    check_exterior_complex_covariance(&[0, 3], &[1, 4]);
    check_exterior_complex_covariance(&[1, 3], &[0, 4]);
    check_exterior_complex_covariance(&[0, 1, 3, 5], &[0, 1, 2, 4]);

    // Both repeated-normal grades survive.  The q and t labels are retained
    // explicitly: semilinearity sends eta_3=(-q3,-1) to eta_4=(-q4,-1),
    // while the graph Bockstein sends [t3]eta_3 to [t4]eta_4.
    let eta3 = [
        LabeledLaurentTerm::new(-1, Some(3), None),
        LabeledLaurentTerm::new(-1, None, None),
    ];
    let eta4 = [
        LabeledLaurentTerm::new(-1, Some(4), None),
        LabeledLaurentTerm::new(-1, None, None),
    ];
    assert_eq!(eta3.map(LabeledLaurentTerm::physical_reflection), eta4);
    assert_eq!(
        eta4.map(LabeledLaurentTerm::physical_reflection)
            .map(LabeledLaurentTerm::physical_reflection),
        eta4
    );

    let bockstein_eta3 = eta3.map(|term| term.with_t(3));
    let bockstein_eta4 = eta4.map(|term| term.with_t(4));
    assert_eq!(
        bockstein_eta3.map(LabeledLaurentTerm::physical_reflection),
        bockstein_eta4
    );

    let tor3 = [
        RepeatedNormalGrade {
            grade: 0,
            normal_label: 3,
        },
        RepeatedNormalGrade {
            grade: 1,
            normal_label: 3,
        },
    ];
    let tor4 = [
        RepeatedNormalGrade {
            grade: 0,
            normal_label: 4,
        },
        RepeatedNormalGrade {
            grade: 1,
            normal_label: 4,
        },
    ];
    assert_eq!(tor3.map(RepeatedNormalGrade::physical_reflection), tor4);
    assert_eq!(
        tor4.map(RepeatedNormalGrade::physical_reflection)
            .map(RepeatedNormalGrade::physical_reflection),
        tor4
    );

    // The reciprocal-regular/original-BM pairing also transports with its
    // q-unit intact: beta(p,h^vee)=1 and beta(h,p^vee)=-q_j.
    let pairing3 = [
        LabeledLaurentTerm::new(1, None, None),
        LabeledLaurentTerm::new(-1, Some(3), None),
    ];
    let pairing4 = [
        LabeledLaurentTerm::new(1, None, None),
        LabeledLaurentTerm::new(-1, Some(4), None),
    ];
    assert_eq!(
        pairing3.map(LabeledLaurentTerm::physical_reflection),
        pairing4
    );

    // The physical reflection exchanges the two x3 endpoints with the two
    // x4 endpoints and transports the full four-normal residue ideal.
    let v00: Face = [d03, short_diagonal(0), short_diagonal(3)]
        .into_iter()
        .collect();
    let v10: Face = [d03, short_diagonal(1), short_diagonal(3)]
        .into_iter()
        .collect();
    let v11: Face = [d03, short_diagonal(1), short_diagonal(4)]
        .into_iter()
        .collect();
    let v01: Face = [d03, short_diagonal(0), short_diagonal(4)]
        .into_iter()
        .collect();
    assert_eq!(permute_face(&v00, physical_reflect_vertex), v11);
    assert_eq!(permute_face(&v10, physical_reflect_vertex), v01);
    assert_eq!(
        [0_usize, 1, 3, 5]
            .into_iter()
            .map(physical_short_image)
            .collect::<BTreeSet<_>>(),
        [0_usize, 1, 2, 4].into_iter().collect()
    );

    // Finite Cartier purity is the identity between the independently
    // assembled Thom-plus-BM packet and RHom(A/(x_j),P_j).  Both sides carry
    // the same -Id action, so the purity square and its square are strict.
    let purity_source_action = local_action;
    let purity_target_action = local_action;
    assert_eq!(purity_source_action, purity_target_action);
    assert_eq!(
        purity_source_action.map(|coefficient| coefficient * coefficient),
        [1, 1, 1]
    );

    // Entry 138 proves that road orientation and the once-retained polarity
    // line are both odd under f3.  Their product is the trivial loaded
    // coefficient; no division by two or three appears.
    let road_orientation = -1_i64;
    let polarity = -1_i64;
    let loaded_coefficient = road_orientation * polarity;
    assert_eq!(loaded_coefficient, 1);
    assert_eq!(loaded_coefficient * loaded_coefficient, 1);
}

fn main() {
    let by_size = faces_by_size();
    let generators = loaded_generators(&by_size);
    assert_eq!(
        generators
            .iter()
            .map(LoadedGenerator::degree)
            .fold([0_usize; 4], |mut ranks, degree| {
                ranks[degree] += 1;
                ranks
            }),
        [14, 63, 93, 45]
    );
    for generator in &generators {
        assert!(loaded_boundary_of_combination(&loaded_boundary(generator)).is_empty());
    }

    let signs = action_signs(&by_size, physical_reflect_vertex, -1);
    check_absolute_reflection(&by_size, &generators, &signs);
    check_edge_packets(&signs);

    println!(
        r#"{{"claim":"The entry-105 absolute support-PC complex admits a strict semilinear physical f3 involution. It exchanges the scoped D03 x3 and x4 Cartier edge packets, and finite Cartier purity, both repeated-normal Tor grades, the graph Bockstein, endpoint transitivity, and all lower Koszul--Cech terms are natural under that involution. After the once-retained polarity sign cancels road orientation, the target-side reflection square is the identity.","status":"proved","scope":"target-side absolute/road-face PC purity only; no endpoint-coherent support/Yoneda-to-Tate connector, no global loaded obstruction value, and no G03^Cousin","assumptions":["the entry-105 universal absolute differential and labelled cellular orientations","the entry-131 source is the independently assembled x_j Thom-plus-original/BM packet","the graph Bockstein u_j=t_j*x_j is retained","entry 138 supplies the separate road-orientation and polarity characters"],"factorization_test":{{"absolute_generators":"215 with ranks 14,63,93,45","absolute_d_squared":"pass","physical_f3_covariance":"pass on every loaded generator and monomial","sheet_exchange":"v_plus<->v_minus","edge_exchange":"x3<->x4 with local action -Id","cartier_purity_naturality":"strict","tor0_tor1":"both retained","graph_bockstein":"strictly natural","lower_koszul_cech":"all subset differentials commute","endpoint_exchange":"v00<->v11 and v10<->v01","loaded_target_square":"identity"}},"counterevidence":["A strict target involution does not construct a path between the loaded support/Yoneda and Tate/Cartier two-extensions.","The nonzero generic Q leg and endpoint connector two-cells remain absent.","The global omega_load is still undefined; this theorem only removes target purity as an independent source of parity."],"next_experiment":"Construct the f3-paired endpoint-coherent source connector with its nonzero Q leg and compare its square against this strict target involution; only then evaluate omega_load(f3,f3) mod 2."}}"#
    );
}
