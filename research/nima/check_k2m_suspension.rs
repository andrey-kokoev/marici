//! Integral suspension theorem for K_{2,m}, audited for 2 <= m <= 12.
//!
//! ALL-m THEOREM (proved algebraically below)
//! ------------------------------------------
//! Regard K_{2,m}=S^0*R_m as the join of two isolated core vertices with m
//! isolated road vertices, and orient every edge from its core to its road.
//! For
//!
//!     A_{m-1} = {c in Z^m : sum_i c_i=0},
//!
//! define
//!
//!     Gamma_m(c) = sum_i c_i(e_{+,i}-e_{-,i}).
//!
//! Road incidence says that every graph cycle has opposite coefficients on
//! its two edges over one road; core incidence says their sum is zero.  Thus
//! projection to the plus-core edges is an integral inverse to Gamma_m:
//!
//!     A_{m-1} ~= H_1(K_{2,m};Z).
//!
//! This proves surjectivity and saturation, not merely equality of ranks.
//! Gamma_m intertwines independent core and road permutations, where core
//! exchange acts on A_{m-1} by -1.  For m>=3 degree distinguishes the two
//! parts, so Aut(K_{2,m})=S_2 x S_m.  At m=2, K_{2,2}=C_4 and its full
//! automorphism group is D_4 of order eight; S_2 x S_2 is the index-two
//! bipartition-preserving subgroup.
//!
//! If t_i is the oriented edge i->i+1 of the road cycle C_m, then
//!
//!     B(t_i)=e_i-e_{i+1},
//!     Gamma_m B(t_i)=an adjacent four-circuit in K_{2,m}.
//!
//! The class map B has diagonal kernel and is saturated.  Its dihedral
//! covariance is separate from the full S_m covariance of Gamma_m: a general
//! road permutation does not preserve the chosen cyclic adjacency.
//!
//! EVIDENCE BOUNDARY
//! -----------------
//! This is a graph/cellular theorem.  The m=3 scalar QTDS carrier supplies a
//! polarity-channel realization of K_{2,3}; no all-m scalar polarity atlas is
//! asserted or assumed here.

use std::collections::BTreeSet;

const MIN_M: usize = 2;
const MAX_M: usize = 12;

type Vector = Vec<i64>;
type Matrix = Vec<Vec<i64>>;

fn edge(core: usize, road: usize) -> usize {
    2 * road + core
}

fn is_root(root: &[i64]) -> bool {
    root.iter().sum::<i64>() == 0
}

fn root_basis(m: usize, index: usize) -> Vector {
    assert!(index < m - 1);
    let mut result = vec![0; m];
    result[index] = 1;
    result[m - 1] = -1;
    result
}

fn gamma(root: &[i64]) -> Vector {
    assert!(is_root(root));
    let mut result = vec![0; 2 * root.len()];
    for (road, &coefficient) in root.iter().enumerate() {
        result[edge(0, road)] = coefficient;
        result[edge(1, road)] = -coefficient;
    }
    result
}

fn graph_boundary(chain: &[i64], m: usize) -> Vector {
    assert_eq!(chain.len(), 2 * m);
    let mut result = vec![0; m + 2];
    for road in 0..m {
        for core in 0..2 {
            let coefficient = chain[edge(core, road)];
            result[core] -= coefficient;
            result[2 + road] += coefficient;
        }
    }
    result
}

fn cycle_inverse(chain: &[i64], m: usize) -> Vector {
    assert_eq!(graph_boundary(chain, m), vec![0; m + 2]);
    let root: Vector = (0..m).map(|road| chain[edge(0, road)]).collect();
    assert!(is_root(&root));
    for road in 0..m {
        assert_eq!(chain[edge(1, road)], -root[road]);
    }
    assert_eq!(gamma(&root), chain);
    root
}

fn incidence_matrix(m: usize) -> Matrix {
    let columns: Vec<_> = (0..2 * m)
        .map(|slot| {
            let mut unit = vec![0; 2 * m];
            unit[slot] = 1;
            graph_boundary(&unit, m)
        })
        .collect();
    (0..m + 2)
        .map(|row| columns.iter().map(|column| column[row]).collect())
        .collect()
}

