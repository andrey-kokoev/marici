//! Exact finite audit of the proposed n=8 scalar-strata site.
//!
//! The base objects are closed support faces
//!
//!     X_S = { triangulations T : S is a subset of T }
//!
//! for a noncrossing set S of octagon diagonals, together with the empty
//! object.  Thus "at least P" physical support is used; disjoint exact-core
//! pieces are not objects of the incidence calculation.
//!
//! This checker proves only finite incidence claims.  It deliberately does
//! not manufacture a Grothendieck coverage or a Voevodsky density structure.

use std::collections::{BTreeMap, BTreeSet};

const N: usize = 8;
const TOP_DIMENSION: isize = (N - 3) as isize;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Edge(usize, usize);

type Face = Vec<Edge>;
type Triangulation = Vec<Edge>;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Bits([u64; 3]);

impl Bits {
    const EMPTY: Self = Self([0; 3]);

    fn insert(&mut self, index: usize) {
        self.0[index / 64] |= 1_u64 << (index % 64);
    }

    fn intersection(self, other: Self) -> Self {
        Self(std::array::from_fn(|index| self.0[index] & other.0[index]))
    }

    fn union(self, other: Self) -> Self {
        Self(std::array::from_fn(|index| self.0[index] | other.0[index]))
    }

    fn contains(self, index: usize) -> bool {
        self.0[index / 64] & (1_u64 << (index % 64)) != 0
    }

    fn is_subset_of(self, other: Self) -> bool {
        (0..3).all(|index| self.0[index] & !other.0[index] == 0)
    }

    fn count(self) -> usize {
        self.0.iter().map(|word| word.count_ones() as usize).sum()
    }
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum Family {
    PhysicalPhysical,
    ScalarScalarIndependent,
    ScalarPhysicalIndependent,
}

#[derive(Clone, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Generator {
    family: Family,
    base: Face,
    first: Edge,
    second: Edge,
}

fn edge(first: usize, second: usize) -> Edge {
    assert_ne!(first, second);
    if first < second {
        Edge(first, second)
    } else {
        Edge(second, first)
    }
}

fn boundary_edge(value: Edge) -> bool {
    value.1 == value.0 + 1 || (value.0 == 0 && value.1 == N - 1)
}

fn physical(value: Edge) -> bool {
    value.0 % 2 != value.1 % 2
}

fn crosses(first: Edge, second: Edge) -> bool {
    if first.0 == second.0 || first.0 == second.1 || first.1 == second.0 || first.1 == second.1 {
        return false;
    }
    (first.0 < second.0 && second.0 < first.1 && first.1 < second.1)
        || (second.0 < first.0 && first.0 < second.1 && second.1 < first.1)
}

fn compatible(face: &Face) -> bool {
    (0..face.len())
        .all(|first| (first + 1..face.len()).all(|second| !crosses(face[first], face[second])))
}

fn contains(face: &Face, value: Edge) -> bool {
    face.binary_search(&value).is_ok()
}

fn face_union(first: &Face, second: &Face) -> Face {
    let mut result = first.clone();
    result.extend(second.iter().copied());
    result.sort();
    result.dedup();
    result
}

fn add_edge(face: &Face, value: Edge) -> Face {
    face_union(face, &vec![value])
}

fn face_contains(large: &Face, small: &Face) -> bool {
    small.iter().all(|&value| contains(large, value))
}

fn catalan(index: usize) -> usize {
    let mut values = vec![0_usize; index + 1];
    values[0] = 1;
    for n in 1..=index {
        values[n] = (0..n).map(|left| values[left] * values[n - left - 1]).sum();
    }
    values[index]
}

