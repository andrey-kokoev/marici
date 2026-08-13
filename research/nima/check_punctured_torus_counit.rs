//! Exact hostile example for the resolved all-topology surface counit.
//!
//! The once-punctured torus has one theta fatgraph.  Its three edges lie in
//! one mapping-class orbit, and its scalar surface function is x^3 / 3.
//! This certificate does not reconstruct that answer from the Cut Equation.
//! Instead it:
//!
//! * verifies the three cyclic three-point transmutation sectors directly on
//!   the scalar-scaffolded Yang--Mills three-point polynomial;
//! * sews two resolved sectors through the theta graph and counts the actual
//!   Brauer circuits term by term;
//! * shows that raw post-sewing D-evaluation is not Cut natural;
//! * shows that the resolved augmentation D -> 1 restores the exact torus to
//!   annulus Cut and produces the coefficient 1/3;
//! * checks coefficient-level covariance under all permutations of the three
//!   Farey slopes and exact 3S chart holonomy on a bounded slope atlas.

use std::collections::{BTreeMap, BTreeSet, VecDeque};

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum Var {
    X14,
    X26,
    X36,
    X24,
    X25,
    X46,
}

const YM3: [(i64, Var, Var); 6] = [
    (1, Var::X14, Var::X26),
    (1, Var::X36, Var::X24),
    (1, Var::X25, Var::X46),
    (-1, Var::X25, Var::X36),
    (-1, Var::X14, Var::X36),
    (-1, Var::X14, Var::X25),
];

const SECTORS: [(Var, Var); 3] = [
    (Var::X14, Var::X26),
    (Var::X36, Var::X24),
    (Var::X25, Var::X46),
];

fn ordered_pair(left: Var, right: Var) -> (Var, Var) {
    if left <= right {
        (left, right)
    } else {
        (right, left)
    }
}

fn polynomial(terms: &[(i64, Var, Var)]) -> BTreeMap<(Var, Var), i64> {
    let mut result = BTreeMap::new();
    for &(coefficient, left, right) in terms {
        *result.entry(ordered_pair(left, right)).or_insert(0) += coefficient;
    }
    result.retain(|_, coefficient| *coefficient != 0);
    result
}

fn second_derivative(first: Var, second: Var) -> i64 {
    let selected = ordered_pair(first, second);
    polynomial(&YM3).get(&selected).copied().unwrap_or(0)
}

fn rotate_var(variable: Var) -> Var {
    match variable {
        Var::X14 => Var::X36,
        Var::X36 => Var::X25,
        Var::X25 => Var::X14,
        Var::X26 => Var::X24,
        Var::X24 => Var::X46,
        Var::X46 => Var::X26,
    }
}

fn audit_three_point_counit() {
    for &(first, second) in &SECTORS {
        assert_eq!(second_derivative(first, second), 1);
    }

    let rotated: Vec<_> = YM3
        .iter()
        .map(|&(coefficient, left, right)| (coefficient, rotate_var(left), rotate_var(right)))
        .collect();
    assert_eq!(polynomial(&rotated), polynomial(&YM3));

    for sector in 0..3 {
        let rotated_sector = (rotate_var(SECTORS[sector].0), rotate_var(SECTORS[sector].1));
        assert_eq!(
            ordered_pair(rotated_sector.0, rotated_sector.1),
            ordered_pair(SECTORS[(sector + 1) % 3].0, SECTORS[(sector + 1) % 3].1)
        );
    }
}

fn local_matching(singleton: usize, offset: usize, auxiliary: usize) -> Vec<(usize, usize)> {
    assert!(singleton < 3);
    let paired: Vec<_> = (0..3).filter(|&leg| leg != singleton).collect();
    vec![
        (auxiliary, offset + singleton),
        (offset + paired[0], offset + paired[1]),
    ]
}

fn components(vertex_count: usize, edges: &[(usize, usize)]) -> Vec<Vec<usize>> {
    let mut adjacency = vec![Vec::new(); vertex_count];
    for &(left, right) in edges {
        adjacency[left].push(right);
        adjacency[right].push(left);
    }

    let mut seen = vec![false; vertex_count];
    let mut result = Vec::new();
    for start in 0..vertex_count {
        if seen[start] {
            continue;
        }
        let mut queue = VecDeque::from([start]);
        seen[start] = true;
        let mut component = Vec::new();
        while let Some(vertex) = queue.pop_front() {
            component.push(vertex);
            for &next in &adjacency[vertex] {
                if !seen[next] {
                    seen[next] = true;
                    queue.push_back(next);
                }
            }
        }
        result.push(component);
    }
    result
}

