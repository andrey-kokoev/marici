//! Integral cellular audit of the octagon associahedron and its physical-cut boundary.
//!
//! `K_5` is the five-dimensional associahedron whose cells are noncrossing
//! octagon dissections.  `B_cut` is the cellular subcomplex consisting of
//! cells whose fixed dissection contains at least one physical (opposite
//! parity) diagonal.  The checker constructs deterministic integral
//! orientations from the Loday realization, verifies d^2=0, performs unit
//! Smith elimination, and audits the D8 action and the pair connecting map.
//!
//! This is a calculation about a CW pair.  It does not declare a
//! Grothendieck topology or identify any six-point conductor chain.

use std::collections::{BTreeMap, BTreeSet};

const N: usize = 8;
const DIM: usize = N - 3;
type Int = i128;
type Vector = [Int; N - 2];
type Matrix = Vec<Vec<Int>>;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Edge(usize, usize);

type Face = Vec<Edge>;
type Triangulation = Vec<Edge>;

fn edge(a: usize, b: usize) -> Edge {
    assert_ne!(a, b);
    if a < b {
        Edge(a, b)
    } else {
        Edge(b, a)
    }
}

fn boundary_edge(e: Edge) -> bool {
    e.1 == e.0 + 1 || (e.0 == 0 && e.1 == N - 1)
}

fn physical(e: Edge) -> bool {
    e.0 % 2 != e.1 % 2
}

fn crosses(a: Edge, b: Edge) -> bool {
    if a.0 == b.0 || a.0 == b.1 || a.1 == b.0 || a.1 == b.1 {
        return false;
    }
    (a.0 < b.0 && b.0 < a.1 && a.1 < b.1) || (b.0 < a.0 && a.0 < b.1 && b.1 < a.1)
}

fn compatible(face: &Face) -> bool {
    (0..face.len()).all(|i| (i + 1..face.len()).all(|j| !crosses(face[i], face[j])))
}

fn contains(face: &Face, e: Edge) -> bool {
    face.binary_search(&e).is_ok()
}

fn add_edge(face: &Face, e: Edge) -> Face {
    let mut result = face.clone();
    result.push(e);
    result.sort();
    result.dedup();
    result
}

fn face_contains(large: &Face, small: &Face) -> bool {
    small.iter().all(|&e| contains(large, e))
}

fn diagonals() -> Vec<Edge> {
    let mut result = Vec::new();
    for a in 0..N {
        for b in a + 1..N {
            let e = edge(a, b);
            if !boundary_edge(e) {
                result.push(e);
            }
        }
    }
    result
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
        for l in &left {
            for r in &right {
                let mut t = Vec::new();
                t.extend(l.iter().copied());
                t.extend(r.iter().copied());
                if pivot > first + 1 {
                    t.push(edge(first, pivot));
                }
                if last > pivot + 1 {
                    t.push(edge(pivot, last));
                }
                t.sort();
                result.push(t);
            }
        }
    }
    result.sort();
    result.dedup();
    memo.insert((first, last), result.clone());
    result
}

fn triangulations() -> Vec<Triangulation> {
    interval_triangulations(0, N - 1, &mut BTreeMap::new())
}

fn faces(triangulations: &[Triangulation]) -> Vec<Face> {
    let mut result = BTreeSet::new();
    for t in triangulations {
        for mask in 0..1_usize << t.len() {
            result.insert(
                t.iter()
                    .copied()
                    .enumerate()
                    .filter_map(|(i, e)| (((mask >> i) & 1) == 1).then_some(e))
                    .collect::<Face>(),
            );
        }
    }
    result.into_iter().collect()
}

fn dimension(face: &Face) -> usize {
    DIM - face.len()
}

fn side(t: &Triangulation, a: usize, b: usize) -> bool {
    let e = edge(a, b);
    boundary_edge(e) || contains(t, e)
}

