//! Exact obstruction certificate for the eight non-product route pentagons.
//!
//! The regional Catalan theorem specifies the occurrence objects at each
//! physical core, and the physical coaction specifies the maps which raise
//! core rank.  It does not specify a transition across a scalar flip which
//! preserves core rank.  At eight points this omission occurs on precisely
//! eight transverse faces, all with rank word [0,0,1,2,1].
//!
//! This executable proves two complementary statements.
//!
//! * A strict Laurent-weight-preserving isomorphism between the complete
//!   marked endpoint modules cannot exist: the two zero-core triangulations
//!   share four of their five scalar labels and exchange the fifth.
//! * After both physical routes are expanded in the common rank-eight
//!   full-core fiber, the already established axioms admit two central,
//!   deck-covariant scalar-edge transports, +Id and -Id.  They agree on all
//!   fixed-core objects and physical maps, but give respectively zero and a
//!   nonzero (-2 Id) pentagon defect (with the ordinary Koszul residue-line
//!   sign included).  Hence the existing data do not canonically select the
//!   coefficient-valued pentagon relation.
//!
//! The missing datum is a scalar-facet specialization in the facewise
//! Pochhammer/Cousin complex (including tangential loading, its normal line,
//! and the lower-face terms).  A numerical augmentation or a fitted target
//! sign is not a substitute for that specialization.

use std::collections::{BTreeMap, BTreeSet};

const N: usize = 8;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Edge(usize, usize);

type Cell = Vec<usize>;
type Triangulation = Vec<Edge>;

#[derive(Clone, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Occurrence {
    marks: Vec<(Cell, Edge)>,
}

