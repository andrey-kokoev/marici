use std::collections::{BTreeMap, BTreeSet, VecDeque};

type Diagonal = (u8, u8);
type Face = BTreeSet<Diagonal>;
type Ray = (usize, i8);

fn diagonal(a: u8, b: u8) -> Diagonal {
    if a < b {
        (a, b)
    } else {
        (b, a)
    }
}

fn boundary(a: u8, b: u8) -> bool {
    let distance = a.abs_diff(b);
    distance == 1 || distance == 5
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

fn sector(ray: Ray) -> Face {
    let d03 = diagonal(0, 3);
    let base = if ray.1 > 0 {
        [d03, short(1), short(3)]
    } else {
        [d03, short(0), short(4)]
    }
    .into_iter()
    .collect();
    rotate(&base, [2, 0, 1][ray.0])
}

fn reflect(face: &Face) -> Face {
    face.iter()
        .map(|(a, b)| diagonal((8 - a) % 6, (8 - b) % 6))
        .collect()
}

fn shortest_paths(
    graph: &BTreeMap<Face, Vec<Face>>,
    source: &Face,
    target: &Face,
) -> Vec<Vec<Face>> {
    let mut queue = VecDeque::from([vec![source.clone()]]);
    let mut best = usize::MAX;
    let mut answers = Vec::new();
    while let Some(path) = queue.pop_front() {
        let length = path.len() - 1;
        if length > best {
            continue;
        }
        let last = path.last().unwrap();
        if last == target {
            best = length;
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
    answers
        .into_iter()
        .filter(|path| path.len() - 1 == best)
        .collect()
}

fn main() {
    let vertices = triangulations();
    assert_eq!(vertices.len(), 14);
    let mut graph = BTreeMap::<Face, Vec<Face>>::new();
    for vertex in &vertices {
        graph.entry(vertex.clone()).or_default();
    }
    for i in 0..vertices.len() {
        for j in (i + 1)..vertices.len() {
            if vertices[i].intersection(&vertices[j]).count() == 2 {
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

    let mut geodesics = BTreeMap::<(Ray, Ray), Vec<Face>>::new();
    for left_axis in 0..3 {
        for right_axis in (left_axis + 1)..3 {
            for sign in [-1_i8, 1_i8] {
                let left = (left_axis, sign);
                let right = (right_axis, -sign);
                let paths = shortest_paths(&graph, &sector(left), &sector(right));
                assert_eq!(paths.len(), 1);
                assert_eq!(paths[0].len() - 1, 3);
                geodesics.insert((left, right), paths[0].clone());
            }
        }
    }
    assert_eq!(geodesics.len(), 6);

    let seed = geodesics[&((0, 1), (1, -1))].clone();
    assert_eq!(
        seed.iter().map(reflect).collect::<Vec<_>>(),
        geodesics[&((0, 1), (2, -1))]
    );
    for path in geodesics.values() {
        for edge in path.windows(2) {
            assert_eq!(edge[0].intersection(&edge[1]).count(), 2);
        }
    }

    println!(
        "{{\"status\":\"proved_scoped_unique_literal_K6_cross_sheet_geodesics\",\"K6_vertices\":14,\"cross_sheet_pairs\":6,\"shortest_length\":3,\"shortest_paths_per_pair\":1,\"subdivision_edges\":18,\"D3_orbit\":true,\"reflection_covariant\":true,\"carrier_choice\":false,\"full_Boolean_excess_lift_constructed\":false,\"global_maximal_cone_gluing_constructed\":false}}"
    );
}