/// Integral coordinates of the Loday associahedron realization.
fn loday(t: &Triangulation) -> Vector {
    let mut result = [0; N - 2];
    for i in 1..N - 1 {
        let middle_triangles: Vec<_> = (0..i)
            .flat_map(|a| {
                (i + 1..N)
                    .filter(move |&b| side(t, a, i) && side(t, i, b) && side(t, a, b))
                    .map(move |b| (a, b))
            })
            .collect();
        assert_eq!(middle_triangles.len(), 1);
        let (a, b) = middle_triangles[0];
        result[i - 1] = ((i - a) * (b - i)) as Int;
    }
    assert_eq!(result.iter().sum::<Int>(), ((N - 2) * (N - 1) / 2) as Int);
    result
}

fn sub(a: Vector, b: Vector) -> Vector {
    std::array::from_fn(|i| a[i] - b[i])
}

fn determinant(mut a: Vec<Vec<Int>>) -> Int {
    let n = a.len();
    if n == 0 {
        return 1;
    }
    assert!(a.iter().all(|row| row.len() == n));
    let mut sign = 1;
    let mut previous = 1;
    for k in 0..n - 1 {
        let Some(pivot) = (k..n).find(|&r| a[r][k] != 0) else {
            return 0;
        };
        if pivot != k {
            a.swap(k, pivot);
            sign = -sign;
        }
        let p = a[k][k];
        for i in k + 1..n {
            for j in k + 1..n {
                let numerator = a[i][j] * p - a[i][k] * a[k][j];
                assert_eq!(numerator % previous, 0);
                a[i][j] = numerator / previous;
            }
        }
        previous = p;
    }
    sign * a[n - 1][n - 1]
}

fn row_subsets(k: usize) -> Vec<Vec<usize>> {
    fn rec(start: usize, left: usize, chosen: &mut Vec<usize>, out: &mut Vec<Vec<usize>>) {
        if left == 0 {
            out.push(chosen.clone());
            return;
        }
        for i in start..=N - 2 - left {
            chosen.push(i);
            rec(i + 1, left - 1, chosen, out);
            chosen.pop();
        }
    }
    let mut out = Vec::new();
    rec(0, k, &mut Vec::new(), &mut out);
    out
}

fn minor(frame: &[Vector], rows: &[usize]) -> Int {
    determinant(
        rows.iter()
            .map(|&row| frame.iter().map(|v| v[row]).collect())
            .collect(),
    )
}

fn independent(frame: &[Vector]) -> bool {
    frame.is_empty()
        || row_subsets(frame.len())
            .iter()
            .any(|rows| minor(frame, rows) != 0)
}

fn face_vertices(face: &Face, triangulations: &[Triangulation]) -> Vec<usize> {
    triangulations
        .iter()
        .enumerate()
        .filter_map(|(i, t)| face_contains(t, face).then_some(i))
        .collect()
}

fn orientation_basis(vertices: &[usize], points: &[Vector], dim: usize) -> Vec<Vector> {
    if dim == 0 {
        return Vec::new();
    }
    let origin = points[vertices[0]];
    let mut result = Vec::new();
    for &v in &vertices[1..] {
        let candidate = sub(points[v], origin);
        let mut trial = result.clone();
        trial.push(candidate);
        if independent(&trial) {
            result.push(candidate);
            if result.len() == dim {
                break;
            }
        }
    }
    assert_eq!(result.len(), dim);
    result
}

fn incidence(
    face: &Face,
    facet: &Face,
    vertices: &BTreeMap<Face, Vec<usize>>,
    bases: &BTreeMap<Face, Vec<Vector>>,
    points: &[Vector],
) -> Int {
    let d = dimension(face);
    assert_eq!(dimension(facet) + 1, d);
    let fv = &vertices[face];
    let gv = &vertices[facet];
    let mut sum_f = [0; N - 2];
    let mut sum_g = [0; N - 2];
    for &v in fv {
        for i in 0..N - 2 {
            sum_f[i] += points[v][i];
        }
    }
    for &v in gv {
        for i in 0..N - 2 {
            sum_g[i] += points[v][i];
        }
    }
    // From the face centroid toward its facet: an outward normal modulo the
    // facet tangent space. Denominators are cleared by positive integers.
    let outward: Vector =
        std::array::from_fn(|i| fv.len() as Int * sum_g[i] - gv.len() as Int * sum_f[i]);
    let mut boundary_frame = vec![outward];
    boundary_frame.extend(bases[facet].iter().copied());
    let ambient = &bases[face];
    for rows in row_subsets(d) {
        let a = minor(ambient, &rows);
        if a != 0 {
            let b = minor(&boundary_frame, &rows);
            assert_ne!(b, 0);
            return if a.signum() == b.signum() { 1 } else { -1 };
        }
    }
    unreachable!()
}

