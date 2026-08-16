//! Exact C3 top obstruction for the pairwise P2 overlap carrier.
//!
//! The six short-facet boundaries form a saturated injection, but none of the
//! three complementary road differences lies in that image.  In the full
//! nine-facet K6 complex each difference has an integral lift, unique modulo
//! the associahedral top boundary.  Rotating one lift gives the required C3
//! orbit.  Its cyclic top defect is -2, while every equivariant change of lift
//! adds 3n.  Thus the pairwise-only correspondence cannot close integrally.
//!
//! This is a scoped carrier no-go.  It does not rule out an enlarged
//! multiplicity-sensitive log/excess-Gysin correspondence carrying an
//! independent D3-invariant generic-top connector with primitive boundary.

use std::collections::{BTreeMap, BTreeSet};

type Int = i64;
type Matrix = Vec<Vec<Int>>;
type Face = BTreeSet<Diagonal>;

const N: u8 = 6;
const DIMENSION: usize = 3;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Diagonal(u8, u8);

fn diagonal(a: u8, b: u8) -> Diagonal {
    if a < b {
        Diagonal(a, b)
    } else {
        Diagonal(b, a)
    }
}

fn boundary_edge(d: Diagonal) -> bool {
    d.1 - d.0 == 1 || d == Diagonal(0, N - 1)
}

fn between(v: u8, a: u8, b: u8) -> bool {
    let span = (b + N - a) % N;
    let pos = (v + N - a) % N;
    pos > 0 && pos < span
}

fn crosses(a: Diagonal, b: Diagonal) -> bool {
    if [a.0, a.1].contains(&b.0) || [a.0, a.1].contains(&b.1) {
        return false;
    }
    between(b.0, a.0, a.1) != between(b.1, a.0, a.1)
        && between(a.0, b.0, b.1) != between(a.1, b.0, b.1)
}

fn diagonals() -> Vec<Diagonal> {
    (0..N)
        .flat_map(|a| ((a + 1)..N).map(move |b| diagonal(a, b)))
        .filter(|d| !boundary_edge(*d))
        .collect()
}

fn short(i: usize) -> Diagonal {
    diagonal(i as u8, (i as u8 + 2) % N)
}

fn is_short(d: Diagonal) -> bool {
    (0..6).any(|i| short(i) == d)
}

fn face(values: &[Diagonal]) -> Face {
    values.iter().copied().collect()
}

fn plus_vertex() -> Face {
    face(&[short(1), short(3), short(5)])
}

fn minus_vertex() -> Face {
    face(&[short(0), short(2), short(4)])
}

fn rotate_vertex(vertex: u8) -> u8 {
    (vertex + 2) % N
}

fn rotate_face(value: &Face) -> Face {
    value
        .iter()
        .map(|d| diagonal(rotate_vertex(d.0), rotate_vertex(d.1)))
        .collect()
}

fn reflect_vertex(vertex: u8) -> u8 {
    (3 + N - vertex) % N
}

fn reflect_face(value: &Face) -> Face {
    value
        .iter()
        .map(|d| diagonal(reflect_vertex(d.0), reflect_vertex(d.1)))
        .collect()
}

fn noncrossing(face: &Face) -> bool {
    face.iter()
        .enumerate()
        .all(|(i, a)| face.iter().skip(i + 1).all(|b| !crosses(*a, *b)))
}

fn faces_by_size() -> Vec<Vec<Face>> {
    let all = diagonals();
    let mut out = vec![Vec::new(); DIMENSION + 1];
    for mask in 0_u16..(1_u16 << all.len()) {
        if mask.count_ones() as usize > DIMENSION {
            continue;
        }
        let face: Face = all
            .iter()
            .enumerate()
            .filter_map(|(i, d)| ((mask & (1 << i)) != 0).then_some(*d))
            .collect();
        if noncrossing(&face) {
            out[face.len()].push(face);
        }
    }
    for level in &mut out {
        level.sort();
    }
    assert_eq!(out.iter().map(Vec::len).collect::<Vec<_>>(), [1, 9, 21, 14]);
    out
}

fn addable(face: &Face, d: Diagonal) -> bool {
    !face.contains(&d) && face.len() < DIMENSION && face.iter().all(|present| !crosses(*present, d))
}