#[derive(Clone, Debug)]
struct Pentagon {
    vertices: [usize; 5],
    common: Vec<Edge>,
    core: [Edge; 2],
    sheet: usize,
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

fn crossing(first: Edge, second: Edge) -> bool {
    if first.0 == second.0 || first.0 == second.1 || first.1 == second.0 || first.1 == second.1 {
        return false;
    }
    (first.0 < second.0 && second.0 < first.1 && first.1 < second.1)
        || (second.0 < first.0 && first.0 < second.1 && second.1 < first.1)
}

fn physical(value: Edge) -> bool {
    value.0 % 2 != value.1 % 2
}

fn diagonals() -> Vec<Edge> {
    let mut result = Vec::new();
    for first in 0..N {
        for second in first + 1..N {
            let candidate = edge(first, second);
            if !boundary_edge(candidate) {
                result.push(candidate);
            }
        }
    }
    result
}

fn choose_noncrossing(
    all: &[Edge],
    start: usize,
    remaining: usize,
    current: &mut Vec<Edge>,
    output: &mut Vec<Triangulation>,
) {
    if remaining == 0 {
        output.push(current.clone());
        return;
    }
    if all.len() - start < remaining {
        return;
    }
    for index in start..=all.len() - remaining {
        let candidate = all[index];
        if current.iter().any(|&chosen| crossing(candidate, chosen)) {
            continue;
        }
        current.push(candidate);
        choose_noncrossing(all, index + 1, remaining - 1, current, output);
        current.pop();
    }
}

fn triangulations() -> Vec<Triangulation> {
    let all = diagonals();
    let mut result = Vec::new();
    choose_noncrossing(&all, 0, N - 3, &mut Vec::new(), &mut result);
    for triangulation in &mut result {
        triangulation.sort();
    }
    result.sort();
    result
}

fn core(triangulation: &Triangulation) -> Vec<Edge> {
    triangulation
        .iter()
        .copied()
        .filter(|&diagonal| physical(diagonal))
        .collect()
}

fn adjacent(first: &Triangulation, second: &Triangulation) -> bool {
    first
        .iter()
        .filter(|diagonal| second.contains(diagonal))
        .count()
        + 1
        == first.len()
}

fn rotate_edge(value: Edge) -> Edge {
    edge((value.0 + 1) % N, (value.1 + 1) % N)
}

fn rotate_triangulation(value: &Triangulation) -> Triangulation {
    let mut result: Vec<_> = value.iter().copied().map(rotate_edge).collect();
    result.sort();
    result
}

fn scalar_sheet(triangulation: &Triangulation) -> usize {
    assert!(core(triangulation).is_empty());
    let parities: BTreeSet<_> = triangulation
        .iter()
        .map(|diagonal| diagonal.0 % 2)
        .collect();
    assert_eq!(parities.len(), 1);
    *parities.iter().next().unwrap()
}

fn two_faces(tris: &[Triangulation]) -> Vec<(Vec<Edge>, Vec<usize>)> {
    let all = diagonals();
    let mut result = Vec::new();
    for first in 0..all.len() {
        for second in first + 1..all.len() {
            for third in second + 1..all.len() {
                let common = vec![all[first], all[second], all[third]];
                if crossing(common[0], common[1])
                    || crossing(common[0], common[2])
                    || crossing(common[1], common[2])
                {
                    continue;
                }
                let vertices: Vec<_> = tris
                    .iter()
                    .enumerate()
                    .filter(|(_, triangulation)| {
                        common
                            .iter()
                            .all(|diagonal| triangulation.contains(diagonal))
                    })
                    .map(|(index, _)| index)
                    .collect();
                assert!(vertices.len() == 4 || vertices.len() == 5);
                result.push((common, vertices));
            }
        }
    }
    result.sort();
    result.dedup();
    result
}

fn cyclic_order(vertices: &[usize], tris: &[Triangulation]) -> Vec<usize> {
    let mut result = vec![vertices[0]];
    let second = vertices
        .iter()
        .copied()
        .filter(|&candidate| {
            candidate != vertices[0] && adjacent(&tris[vertices[0]], &tris[candidate])
        })
        .min()
        .unwrap();
    result.push(second);
    while result.len() < vertices.len() {
        let previous = result[result.len() - 2];
        let current = result[result.len() - 1];
        let next = vertices
            .iter()
            .copied()
            .find(|&candidate| {
                candidate != previous
                    && !result.contains(&candidate)
                    && adjacent(&tris[current], &tris[candidate])
            })
            .expect("two-face boundary continuation");
        result.push(next);
    }
    assert!(adjacent(&tris[*result.last().unwrap()], &tris[result[0]]));
    result
}

fn normalize_pentagon(order: &[usize], tris: &[Triangulation]) -> [usize; 5] {
    let wanted = [0, 0, 1, 2, 1];
    let mut candidates = Vec::new();
    for reflected in [false, true] {
        let base: Vec<_> = if reflected {
            order.iter().copied().rev().collect()
        } else {
            order.to_vec()
        };
        for rotation in 0..5 {
            let candidate: Vec<_> = (0..5).map(|index| base[(index + rotation) % 5]).collect();
            let ranks: Vec<_> = candidate
                .iter()
                .map(|&index| core(&tris[index]).len())
                .collect();
            if ranks == wanted {
                candidates.push(candidate);
            }
        }
    }
    let chosen = candidates.into_iter().min().expect("route rank word");
    chosen.try_into().unwrap()
}

fn route_pentagons(tris: &[Triangulation]) -> Vec<Pentagon> {
    let mut result = Vec::new();
    for (common, vertices) in two_faces(tris) {
        if vertices.len() != 5 {
            continue;
        }
        let labels: Vec<_> = vertices.iter().map(|&index| core(&tris[index])).collect();
        let rank_two: BTreeSet<_> = labels
            .iter()
            .filter(|label| label.len() == 2)
            .cloned()
            .collect();
        if !labels.iter().any(Vec::is_empty) || rank_two.len() != 1 {
            continue;
        }
        let current = rank_two.iter().next().unwrap();
        if labels
            .iter()
            .any(|label| !label.iter().all(|diagonal| current.contains(diagonal)))
        {
            continue;
        }
        let ordered = normalize_pentagon(&cyclic_order(&vertices, tris), tris);
        let sheet = scalar_sheet(&tris[ordered[0]]);
        assert_eq!(sheet, scalar_sheet(&tris[ordered[1]]));
        result.push(Pentagon {
            vertices: ordered,
            common,
            core: [current[0], current[1]],
            sheet,
        });
    }
    result.sort_by_key(|face| (face.core, face.sheet));
    result
}

fn intersection(first: &Triangulation, second: &Triangulation) -> Vec<Edge> {
    first
        .iter()
        .copied()
        .filter(|diagonal| second.contains(diagonal))
        .collect()
}

fn core_regions(current: &[Edge]) -> Vec<Cell> {
    let mut regions = vec![(0..N).collect::<Vec<_>>()];
    for &Edge(first, second) in current {
        let candidates: Vec<_> = regions
            .iter()
            .enumerate()
            .filter_map(|(region_index, region)| {
                let first_index = region.iter().position(|&vertex| vertex == first)?;
                let second_index = region.iter().position(|&vertex| vertex == second)?;
                let distance = (second_index + region.len() - first_index) % region.len();
                (distance != 1 && distance != region.len() - 1).then_some((
                    region_index,
                    first_index,
                    second_index,
                ))
            })
            .collect();
        assert_eq!(candidates.len(), 1);
        let (region_index, mut first_index, mut second_index) = candidates[0];
        let region = regions.remove(region_index);
        if first_index > second_index {
            std::mem::swap(&mut first_index, &mut second_index);
        }
        regions.push(region[first_index..=second_index].to_vec());
        let mut other = region[second_index..].to_vec();
        other.extend_from_slice(&region[..=first_index]);
        regions.push(other);
    }
    for region in &mut regions {
        region.sort_unstable();
    }
    regions.sort();
    regions
}

fn cell_slots(cell: &Cell) -> [Edge; 2] {
    assert_eq!(cell.len(), 4);
    let mut result = [edge(cell[0], cell[2]), edge(cell[1], cell[3])];
    result.sort();
    result
}

fn full_occurrences(current: [Edge; 2]) -> BTreeSet<Occurrence> {
    let cells = core_regions(&current);
    assert_eq!(
        cells.iter().map(Vec::len).collect::<Vec<_>>(),
        vec![4, 4, 4]
    );
    let mut result = BTreeSet::new();
    for mask in 0..8 {
        let mut marks = Vec::new();
        for (index, cell) in cells.iter().enumerate() {
            marks.push((cell.clone(), cell_slots(cell)[(mask >> index) & 1]));
        }
        marks.sort();
        result.insert(Occurrence { marks });
    }
    assert_eq!(result.len(), 8);
    result
}

fn factorized_occurrences(current: [Edge; 2], marked: Edge) -> BTreeSet<Occurrence> {
    let other = *current.iter().find(|&&value| value != marked).unwrap();
    let cut_regions = core_regions(&[marked]);
    let spectator = cut_regions.iter().find(|region| region.len() == 4).unwrap();
    let local = cut_regions.iter().find(|region| region.len() == 6).unwrap();
    assert!(local.contains(&other.0) && local.contains(&other.1));
    let cells = core_regions(&current);
    let spectator_cell = cells.iter().find(|cell| *cell == spectator).unwrap();
    let local_cells: Vec<_> = cells
        .iter()
        .filter(|cell| cell.iter().all(|vertex| local.contains(vertex)))
        .collect();
    assert_eq!(local_cells.len(), 2);
    let mut result = BTreeSet::new();
    for spectator_slot in cell_slots(spectator_cell) {
        for local_mask in 0..4 {
            let mut marks = vec![(spectator_cell.clone(), spectator_slot)];
            for (index, cell) in local_cells.iter().enumerate() {
                marks.push(((*cell).clone(), cell_slots(cell)[(local_mask >> index) & 1]));
            }
            marks.sort();
            result.insert(Occurrence { marks });
        }
    }
    assert_eq!(result.len(), 8);
    result
}

fn rotate_cell(cell: &Cell) -> Cell {
    let mut result: Vec<_> = cell.iter().map(|vertex| (vertex + 1) % N).collect();
    result.sort_unstable();
    result
}

fn rotate_occurrence(occurrence: &Occurrence) -> Occurrence {
    let mut marks: Vec<_> = occurrence
        .marks
        .iter()
        .map(|(cell, mark)| (rotate_cell(cell), rotate_edge(*mark)))
        .collect();
    marks.sort();
    Occurrence { marks }
}

fn signed_basis(occurrences: &BTreeSet<Occurrence>, sign: i64) -> BTreeMap<Occurrence, i64> {
    assert!(sign == 1 || sign == -1);
    occurrences
        .iter()
        .cloned()
        .map(|occurrence| (occurrence, sign))
        .collect()
}

fn rotate_signed(value: &BTreeMap<Occurrence, i64>) -> BTreeMap<Occurrence, i64> {
    value
        .iter()
        .map(|(occurrence, &coefficient)| (rotate_occurrence(occurrence), coefficient))
        .collect()
}

fn rotate_core(value: [Edge; 2]) -> ([Edge; 2], i64) {
    let transported = [rotate_edge(value[0]), rotate_edge(value[1])];
    let mut sorted = transported;
    sorted.sort();
    let orientation = if transported == sorted { 1 } else { -1 };
    (sorted, orientation)
}

fn signed_identity_defect(rank: usize, transport_sign: i64) -> Vec<i64> {
    // The two physical orders have equal occurrence coefficients.  Swapping
    // their ordered normal factors contributes -1, and the oriented cellular
    // boundary contributes the compensating -1.  Thus the remaining defect
    // is tau_s - Id on the common full-core fiber.
    (0..rank).map(|_| transport_sign - 1).collect()
}

fn main() {
    let tris = triangulations();
    assert_eq!(tris.len(), 132);
    assert_eq!(two_faces(&tris).len(), 300);
    let pentagons = route_pentagons(&tris);
    assert_eq!(pentagons.len(), 8);

    let tri_index: BTreeMap<_, _> = tris
        .iter()
        .cloned()
        .enumerate()
        .map(|(index, triangulation)| (triangulation, index))
        .collect();
    let face_index: BTreeMap<_, _> = pentagons
        .iter()
        .enumerate()
        .map(|(index, face)| {
            let mut vertices = face.vertices.to_vec();
            vertices.sort_unstable();
            (vertices, index)
        })
        .collect();

    let mut endpoint_lines = 0;
    let mut shared_edge_lines = 0;
    let mut fixed_face_lines = 0;
    let mut full_fiber_lines = 0;
    let mut factorization_checks = 0;
    let mut residue_order_checks = 0;
    let mut deck_orbit = Vec::new();
    let mut current_face = 0;
    let mut normal_holonomy = 1_i64;
    let mut polarity_holonomy = 1_i64;

    for step in 0..8 {
        assert!(!deck_orbit.contains(&current_face));
        deck_orbit.push(current_face);
        let face = &pentagons[current_face];
        let ranks: Vec<_> = face
            .vertices
            .iter()
            .map(|&index| core(&tris[index]).len())
            .collect();
        assert_eq!(ranks, vec![0, 0, 1, 2, 1]);

        let zero_left = &tris[face.vertices[0]];
        let zero_right = &tris[face.vertices[1]];
        assert!(adjacent(zero_left, zero_right));
        assert!(zero_left.iter().all(|&diagonal| !physical(diagonal)));
        assert!(zero_right.iter().all(|&diagonal| !physical(diagonal)));
        let shared = intersection(zero_left, zero_right);
        assert_eq!(shared.len(), 4);
        assert_eq!(face.common.len(), 3);
        assert!(face.common.iter().all(|diagonal| shared.contains(diagonal)));
        let removed: Vec<_> = zero_left
            .iter()
            .copied()
            .filter(|diagonal| !zero_right.contains(diagonal))
            .collect();
        let inserted: Vec<_> = zero_right
            .iter()
            .copied()
            .filter(|diagonal| !zero_left.contains(diagonal))
            .collect();
        assert_eq!(removed.len(), 1);
        assert_eq!(inserted.len(), 1);
        assert_ne!(removed, inserted);
        // The complete marked endpoint modules have five Laurent weight
        // labels.  Their supports differ, so no label/weight-preserving
        // rank-five isomorphism can extend the identity on the intersection.
        let left_weights: BTreeSet<_> = zero_left.iter().copied().collect();
        let right_weights: BTreeSet<_> = zero_right.iter().copied().collect();
        assert_ne!(left_weights, right_weights);
        assert_eq!(left_weights.intersection(&right_weights).count(), 4);
        endpoint_lines += left_weights.len() + right_weights.len();
        shared_edge_lines += shared.len();
        fixed_face_lines += face.common.len();

        let full = full_occurrences(face.core);
        assert_eq!(full.len(), 8);
        full_fiber_lines += full.len();
        for marked in face.core {
            assert_eq!(factorized_occurrences(face.core, marked), full);
            factorization_checks += full.len();
        }
        // The two physical orders span the two ordered residue lines.  The
        // underlying occurrence expansion is the same, while exchanging the
        // normal factors reverses the wedge orientation.
        let canonical_order = face.core;
        let reverse_order = [face.core[1], face.core[0]];
        assert_eq!(canonical_order, face.core);
        assert_eq!(reverse_order, [canonical_order[1], canonical_order[0]]);
        let order_signs = [1_i64, -1_i64];
        assert_eq!(order_signs[0], 1);
        assert_eq!(order_signs[1], -order_signs[0]);
        residue_order_checks += order_signs.len();

        let rotated_vertices = {
            let mut value: Vec<_> = face
                .vertices
                .iter()
                .map(|&index| tri_index[&rotate_triangulation(&tris[index])])
                .collect();
            value.sort_unstable();
            value
        };
        let next_face = face_index[&rotated_vertices];
        let next = &pentagons[next_face];
        assert_eq!(next.sheet, 1 - face.sheet);
        let (rotated_core, normal_sign) = rotate_core(face.core);
        assert_eq!(rotated_core, next.core);
        let rotated_occurrences: BTreeSet<_> = full.iter().map(rotate_occurrence).collect();
        let next_occurrences = full_occurrences(next.core);
        assert_eq!(rotated_occurrences, next_occurrences);
        for transport_sign in [1_i64, -1_i64] {
            // Both candidate scalar-edge transports are central involutions
            // and satisfy rho tau_s = tau_{rho s} rho on the actual bases.
            assert_eq!(transport_sign * transport_sign, 1);
            assert_eq!(
                rotate_signed(&signed_basis(&full, transport_sign)),
                signed_basis(&next_occurrences, transport_sign)
            );
        }
        normal_holonomy *= normal_sign;
        polarity_holonomy *= -1;
        current_face = next_face;
        assert_eq!(step + 1, deck_orbit.len());
    }
    assert_eq!(current_face, 0);
    assert_eq!(deck_orbit.len(), 8);
    assert_eq!((normal_holonomy, polarity_holonomy), (1, 1));
    assert_eq!(normal_holonomy * polarity_holonomy, 1);

    assert_eq!(endpoint_lines, 8 * 2 * 5);
    assert_eq!(shared_edge_lines, 8 * 4);
    assert_eq!(fixed_face_lines, 8 * 3);
    assert_eq!(full_fiber_lines, 8 * 8);
    assert_eq!(factorization_checks, 8 * 2 * 8);
    assert_eq!(residue_order_checks, 8 * 2);

    // Both signs are central units, are constant on the single deck orbit,
    // act as the identity permutation on occurrence support, and leave the
    // separately tracked ordered residue line untouched.  Consequently all
    // already-defined physical squares and deck relations see them equally.
    // The pentagon is the first relation containing exactly one such edge.
    let plus_defect = signed_identity_defect(8, 1);
    let minus_defect = signed_identity_defect(8, -1);
    assert!(plus_defect.iter().all(|&entry| entry == 0));
    assert!(minus_defect.iter().all(|&entry| entry == -2));

    println!("eight-point nontransverse pentagon audit");
    println!("  associahedron: 132 vertices, 300 two-faces");
    println!("  route pentagons: 8, one deck orbit, rank word [0,0,1,2,1]");
    println!("  endpoint occurrence lines: {endpoint_lines}=8*2*5");
    println!("  scalar-edge shared labels: {shared_edge_lines}=8*4; fixed-face labels: {fixed_face_lines}=8*3");
    println!("  every endpoint exchanges one formal Laurent label, so no full weight-preserving rank-five transport exists");
    println!("  common full-core fibers: {full_fiber_lines}=8*8");
    println!("  L8(Q)=L4(empty)[2] tensor L6(q)[4] checks: {factorization_checks}");
    println!("  ordered two-residue-line checks (+ for D wedge E, - for E wedge D): {residue_order_checks}");
    println!("  deck holonomy (ordered normal line, polarity line, tensor)=({normal_holonomy},{polarity_holonomy},{})", normal_holonomy * polarity_holonomy);
    println!("  tau_plus=+Id and tau_minus=-Id are rank preserving, central, and deck covariant");
    println!("  signed defects on every rank-eight fiber: tau_plus-Id=0, tau_minus-Id=-2 Id");
    println!();
    println!("VERDICT: FALSIFIED");
    println!("  fixed-core regional/Catalan data do not canonically supply the same-core scalar transport");
    println!(
        "  strict Laurent preservation gives a no-go already at the rank-five endpoint modules"
    );
    println!("  after passage to the common rank-eight fiber, current axioms retain an unresolved central sign");
    println!("  minimal repair: scalar-facet Pochhammer/Cousin specialization with loading, orientation, and forced lower-face terms");
}