fn interval_triangulations(
    first: usize,
    last: usize,
    memo: &mut BTreeMap<(usize, usize), Vec<Triangulation>>,
) -> Vec<Triangulation> {
    if last <= first + 1 {
        return vec![Vec::new()];
    }
    if let Some(saved) = memo.get(&(first, last)) {
        return saved.clone();
    }
    let mut result = Vec::new();
    for pivot in first + 1..last {
        let left = interval_triangulations(first, pivot, memo);
        let right = interval_triangulations(pivot, last, memo);
        for left_tri in &left {
            for right_tri in &right {
                let mut triangulation = Vec::new();
                triangulation.extend(left_tri.iter().copied());
                triangulation.extend(right_tri.iter().copied());
                if pivot > first + 1 {
                    triangulation.push(edge(first, pivot));
                }
                if last > pivot + 1 {
                    triangulation.push(edge(pivot, last));
                }
                triangulation.sort();
                result.push(triangulation);
            }
        }
    }
    result.sort();
    result.dedup();
    memo.insert((first, last), result.clone());
    result
}

fn triangulations() -> Vec<Triangulation> {
    let result = interval_triangulations(0, N - 1, &mut BTreeMap::new());
    assert_eq!(result.len(), catalan(N - 2));
    assert!(result
        .iter()
        .all(|triangulation| triangulation.len() == N - 3));
    result
}

fn diagonals() -> Vec<Edge> {
    let mut result = Vec::new();
    for first in 0..N {
        for second in first + 1..N {
            let value = edge(first, second);
            if !boundary_edge(value) {
                result.push(value);
            }
        }
    }
    result
}

fn faces(triangulations: &[Triangulation]) -> Vec<Face> {
    let mut result = BTreeSet::new();
    for triangulation in triangulations {
        for mask in 0..1_usize << triangulation.len() {
            let face: Face = triangulation
                .iter()
                .copied()
                .enumerate()
                .filter_map(|(index, value)| ((mask >> index) & 1 == 1).then_some(value))
                .collect();
            assert!(compatible(&face));
            result.insert(face);
        }
    }
    result.into_iter().collect()
}

fn support(face: &Face, triangulations: &[Triangulation]) -> Bits {
    let mut result = Bits::EMPTY;
    for (index, triangulation) in triangulations.iter().enumerate() {
        if face_contains(triangulation, face) {
            result.insert(index);
        }
    }
    result
}

fn internal_in_region(region: &[usize], value: Edge) -> bool {
    let Some(first) = region.iter().position(|&vertex| vertex == value.0) else {
        return false;
    };
    let Some(second) = region.iter().position(|&vertex| vertex == value.1) else {
        return false;
    };
    let distance = first.abs_diff(second);
    distance != 1 && distance != region.len() - 1
}

fn regions(face: &Face) -> Vec<Vec<usize>> {
    let mut result = vec![(0..N).collect::<Vec<_>>()];
    for &diagonal in face {
        let matches: Vec<_> = result
            .iter()
            .enumerate()
            .filter_map(|(index, region)| internal_in_region(region, diagonal).then_some(index))
            .collect();
        assert_eq!(matches.len(), 1, "diagonal must split exactly one region");
        let old = result.remove(matches[0]);
        let first_position = old.iter().position(|&vertex| vertex == diagonal.0).unwrap();
        let second_position = old.iter().position(|&vertex| vertex == diagonal.1).unwrap();
        let first = first_position.min(second_position);
        let second = first_position.max(second_position);
        let left = old[first..=second].to_vec();
        let mut right = old[second..].to_vec();
        right.extend_from_slice(&old[..=first]);
        assert!(left.len() >= 3 && right.len() >= 3);
        result.push(left);
        result.push(right);
    }
    assert_eq!(result.len(), face.len() + 1);
    result.sort();
    result
}

fn region_of(face_regions: &[Vec<usize>], value: Edge) -> usize {
    let matches: Vec<_> = face_regions
        .iter()
        .enumerate()
        .filter_map(|(index, region)| internal_in_region(region, value).then_some(index))
        .collect();
    assert_eq!(
        matches.len(),
        1,
        "available diagonal must belong to one factor"
    );
    matches[0]
}

fn available(face: &Face, value: Edge) -> bool {
    !contains(face, value) && compatible(&add_edge(face, value))
}

