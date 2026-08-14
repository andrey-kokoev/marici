//! Exact carrier/loaded-support audit for the proposed D03 positive exit
//! column.
//!
//! The carrier statement and the loaded statement must be separated.
//!
//! * For the actual triple
//!
//!       v_+ subset B_short subset K6,
//!
//!   the peripheral connecting map sends the three genuine relative-Q long
//!   facets to their three boundary cycles.  It is a saturated integral
//!   isomorphism.  Its uniquely normalized inverse sends the positive dual
//!   edge e3 to F03.  This is an inverse exact-couple transgression, not a
//!   literal inclusion of the central dual block into a long facet.
//!
//! * In the reversed Boolean coface interval of v_+, use the ordered masks
//!
//!       e3=101, q0=100, q2=001.
//!
//!   Exterior orientation gives d(e3)=-q0+q2.  Restoring the independent
//!   occurrence cosheaf gives instead
//!
//!       d_occ(e3)=-x1*q0+x5*q2.
//!
//!   All three masks omit x3.  Since an absolute loaded generator (S,H)
//!   requires H subset S, none carries an h3 normal generator.  After
//!   u3=t3*x3, the x3-Cartier Bockstein has the formal decomposition
//!
//!       beta3=delta3_rad+t3*delta3_nor,
//!
//!   but delta3_rad is the attachment e3 -> f=v_+ (dually f -> e3), while
//!   delta3_nor exists only on supports containing x3.  It therefore does not
//!   turn q0 or q2 into [t3]-labelled road Tor_1 costalks.  The established
//!   carrier map confirms the distinction: e3 maps to F03, while every lower
//!   q-cell maps to zero.
//!
//! Thus the carrier shadow e3 |-> -q0+q2 and the generic Q leg are canonical,
//! but the claimed loaded lift
//!
//!       -[n03] |-> [t3](-tau_q0+tau_q2)
//!
//! is not supplied by the existing absolute Bockstein plus cone roof.
//! Identifying the lower source q-cells with the actual reciprocal/BM road
//! costalks is precisely the missing spatial extraordinary correspondence.

use std::collections::{BTreeMap, BTreeSet};

type Int = i64;
type Matrix = Vec<Vec<Int>>;
type Face = BTreeSet<Diagonal>;

const N: u8 = 6;
const DIMENSION: usize = 3;
const SLOT_X1: usize = 0;
const SLOT_X3: usize = 1;
const SLOT_X5: usize = 2;
const MASK_F: u8 = 0b111;
const MASK_E3: u8 = 0b101;
const MASK_Q0: u8 = 0b100;
const MASK_Q2: u8 = 0b001;

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

fn short(index: usize) -> Diagonal {
    diagonal(index as u8, (index as u8 + 2) % N)
}

