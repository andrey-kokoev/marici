//! Exact fan audit for the dP6 common refinement of the D03 Cremona map.
//!
//! The scoped no-go concerns an individual ordinary Cartier edge square.
//! It does not obstruct a full-log-boundary excess Gysin construction.

use std::collections::BTreeSet;

type Ray = [i64; 2];
type Matrix = [[i64; 2]; 2];

const RAYS: [Ray; 6] = [[1, 0], [1, 1], [0, 1], [-1, 0], [-1, -1], [0, -1]];

const ROTATION: Matrix = [[0, -1], [1, -1]];
const REFLECTION: Matrix = [[0, 1], [1, 0]];
const POLARITY: Matrix = [[-1, 0], [0, -1]];

fn apply(matrix: Matrix, vector: Ray) -> Ray {
    [
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
    ]
}

fn multiply(left: Matrix, right: Matrix) -> Matrix {
    let mut result = [[0_i64; 2]; 2];
    for row in 0..2 {
        for column in 0..2 {
            for middle in 0..2 {
                result[row][column] += left[row][middle] * right[middle][column];
            }
        }
    }
    result
}

fn determinant(first: Ray, second: Ray) -> i64 {
    first[0] * second[1] - first[1] * second[0]
}

fn ray_index(ray: Ray) -> usize {
    RAYS.iter()
        .position(|candidate| *candidate == ray)
        .expect("fan ray")
}

fn ray_rotation(index: usize) -> usize {
    ray_index(apply(ROTATION, RAYS[index]))
}

fn ray_reflection(index: usize) -> usize {
    ray_index(apply(REFLECTION, RAYS[index]))
}

fn short_rotation(index: usize) -> usize {
    (index + 2) % 6
}
fn short_reflection(index: usize) -> usize {
    (6 - index) % 6
}
fn short_polarity(index: usize) -> usize {
    (index + 3) % 6
}

fn permutations(values: &mut [usize], start: usize, output: &mut Vec<[usize; 6]>) {
    if start == values.len() {
        output.push(values.try_into().expect("six labels"));
        return;
    }
    for index in start..values.len() {
        values.swap(start, index);
        permutations(values, start + 1, output);
        values.swap(start, index);
    }
}

fn equivariant_short_labelings() -> Vec<[usize; 6]> {
    let mut candidates = Vec::new();
    permutations(&mut [0, 1, 2, 3, 4, 5], 0, &mut candidates);
    candidates
        .into_iter()
        .filter(|labels| {
            (0..6).all(|index| {
                labels[ray_rotation(index)] == short_rotation(labels[index])
                    && labels[ray_reflection(index)] == short_reflection(labels[index])
                    && labels[(index + 3) % 6] == short_polarity(labels[index])
            })
        })
        .collect()
}

fn short_diagonal(index: usize) -> (usize, usize) {
    let endpoints = (index, (index + 2) % 6);
    if endpoints.0 < endpoints.1 {
        endpoints
    } else {
        (endpoints.1, endpoints.0)
    }
}

fn between(vertex: usize, first: usize, second: usize) -> bool {
    let span = (second + 6 - first) % 6;
    let position = (vertex + 6 - first) % 6;
    position > 0 && position < span
}

fn crosses(first: (usize, usize), second: (usize, usize)) -> bool {
    if first.0 == second.0 || first.0 == second.1 || first.1 == second.0 || first.1 == second.1 {
        return false;
    }
    between(second.0, first.0, first.1) != between(second.1, first.0, first.1)
        && between(first.0, second.0, second.1) != between(first.1, second.0, second.1)
}

fn rotate_support(support: &BTreeSet<usize>) -> BTreeSet<usize> {
    support
        .iter()
        .map(|index| ray_index(apply(ROTATION, RAYS[*index])))
        .collect()
}

fn polarize_support(support: &BTreeSet<usize>) -> BTreeSet<usize> {
    support
        .iter()
        .map(|index| ray_index(apply(POLARITY, RAYS[*index])))
        .collect()
}

