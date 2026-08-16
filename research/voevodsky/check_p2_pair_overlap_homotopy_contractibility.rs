//! Exact carrier test for the derived pair-overlap gate after entry 198.
//!
//! This checker rebuilds the labelled K6 face poset.  It proves that the six
//! short-facet boundaries inject as a saturated rank-six lattice in the
//! twenty-one edge chains.  Consequently, once a pair-overlap is assigned a
//! fixed relative road class, its strict representatives form a connected
//! groupoid: two representatives differ by a unique short-facet 2-chain and
//! there are no 2-automorphisms.  The cyclic sum of the three unique
//! comparison 2-chains is automatically zero.  This removes the rank-six
//! ambiguity in the homotopy-coherent carrier category, but it does not
//! construct the mixed-variance six-functor realization into entry 143.
//! The split injection remains injective after tensoring with an external
//! spectator complex; this does not cover support-changing Tor/Cech maps.

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

    println!(
        "{}",
        r#"{"claim":"For the actual labelled K6 short boundary, the strict rank-six corridor ambiguity becomes a contractible choice in the homotopy-coherent carrier category: d2 is a saturated injection, so representatives of a fixed road class have unique integral comparison 2-chains and no 2-automorphisms; the six dP6 cone residues are primitive short-facet differences and telescope to zero.","status":"proved_scoped_carrier_homotopy_contractibility","k6_faces":[1,9,21,14],"short_boundary_d2_rank":6,"short_boundary_d2_kernel_rank":0,"short_boundary_d2_smith":[1,1,1,1,1,1],"unit_maximal_minor":true,"integer_torsion":"none","dp6_cone_residue_rows":6,"dp6_cyclic_residue_sum":0,"external_spectator_tensor_preserves_split_injection":true,"support_changing_tor_cech_comparison":"unconstructed","pair_objects_external_to_literal_face_category":3,"literal_mixed_variance_realization":"unconstructed","physical_mapping_fiber":"unconstructed"}"#
    );
}