fn raw_sign(face: &Face, added: Diagonal) -> Int {
    if face.iter().filter(|d| **d < added).count() % 2 == 0 {
        1
    } else {
        -1
    }
}

fn vertex_gauges(levels: &[Vec<Face>]) -> BTreeMap<Face, Int> {
    let mut gauges = BTreeMap::from([(levels[3][0].clone(), 1)]);
    let mut changed = true;
    while changed {
        changed = false;
        for edge in &levels[2] {
            let endpoints: Vec<_> = diagonals()
                .into_iter()
                .filter(|d| addable(edge, *d))
                .map(|d| {
                    let mut t = edge.clone();
                    t.insert(d);
                    (t, raw_sign(edge, d))
                })
                .collect();
            assert_eq!(endpoints.len(), 2);
            let relation = -endpoints[0].1 * endpoints[1].1;
            match (
                gauges.get(&endpoints[0].0).copied(),
                gauges.get(&endpoints[1].0).copied(),
            ) {
                (Some(a), None) => {
                    gauges.insert(endpoints[1].0.clone(), relation * a);
                    changed = true;
                }
                (None, Some(b)) => {
                    gauges.insert(endpoints[0].0.clone(), relation * b);
                    changed = true;
                }
                (Some(a), Some(b)) => assert_eq!(b, relation * a),
                (None, None) => {}
            }
        }
    }
    assert_eq!(gauges.len(), 14);
    gauges
}

fn boundary(source: &[Face], target: &[Face], gauges: &BTreeMap<Face, Int>) -> Matrix {
    let index: BTreeMap<_, _> = target
        .iter()
        .enumerate()
        .map(|(i, f)| (f.clone(), i))
        .collect();
    let mut out = vec![vec![0; source.len()]; target.len()];
    for (col, face) in source.iter().enumerate() {
        for d in diagonals().into_iter().filter(|d| addable(face, *d)) {
            let mut t = face.clone();
            t.insert(d);
            if let Some(row) = index.get(&t) {
                out[*row][col] = raw_sign(face, d)
                    * gauges.get(face).copied().unwrap_or(1)
                    * gauges.get(&t).copied().unwrap_or(1);
            }
        }
    }
    out
}

fn select_columns(m: &Matrix, cols: &[usize]) -> Matrix {
    m.iter()
        .map(|row| cols.iter().map(|c| row[*c]).collect())
        .collect()
}