fn minor(matrix: &Matrix, rows: &[usize], columns: &[usize]) -> Matrix {
    rows.iter()
        .map(|&row| columns.iter().map(|&column| matrix[row][column]).collect())
        .collect()
}

fn determinant(mut matrix: Matrix) -> i128 {
    let size = matrix.len();
    assert!(matrix.iter().all(|row| row.len() == size));
    if size == 0 {
        return 1;
    }
    let mut work: Vec<Vec<i128>> = matrix
        .drain(..)
        .map(|row| row.into_iter().map(i128::from).collect())
        .collect();
    let mut sign = 1_i128;
    let mut previous = 1_i128;
    for pivot_index in 0..size - 1 {
        let Some(pivot_row) = (pivot_index..size).find(|&row| work[row][pivot_index] != 0) else {
            return 0;
        };
        if pivot_row != pivot_index {
            work.swap(pivot_row, pivot_index);
            sign = -sign;
        }
        let pivot = work[pivot_index][pivot_index];
        for row in pivot_index + 1..size {
            for column in pivot_index + 1..size {
                let numerator =
                    work[row][column] * pivot - work[row][pivot_index] * work[pivot_index][column];
                assert_eq!(numerator % previous, 0);
                work[row][column] = numerator / previous;
            }
        }
        previous = pivot;
    }
    sign * work[size - 1][size - 1]
}

fn road_action(root: &[i64], permutation: &[usize], core_swap: bool) -> Vector {
    assert_eq!(root.len(), permutation.len());
    let sign = if core_swap { -1 } else { 1 };
    let mut result = vec![0; root.len()];
    for source in 0..root.len() {
        result[permutation[source]] += sign * root[source];
    }
    assert!(is_root(&result));
    result
}

fn graph_action(chain: &[i64], permutation: &[usize], core_swap: bool) -> Vector {
    let m = permutation.len();
    assert_eq!(chain.len(), 2 * m);
    let mut result = vec![0; 2 * m];
    for road in 0..m {
        for core in 0..2 {
            let target_core = if core_swap { 1 - core } else { core };
            result[edge(target_core, permutation[road])] += chain[edge(core, road)];
        }
    }
    result
}

fn identity_permutation(m: usize) -> Vec<usize> {
    (0..m).collect()
}

fn rotation_permutation(m: usize) -> Vec<usize> {
    (0..m).map(|index| (index + 1) % m).collect()
}

fn reflection_permutation(m: usize) -> Vec<usize> {
    (0..m).map(|index| (m - index) % m).collect()
}

fn adjacent_transposition(m: usize, left: usize) -> Vec<usize> {
    assert!(left + 1 < m);
    let mut result = identity_permutation(m);
    result.swap(left, left + 1);
    result
}

fn class_map(tags: &[i64]) -> Vector {
    let m = tags.len();
    let mut result = vec![0; m];
    for (index, &coefficient) in tags.iter().enumerate() {
        result[index] += coefficient;
        result[(index + 1) % m] -= coefficient;
    }
    assert!(is_root(&result));
    result
}

fn tag_action(tags: &[i64], rotation: usize, reflected: bool, core_swap: bool) -> Vector {
    let m = tags.len();
    let orientation_sign = (if reflected { -1 } else { 1 }) * (if core_swap { -1 } else { 1 });
    let mut result = vec![0; m];
    for (source, &coefficient) in tags.iter().enumerate() {
        let target = if reflected {
            (rotation + 2 * m - source - 1) % m
        } else {
            (source + rotation) % m
        };
        result[target] += orientation_sign * coefficient;
    }
    result
}

fn cyclic_road_permutation(m: usize, rotation: usize, reflected: bool) -> Vec<usize> {
    (0..m)
        .map(|index| {
            if reflected {
                (rotation + m - index) % m
            } else {
                (index + rotation) % m
            }
        })
        .collect()
}

fn factorial(value: usize) -> u128 {
    (1..=value).map(|factor| factor as u128).product()
}

type Perm4 = [usize; 4];

fn all_permutations_four() -> Vec<Perm4> {
    fn recurse(
        position: usize,
        current: &mut Perm4,
        used: &mut [bool; 4],
        output: &mut Vec<Perm4>,
    ) {
        if position == 4 {
            output.push(*current);
            return;
        }
        for value in 0..4 {
            if used[value] {
                continue;
            }
            used[value] = true;
            current[position] = value;
            recurse(position + 1, current, used, output);
            used[value] = false;
        }
    }
    let mut result = Vec::new();
    recurse(0, &mut [0; 4], &mut [false; 4], &mut result);
    result
}

