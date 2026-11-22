//! Enumerate unordered balanced colourings first; index counts by matched leftover, not by coloring. No larger patch or forbidden-four prefilter. A dominated independent pair is deficient iff both are private neighbours of the same support vertex (automatically nonadjacent).
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
fn main() {
    println!("record\tmatched\tbalanced\tdominated\tpair\ttriple\tfull");
    for (idx, l) in io::stdin().lock().lines().enumerate() {
        let line = l.unwrap();
        let g = line.as_bytes();
        let n = (g[0] - 63) as usize;
        assert_eq!(n, 22);
        let f = (1 << n) - 1;
        let mut h = vec![0; n];
        let mut edges = vec![];
        for j in 0..n {
            for i in 0..j {
                let k = j * (j - 1) / 2 + i;
                if ((g[1 + k / 6] - 63) >> (5 - k % 6)) & 1 == 1 {
                    h[i] |= 1 << j;
                    h[j] |= 1 << i;
                    edges.push(1 << i | 1 << j)
                }
            }
        }
        let mut stage = vec![0u8; 1 << n];
        for (i, &x) in edges.iter().enumerate() {
            for (j, &y) in edges[..i].iter().enumerate() {
                if x & y != 0 {
                    continue;
                }
                for &z in &edges[..j] {
                    if z & (x | y) != 0 {
                        continue;
                    }
                    let s = x | y | z;
                    for v in verts(f ^ s) {
                        stage[(s | v) as usize] = 1
                    }
                }
            }
        }
        let mut p = vec![];
        let mut six = vec![];
        for s in 0u32..1 << n {
            let k = s.count_ones();
            if (k == 5 || k == 6) && verts(s).all(|v| s & h[v.trailing_zeros() as usize] == 0) {
                if k == 5 {
                    p.push(s)
                } else {
                    six.push(s)
                }
            }
        }
        let dom: Vec<_> = p
            .iter()
            .map(|&s| verts(s).fold(0, |u, v| u | h[v.trailing_zeros() as usize]))
            .collect();
        let privs: Vec<Vec<u32>> = p
            .iter()
            .map(|&s| {
                verts(s)
                    .map(|b| {
                        verts(f ^ s)
                            .filter(|&v| h[v.trailing_zeros() as usize] & s == b)
                            .sum::<u32>()
                    })
                    .filter(|x| x.count_ones() > 1)
                    .collect()
            })
            .collect();
        let deficits: Vec<[Vec<u32>; 2]> = p
            .iter()
            .map(|&s| {
                let mut a = [vec![], vec![]];
                for &t in &six {
                    let j = t & !s;
                    if j.count_ones() == 3 || j.count_ones() == 4 {
                        a[j.count_ones() as usize - 3].push(j)
                    }
                }
                a
            })
            .collect();
        let dis: Vec<Vec<usize>> = p
            .iter()
            .enumerate()
            .map(|(i, &s)| (i + 1..p.len()).filter(|&j| s & p[j] == 0).collect())
            .collect();
        for i in 0..p.len() {
            for &j in &dis[i] {
                let xy = p[i] | p[j];
                for &k in &dis[j] {
                    if xy & p[k] != 0 {
                        continue;
                    }
                    let r = f ^ (xy | p[k]);
                    let slot = &mut stage[r as usize];
                    if *slot == 0 {
                        continue;
                    }
                    let mut l = 2;
                    if r & !(dom[i] & dom[j] & dom[k]) == 0 {
                        l = 3;
                        if [i, j, k]
                            .iter()
                            .all(|&t| privs[t].iter().all(|&b| (b & r).count_ones() <= 1))
                        {
                            l = 4;
                            for d in 0..2 {
                                if [i, j, k]
                                    .iter()
                                    .any(|&t| deficits[t][d].iter().any(|&b| b & !r == 0))
                                {
                                    break;
                                }
                                l += 1
                            }
                        }
                    }
                    if l == 5 {
                        for t in [i, j, k] {
                            for &q in &deficits[t][1] {
                                if q & !r != 0 {
                                    continue;
                                }
                                let mut deg: Vec<_> = verts(p[t])
                                    .map(|v| (h[v.trailing_zeros() as usize] & q).count_ones())
                                    .filter(|&d| d > 0)
                                    .collect();
                                deg.sort();
                                assert!(deg.len() == 3 && deg[0] >= 2);
                                eprintln!(
                                    "{}\t{}\t{}\t{}\t{}\t{}{}{}",
                                    idx + 1,
                                    r,
                                    p[i] | 0,
                                    p[t],
                                    q,
                                    deg[0],
                                    deg[1],
                                    deg[2]
                                );
                            }
                        }
                    }
                    *slot = (*slot).max(l)
                }
            }
        }
        let mut counts = [0; 6];
        for a in stage {
            for i in 0..a as usize {
                counts[i] += 1
            }
        }
        print!("{}", idx + 1);
        for c in counts {
            print!("\t{}", c)
        }
        println!();
    }
}