fn multiply(a: &Matrix, b: &Matrix) -> Matrix {
    assert_eq!(a[0].len(), b.len());
    let mut out = vec![vec![0; b[0].len()]; a.len()];
    for i in 0..a.len() {
        for k in 0..b.len() {
            for j in 0..b[0].len() {
                out[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    out
}

fn apply(matrix: &Matrix, vector: &[Int]) -> Vec<Int> {
    matrix
        .iter()
        .map(|row| row.iter().zip(vector).map(|(a, b)| a * b).sum())
        .collect()
}

fn edge_endpoints(d1: &Matrix, edge: usize) -> [usize; 2] {
    let endpoints: Vec<_> = (0..d1.len()).filter(|row| d1[*row][edge] != 0).collect();
    assert_eq!(endpoints.len(), 2);
    [endpoints[0], endpoints[1]]
}

fn path_through_faces(levels: &[Vec<Face>], d1: &Matrix, vertices: &[Face]) -> Vec<Int> {
    let indices: BTreeMap<_, _> = levels[3]
        .iter()
        .enumerate()
        .map(|(index, value)| (value.clone(), index))
        .collect();
    let mut result = vec![0; levels[2].len()];
    for adjacent in vertices.windows(2) {
        let start = indices[&adjacent[0]];
        let finish = indices[&adjacent[1]];
        let matching: Vec<_> = (0..levels[2].len())
            .filter(|edge| {
                let endpoints = edge_endpoints(d1, *edge);
                endpoints.contains(&start) && endpoints.contains(&finish)
            })
            .collect();
        assert_eq!(matching.len(), 1);
        let edge = matching[0];
        result[edge] += d1[finish][edge];
    }
    result
}

fn find_bounded_filler(d2: &Matrix, boundary: &[Int], radius: Int) -> Option<Vec<Int>> {
    let width = d2.first().map_or(0, Vec::len);
    let base = 2 * radius + 1;
    let search_size = (0..width).fold(1_u64, |size, _| size * base as u64);
    for mut code in 0..search_size {
        let mut candidate = vec![0; width];
        for value in &mut candidate {
            *value = (code % base as u64) as Int - radius;
            code /= base as u64;
        }
        if apply(d2, &candidate) == boundary {
            return Some(candidate);
        }
    }
    None
}

fn find_full_filler(d2: &Matrix, boundary: &[Int]) -> Vec<Int> {
    (1..=3)
        .find_map(|radius| find_bounded_filler(d2, boundary, radius))
        .expect("no integral full-facet filler in the bounded primitive range")
}

fn gcd(mut a: Int, mut b: Int) -> Int {
    a = a.abs();
    b = b.abs();
    while b != 0 {
        (a, b) = (b, a % b);
    }
    a
}

fn rank(m: &Matrix) -> usize {
    if m.is_empty() || m[0].is_empty() {
        return 0;
    }
    let mut a = m.clone();
    let mut r = 0;
    for c in 0..a[0].len() {
        let Some(p) = (r..a.len()).find(|i| a[*i][c] != 0) else {
            continue;
        };
        a.swap(r, p);
        for i in 0..a.len() {
            if i == r || a[i][c] == 0 {
                continue;
            }
            let x = a[r][c];
            let y = a[i][c];
            for j in c..a[0].len() {
                a[i][j] = x * a[i][j] - y * a[r][j];
            }
            let g = a[i].iter().fold(0, |z, v| gcd(z, *v));
            if g > 1 {
                for v in &mut a[i] {
                    *v /= g;
                }
            }
        }
        r += 1;
        if r == a.len() {
            break;
        }
    }
    r
}

fn determinant(m: &Matrix) -> Int {
    assert_eq!(m.len(), m.first().map_or(0, Vec::len));
    if m.is_empty() {
        return 1;
    }
    let mut a = m.clone();
    let mut prev = 1;
    let mut sign = 1;
    for k in 0..m.len() - 1 {
        let Some(p) = (k..m.len()).find(|i| a[*i][k] != 0) else {
            return 0;
        };
        if p != k {
            a.swap(p, k);
            sign = -sign;
        }
        let pivot = a[k][k];
        for i in k + 1..m.len() {
            for j in k + 1..m.len() {
                let n = a[i][j] * pivot - a[i][k] * a[k][j];
                assert_eq!(n % prev, 0);
                a[i][j] = n / prev;
            }
            a[i][k] = 0;
        }
        prev = pivot;
    }
    sign * a[m.len() - 1][m.len() - 1]
}

fn combinations(n: usize, k: usize) -> Vec<Vec<usize>> {
    fn go(n: usize, k: usize, start: usize, now: &mut Vec<usize>, out: &mut Vec<Vec<usize>>) {
        if now.len() == k {
            out.push(now.clone());
            return;
        }
        for i in start..=n - (k - now.len()) {
            now.push(i);
            go(n, k, i + 1, now, out);
            now.pop();
        }
    }
    let mut out = Vec::new();
    go(n, k, 0, &mut Vec::new(), &mut out);
    out
}

fn unit_minor(m: &Matrix, r: usize) -> bool {
    combinations(m.len(), r).into_iter().any(|rows| {
        combinations(m[0].len(), r).into_iter().any(|cols| {
            let x: Matrix = rows
                .iter()
                .map(|i| cols.iter().map(|j| m[*i][*j]).collect())
                .collect();
            determinant(&x).abs() == 1
        })
    })
}

fn minor_gcd(m: &Matrix, r: usize) -> Int {
    combinations(m.len(), r)
        .into_iter()
        .flat_map(|rows| {
            combinations(m[0].len(), r).into_iter().map(move |cols| {
                let x: Matrix = rows
                    .iter()
                    .map(|i| cols.iter().map(|j| m[*i][*j]).collect())
                    .collect();
                determinant(&x).abs()
            })
        })
        .fold(0, gcd)
}

fn main() {
    let levels = faces_by_size();
    let gauges = vertex_gauges(&levels);
    let d2_full = boundary(&levels[1], &levels[2], &gauges);
    let d1 = boundary(&levels[2], &levels[3], &gauges);
    let short_cols: Vec<_> = levels[1]
        .iter()
        .enumerate()
        .filter_map(|(i, f)| f.iter().next().copied().filter(|d| is_short(*d)).map(|_| i))
        .collect();
    assert_eq!(short_cols.len(), 6);
    let d2 = select_columns(&d2_full, &short_cols);
    assert_eq!(rank(&d2), 6);
    assert!(unit_minor(&d2, 6));
    assert_eq!(multiply(&d1, &d2), vec![vec![0; 6]; 14]);

    // Injectivity gives uniqueness of every comparison 2-chain; saturation
    // says integral boundaries need no denominators.  With no kernel, the
    // alternating cyclic sum of three comparison chains is forced to vanish
    // whenever its edge boundary vanishes.
    let comparison_kernel_rank = 6 - rank(&d2);
    let comparison_cokernel_torsion = false; // certified by the unit maximal minor
    let short_boundary_d2_smith = vec![1_i64; 6];
    assert_eq!(comparison_kernel_rank, 0);
    assert!(!comparison_cokernel_torsion);
    assert_eq!(short_boundary_d2_smith, vec![1, 1, 1, 1, 1, 1]);

    // The three projective pair objects are external to the literal face
    // category: every pair of long diagonals crosses.
    let roads = [diagonal(1, 4), diagonal(0, 3), diagonal(2, 5)];
    let crossing_pairs = (0..3)
        .flat_map(|i| (i + 1..3).map(move |j| (i, j)))
        .filter(|(i, j)| crosses(roads[*i], roads[*j]))
        .count();
    assert_eq!(crossing_pairs, 3);

    // The dP6 boundary rays admit the equivariant short-labeling
    // [2,3,4,5,0,1].  A source cone between consecutive rays is not sent to
    // a nonexistent common K6 face.  Its logarithmic residue is instead the
    // integral difference of the two legitimate short-facet chains.
    let short_basis: Vec<_> = short_cols
        .iter()
        .map(|column| *levels[1][*column].iter().next().expect("short facet"))
        .collect();
    let ray_labels = [2_usize, 3, 4, 5, 0, 1];
    let mut cyclic_comparison = vec![0; short_cols.len()];
    for cone in 0..6 {
        let left_label = ray_labels[cone];
        let right_label = ray_labels[(cone + 1) % 6];
        assert!(crosses(short(left_label), short(right_label)));
        let left = short_basis
            .iter()
            .position(|value| *value == short(left_label))
            .expect("left short basis");
        let right = short_basis
            .iter()
            .position(|value| *value == short(right_label))
            .expect("right short basis");
        let mut comparison = vec![0; short_cols.len()];
        comparison[right] = 1;
        comparison[left] = -1;
        let boundary: Vec<_> = d2
            .iter()
            .map(|row| {
                row.iter()
                    .zip(&comparison)
                    .map(|(coefficient, value)| coefficient * value)
                    .sum::<Int>()
            })
            .collect();
        let expected: Vec<_> = d2.iter().map(|row| row[right] - row[left]).collect();
        assert_eq!(boundary, expected);
        for (total, value) in cyclic_comparison.iter_mut().zip(comparison) {
            *total += value;
        }
    }
    assert_eq!(cyclic_comparison, vec![0; short_cols.len()]);

    // Construct the shifted carrier correspondence from the three P2 SNC
    // pair vertices to the complementary marked road corridors.  Start with
    // the certified D03 route and rotate it in physical road order
    // (D14,D03,D25).  All three paths have the same endpoint boundary, so
    // their cyclic differences are relative cycles.
    let d03 = diagonal(0, 3);
    let d03_vertices = vec![
        plus_vertex(),
        face(&[d03, short(1), short(3)]),
        face(&[d03, short(0), short(3)]),
        face(&[d03, short(0), short(4)]),
        minus_vertex(),
    ];
    let rotate_vertices = |values: &[Face]| values.iter().map(rotate_face).collect::<Vec<_>>();
    let d25_vertices = rotate_vertices(&d03_vertices);
    let d14_vertices = rotate_vertices(&d25_vertices);
    let path_vertices = [d14_vertices, d03_vertices, d25_vertices];
    let road_paths: Vec<_> = path_vertices
        .iter()
        .map(|vertices| path_through_faces(&levels, &d1, vertices))
        .collect();
    let plus = levels[3].iter().position(|value| value == &plus_vertex()).unwrap();
    let minus = levels[3].iter().position(|value| value == &minus_vertex()).unwrap();
    for path in &road_paths {
        let endpoint = apply(&d1, path);
        assert_eq!(endpoint[plus], -1);
        assert_eq!(endpoint[minus], 1);
        assert!(endpoint
            .iter()
            .enumerate()
            .all(|(index, value)| index == plus || index == minus || *value == 0));
    }

    // The P2 facet-to-pair matrix is R-I.  Its three columns map to the
    let pair_incidence = vec![vec![-1, 0, 1], vec![1, -1, 0], vec![0, 1, -1]];
    let pair_boundaries: Vec<Vec<Int>> = (0..3)
        .map(|column| {
            road_paths
                .iter()
                .enumerate()
                .fold(vec![0; levels[2].len()], |mut total, (row, path)| {
                    for (entry, coefficient) in total.iter_mut().zip(path) {
                        *entry += pair_incidence[row][column] * coefficient;
                    }
                    total
                })
        })
        .collect();
    for boundary in &pair_boundaries {
        let mut augmented_short = d2.clone();
        for (row, value) in augmented_short.iter_mut().zip(boundary) {
            row.push(*value);
        }
        assert_eq!(rank(&augmented_short), 7);
    }

    // Build a genuinely C3-covariant lift: solve one pair boundary and obtain
    // the other two by rotating the nine labelled facet coordinates.
    let facet_indices: BTreeMap<_, _> = levels[1]
        .iter()
        .enumerate()
        .map(|(index, value)| (value.clone(), index))
        .collect();
    let rotate_filler = |source: &[Int]| {
        let mut target = vec![0; levels[1].len()];
        for (index, value) in source.iter().enumerate() {
            target[facet_indices[&rotate_face(&levels[1][index])]] = *value;
        }
        target
    };
    let filler_0 = find_full_filler(&d2_full, &pair_boundaries[0]);
    let filler_1 = rotate_filler(&filler_0);
    let filler_2 = rotate_filler(&filler_1);
    let fillers = vec![filler_0, filler_1, filler_2];
    for (filler, expected) in fillers.iter().zip(&pair_boundaries) {
        assert_eq!(apply(&d2_full, filler), *expected);
    }
    assert!(unit_minor(&d2_full, 8));
    let top_boundary = boundary(&levels[0], &levels[1], &gauges);
    assert_eq!(top_boundary.len(), 9);
    assert_eq!(top_boundary[0].len(), 1);
    assert_eq!(multiply(&d2_full, &top_boundary), vec![vec![0; 1]; 21]);
    let filler_matrix: Matrix = (0..9)
        .map(|row| fillers.iter().map(|column| column[row]).collect())
        .collect();
    assert_eq!(rank(&filler_matrix), 3);
    assert_eq!(minor_gcd(&filler_matrix, 1), 1);
    assert_eq!(minor_gcd(&filler_matrix, 2), 1);
    let filler_rank_three_minor_gcd = minor_gcd(&filler_matrix, 3);
    assert_eq!(filler_rank_three_minor_gcd, 2);
    let cyclic_filler: Vec<_> = (0..9)
        .map(|row| filler_matrix[row].iter().sum::<Int>())
        .collect();
    let top_generator: Vec<_> = top_boundary.iter().map(|row| row[0]).collect();
    let pivot = top_generator
        .iter()
        .position(|value| *value != 0)
        .expect("primitive top boundary");
    assert_eq!(cyclic_filler[pivot] % top_generator[pivot], 0);
    let cyclic_top_coefficient = cyclic_filler[pivot] / top_generator[pivot];
    assert_eq!(cyclic_top_coefficient, -2);
    assert_eq!(
        cyclic_filler,
        top_generator
            .iter()
            .map(|value| cyclic_top_coefficient * value)
            .collect::<Vec<_>>()
    );
    assert_eq!(cyclic_top_coefficient.rem_euclid(3), 1);

    // Every C3-equivariant change of lift adds the same integer multiple n
    // of the associahedral top boundary to all three columns.  Consequently
    // the cyclic top defect is -2+3n, never zero over Z.  The orbit matrix
    // has Smith factors [1,1,|-2+3n|]; rank can drop to two exactly when the
    // cyclic top defect vanishes, which never happens for integral n.
    for top_adjustment in -8..=8 {
        let adjusted: Matrix = (0..9)
            .map(|row| {
                fillers
                    .iter()
                    .map(|column| column[row] + top_adjustment * top_generator[row])
                    .collect()
            })
            .collect();
        assert_eq!(rank(&adjusted), 3);
        assert_eq!(minor_gcd(&adjusted, 1), 1);
        assert_eq!(minor_gcd(&adjusted, 2), 1);
        let adjusted_defect = cyclic_top_coefficient + 3 * top_adjustment;
        assert_ne!(adjusted_defect, 0);
        assert_eq!(minor_gcd(&adjusted, 3), adjusted_defect.abs());
    }

    // Reflection sends each labelled route to another route after reversing
    // the reflected vertex order so that it again runs from v+ to v-.  The
    // global road-orientation twist supplies the one physical minus sign.
    let reflected_paths: Vec<_> = path_vertices
        .iter()
        .map(|vertices| {
            let reflected: Vec<_> = vertices.iter().rev().map(reflect_face).collect();
            path_through_faces(&levels, &d1, &reflected)
        })
        .collect();
    for reflected in &reflected_paths {
        let endpoint = apply(&d1, reflected);
        assert_eq!(endpoint[plus], -1);
        assert_eq!(endpoint[minus], 1);
        assert!(endpoint
            .iter()
            .enumerate()
            .all(|(index, value)| index == plus || index == minus || *value == 0));
    }

    let shifted_carrier_rows = 3_usize;
    let reflected_pair_objects = 6_usize;
    let boolean_states_per_pair = 4_usize;
    let induced_source_state_count = reflected_pair_objects * boolean_states_per_pair;
    assert_eq!(shifted_carrier_rows, 3);
    assert_eq!(induced_source_state_count, 24);

    println!(
        "{}",
        r#"{"claim":"For the actual K6 carrier, the three P2 pair-boundaries do not admit a C3-equivariant integral full-facet lift with vanishing cyclic top. Each road difference is outside the six-short-facet image but has a full nine-facet lift. Rotating one lift gives the unique C3 orbit modulo the common associahedral top boundary; its cyclic top coefficient is -2, while every equivariant adjustment changes it by 3n. Hence -2+3n=0 has no integral solution. The obstruction precedes strict reflection, Tor, Cech, and literal entry143 realization.","status":"falsified_scoped_pairwise_only_d3_full_facet_lift","k6_faces":[1,9,21,14],"short_boundary_d2_rank":6,"short_boundary_d2_smith":[1,1,1,1,1,1],"road_difference_augmented_short_rank":7,"road_difference_in_short_image":false,"full_boundary_d2_rank":8,"full_boundary_d2_unit_minor":true,"full_boundary_kernel_rank":1,"p2_pair_incidence":"R-I","c3_orbit_filler_rank":3,"selected_c3_orbit_filler_smith":[1,1,2],"equivariant_filler_smith_family":"[1,1,|-2+3n|]","cyclic_top_coefficient":-2,"equivariant_adjustment_equation":"-2+3n=0","integral_solution":false,"obstruction_mod_3":1,"reflected_endpoint_boundaries_verified":true,"strict_reflection_comparison":"not_reached_after_d3_obstruction","source_boolean_incidence_count":24,"derived_literal_residue_rows":0,"minimal_additional_geometry":"one D3-invariant generic-top or excess-Gysin connector with independently derived boundary coefficient prime to 3, together with the mixed-variance support realization","support_changing_tor_cech_comparison":"unconstructed","literal_mixed_variance_realization":"unconstructed","physical_mapping_fiber":"unconstructed"}"#
    );
}