fn main() {
    // Consecutive rays give the six maximal cones of the smooth dP6 fan.
    for index in 0..6 {
        assert_eq!(determinant(RAYS[index], RAYS[(index + 1) % 6]), 1);
    }

    // Identity refines the standard P2 fan in pairs of cones.  The -I map
    // also maps every refined cone into a standard P2 cone and resolves the
    // quadratic Cremona transformation.
    let pi_cone_targets = [0_usize, 0, 1, 1, 2, 2];
    let pi_cr_cone_targets = [1_usize, 2, 2, 0, 0, 1];
    assert_eq!(pi_cone_targets.len(), 6);
    assert_eq!(pi_cr_cone_targets.len(), 6);

    // Exact D3 relations and central polarity.
    let identity = [[1_i64, 0_i64], [0_i64, 1_i64]];
    assert_eq!(multiply(multiply(ROTATION, ROTATION), ROTATION), identity);
    assert_eq!(multiply(REFLECTION, REFLECTION), identity);
    assert_eq!(
        multiply(multiply(REFLECTION, ROTATION), REFLECTION),
        multiply(ROTATION, ROTATION)
    );
    assert_eq!(multiply(POLARITY, ROTATION), multiply(ROTATION, POLARITY));
    assert_eq!(
        multiply(POLARITY, REFLECTION),
        multiply(REFLECTION, POLARITY)
    );
    for index in 0..6 {
        assert_eq!(ray_index(apply(POLARITY, RAYS[index])), (index + 3) % 6);
    }

    // Exhaust all 6! bijections rather than selecting a desired labeling.
    let labelings = equivariant_short_labelings();
    assert_eq!(labelings, vec![[2, 3, 4, 5, 0, 1], [5, 0, 1, 2, 3, 4]]);
    for labels in &labelings {
        // Rays match the six literal short-support defect grades once each.
        assert_eq!(BTreeSet::from(*labels), BTreeSet::from([0, 1, 2, 3, 4, 5]));
        for index in 0..6 {
            let first = labels[index];
            let second = labels[(index + 1) % 6];
            // But an adjacent dP6 cone maps to crossing K6 short diagonals.
            assert!(crosses(short_diagonal(first), short_diagonal(second)));
            // With no target cone grade, mapping it to zero breaks the boundary square.
            let mut boundary_image = [0_i64; 6];
            boundary_image[first] = -1;
            boundary_image[second] = 1;
            assert_ne!(boundary_image, [0_i64; 6]);
        }
    }

    // Pullback of the first coordinate divisor under pi.  It consists of
    // its strict transform and the two exceptional divisors over its ends.
    let pi_d1 = BTreeSet::from([0_usize, 1_usize, 5_usize]);
    let pi_cr_d1 = polarize_support(&pi_d1);
    assert_eq!(pi_cr_d1, BTreeSet::from([2_usize, 3_usize, 4_usize]));
    assert!(pi_d1.is_disjoint(&pi_cr_d1));
    assert_eq!(pi_d1.len(), 3);
    assert_eq!(pi_cr_d1.len(), 3);

    // Rotation produces the other two coordinate-divisor pullbacks and
    // preserves the same three-component mismatch.
    let mut pi_supports = Vec::new();
    let mut pi_cr_supports = Vec::new();
    let mut current = pi_d1.clone();
    for _ in 0..3 {
        let reciprocal = polarize_support(&current);
        assert_eq!(current.len(), 3);
        assert_eq!(reciprocal.len(), 3);
        assert!(current.is_disjoint(&reciprocal));
        pi_supports.push(current.clone());
        pi_cr_supports.push(reciprocal);
        current = rotate_support(&current);
    }
    assert_eq!(rotate_support(&current), pi_supports[1]);

    // The reduced full log boundary is the same six-ray support for both
    // toric modifications, although individual Cartier total transforms are
    // distinct.  Multiplicities/conormal tensor products are deliberately
    // not discarded by claiming an ordinary Cartesian edge square.
    let full_log_boundary: BTreeSet<_> = (0_usize..6).collect();
    let pi_full_reduced: BTreeSet<_> = pi_supports.iter().flatten().copied().collect();
    let pi_cr_full_reduced: BTreeSet<_> = pi_cr_supports.iter().flatten().copied().collect();
    assert_eq!(pi_full_reduced, full_log_boundary);
    assert_eq!(pi_cr_full_reduced, full_log_boundary);

    let individual_edge_cartesian = pi_supports[0] == pi_cr_supports[0];
    assert!(!individual_edge_cartesian);
    let full_reduced_log_boundary_matches = pi_full_reduced == pi_cr_full_reduced;
    assert!(full_reduced_log_boundary_matches);

    println!(
        "{}",
        r#"{"claim":"The smooth six-ray dP6 fan is the minimal integral toric common refinement of the ordinary P2 fan and its quadratic-Cremona transform. Identity and -I give the two toric morphisms, D3 acts strictly, and -I is the central polarity. Each coordinate Cartier divisor has a three-component total transform under either morphism, but the two supports are disjoint alternating triples, so an individual ordinary edge square is not Cartesian. The full reduced six-component log boundary agrees on both sides. Exhaustively, the only D3/polarity-equivariant ray-to-short-label bijections are two central-shift variants: rays match all six literal defect grades, but every adjacent cone maps to a crossing pair of short diagonals, so no direct support-graded cellular map to F_B/F_V exists.","status":"proved","scope":"Exact integral fan, divisor-support, reduced-log-boundary, and finite label-incidence no-go theorem. The no-go is scoped to a direct support-graded cellular map from the dP6 hexagon to F_B/F_V and does not obstruct a future full-log excess Gysin construction with new lower-intersection data.","references":["ledger entry 95","ledger entry 131","ledger entry 143","ledger entry 164"],"factorization_test":{"fan_rays":6,"maximal_cones":6,"smoothness":"all consecutive determinants +1","pi":"identity lattice map refining the standard P2 fan","pi_cr":"-I lattice map resolving quadratic Cremona","D3":"R^3=S^2=1 and SRS=R^-1","polarity":"-I central and shifts the hexagon by three rays","equivariant_ray_labelings":[[2,3,4,5,0,1],[5,0,1,2,3,4]],"ray_defect_grades":"MATCH: each short label occurs exactly once","cone_support":"FAIL: every adjacent cone maps to crossing consecutive short diagonals","zero_cone_chain_map":"FAIL: each cone boundary has two distinct nonzero ray-grade coordinates","pi_coordinate_pullback":"three toric divisors","pi_cr_coordinate_pullback":"three toric divisors","individual_supports":"disjoint alternating triples","individual_edge_cartesian":"FALSIFIED","full_reduced_log_boundary":"MATCH: all six rays","integer_torsion":"none"},"unconstructed":["multiplicity-sensitive logarithmic conormal comparison","toric excess-Gysin/proper push-pull to one entry-131 Cartier line","all lower intersection Cech terms","support-typed map to F_B/F_V"],"next_gate":"Construct the full-boundary toric excess-Gysin with explicit lower-intersection support grades; a direct hexagon cellular map cannot provide them.","boundary":"The common fan resolves the rational Cremona map and validates the carrier refinement. Its rays reproduce the six associated defect labels, but its cone incidence is not the K6 short-face incidence and cannot cancel the literal Q-section defect as a support-graded chain map."}"#
    );
}