fn zero_matrix(rows: usize, columns: usize) -> Matrix {
    vec![vec![0; columns]; rows]
}

fn multiply(a: &Matrix, b: &Matrix) -> Matrix {
    if a.is_empty() || b.is_empty() {
        return Vec::new();
    }
    assert_eq!(a[0].len(), b.len());
    let mut out = zero_matrix(a.len(), b[0].len());
    for i in 0..a.len() {
        for k in 0..b.len() {
            if a[i][k] != 0 {
                for j in 0..b[0].len() {
                    out[i][j] += a[i][k] * b[k][j];
                }
            }
        }
    }
    out
}

/// Unit-pivot Smith elimination. A zero remainder certifies that every
/// nonzero invariant factor is exactly one, not merely the rational rank.
fn unit_smith_rank(value: &Matrix) -> usize {
    if value.is_empty() || value[0].is_empty() {
        return 0;
    }
    let mut a = value.clone();
    let rows = a.len();
    let columns = a[0].len();
    let mut p = 0;
    while p < rows && p < columns {
        let found =
            (p..rows).find_map(|i| (p..columns).find(|&j| a[i][j].abs() == 1).map(|j| (i, j)));
        let Some((i0, j0)) = found else { break };
        a.swap(p, i0);
        for row in &mut a {
            row.swap(p, j0);
        }
        if a[p][p] == -1 {
            for x in &mut a[p] {
                *x = -*x;
            }
        }
        for i in 0..rows {
            if i == p {
                continue;
            }
            let q = a[i][p];
            for j in p..columns {
                a[i][j] -= q * a[p][j];
            }
        }
        for j in 0..columns {
            if j == p {
                continue;
            }
            let q = a[p][j];
            for i in 0..rows {
                a[i][j] -= q * a[i][p];
            }
        }
        p += 1;
    }
    assert!(a[p..]
        .iter()
        .all(|row| row[p.min(columns)..].iter().all(|&x| x == 0)));
    p
}

fn cells_by_dimension(all_faces: &[Face], predicate: impl Fn(&Face) -> bool) -> Vec<Vec<Face>> {
    let mut result = vec![Vec::new(); DIM + 1];
    for face in all_faces.iter().filter(|face| predicate(face)) {
        result[dimension(face)].push(face.clone());
    }
    result
}

fn boundary_matrix(
    cells: &[Vec<Face>],
    degree: usize,
    incidences: &[BTreeMap<(Face, Face), Int>],
) -> Matrix {
    let rows: BTreeMap<_, _> = cells[degree - 1]
        .iter()
        .cloned()
        .enumerate()
        .map(|(i, f)| (f, i))
        .collect();
    let mut out = zero_matrix(cells[degree - 1].len(), cells[degree].len());
    for (j, face) in cells[degree].iter().enumerate() {
        for ((source, facet), &coefficient) in &incidences[degree] {
            if source == face {
                if let Some(&i) = rows.get(facet) {
                    out[i][j] = coefficient;
                }
            }
        }
    }
    out
}

fn homology(cells: &[Vec<Face>], boundaries: &[Matrix]) -> (Vec<usize>, Vec<usize>) {
    let counts: Vec<_> = cells.iter().map(Vec::len).collect();
    let mut ranks = vec![0; DIM + 1];
    for d in 1..=DIM {
        ranks[d] = unit_smith_rank(&boundaries[d]);
    }
    let betti = (0..=DIM)
        .map(|d| counts[d] - ranks[d] - if d < DIM { ranks[d + 1] } else { 0 })
        .collect();
    (ranks, betti)
}

fn transform_vertex(i: usize, reflection: bool, shift: usize) -> usize {
    if reflection {
        (shift + N - i) % N
    } else {
        (i + shift) % N
    }
}

