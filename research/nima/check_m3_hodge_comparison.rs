//! Exact m=3 comparison certificate for the six-point QTDS contact flow and
//! the marked-theta Ward/circuit current.
//!
//! PROVED HERE
//! -----------
//! * Both coefficient calculations have the same augmented cellular skeleton
//!
//!       0 -> Z --d2--> Z^3 --B--> A2 -> 0,
//!
//!   where B(t_i)=e_i-e_{i+1} and d2(1)=(1,1,1).
//! * Their rational zero-circulation current is the same Green operator
//!
//!       sigma(c) = B^T c / 3,       B sigma(c)=c  for c in A2.
//!
//! * Rotation, reflection, and polarity/core-exchange characters agree after
//!   one explicitly declared label identification.  Reflection and the
//!   polarity/core involution both negate the relation cell.
//! * Contracting each canonical QTDS tripod route gives the polarity-channel
//!   incidence graph K_{2,3}=S^0*R_3.  The suspension map
//!
//!       Gamma(c)=sum_i c_i(e_{+,i}-e_{-,i})
//!
//!   is a primitive integral isomorphism A2 -> H1(K_{2,3}).  It sends each
//!   oriented triangle edge to the corresponding adjacent four-circuit.
//!   The order-six rotation combining polarity exchange with road rotation,
//!   and road reflection, generate every automorphism of K_{2,3}.
//! * With that identification, all integral D3-equivariant chain comparisons
//!   are
//!
//!       F0 = a I on A2,
//!       F1 = a I + b J on Z^3,
//!       F2 = a + 3b on Z,
//!
//!   for arbitrary a,b in Z.  Boundary and symmetry alone do not select a,b,
//!   but the suspension and individual-support condition do: F(t_i) must be
//!   the adjacent four-circuit Gamma(B t_i), hence a=1,b=0.  The earlier zero
//!   versus identity ambiguity is removed at the combinatorial carrier level.
//! * Composing Gamma with the exact Ward bridge Theta sends the full symbolic
//!   six-point QTDS contact matrix to an explicit 7-by-6 integral matrix in
//!   the Ward quotient.  Every column is killed by the Ward contact map, and
//!   the typed D6 generators intertwine it exactly.
//! * The already counted punctured-torus edge Cut does not yet define a chain
//!   map on this oriented resolution: its tag functional sends d2(1) to 1
//!   (and the orbit sum sends it to 3).  An oriented annulus/open-curve target
//!   and the image of the relation generator are missing.
//!
//! NOT PROVED HERE
//! ---------------
//! The canonical suspension is not yet a map of physical coefficient systems:
//! no scalar-first-jet map identifies the QTDS contact polynomials with Ward
//! coefficients, and no physical Cut square between them is claimed.  The
//! final Cut audit is a typing obstruction, not a falsification of a future
//! derived comparison.

use std::collections::BTreeSet;

type Vector = Vec<i64>;
type Matrix = Vec<Vec<i64>>;

const BOUNDARY: [[i64; 3]; 3] = [[1, 0, -1], [-1, 1, 0], [0, -1, 1]];
const RELATION: [i64; 3] = [1, 1, 1];

fn mat_vec(matrix: &Matrix, vector: &[i64]) -> Vector {
    matrix
        .iter()
        .map(|row| row.iter().zip(vector).map(|(a, b)| a * b).sum())
        .collect()
}

fn mat_mul(left: &Matrix, right: &Matrix) -> Matrix {
    assert_eq!(left[0].len(), right.len());
    (0..left.len())
        .map(|row| {
            (0..right[0].len())
                .map(|column| {
                    (0..right.len())
                        .map(|middle| left[row][middle] * right[middle][column])
                        .sum()
                })
                .collect()
        })
        .collect()
}

fn transpose(matrix: &Matrix) -> Matrix {
    (0..matrix[0].len())
        .map(|column| matrix.iter().map(|row| row[column]).collect())
        .collect()
}

fn scale(coefficient: i64, vector: &[i64]) -> Vector {
    vector.iter().map(|entry| coefficient * entry).collect()
}

fn boundary_matrix() -> Matrix {
    BOUNDARY.iter().map(|row| row.to_vec()).collect()
}

/// Columns are the six boundary variables x0,...,x5; rows are the three
/// physical-channel contact coefficients in q_+ - q_-.
fn qtds_contact_matrix() -> Matrix {
    vec![
        vec![1, 1, 0, -1, -1, 0],
        vec![0, -1, -1, 0, 1, 1],
        vec![-1, 0, 1, 1, 0, -1],
    ]
}

