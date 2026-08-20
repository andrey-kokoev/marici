//! Exact finite-field audit of the canonical spurious-kernel corner complex.
//!
//! The only source-free comparison between K_6,K_7,K_8 is induced by their
//! inclusions in the common six-master fiber.  This checker computes the
//! corresponding difference map at the triple flat [6,7,8].

type Mat = [[i64; 6]; 6];

fn mod_pow(mut a: i64, mut n: i64, p: i64) -> i64 {
    let mut out = 1;
    while n > 0 {
        if n & 1 == 1 { out = out * a % p; }
        a = a * a % p;
        n >>= 1;
    }
    out
}

fn rref(mut a: Vec<Vec<i64>>, p: i64) -> (Vec<Vec<i64>>, Vec<usize>) {
    for row in &mut a {
        for x in row { *x = x.rem_euclid(p); }
    }
    let width = a.first().map_or(0, Vec::len);
    let mut pivot_cols = Vec::new();
    let mut pivot_row = 0;
    for col in 0..width {
        let Some(found) = (pivot_row..a.len()).find(|r| a[*r][col] != 0) else {
            continue;
        };
        a.swap(pivot_row, found);
        let inv = mod_pow(a[pivot_row][col], p - 2, p);
        for x in &mut a[pivot_row][col..] { *x = *x * inv % p; }
        for row in 0..a.len() {
            if row == pivot_row { continue; }
            let factor = a[row][col];
            for j in col..width {
                a[row][j] = (a[row][j] - factor * a[pivot_row][j]).rem_euclid(p);
            }
        }
        pivot_cols.push(col);
        pivot_row += 1;
        if pivot_row == a.len() { break; }
    }
    (a, pivot_cols)
}

fn rank(a: Vec<Vec<i64>>, p: i64) -> usize { rref(a, p).1.len() }

/// Return a basis of column vectors for the right kernel.
fn dynamic_kernel_basis(a: Vec<Vec<i64>>, p: i64) -> Vec<Vec<i64>> {
    let width = a.first().map_or(0, Vec::len);
    let (reduced, pivots) = rref(a, p);
    let free: Vec<usize> = (0..width).filter(|j| !pivots.contains(j)).collect();
    free.into_iter().map(|free_col| {
        let mut vector = vec![0; width];
        vector[free_col] = 1;
        for (row, pivot_col) in pivots.iter().enumerate() {
            vector[*pivot_col] = (-reduced[row][free_col]).rem_euclid(p);
        }
        vector
    }).collect()
}

fn kernel_basis(a: &Mat, p: i64) -> Vec<Vec<i64>> {
    dynamic_kernel_basis(a.iter().map(|row| row.to_vec()).collect(), p)
}

fn stacked_rank(matrices: &[&Mat], p: i64) -> usize {
    rank(
        matrices.iter().flat_map(|m| m.iter().map(|row| row.to_vec())).collect(),
        p,
    )
}

fn audit(p: i64) -> (Vec<usize>, i64) {
    // Four times the published M_6,M_7,M_8 matrices.
    let m6: Mat = [
        [0,0,0,0,0,0],[-2,4,0,0,0,0],[0,0,0,0,0,0],
        [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,-1,2,-2,4],
    ];
    let m7: Mat = [
        [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],
        [0,0,0,0,0,0],[0,0,0,0,0,0],[0,-2,1,-2,-2,4],
    ];
    let m8: Mat = [
        [0,0,0,0,0,0],[0,0,0,0,0,0],[-2,0,4,-8,0,0],
        [1,0,-2,4,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],
    ];
    let matrices = [&m6, &m7, &m8];
    let kernels: Vec<Vec<Vec<i64>>> = matrices.iter().map(|m| kernel_basis(m, p)).collect();
    let kernel_dims: Vec<usize> = kernels.iter().map(Vec::len).collect();

    let pair_intersections = vec![
        6 - stacked_rank(&[&m6, &m7], p),
        6 - stacked_rank(&[&m6, &m8], p),
        6 - stacked_rank(&[&m7, &m8], p),
    ];
    let common_intersection = 6 - stacked_rank(&[&m6, &m7, &m8], p);

    // d(v6,v7,v8)=(v6-v7,v7-v8) in V+V.
    let source_dim: usize = kernel_dims.iter().sum();
    let mut d = vec![vec![0; source_dim]; 12];
    let mut offset = 0;
    for (s, basis) in kernels.iter().enumerate() {
        for vector in basis {
            for coordinate in 0..6 {
                match s {
                    0 => d[coordinate][offset] = vector[coordinate],
                    1 => {
                        d[coordinate][offset] = (-vector[coordinate]).rem_euclid(p);
                        d[6 + coordinate][offset] = vector[coordinate];
                    }
                    2 => d[6 + coordinate][offset] = (-vector[coordinate]).rem_euclid(p),
                    _ => unreachable!(),
                }
            }
            offset += 1;
        }
    }
    let differential_rank = rank(d.clone(), p);
    let h0 = source_dim - differential_rank;
    let ambient_cokernel = 12 - differential_rank;

    let mut result = kernel_dims;
    result.extend(pair_intersections);
    result.extend([common_intersection, differential_rank, h0, ambient_cokernel]);

    // Compute the induced eigenvalue directly on coker(d), using its dual
    // ker(d^T). This avoids choosing a noncanonical representative quotient.
    let d_transpose: Vec<Vec<i64>> = (0..source_dim)
        .map(|column| (0..12).map(|row| d[row][column]).collect())
        .collect();
    let cokernel_dual = dynamic_kernel_basis(d_transpose, p);
    assert_eq!(cokernel_dual.len(), 1);
    let functional = &cokernel_dual[0];
    let total: Mat = core::array::from_fn(|i| {
        core::array::from_fn(|j| (m6[i][j] + m7[i][j] + m8[i][j]).rem_euclid(p))
    });
    let acted_dual: Vec<i64> = (0..12)
        .map(|column| {
            let block = column / 6;
            let local_column = column % 6;
            (0..6)
                .map(|local_row| functional[block * 6 + local_row] * total[local_row][local_column])
                .sum::<i64>()
                .rem_euclid(p)
        })
        .collect();
    let pivot = functional.iter().position(|x| *x != 0).unwrap();
    let eigenvalue = acted_dual[pivot] * mod_pow(functional[pivot], p - 2, p) % p;
    assert!(acted_dual.iter().zip(functional).all(|(a, f)| {
        (*a - eigenvalue * *f).rem_euclid(p) == 0
    }));
    (result, eigenvalue)
}

fn main() {
    let first = audit(32003);
    let second = audit(32009);
    assert_eq!(first.0, second.0);
    assert_eq!(first.1, second.1);
    assert_eq!(&first.0[0..3], &[4,5,5]);
    assert_eq!(first.0[6], 3);
    assert_eq!(first.0[8], 3);
    println!(
        "kernel_dims={:?} pair_intersections={:?} common_intersection={} \
         difference_rank={} h0={} h1={} triple_residue_on_h1={}",
        &first.0[0..3], &first.0[3..6], first.0[6], first.0[7],
        first.0[8], first.0[9], first.1,
    );
}