fn transform_face(face: &Face, reflection: bool, shift: usize) -> Face {
    let mut result: Face = face
        .iter()
        .map(|e| {
            edge(
                transform_vertex(e.0, reflection, shift),
                transform_vertex(e.1, reflection, shift),
            )
        })
        .collect();
    result.sort();
    result
}

/// Orientation signs for one cellular D8 automorphism, obtained from the
/// already certified signed incidence matrices. Compatibility over every
/// facet is checked rather than assumed from a coordinate symmetry.
fn action_signs(
    all_cells: &[Vec<Face>],
    incidences: &[BTreeMap<(Face, Face), Int>],
    reflection: bool,
    shift: usize,
) -> Vec<BTreeMap<Face, Int>> {
    let mut result = vec![BTreeMap::new(); DIM + 1];
    for face in &all_cells[0] {
        result[0].insert(face.clone(), 1);
    }
    for d in 1..=DIM {
        for face in &all_cells[d] {
            let mut candidate = None;
            for ((source, facet), &a) in &incidences[d] {
                if source != face {
                    continue;
                }
                let image_face = transform_face(face, reflection, shift);
                let image_facet = transform_face(facet, reflection, shift);
                let b = incidences[d][&(image_face, image_facet)];
                let s_facet = result[d - 1][facet];
                let value = a * s_facet / b;
                assert!(value.abs() == 1);
                if let Some(old) = candidate {
                    assert_eq!(old, value, "D8 action must be a chain map");
                } else {
                    candidate = Some(value);
                }
            }
            result[d].insert(face.clone(), candidate.unwrap());
        }
    }
    result
}

fn chain_trace(
    cells: &[Vec<Face>],
    signs: &[BTreeMap<Face, Int>],
    reflection: bool,
    shift: usize,
) -> Vec<Int> {
    (0..=DIM)
        .map(|d| {
            cells[d]
                .iter()
                .filter_map(|face| {
                    (transform_face(face, reflection, shift) == *face).then_some(signs[d][face])
                })
                .sum()
        })
        .collect()
}

fn alternating_trace(trace: &[Int]) -> Int {
    trace
        .iter()
        .enumerate()
        .map(|(d, &x)| if d % 2 == 0 { x } else { -x })
        .sum()
}

fn format_edge(e: Edge) -> String {
    format!("{}{}", e.0, e.1)
}
fn format_face(face: &Face) -> String {
    face.iter()
        .map(|&e| format_edge(e))
        .collect::<Vec<_>>()
        .join(".")
}

fn physical_diagonal(i: usize) -> Edge {
    edge(i % N, (i + 3) % N)
}

fn physical_label(e: Edge) -> usize {
    (0..N).find(|&i| physical_diagonal(i) == e).unwrap()
}

fn graph_cycle(vertices: &[usize], graph_edges: &[(usize, usize)]) -> Vec<Int> {
    let edge_index: BTreeMap<_, _> = graph_edges
        .iter()
        .copied()
        .enumerate()
        .map(|(i, e)| (e, i))
        .collect();
    let mut result = vec![0; graph_edges.len()];
    for i in 0..vertices.len() {
        let a = vertices[i];
        let b = vertices[(i + 1) % vertices.len()];
        let oriented = if a < b { (a, b) } else { (b, a) };
        let coefficient = if a < b { 1 } else { -1 };
        result[edge_index[&oriented]] += coefficient;
    }
    result
}

fn graph_boundary(chain: &[Int], graph_edges: &[(usize, usize)]) -> Vec<Int> {
    let mut result = vec![0; N];
    for (&coefficient, &(a, b)) in chain.iter().zip(graph_edges) {
        result[a] -= coefficient;
        result[b] += coefficient;
    }
    result
}