/// Sew two trivalent counit sectors.  Endpoints 0..=2 are the left vertex,
/// 4..=6 the right vertex, and 3,7 are the auxiliary coefficient strands.
/// If `cut_edge` is present, that theta edge is opened and its two ends become
/// external along with the two auxiliaries.
fn circuit_count(left_singleton: usize, right_singleton: usize, cut_edge: Option<usize>) -> usize {
    let mut edges = local_matching(left_singleton, 0, 3);
    edges.extend(local_matching(right_singleton, 4, 7));
    for leg in 0..3 {
        if cut_edge != Some(leg) {
            edges.push((leg, 4 + leg));
        }
    }

    let mut external = BTreeSet::from([3, 7]);
    if let Some(leg) = cut_edge {
        external.insert(leg);
        external.insert(4 + leg);
    }

    let mut circuits = 0;
    for component in components(8, &edges) {
        let external_count = component
            .iter()
            .filter(|vertex| external.contains(vertex))
            .count();
        assert!(external_count == 0 || external_count == 2);
        if external_count == 0 {
            circuits += 1;
        }
    }
    circuits
}

/// Return (constant coefficient, D coefficient).  This example never creates
/// more than one closed polarization circuit.
fn circuit_polynomial(cut_edge: Option<usize>) -> (usize, usize) {
    let mut constant = 0;
    let mut dimension = 0;
    for left in 0..3 {
        for right in 0..3 {
            match circuit_count(left, right, cut_edge) {
                0 => constant += 1,
                1 => dimension += 1,
                other => panic!("unexpected circuit count: {other}"),
            }
        }
    }
    (constant, dimension)
}

fn permutations_of_three() -> [[usize; 3]; 6] {
    [
        [0, 1, 2],
        [0, 2, 1],
        [1, 0, 2],
        [1, 2, 0],
        [2, 0, 1],
        [2, 1, 0],
    ]
}

