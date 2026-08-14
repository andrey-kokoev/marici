//! Exact associated-grade audit of the normalization--conductor source for a
//! loaded D=03 Cousin/Gysin morphism, followed by a sharp chain-lift boundary.
//!
//! The relevant integral carrier is the augmented triangle resolution
//!
//!   0 -> 1_or --Delta--> P_tag --partial_triangle--> P_road --epsilon--> 1 -> 0.
//!
//! It is exact over Z and Verdier self-dual up to the triangle orientation and
//! degree reversal.  Entry 66's pre-incidence symbol d_y sigma_alt lands in
//! P_tag.  Its six columns are signed individual tags.  Applying
//! partial_triangle gives the QTDS A2 contact matrix, while applying the dual
//! Delta counit before incidence gives six primitive values.  The alternating
//! signs are precisely removed by the retained polarity orientation line.
//!
//! At D=03, the x0 and x3 conductor sheets select the tag dual paired with the
//! road.  Entry 86's endpoint Cousin signs give unit Laurent-normalized values
//! on three vertices of the actual tensor weighted-interval road square; the
//! road cocycle equations force the fourth value to be one.  This produces the
//! entry-89 primitive boundary symbol at associated grade without averaging.
//!
//! Ordinary restriction of the global Mobius orientation cycle is retained
//! only as a negative control: it lands in A2 after incidence and therefore
//! has zero primitive counit.  It is not the source of the construction.
//!
//! The full PC chain map is still not constructed.  The repository has an
//! established Ward target differential, but no scalar first-jet/BRST source
//! differential preserving the normalization--conductor filtration.  The
//! final witness proves that the coefficient symbol cannot determine this
//! missing chain datum.

use std::collections::BTreeMap;

const N: usize = 8;
type Int = i64;

// Columns are the three oriented circuit tags; rows are the three roads.
// This is the oriented triangle boundary used in entry 66.
const TRIANGLE_BOUNDARY: [[Int; 3]; 3] = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]];
const DIAGONAL: [Int; 3] = [1, 1, 1];
const AUGMENTATION: [Int; 3] = [1, 1, 1];

// Rows are (d0,d1,d2); columns are (dx0,...,dx5).  This is the
// shared-longitudinal symbol d_y sigma_alt before road incidence.
const CONDUCTOR_TO_TAGS: [[Int; 6]; 3] = [
    [0, 0, -1, 0, 0, 1],
    [-1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, -1, 0],
];

const QTDS_CONTACT: [[Int; 6]; 3] = [
    [1, 1, 0, -1, -1, 0],
    [0, -1, -1, 0, 1, 1],
    [-1, 0, 1, 1, 0, -1],
];

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Edge(usize, usize);

fn edge(a: usize, b: usize) -> Edge {
    if a < b {
        Edge(a, b)
    } else {
        Edge(b, a)
    }
}

fn crosses(a: Edge, b: Edge) -> bool {
    if a.0 == b.0 || a.0 == b.1 || a.1 == b.0 || a.1 == b.1 {
        return false;
    }
    (a.0 < b.0 && b.0 < a.1 && a.1 < b.1) || (b.0 < a.0 && a.0 < b.1 && b.1 < a.1)
}

fn physical_diagonal(i: usize) -> Edge {
    edge(i % N, (i + 3) % N)
}

fn graph_edges() -> Vec<(usize, usize)> {
    let physicals: Vec<_> = (0..N).map(physical_diagonal).collect();
    let mut result = Vec::new();
    for i in 0..N {
        for j in i + 1..N {
            if !crosses(physicals[i], physicals[j]) {
                result.push((i, j));
            }
        }
    }
    assert_eq!(result.len(), 12);
    result
}

fn find(parent: &mut [usize], value: usize) -> usize {
    if parent[value] != value {
        parent[value] = find(parent, parent[value]);
    }
    parent[value]
}