fn is_root(vector: &[i64]) -> bool {
    vector.len() == 3 && vector.iter().sum::<i64>() == 0
}

fn root_from_coordinates(coordinates: [i64; 2]) -> Vector {
    vec![
        coordinates[0],
        coordinates[1],
        -coordinates[0] - coordinates[1],
    ]
}

fn root_coordinates(root: &[i64]) -> [i64; 2] {
    assert!(is_root(root));
    [root[0], root[1]]
}

/// Three times sigma(c).  The only denominator is the numerical Jacobian
/// order 3; no kinematic propagator is introduced.
fn green_numerator(root: &[i64]) -> Vector {
    assert!(is_root(root));
    mat_vec(&transpose(&boundary_matrix()), root)
}

fn class_map(tags: &[i64]) -> Vector {
    mat_vec(&boundary_matrix(), tags)
}

fn road_permutation(rotation: usize, reflected: bool) -> [usize; 3] {
    std::array::from_fn(|index| {
        if reflected {
            (rotation + 3 - index) % 3
        } else {
            (index + rotation) % 3
        }
    })
}

/// Action on A2.  The `sheet` sign is QTDS polarity exchange on the top row
/// and marked-theta core exchange on the bottom row.  Equating those two
/// involutions is an explicit comparison datum, not a derived fact.
fn root_action(root: &[i64], rotation: usize, reflected: bool, sheet: bool) -> Vector {
    assert!(is_root(root));
    let permutation = road_permutation(rotation, reflected);
    let sign = if sheet { -1 } else { 1 };
    let mut result = vec![0; 3];
    for source in 0..3 {
        result[permutation[source]] += sign * root[source];
    }
    assert!(is_root(&result));
    result
}

/// Oriented-edge action for t_i with B(t_i)=e_i-e_{i+1}.
fn tag_action(tags: &[i64], rotation: usize, reflected: bool, sheet: bool) -> Vector {
    let sheet_sign = if sheet { -1 } else { 1 };
    let reflection_sign = if reflected { -1 } else { 1 };
    let mut result = vec![0; 3];
    for source in 0..3 {
        let target = if reflected {
            (rotation + 6 - source - 1) % 3
        } else {
            (source + rotation) % 3
        };
        result[target] += sheet_sign * reflection_sign * tags[source];
    }
    result
}

fn relation_character(reflected: bool, sheet: bool) -> i64 {
    (if reflected { -1 } else { 1 }) * (if sheet { -1 } else { 1 })
}

fn action_matrix_roots(rotation: usize, reflected: bool) -> Matrix {
    let basis = [root_from_coordinates([1, 0]), root_from_coordinates([0, 1])];
    let columns: Vec<_> = basis
        .iter()
        .map(|root| root_coordinates(&root_action(root, rotation, reflected, false)))
        .collect();
    (0..2)
        .map(|row| columns.iter().map(|column| column[row]).collect())
        .collect()
}

fn action_matrix_tags(rotation: usize, reflected: bool) -> Matrix {
    let columns: Vec<_> = (0..3)
        .map(|index| {
            let mut tag = vec![0; 3];
            tag[index] = 1;
            tag_action(&tag, rotation, reflected, false)
        })
        .collect();
    (0..3)
        .map(|row| columns.iter().map(|column| column[row]).collect())
        .collect()
}

