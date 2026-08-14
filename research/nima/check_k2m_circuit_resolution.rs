//! Exact integral circuit-tag resolution for K_{2,m}, 2 <= m <= 12.
//!
//! All 2m graph edges are oriented from one of two core vertices to one of m
//! road vertices.  Graph cycles are therefore
//!
//!     (a_0,-a_0, ..., a_{m-1},-a_{m-1}),  sum_i a_i = 0,
//!
//! so H_1(K_{2,m};Z) is the root lattice A_{m-1}.  The m oriented adjacent
//! circuit tags have classes c_i=e_i-e_{i+1} (indices modulo m).  This file
//! audits the exact sequence
//!
//!     0 -> Z_diagonal -> Z^m_tags -> A_{m-1} -> 0,
//!
//! its D_m x C_2(core-swap) covariance, its integral Smith data, and the
//! denominator-m obstruction to an equivariant additive section.
//!
//! This is only a lattice theorem.  It does not identify these formal circuit
//! tags with coefficients or chain-level states of the scalar/Brauer carrier.

const MIN_M: usize = 2;
const MAX_M: usize = 12;

type Vector = Vec<i64>;
type Matrix = Vec<Vec<i64>>;

fn determinant(matrix: &Matrix) -> i128 {
    let size = matrix.len();
    assert!(matrix.iter().all(|row| row.len() == size));
    if size == 0 {
        return 1;
    }
    let mut work: Vec<Vec<i128>> = matrix
        .iter()
        .map(|row| row.iter().map(|&entry| i128::from(entry)).collect())
        .collect();
    let mut sign = 1_i128;
    let mut previous = 1_i128;
    for pivot_column in 0..size - 1 {
        let Some(pivot_row) = (pivot_column..size)
            .find(|&row| work[row][pivot_column] != 0)
        else {
            return 0;
        };
        if pivot_row != pivot_column {
            work.swap(pivot_row, pivot_column);
            sign = -sign;
        }
        let pivot = work[pivot_column][pivot_column];
        for row in pivot_column + 1..size {
            for column in pivot_column + 1..size {
                let numerator = work[row][column] * pivot
                    - work[row][pivot_column] * work[pivot_column][column];
                assert_eq!(numerator % previous, 0);
                work[row][column] = numerator / previous;
            }
        }
        previous = pivot;
    }
    sign * work[size - 1][size - 1]
}

fn combinations(size: usize, choose: usize) -> Vec<Vec<usize>> {
    fn recurse(
        next: usize,
        size: usize,
        remaining: usize,
        current: &mut Vec<usize>,
        output: &mut Vec<Vec<usize>>,
    ) {
        if remaining == 0 {
            output.push(current.clone());
            return;
        }
        for value in next..=size - remaining {
            current.push(value);
            recurse(value + 1, size, remaining - 1, current, output);
            current.pop();
        }
    }
    let mut output = Vec::new();
    recurse(0, size, choose, &mut Vec::new(), &mut output);
    output
}

fn minor(matrix: &Matrix, rows: &[usize], columns: &[usize]) -> Matrix {
    rows.iter()
        .map(|&row| columns.iter().map(|&column| matrix[row][column]).collect())
        .collect()
}

fn has_unit_minor(matrix: &Matrix, size: usize) -> bool {
    let row_sets = combinations(matrix.len(), size);
    let column_sets = combinations(matrix[0].len(), size);
    row_sets.iter().any(|rows| {
        column_sets
            .iter()
            .any(|columns| determinant(&minor(matrix, rows, columns)).abs() == 1)
    })
}

fn identity(size: usize) -> Matrix {
    (0..size)
        .map(|row| {
            (0..size)
                .map(|column| i64::from(row == column))
                .collect()
        })
        .collect()
}

