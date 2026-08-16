use std::collections::{BTreeMap, BTreeSet, VecDeque};

type Edge = (usize, usize);

fn edge(a: usize, b: usize) -> Edge {
    if a < b {
        (a, b)
    } else {
        (b, a)
    }
}

fn oriented_edge(a: usize, b: usize) -> (Edge, i64) {
    (edge(a, b), if a < b { 1 } else { -1 })
}

fn rotate(v: usize) -> usize {
    (v + 2) % 6
}

fn reflect(v: usize) -> usize {
    (7 - v) % 6
}

fn determinant(mut matrix: Vec<Vec<i64>>) -> i64 {
    let n = matrix.len();
    if n == 0 {
        return 1;
    }
    let mut sign = 1_i64;
    let mut previous = 1_i64;
    for pivot in 0..(n - 1) {
        let Some(row) = (pivot..n).find(|row| matrix[*row][pivot] != 0) else {
            return 0;
        };
        if row != pivot {
            matrix.swap(row, pivot);
            sign = -sign;
        }
        let value = matrix[pivot][pivot];
        for i in (pivot + 1)..n {
            for j in (pivot + 1)..n {
                matrix[i][j] =
                    (matrix[i][j] * value - matrix[i][pivot] * matrix[pivot][j]) / previous;
            }
        }
        previous = value;
    }
    sign * matrix[n - 1][n - 1]
}

fn combinations(n: usize, k: usize) -> Vec<Vec<usize>> {
    fn visit(start: usize, n: usize, k: usize, chosen: &mut Vec<usize>, out: &mut Vec<Vec<usize>>) {
        if chosen.len() == k {
            out.push(chosen.clone());
            return;
        }
        for value in start..=n - (k - chosen.len()) {
            chosen.push(value);
            visit(value + 1, n, k, chosen, out);
            chosen.pop();
        }
    }
    let mut out = Vec::new();
    visit(0, n, k, &mut Vec::new(), &mut out);
    out
}

fn main() {
    // Ordered pair sectors map canonically to signed omitted-road axes.
    let signed_axis = [(2, 1_i64), (1, -1), (0, 1), (2, -1), (1, 1), (0, -1)];
    for axis in 0..3 {
        let pair = (0..6)
            .filter(|vertex| signed_axis[*vertex].0 == axis)
            .collect::<Vec<_>>();
        assert_eq!(pair.len(), 2);
        assert_eq!(pair[0] + 3, pair[1]);
        assert_eq!(signed_axis[pair[0]].1, -signed_axis[pair[1]].1);
    }

    let opposite = (0..3).map(|i| edge(i, i + 3)).collect::<BTreeSet<_>>();
    let edges = (0..6)
        .flat_map(|a| ((a + 1)..6).map(move |b| edge(a, b)))
        .filter(|present| !opposite.contains(present))
        .collect::<Vec<_>>();
    assert_eq!(edges.len(), 12);
    let edge_index = edges
        .iter()
        .enumerate()
        .map(|(index, present)| (*present, index))
        .collect::<BTreeMap<_, _>>();

    let vertex_for = |axis: usize, sign: i64| {
        (0..6)
            .find(|vertex| signed_axis[*vertex] == (axis, sign))
            .unwrap()
    };
    let mut faces = Vec::new();
    let mut top_coefficients = Vec::new();
    for mask in 0_u8..8 {
        let signs = std::array::from_fn::<_, 3, _>(|axis| {
            if mask & (1 << axis) == 0 {
                1_i64
            } else {
                -1_i64
            }
        });
        faces.push([
            vertex_for(0, signs[0]),
            vertex_for(1, signs[1]),
            vertex_for(2, signs[2]),
        ]);
        top_coefficients.push(signs.iter().product::<i64>());
    }
    assert_eq!(faces.len(), 8);

    let mut d1 = vec![vec![0_i64; edges.len()]; 6];
    for (column, (a, b)) in edges.iter().copied().enumerate() {
        d1[a][column] = -1;
        d1[b][column] = 1;
    }
    let mut d2 = vec![vec![0_i64; faces.len()]; edges.len()];
    for (column, [a, b, c]) in faces.iter().copied().enumerate() {
        for ((present, orientation), coefficient) in [
            (oriented_edge(b, c), 1),
            (oriented_edge(a, c), -1),
            (oriented_edge(a, b), 1),
        ] {
            d2[edge_index[&present]][column] += orientation * coefficient;
        }
    }
    for row in 0..6 {
        for column in 0..faces.len() {
            assert_eq!(
                (0..edges.len())
                    .map(|middle| d1[row][middle] * d2[middle][column])
                    .sum::<i64>(),
                0
            );
        }
    }

    let mut top_boundary = vec![0_i64; edges.len()];
    for row in 0..edges.len() {
        top_boundary[row] = (0..faces.len())
            .map(|column| d2[row][column] * top_coefficients[column])
            .sum();
    }
    assert!(top_boundary.iter().all(|value| *value == 0));
    assert!(top_coefficients.iter().any(|value| value.abs() == 1));

    let unit_rank7_minor = combinations(edges.len(), 7).into_iter().any(|rows| {
        combinations(faces.len(), 7).into_iter().any(|columns| {
            determinant(
                rows.iter()
                    .map(|row| columns.iter().map(|column| d2[*row][*column]).collect())
                    .collect(),
            )
            .abs()
                == 1
        })
    });
    assert!(unit_rank7_minor);

    let mut seen = BTreeSet::from([0_usize]);
    let mut queue = VecDeque::from([0_usize]);
    while let Some(vertex) = queue.pop_front() {
        for (a, b) in &edges {
            let next = if *a == vertex {
                Some(*b)
            } else if *b == vertex {
                Some(*a)
            } else {
                None
            };
            if let Some(next) = next {
                if seen.insert(next) {
                    queue.push_back(next);
                }
            }
        }
    }
    assert_eq!(seen.len(), 6);

    for action in [rotate as fn(usize) -> usize, reflect] {
        assert!(edges
            .iter()
            .all(|(a, b)| edge_index.contains_key(&edge(action(*a), action(*b)))));
        assert!(faces.iter().all(|face| {
            let image = face
                .iter()
                .map(|vertex| action(*vertex))
                .collect::<BTreeSet<_>>();
            faces
                .iter()
                .any(|candidate| candidate.iter().copied().collect::<BTreeSet<_>>() == image)
        }));
    }

    println!(
        "{{\"status\":\"proved_scoped_conductor_cross_polytope_carrier\",\"conductor_rank\":3,\"signed_sector_vertices\":6,\"opposite_pairs\":3,\"edges\":12,\"faces\":8,\"d1_rank\":5,\"d1_smith_nonzero_all_ones\":true,\"d2_rank\":7,\"d2_smith_nonzero_all_ones\":true,\"H2_rank\":1,\"H1_rank\":0,\"H0_rank\":1,\"primitive_fundamental_cycle\":true,\"D3\":true,\"reflection\":true,\"loaded_face_BC_maps_constructed\":false,\"six_functor_realization_constructed\":false}}"
    );
}