fn audit_cellular_hodge_square() {
    let boundary = boundary_matrix();
    assert_eq!(class_map(&RELATION), vec![0; 3]);

    // A unit 2-minor proves that B surjects integrally onto A2; together with
    // ker(B)=Z(1,1,1), this is the saturated cellular resolution.
    assert_eq!(
        boundary[0][0] * boundary[1][1] - boundary[0][1] * boundary[1][0],
        1
    );
    for tags in [vec![1, 1, 1], vec![2, 2, 2], vec![-3, -3, -3]] {
        assert_eq!(class_map(&tags), vec![0; 3]);
    }

    let laplacian = mat_mul(&boundary, &transpose(&boundary));
    for root in [
        root_from_coordinates([1, 0]),
        root_from_coordinates([0, 1]),
        root_from_coordinates([2, -5]),
    ] {
        assert_eq!(mat_vec(&laplacian, &root), scale(3, &root));
        let numerator = green_numerator(&root);
        assert_eq!(numerator.iter().sum::<i64>(), 0);
        assert_eq!(class_map(&numerator), scale(3, &root));
    }

    // The exact generic contact vector used by the scalar/Rees tripod audit.
    assert_eq!(green_numerator(&[2, -5, 3]), vec![7, -8, 1]);

    // The symbolic six-point QTDS contact difference in the basis x0,...,x5.
    let qtds_contact = qtds_contact_matrix();
    for column in 0..6 {
        assert_eq!(qtds_contact.iter().map(|row| row[column]).sum::<i64>(), 0);
    }
    let current_numerator = mat_mul(&transpose(&boundary), &qtds_contact);
    assert_eq!(
        mat_mul(&boundary, &current_numerator),
        qtds_contact
            .iter()
            .map(|row| row.iter().map(|entry| 3 * entry).collect())
            .collect::<Matrix>()
    );

    // The Ward root c(p,q)=[p,q,-p-q] has exactly the previously certified
    // marked-theta section numerator.
    let ward_root = root_from_coordinates([11, -4]);
    assert_eq!(green_numerator(&ward_root), vec![15, 3, -18]);
    let [p, q] = root_coordinates(&ward_root);
    assert_eq!(
        green_numerator(&ward_root),
        vec![p - q, p + 2 * q, -2 * p - q]
    );
}

type WardChain = [i64; 7];
type GraphChain = [i64; 6];

fn graph_edge(core: usize, road: usize) -> usize {
    2 * road + core
}

fn graph_boundary(chain: &GraphChain) -> [i64; 5] {
    let mut result = [0; 5];
    for road in 0..3 {
        for core in 0..2 {
            let coefficient = chain[graph_edge(core, road)];
            result[core] -= coefficient;
            result[2 + road] += coefficient;
        }
    }
    result
}

/// Integral suspension from reduced road zero-chains to the incidence-graph
/// cycle lattice.  Edges are oriented from a polarity vertex to a road.
fn suspension(root: &[i64]) -> GraphChain {
    assert!(is_root(root));
    let mut result = [0; 6];
    for road in 0..3 {
        result[graph_edge(0, road)] = root[road];
        result[graph_edge(1, road)] = -root[road];
    }
    assert_eq!(graph_boundary(&result), [0; 5]);
    result
}

fn graph_chain_action(
    chain: &GraphChain,
    rotation: usize,
    reflected: bool,
    core_swap: bool,
) -> GraphChain {
    let roads = road_permutation(rotation, reflected);
    let mut result = [0; 6];
    for road in 0..3 {
        for core in 0..2 {
            let target_core = if core_swap { 1 - core } else { core };
            result[graph_edge(target_core, roads[road])] += chain[graph_edge(core, road)];
        }
    }
    result
}

fn adjacent_circuit(tag: usize) -> GraphChain {
    let mut unit = vec![0; 3];
    unit[tag] = 1;
    suspension(&class_map(&unit))
}

fn incidence_edge(first: usize, second: usize) -> bool {
    (first < 2 && second >= 2) || (second < 2 && first >= 2)
}

type VertexPermutation = [usize; 5];

fn compose_permutations(after: VertexPermutation, before: VertexPermutation) -> VertexPermutation {
    std::array::from_fn(|vertex| after[before[vertex]])
}

fn is_graph_automorphism(permutation: &VertexPermutation) -> bool {
    let distinct: BTreeSet<_> = permutation.iter().copied().collect();
    if distinct.len() != 5 {
        return false;
    }
    (0..5).all(|first| {
        (0..5).all(|second| {
            incidence_edge(first, second) == incidence_edge(permutation[first], permutation[second])
        })
    })
}

fn all_vertex_permutations() -> Vec<VertexPermutation> {
    fn recurse(
        position: usize,
        current: &mut VertexPermutation,
        used: &mut [bool; 5],
        output: &mut Vec<VertexPermutation>,
    ) {
        if position == 5 {
            output.push(*current);
            return;
        }
        for value in 0..5 {
            if used[value] {
                continue;
            }
            used[value] = true;
            current[position] = value;
            recurse(position + 1, current, used, output);
            used[value] = false;
        }
    }
    let mut output = Vec::new();
    recurse(0, &mut [0; 5], &mut [false; 5], &mut output);
    output
}