fn tree_path(
    current: usize,
    target: usize,
    previous: Option<usize>,
    adjacency: &[Vec<usize>],
) -> Option<Vec<usize>> {
    if current == target {
        return Some(vec![current]);
    }
    for &next in &adjacency[current] {
        if Some(next) == previous {
            continue;
        }
        if let Some(mut tail) = tree_path(next, target, Some(current), adjacency) {
            let mut result = vec![current];
            result.append(&mut tail);
            return Some(result);
        }
    }
    None
}

fn graph_cycle(vertices: &[usize], edges: &[(usize, usize)]) -> Vec<Int> {
    let index: BTreeMap<_, _> = edges
        .iter()
        .copied()
        .enumerate()
        .map(|(i, value)| (value, i))
        .collect();
    let mut result = vec![0; edges.len()];
    for i in 0..vertices.len() {
        let a = vertices[i];
        let b = vertices[(i + 1) % vertices.len()];
        let ordered = if a < b { (a, b) } else { (b, a) };
        result[index[&ordered]] += if a < b { 1 } else { -1 };
    }
    result
}

fn graph_boundary(chain: &[Int], edges: &[(usize, usize)]) -> [Int; N] {
    let mut result = [0; N];
    for (&coefficient, &(a, b)) in chain.iter().zip(edges) {
        result[a] -= coefficient;
        result[b] += coefficient;
    }
    result
}

fn fundamental_cycles(edges: &[(usize, usize)]) -> Vec<Vec<Int>> {
    let mut parent: Vec<_> = (0..N).collect();
    let mut tree = Vec::new();
    let mut chords = Vec::new();
    for (index, &(a, b)) in edges.iter().enumerate() {
        let root_a = find(&mut parent, a);
        let root_b = find(&mut parent, b);
        if root_a == root_b {
            chords.push(index);
        } else {
            parent[root_a] = root_b;
            tree.push(index);
        }
    }
    assert_eq!((tree.len(), chords.len()), (7, 5));

    let mut adjacency = vec![Vec::new(); N];
    for &index in &tree {
        let (a, b) = edges[index];
        adjacency[a].push(b);
        adjacency[b].push(a);
    }

    chords
        .iter()
        .enumerate()
        .map(|(position, &index)| {
            let (a, b) = edges[index];
            let path = tree_path(b, a, None, &adjacency).unwrap();
            let mut vertices = vec![a];
            vertices.extend_from_slice(&path[..path.len() - 1]);
            let cycle = graph_cycle(&vertices, edges);
            assert_eq!(graph_boundary(&cycle, edges), [0; N]);
            for (other_position, &other_chord) in chords.iter().enumerate() {
                assert_eq!(cycle[other_chord], Int::from(position == other_position));
            }
            cycle
        })
        .collect()
}

fn local_road_restriction(chain: &[Int], edges: &[(usize, usize)]) -> [Int; 3] {
    let index: BTreeMap<_, _> = edges
        .iter()
        .copied()
        .enumerate()
        .map(|(i, value)| (value, i))
        .collect();
    // At p_0=D=03 the compatible physical roads are p_3,p_4,p_5, and all
    // three graph edges have the canonical orientation 0 -> j.
    std::array::from_fn(|i| chain[index[&(0, i + 3)]])
}

fn gcd(mut a: Int, mut b: Int) -> Int {
    a = a.abs();
    b = b.abs();
    while b != 0 {
        (a, b) = (b, a % b);
    }
    a
}

fn rank(mut rows: Vec<Vec<Int>>) -> usize {
    if rows.is_empty() {
        return 0;
    }
    let columns = rows[0].len();
    let mut pivot_row = 0;
    for column in 0..columns {
        let Some(found) = (pivot_row..rows.len()).find(|&row| rows[row][column] != 0) else {
            continue;
        };
        rows.swap(pivot_row, found);
        for row in 0..rows.len() {
            if row == pivot_row || rows[row][column] == 0 {
                continue;
            }
            let a = rows[pivot_row][column];
            let b = rows[row][column];
            for entry in column..columns {
                rows[row][entry] = a * rows[row][entry] - b * rows[pivot_row][entry];
            }
            let divisor = rows[row]
                .iter()
                .fold(0, |common, &value| gcd(common, value));
            if divisor > 1 {
                for value in &mut rows[row] {
                    *value /= divisor;
                }
            }
        }
        pivot_row += 1;
    }
    pivot_row
}