fn object_support(constraints: &Face, support_by_face: &BTreeMap<Face, Bits>) -> Bits {
    if !compatible(constraints) {
        Bits::EMPTY
    } else {
        *support_by_face
            .get(constraints)
            .expect("every noncrossing constraint set is an associahedral face")
    }
}

fn candidate_generators(all_faces: &[Face], all_diagonals: &[Edge]) -> Vec<Generator> {
    let mut result = BTreeSet::new();
    for base in all_faces {
        let face_regions = regions(base);
        let candidates: Vec<_> = all_diagonals
            .iter()
            .copied()
            .filter(|&value| available(base, value))
            .collect();
        for first_index in 0..candidates.len() {
            for second_index in first_index + 1..candidates.len() {
                let first = candidates[first_index];
                let second = candidates[second_index];
                if !compatible(&face_union(base, &vec![first, second])) {
                    continue;
                }
                let first_physical = physical(first);
                let second_physical = physical(second);
                let family = if first_physical && second_physical {
                    Some(Family::PhysicalPhysical)
                } else {
                    let independent =
                        region_of(&face_regions, first) != region_of(&face_regions, second);
                    if !first_physical && !second_physical && independent {
                        Some(Family::ScalarScalarIndependent)
                    } else if first_physical != second_physical && independent {
                        Some(Family::ScalarPhysicalIndependent)
                    } else {
                        None
                    }
                };
                if let Some(family) = family {
                    let (first, second) =
                        if family == Family::ScalarPhysicalIndependent && physical(first) {
                            (second, first)
                        } else {
                            (first, second)
                        };
                    result.insert(Generator {
                        family,
                        base: base.clone(),
                        first,
                        second,
                    });
                }
            }
        }
    }
    result.into_iter().collect()
}

fn face_dimension(face: &Face) -> isize {
    TOP_DIMENSION - face.len() as isize
}