fn generated_d6() -> BTreeSet<VertexPermutation> {
    // r:(epsilon,i)->(epsilon+1,i+1), s:(epsilon,i)->(epsilon,-i).
    let rotation: VertexPermutation = [1, 0, 3, 4, 2];
    let reflection: VertexPermutation = [0, 1, 2, 4, 3];
    let identity: VertexPermutation = [0, 1, 2, 3, 4];

    let mut power = identity;
    for exponent in 1..=6 {
        power = compose_permutations(rotation, power);
        assert_eq!(power == identity, exponent == 6);
    }
    assert_eq!(compose_permutations(reflection, reflection), identity);
    let rotation_inverse = (0..5).fold(identity, |value, _| compose_permutations(rotation, value));
    assert_eq!(
        compose_permutations(reflection, compose_permutations(rotation, reflection)),
        rotation_inverse
    );

    let mut group = BTreeSet::from([identity]);
    loop {
        let previous = group.len();
        let elements: Vec<_> = group.iter().copied().collect();
        for element in elements {
            group.insert(compose_permutations(rotation, element));
            group.insert(compose_permutations(reflection, element));
        }
        if group.len() == previous {
            break;
        }
    }
    group
}

fn audit_suspension_carrier() -> (usize, usize) {
    // The join S^0*R3 contains exactly all six polarity-channel incidences
    // and no core-core or road-road edge: it is K_{2,3}.
    let join_edges: BTreeSet<_> = (0..2)
        .flat_map(|core| (0..3).map(move |road| (core, 2 + road)))
        .collect();
    let graph_edges: BTreeSet<_> = (0..5)
        .flat_map(|first| ((first + 1)..5).map(move |second| (first, second)))
        .filter(|&(first, second)| incidence_edge(first, second))
        .collect();
    assert_eq!(join_edges, graph_edges);
    assert_eq!(graph_edges.len(), 6);

    // Gamma is primitive: projection to the three plus-polarity edges is its
    // integral inverse on cycles.  The road boundary forces the minus entries
    // to be the negatives, while either core boundary imposes sum(c)=0.
    for root in [
        root_from_coordinates([1, 0]),
        root_from_coordinates([0, 1]),
        root_from_coordinates([7, -3]),
    ] {
        let cycle = suspension(&root);
        let projected: Vector = (0..3).map(|road| cycle[graph_edge(0, road)]).collect();
        assert_eq!(projected, root);
        for road in 0..3 {
            assert_eq!(cycle[graph_edge(1, road)], -cycle[graph_edge(0, road)]);
        }
    }

    // Every triangle tag is sent to the adjacent four-edge circuit.  Their
    // diagonal relation maps to zero, exactly as Gamma o B requires.
    let mut circuit_sum = [0; 6];
    for tag in 0..3 {
        let circuit = adjacent_circuit(tag);
        assert_eq!(graph_boundary(&circuit), [0; 5]);
        assert_eq!(circuit.iter().filter(|&&entry| entry != 0).count(), 4);
        assert!(circuit.iter().all(|entry| entry.abs() <= 1));
        for edge in 0..6 {
            circuit_sum[edge] += circuit[edge];
        }
    }
    assert_eq!(circuit_sum, [0; 6]);

    // D6 covariance.  r combines polarity exchange and road rotation; s is
    // road reflection.  On A2 these are c |-> -R(c) and c |-> S(c).
    let roots = [root_from_coordinates([1, 0]), root_from_coordinates([0, 1])];
    let mut covariance_checks = 0;
    for (rotation, reflected, core_swap) in [(1, false, true), (0, true, false)] {
        for root in &roots {
            assert_eq!(
                suspension(&root_action(root, rotation, reflected, core_swap)),
                graph_chain_action(&suspension(root), rotation, reflected, core_swap,)
            );
            covariance_checks += 1;
        }
        for tag in 0..3 {
            let mut unit = vec![0; 3];
            unit[tag] = 1;
            assert_eq!(
                suspension(&class_map(&tag_action(
                    &unit, rotation, reflected, core_swap,
                ))),
                graph_chain_action(&adjacent_circuit(tag), rotation, reflected, core_swap,)
            );
            covariance_checks += 1;
        }
    }

    let generated = generated_d6();
    assert_eq!(generated.len(), 12);
    assert!(generated.iter().all(is_graph_automorphism));
    let all_automorphisms: BTreeSet<_> = all_vertex_permutations()
        .into_iter()
        .filter(is_graph_automorphism)
        .collect();
    assert_eq!(all_automorphisms.len(), 2 * 6);
    assert!(all_automorphisms.iter().all(|permutation| {
        permutation[0] < 2
            && permutation[1] < 2
            && permutation[2] >= 2
            && permutation[3] >= 2
            && permutation[4] >= 2
    }));
    assert_eq!(generated, all_automorphisms);
    (covariance_checks, all_automorphisms.len())
}

