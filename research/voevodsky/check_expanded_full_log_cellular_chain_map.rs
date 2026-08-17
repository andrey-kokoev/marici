//! Integral cellular realization of the minimally expanded full-log octahedron
//! in the literal K6 associahedral sphere. This proves a finite chain map; it
//! does not claim a proper/extraordinary six-functor kernel.

use std::collections::{BTreeMap, BTreeSet, VecDeque};

type Diagonal = (u8, u8);
type Face = BTreeSet<Diagonal>;

fn diagonal(a: u8, b: u8) -> Diagonal {
    if a < b {
        (a, b)
    } else {
        (b, a)
    }
}

fn boundary(a: u8, b: u8) -> bool {
    matches!(a.abs_diff(b), 1 | 5)
}

fn crosses((a, b): Diagonal, (c, d): Diagonal) -> bool {
    (a < c && c < b && b < d) || (c < a && a < d && d < b)
}

fn triangulations() -> Vec<Face> {
    let diagonals = (0..6)
        .flat_map(|a| ((a + 1)..6).map(move |b| (a, b)))
        .filter(|(a, b)| !boundary(*a, *b))
        .collect::<Vec<_>>();
    (0_u16..(1_u16 << diagonals.len()))
        .filter_map(|mask| {
            let chosen = diagonals
                .iter()
                .enumerate()
                .filter(|(index, _)| mask & (1 << index) != 0)
                .map(|(_, value)| *value)
                .collect::<Face>();
            (chosen.len() == 3
                && !chosen.iter().any(|left| {
                    chosen
                        .iter()
                        .any(|right| left < right && crosses(*left, *right))
                }))
            .then_some(chosen)
        })
        .collect()
}

fn short(index: usize) -> Diagonal {
    diagonal(index as u8, (index as u8 + 2) % 6)
}

fn rotate(face: &Face, turns: usize) -> Face {
    face.iter()
        .map(|(a, b)| diagonal((a + 2 * turns as u8) % 6, (b + 2 * turns as u8) % 6))
        .collect()
}

fn sector(axis: usize, sign: i8) -> Face {
    let d03 = diagonal(0, 3);
    let base = if sign > 0 {
        [d03, short(1), short(3)]
    } else {
        [d03, short(0), short(4)]
    }
    .into_iter()
    .collect();
    rotate(&base, [2, 0, 1][axis])
}

fn shortest_path(graph: &BTreeMap<Face, Vec<Face>>, source: &Face, target: &Face) -> Vec<Face> {
    let mut queue = VecDeque::from([vec![source.clone()]]);
    let mut answers = Vec::new();
    let mut best = usize::MAX;
    while let Some(path) = queue.pop_front() {
        if path.len() - 1 > best {
            continue;
        }
        let last = path.last().unwrap();
        if last == target {
            best = path.len() - 1;
            answers.push(path);
            continue;
        }
        for next in &graph[last] {
            if !path.contains(next) {
                let mut extended = path.clone();
                extended.push(next.clone());
                queue.push_back(extended);
            }
        }
    }
    let shortest = answers
        .into_iter()
        .filter(|path| path.len() - 1 == best)
        .collect::<Vec<_>>();
    assert_eq!(shortest.len(), 1);
    shortest.into_iter().next().unwrap()
}

fn edge_vector(path: &[Face], edge_index: &BTreeMap<(Face, Face), usize>, count: usize) -> Vec<i8> {
    let mut vector = vec![0_i8; count];
    for pair in path.windows(2) {
        let (key, sign) = if pair[0] < pair[1] {
            ((pair[0].clone(), pair[1].clone()), 1)
        } else {
            ((pair[1].clone(), pair[0].clone()), -1)
        };
        vector[edge_index[&key]] += sign;
    }
    vector
}

