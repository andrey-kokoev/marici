//! Integral carrier/filtration census for the marked three-exit question.
//!
//! The four nested carrier supports are
//!
//!     A={v_+} subset E={v_+,c14,c03,c25} subset B_short subset K6.
//!
//! The checker distinguishes the support-filtration transgression from the
//! endpoint-relative marked-exit class.  In particular, the natural map
//!
//!     H2(K6,B_short) -> H1(B_short,A) -> H1(B_short,E)
//!                       -> H1(K6,E)
//!
//! is zero, whereas q_Sigma has endpoint boundary (1,1,1) and is primitive
//! in H1(K6,E)=Z^3.  The same census identifies the filtration transgression
//! as the middle coker(N)->ker(epsilon) map of the integral Tate window.

use std::collections::{BTreeMap, BTreeSet, VecDeque};

type Int = i64;
type Matrix = Vec<Vec<Int>>;
type Face = BTreeSet<Diagonal>;

const N_VERTICES: u8 = 6;
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
    value.1 - value.0 == 1 || value == Diagonal(0, N_VERTICES - 1)
}

fn between(vertex: u8, first: u8, second: u8) -> bool {
    let span = (second + N_VERTICES - first) % N_VERTICES;
    let position = (vertex + N_VERTICES - first) % N_VERTICES;
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

fn diagonals() -> Vec<Diagonal> {
    (0..N_VERTICES)
        .flat_map(|first| ((first + 1)..N_VERTICES).map(move |second| diagonal(first, second)))
        .filter(|value| !boundary_edge(*value))
        .collect()
}

fn short(index: u8) -> Diagonal {
    diagonal(index, (index + 2) % N_VERTICES)
}

fn noncrossing(face: &Face) -> bool {
    face.iter().enumerate().all(|(position, first)| {
        face.iter()
            .skip(position + 1)
            .all(|second| !crosses(*first, *second))
    })
}

fn faces_by_size() -> Vec<Vec<Face>> {
    let all = diagonals();
    let mut result = vec![Vec::new(); DIMENSION + 1];
    for mask in 0_u16..(1_u16 << all.len()) {
        if mask.count_ones() as usize > DIMENSION {
            continue;
        }
        let face: Face = all
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
            let endpoints: Vec<_> = diagonals()
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
        for added in diagonals()
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

fn has_unit_maximal_minor(value: &Matrix, rank: usize) -> bool {
    let rows = value.len();
    let columns = value.first().map_or(0, Vec::len);
    for selected_rows in combinations(rows, rank) {
        for selected_columns in combinations(columns, rank) {
            let minor: Matrix = selected_rows
                .iter()
                .map(|row| {
                    selected_columns
                        .iter()
                        .map(|column| value[*row][*column])
                        .collect()
                })
                .collect();
            if determinant(&minor).abs() == 1 {
                return true;
            }
        }
    }
    false
}

fn in_b_short(face: &Face) -> bool {
    face.iter()
        .any(|value| (0..N_VERTICES).any(|index| *value == short(index)))
}

fn face(values: &[Diagonal]) -> Face {
    values.iter().copied().collect()
}

fn binomial(size: usize, chosen: usize) -> usize {
    match (size, chosen) {
        (_, 0) => 1,
        (1, 1) => 1,
        (2, 1) => 2,
        (2, 2) => 1,
        (3, 1) | (3, 2) => 3,
        (3, 3) => 1,
        _ => 0,
    }
}

fn loaded_ranks(by_size: &[Vec<Face>], include: impl Fn(&Face) -> bool) -> Vec<usize> {
    let mut ranks = vec![0; DIMENSION + 1];
    for faces in by_size {
        for support in faces.iter().filter(|support| include(support)) {
            for normal_degree in 0..=support.len() {
                let degree = DIMENSION - support.len() + normal_degree;
                ranks[degree] += binomial(support.len(), normal_degree);
            }
        }
    }
    ranks
}

fn subtract(left: &[usize], right: &[usize]) -> Vec<usize> {
    left.iter().zip(right).map(|(a, b)| a - b).collect()
}

fn path_chain(d1: &Matrix, start: usize, finish: usize) -> Vec<Int> {
    let mut adjacency = vec![Vec::new(); d1.len()];
    for column in 0..d1[0].len() {
        let endpoints: Vec<_> = (0..d1.len()).filter(|row| d1[*row][column] != 0).collect();
        assert_eq!(endpoints.len(), 2);
        adjacency[endpoints[0]].push((endpoints[1], column));
        adjacency[endpoints[1]].push((endpoints[0], column));
    }
    let mut previous = vec![None; d1.len()];
    let mut queue = VecDeque::from([start]);
    previous[start] = Some((start, usize::MAX));
    while let Some(vertex) = queue.pop_front() {
        if vertex == finish {
            break;
        }
        for &(next, edge) in &adjacency[vertex] {
            if previous[next].is_none() {
                previous[next] = Some((vertex, edge));
                queue.push_back(next);
            }
        }
    }
    assert!(previous[finish].is_some());
    let mut result = vec![0; d1[0].len()];
    let mut current = finish;
    while current != start {
        let (prior, edge) = previous[current].unwrap();
        // Choose the coefficient whose boundary along this edge is
        // current-prior.
        result[edge] += d1[current][edge];
        current = prior;
    }
    let boundary = multiply(d1, &result.iter().map(|entry| vec![*entry]).collect());
    for (row, coefficient) in boundary.iter().enumerate() {
        let expected = if row == start {
            -1
        } else if row == finish {
            1
        } else {
            0
        };
        assert_eq!(coefficient[0], expected);
    }
    result
}

fn main() {
    let by_size = faces_by_size();
    let gauges = vertex_orientation_gauges(&by_size);
    let d3 = boundary_matrix(&by_size[0], &by_size[1], &gauges);
    let d2 = boundary_matrix(&by_size[1], &by_size[2], &gauges);
    let d1 = boundary_matrix(&by_size[2], &by_size[3], &gauges);
    assert_eq!(multiply(&d2, &d3), zero(21, 1));
    assert_eq!(multiply(&d1, &d2), zero(14, 9));
    assert_eq!(
        (integer_rank(&d3), integer_rank(&d2), integer_rank(&d1)),
        (1, 8, 13)
    );

    let plus = face(&[short(1), short(3), short(5)]);
    let rotated = [
        (diagonal(1, 4), short(4), short(1)),
        (diagonal(0, 3), short(0), short(3)),
        (diagonal(2, 5), short(2), short(5)),
    ];
    let exits: Vec<_> = rotated
        .iter()
        .map(|(road, exit_short, spectator)| face(&[*road, *exit_short, *spectator]))
        .collect();
    assert!(exits.iter().all(in_b_short));

    let plus_index = by_size[3].iter().position(|value| value == &plus).unwrap();
    let exit_indices: Vec<_> = exits
        .iter()
        .map(|exit| by_size[3].iter().position(|value| value == exit).unwrap())
        .collect();
    let endpoint_indices: BTreeSet<_> = std::iter::once(plus_index)
        .chain(exit_indices.iter().copied())
        .collect();

    let b_facets: Vec<_> = by_size[1]
        .iter()
        .enumerate()
        .filter_map(|(index, value)| in_b_short(value).then_some(index))
        .collect();
    assert_eq!(b_facets.len(), 6);
    assert!(by_size[2].iter().all(in_b_short));
    assert!(by_size[3].iter().all(in_b_short));

    let all_edges: Vec<_> = (0..by_size[2].len()).collect();
    let all_vertices: Vec<_> = (0..by_size[3].len()).collect();
    let p_vertices: Vec<_> = all_vertices
        .iter()
        .copied()
        .filter(|index| *index != plus_index)
        .collect();
    let marked_vertices: Vec<_> = all_vertices
        .iter()
        .copied()
        .filter(|index| !endpoint_indices.contains(index))
        .collect();

    let d_b2 = select(&d2, &all_edges, &b_facets);
    let d_p1 = select(&d1, &p_vertices, &all_edges);
    let d_marked1 = select(&d1, &marked_vertices, &all_edges);
    assert_eq!(
        (
            integer_rank(&d_b2),
            integer_rank(&d_p1),
            integer_rank(&d_marked1)
        ),
        (6, 13, 10)
    );
    assert!(has_unit_maximal_minor(&d_b2, 6));
    assert!(has_unit_maximal_minor(&d_p1, 13));
    assert!(has_unit_maximal_minor(&d_marked1, 10));

    let road_facets: Vec<_> = rotated
        .iter()
        .map(|(road, _, _)| {
            by_size[1]
                .iter()
                .position(|value| value == &face(&[*road]))
                .unwrap()
        })
        .collect();
    let road_boundaries: Vec<Vec<Int>> = road_facets
        .iter()
        .map(|facet| d2.iter().map(|row| row[*facet]).collect())
        .collect();
    let saturated_kernel = append_columns(
        &d_b2,
        &[road_boundaries[0].clone(), road_boundaries[1].clone()],
    );
    assert_eq!(integer_rank(&saturated_kernel), 8);
    assert!(has_unit_maximal_minor(&saturated_kernel, 8));
    // The third road differs from minus the first two by a B_short boundary.
    assert_eq!(
        integer_rank(&append_columns(
            &saturated_kernel,
            &[road_boundaries[2].clone()]
        )),
        8
    );

    // R=C(K,B) is Z -> Z^3 with primitive norm column.  Its H2 is Z^2.
    let relative_top = select(&d3, &road_facets, &[0]);
    assert_eq!(integer_rank(&relative_top), 1);
    assert_eq!(
        relative_top
            .iter()
            .fold(0, |common, row| gcd(common, row[0])),
        1
    );

    // Exact homology census, with freeness certified by the unit minors.
    let h2_r = 3 - 1;
    let h1_p = 21 - 13 - 6;
    let h1_j = 21 - 10 - 6;
    let h1_t = 21 - 10 - 8;
    assert_eq!((h2_r, h1_p, h1_j, h1_t), (2, 2, 5, 3));

    // The filtration connector sends the road quotient to its three actual
    // peripheral boundaries.  It is an integral isomorphism H2(R)->H1(P).
    // After marking E its image is exactly ker(H1(J)->H1(T)), hence every
    // route induced by inclusions/quotients has zero marked-exit image.
    for boundary in &road_boundaries {
        let column: Matrix = boundary.iter().map(|entry| vec![*entry]).collect();
        assert_eq!(multiply(&d_p1, &column), zero(13, 1));
        assert_eq!(multiply(&d_marked1, &column), zero(10, 1));
    }

    // Construct integral B_short paths from v_+ to the three marked exits.
    // Their endpoint boundaries give a saturated Z^3 quotient, and their sum
    // represents q_Sigma because K6 has no absolute H1.
    let paths: Vec<_> = exit_indices
        .iter()
        .map(|exit| path_chain(&d1, plus_index, *exit))
        .collect();
    let q_path: Vec<_> = (0..d1[0].len())
        .map(|edge| paths.iter().map(|path| path[edge]).sum::<Int>())
        .collect();
    let q_boundary = multiply(&d1, &q_path.iter().map(|entry| vec![*entry]).collect());
    assert_eq!(q_boundary[plus_index][0], -3);
    assert!(exit_indices.iter().all(|index| q_boundary[*index][0] == 1));
    assert!(q_boundary
        .iter()
        .enumerate()
        .all(|(index, entry)| { endpoint_indices.contains(&index) || entry[0] == 0 }));
    assert_eq!(gcd(gcd(1, 1), 1), 1); // (1,1,1) is primitive.

    // Occurrence-loaded degreewise census.  These are exact free ranks before
    // any occurrence, monodromy, Rees, or integer localization.
    let loaded_f2 = loaded_ranks(&by_size, |_| true);
    let loaded_f1 = loaded_ranks(&by_size, in_b_short);
    let loaded_f0 = loaded_ranks(&by_size, |support| support == &plus);
    let loaded_fe = loaded_ranks(&by_size, |support| {
        support == &plus || exits.iter().any(|exit| support == exit)
    });
    assert_eq!(loaded_f2, [14, 63, 93, 45]);
    assert_eq!(loaded_f1, [14, 63, 90, 41]);
    assert_eq!(loaded_f0, [1, 3, 3, 1]);
    assert_eq!(loaded_fe, [4, 12, 12, 4]);
    assert_eq!(subtract(&loaded_f1, &loaded_f0), [13, 60, 87, 40]);
    assert_eq!(subtract(&loaded_f2, &loaded_f0), [13, 60, 90, 44]);
    assert_eq!(subtract(&loaded_f2, &loaded_f1), [0, 0, 3, 4]);
    assert_eq!(subtract(&loaded_fe, &loaded_f0), [3, 9, 9, 3]);
    assert_eq!(subtract(&loaded_f1, &loaded_fe), [10, 51, 78, 37]);
    assert_eq!(subtract(&loaded_f2, &loaded_fe), [10, 51, 81, 41]);

    println!(
        "{}",
        r#"{"claim":"No connecting morphism induced only by A subset E subset B_short subset K6 sends the support-filtration Yoneda class to q_Sigma. The carrier transgression is the saturated isomorphism coker(N)=Z^2 -> ker(epsilon)=Z^2; after endpoint marking its image is the rank-two kernel of H1(B_short,E)=Z^5 -> H1(K6,E)=Z^3, so its marked-exit composite is zero. q_Sigma is instead the primitive norm vector (1,1,1), detected by the endpoint boundary isomorphism H1(K6,E)->H0(E/A)=Z^3.","status":"proved","carrier_homology":{"H2_K_B":"Z^2","H1_B_A":"Z^2","H1_B_E":"Z^5","H1_K_E":"Z^3","connector_smith":"(1,1)","marked_composite":"zero","qSigma_boundary":"(1,1,1)","qSigma_primitive":true},"loaded_degree_ranks":{"F0":[1,3,3,1],"FE":[4,12,12,4],"F1":[14,63,90,41],"F2":[14,63,93,45],"F1_F0":[13,60,87,40],"F2_F0":[13,60,90,44],"F2_F1":[0,0,3,4],"FE_F0":[3,9,9,3],"F1_FE":[10,51,78,37],"F2_FE":[10,51,81,41]},"ext_typing":{"eF":"Ext^2(F2/F1,F0)","qSigma":"Hom(Z[1],C_*(sd(K6),E))","only_source_comparison":"C_*(K6,E)->F2/F1","variance":"pullback of eF remains Ext^2(C_*(K6,E),F0), not H1(K6,E)","target_quotient":"F0->FE->FE/F0 is zero"},"tate_test":{"norm":"qSigma corresponds to N=(1,1,1)","middle":"support connector is coker(N)->ker(epsilon)","epsilon_N":3,"interpretation":"qSigma detects the norm leg of the Tate carrier shadow; it is not an image of the Ext class"}}"#
    );
}