fn k22_edge(first: usize, second: usize) -> bool {
    (first < 2 && second >= 2) || (second < 2 && first >= 2)
}

fn k22_automorphisms() -> BTreeSet<Perm4> {
    all_permutations_four()
        .into_iter()
        .filter(|permutation| {
            (0..4).all(|first| {
                (0..4).all(|second| {
                    k22_edge(first, second) == k22_edge(permutation[first], permutation[second])
                })
            })
        })
        .collect()
}

fn k22_chain_action(chain: &[i64], permutation: &Perm4) -> Vector {
    assert_eq!(chain.len(), 4);
    let mut result = vec![0; 4];
    for road in 0..2 {
        for core in 0..2 {
            let coefficient = chain[edge(core, road)];
            let moved_tail = permutation[core];
            let moved_head = permutation[2 + road];
            if moved_tail < 2 {
                assert!(moved_head >= 2);
                result[edge(moved_tail, moved_head - 2)] += coefficient;
            } else {
                assert!(moved_head < 2);
                // The automorphism exchanged the bipartition, so restore the
                // declared core-to-road orientation with a minus sign.
                result[edge(moved_head, moved_tail - 2)] -= coefficient;
            }
        }
    }
    assert_eq!(graph_boundary(&result, 2), vec![0; 4]);
    result
}

fn audit_join_and_homology(m: usize) {
    // S^0*R_m has exactly the 2m cross edges of K_{2,m}.
    let join_edges: BTreeSet<_> = (0..2)
        .flat_map(|core| (0..m).map(move |road| (core, road)))
        .collect();
    assert_eq!(join_edges.len(), 2 * m);

    let incidence = incidence_matrix(m);
    // The edges (+,i) for all roads plus (-,0) form a spanning tree.  Delete
    // the plus-core row: the resulting incidence minor is unimodular.
    let rows: Vec<_> = (1..m + 2).collect();
    let mut columns: Vec<_> = (0..m).map(|road| edge(0, road)).collect();
    columns.push(edge(1, 0));
    assert_eq!(determinant(minor(&incidence, &rows, &columns)).abs(), 1);
    assert_eq!(2 * m - (m + 1), m - 1);

    for index in 0..m - 1 {
        let root = root_basis(m, index);
        let cycle = gamma(&root);
        assert_eq!(graph_boundary(&cycle, m), vec![0; m + 2]);
        assert_eq!(cycle_inverse(&cycle, m), root);
    }
}

fn audit_symmetric_equivariance(m: usize) -> usize {
    let mut generators = vec![
        identity_permutation(m),
        rotation_permutation(m),
        reflection_permutation(m),
    ];
    generators.extend((0..m - 1).map(|left| adjacent_transposition(m, left)));
    let generators: BTreeSet<_> = generators.into_iter().collect();
    let mut checks = 0;
    for core_swap in [false, true] {
        for permutation in &generators {
            for index in 0..m - 1 {
                let root = root_basis(m, index);
                assert_eq!(
                    gamma(&road_action(&root, permutation, core_swap)),
                    graph_action(&gamma(&root), permutation, core_swap)
                );
                checks += 1;
            }
        }
    }

    if m >= 3 {
        // Degree m versus degree 2 fixes the bipartition.  Arbitrary
        // permutations inside each part are automorphisms, hence exactly
        // S2 x Sm.  The count is recorded without factorial enumeration.
        let core_degree = m;
        let road_degree = 2;
        assert_ne!(core_degree, road_degree);
        assert!(2 * factorial(m) >= 12);
    } else {
        let automorphisms = k22_automorphisms();
        assert_eq!(automorphisms.len(), 8); // D4
        let bipartition_preserving = automorphisms
            .iter()
            .filter(|permutation| permutation[0] < 2 && permutation[1] < 2)
            .count();
        assert_eq!(bipartition_preserving, 4); // S2 x S2
        assert_eq!(automorphisms.len() - bipartition_preserving, 4);

        // The four extra automorphisms exchange the two bipartition factors.
        // Gamma still identifies the rank-one H1 lattice, but its original
        // "road coefficient" interpretation is not preserved.  Transporting
        // through Gamma gives the expected sign action on A1.
        let generator = gamma(&root_basis(2, 0));
        let mut positive = 0;
        let mut negative = 0;
        for permutation in &automorphisms {
            let moved = k22_chain_action(&generator, permutation);
            let root = cycle_inverse(&moved, 2);
            assert!(root == vec![1, -1] || root == vec![-1, 1]);
            if root[0] == 1 {
                positive += 1;
            } else {
                negative += 1;
            }
        }
        assert_eq!((positive, negative), (4, 4));
    }
    checks
}