fn matrix_subtract(left: &Matrix, right: &Matrix) -> Matrix {
    assert_eq!(left.len(), right.len());
    left.iter()
        .zip(right)
        .map(|(left_row, right_row)| {
            assert_eq!(left_row.len(), right_row.len());
            left_row
                .iter()
                .zip(right_row)
                .map(|(left_entry, right_entry)| left_entry - right_entry)
                .collect()
        })
        .collect()
}

fn standard_basis(size: usize, index: usize) -> Vector {
    let mut result = vec![0; size];
    result[index] = 1;
    result
}

fn root_basis_vector(m: usize, index: usize) -> Vector {
    assert!(index < m - 1);
    let mut result = standard_basis(m, index);
    result[m - 1] = -1;
    result
}

fn is_root(vector: &[i64]) -> bool {
    vector.iter().sum::<i64>() == 0
}

fn root_coordinates(vector: &[i64]) -> Vector {
    assert!(is_root(vector));
    vector[..vector.len() - 1].to_vec()
}

fn edge(core: usize, road: usize) -> usize {
    2 * road + core
}

fn graph_chain(root: &[i64]) -> Vector {
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

fn graph_incidence_matrix(m: usize) -> Matrix {
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

fn class_matrix(m: usize) -> Matrix {
    let columns: Vec<_> = (0..m)
        .map(|index| class_map(&standard_basis(m, index)))
        .collect();
    (0..m)
        .map(|row| columns.iter().map(|column| column[row]).collect())
        .collect()
}

fn restricted_class_matrix(m: usize) -> Matrix {
    let columns: Vec<_> = (0..m - 1)
        .map(|index| root_coordinates(&class_map(&root_basis_vector(m, index))))
        .collect();
    (0..m - 1)
        .map(|row| columns.iter().map(|column| column[row]).collect())
        .collect()
}

fn road_permutation(m: usize, rotation: usize, reflected: bool) -> Vec<usize> {
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

fn permutation_sign(permutation: &[usize]) -> i64 {
    let inversions = (0..permutation.len())
        .flat_map(|left| ((left + 1)..permutation.len()).map(move |right| (left, right)))
        .filter(|&(left, right)| permutation[left] > permutation[right])
        .count();
    if inversions % 2 == 0 { 1 } else { -1 }
}

fn root_action(
    root: &[i64],
    rotation: usize,
    reflected: bool,
    core_swap: bool,
) -> Vector {
    let permutation = road_permutation(root.len(), rotation, reflected);
    let core_sign = if core_swap { -1 } else { 1 };
    let mut result = vec![0; root.len()];
    for (source, &coefficient) in root.iter().enumerate() {
        result[permutation[source]] += core_sign * coefficient;
    }
    assert!(is_root(&result));
    result
}

fn tag_action(
    tags: &[i64],
    rotation: usize,
    reflected: bool,
    core_swap: bool,
) -> Vector {
    let m = tags.len();
    let core_sign = if core_swap { -1 } else { 1 };
    let reflection_sign = if reflected { -1 } else { 1 };
    let mut result = vec![0; m];
    for (source, &coefficient) in tags.iter().enumerate() {
        let target = if reflected {
            (rotation + 2 * m - source - 1) % m
        } else {
            (source + rotation) % m
        };
        result[target] += core_sign * reflection_sign * coefficient;
    }
    result
}

fn graph_chain_action(
    chain: &[i64],
    m: usize,
    rotation: usize,
    reflected: bool,
    core_swap: bool,
) -> Vector {
    let permutation = road_permutation(m, rotation, reflected);
    let mut result = vec![0; 2 * m];
    for road in 0..m {
        for core in 0..2 {
            let target_core = if core_swap { 1 - core } else { core };
            result[edge(target_core, permutation[road])] += chain[edge(core, road)];
        }
    }
    result
}

fn action_matrix_on_roots(
    m: usize,
    rotation: usize,
    reflected: bool,
    core_swap: bool,
) -> Matrix {
    let columns: Vec<_> = (0..m - 1)
        .map(|index| {
            root_coordinates(&root_action(
                &root_basis_vector(m, index),
                rotation,
                reflected,
                core_swap,
            ))
        })
        .collect();
    (0..m - 1)
        .map(|row| columns.iter().map(|column| column[row]).collect())
        .collect()
}

fn action_matrix_on_tags(
    m: usize,
    rotation: usize,
    reflected: bool,
    core_swap: bool,
) -> Matrix {
    let columns: Vec<_> = (0..m)
        .map(|index| {
            tag_action(
                &standard_basis(m, index),
                rotation,
                reflected,
                core_swap,
            )
        })
        .collect();
    (0..m)
        .map(|row| columns.iter().map(|column| column[row]).collect())
        .collect()
}

// Returns m times the unique rotation-equivariant rational section whose tag
// coefficients sum to zero.
fn rational_section_numerator(root: &[i64]) -> Vector {
    assert!(is_root(root));
    let m = root.len();
    let weighted_tail: i64 = (1..m)
        .map(|index| i64::try_from(m - index).expect("small m") * root[index])
        .sum();
    let mut result = vec![0; m];
    result[0] = -weighted_tail;
    let scale = i64::try_from(m).expect("small m");
    for index in 1..m {
        result[index] = result[index - 1] + scale * root[index];
    }
    assert_eq!(result.iter().sum::<i64>(), 0);
    let mapped = class_map(&result);
    assert_eq!(
        mapped,
        root.iter().map(|coefficient| scale * coefficient).collect::<Vector>()
    );
    result
}

fn scalar_multiple(vector: &[i64], coefficient: i64) -> Vector {
    vector.iter().map(|entry| coefficient * entry).collect()
}

fn audit_graph_homology(m: usize) {
    let incidence = graph_incidence_matrix(m);
    // A spanning tree consists of core0--every-road plus core1--road0.  Delete
    // the core0 row from its incidence matrix.  Its determinant is a unit, so
    // the graph incidence rank is m+1 and its image is saturated.
    let rows: Vec<_> = (1..m + 2).collect();
    let mut columns: Vec<_> = (0..m).map(|road| edge(0, road)).collect();
    columns.push(edge(1, 0));
    assert_eq!(determinant(&minor(&incidence, &rows, &columns)).abs(), 1);
    // Column sums vanish, giving the matching rank upper bound m+1.
    for column in 0..2 * m {
        assert_eq!(incidence.iter().map(|row| row[column]).sum::<i64>(), 0);
    }
    assert_eq!(2 * m - (m + 1), m - 1);
    for index in 0..m - 1 {
        let root = root_basis_vector(m, index);
        assert_eq!(graph_boundary(&graph_chain(&root), m), vec![0; m + 2]);
    }
}

fn audit_exact_sequence_and_smith(m: usize) -> (Vec<i64>, Vec<i64>, i128) {
    let matrix = class_matrix(m);
    let diagonal = vec![1; m];
    assert_eq!(class_map(&diagonal), vec![0; m]);
    // The leading k-by-k minor is unit lower triangular for every k<m.
    for size in 1..m {
        let indices: Vec<_> = (0..size).collect();
        assert_eq!(determinant(&minor(&matrix, &indices, &indices)).abs(), 1);
    }
    assert_eq!(determinant(&matrix), 0);
    // B(t)=0 implies t_i=t_{i-1}, so the kernel is exactly Z*diagonal.
    for index in 0..m {
        let previous = (index + m - 1) % m;
        assert_eq!(matrix[index][index], 1);
        assert_eq!(matrix[index][previous], -1);
        assert_eq!(matrix[index].iter().filter(|&&entry| entry != 0).count(), 2);
    }
    let full_smith: Vec<i64> = (0..m)
        .map(|index| if index + 1 == m { 0 } else { 1 })
        .collect();

    let restricted = restricted_class_matrix(m);
    let determinant_restricted = determinant(&restricted);
    assert_eq!(determinant_restricted.abs(), i128::try_from(m).expect("small m"));
    // Unit minors through rank-1 and determinant m give SNF(1,...,1,m).
    for size in 1..m - 1 {
        assert!(has_unit_minor(&restricted, size));
    }
    let restricted_smith: Vec<i64> = (0..m - 1)
        .map(|index| {
            if index + 1 == m - 1 {
                i64::try_from(m).expect("small m")
            } else {
                1
            }
        })
        .collect();

    // Z*diagonal plus the sum-zero tag lattice has index m in Z^m.
    let splitting_columns: Vec<_> = std::iter::once(diagonal)
        .chain((0..m - 1).map(|index| root_basis_vector(m, index)))
        .collect();
    let splitting_matrix: Matrix = (0..m)
        .map(|row| splitting_columns.iter().map(|column| column[row]).collect())
        .collect();
    assert_eq!(determinant(&splitting_matrix).abs(), i128::try_from(m).expect("small m"));
    (full_smith, restricted_smith, determinant_restricted)
}

fn audit_covariance_and_characters(m: usize) -> usize {
    let diagonal = vec![1; m];
    let mut checks = 0;
    for core_swap in [false, true] {
        for reflected in [false, true] {
            for rotation in 0..m {
                let relation_character =
                    (if reflected { -1 } else { 1 }) * (if core_swap { -1 } else { 1 });
                assert_eq!(
                    tag_action(&diagonal, rotation, reflected, core_swap),
                    scalar_multiple(&diagonal, relation_character)
                );
                for index in 0..m {
                    let tag = standard_basis(m, index);
                    assert_eq!(
                        class_map(&tag_action(&tag, rotation, reflected, core_swap)),
                        root_action(&class_map(&tag), rotation, reflected, core_swap)
                    );
                    checks += 1;
                }
                for index in 0..m - 1 {
                    let root = root_basis_vector(m, index);
                    assert_eq!(
                        graph_chain_action(
                            &graph_chain(&root),
                            m,
                            rotation,
                            reflected,
                            core_swap,
                        ),
                        graph_chain(&root_action(
                            &root,
                            rotation,
                            reflected,
                            core_swap,
                        ))
                    );
                    checks += 1;
                }

                let root_matrix =
                    action_matrix_on_roots(m, rotation, reflected, core_swap);
                let tag_matrix =
                    action_matrix_on_tags(m, rotation, reflected, core_swap);
                let road_sign = permutation_sign(&road_permutation(m, rotation, reflected));
                let expected_root_det = road_sign
                    * if core_swap && (m - 1) % 2 == 1 { -1 } else { 1 };
                assert_eq!(determinant(&root_matrix), i128::from(expected_root_det));
                assert_eq!(
                    determinant(&tag_matrix),
                    i128::from(relation_character * expected_root_det)
                );
                checks += 2;
            }
        }
    }

    // Generator characters.
    let rotation_det = if (m - 1) % 2 == 0 { 1 } else { -1 };
    assert_eq!(
        determinant(&action_matrix_on_roots(m, 1 % m, false, false)),
        rotation_det
    );
    let reflection_det = if ((m - 1) / 2) % 2 == 0 { 1 } else { -1 };
    assert_eq!(
        determinant(&action_matrix_on_roots(m, 0, true, false)),
        reflection_det
    );
    assert_eq!(
        determinant(&action_matrix_on_roots(m, 0, false, true)),
        rotation_det
    );
    checks
}

fn audit_section_obstruction(m: usize) -> usize {
    let scale = i64::try_from(m).expect("small m");
    let mut checks = 0;
    for core_swap in [false, true] {
        for reflected in [false, true] {
            for rotation in 0..m {
                for index in 0..m - 1 {
                    let root = root_basis_vector(m, index);
                    assert_eq!(
                        rational_section_numerator(&root_action(
                            &root,
                            rotation,
                            reflected,
                            core_swap,
                        )),
                        tag_action(
                            &rational_section_numerator(&root),
                            rotation,
                            reflected,
                            core_swap,
                        )
                    );
                    checks += 1;
                }
            }
        }
    }

    // The first root basis vector has numerator coefficient 1, so its reduced
    // rational lift really contains 1/m, not merely a divisor of 1/m.
    let denominator_witness = rational_section_numerator(&root_basis_vector(m, 0));
    assert_eq!(denominator_witness[0], 1);
    assert!(denominator_witness.iter().any(|entry| entry % scale != 0));

    // Rotation has no invariant functional on A_{m-1}: R-I has determinant m.
    // Therefore every rotation-equivariant section has coefficient sum zero.
    // On that sum-zero tag lattice it would invert B|A integrally, impossible
    // because det(B|A)=m>1.  This also proves uniqueness over Q.
    let rotation_minus_identity = matrix_subtract(
        &action_matrix_on_roots(m, 1 % m, false, false),
        &identity(m - 1),
    );
    assert_eq!(determinant(&rotation_minus_identity).abs(), i128::from(scale));
    assert_eq!(determinant(&restricted_class_matrix(m)).abs(), i128::from(scale));
    checks + 2
}

fn audit_m3_regression() {
    let m = 3;
    assert_eq!(
        class_matrix(m),
        vec![vec![1, 0, -1], vec![-1, 1, 0], vec![0, -1, 1]]
    );
    assert_eq!(restricted_class_matrix(m), vec![vec![2, 1], vec![-1, 1]]);
    assert_eq!(
        rational_section_numerator(&root_basis_vector(m, 0)),
        vec![1, 1, -2]
    );
    assert_eq!(
        rational_section_numerator(&root_basis_vector(m, 1)),
        vec![-1, 2, -1]
    );
    // This is the reflection [0,2,1] used in check_ward_cycle_brauer_map.rs:
    // it fixes the support of c_1 and reverses its orientation.
    assert_eq!(
        tag_action(&standard_basis(m, 1), 0, true, false),
        scalar_multiple(&standard_basis(m, 1), -1)
    );
    assert_eq!(determinant(&restricted_class_matrix(m)).abs(), 3);
}

fn main() {
    let mut total_covariance_checks = 0;
    let mut total_section_checks = 0;
    let mut rows = Vec::new();
    for m in MIN_M..=MAX_M {
        audit_graph_homology(m);
        let (full_smith, restricted_smith, restricted_determinant) =
            audit_exact_sequence_and_smith(m);
        total_covariance_checks += audit_covariance_and_characters(m);
        total_section_checks += audit_section_obstruction(m);
        rows.push((m, full_smith, restricted_smith, restricted_determinant.abs()));
    }
    audit_m3_regression();

    println!("K_{{2,m}} integral circuit-resolution certificate");
    println!("================================================");
    println!("  audited m:                              {MIN_M}..={MAX_M}");
    println!("  D_m x core-swap covariance checks:      {total_covariance_checks}");
    println!("  rational-section covariance/checks:     {total_section_checks}");
    for (m, full_smith, restricted_smith, determinant_restricted) in rows {
        println!(
            "  m={m:2}: H1 rank={:2}, SNF(B)={full_smith:?}, SNF(B|A)={restricted_smith:?}, index={determinant_restricted}",
            m - 1
        );
    }
    println!();
    println!("CHARACTERS");
    println!("  diagonal relation: rotation +1, reflection -1, core swap -1");
    println!("  det H1(g): sign(road permutation) * (-1)^((m-1)*core_swap)");
    println!();
    println!("VERDICT");
    println!("  0 -> Z(diagonal) -> Z^m_tags -> A_(m-1) -> 0 is exact and saturated");
    println!("  B restricted to the sum-zero tag lattice has SNF(1,...,1,m) and index m");
    println!("  the unique equivariant rational section has exact denominator m");
    println!("  no integral D_m-equivariant section exists (rotation alone obstructs it)");
    println!("  m=3 exactly recovers the tag relation, 1/3 section, and reflected-tag sign of check_ward_cycle_brauer_map.rs");
    println!("  no physical scalar/Brauer coefficient or chain map is asserted");
}