fn bounded_vectors(dimension: usize, bound: i8) -> Vec<Vec<i8>> {
    fn extend(dimension: usize, remaining: i8, current: &mut Vec<i8>, output: &mut Vec<Vec<i8>>) {
        if current.len() == dimension {
            output.push(current.clone());
            return;
        }
        for value in -remaining..=remaining {
            current.push(value);
            extend(dimension, remaining - value.abs(), current, output);
            current.pop();
        }
    }
    let mut output = Vec::new();
    extend(dimension, bound, &mut Vec::new(), &mut output);
    output
}

fn rank_i64(matrix: &[Vec<i64>]) -> usize {
    if matrix.is_empty() {
        return 0;
    }
    let mut work = matrix
        .iter()
        .map(|row| row.iter().map(|value| *value as f64).collect::<Vec<_>>())
        .collect::<Vec<_>>();
    let mut rank = 0;
    for column in 0..work[0].len() {
        let Some(pivot) = (rank..work.len()).find(|row| work[*row][column].abs() > 0.5) else {
            continue;
        };
        work.swap(rank, pivot);
        let divisor = work[rank][column];
        for entry in &mut work[rank][column..] {
            *entry /= divisor;
        }
        let pivot_row = work[rank].clone();
        for row in 0..work.len() {
            if row == rank {
                continue;
            }
            let factor = work[row][column];
            for entry in column..work[row].len() {
                work[row][entry] -= factor * pivot_row[entry];
            }
        }
        rank += 1;
        if rank == work.len() {
            break;
        }
    }
    rank
}

fn unit_peel_rank(matrix: &[Vec<i64>], omitted_column: usize) -> usize {
    let mut active = (0..matrix[0].len())
        .filter(|column| *column != omitted_column)
        .collect::<BTreeSet<_>>();
    let mut peeled = 0;
    loop {
        let pivot = matrix.iter().find_map(|row| {
            let support = active
                .iter()
                .filter(|column| row[**column] != 0)
                .copied()
                .collect::<Vec<_>>();
            if support.len() == 1 && row[support[0]].abs() == 1 {
                Some(support[0])
            } else {
                None
            }
        });
        let Some(column) = pivot else {
            break;
        };
        active.remove(&column);
        peeled += 1;
    }
    peeled
}