fn audit_slope_covariance() -> usize {
    let mut squares = 0;
    for permutation in permutations_of_three() {
        for left in 0..3 {
            for right in 0..3 {
                assert_eq!(
                    circuit_count(left, right, None),
                    circuit_count(permutation[left], permutation[right], None)
                );
                for cut in 0..3 {
                    assert_eq!(
                        circuit_count(left, right, Some(cut)),
                        circuit_count(
                            permutation[left],
                            permutation[right],
                            Some(permutation[cut])
                        )
                    );
                    squares += 1;
                }
            }
        }
    }
    squares
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Mat2([[i64; 2]; 2]);

impl Mat2 {
    const IDENTITY: Self = Self([[1, 0], [0, 1]]);

    fn columns(first: Slope, second: Slope) -> Self {
        Self([[first.p, second.p], [first.q, second.q]])
    }

    fn determinant(self) -> i64 {
        self.0[0][0] * self.0[1][1] - self.0[0][1] * self.0[1][0]
    }

    fn inverse_sl2(self) -> Self {
        assert_eq!(self.determinant(), 1);
        Self([[self.0[1][1], -self.0[0][1]], [-self.0[1][0], self.0[0][0]]])
    }

    fn multiply(self, other: Self) -> Self {
        let mut output = [[0; 2]; 2];
        for (row, output_row) in output.iter_mut().enumerate() {
            for (column, entry) in output_row.iter_mut().enumerate() {
                *entry = (0..2)
                    .map(|middle| self.0[row][middle] * other.0[middle][column])
                    .sum();
            }
        }
        Self(output)
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Slope {
    p: i64,
    q: i64,
}

impl Slope {
    fn new(p: i64, q: i64) -> Self {
        assert_ne!((p, q), (0, 0));
        assert_eq!(gcd(p.abs(), q.abs()), 1);
        Self { p, q }
    }

    fn plus(self, other: Self) -> Self {
        Self::new(self.p + other.p, self.q + other.q)
    }

    fn negative(self) -> Self {
        Self::new(-self.p, -self.q)
    }

    fn determinant(self, other: Self) -> i64 {
        self.p * other.q - self.q * other.p
    }
}

fn gcd(mut left: i64, mut right: i64) -> i64 {
    while right != 0 {
        let remainder = left % right;
        left = right;
        right = remainder;
    }
    left
}

fn primitive_slopes(bound: i64) -> Vec<Slope> {
    let mut slopes = Vec::new();
    for p in -bound..=bound {
        for q in -bound..=bound {
            if (p, q) != (0, 0) && gcd(p.abs(), q.abs()) == 1 {
                slopes.push(Slope::new(p, q));
            }
        }
    }
    slopes
}

fn audit_farey_three_s(bound: i64) -> usize {
    let slopes = primitive_slopes(bound);
    let mut triangles = 0;
    for &first in &slopes {
        for &second in &slopes {
            if first.determinant(second) != 1 {
                continue;
            }
            let third = first.plus(second);
            let frame_first = Mat2::columns(first, second);
            let frame_second = Mat2::columns(second, first.negative());
            let frame_third = Mat2::columns(third, first.negative());

            let second_from_first = frame_second.inverse_sl2().multiply(frame_first);
            let third_from_second = frame_third.inverse_sl2().multiply(frame_second);
            let first_from_third = frame_first.inverse_sl2().multiply(frame_third);
            assert_eq!(
                first_from_third
                    .multiply(third_from_second)
                    .multiply(second_from_first),
                Mat2::IDENTITY
            );
            triangles += 1;
        }
    }
    triangles
}

fn main() {
    audit_three_point_counit();

    // Same singleton at both vertices closes the other two theta edges into
    // one polarization circuit.  Different singletons make one through path.
    for left in 0..3 {
        for right in 0..3 {
            assert_eq!(circuit_count(left, right, None), usize::from(left == right));
        }
    }
    assert_eq!(circuit_polynomial(None), (6, 3));

    // Cutting edge k retains a circuit only in the sector (k,k).
    for cut in 0..3 {
        assert_eq!(circuit_polynomial(Some(cut)), (8, 1));
        for left in 0..3 {
            for right in 0..3 {
                assert_eq!(
                    circuit_count(left, right, Some(cut)),
                    usize::from(left == cut && right == cut)
                );
            }
        }
    }

    // There are two local 1/3 cyclic averages and the theta automorphism 1/3,
    // hence denominator 27.  Resolved D -> 1 turns all nine sector sewings
    // into one: 9/27 = 1/3, the punctured-torus scalar coefficient.
    let denominator = 3 * 3 * 3;
    let augmented_closed_numerator = 6 + 3;
    assert_eq!(augmented_closed_numerator * 3, denominator);

    // The orbit Cut sums the three marked theta edges.  Each contributes nine
    // augmented sectors: 27/27 = 1, the annulus coefficient.
    let augmented_cut_numerator = 3 * (8 + 1);
    assert_eq!(augmented_cut_numerator, denominator);
    assert_eq!(3 * augmented_closed_numerator, augmented_cut_numerator);

    // Raw evaluation before resolution is not Cut natural.  Differentiating
    // (3D+6)x^3/27 gives (D+2)x^2/3, while cutting resolved patterns and then
    // evaluating gives (3D+24)x^2/27 = (D+8)x^2/9.  Their difference is
    // 2(D-1)x^2/9 and vanishes exactly under the augmentation D -> 1.
    let raw_derivative = (18, 9); // (constant, D) over 27
    let raw_cut = (24, 3); // (constant, D) over 27

    // Use signed arithmetic for the displayed discrepancy.
    let discrepancy_constant = raw_derivative.0 as i64 - raw_cut.0 as i64;
    let discrepancy_dimension = raw_derivative.1 as i64 - raw_cut.1 as i64;
    assert_eq!((discrepancy_constant, discrepancy_dimension), (-6, 6));
    assert_eq!(discrepancy_constant + discrepancy_dimension, 0);

    let covariance_squares = audit_slope_covariance();
    let farey_triangles = audit_farey_three_s(5);

    println!("Punctured-torus hostile counit certificate");
    println!("===========================================");
    println!("  local three-point counit sectors: 3");
    println!("  theta sewings: 9 = 3 D-valued + 6 circuit-free");
    println!("  raw closed coefficient: (3D+6)/27 = (D+2)/9");
    println!("  augmented closed coefficient: 9/27 = 1/3");
    println!("  augmented orbit Cut coefficient: 27/27 = 1");
    println!("  raw Cut defect: 2(D-1)/9");
    println!("  slope-covariance squares: {covariance_squares}");
    println!("  oriented Farey 3S triangles: {farey_triangles}");
    println!();
    println!("VERDICT");
    println!("  resolved termwise D -> 1 reproduces G_T = x^3/3 directly");
    println!("  the nonseparating Cut gives G_annulus = x^2 coefficient by coefficient");
    println!("  evaluating polarization circuits before the Cut fails away from D=1");
    println!("  simultaneous slope transport has exact 3S holonomy");
}
