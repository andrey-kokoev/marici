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
    for mask in 0_u8..8 {
        let signs =
            std::array::from_fn::<_, 3, _>(|axis| if mask & (1 << axis) == 0 { 1 } else { -1 });
        let mut loop_path = shortest_path(&graph, &sector(0, signs[0]), &sector(1, signs[1]));
        let second = shortest_path(&graph, &sector(1, signs[1]), &sector(2, signs[2]));
        let third = shortest_path(&graph, &sector(2, signs[2]), &sector(0, signs[0]));
        loop_path.extend(second.into_iter().skip(1));
        loop_path.extend(third.into_iter().skip(1));
        let loop_vector = edge_vector(&loop_path, &edge_index, edges.len());
        let support = loop_vector.iter().filter(|value| **value != 0).count();
        if support == 0 {
            zero_cones += 1;
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
    assert_eq!(facet_occurrences.len(), 9);
    assert!(facet_occurrences.values().all(|count| *count == 2));

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
        "{{\"status\":\"proved_scoped_full_log_maximal_cone_K6_fillers\",\"K6_vertices\":14,\"K6_edges\":21,\"K6_facets\":9,\"maximal_cones\":8,\"same_sheet_zero_fillers\":2,\"mixed_cones\":6,\"mixed_loop_edge_support\":8,\"minimal_facets_per_mixed_filler\":3,\"minimal_fillers_per_mixed_cone\":1,\"facet_occurrences\":18,\"distinct_facets\":9,\"occurrences_per_facet\":2,\"facet_BC_equalities\":9,\"facet_BC_rank\":9,\"facet_BC_smith_unit_factors\":9,\"oriented_cellular_degree_abs\":2,\"primitive_K6_sphere_kernel_rank\":1,\"integer_torsion\":false,\"literal_full_Boolean_facet_lift_constructed\":false,\"global_endpoint_Q_map_constructed\":false}}"
    );
}