fn main() {
    let vertices = triangulations();
    assert_eq!(vertices.len(), 14);
    let mut graph = BTreeMap::<Face, Vec<Face>>::new();
    for vertex in &vertices {
        graph.entry(vertex.clone()).or_default();
    }
    let mut edges = Vec::<(Face, Face)>::new();
    for i in 0..vertices.len() {
        for j in (i + 1)..vertices.len() {
            if vertices[i].intersection(&vertices[j]).count() == 2 {
                let pair = if vertices[i] < vertices[j] {
                    (vertices[i].clone(), vertices[j].clone())
                } else {
                    (vertices[j].clone(), vertices[i].clone())
                };
                edges.push(pair);
                graph
                    .get_mut(&vertices[i])
                    .unwrap()
                    .push(vertices[j].clone());
                graph
                    .get_mut(&vertices[j])
                    .unwrap()
                    .push(vertices[i].clone());
            }
        }
    }
    edges.sort();
    assert_eq!(edges.len(), 21);
    let edge_index = edges
        .iter()
        .cloned()
        .enumerate()
        .map(|(index, edge)| (edge, index))
        .collect::<BTreeMap<_, _>>();

    // Independently construct the expanded octahedral source.  Its six
    // original vertices are (axis, sign).  Every opposite-sign edge receives
    // two occurrence-distinct internal vertices; equal-sign edges stay
    // unsubdivided, even when Gamma_0 identifies their endpoints.
    let source_vertex = |axis: usize, sign: i8| axis * 2 + usize::from(sign < 0);
    let mut source_vertex_count = 6;
    let mut source_segments = Vec::<(usize, usize)>::new();
    let mut expanded_edge_chains = BTreeMap::<(usize, i8, usize, i8), Vec<(usize, i8)>>::new();
    let mut gamma_one_edges = BTreeMap::<(usize, i8, usize, i8), Vec<i8>>::new();
    for left_axis in 0..3 {
        for right_axis in (left_axis + 1)..3 {
            for left_sign in [1_i8, -1] {
                for right_sign in [1_i8, -1] {
                    let path = shortest_path(
                        &graph,
                        &sector(left_axis, left_sign),
                        &sector(right_axis, right_sign),
                    );
                    let gamma = edge_vector(&path, &edge_index, edges.len());
                    let mut chain_vertices = vec![source_vertex(left_axis, left_sign)];
                    if left_sign != right_sign {
                        assert_eq!(path.len() - 1, 3);
                        chain_vertices.push(source_vertex_count);
                        chain_vertices.push(source_vertex_count + 1);
                        source_vertex_count += 2;
                    } else {
                        assert_eq!(path.len() - 1, 2);
                    }
                    chain_vertices.push(source_vertex(right_axis, right_sign));
                    let mut chain = Vec::new();
                    for endpoints in chain_vertices.windows(2) {
                        let segment = source_segments.len();
                        source_segments.push((endpoints[0], endpoints[1]));
                        chain.push((segment, 1));
                    }
                    expanded_edge_chains
                        .insert((left_axis, left_sign, right_axis, right_sign), chain);
                    gamma_one_edges.insert((left_axis, left_sign, right_axis, right_sign), gamma);
                }
            }
        }
    }
    assert_eq!(source_vertex_count, 18);
    assert_eq!(source_segments.len(), 24);

    let mut source_d1 = vec![vec![0_i64; source_segments.len()]; source_vertex_count];
    for (column, (source, target)) in source_segments.iter().enumerate() {
        source_d1[*source][column] = -1;
        source_d1[*target][column] = 1;
    }
    assert_eq!(rank_i64(&source_d1), 17);

    let mut source_d2 = vec![vec![0_i64; 8]; source_segments.len()];
    let mut expected_gamma_boundaries = Vec::<Vec<i8>>::new();
    for mask in 0_u8..8 {
        let signs =
            std::array::from_fn::<_, 3, _>(|axis| if mask & (1 << axis) == 0 { 1 } else { -1 });
        let mut gamma_boundary = vec![0_i8; edges.len()];
        for (left_axis, right_axis, direction) in [(0, 1, 1_i8), (1, 2, 1), (0, 2, -1)] {
            let key = (left_axis, signs[left_axis], right_axis, signs[right_axis]);
            for (segment, local_sign) in &expanded_edge_chains[&key] {
                source_d2[*segment][mask as usize] += i64::from(direction * local_sign);
            }
            for (entry, value) in gamma_boundary.iter_mut().zip(&gamma_one_edges[&key]) {
                *entry += direction * value;
            }
        }
        expected_gamma_boundaries.push(gamma_boundary);
    }
    let mut source_boundary_squared = Vec::new();
    for row in 0..source_vertex_count {
        for column in 0..8 {
            source_boundary_squared.push(
                (0..source_segments.len())
                    .map(|middle| source_d1[row][middle] * source_d2[middle][column])
                    .sum::<i64>(),
            );
        }
    }
    assert!(source_boundary_squared.iter().all(|value| *value == 0));
    assert_eq!(rank_i64(&source_d2), 7);
    assert!((0..8).any(|omitted| unit_peel_rank(&source_d2, omitted) == 7));

    let labels = (0..6)
        .flat_map(|a| ((a + 1)..6).map(move |b| (a, b)))
        .filter(|(a, b)| !boundary(*a, *b))
        .collect::<Vec<_>>();
    let mut facet_vectors = Vec::new();
    for label in &labels {
        let facet_vertices = vertices
            .iter()
            .filter(|vertex| vertex.contains(label))
            .cloned()
            .collect::<BTreeSet<_>>();
        let start = facet_vertices.iter().next().unwrap().clone();
        let mut path = vec![start.clone()];
        let mut previous = None;
        let mut current = start.clone();
        loop {
            let mut neighbors = graph[&current]
                .iter()
                .filter(|next| facet_vertices.contains(*next) && Some(*next) != previous.as_ref())
                .cloned()
                .collect::<Vec<_>>();
            neighbors.sort();
            let next = neighbors
                .iter()
                .find(|next| **next != start)
                .cloned()
                .unwrap_or_else(|| neighbors[0].clone());
            if next == start {
                path.push(start.clone());
                break;
            }
            path.push(next.clone());
            previous = Some(current);
            current = next;
        }
        assert!(matches!(path.len() - 1, 4 | 5));
        facet_vectors.push(edge_vector(&path, &edge_index, edges.len()));
    }
    assert_eq!(facet_vectors.len(), 9);
    let norm_three_candidates = bounded_vectors(9, 3);

    let mut zero_cones = 0;
    let mut mixed_cones = 0;
    let mut facet_occurrences = BTreeMap::<Diagonal, usize>::new();
    let mut oriented_total = vec![0_i8; 9];
    let mut gamma_two_columns = Vec::<Vec<i8>>::new();
    for mask in 0_u8..8 {
        let signs =
            std::array::from_fn::<_, 3, _>(|axis| if mask & (1 << axis) == 0 { 1 } else { -1 });
        let mut loop_path = shortest_path(&graph, &sector(0, signs[0]), &sector(1, signs[1]));
        let second = shortest_path(&graph, &sector(1, signs[1]), &sector(2, signs[2]));
        let third = shortest_path(&graph, &sector(2, signs[2]), &sector(0, signs[0]));
        loop_path.extend(second.into_iter().skip(1));
        loop_path.extend(third.into_iter().skip(1));
        let loop_vector = edge_vector(&loop_path, &edge_index, edges.len());
        assert_eq!(loop_vector, expected_gamma_boundaries[mask as usize]);
        let support = loop_vector.iter().filter(|value| **value != 0).count();
        if support == 0 {
            zero_cones += 1;
            gamma_two_columns.push(vec![0; 9]);
            continue;
        }
        assert_eq!(support, 8);
        mixed_cones += 1;

        let mut solutions = Vec::<Vec<i8>>::new();
        for code in 0..3_usize.pow(9) {
            let mut value = code;
            let coefficients = (0..9)
                .map(|_| {
                    let coefficient = (value % 3) as i8 - 1;
                    value /= 3;
                    coefficient
                })
                .collect::<Vec<_>>();
            let mut boundary_sum = vec![0_i8; edges.len()];
            for (coefficient, facet) in coefficients.iter().zip(&facet_vectors) {
                for (entry, value) in boundary_sum.iter_mut().zip(facet) {
                    *entry += coefficient * value;
                }
            }
            if boundary_sum == loop_vector {
                solutions.push(coefficients);
            }
        }
        let minimum = solutions
            .iter()
            .map(|solution| {
                solution
                    .iter()
                    .map(|value| value.abs() as usize)
                    .sum::<usize>()
            })
            .min()
            .unwrap();
        let minimal = solutions
            .iter()
            .filter(|solution| {
                solution
                    .iter()
                    .map(|value| value.abs() as usize)
                    .sum::<usize>()
                    == minimum
            })
            .collect::<Vec<_>>();
        assert_eq!(minimum, 3);
        assert_eq!(minimal.len(), 1);
        let all_norm_at_most_three = norm_three_candidates
            .iter()
            .filter(|coefficients| {
                let mut boundary_sum = vec![0_i8; edges.len()];
                for (coefficient, facet) in coefficients.iter().zip(&facet_vectors) {
                    for (entry, value) in boundary_sum.iter_mut().zip(facet) {
                        *entry += coefficient * value;
                    }
                }
                boundary_sum == loop_vector
            })
            .collect::<Vec<_>>();
        assert_eq!(all_norm_at_most_three.len(), 1);
        assert_eq!(
            all_norm_at_most_three[0]
                .iter()
                .map(|value| value.abs() as usize)
                .sum::<usize>(),
            3
        );
        gamma_two_columns.push(minimal[0].clone());
        let source_orientation = signs.iter().product::<i8>();
        for (total, coefficient) in oriented_total.iter_mut().zip(minimal[0]) {
            *total += source_orientation * coefficient;
        }
        for (label, coefficient) in labels.iter().zip(minimal[0]) {
            if *coefficient != 0 {
                *facet_occurrences.entry(*label).or_default() += 1;
            }
        }
    }
    assert_eq!(zero_cones, 2);
    assert_eq!(mixed_cones, 6);
    assert_eq!(gamma_two_columns.len(), 8);
    assert_eq!(facet_occurrences.len(), 9);
    assert!(facet_occurrences.values().all(|count| *count == 2));

    let target_d2 = (0..edges.len())
        .map(|row| {
            (0..facet_vectors.len())
                .map(|column| i64::from(facet_vectors[column][row]))
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();
    assert_eq!(rank_i64(&target_d2), 8);
    assert!((0..9).any(|omitted| unit_peel_rank(&target_d2, omitted) == 8));
    for column in 0..8 {
        for row in 0..edges.len() {
            let boundary = (0..9)
                .map(|facet| target_d2[row][facet] * i64::from(gamma_two_columns[column][facet]))
                .sum::<i64>();
            assert_eq!(boundary, i64::from(expected_gamma_boundaries[column][row]));
        }
    }

    let mut sphere_candidates = Vec::<Vec<i8>>::new();
    for code in 0..3_usize.pow(9) {
        let mut value = code;
        let coefficients = (0..9)
            .map(|_| {
                let coefficient = (value % 3) as i8 - 1;
                value /= 3;
                coefficient
            })
            .collect::<Vec<_>>();
        if coefficients.iter().all(|coefficient| *coefficient == 0) {
            continue;
        }
        let mut boundary_sum = vec![0_i8; edges.len()];
        for (coefficient, facet) in coefficients.iter().zip(&facet_vectors) {
            for (entry, value) in boundary_sum.iter_mut().zip(facet) {
                *entry += coefficient * value;
            }
        }
        if boundary_sum.iter().all(|entry| *entry == 0) {
            sphere_candidates.push(coefficients);
        }
    }
    assert_eq!(sphere_candidates.len(), 2);
    let sphere = sphere_candidates
        .into_iter()
        .find(|candidate| candidate.iter().find(|value| **value != 0) == Some(&1))
        .unwrap();
    assert!(sphere.iter().all(|coefficient| coefficient.abs() == 1));
    let degree: i8 = if oriented_total
        .iter()
        .zip(&sphere)
        .all(|(total, primitive)| *total == 2 * primitive)
    {
        2
    } else if oriented_total
        .iter()
        .zip(&sphere)
        .all(|(total, primitive)| *total == -2 * primitive)
    {
        -2
    } else {
        panic!("oriented maximal-cone sum is not a scalar fundamental sphere");
    };
    assert_eq!(degree.abs(), 2);

    println!(
        "{{\"status\":\"proved_expanded_full_log_integral_cellular_chain_map\",\"source_C2\":8,\"source_C1\":24,\"source_C0\":18,\"source_inserted_vertices\":12,\"source_d1_rank\":17,\"source_d2_rank\":7,\"source_d2_smith_unit_factors\":7,\"target_C2\":9,\"target_C1\":21,\"target_C0\":14,\"target_d2_rank\":8,\"target_d2_smith_unit_factors\":8,\"chain_equation\":true,\"same_sheet_zero_fillers\":2,\"mixed_fillers\":6,\"minimal_facets_per_mixed_filler\":3,\"gamma2_homogeneous_module\":\"Z^8\",\"oriented_cellular_degree_abs\":2,\"finite_chain_realization\":true,\"proper_extraordinary_kernel_constructed\":false,\"literal_full_Boolean_facet_lift_reused_not_reproved\":true,\"mapping_fiber_instantiated\":false}}"
    );
}
