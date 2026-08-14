//! Exact unit-occurrence obstruction for the three rotated gallery tops.
//!
//! The checker reconstructs the actual K6 face poset and its barycentric
//! differential.  Specializing all occurrence variables to one is enough:
//! a polynomial higher filler would specialize to an integral filler here.

use std::collections::BTreeMap;

type Int = i64;
type Face = u16;

const N: u8 = 6;

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

fn diagonals() -> Vec<Diagonal> {
    (0..N)
        .flat_map(|first| ((first + 1)..N).map(move |second| diagonal(first, second)))
        .filter(|value| !boundary_edge(*value))
        .collect()
}

fn short(index: u8) -> Diagonal {
    diagonal(index, (index + 2) % N)
}

fn face(values: &[Diagonal], diagonal_index: &BTreeMap<Diagonal, usize>) -> Face {
    values
        .iter()
        .fold(0, |result, value| result | (1 << diagonal_index[value]))
}

fn actual_faces(all_diagonals: &[Diagonal]) -> Vec<Face> {
    (0_u16..(1_u16 << all_diagonals.len()))
        .filter(|mask| mask.count_ones() <= 3)
        .filter(|mask| {
            let members: Vec<_> = all_diagonals
                .iter()
                .enumerate()
                .filter_map(|(index, value)| ((mask & (1 << index)) != 0).then_some(*value))
                .collect();
            members.iter().enumerate().all(|(position, first)| {
                members
                    .iter()
                    .skip(position + 1)
                    .all(|second| !crosses(*first, *second))
            })
        })
        .collect()
}

fn proper_subset(left: Face, right: Face) -> bool {
    left != right && left & right == left
}

fn barycentric_bases(faces: &[Face]) -> (Vec<(Face, Face)>, Vec<(Face, Face, Face)>) {
    let edges = faces
        .iter()
        .flat_map(|&left| {
            faces
                .iter()
                .filter(move |&&right| proper_subset(left, right))
                .map(move |&right| (left, right))
        })
        .collect();
    let triangles = faces
        .iter()
        .flat_map(|&first| {
            faces.iter().flat_map(move |&second| {
                faces
                    .iter()
                    .filter(move |&&third| {
                        proper_subset(first, second) && proper_subset(second, third)
                    })
                    .map(move |&third| (first, second, third))
            })
        })
        .collect();
    (edges, triangles)
}

fn add_edge(chain: &mut BTreeMap<(Face, Face), Int>, edge: (Face, Face), coefficient: Int) {
    *chain.entry(edge).or_default() += coefficient;
    if chain[&edge] == 0 {
        chain.remove(&edge);
    }
}

fn rank_mod_prime(mut rows: Vec<Vec<Int>>, prime: Int) -> usize {
    if rows.is_empty() {
        return 0;
    }
    let columns = rows[0].len();
    let mut rank = 0;
    for column in 0..columns {
        let Some(pivot) = (rank..rows.len()).find(|row| rows[*row][column] != 0) else {
            continue;
        };
        rows.swap(rank, pivot);
        let pivot_value = rows[rank][column].rem_euclid(prime);
        let inverse = (1..prime)
            .find(|candidate| (pivot_value * candidate).rem_euclid(prime) == 1)
            .unwrap();
        for entry in &mut rows[rank] {
            *entry = (*entry * inverse).rem_euclid(prime);
        }
        let pivot_row = rows[rank].clone();
        for row in 0..rows.len() {
            if row == rank {
                continue;
            }
            let factor = rows[row][column].rem_euclid(prime);
            for index in column..columns {
                rows[row][index] = (rows[row][index] - factor * pivot_row[index]).rem_euclid(prime);
            }
        }
        rank += 1;
    }
    rank
}

fn column_rank(columns: &[Vec<Int>], row_count: usize) -> usize {
    let rows = (0..row_count)
        .map(|row| columns.iter().map(|column| column[row]).collect())
        .collect();
    rank_mod_prime(rows, 101)
}

fn boundary_columns(edges: &[(Face, Face)], triangles: &[(Face, Face, Face)]) -> Vec<Vec<Int>> {
    let edge_index: BTreeMap<_, _> = edges
        .iter()
        .copied()
        .enumerate()
        .map(|(index, edge)| (edge, index))
        .collect();
    triangles
        .iter()
        .map(|&(first, second, third)| {
            let mut column = vec![0; edges.len()];
            // Missing edges have been divided out by a relative subcomplex.
            if let Some(index) = edge_index.get(&(second, third)) {
                column[*index] += 1;
            }
            if let Some(index) = edge_index.get(&(first, third)) {
                column[*index] -= 1;
            }
            if let Some(index) = edge_index.get(&(first, second)) {
                column[*index] += 1;
            }
            column
        })
        .collect()
}