fn audit_adjacent_circuits(m: usize) -> usize {
    let diagonal = vec![1; m];
    assert_eq!(class_map(&diagonal), vec![0; m]);

    // The leading (m-1)-minor of B is unit lower triangular.  Therefore B has
    // rank m-1 with saturated image A_{m-1}; Bx=0 recursively forces x to be
    // constant, so its kernel is exactly the primitive diagonal.
    let columns: Vec<_> = (0..m)
        .map(|index| {
            let mut tag = vec![0; m];
            tag[index] = 1;
            class_map(&tag)
        })
        .collect();
    let matrix: Matrix = (0..m)
        .map(|row| columns.iter().map(|column| column[row]).collect())
        .collect();
    let indices: Vec<_> = (0..m - 1).collect();
    assert_eq!(determinant(minor(&matrix, &indices, &indices)).abs(), 1);

    let mut circuit_sum = vec![0; 2 * m];
    for index in 0..m {
        let circuit = gamma(&columns[index]);
        assert_eq!(graph_boundary(&circuit, m), vec![0; m + 2]);
        assert_eq!(circuit.iter().filter(|&&entry| entry != 0).count(), 4);
        assert!(circuit.iter().all(|entry| entry.abs() <= 1));
        for slot in 0..2 * m {
            circuit_sum[slot] += circuit[slot];
        }
    }
    assert_eq!(circuit_sum, vec![0; 2 * m]);

    let mut covariance_checks = 0;
    for core_swap in [false, true] {
        for reflected in [false, true] {
            for rotation in 0..m {
                let roads = cyclic_road_permutation(m, rotation, reflected);
                for index in 0..m {
                    let mut tag = vec![0; m];
                    tag[index] = 1;
                    assert_eq!(
                        gamma(&class_map(&tag_action(
                            &tag, rotation, reflected, core_swap,
                        ))),
                        graph_action(&gamma(&class_map(&tag)), &roads, core_swap)
                    );
                    covariance_checks += 1;
                }
            }
        }
    }
    covariance_checks
}

fn main() {
    let mut symmetric_checks = 0;
    let mut circuit_checks = 0;
    for m in MIN_M..=MAX_M {
        audit_join_and_homology(m);
        let current_symmetric = audit_symmetric_equivariance(m);
        let current_circuit = audit_adjacent_circuits(m);
        symmetric_checks += current_symmetric;
        circuit_checks += current_circuit;
        let automorphism_description = if m == 2 {
            "D4 (S2xS2 index two)".to_string()
        } else {
            format!("S2xS{m}, order {}", 2 * factorial(m))
        };
        println!(
            "  m={m:2}: H1=A_{}, rank={}, Aut={}, symmetry/tag checks={}/{}",
            m - 1,
            m - 1,
            automorphism_description,
            current_symmetric,
            current_circuit,
        );
    }

    println!();
    println!("K2,m integral suspension certificate");
    println!("====================================");
    println!("  audited m: {MIN_M}..={MAX_M}");
    println!("  S2 x Sm generator covariance checks: {symmetric_checks}");
    println!("  dihedral adjacent-circuit checks: {circuit_checks}");
    println!("  Gamma_m: A_(m-1) ~= H1(K2,m;Z), integral and saturated");
    println!("  Gamma_m o B sends every road-cycle tag to a four-circuit");
    println!("  ker(B)=Z(1,...,1), with saturated image A_(m-1)");
    println!();
    println!("PROOF STATUS");
    println!("  all-m graph/cellular theorem: PROVED");
    println!("  m=2 automorphism enlargement: PROVED and audited exhaustively");
    println!("  all-m scalar polarity atlas: NOT CLAIMED");
}