fn graph_transform_chain(
    chain: &[Int],
    graph_edges: &[(usize, usize)],
    reflection: bool,
    shift: usize,
) -> Vec<Int> {
    let edge_index: BTreeMap<_, _> = graph_edges
        .iter()
        .copied()
        .enumerate()
        .map(|(i, e)| (e, i))
        .collect();
    let vertex_image: Vec<_> = (0..N)
        .map(|i| physical_label(transform_face(&vec![physical_diagonal(i)], reflection, shift)[0]))
        .collect();
    let mut result = vec![0; graph_edges.len()];
    for (i, &(a, b)) in graph_edges.iter().enumerate() {
        let x = vertex_image[a];
        let y = vertex_image[b];
        let target = if x < y { (x, y) } else { (y, x) };
        result[edge_index[&target]] += chain[i] * if x < y { 1 } else { -1 };
    }
    result
}

fn find(parent: &mut [usize], x: usize) -> usize {
    if parent[x] != x {
        parent[x] = find(parent, parent[x]);
    }
    parent[x]
}

fn main() {
    let triangulations = triangulations();
    let all_diagonals = diagonals();
    let all_faces = faces(&triangulations);
    assert_eq!(
        (triangulations.len(), all_diagonals.len(), all_faces.len()),
        (132, 20, 903)
    );
    assert_eq!(all_diagonals.iter().filter(|&&e| physical(e)).count(), 8);

    let points: Vec<_> = triangulations.iter().map(loday).collect();
    let vertices: BTreeMap<_, _> = all_faces
        .iter()
        .cloned()
        .map(|face| {
            let vs = face_vertices(&face, &triangulations);
            (face, vs)
        })
        .collect();
    let bases: BTreeMap<_, _> = all_faces
        .iter()
        .cloned()
        .map(|face| {
            let basis = orientation_basis(&vertices[&face], &points, dimension(&face));
            (face, basis)
        })
        .collect();

    let mut incidences = vec![BTreeMap::new(); DIM + 1];
    for face in &all_faces {
        let d = dimension(face);
        if d == 0 {
            continue;
        }
        for &e in &all_diagonals {
            if !contains(face, e) {
                let facet = add_edge(face, e);
                if compatible(&facet) {
                    let coefficient = incidence(face, &facet, &vertices, &bases, &points);
                    assert!(coefficient.abs() == 1);
                    incidences[d].insert((face.clone(), facet), coefficient);
                }
            }
        }
    }

    let k_cells = cells_by_dimension(&all_faces, |_| true);
    let b_cells = cells_by_dimension(&all_faces, |face| face.iter().any(|&e| physical(e)));
    let relative_cells = cells_by_dimension(&all_faces, |face| face.iter().all(|&e| !physical(e)));
    let k_counts: Vec<_> = k_cells.iter().map(Vec::len).collect();
    let b_counts: Vec<_> = b_cells.iter().map(Vec::len).collect();
    let relative_counts: Vec<_> = relative_cells.iter().map(Vec::len).collect();
    assert_eq!(k_counts, vec![132, 330, 300, 120, 20, 1]);
    assert!((0..=DIM).all(|d| b_counts[d] + relative_counts[d] == k_counts[d]));

    // B_cut is closed under passage to cellular boundary.
    for d in 1..=DIM {
        for face in &b_cells[d] {
            for ((source, facet), _) in &incidences[d] {
                if source == face {
                    assert!(facet.iter().any(|&e| physical(e)));
                }
            }
        }
    }

    let make_boundaries = |cells: &[Vec<Face>]| {
        let mut result = vec![Vec::new(); DIM + 1];
        for d in 1..=DIM {
            result[d] = boundary_matrix(cells, d, &incidences);
        }
        for d in 2..=DIM {
            let square = multiply(&result[d - 1], &result[d]);
            assert!(square.iter().flatten().all(|&x| x == 0));
        }
        result
    };
    let k_boundaries = make_boundaries(&k_cells);
    let b_boundaries = make_boundaries(&b_cells);
    let relative_boundaries = make_boundaries(&relative_cells);
    let (k_ranks, k_betti) = homology(&k_cells, &k_boundaries);
    let (b_ranks, b_betti) = homology(&b_cells, &b_boundaries);
    let (relative_ranks, relative_betti) = homology(&relative_cells, &relative_boundaries);
    assert_eq!(k_betti, vec![1, 0, 0, 0, 0, 0]);
    assert_eq!(b_betti, vec![1, 5, 0, 0, 0, 0]);
    assert_eq!(relative_betti, vec![0, 0, 5, 0, 0, 0]);

    // The eight cut facets form a good cellular cover of B_cut.  Compatible
    // pairs have nonempty associahedral-face intersections; no compatible
    // triple exists. Thus its nerve is the 8-vertex, 12-edge Möbius ladder.
    let physicals: Vec<_> = (0..N).map(physical_diagonal).collect();
    assert_eq!(physicals.iter().copied().collect::<BTreeSet<_>>().len(), N);
    let mut graph_edges = Vec::new();
    for i in 0..N {
        for j in i + 1..N {
            if !crosses(physicals[i], physicals[j]) {
                graph_edges.push((i, j));
            }
        }
    }
    assert_eq!(graph_edges.len(), 12);
    for i in 0..N {
        let neighbors: BTreeSet<_> = graph_edges
            .iter()
            .filter_map(|&(a, b)| {
                if a == i {
                    Some(b)
                } else if b == i {
                    Some(a)
                } else {
                    None
                }
            })
            .collect();
        assert_eq!(
            neighbors,
            [((i + 3) % N), ((i + 4) % N), ((i + 5) % N)]
                .iter()
                .copied()
                .collect()
        );
    }
    let mut compatible_triples = 0;
    for i in 0..N {
        for j in i + 1..N {
            for k in j + 1..N {
                if !crosses(physicals[i], physicals[j])
                    && !crosses(physicals[i], physicals[k])
                    && !crosses(physicals[j], physicals[k])
                {
                    compatible_triples += 1;
                }
            }
        }
    }
    assert_eq!(compatible_triples, 0);

    // A graph spanning tree identifies its integral cycle lattice with the
    // five chord coordinates. This makes saturation and index statements
    // genuine Z-lattice calculations rather than rational rank counts.
    let mut parent: Vec<_> = (0..N).collect();
    let mut chords = Vec::new();
    for (index, &(a, b)) in graph_edges.iter().enumerate() {
        let ra = find(&mut parent, a);
        let rb = find(&mut parent, b);
        if ra != rb {
            parent[ra] = rb;
        } else {
            chords.push(index);
        }
    }
    assert_eq!(chords.len(), 5);
    let outer_vertices: Vec<_> = (0..N).map(|j| (3 * j) % N).collect();
    let outer_cycle = graph_cycle(&outer_vertices, &graph_edges);
    assert!(graph_boundary(&outer_cycle, &graph_edges)
        .iter()
        .all(|&x| x == 0));
    let square_vertices: Vec<Vec<usize>> = (0..4)
        .map(|j| {
            let q = |offset: usize| (3 * (j + offset)) % N;
            vec![q(0), q(1), q(5), q(4)]
        })
        .collect();
    let square_cycles: Vec<_> = square_vertices
        .iter()
        .map(|v| graph_cycle(v, &graph_edges))
        .collect();
    assert!(square_cycles
        .iter()
        .all(|c| graph_boundary(c, &graph_edges).iter().all(|&x| x == 0)));
    let square_chords: Matrix = chords
        .iter()
        .map(|&row| square_cycles.iter().map(|c| c[row]).collect())
        .collect();
    assert_eq!(unit_smith_rank(&square_chords), 4); // saturated rank-four sublattice
    let full_chords: Matrix = chords
        .iter()
        .map(|&row| {
            square_cycles
                .iter()
                .map(|c| c[row])
                .chain(std::iter::once(outer_cycle[row]))
                .collect()
        })
        .collect();
    let local_plus_outer_index = determinant(full_chords).abs();
    assert_eq!(local_plus_outer_index, 2);

    // Degreewise exact cellular recollement. The relative/Borel--Moore
    // carrier is a quotient complex, not the free module on missed vertices.
    for d in 0..=DIM {
        assert_eq!(k_cells[d].len(), b_cells[d].len() + relative_cells[d].len());
    }
    assert_eq!(relative_cells[0].len(), 4);
    assert_eq!(relative_ranks[1], 4); // all four free occurrence classes attach
    assert_eq!(relative_betti[0], 0);

    let zero_core: Vec<_> = relative_cells[0].iter().cloned().collect();
    let zero_core_indices: Vec<_> = zero_core
        .iter()
        .map(|face| triangulations.binary_search(face).unwrap())
        .collect();
    assert_eq!(zero_core_indices, vec![16, 24, 96, 100]);

    // Each zero-core chart has four one-flip exits to cut facets. Their four
    // cut labels are exactly one of the four squares in the Möbius nerve.
    let square_vertex_sets: BTreeSet<_> = square_vertices
        .iter()
        .map(|cycle| cycle.iter().copied().collect::<BTreeSet<_>>())
        .collect();
    let mut zero_chart_squares = Vec::new();
    for zero in &zero_core {
        let zero_index = triangulations.binary_search(zero).unwrap();
        let mut exits = BTreeSet::new();
        for one_cell in &relative_cells[1] {
            if !face_contains(zero, one_cell) {
                continue;
            }
            let endpoints = &vertices[one_cell];
            assert_eq!(endpoints.len(), 2);
            let other = *endpoints.iter().find(|&&i| i != zero_index).unwrap();
            let cuts: Vec<_> = triangulations[other]
                .iter()
                .copied()
                .filter(|&e| physical(e))
                .collect();
            if cuts.len() == 1 {
                exits.insert(physical_label(cuts[0]));
            } else {
                assert!(cuts.is_empty());
            }
        }
        assert_eq!(exits.len(), 4);
        assert!(square_vertex_sets.contains(&exits));
        zero_chart_squares.push((zero_index, exits));
    }
    assert_eq!(
        zero_chart_squares
            .iter()
            .map(|(_, s)| s.clone())
            .collect::<BTreeSet<_>>()
            .len(),
        4
    );

    let relative_row: BTreeMap<_, _> = relative_cells[0]
        .iter()
        .cloned()
        .enumerate()
        .map(|(i, f)| (f, i))
        .collect();
    let mut attachments = Vec::new();
    for (j, one_cell) in relative_cells[1].iter().enumerate() {
        let support: Vec<_> = zero_core
            .iter()
            .filter_map(|v| {
                let i = relative_row[v];
                let c = relative_boundaries[1][i][j];
                (c != 0).then_some((triangulations.binary_search(v).unwrap(), c))
            })
            .collect();
        if !support.is_empty() {
            attachments.push((format_face(one_cell), support));
        }
    }
    assert!(
        attachments
            .iter()
            .flat_map(|(_, s)| s)
            .map(|(i, _)| *i)
            .collect::<BTreeSet<_>>()
            .len()
            == 4
    );

    // D8 cellular action and equivariant connecting isomorphism. Since K is
    // contractible, delta: H_2(K,B) -> H_1(B) is an isomorphism. We compute
    // both characters independently from cellular Lefschetz traces.
    let mut character = Vec::new();
    let mut relative_character = Vec::new();
    let mut d8_zero_orbits = BTreeSet::new();
    for reflection in [false, true] {
        for shift in 0..N {
            let signs = action_signs(&k_cells, &incidences, reflection, shift);
            let k_trace = chain_trace(&k_cells, &signs, reflection, shift);
            let b_trace = chain_trace(&b_cells, &signs, reflection, shift);
            let q_trace = chain_trace(&relative_cells, &signs, reflection, shift);
            assert_eq!(alternating_trace(&k_trace), 1);
            let h1_b = 1 - alternating_trace(&b_trace);
            let h2_q = alternating_trace(&q_trace);
            assert_eq!(h1_b, h2_q);
            // Independent nerve-graph trace.
            let vertex_image: Vec<_> = (0..N)
                .map(|i| {
                    physical_label(
                        transform_face(&vec![physical_diagonal(i)], reflection, shift)[0],
                    )
                })
                .collect();
            let graph_c0_trace: Int = (0..N).filter(|&i| vertex_image[i] == i).count() as Int;
            let graph_c1_trace: Int = graph_edges
                .iter()
                .map(|&(a, b)| {
                    let x = vertex_image[a];
                    let y = vertex_image[b];
                    let image = if x < y { (x, y) } else { (y, x) };
                    if image == (a, b) {
                        if x < y {
                            1
                        } else {
                            -1
                        }
                    } else {
                        0
                    }
                })
                .sum();
            let graph_h1 = 1 - graph_c0_trace + graph_c1_trace;
            assert_eq!(h1_b, graph_h1);
            character.push((reflection, shift, h1_b));
            relative_character.push(h2_q);
            for face in &zero_core {
                d8_zero_orbits.insert(transform_face(face, reflection, shift));
            }
        }
    }
    assert_eq!(d8_zero_orbits.len(), 4);
    assert_eq!(character[0].2, 5);
    assert_eq!(
        character
            .iter()
            .filter(|(reflection, _, _)| !reflection)
            .map(|x| x.2)
            .collect::<Vec<_>>(),
        vec![5, 1, 1, 1, -3, 1, 1, 1]
    );
    assert!(character
        .iter()
        .filter(|(reflection, _, _)| *reflection)
        .all(|x| x.2 == -1));

    // D8 permutes the four local squares (with orientation) and acts on the
    // outer octagon by the global orientation character. Since the square
    // lattice is saturated and outer=2 times a quotient generator, the
    // residual integral quotient is a primitive orientation line.
    for reflection in [false, true] {
        for shift in 0..N {
            let transformed_outer =
                graph_transform_chain(&outer_cycle, &graph_edges, reflection, shift);
            let expected_outer: Vec<_> = outer_cycle
                .iter()
                .map(|&x| if reflection { -x } else { x })
                .collect();
            assert_eq!(transformed_outer, expected_outer);
            for square in &square_cycles {
                let transformed = graph_transform_chain(square, &graph_edges, reflection, shift);
                assert!(square_cycles.iter().any(|candidate| {
                    transformed == *candidate
                        || transformed.iter().zip(candidate).all(|(a, b)| *a == -*b)
                }));
            }
        }
    }

    // Multiplicity of the global orientation character (r -> +1, reflection
    // -> -1) inside the five-dimensional D8 module. This detects an
    // orientation-odd line, but does not identify it with the additional
    // polarity/core character carried by a local road costalk.
    let orientation_multiplicity_numerator: Int = character
        .iter()
        .map(|&(reflection, _, chi)| chi * if reflection { -1 } else { 1 })
        .sum();
    assert_eq!(orientation_multiplicity_numerator % 16, 0);
    let orientation_multiplicity = orientation_multiplicity_numerator / 16;

    println!("n=8 integral cut recollement audit: PASS");
    println!("K_cell_counts={k_counts:?} K_boundary_smith_ranks={k_ranks:?} K_homology_betti={k_betti:?} torsion=none");
    println!("B_cut_cell_counts={b_counts:?} B_boundary_smith_ranks={b_ranks:?} B_homology_betti={b_betti:?} torsion=none");
    println!("relative_cell_counts={relative_counts:?} relative_boundary_smith_ranks={relative_ranks:?} relative_homology_betti={relative_betti:?} torsion=none");
    println!("degreewise_short_exact_recollement=PASS BM_open_carrier=C_*(K5,B_cut)");
    println!(
        "zero_core_vertex_indices={zero_core_indices:?} D8_orbit_size={}",
        d8_zero_orbits.len()
    );
    println!("cut_nerve=Mobius_ladder_Gamma8 vertices=8 edges=12 triangles=0 good_intersections=associahedral_faces");
    println!("zero_core_chart_to_nerve_squares={zero_chart_squares:?}");
    println!("local_square_lattice_rank=4 saturated=true quotient=Z outer_octagon_quotient_multiple=2 combined_index={local_plus_outer_index}");
    println!(
        "zero_core_relative_d1_rank={} zero_core_H0=0",
        relative_ranks[1]
    );
    println!("zero_core_attaching_columns={attachments:?}");
    println!("D8_H1_B_equals_H2_relative_character={character:?}");
    println!("orientation_character_multiplicity={orientation_multiplicity}");
    println!("D8_module_over_Q=orientation_line_plus_V1_plus_V3 integral_square_quotient_character=orientation");
    println!("connecting_delta_H2_relative_to_H1_B=equivariant_isomorphism_rank5");
    println!("chi_N_identification=NOT_TYPED entry66_sigma_alt_identification=NOT_TYPED");
}
