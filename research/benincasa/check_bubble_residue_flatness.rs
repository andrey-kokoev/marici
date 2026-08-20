//! Exact Kohno-flatness and regularity audit for the published bubble residues.

use std::collections::{BTreeMap, BTreeSet};

type Mat = [[i64; 6]; 6];

fn add(a: &Mat, b: &Mat) -> Mat {
    let mut out = [[0; 6]; 6];
    for i in 0..6 { for j in 0..6 { out[i][j] = a[i][j] + b[i][j]; } }
    out
}

fn mul(a: &Mat, b: &Mat) -> Mat {
    let mut out = [[0; 6]; 6];
    for i in 0..6 { for j in 0..6 { for k in 0..6 { out[i][j] += a[i][k] * b[k][j]; } } }
    out
}

fn comm(a: &Mat, b: &Mat) -> Mat {
    let ab = mul(a, b); let ba = mul(b, a);
    let mut out = [[0; 6]; 6];
    for i in 0..6 { for j in 0..6 { out[i][j] = ab[i][j] - ba[i][j]; } }
    out
}

fn zero(a: &Mat) -> bool { a.iter().flatten().all(|x| *x == 0) }

fn gcd(a: i64, b: i64) -> i64 { if b == 0 { a.abs() } else { gcd(b, a % b) } }

fn canonical(mut v: [i64; 3]) -> [i64; 3] {
    let g = gcd(gcd(v[0], v[1]), v[2]);
    if g > 1 { for x in &mut v { *x /= g; } }
    if v.iter().find(|x| **x != 0).is_some_and(|x| *x < 0) { for x in &mut v { *x = -*x; } }
    v
}

fn cross(a: [i64; 3], b: [i64; 3]) -> [i64; 3] {
    canonical([a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]])
}

fn dot(a: [i64; 3], b: [i64; 3]) -> i64 { a[0]*b[0]+a[1]*b[1]+a[2]*b[2] }

fn rank_mod(rows: &[Vec<i64>], p: i64) -> usize {
    let mut a: Vec<Vec<i64>> = rows.iter().map(|r| r.iter().map(|x| x.rem_euclid(p)).collect()).collect();
    let mut rank = 0;
    let width = a.first().map_or(0, Vec::len);
    for col in 0..width {
        let Some(pivot) = (rank..a.len()).find(|r| a[*r][col] != 0) else { continue };
        a.swap(rank, pivot);
        let inv = mod_pow(a[rank][col], p-2, p);
        for j in col..width { a[rank][j] = a[rank][j] * inv % p; }
        for r in 0..a.len() {
            if r == rank { continue; }
            let f = a[r][col];
            for j in col..width { a[r][j] = (a[r][j] - f*a[rank][j]).rem_euclid(p); }
        }
        rank += 1;
        if rank == a.len() { break; }
    }
    rank
}

fn rows(matrix: &Mat) -> Vec<Vec<i64>> { matrix.iter().map(|r| r.to_vec()).collect() }

fn preserves_kernel(constraint: &Mat, action: &Mat, p: i64) -> bool {
    let base = rows(constraint);
    let mut augmented = base.clone();
    augmented.extend(rows(&mul(constraint, action)));
    rank_mod(&base, p) == rank_mod(&augmented, p)
}

fn mod_pow(mut a: i64, mut n: i64, p: i64) -> i64 {
    let mut out = 1;
    while n > 0 { if n & 1 == 1 { out = out*a % p; } a = a*a % p; n >>= 1; }
    out
}

fn main() {
    // Four times the source matrices M_1,...,M_8, in source basis order.
    let m: [Mat; 8] = [
        [[16,0,0,0,0,0],[0,8,0,0,0,0],[0,0,8,0,0,0],[0,0,0,0,0,0],[0,0,0,0,8,0],[0,0,0,0,0,0]],
        [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[-2,0,0,8,0,0],[0,0,0,0,8,0],[0,0,0,0,0,0]],
        [[0,0,0,0,0,0],[2,4,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,1,2,2,4]],
        [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,2,-1,-2,2,4]],
        [[0,0,0,0,0,0],[0,0,0,0,0,0],[2,0,4,8,0,0],[1,0,2,4,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
        [[0,0,0,0,0,0],[-2,4,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,-1,2,-2,4]],
        [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,-2,1,-2,-2,4]],
        [[0,0,0,0,0,0],[0,0,0,0,0,0],[-2,0,4,-8,0,0],[1,0,-2,4,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
    ];
    let normals = [[0,0,1],[1,1,0],[1,0,1],[0,1,1],[1,1,2],[1,0,-1],[0,1,-1],[1,1,-2]];

    let mut directions = BTreeSet::new();
    for i in 0..8 { for j in i+1..8 { directions.insert(cross(normals[i], normals[j])); } }
    directions.remove(&[0,0,0]);
    let mut flats: BTreeMap<[i64;3], Vec<usize>> = BTreeMap::new();
    for d in directions { flats.insert(d, (0..8).filter(|i| dot(normals[*i], d) == 0).collect()); }
    for indices in flats.values() {
        let sum = indices.iter().fold([[0;6];6], |acc, i| add(&acc, &m[*i]));
        for i in indices { assert!(zero(&comm(&m[*i], &sum))); }
    }

    let ranks: Vec<usize> = m.iter().map(|matrix| rank_mod(&matrix.iter().map(|r| r.to_vec()).collect::<Vec<_>>(), 32003)).collect();
    let ranks_replication: Vec<usize> = m.iter().map(|matrix| rank_mod(&matrix.iter().map(|r| r.to_vec()).collect::<Vec<_>>(), 32009)).collect();
    assert_eq!(ranks, ranks_replication);
    let spurious_rows: Vec<Vec<i64>> = [5usize,6,7].iter().flat_map(|i| m[*i].iter().map(|r| r.to_vec())).collect();
    let common_kernel_dimension = 6-rank_mod(&spurious_rows, 32003);
    assert_eq!(common_kernel_dimension, 6-rank_mod(&spurious_rows, 32009));
    let mut individual_failures = Vec::new();
    let mut flat_sum_failures = Vec::new();
    let spurious_flats: Vec<Vec<usize>> = flats.values().filter(|indices| indices.iter().any(|i| *i >= 5)).map(|indices| indices.iter().map(|i| i+1).collect()).collect();
    for s in 5..8 {
        for j in 0..5 {
            let preserves = preserves_kernel(&m[s], &m[j], 32003);
            assert_eq!(preserves, preserves_kernel(&m[s], &m[j], 32009));
            if !preserves { individual_failures.push((s+1,j+1)); }
        }
        for indices in flats.values().filter(|indices| indices.contains(&s)) {
            let sum_other = indices.iter().filter(|i| **i != s).fold([[0;6];6], |acc, i| add(&acc, &m[*i]));
            let preserves = preserves_kernel(&m[s], &sum_other, 32003);
            assert_eq!(preserves, preserves_kernel(&m[s], &sum_other, 32009));
            if !preserves { flat_sum_failures.push((s+1,indices.iter().map(|i| i+1).collect::<Vec<_>>())); }
        }
    }
    println!("rank_two_flats={} kohno_failures=0 residue_ranks={:?} spurious_common_kernel_dim={} individual_kernel_failures={:?} flat_sum_kernel_failures={:?} spurious_flats={:?}", flats.len(), ranks, common_kernel_dimension, individual_failures, flat_sum_failures, spurious_flats);
}
