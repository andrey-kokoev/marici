use std::collections::BTreeMap;

const PRIME: i64 = 2_305_843_009_213_693_951;

fn modp(x: i128) -> i64 {
    let p = PRIME as i128;
    let mut y = x % p;
    if y < 0 {
        y += p;
    }
    y as i64
}

fn pow_mod(mut a: i64, mut n: i64) -> i64 {
    let mut out = 1_i64;
    while n > 0 {
        if n & 1 == 1 {
            out = modp(out as i128 * a as i128);
        }
        a = modp(a as i128 * a as i128);
        n >>= 1;
    }
    out
}

fn rank_mod(mut matrix: Vec<Vec<i64>>) -> usize {
    if matrix.is_empty() {
        return 0;
    }
    let rows = matrix.len();
    let cols = matrix[0].len();
    let mut pivot_row = 0;
    for col in 0..cols {
        let Some(pivot) = (pivot_row..rows).find(|&row| matrix[row][col] != 0) else {
            continue;
        };
        matrix.swap(pivot_row, pivot);
        let inverse = pow_mod(matrix[pivot_row][col], PRIME - 2);
        for entry in &mut matrix[pivot_row] {
            *entry = modp(*entry as i128 * inverse as i128);
        }
        for row in 0..rows {
            if row == pivot_row || matrix[row][col] == 0 {
                continue;
            }
            let coefficient = matrix[row][col];
            for j in col..cols {
                matrix[row][j] =
                    modp(matrix[row][j] as i128 - coefficient as i128 * matrix[pivot_row][j] as i128);
            }
        }
        pivot_row += 1;
        if pivot_row == rows {
            break;
        }
    }
    pivot_row
}

fn subsets(size: usize) -> Vec<Vec<usize>> {
    (0..(1usize << 4))
        .filter(|mask| mask.count_ones() as usize == size)
        .map(|mask| (0..4).filter(|i| mask & (1 << i) != 0).collect())
        .collect()
}

fn wedge_one_matrix(degree: usize) -> Vec<Vec<i64>> {
    let source = subsets(degree);
    let target = subsets(degree + 1);
    let target_index: BTreeMap<Vec<usize>, usize> =
        target.into_iter().enumerate().map(|(i, s)| (s, i)).collect();
    let mut matrix = vec![vec![0; source.len()]; target_index.len()];
    for (column, subset) in source.iter().enumerate() {
        for added in 0..4 {
            if subset.contains(&added) {
                continue;
            }
            let sign = if subset.iter().filter(|&&x| x < added).count() % 2 == 0 {
                1
            } else {
                -1
            };
            let mut image = subset.clone();
            image.push(added);
            image.sort_unstable();
            matrix[target_index[&image]][column] = modp(sign);
        }
    }
    matrix
}

fn multiply(a: &[Vec<i64>], b: &[Vec<i64>]) -> Vec<Vec<i64>> {
    if a.is_empty() || b.is_empty() {
        return Vec::new();
    }
    let mut out = vec![vec![0; b[0].len()]; a.len()];
    for i in 0..a.len() {
        for k in 0..b.len() {
            for j in 0..b[0].len() {
                out[i][j] = modp(out[i][j] as i128 + a[i][k] as i128 * b[k][j] as i128);
            }
        }
    }
    out
}

fn main() {
    let partner = std::env::args().nth(1).as_deref() == Some("partner");
    // Rows are gradients of (rho, q, U_minus, U_plus) in (rho, q, p, A).
    let jacobian = if partner {
        // Gradients of (rho, q, V_minus, V_plus) in (rho, q, p, B).
        vec![
            vec![1, 0, 0, 0],
            vec![0, 1, 0, 0],
            vec![0, 0, 1, -1],
            vec![0, 0, 1, 1],
        ]
    } else {
        vec![
            vec![1, 0, 0, 0],
            vec![0, 1, 0, 0],
            vec![0, 1, 3, -2],
            vec![0, 1, 3, 2],
        ]
    };
    let jacobian_rank = rank_mod(jacobian);
    let jacobian_determinant = if partner { 2 } else { 12 };

    let differentials: Vec<_> = (0..4).map(wedge_one_matrix).collect();
    let ranks: Vec<_> = differentials.iter().cloned().map(rank_mod).collect();
    let square_zero: Vec<_> = (0..3)
        .map(|degree| {
            multiply(&differentials[degree + 1], &differentials[degree])
                .iter()
                .flatten()
                .all(|entry| *entry == 0)
        })
        .collect();
    let dimensions = [1usize, 4, 6, 4, 1];
    let homology: Vec<_> = (0..5)
        .map(|degree| {
            let incoming = if degree == 0 { 0 } else { ranks[degree - 1] };
            let outgoing = if degree == 4 { 0 } else { ranks[degree] };
            dimensions[degree] - incoming - outgoing
        })
        .collect();

    assert_eq!(jacobian_rank, 4);
    assert_eq!(ranks, vec![1, 3, 3, 1]);
    assert!(square_zero.iter().all(|value| *value));
    assert_eq!(homology, vec![0, 0, 0, 0, 0]);

    println!("schema=marici.benincasa.rank12_rational_tangency_support_cube.v1");
    println!(
        "factor_order={}",
        if partner {
            "(rho,q,V_minus,V_plus)"
        } else {
            "(rho,q,U_minus,U_plus)"
        }
    );
    if partner {
        println!("V_minus=p-B");
        println!("V_plus=p+B");
    } else {
        println!("U_minus=3*p+q-2*A");
        println!("U_plus=3*p+q+2*A");
    }
    println!("jacobian_determinant={jacobian_determinant}");
    println!("jacobian_rank={jacobian_rank}");
    println!("dimensions={dimensions:?}");
    println!("differential_ranks={ranks:?}");
    println!("square_zero={square_zero:?}");
    println!("homology={homology:?}");
}