fn main() {
    let triangulations = triangulations();
    let all_diagonals = diagonals();
    let all_faces = faces(&triangulations);
    assert_eq!(triangulations.len(), 132);
    assert_eq!(all_diagonals.len(), 20);
    assert_eq!(
        all_diagonals
            .iter()
            .filter(|&&value| physical(value))
            .count(),
        8
    );
    assert_eq!(all_faces.len(), 903);

    let support_by_face: BTreeMap<_, _> = all_faces
        .iter()
        .cloned()
        .map(|face| {
            let vertices = support(&face, &triangulations);
            assert!(vertices.count() > 0);
            (face, vertices)
        })
        .collect();

    let face_vector: BTreeMap<_, _> = all_faces.iter().fold(BTreeMap::new(), |mut map, face| {
        *map.entry(face_dimension(face)).or_insert(0_usize) += 1;
        map
    });
    assert_eq!(
        face_vector,
        BTreeMap::from([(0, 132), (1, 330), (2, 300), (3, 120), (4, 20), (5, 1)])
    );

    // Audit every intersection in the closed face poset.  Crossing unions
    // have empty support; noncrossing unions are the categorical pullbacks.
    let mut intersection_checks = 0_usize;
    let mut empty_intersections = 0_usize;
    for first_index in 0..all_faces.len() {
        for second_index in first_index..all_faces.len() {
            let first = &all_faces[first_index];
            let second = &all_faces[second_index];
            let union = face_union(first, second);
            let expected = object_support(&union, &support_by_face);
            let actual = support_by_face[first].intersection(support_by_face[second]);
            assert_eq!(actual, expected);
            if actual == Bits::EMPTY {
                empty_intersections += 1;
            }
            intersection_checks += 1;
        }
    }
    assert_eq!(
        intersection_checks,
        all_faces.len() * (all_faces.len() + 1) / 2
    );

    let generators = candidate_generators(&all_faces, &all_diagonals);
    let family_counts = generators
        .iter()
        .fold(BTreeMap::new(), |mut map, generator| {
            *map.entry(generator.family).or_insert(0_usize) += 1;
            map
        });
    assert!(family_counts.values().all(|&count| count > 0));

    // These pairs are transverse intersection squares, but their two proper
    // faces do not cover the ambient cell in its actual triangulation-support
    // realization. They therefore cannot simply be declared covers for the
    // natural cellular/support topology.
    let mut uncovered_profiles = BTreeMap::<Family, (usize, usize, usize)>::new();
    let mut representable_descent_checks = 0_usize;
    for generator in &generators {
        let x = support_by_face[&generator.base];
        let first_face = add_edge(&generator.base, generator.first);
        let second_face = add_edge(&generator.base, generator.second);
        let both_face = add_edge(&first_face, generator.second);
        let y = support_by_face[&first_face];
        let a = support_by_face[&second_face];
        let uncovered = x.count() - y.union(a).count();
        assert!(uncovered > 0);
        uncovered_profiles
            .entry(generator.family)
            .and_modify(|profile| {
                profile.0 += 1;
                profile.1 = profile.1.min(uncovered);
                profile.2 = profile.2.max(uncovered);
            })
            .or_insert((1, uncovered, uncovered));

        // In the incidence poset, representables nevertheless satisfy the
        // square sheaf equation: the categorical join of the two codimension
        // one faces is the ambient face.  This separates subcanonicity of an
        // abstractly declared cd-topology from separatedness of the physical
        // occurrence/coefficient object.
        for represented in &all_faces {
            let hom_x = face_contains(&generator.base, represented);
            let hom_y = face_contains(&first_face, represented);
            let hom_a = face_contains(&second_face, represented);
            let hom_b = face_contains(&both_face, represented);
            assert!(!hom_y || hom_b);
            assert!(!hom_a || hom_b);
            assert_eq!(hom_x, hom_y && hom_a);
            representable_descent_checks += 1;
        }
    }

    // Even all eight physical Cut faces miss the four zero-core/contact
    // triangulations of the octagon.
    let top = support_by_face[&Vec::new()];
    let mut all_cut_support = Bits::EMPTY;
    for &cut in all_diagonals.iter().filter(|&&value| physical(value)) {
        all_cut_support = all_cut_support.union(support_by_face[&vec![cut]]);
    }
    assert_eq!(top.count(), 132);
    assert_eq!(all_cut_support.count(), 128);
    let uncovered_cut_vertices: Vec<_> = triangulations
        .iter()
        .enumerate()
        .filter(|(index, _)| !all_cut_support.contains(*index))
        .map(|(index, triangulation)| {
            assert!(triangulation.iter().all(|&value| !physical(value)));
            index
        })
        .collect();
    assert_eq!(uncovered_cut_vertices.len(), 4);
    let cut_restriction_kernel_rank = top.count() - all_cut_support.count();
    assert_eq!(cut_restriction_kernel_rank, 4);

    // Each undeformed generator is a genuine codimension-(1,1) coordinate
    // square.  This is only a dimension profile, not a density structure.
    for generator in &generators {
        let first = add_edge(&generator.base, generator.first);
        let second = add_edge(&generator.base, generator.second);
        let both = add_edge(&first, generator.second);
        let dimension = face_dimension(&generator.base);
        assert_eq!(face_dimension(&first), dimension - 1);
        assert_eq!(face_dimension(&second), dimension - 1);
        assert_eq!(face_dimension(&both), dimension - 2);
    }

    // Saturate by every available base change X_T -> X_S, namely T superset
    // S.  A pullback may be nondegenerate, degenerate because an axis is
    // already in T, or empty because T crosses an axis.
    let mut base_change_checks = 0_usize;
    let mut nondegenerate_base_changes = 0_usize;
    let mut degenerate_base_changes = 0_usize;
    let mut empty_base_changes = 0_usize;
    let mut regularity_self_intersection_checks = 0_usize;
    let mut saturated_squares = BTreeSet::new();
    for generator in &generators {
        for target in &all_faces {
            if !face_contains(target, &generator.base) {
                continue;
            }
            let first_constraints = add_edge(target, generator.first);
            let second_constraints = add_edge(target, generator.second);
            let both_constraints = add_edge(&first_constraints, generator.second);
            let x = support_by_face[target];
            let y = object_support(&first_constraints, &support_by_face);
            let a = object_support(&second_constraints, &support_by_face);
            let b = object_support(&both_constraints, &support_by_face);

            // Pullback and monomorphic-leg audit.
            assert_eq!(b, y.intersection(a));
            assert!(b.is_subset_of(y));
            assert!(b.is_subset_of(a));
            assert!(y.is_subset_of(x));
            assert!(a.is_subset_of(x));

            // With both cover legs monic, the diagonal/self-intersection
            // part of regularity reduces to these identity pullbacks.  This
            // does not assert that the pair has been declared a cover.
            assert_eq!(y.intersection(y), y);
            assert_eq!(a.intersection(a), a);
            assert_eq!(x.intersection(y), y);
            assert_eq!(x.intersection(a), a);
            regularity_self_intersection_checks += 4;

            if y == Bits::EMPTY || a == Bits::EMPTY {
                empty_base_changes += 1;
            } else if y == x || a == x {
                degenerate_base_changes += 1;
            } else {
                nondegenerate_base_changes += 1;
            }
            saturated_squares.insert((generator.family, x, y, a, b));
            base_change_checks += 1;
        }
    }

    // The dependent route carriers are not base intersections.  They are
    // retained as transfer data and excluded from the generator census.
    let pentagon = vec![edge(1, 3), edge(3, 5), edge(5, 7)];
    let square = vec![edge(0, 2), edge(0, 4), edge(0, 6)];
    let fixed_core = vec![edge(0, 3), edge(0, 5)];
    assert_eq!(support_by_face[&pentagon].count(), 5);
    assert_eq!(support_by_face[&square].count(), 4);
    assert_eq!(support_by_face[&fixed_core].count(), 8);
    assert_eq!(
        support_by_face[&pentagon].intersection(support_by_face[&square]),
        Bits::EMPTY
    );
    assert_eq!(
        support_by_face[&pentagon]
            .intersection(support_by_face[&fixed_core])
            .count(),
        1
    );
    assert_eq!(
        support_by_face[&square]
            .intersection(support_by_face[&fixed_core])
            .count(),
        1
    );
    assert!(!compatible(&face_union(&pentagon, &square)));

    println!("n=8 closed scalar-strata audit: PASS");
    println!("triangulations={}", triangulations.len());
    println!("nonempty_faces={} plus_empty=1", all_faces.len());
    println!("face_vector_by_dimension={face_vector:?}");
    println!("intersection_checks={intersection_checks} empty_intersections={empty_intersections}");
    println!("candidate_generators={}", generators.len());
    println!("candidate_family_counts={family_counts:?}");
    println!("proper_face_pair_uncovered_profiles={uncovered_profiles:?}");
    println!("abstract_poset_representable_descent_checks={representable_descent_checks} PASS");
    println!(
        "all_physical_cut_support=128/132 uncovered_zero_core_contact_vertices={uncovered_cut_vertices:?}"
    );
    println!("free_occurrence_cut_restriction_kernel_rank={cut_restriction_kernel_rank}");
    println!("base_change_checks={base_change_checks}");
    println!("saturated_square_classes={}", saturated_squares.len());
    println!(
        "base_change_types: nondegenerate={nondegenerate_base_changes} degenerate={degenerate_base_changes} empty={empty_base_changes}"
    );
    println!(
        "monomorphic_legs=PASS pullbacks=PASS typed_self_intersections={} PASS",
        regularity_self_intersection_checks
    );
    println!(
        "natural_cellular_cut_coverage=FAIL coverage_declared=false simple_cover_refinement=UNDEFINED"
    );
    println!("dimension_profile=PASS density_structure_declared=false boundedness=UNDEFINED");
    println!(
        "dependent_route: P_vertices=5 S_vertices=4 K_Q_vertices=8 P_cap_S=0 P_cap_K_Q=1 S_cap_K_Q=1 classification=TRANSFER_NOT_CDH"
    );
}