fn ward_contact_column(column: usize) -> GraphChain {
    let mut result = [0; 6];
    match column {
        0..=3 => {
            let core = column / 2;
            let road = column % 2;
            result[graph_edge(core, (road + 1) % 3)] += 1;
            result[graph_edge(core, (road + 2) % 3)] -= 1;
        }
        4..=6 => {
            let road = column - 4;
            result[graph_edge(0, road)] += 1;
            result[graph_edge(1, road)] -= 1;
        }
        _ => unreachable!(),
    }
    result
}

fn ward_contact(chain: WardChain) -> GraphChain {
    let mut result = [0; 6];
    for column in 0..7 {
        let source = ward_contact_column(column);
        for edge in 0..6 {
            result[edge] += chain[column] * source[edge];
        }
    }
    result
}

fn ward_bridge(p: i64, q: i64) -> WardChain {
    [q, -p, -q, p, -p, -q, p + q]
}

fn permutation_sign(permutation: [usize; 3]) -> i64 {
    let inversions = (0..3)
        .flat_map(|left| ((left + 1)..3).map(move |right| (left, right)))
        .filter(|&(left, right)| permutation[left] > permutation[right])
        .count();
    if inversions % 2 == 0 {
        1
    } else {
        -1
    }
}

/// The exact action in the quotient chart
/// (l00,l01,l10,l11,q0,q1,q2), copied from the Ward-cycle certificate.
fn ward_action(ward: WardChain, rotation: usize, reflected: bool, core_swap: bool) -> WardChain {
    let roads = road_permutation(rotation, reflected);
    let full = [
        ward[0], ward[1], 0, ward[2], ward[3], 0, ward[4], ward[5], ward[6],
    ];
    let mut moved = [0; 9];
    let road_sign = permutation_sign(roads);
    for core in 0..2 {
        for road in 0..3 {
            let source = 3 * core + road;
            let target = 3 * (if core_swap { 1 - core } else { core }) + roads[road];
            moved[target] += road_sign * full[source];
        }
    }
    for road in 0..3 {
        let core_sign = if core_swap { -1 } else { 1 };
        moved[6 + roads[road]] += core_sign * full[6 + road];
    }
    [
        moved[0] - moved[2],
        moved[1] - moved[2],
        moved[3] - moved[5],
        moved[4] - moved[5],
        moved[6],
        moved[7],
        moved[8],
    ]
}

fn audit_ward_source_typing() {
    for [p, q] in [[1, 0], [0, 1], [3, -7]] {
        assert_eq!(ward_contact(ward_bridge(p, q)), [0; 6]);
        let graph_cycle = [p, -p, q, -q, -p - q, p + q];
        assert_eq!(
            graph_cycle,
            [
                p,
                -p,
                q,
                -q,
                root_from_coordinates([p, q])[2],
                -root_from_coordinates([p, q])[2],
            ]
        );
    }
}

fn audit_symbolic_qtds_to_ward() -> (Matrix, usize) {
    let contact = qtds_contact_matrix();
    let columns: Vec<WardChain> = (0..6)
        .map(|variable| {
            let root: Vector = (0..3).map(|road| contact[road][variable]).collect();
            assert!(is_root(&root));
            let [p, q] = root_coordinates(&root);
            let ward = ward_bridge(p, q);
            assert_eq!(ward_contact(ward), [0; 6]);
            ward
        })
        .collect();
    let matrix: Matrix = (0..7)
        .map(|row| columns.iter().map(|column| column[row]).collect())
        .collect();

    // This is Theta o Gamma on every symbolic boundary-variable column.
    let expected = vec![
        vec![0, -1, -1, 0, 1, 1],
        vec![-1, -1, 0, 1, 1, 0],
        vec![0, 1, 1, 0, -1, -1],
        vec![1, 1, 0, -1, -1, 0],
        vec![-1, -1, 0, 1, 1, 0],
        vec![0, 1, 1, 0, -1, -1],
        vec![1, 0, -1, -1, 0, 1],
    ];
    assert_eq!(matrix, expected);

    // The typed D6 generators also act on the six boundary variables:
    // external rotation j |-> j+1, and reflection j |-> 1-j mod 6.
    let generators = [
        (1, false, true, [1, 2, 3, 4, 5, 0]),
        (0, true, false, [1, 0, 5, 4, 3, 2]),
    ];
    let mut covariance_checks = 0;
    for (rotation, reflected, core_swap, variables) in generators {
        for source in 0..6 {
            let root: Vector = (0..3).map(|road| contact[road][source]).collect();
            let target = variables[source];
            let target_root: Vector = (0..3).map(|road| contact[road][target]).collect();
            assert_eq!(
                root_action(&root, rotation, reflected, core_swap),
                target_root
            );
            assert_eq!(
                ward_action(columns[source], rotation, reflected, core_swap),
                columns[target]
            );
            covariance_checks += 2;
        }
    }
    (matrix, covariance_checks)
}