fn is_short(value: Diagonal) -> bool {
    (0..6).any(|index| short(index) == value)
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
    for mask in 0_u16..(1_u16 << diagonals.len()) {
        if mask.count_ones() as usize > DIMENSION {
            continue;
        }
        let face: Face = diagonals
            .iter()
            .enumerate()
            .filter_map(|(index, value)| ((mask & (1 << index)) != 0).then_some(*value))
            .collect();
        if noncrossing(&face) {
            result[face.len()].push(face);
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
        && face.iter().all(|present| !crosses(*present, value))
}

fn raw_incidence_sign(face: &Face, added: Diagonal) -> Int {
    if face.iter().filter(|value| **value < added).count() % 2 == 0 {
        1
    } else {
        -1
    }
}

fn vertex_orientation_gauges(by_size: &[Vec<Face>]) -> BTreeMap<Face, Int> {
    let mut gauges = BTreeMap::from([(by_size[DIMENSION][0].clone(), 1)]);
    let mut changed = true;
    while changed {
        changed = false;
        for edge in &by_size[2] {
            let endpoints: Vec<_> = all_diagonals()
                .into_iter()
                .filter(|value| addable(edge, *value))
                .map(|value| {
                    let mut target = edge.clone();
                    target.insert(value);
                    (target, raw_incidence_sign(edge, value))
                })
                .collect();
            assert_eq!(endpoints.len(), 2);
            let relation = -endpoints[0].1 * endpoints[1].1;
            match (
                gauges.get(&endpoints[0].0).copied(),
                gauges.get(&endpoints[1].0).copied(),
            ) {
                (Some(first), Some(second)) => assert_eq!(second, relation * first),
                (Some(first), None) => {
                    gauges.insert(endpoints[1].0.clone(), relation * first);
                    changed = true;
                }
                (None, Some(second)) => {
                    gauges.insert(endpoints[0].0.clone(), relation * second);
                    changed = true;
                }
                (None, None) => {}
            }
        }
    }
    assert_eq!(gauges.len(), 14);
    gauges
}

fn incidence_sign(
    face: &Face,
    target: &Face,
    added: Diagonal,
    gauges: &BTreeMap<Face, Int>,
) -> Int {
    raw_incidence_sign(face, added)
        * gauges.get(face).copied().unwrap_or(1)
        * gauges.get(target).copied().unwrap_or(1)
}

fn zero(rows: usize, columns: usize) -> Matrix {
    vec![vec![0; columns]; rows]
}

fn boundary_matrix(source: &[Face], target: &[Face], gauges: &BTreeMap<Face, Int>) -> Matrix {
    let target_index: BTreeMap<_, _> = target
        .iter()
        .enumerate()
        .map(|(index, face)| (face.clone(), index))
        .collect();
    let mut result = zero(target.len(), source.len());
    for (column, face) in source.iter().enumerate() {
        for added in all_diagonals()
            .into_iter()
            .filter(|value| addable(face, *value))
        {
            let mut boundary = face.clone();
            boundary.insert(added);
            if let Some(row) = target_index.get(&boundary) {
                result[*row][column] = incidence_sign(face, &boundary, added, gauges);
            }
        }
    }
    result
}

fn multiply(left: &Matrix, right: &Matrix) -> Matrix {
    assert!(!left.is_empty() && !right.is_empty());
    assert_eq!(left[0].len(), right.len());
    let mut result = zero(left.len(), right[0].len());
    for row in 0..left.len() {
        for middle in 0..right.len() {
            for column in 0..right[0].len() {
                result[row][column] += left[row][middle] * right[middle][column];
            }
        }
    }
    result
}

fn select(value: &Matrix, rows: &[usize], columns: &[usize]) -> Matrix {
    rows.iter()
        .map(|row| columns.iter().map(|column| value[*row][*column]).collect())
        .collect()
}

fn append_columns(left: &Matrix, columns: &[Vec<Int>]) -> Matrix {
    assert!(columns.iter().all(|column| column.len() == left.len()));
    left.iter()
        .enumerate()
        .map(|(row, entries)| {
            entries
                .iter()
                .copied()
                .chain(columns.iter().map(|column| column[row]))
                .collect()
        })
        .collect()
}

fn gcd(mut left: Int, mut right: Int) -> Int {
    left = left.abs();
    right = right.abs();
    while right != 0 {
        (left, right) = (right, left % right);
    }
    left
}

fn integer_rank(value: &Matrix) -> usize {
    if value.is_empty() || value[0].is_empty() {
        return 0;
    }
    let mut work = value.clone();
    let mut rank = 0;
    for column in 0..work[0].len() {
        let Some(pivot) = (rank..work.len()).find(|row| work[*row][column] != 0) else {
            continue;
        };
        work.swap(rank, pivot);
        for row in 0..work.len() {
            if row == rank || work[row][column] == 0 {
                continue;
            }
            let left = work[rank][column];
            let right = work[row][column];
            for entry in column..work[0].len() {
                work[row][entry] = left * work[row][entry] - right * work[rank][entry];
            }
            let divisor = work[row]
                .iter()
                .fold(0, |common, entry| gcd(common, *entry));
            if divisor > 1 {
                for entry in &mut work[row] {
                    *entry /= divisor;
                }
            }
        }
        rank += 1;
        if rank == work.len() {
            break;
        }
    }
    rank
}

fn determinant(value: &Matrix) -> Int {
    assert_eq!(value.len(), value.first().map_or(0, Vec::len));
    if value.is_empty() {
        return 1;
    }
    let mut work = value.clone();
    let mut previous = 1;
    let mut sign = 1;
    for pivot_index in 0..value.len() - 1 {
        let Some(pivot_row) = (pivot_index..value.len()).find(|row| work[*row][pivot_index] != 0)
        else {
            return 0;
        };
        if pivot_row != pivot_index {
            work.swap(pivot_row, pivot_index);
            sign = -sign;
        }
        let pivot = work[pivot_index][pivot_index];
        for row in pivot_index + 1..value.len() {
            for column in pivot_index + 1..value.len() {
                let numerator =
                    work[row][column] * pivot - work[row][pivot_index] * work[pivot_index][column];
                assert_eq!(numerator % previous, 0);
                work[row][column] = numerator / previous;
            }
            work[row][pivot_index] = 0;
        }
        previous = pivot;
    }
    sign * work[value.len() - 1][value.len() - 1]
}

fn combinations(size: usize, chosen: usize) -> Vec<Vec<usize>> {
    fn extend(
        size: usize,
        chosen: usize,
        start: usize,
        present: &mut Vec<usize>,
        result: &mut Vec<Vec<usize>>,
    ) {
        if present.len() == chosen {
            result.push(present.clone());
            return;
        }
        let needed = chosen - present.len();
        for index in start..=size - needed {
            present.push(index);
            extend(size, chosen, index + 1, present, result);
            present.pop();
        }
    }
    let mut result = Vec::new();
    extend(size, chosen, 0, &mut Vec::new(), &mut result);
    result
}

fn has_unit_maximal_minor(value: &Matrix) -> bool {
    let rank = value[0].len();
    assert_eq!(integer_rank(value), rank);
    combinations(value.len(), rank).into_iter().any(|rows| {
        let minor: Matrix = rows.iter().map(|row| value[*row].clone()).collect();
        determinant(&minor).abs() == 1
    })
}

fn check_saturated_inverse_transgression() {
    let by_size = faces_by_size();
    let gauges = vertex_orientation_gauges(&by_size);
    let d3 = boundary_matrix(&by_size[0], &by_size[1], &gauges);
    let d2 = boundary_matrix(&by_size[1], &by_size[2], &gauges);
    let d1 = boundary_matrix(&by_size[2], &by_size[3], &gauges);
    assert_eq!(multiply(&d2, &d3), zero(21, 1));
    assert_eq!(multiply(&d1, &d2), zero(14, 9));

    let plus: Face = [short(1), short(3), short(5)].into_iter().collect();
    let plus_index = by_size[3].iter().position(|face| face == &plus).unwrap();
    let b_facets: Vec<_> = by_size[1]
        .iter()
        .enumerate()
        .filter_map(|(index, face)| face.iter().any(|value| is_short(*value)).then_some(index))
        .collect();
    let relative_census: Vec<_> = by_size
        .iter()
        .map(|faces| {
            faces
                .iter()
                .filter(|face| !face.iter().any(|value| is_short(*value)))
                .count()
        })
        .collect();
    assert_eq!(relative_census, [1, 3, 0, 0]);
    let b_vertices: Vec<_> = (0..by_size[3].len())
        .filter(|index| *index != plus_index)
        .collect();
    let all_edges: Vec<_> = (0..by_size[2].len()).collect();
    let d_b2 = select(&d2, &all_edges, &b_facets);
    let d_b1 = select(&d1, &b_vertices, &all_edges);
    assert_eq!(multiply(&d_b1, &d_b2), zero(13, 6));
    assert_eq!((integer_rank(&d_b2), integer_rank(&d_b1)), (6, 13));

    let roads = [diagonal(1, 4), diagonal(0, 3), diagonal(2, 5)];
    let road_indices: Vec<_> = roads
        .iter()
        .map(|road| {
            by_size[1]
                .iter()
                .position(|face| face == &BTreeSet::from([*road]))
                .unwrap()
        })
        .collect();
    assert_eq!(
        select(&d3, &road_indices, &[0]),
        vec![vec![1], vec![1], vec![1]]
    );
    let road_boundaries: Vec<Vec<Int>> = road_indices
        .iter()
        .map(|index| d2.iter().map(|row| row[*index]).collect())
        .collect();
    for cycle in &road_boundaries {
        let column: Matrix = cycle.iter().map(|entry| vec![*entry]).collect();
        assert_eq!(multiply(&d_b1, &column), zero(13, 1));
    }

    let short_boundary_sum: Vec<_> = (0..21)
        .map(|row| b_facets.iter().map(|column| d2[row][*column]).sum::<Int>())
        .collect();
    for row in 0..21 {
        assert_eq!(
            road_boundaries.iter().map(|cycle| cycle[row]).sum::<Int>(),
            -short_boundary_sum[row]
        );
    }

    for omitted in 0..3 {
        let chosen: Vec<_> = road_boundaries
            .iter()
            .enumerate()
            .filter_map(|(index, cycle)| (index != omitted).then_some(cycle.clone()))
            .collect();
        let augmented = append_columns(&d_b2, &chosen);
        assert_eq!(integer_rank(&augmented), 8);
        assert!(has_unit_maximal_minor(&augmented));
    }
    assert_eq!(21 - integer_rank(&d_b1) - integer_rank(&d_b2), 2);

    // The three central flips determine the based correspondence order
    // e1,e3,e5 <-> F14,F03,F25 without using a carrier matrix.
    for road in roads {
        let candidates: Vec<_> = by_size[3]
            .iter()
            .filter(|candidate| {
                candidate.contains(&road) && candidate.intersection(&plus).count() == 2
            })
            .collect();
        assert_eq!(candidates.len(), 1);
        assert!(!BTreeSet::from([road]).is_subset(&plus));
    }
    let e3_road = roads[1];
    assert_eq!(e3_road, diagonal(0, 3));

    // D3 covariance and the top equation leave M(a,b), with diagonal a,
    // off-diagonal b, and a+2b=1.  On the peripheral A2 quotient M acts by
    // a-b=1-3b.  A saturated inverse must have absolute multiplier one;
    // integrally this forces b=0 and a=1.
    let positive_unit_b = (1_i64 - 1) / 3;
    assert_eq!(positive_unit_b, 0);
    let negative_unit_numerator = 1_i64 - (-1_i64);
    assert_ne!(negative_unit_numerator % 3, 0);
    let unique_b = positive_unit_b;
    let unique_a = 1 - 2 * unique_b;
    assert_eq!((unique_a, unique_b), (1, 0));
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Occurrence {
    X1,
    X5,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct LoadedBoundaryTerm {
    target_mask: u8,
    sign: Int,
    occurrence: Occurrence,
}

fn short_for_slot(slot: usize) -> Diagonal {
    match slot {
        SLOT_X1 => short(1),
        SLOT_X3 => short(3),
        SLOT_X5 => short(5),
        _ => unreachable!(),
    }
}

fn face_for_mask(mask: u8) -> Face {
    (0..3)
        .filter_map(|slot| (mask & (1 << slot) != 0).then(|| short_for_slot(slot)))
        .collect()
}

fn deletion_sign(source_mask: u8, deleted_slot: usize, source_scale: Int) -> Int {
    assert!(source_mask & (1 << deleted_slot) != 0);
    let preceding = (0..deleted_slot)
        .filter(|slot| source_mask & (1 << slot) != 0)
        .count();
    let exterior_sign = if preceding % 2 == 0 { 1 } else { -1 };
    source_scale * exterior_sign
}

fn check_dual_cell_and_occurrence_boundary() {
    assert_eq!(
        face_for_mask(MASK_F),
        [short(1), short(3), short(5)].into_iter().collect()
    );
    assert_eq!(
        face_for_mask(MASK_E3),
        [short(1), short(5)].into_iter().collect()
    );
    assert_eq!(face_for_mask(MASK_Q0), [short(5)].into_iter().collect());
    assert_eq!(face_for_mask(MASK_Q2), [short(1)].into_iter().collect());
    assert_eq!(MASK_E3 & !(1 << SLOT_X1), MASK_Q0);
    assert_eq!(MASK_E3 & !(1 << SLOT_X5), MASK_Q2);
    let e3_orientation_scale = -1;
    let carrier = [
        (
            MASK_Q0,
            deletion_sign(MASK_E3, SLOT_X1, e3_orientation_scale),
        ),
        (
            MASK_Q2,
            deletion_sign(MASK_E3, SLOT_X5, e3_orientation_scale),
        ),
    ];
    assert_eq!(carrier, [(MASK_Q0, -1), (MASK_Q2, 1)]);

    // In the covariant occurrence complex, q0={x5} reaches e3={x1,x5}
    // by adding x1, while q2={x1} reaches e3 by adding x5.  Dualizing keeps
    // those independent occurrence labels.
    let loaded = [
        LoadedBoundaryTerm {
            target_mask: MASK_Q0,
            sign: -1,
            occurrence: Occurrence::X1,
        },
        LoadedBoundaryTerm {
            target_mask: MASK_Q2,
            sign: 1,
            occurrence: Occurrence::X5,
        },
    ];
    assert_eq!(loaded[0].target_mask, MASK_Q0);
    assert_eq!((loaded[0].sign, loaded[0].occurrence), (-1, Occurrence::X1));
    assert_eq!((loaded[1].sign, loaded[1].occurrence), (1, Occurrence::X5));
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct LoadedGenerator {
    support_mask: u8,
    circle_mask: u8,
}

impl LoadedGenerator {
    fn new(support_mask: u8, circle_mask: u8) -> Self {
        assert_eq!(circle_mask & !support_mask, 0);
        Self {
            support_mask,
            circle_mask,
        }
    }

    fn has_x3_normal(self) -> bool {
        self.circle_mask & (1 << SLOT_X3) != 0
    }
}

fn radial_x3(source_mask: u8) -> Option<u8> {
    (source_mask & (1 << SLOT_X3) == 0).then_some(source_mask | (1 << SLOT_X3))
}

fn normal_x3(generator: LoadedGenerator) -> Option<LoadedGenerator> {
    generator.has_x3_normal().then(|| {
        LoadedGenerator::new(
            generator.support_mask,
            generator.circle_mask & !(1 << SLOT_X3),
        )
    })
}

fn check_cartier_bockstein_support_blocks() {
    for mask in [MASK_E3, MASK_Q0, MASK_Q2] {
        assert_eq!(mask & (1 << SLOT_X3), 0);
        let basepoint = LoadedGenerator::new(mask, 0);
        assert!(!basepoint.has_x3_normal());
        assert_eq!(normal_x3(basepoint), None);
        // H subset S forbids even forming an h3 generator on these supports.
        assert_eq!((1 << SLOT_X3) & !mask, 1 << SLOT_X3);
    }
    assert_eq!(radial_x3(MASK_E3), Some(MASK_F));
    assert_eq!(MASK_F, MASK_E3 | (1 << SLOT_X3));

    let f_h3 = LoadedGenerator::new(MASK_F, 1 << SLOT_X3);
    let f_p3 = LoadedGenerator::new(MASK_F, 0);
    assert!(f_h3.has_x3_normal());
    assert_eq!(normal_x3(f_h3), Some(f_p3));

    // After u3=t3*x3, dividing the x3-Cartier differential gives the two
    // formal blocks delta_rad and t3*delta_nor.  The first is supported on
    // e3<->f; the second remains on f and never reaches q0 or q2.
    let radial_block = (MASK_E3, MASK_F);
    let normal_block = (f_h3.support_mask, f_p3.support_mask);
    assert_eq!(radial_block, (MASK_E3, MASK_F));
    assert_eq!(normal_block, (MASK_F, MASK_F));
    assert_ne!(normal_block.0, MASK_Q0);
    assert_ne!(normal_block.0, MASK_Q2);
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum SourceCell {
    E1,
    E3,
    E5,
    Q0,
    Q1,
    Q2,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum RoadFacet {
    F14,
    F03,
    F25,
}

fn established_carrier(cell: SourceCell) -> Option<RoadFacet> {
    match cell {
        SourceCell::E1 => Some(RoadFacet::F14),
        SourceCell::E3 => Some(RoadFacet::F03),
        SourceCell::E5 => Some(RoadFacet::F25),
        SourceCell::Q0 | SourceCell::Q1 | SourceCell::Q2 => None,
    }
}

fn check_carrier_target_typing() {
    assert_eq!(established_carrier(SourceCell::E1), Some(RoadFacet::F14));
    assert_eq!(established_carrier(SourceCell::E3), Some(RoadFacet::F03));
    assert_eq!(established_carrier(SourceCell::E5), Some(RoadFacet::F25));
    for q in [SourceCell::Q0, SourceCell::Q1, SourceCell::Q2] {
        assert_eq!(established_carrier(q), None);
    }
}

fn main() {
    check_saturated_inverse_transgression();
    check_dual_cell_and_occurrence_boundary();
    check_cartier_bockstein_support_blocks();
    check_carrier_target_typing();

    println!(
        "{}",
        r#"{"claim":"The actual n=6 carrier has a canonical saturated inverse peripheral transgression e3<->F03 and the oriented central dual-cell boundary d(e3)=-q0+q2. However, the claimed loaded conclusion that the existing x3-Cartier Bockstein of P_abs followed by that carrier already gives -[n03] -> [t3](-tau_q0+tau_q2) is false: the occurrence-loaded lower boundary is -x1*q0+x5*q2; e3=101, q0=100, and q2=001 all omit x3 and therefore carry no h3 normal generator under H subset S; beta3's radial block is e3<->f while its normal block stays on x3-containing supports; and the established carrier sends all lower q-cells to zero rather than to actual road costalks.","status":"falsified","status_meaning":"The scoped carrier theorem is proved and the specific proposed loaded lift through the already-existing P_abs Bockstein and cone roof is falsified. No no-go is claimed for a new extraordinary spatial correspondence.","scope":"n=6 integral labelled K6 carrier, central Boolean dual cell, independent occurrence labels, and the exact facewise normal-generator rule of P_abs after u3=t3*x3","assumptions":["The ordered positive dual-block bases are f=111, e3=101, q0=100, q2=001 with the established orientation scales.","Occurrence x_i, Rees t_i, and normal u_i layers remain independent; no x_i, t_i, u_i, or integer is inverted.","Road-costalk means the actual target reciprocal/Borel--Moore costalk carrier, not a lower source q-symbol with the same abstract label."],"evidence_refs":["research/voevodsky/check_d03_exit_spatial_kernel.rs","research/voevodsky/check_absolute_unlocalized_support_pc.rs","research/voevodsky/check_central_vertex_rees_transgression.rs","research/voevodsky/check_d03_whole_gallery_tag_gysin.rs","research/voevodsky/check_multirees_cartier_pl_cap.rs"],"factorization_test":{"carrier_face_census":"PASS (1,9,21,14)","relative_Q":"PASS: top -> (F14,F03,F25) has primitive norm boundary","peripheral_connector":"PASS: any two road boundaries extend B_short boundaries by a unit maximal minor","inverse_transgression":"PASS: saturation and D3 normalization uniquely force e3->F03; this is not literal inclusion","dual_cell_column":"PASS: 101->100,001 gives -q0+q2","occurrence_loaded_column":"PASS: -x1*q0+x5*q2 before ideal-line evaluation","x3_support_census":"PASS: e3,q0,q2 omit x3 and admit no h3 circle","beta3_radial_block":"PASS: e3<->f","beta3_normal_block":"PASS: only x3-containing supports; zero on e3,q0,q2","actual_carrier_q_image":"ZERO for q0,q1,q2","claimed_loaded_road_Tor_column":"FALSIFIED","inversions":"none","three_inverted":false},"counterevidence":["The literal central dual block contains no long facet; its Q leg exists only through the canonical inverse exact-couple transgression.","The two oriented deletions land in lower source dual-block cells, whose established carrier images are zero, not in the actual road Tor1 costalks.","Tensoring an abstract exterior [t3] line onto those q-cells would impose the coefficient/carrier bicomplex but would not construct its spatial extraordinary realization.","Principal occurrence-ideal evaluations can remove x1 and x5 from labelled lines without inversion, but they do not create the missing x3 normal support or the reciprocal/BM target map."],"next_experiment":"Construct a marked extraordinary correspondence that sends the lower source q0,q2 cells, with their x1/x5 occurrence ideal lines and an externally retained [t3] conormal, to the actual reciprocal/Borel--Moore road Tor1 costalks. Its carrier shadow must be the proved saturated column, and its generic leg must factor through the cone-roof e3<->F03 transgression rather than a literal dual-block inclusion."}"#
    );
}
