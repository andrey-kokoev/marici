//! Construct balanced three-port extensions on unseen order-27 cores. Only sufficient positive certificates: R has a 4-matching; every R+S is tiled by C5+C5+C5 or T8+C5+edge. No maximum row or SAT solver. Generate T8 via a four-cycle and two internally disjoint three-edge paths on its diagonals.
use std::{
    collections::{HashMap, HashSet},
    io::{self, BufRead},
};
fn bits(mut m: u32) -> impl Iterator<Item = u32> {
    std::iter::from_fn(move || {
        if m == 0 {
            None
        } else {
            let x = m & m.wrapping_neg();
            m ^= x;
            Some(x)
        }
    })
}
fn paths(h: &[u32], a: usize, b: usize, w: u32) -> Vec<u32> {
    let mut p = vec![];
    for x in bits(h[a] & w) {
        for y in bits(h[b] & w & h[x.trailing_zeros() as usize]) {
            p.push(x | y)
        }
    }
    p
}
fn audit(g: &[u8]) -> Option<(u32, [u32; 3], Vec<Vec<u32>>)> {
    let n = (g[0] - 63) as usize;
    assert_eq!(n, 27);
    let f = (1 << n) - 1;
    let mut h = vec![0; n];
    let mut edges = vec![];
    for j in 0..n {
        for i in 0..j {
            let k = j * (j - 1) / 2 + i;
            if (g[1 + k / 6] - 63) >> (5 - k % 6) & 1 == 1 {
                h[i] |= 1 << j;
                h[j] |= 1 << i;
                edges.push(1 << i | 1 << j)
            }
        }
    }
    let mut eight = HashSet::new();
    let mut five = HashSet::new();
    for a in 0..n {
        for b in a + 1..n {
            let c = h[a] & h[b];
            for x in bits(c) {
                for p in paths(&h, a, b, f ^ x) {
                    five.insert((1 << a) | (1 << b) | x | p);
                }
                for y in bits(c & (x - 1)) {
                    let base = (1 << a) | (1 << b) | x | y;
                    for p in paths(&h, a, b, f ^ base) {
                        for q in paths(
                            &h,
                            x.trailing_zeros() as usize,
                            y.trailing_zeros() as usize,
                            f ^ (base | p),
                        ) {
                            eight.insert(base | p | q);
                        }
                    }
                }
            }
        }
    }
    let six: Vec<_> = {
        fn gen(h: &[u32], v: u32, s: u32, d: u8, o: &mut Vec<u32>) {
            if d == 0 {
                o.push(s);
                return;
            }
            for x in bits(v) {
                gen(
                    h,
                    (v & (x - 1)) & !h[x.trailing_zeros() as usize],
                    s | x,
                    d - 1,
                    o,
                )
            }
        }
        let mut o = vec![];
        gen(&h, f, 0, 6, &mut o);
        o
    };
    let mut cache = HashMap::new();
    let use_eight = !std::env::args().any(|a| a == "--pentagons-only");
    let mut cert = |w: u32| -> Vec<u32> {
        cache
            .entry(w)
            .or_insert_with(|| {
                let p: Vec<_> = five.iter().filter(|&&s| s & !w == 0).copied().collect();
                for &a in &p {
                    for &b in &p {
                        if a < b && a & b == 0 && five.contains(&(w ^ a ^ b)) {
                            return vec![a, b, w ^ a ^ b];
                        }
                    }
                    for &e in &edges {
                        if use_eight && e & !(w ^ a) == 0 && eight.contains(&(w ^ a ^ e)) {
                            return vec![a, e, w ^ a ^ e];
                        }
                    }
                }
                vec![]
            })
            .clone()
    };
    let mut ne = vec![vec![]; six.len()];
    for i in 0..six.len() {
        for j in 0..i {
            if six[i] & six[j] == 0 && !cert(f ^ six[i] ^ six[j]).is_empty() {
                ne[i].push(j)
            }
        }
    }
    fn mat(h: &[u32], r: u32, d: u8) -> bool {
        d == 0
            || bits(r).any(|x| {
                bits(h[x.trailing_zeros() as usize] & r & (x - 1)).any(|y| mat(h, r ^ x ^ y, d - 1))
            })
    }
    for i in 0..six.len() {
        for &j in &ne[i] {
            for &k in &ne[j] {
                if ne[i].binary_search(&k).is_ok() {
                    let s = [six[i], six[j], six[k]];
                    let r = f ^ (s[0] | s[1] | s[2]);
                    if mat(&h, r, 4) {
                        return Some((r, s, s.iter().map(|u| cert(r | u)).collect()));
                    }
                }
            }
        }
    }
    None
}
fn main() {
    for (i, l) in io::stdin().lock().lines().enumerate() {
        println!("{}\t{:?}", i + 1, audit(l.unwrap().as_bytes()));
    }
}