fn audit_characters_and_green_covariance() -> usize {
    let relation = RELATION.to_vec();
    let roots = [root_from_coordinates([1, 0]), root_from_coordinates([0, 1])];
    let mut checks = 0;
    for sheet in [false, true] {
        for reflected in [false, true] {
            for rotation in 0..3 {
                assert_eq!(
                    tag_action(&relation, rotation, reflected, sheet),
                    scale(relation_character(reflected, sheet), &relation)
                );
                for root in &roots {
                    let transformed_root = root_action(root, rotation, reflected, sheet);
                    assert_eq!(
                        green_numerator(&transformed_root),
                        tag_action(&green_numerator(root), rotation, reflected, sheet,)
                    );
                    assert_eq!(
                        class_map(&tag_action(
                            &green_numerator(root),
                            rotation,
                            reflected,
                            sheet,
                        )),
                        scale(3, &transformed_root)
                    );
                    checks += 2;
                }
            }
        }
    }
    checks
}

// Unknown ordering for the comparison equations:
//   f2;
//   f1(row,column), 0<=row,column<3;
//   f0(row,column), 0<=row,column<2.
const UNKNOWNS: usize = 14;

fn f1_index(row: usize, column: usize) -> usize {
    1 + 3 * row + column
}

fn f0_index(row: usize, column: usize) -> usize {
    10 + 2 * row + column
}

fn add_equation(equations: &mut Matrix, terms: &[(usize, i64)]) {
    let mut row = vec![0; UNKNOWNS];
    for &(index, coefficient) in terms {
        row[index] += coefficient;
    }
    equations.push(row);
}