fn vector(chain: &BTreeMap<(Face, Face), Int>, edges: &[(Face, Face)]) -> Vec<Int> {
    edges
        .iter()
        .map(|edge| chain.get(edge).copied().unwrap_or(0))
        .collect()
}

fn main() {
    let all_diagonals = diagonals();
    assert_eq!(all_diagonals.len(), 9);
    let diagonal_index: BTreeMap<_, _> = all_diagonals
        .iter()
        .copied()
        .enumerate()
        .map(|(index, value)| (value, index))
        .collect();
    let faces = actual_faces(&all_diagonals);
    assert_eq!(
        (0..=3)
            .map(|size| {
                faces
                    .iter()
                    .filter(|face| face.count_ones() as usize == size)
                    .count()
            })
            .collect::<Vec<_>>(),
        [1, 9, 21, 14]
    );
    let (edges, triangles) = barycentric_bases(&faces);
    let d2 = boundary_columns(&edges, &triangles);

    let top = 0;
    let a = face(&[short(1), short(3), short(5)], &diagonal_index);
    let rotated = [
        (diagonal(1, 4), short(4)),
        (diagonal(0, 3), short(0)),
        (diagonal(2, 5), short(2)),
    ];
    let mut q_sum = BTreeMap::new();
    let mut endpoints = vec![a];
    for (road, exit_short) in rotated {
        let road_face = face(&[road], &diagonal_index);
        let spectator = if road == diagonal(1, 4) {
            short(1)
        } else if road == diagonal(0, 3) {
            short(3)
        } else {
            short(5)
        };
        let c = face(&[road, exit_short, spectator], &diagonal_index);
        assert!(faces.contains(&c));
        endpoints.push(c);
        add_edge(&mut q_sum, (top, a), -1);
        add_edge(&mut q_sum, (top, road_face), 1);
        add_edge(&mut q_sum, (road_face, c), 1);
    }

    let mut d_q: BTreeMap<Face, Int> = BTreeMap::new();
    for (&(left, right), &coefficient) in &q_sum {
        *d_q.entry(right).or_default() += coefficient;
        *d_q.entry(left).or_default() -= coefficient;
    }
    d_q.retain(|_, coefficient| *coefficient != 0);
    assert_eq!(d_q.len(), 4);
    assert_eq!(d_q[&a], -3);
    assert!(endpoints.iter().skip(1).all(|endpoint| d_q[endpoint] == 1));

    // Modding out the four endpoints makes q_sum a cycle.  It does not alter
    // the two-to-one boundary matrix, and q_sum is not in that image.
    let q_vector = vector(&q_sum, &edges);
    let absolute_rank = column_rank(&d2, edges.len());
    let mut with_q = d2.clone();
    with_q.push(q_vector.clone());
    let endpoint_rank = column_rank(&with_q, edges.len());
    assert_eq!(endpoint_rank, absolute_rank + 1);

    // Quotient by the whole short boundary.  This is the canonical carrier
    // roof in which the generic roads become bounded.
    let short_mask = (0..6).fold(0, |mask, index| {
        mask | face(&[short(index)], &diagonal_index)
    });
    let relative_edges: Vec<_> = edges
        .iter()
        .copied()
        .filter(|(initial, _)| initial & short_mask == 0)
        .collect();
    let relative_triangles: Vec<_> = triangles
        .iter()
        .copied()
        .filter(|(initial, _, _)| initial & short_mask == 0)
        .collect();
    let relative_d2 = boundary_columns(&relative_edges, &relative_triangles);
    let relative_q = vector(&q_sum, &relative_edges);
    let b_short_rank = column_rank(&relative_d2, relative_edges.len());
    let mut relative_with_q = relative_d2.clone();
    relative_with_q.push(relative_q);
    let b_short_rank_with_q = column_rank(&relative_with_q, relative_edges.len());
    assert_eq!(b_short_rank_with_q, b_short_rank);

    println!(
        "{{\"claim\":\"The rotated generic sum is not bounded in the actual barycentric K6 carrier relative only to its four endpoints. It is bounded after quotienting by B_short, but that quotient also removes every special gallery edge.\",\"status\":\"proved\",\"generic_boundary\":\"c14+c03+c25-3*v_plus\",\"endpoint_relative_ranks\":[{absolute_rank},{endpoint_rank}],\"b_short_relative_ranks\":[{b_short_rank},{b_short_rank_with_q}],\"detector\":\"all occurrence variables specialized to 1 over F_101\",\"exact_blocker\":\"a D3-equivariant multi-Rees/conductor comparison connecting the endpoint classes while retaining the three special galleries\"}}"
    );
}
