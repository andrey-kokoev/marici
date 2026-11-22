//! rustc -O ramsey_reservoir_descent.rs -o descent; descent < pauli-realization-catalogues/r37_22.g6 > ramsey_reservoir_descent.tsv
mod ramsey_patch_glue;
use std::collections::HashSet;
use std::io::{self, BufRead};
fn verts(mut m: u32) -> impl Iterator<Item = u32> {
    std::iter::from_fn(move || {
        if m == 0 {
            None
        } else {
            let b = m & m.wrapping_neg();
            m ^= b;
            Some(b)
        }
    })
}
fn adj(h: &[u32], b: u32) -> u32 {
    h[b.trailing_zeros() as usize]
}
fn ind(h: &[u32], s: u32) -> bool {
    verts(s).all(|v| adj(h, v) & s == 0)
}
fn feasible(h: &[u32], a: u32, b: u32) -> bool {
    if verts(b).any(|v| b & !(v | adj(h, v)) != 0) {
        return false;
    }
    let v = a ^ b;
    if v.count_ones() > 6 {
        return false;
    }
    let mut pool = HashSet::new();
    let mut s = v;
    loop {
        if s.count_ones() <= 2 && ind(h, s) {
            let u = s | b;
            let ok = verts(u).all(|x| {
                let y = u & !(x | adj(h, x));
                verts(y).all(|z| y & !(z | adj(h, z)) == 0)
            });
            if ok {
                pool.insert(s);
            }
        }
        if s == 0 {
            break;
        }
        s = (s - 1) & v
    }
    pool.iter().any(|&s| {
        pool.iter()
            .any(|&t| s & t == 0 && pool.contains(&(v ^ s ^ t)))
    })
}
fn main() {
    println!("record\tmatched\tpass_four\tpass_triple\tpair\tarc\tcommon\tplus_pairs\tplus_singles\tfull\tforbidden_fours");
    for (idx, l) in io::stdin().lock().lines().enumerate() {
        let l = l.unwrap();
        let g = l.as_bytes();
        let n = (g[0] - 63) as usize;
        assert_eq!(n, 22);
        let f = (1 << n) - 1;
        let mut h = vec![0; n];
        let mut e = vec![];
        for j in 0..n {
            for i in 0..j {
                let k = j * (j - 1) / 2 + i;
                if ((g[1 + k / 6] - 63) >> (5 - k % 6)) & 1 == 1 {
                    h[i] |= 1 << j;
                    h[j] |= 1 << i;
                    e.push(1 << i | 1 << j);
                }
            }
        }
        let mut matched = HashSet::new();
        for (i, &x) in e.iter().enumerate() {
            for (j, &y) in e[..i].iter().enumerate() {
                if x & y != 0 {
                    continue;
                }
                for &z in &e[..j] {
                    if z & (x | y) != 0 {
                        continue;
                    }
                    let s = x | y | z;
                    for v in verts(f ^ s) {
                        matched.insert(s | v);
                    }
                }
            }
        }
        let mut ban = vec![false; 1 << n];
        let mut triples = vec![];
        let mut nf = 0;
        for q in 0u32..1 << n {
            let k = q.count_ones();
            if !(k == 3 || k == 4) || !ind(&h, q) {
                continue;
            }
            let a = f & !verts(q).fold(q, |u, b| u | adj(&h, b));
            if k == 4 && a.count_ones() >= 4 {
                ban[q as usize] = true;
                nf += 1
            }
            if k == 3 {
                triples.push((q, a));
            }
        }
        // Upward closure on seven-sets: spread forbidden fours only to exact size seven.
        let mut kill = HashSet::new();
        for (i, &b) in ban.iter().enumerate() {
            if !b {
                continue;
            }
            let q = i as u32;
            for x in verts(f ^ q) {
                for y in verts((f ^ q) & (x - 1)) {
                    for z in verts((f ^ q) & (y - 1)) {
                        kill.insert(q | x | y | z);
                    }
                }
            }
        }
        let good: Vec<_> = matched
            .iter()
            .filter(|s| !kill.contains(*s))
            .copied()
            .collect();
        let mut killed = HashSet::new();
        for (q, a) in triples {
            let mut b = a;
            loop {
                if b.count_ones() <= 2 && !feasible(&h, a, b) {
                    killed.insert((q, b));
                }
                if b == 0 {
                    break;
                }
                b = (b - 1) & a;
            }
        }
        let mut top = vec![];
        let mut five = vec![];
        for u in 0u32..1 << n {
            match u.count_ones() {
                5 if ind(&h, u) => five.push(u),
                6 if ind(&h, u) => top.push(u),
                _ => (),
            }
        }
        let mut pass = 0;
        let mut full = 0;
        let mut layers = [0; 3];
        let mut pairs = 0;
        let mut arcs = 0;
        let mut cache = ramsey_patch_glue::Cache::new();
        for &s in &good {
            let mut ok = true;
            'scan: for x in verts(s) {
                for y in verts(s & (x - 1) & !adj(&h, x)) {
                    for z in verts(s & (y - 1) & !(adj(&h, x) | adj(&h, y))) {
                        let q = x | y | z;
                        let b = s & !(q | adj(&h, x) | adj(&h, y) | adj(&h, z));
                        if killed.contains(&(q, b)) {
                            ok = false;
                            break 'scan;
                        }
                    }
                }
            }
            if ok {
                pass += 1;
                let (p, a) = ramsey_patch_glue::test(&h, s, f, &mut cache);
                pairs += p as usize;
                arcs += a as usize;
                if a {
                    for threshold in (1..=3).rev() {
                        let pool: HashSet<_> = five
                            .iter()
                            .filter(|&&t| {
                                s & t == 0
                                    && !top.iter().any(|&u| {
                                        u & !(s | t) == 0 && (u & s).count_ones() >= threshold
                                    })
                            })
                            .copied()
                            .collect();
                        if !pool.iter().any(|&x| {
                            pool.iter()
                                .any(|&y| x < y && x & y == 0 && pool.contains(&(f ^ s ^ x ^ y)))
                        }) {
                            break;
                        }
                        layers[(3 - threshold) as usize] += 1;
                    }
                }
                let pool: HashSet<_> = five
                    .iter()
                    .filter(|&&t| s & t == 0 && !top.iter().any(|&u| u & !(s | t) == 0))
                    .copied()
                    .collect();
                if pool.iter().any(|&x| {
                    pool.iter()
                        .any(|&y| x < y && x & y == 0 && pool.contains(&(f ^ s ^ x ^ y)))
                }) {
                    assert!(a);
                    full += 1
                }
            }
        }
        println!(
            "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}",
            idx + 1,
            matched.len(),
            good.len(),
            pass,
            pairs,
            arcs,
            layers[0],
            layers[1],
            layers[2],
            full,
            nf
        );
    }
}