fn comparison_equations() -> Matrix {
    // B in the basis u0=e0-e2, u1=e1-e2 of A2.
    let reduced_boundary = vec![vec![1, 0, -1], vec![-1, 1, 0]];
    let mut equations = Vec::new();

    // reduced_boundary F1 = F0 reduced_boundary.
    for row in 0..2 {
        for column in 0..3 {
            let mut terms = Vec::new();
            for middle in 0..3 {
                terms.push((f1_index(middle, column), reduced_boundary[row][middle]));
            }
            for middle in 0..2 {
                terms.push((f0_index(row, middle), -reduced_boundary[middle][column]));
            }
            add_equation(&mut equations, &terms);
        }
    }

    // F1 d2 = d2 F2.
    for row in 0..3 {
        let mut terms = vec![(0, -1)];
        for column in 0..3 {
            terms.push((f1_index(row, column), 1));
        }
        add_equation(&mut equations, &terms);
    }

    // D3 covariance.  The sheet/core involution is -I in every degree and
    // therefore adds no new equation once it has been identified.
    for (rotation, reflected) in [(1, false), (0, true)] {
        let tag_action = action_matrix_tags(rotation, reflected);
        let root_action = action_matrix_roots(rotation, reflected);

        // F1 A1 - A1 F1 = 0.
        for row in 0..3 {
            for column in 0..3 {
                let mut terms = Vec::new();
                for middle in 0..3 {
                    terms.push((f1_index(row, middle), tag_action[middle][column]));
                    terms.push((f1_index(middle, column), -tag_action[row][middle]));
                }
                add_equation(&mut equations, &terms);
            }
        }

        // F0 A0 - A0 F0 = 0.
        for row in 0..2 {
            for column in 0..2 {
                let mut terms = Vec::new();
                for middle in 0..2 {
                    terms.push((f0_index(row, middle), root_action[middle][column]));
                    terms.push((f0_index(middle, column), -root_action[row][middle]));
                }
                add_equation(&mut equations, &terms);
            }
        }
    }
    equations
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Rat {
    numerator: i128,
    denominator: i128,
}

impl Rat {
    fn new(mut numerator: i128, mut denominator: i128) -> Self {
        assert_ne!(denominator, 0);
        if denominator < 0 {
            numerator = -numerator;
            denominator = -denominator;
        }
        let divisor = gcd(numerator.abs(), denominator);
        Self {
            numerator: numerator / divisor,
            denominator: denominator / divisor,
        }
    }

    const ZERO: Self = Self {
        numerator: 0,
        denominator: 1,
    };

    fn subtract(self, other: Self) -> Self {
        Self::new(
            self.numerator * other.denominator - other.numerator * self.denominator,
            self.denominator * other.denominator,
        )
    }

    fn multiply(self, other: Self) -> Self {
        Self::new(
            self.numerator * other.numerator,
            self.denominator * other.denominator,
        )
    }

    fn divide(self, other: Self) -> Self {
        Self::new(
            self.numerator * other.denominator,
            self.denominator * other.numerator,
        )
    }
}

fn gcd(mut left: i128, mut right: i128) -> i128 {
    while right != 0 {
        let remainder = left % right;
        left = right;
        right = remainder;
    }
    left.max(1)
}

fn rational_rank(matrix: &Matrix) -> usize {
    let mut work: Vec<Vec<Rat>> = matrix
        .iter()
        .map(|row| {
            row.iter()
                .map(|&entry| Rat::new(i128::from(entry), 1))
                .collect()
        })
        .collect();
    let mut pivot_row = 0;
    for column in 0..matrix[0].len() {
        let Some(found) = (pivot_row..work.len()).find(|&row| work[row][column] != Rat::ZERO)
        else {
            continue;
        };
        work.swap(pivot_row, found);
        let pivot = work[pivot_row][column];
        for entry in column..work[0].len() {
            work[pivot_row][entry] = work[pivot_row][entry].divide(pivot);
        }
        for row in 0..work.len() {
            if row == pivot_row || work[row][column] == Rat::ZERO {
                continue;
            }
            let factor = work[row][column];
            for entry in column..work[0].len() {
                work[row][entry] =
                    work[row][entry].subtract(factor.multiply(work[pivot_row][entry]));
            }
        }
        pivot_row += 1;
        if pivot_row == work.len() {
            break;
        }
    }
    pivot_row
}

fn comparison_vector(a: i64, b: i64) -> Vector {
    let mut result = vec![0; UNKNOWNS];
    result[0] = a + 3 * b;
    for row in 0..3 {
        for column in 0..3 {
            result[f1_index(row, column)] = a * i64::from(row == column) + b;
        }
    }
    for row in 0..2 {
        for column in 0..2 {
            result[f0_index(row, column)] = a * i64::from(row == column);
        }
    }
    result
}

fn equations_annihilate(equations: &Matrix, vector: &[i64]) -> bool {
    equations
        .iter()
        .all(|row| row.iter().zip(vector).map(|(a, b)| a * b).sum::<i64>() == 0)
}

fn audit_comparison_classification() -> usize {
    let equations = comparison_equations();
    let rank = rational_rank(&equations);
    assert_eq!(rank, UNKNOWNS - 2);

    let a_generator = comparison_vector(1, 0);
    let b_generator = comparison_vector(0, 1);
    assert!(equations_annihilate(&equations, &a_generator));
    assert!(equations_annihilate(&equations, &b_generator));
    // These coordinates recover the parameters integrally.  Since the
    // rational kernel has dimension two, every integral solution is uniquely
    // a,b in Z with the displayed formula.
    assert_eq!(a_generator[f0_index(0, 0)], 1);
    assert_eq!(a_generator[f1_index(0, 1)], 0);
    assert_eq!(b_generator[f0_index(0, 0)], 0);
    assert_eq!(b_generator[f1_index(0, 1)], 1);

    // On every sum-zero Green current, J vanishes, so boundary and symmetry
    // equations alone do not select a.  Both zero and identity satisfy those
    // equations.
    let current = green_numerator(&root_from_coordinates([1, 0]));
    let j_current = vec![current.iter().sum::<i64>(); 3];
    assert_eq!(j_current, vec![0; 3]);
    assert!(equations_annihilate(&equations, &comparison_vector(0, 0)));
    assert!(equations_annihilate(&equations, &comparison_vector(1, 0)));

    // The incidence carrier supplies the missing normalization: a named
    // triangle edge maps to the individually named adjacent four-circuit,
    // not that circuit plus b times the diagonal relation.  Thus F1=I, and
    // the chain equations force F0=I and F2=I: a=1,b=0.
    let carrier_comparison = comparison_vector(1, 0);
    assert_eq!(carrier_comparison[0], 1);
    for row in 0..3 {
        for column in 0..3 {
            assert_eq!(
                carrier_comparison[f1_index(row, column)],
                i64::from(row == column)
            );
        }
    }
    for row in 0..2 {
        for column in 0..2 {
            assert_eq!(
                carrier_comparison[f0_index(row, column)],
                i64::from(row == column)
            );
        }
    }
    equations.len()
}

fn audit_cut_typing_obstruction() {
    // The punctured-torus state certificate says that cutting road k retains
    // the unique circuit on the complementary pair.  With t_i the circuit on
    // roads (i,i+1), the resulting count functional is kappa_k(t)=t_{k+1}.
    // It does not kill the cellular relation and therefore cannot be the
    // degree-zero part of a chain map into a target concentrated in degree 0.
    for cut_road in 0..3 {
        let retained_tag = (cut_road + 1) % 3;
        assert_eq!(RELATION[retained_tag], 1);
    }
    assert_eq!(RELATION.iter().sum::<i64>(), 3); // orbit Cut

    // A naive attempt to match this count to the six-point QTDS physical
    // residue already fails on the first root: QTDS Hodge coefficients are
    // contact polynomials (zero physical pole residue), whereas the retained
    // Ward tag coefficient is nonzero.  This is not a physical contradiction:
    // the two Cuts have different topology and the Ward count has not been
    // lifted to the oriented relation complex.
    let numerator = green_numerator(&root_from_coordinates([1, 0]));
    assert_eq!(numerator, vec![1, 1, -2]);
    assert_ne!(numerator[1], 0); // cut road 0 retains t_1
}

fn main() {
    audit_cellular_hodge_square();
    let (suspension_covariance_checks, automorphisms) = audit_suspension_carrier();
    audit_ward_source_typing();
    let (symbolic_ward_matrix, symbolic_covariance_checks) = audit_symbolic_qtds_to_ward();
    let covariance_checks = audit_characters_and_green_covariance();
    let comparison_equations = audit_comparison_classification();
    audit_cut_typing_obstruction();

    println!("m=3 QTDS--Ward Hodge comparison certificate");
    println!("=============================================");
    println!("  cellular modules: Z -> Z^3 -> A2");
    println!("  B = [[1,0,-1],[-1,1,0],[0,-1,1]]");
    println!("  d2(1) = (1,1,1)");
    println!("  QTDS and Ward Green current: sigma(c)=B^T c/3");
    println!("  polarity-channel carrier: K2,3 = S0 * R3");
    println!("  suspension Gamma: A2 ~= H1(K2,3), primitive and integral");
    println!("  suspension/tag covariance checks: {suspension_covariance_checks}");
    println!("  generated D6 / all K2,3 automorphisms: 12/{automorphisms}");
    println!("  D3 x sheet/core covariance checks: {covariance_checks}");
    println!("  comparison equations: {comparison_equations}, rank 12, nullity 2");
    println!("  all comparisons: F0=aI, F1=aI+bJ, F2=a+3b");
    println!("  support-preserving suspension selects: a=1, b=0");
    println!(
        "  symbolic Theta o Gamma matrix: {}x{}; Ward-kernel columns: 6/6",
        symbolic_ward_matrix.len(),
        symbolic_ward_matrix[0].len()
    );
    println!("  symbolic D6 coefficient checks: {symbolic_covariance_checks}");
    println!();
    println!("PROOF STATUS");
    println!("  exact common cellular/Hodge skeleton: PROVED");
    println!("  canonical combinatorial carrier comparison: PROVED");
    println!("  explicit QTDS-to-Ward coefficient-module map: PROVED");
    println!("  physical first-jet coefficient comparison: NOT CONSTRUCTED");
    println!("  physical Cut square: NOT TYPED");
    println!("  missing map: oriented edge-Cut into an annulus/open-curve target,");
    println!("               including the image of the relation generator");
}