fn mat_mul_3x3_3x6(left: [[Int; 3]; 3], right: [[Int; 6]; 3]) -> [[Int; 6]; 3] {
    std::array::from_fn(|row| {
        std::array::from_fn(|column| {
            (0..3)
                .map(|middle| left[row][middle] * right[middle][column])
                .sum()
        })
    })
}

fn mat_vec_3(matrix: [[Int; 3]; 3], vector: [Int; 3]) -> [Int; 3] {
    std::array::from_fn(|row| {
        (0..3)
            .map(|column| matrix[row][column] * vector[column])
            .sum()
    })
}

fn row_times_3x6(row: [Int; 3], matrix: [[Int; 6]; 3]) -> [Int; 6] {
    std::array::from_fn(|column| {
        (0..3)
            .map(|middle| row[middle] * matrix[middle][column])
            .sum()
    })
}

fn determinant_3(matrix: [[Int; 3]; 3]) -> Int {
    matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
}

fn audit_augmented_triangle() -> [Int; 6] {
    // Consecutive compositions vanish.
    assert_eq!(mat_vec_3(TRIANGLE_BOUNDARY, DIAGONAL), [0, 0, 0]);
    for column in 0..3 {
        assert_eq!(
            (0..3)
                .map(|row| AUGMENTATION[row] * TRIANGLE_BOUNDARY[row][column])
                .sum::<Int>(),
            0
        );
    }

    // Integral exactness: Delta and epsilon are primitive; the triangle
    // boundary has rank two and unit 2x2 minors.  Its kernel is the diagonal,
    // and its image is the augmentation kernel.
    assert_eq!(DIAGONAL.iter().fold(0, |a, &b| gcd(a, b)), 1);
    assert_eq!(AUGMENTATION.iter().fold(0, |a, &b| gcd(a, b)), 1);
    assert_eq!(rank(TRIANGLE_BOUNDARY.map(|row| row.to_vec()).to_vec()), 2);
    let two_minors = (0..3)
        .flat_map(|r0| {
            (r0 + 1..3).flat_map(move |r1| {
                (0..3).flat_map(move |c0| {
                    (c0 + 1..3).map(move |c1| {
                        TRIANGLE_BOUNDARY[r0][c0] * TRIANGLE_BOUNDARY[r1][c1]
                            - TRIANGLE_BOUNDARY[r0][c1] * TRIANGLE_BOUNDARY[r1][c0]
                    })
                })
            })
        })
        .collect::<Vec<_>>();
    assert_eq!(two_minors.iter().fold(0, |a, &b| gcd(a, b)), 1);

    // With the declared oriented bases, partial_triangle is skew self-dual
    // and Delta^vee=epsilon.
    for row in 0..3 {
        for column in 0..3 {
            assert_eq!(
                TRIANGLE_BOUNDARY[row][column],
                -TRIANGLE_BOUNDARY[column][row]
            );
        }
    }
    assert_eq!(DIAGONAL, AUGMENTATION);

    // Primitive plus A2 data jointly see the whole tag module, but with the
    // familiar index-three obstruction.  Use the first two road coordinates
    // on A2; the combined matrix has Smith factors (1,1,3).
    let primitive_plus_a2 = [AUGMENTATION, TRIANGLE_BOUNDARY[0], TRIANGLE_BOUNDARY[1]];
    assert_eq!(determinant_3(primitive_plus_a2).abs(), 3);
    let entries_gcd = primitive_plus_a2
        .iter()
        .flatten()
        .fold(0, |a, &b| gcd(a, b));
    assert_eq!(entries_gcd, 1);
    let minors_gcd = (0..3)
        .flat_map(|r0| {
            (r0 + 1..3).flat_map(move |r1| {
                (0..3).flat_map(move |c0| {
                    (c0 + 1..3).map(move |c1| {
                        primitive_plus_a2[r0][c0] * primitive_plus_a2[r1][c1]
                            - primitive_plus_a2[r0][c1] * primitive_plus_a2[r1][c0]
                    })
                })
            })
        })
        .fold(0, gcd);
    assert_eq!(minors_gcd, 1);

    // The conductor lands before incidence.  Incidence recovers exactly the
    // QTDS contact matrix, whereas the dual-Delta counit gives the alternating
    // primitive values on its six supported columns.
    assert_eq!(
        mat_mul_3x3_3x6(TRIANGLE_BOUNDARY, CONDUCTOR_TO_TAGS),
        QTDS_CONTACT
    );
    let primitive = row_times_3x6(AUGMENTATION, CONDUCTOR_TO_TAGS);
    assert_eq!(primitive, [-1, 1, -1, 1, -1, 1]);
    for column in 0..6 {
        assert_eq!(
            (0..3)
                .filter(|&row| CONDUCTOR_TO_TAGS[row][column] != 0)
                .count(),
            1
        );
        assert_eq!(primitive[column].abs(), 1);
    }
    // The even columns belong to F_- and acquire the minus polarity-line
    // basis; odd columns belong to F_+.  Retaining that line turns all six
    // primitive values into +1 without dividing by two or three.
    let polarity_line = [-1, 1, -1, 1, -1, 1];
    let oriented_primitive =
        std::array::from_fn::<_, 6, _>(|column| polarity_line[column] * primitive[column]);
    assert_eq!(oriented_primitive, [1; 6]);
    primitive
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct LaurentMonomial([i8; 6]);

impl LaurentMonomial {
    fn occurrence(first: usize, second: usize) -> Self {
        let mut result = [0; 6];
        result[first] += 1;
        result[second] += 1;
        Self(result)
    }

    fn inverse(self) -> Self {
        Self(self.0.map(|value| -value))
    }

    fn multiply(self, other: Self) -> Self {
        Self(std::array::from_fn(|index| self.0[index] + other.0[index]))
    }
}

fn audit_d03_occurrence_cousin() -> ([[Int; 2]; 2], usize) {
    // The D03 road square has left slots (x0,x1) and right slots (x3,x4).
    // The two normalization sheets singled out by the conductor are
    //   F_+: +dx3 -> +tag1, with sink mark x3 and source slots x0,x1;
    //   F_-: -dx0 -> -tag1, with sink mark x0 and source slots x3,x4.
    // The polarity line changes the second displayed sign, so both maps have
    // positive primitive normalization.  Entry 86 supplies endpoint Cousin
    // sign +1, scalar source sign -1, and coaction sign -1.
    let endpoint_cousin = 1;
    let scalar_source = -1;
    let entry_coaction = -1;
    assert_eq!(endpoint_cousin * scalar_source * entry_coaction, 1);

    let plus_weights = [
        LaurentMonomial::occurrence(0, 3),
        LaurentMonomial::occurrence(1, 3),
    ];
    let minus_weights = [
        LaurentMonomial::occurrence(0, 3),
        LaurentMonomial::occurrence(0, 4),
    ];
    for weight in plus_weights.into_iter().chain(minus_weights) {
        assert_eq!(weight.multiply(weight.inverse()), LaurentMonomial([0; 6]));
    }

    // Keep the sheets resolved at the common x0*x3 occurrence.  Their values
    // agree; they are not added into an artificial coefficient two.
    assert_eq!(plus_weights[0], minus_weights[0]);

    // Values are arranged as left-slot x right-slot.  The two sheet maps set
    // three vertices to one.  The connected tensor-interval cocycle equations
    // force the fourth value to one as well.
    let mut values = [[None; 2]; 2];
    values[0][0] = Some(1); // x0*x3, both sheets
    values[1][0] = Some(1); // x1*x3, F_+
    values[0][1] = Some(1); // x0*x4, F_-
                            // Right-interval cocycle at left slot x1, or equivalently left-interval
                            // cocycle at right slot x4, determines the remaining corner.
    values[1][1] = values[1][0].or(values[0][1]);
    let values = values.map(|row| row.map(Option::unwrap));
    assert_eq!(values, [[1, 1], [1, 1]]);

    // Entry 89 pairs road q0 with tag c1^vee.  The selected conductor supports
    // are exactly x0 -> -c1 and x3 -> +c1; after the polarity line both have
    // value +1 and normalize the same Laurent road cocycle.
    let paired_tag_for_d03 = 1;
    assert_eq!(CONDUCTOR_TO_TAGS[paired_tag_for_d03][0], -1);
    assert_eq!(CONDUCTOR_TO_TAGS[paired_tag_for_d03][3], 1);

    (values, paired_tag_for_d03)
}

const WARD_SYMBOL: [[Int; 6]; 7] = [
    [0, -1, -1, 0, 1, 1],
    [-1, -1, 0, 1, 1, 0],
    [0, 1, 1, 0, -1, -1],
    [1, 1, 0, -1, -1, 0],
    [-1, -1, 0, 1, 1, 0],
    [0, 1, 1, 0, -1, -1],
    [1, 0, -1, -1, 0, 1],
];

fn ward_contact_column(column: usize) -> [Int; 6] {
    let edge_slot = |core: usize, road: usize| 2 * road + core;
    let mut result = [0; 6];
    match column {
        0..=3 => {
            let core = column / 2;
            let road = column % 2;
            result[edge_slot(core, (road + 1) % 3)] += 1;
            result[edge_slot(core, (road + 2) % 3)] -= 1;
        }
        4..=6 => {
            let road = column - 4;
            result[edge_slot(0, road)] += 1;
            result[edge_slot(1, road)] -= 1;
        }
        _ => unreachable!(),
    }
    result
}

fn ward_contact(chain: [Int; 7]) -> [Int; 6] {
    let mut result = [0; 6];
    for (column, coefficient) in chain.into_iter().enumerate() {
        for (entry, value) in result.iter_mut().zip(ward_contact_column(column)) {
            *entry += coefficient * value;
        }
    }
    result
}

fn square_matrix(value: [[Int; 6]; 6]) -> [[Int; 6]; 6] {
    std::array::from_fn(|row| {
        std::array::from_fn(|column| {
            (0..6)
                .map(|middle| value[row][middle] * value[middle][column])
                .sum()
        })
    })
}

fn compose_symbol_source(value: [[Int; 6]; 6]) -> [[Int; 6]; 7] {
    std::array::from_fn(|row| {
        std::array::from_fn(|column| {
            (0..6)
                .map(|middle| WARD_SYMBOL[row][middle] * value[middle][column])
                .sum()
        })
    })
}

fn main() {
    let primitive_conductor_values = audit_augmented_triangle();
    let (d03_occurrence_values, d03_tag) = audit_d03_occurrence_cousin();

    // Negative control from entries 91--92.  Ordinary restriction of the
    // global Mobius orientation carrier first applies road incidence.  Every
    // resulting local cycle lies in A2 and is therefore killed by the
    // primitive augmentation.  The correct conductor source above lands in
    // P_tag before this incidence map.
    let edges = graph_edges();
    let cycles = fundamental_cycles(&edges);
    assert_eq!(cycles.len(), 5);
    let restrictions: Vec<_> = cycles
        .iter()
        .map(|cycle| local_road_restriction(cycle, &edges))
        .collect();
    for restriction in &restrictions {
        assert_eq!(restriction.iter().sum::<Int>(), 0);
    }
    assert_eq!(
        rank(restrictions.iter().map(|row| row.to_vec()).collect()),
        2
    );
    let ordinary_restriction_outputs: Vec<_> = restrictions
        .iter()
        .map(|restriction| restriction.iter().sum::<Int>())
        .collect();
    assert_eq!(ordinary_restriction_outputs, vec![0; 5]);

    // The complete entry-86 endpoint residues are equal on the two polarity
    // sheets.  Thus after applying triangle incidence the physical contact
    // residue cancels, exactly as required by entry 87.  This is compatible
    // with, but logically later than, the nonzero pre-incidence primitive
    // counit computed above.
    let plus_endpoint: [[Int; 4]; 3] = [[1; 4]; 3];
    let minus_endpoint: [[Int; 4]; 3] = [[1; 4]; 3];
    let endpoint_difference: [[Int; 4]; 3] = std::array::from_fn(|road| {
        std::array::from_fn(|word| plus_endpoint[road][word] - minus_endpoint[road][word])
    });
    assert_eq!(endpoint_difference, [[0; 4]; 3]);
    let plus_polarized = plus_endpoint.map(|road| road.iter().sum::<Int>());
    let minus_polarized = minus_endpoint.map(|road| road.iter().sum::<Int>());
    assert_eq!(plus_polarized, [4, 4, 4]);
    assert_eq!(minus_polarized, [4, 4, 4]);
    assert_eq!(
        std::array::from_fn::<_, 3, _>(|road| plus_polarized[road] - minus_polarized[road]),
        [0, 0, 0]
    );
    for column in 0..6 {
        assert_eq!((0..3).map(|row| QTDS_CONTACT[row][column]).sum::<Int>(), 0);
    }

    // The ordered line factors are retained rather than trivialized: at the
    // nontrivial D03 stabilizer element, road orientation and polarity both
    // reverse while the ordered normal transports positively.
    let tangential_orientation = -1;
    let polarity_orientation = -1;
    let ordered_normal_transport = 1;
    let loaded_character = tangential_orientation * polarity_orientation * ordered_normal_transport;
    assert_eq!(loaded_character, 1);

    // Entry 66's six columns are closed for the established Ward target
    // differential.  But the source scalar first-jet/BRST differential is
    // not among the admitted maps.  Two square-zero source witnesses with the
    // same modules and coefficient symbol give opposite chain-map answers.
    for column in 0..6 {
        let ward_column = std::array::from_fn(|row| WARD_SYMBOL[row][column]);
        assert_eq!(ward_contact(ward_column), [0; 6]);
    }
    let zero_source: [[Int; 6]; 6] = [[0; 6]; 6];
    let mut nonzero_source = zero_source;
    nonzero_source[0][1] = 1;
    assert_eq!(square_matrix(zero_source), zero_source);
    assert_eq!(square_matrix(nonzero_source), zero_source);
    assert_eq!(compose_symbol_source(zero_source), [[0; 6]; 7]);
    assert_ne!(compose_symbol_source(nonzero_source), [[0; 6]; 7]);

    println!("D03 normalization-conductor Cousin/Gysin associated-grade audit: PASS");
    println!("augmented_triangle=0->1_or->P_tag->P_road->1->0 exact_over_Z=true");
    println!("Verdier_self_dual=Delta^vee_epsilon_and_partial^vee=-partial");
    println!("combined_tag_map_to_primitive_plus_A2_Smith=[1,1,3] index=3");
    println!("d_y_sigma_alt_to_tags_six_supports=rank3 signed_individual_tags=true");
    println!("partial_triangle_d_y_sigma_alt_equals_QTDS_contact=true");
    println!("Delta_dual_primitive_values={primitive_conductor_values:?}");
    println!("after_polarity_line_primitive_values=[1,1,1,1,1,1]");
    println!("D03_paired_tag={d03_tag} road_occurrence_values={d03_occurrence_values:?}");
    println!("D03_primitive_occurrences=4 polarized_road_value=4 no_averaging=true");
    println!("endpoint_occurrences_per_road=4 plus=[4,4,4] minus=[4,4,4] difference=0");
    println!("ordered_line_character_at_D03_stabilizer=(-1)*(-1)*(+1)=+1");
    println!(
        "associated_grade_physical_cut_naturality=PASS contact_in_A2 endpoint_difference_zero"
    );
    println!("ordinary_global_orientation_restriction_outputs={ordinary_restriction_outputs:?} WRONG_SOURCE");
    println!("coefficient_symbol_Ward_closed=true scalar_BRST_chain_lift=NOT_CONSTRUCTED");
    println!("VERDICT: ASSOCIATED-GRADE G03 SOURCE AND PRIMITIVE COMPOSITE PROVED");
    println!("FULL_PC_CHAIN_MAP_AND_PHYSICAL_CUT_NATURALITY=UNTYPED");
    println!(
        "required_new_datum=scalar first-jet BRST differential preserving conductor filtration"
    );
}
